# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OrderPreparation(models.Model):
    _name = 'order.preparation'
    _description = 'order preparation'

    state = fields.Selection(
        [('draft', 'draft'), ('preparation', 'preparation'), ('production', 'production'),
         ('done', 'done'), ('cancel', 'cancel')],
        string='state',
        default='draft'
    )
    name = fields.Char(
        'Order',
        default='/'
    )
    user_id = fields.Many2one(
        'res.users',
        string='User',
        required=True,
        default=lambda self: self.env.user.id
    )
    date_from = fields.Datetime(
        string='From',
    )
    date_to = fields.Datetime(
        string='to',
    )
    move_ids = fields.Many2many(
        comodel_name='stock.move',
        relation='preparation_from_move_rel',
        column1='preparation_id',
        column2='move_id',
        string='Moves',
        copy=False
    )
    picking_ids = fields.Many2many(
        'stock.picking',
        string='Pickings',
        copy=True
    )
    line_ids = fields.One2many(
        'order.preparation.line',
        'preparation_id',
        string='Consolidated',
        copy=False
    )
    production_ids = fields.Many2many(
        'mrp.production',
        string='production',
    )
    picking_batch_id = fields.Many2one(
        'stock.picking.batch',
        string='picking batch',
    )

    def get_pickings(self):
        self.ensure_one()
        picking_ids = self.env['stock.picking'].search(
            [('create_date', '>=', self.date_from),
             ('create_date', '<=', self.date_to),
             ('state', 'not in', ['draft', 'done']),
             ('picking_type_id.code', '=', 'outgoing')]
        )
        self.picking_ids = [(6, 0, picking_ids.ids)]

    def recompute_moves(self):
        self.ensure_one()
        move_ids = []
        if not len(self.picking_ids):
            raise ValidationError(_('Preparation require pickings'))
        for picking_id in self.picking_ids:
            move_ids += [x.id for x in picking_id.move_lines if x.state not in ['done', 'cancel']]
        if not len(move_ids):
            raise ValidationError(_('Preparation require product stock moves'))

        self.move_ids = [(6, 0, move_ids)]

    def action_preparation(self):
        self.ensure_one()
        self.recompute_moves()

        new_moves = {}

        for move in self.move_ids:
            if move.product_id.type != 'product':
                continue
            if move.product_id.id not in new_moves:
                new_moves[move.product_id.id] = {
                    'total': 0,
                    'qty_available': move.product_id.qty_available,
                    'produce_qty': 0,
                    'disp_qty': 0,
                    'move_ids': []
                }

            new_moves[move.product_id.id]['total'] += move.product_uom_qty
            new_moves[move.product_id.id]['uom_id'] = move.product_id.uom_id.id
            new_moves[move.product_id.id]['move_ids'].append((4, move.id))

        for product_id in new_moves.keys():
            if new_moves[product_id]['qty_available'] >= new_moves[product_id]['total']:
                disp_qty = new_moves[product_id]['total']
                produce_qty = 0
            else:
                disp_qty = new_moves[product_id]['qty_available']
                produce_qty = new_moves[product_id][
                    'total'] - new_moves[product_id]['qty_available']

            self.env['order.preparation.line'].create({
                'product_id': product_id,
                'product_qty': new_moves[product_id]['total'],
                'qty_available': new_moves[product_id]['qty_available'],
                'produce_qty': produce_qty,
                'disp_qty': disp_qty,
                'preparation_id': self.id,
                'move_ids': new_moves[product_id]['move_ids']
            })

        vals = {}
        vals['name'] = self.env[
            'ir.sequence'].next_by_code('order.preparation')
        vals['state'] = 'preparation'
        picking_batch = self.env['stock.picking.batch'].create(
            {'user_id': self.user_id.id,
             'picking_ids': [(6, 0, self.picking_ids.ids)]}
        )
        vals['picking_batch_id'] = picking_batch.id

        self.write(vals)

    def action_production(self):
        self.ensure_one()
        production_ids = []
        for line in self.line_ids:
            if line.line.produce_qty > line.product_id.potential_qty:
                raise ValidationError('No puede producir mas del potencial')

            if line.produce_qty > 0 and len(line.product_id.bom_id):
                production = self.env['mrp.production'].create({
                    'product_id': line.product_id.id,
                    'product_qty': line.produce_qty,
                    'product_uom_id': line.product_id.uom_id.id,
                    'bom_id': line.product_id.bom_id.id,
                    'user_id': self.user_id.id
                })
                production.onchange_product_id()
                production._onchange_bom_id()
                production.product_qty = line.produce_qty
                production._onchange_move_raw()

                production.action_confirm()
                production_ids.append(production.id)

        vals = {}
        vals['production_ids'] = [(6, 0, production_ids)]
        vals['state'] = 'production'
        self.write(vals)


class OrderPreparationLine(models.Model):
    _name = 'order.preparation.line'
    _description = 'order preparation line'
    _order = "sequence asc"

    sequence = fields.Integer(
        string='Sequence',
    )
    preparation_id = fields.Many2one(
        'order.preparation',
        string='Preparation',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    potential_qty = fields.Float(
        string='potencial',
        related='product_id.potential_qty',
        store=True,
    )
    location_id = fields.Many2one(
        'stock.location',
        string='Location',
    )
    product_qty = fields.Float(
        string='Qty',
    )
    move_ids = fields.Many2many(
        'stock.move',
        string='Moves',
    )
    moved_qty = fields.Float(
        string='moved qty',
        compute="_compute_moved_qty"
    )
    qty_available = fields.Float(
        string='available',
    )
    produce_qty = fields.Float(
        string='to produce',
    )
    disp_qty = fields.Float(
        string='Collect',
    )
    @api.onchange('produce_qty')
    def _onchange_produce_qty(self):
        if self.produce_qty > self.product_id.potential_qty:
            raise ValidationError('No puede producir mas del potencial')
    

    def _compute_moved_qty(self):
        for line in self:
            moved_qty = 0.0
            for move in line.move_ids:
                if move.state == 'done':
                    moved_qty += move.product_uom_qty
            line.moved_qty = moved_qty
