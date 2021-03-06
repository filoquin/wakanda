from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from math import floor

import logging
logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    wak_order = fields.Boolean(
        string='From Wakanda app',
    )
    show_promos = fields.Boolean(
        string='show promos',
    )
    promo_line_ids = fields.One2many(
        'sale.order.promo',
        'order_id',
        string='Promos',
    )

    @api.model
    def wkn_create(self, lines, coupon_code=False):

        order_line = []
        for line in lines:
            product = self.env['product.product'].browse(line['id'])
            order_line.append((0, 0, {'product_id': product.id, 'product_uom_qty': line['qty']}))
        order = {
            'user_id': self.env.user.id,
            'partner_id': self.env.user.partner_id.id,
            'pricelist_id': self.env.user.partner_id.property_product_pricelist.id,
            'wak_order': True,
            'order_line': order_line
        }
        order_id = self.create(order)
        order_id.checkTotal()
        #order_id.order_line.expand_pack_line()
        if coupon_code and len(coupon_code):
            res = self.wkn_apply_coupon(order_id, coupon_code)
            if 'not_found' in res:
                raise ValidationError(_('El codigo es incorrecto.'))
        order_id.sudo().get_promos()
        order_id.recompute_coupon_lines()

        return order_id.read(['show_promos', 'promo_line_ids'])

    @api.model
    def wkn_apply_coupon(self, order, coupon_code):
        error_status = {}
        program = self.env['sale.coupon.program'].search([('promo_code', '=', coupon_code)])
        if program:
            error_status = program._check_promo_code(order, coupon_code)
            if not error_status:
                if program.promo_applicability == 'on_next_order':
                    # Avoid creating the coupon if it already exist
                    if program.discount_line_product_id.id not in order.generated_coupon_ids.filtered(lambda coupon: coupon.state in ['new', 'reserved']).mapped('discount_line_product_id').ids:
                        coupon = order._create_reward_coupon(program)
                        return {
                            'generated_coupon': {
                                'reward': coupon.program_id.discount_line_product_id.name,
                                'code': coupon.code,
                            }
                        }
                else:  # The program is applied on this order
                    order._create_reward_line(program)
                    order.code_promo_program_id = program
        else:
            coupon = self.env['sale.coupon'].search([('code', '=', coupon_code)], limit=1)
            if coupon:
                error_status = coupon._check_coupon_code(order)
                if not error_status:
                    order._create_reward_line(coupon.program_id)
                    order.applied_coupon_ids += coupon
                    coupon.write({'state': 'used'})
            else:
                error_status = {'not_found': _('The code %s is invalid') % (coupon_code)}
        return error_status

    def compute_promos(self):
        self.get_promos()

    def read_promos(self):
        self.ensure_one()
        self.sudo().get_promos()
        return self.promo_line_ids.read(['promo_id', 'product_qty', 'product_id', 'discount'])

    def get_promos(self):
        self.promo_line_ids.unlink()
        self.ensure_one()
        promo_ids = self.env['wak.promo'].search([
            ('from_time', '<=', self.date_order),
            ('to_time', '>=', self.date_order),
        ])
        show_promos = False

        if len(promo_ids):
            for promo_id in promo_ids:
                used_qty = sum(
                    [x.product_uom_qty for x in self.order_line if x.promo_id.id == promo_id.id])
                qty = 0.0
                amount = 0.0
                gift_qty = 0
                for line in self.order_line:
                    if line.product_id.id in promo_id.required_product_ids.ids \
                            and not len(line.promo_id):
                        qty += line.product_uom_qty
                        amount += line.price_unit
                if promo_id.rule_type == 'qty_product' and qty >= promo_id.rule_qty:
                    gift_qty = promo_id.gift_qty - used_qty
                elif promo_id.rule_type == 'multiple_product' and qty >= promo_id.rule_qty:
                    gift_qty = promo_id.gift_qty * \
                        floor(qty / promo_id.rule_qty) - used_qty
                elif promo_id.rule_type == 'amount' and amount >= promo_id.rule_qty:
                    gift_qty = promo_id.gift_qty - used_qty
                if gift_qty > 0:
                    show_promos = True
                    for x in promo_id.gift_product_ids:
                        self.env['sale.order.promo'].create({
                            'promo_id': promo_id.id,
                            'order_id': self.id,
                            'product_id': x.id,
                            'product_qty': gift_qty,
                            'discount': promo_id.gift_discount,
                        })
        self.show_promos = show_promos

    def action_confirm(self):
        self.checkTotal()
        res = super().action_confirm()
        self.get_promos()
        return res

    def checkTotal(self):
        if self.env.user.has_group('wakanda_base.wak_group_revendedor') or self.env.user.id == 2:
            max_qty = self.env['ir.config_parameter'].sudo().get_param(
                'max_qty', default=20)
            max_amount = self.env['ir.config_parameter'].sudo().get_param(
                'max_amount', default=1)
            qty = 0
            for line in self.order_line:
                if line.product_id.pack_ok:# and line.product_id.pack_type == 'non_detailed'
                    for pack_line in line.product_id.pack_line_ids:
                        qty += pack_line.quantity * line.product_uom_qty

                else:
                    qty += line.product_uom_qty
            if qty < int(max_qty):
                raise ValidationError(_('La orden no tiene la cantidad minima de productos.'))

    def _get_wkn_delivery_methods(self):
        address = self.partner_shipping_id
        # searching on website_published will also search for available website
        # (_search method on computed field)
        return self.env['delivery.carrier'].sudo().search([('is_published', '=', True)]).available_carriers(address)

    def read_delivery_methods(self):
        carriers = []

        delivery_methods = self._get_wkn_delivery_methods()
        return delivery_methods.read(['display_name', 'amount'])
        for delivery_method in delivery_methods:
            vals = delivery_method.rate_shipment(self)
            if vals.get('success'):
                carrier_tmp = {}
                carrier_tmp['delivery_message'] = vals.get(
                    'warning_message', False)
                carrier_tmp['delivery_price'] = vals['price']
                carrier_tmp['display_price'] = vals['carrier_price']
                carrier_tmp['name'] = delivery_method.display_name
                carrier_tmp['id'] = delivery_method.id

        return carriers

    def wkn_delivery_confirm(self, carrier_id, delivery_price):
        self.ensure_one()

        carrier_id = self.env['delivery.carrier'].sudo().browse(carrier_id)
        self.sudo().set_delivery_line(carrier_id, delivery_price)
        self.sudo().write({
            'recompute_delivery_price': False,
            # 'delivery_message': self.delivery_message,
        })
        self.sudo().action_confirm()
        #self.sudo().picking_ids.action_pack_operation_auto_fill()
        logger.info('aca')
        return True


class SaleOrderPromo(models.Model):
    _name = 'sale.order.promo'
    _description = 'Sale order promo'

    order_id = fields.Many2one(
        'sale.order',
        string='sale order',
    )
    promo_id = fields.Many2one(
        'wak.promo',
        string='Promo',
    )
    product_qty = fields.Float(
        string='qty',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    discount = fields.Float(
        string='Discount',
    )

    def AddPromo(self, count=False):
        self.ensure_one()
        product_uom_qty = count if count else self.product_qty
        line = {
            'name': ':::PROMO::: %s' % self.product_id.display_name,
            'product_id': self.product_id.id,
            'product_uom_qty': product_uom_qty,
            'order_id': self.order_id.id,
            'promo_id': self.promo_id.id,
            'discount': self.discount,
        }
        self.env['sale.order.line'].create(line)
        #self.order_id.get_promos()

    def add_promo_read_promos(self, count= False):
        self.ensure_one()
        self.AddPromo(count)
        return self.order_id.read_promos()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    promo_id = fields.Many2one(
        'wak.promo',
        string='Promo',
    )
