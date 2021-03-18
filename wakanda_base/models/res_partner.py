from odoo import fields, models, tools
from odoo.exceptions import UserError
from math import floor

import logging
logger = logging.getLogger(__name__)


class ResPartnerStat(models.Model):
    _name = 'res.partner.stat'
    _description = 'view partner stats'
    _auto = False

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
    )
    product_uom_qty = fields.Float(
        string='product_uom_qty',
    )
    order_count = fields.Float(
        string='order_count',
    )
    amount_total = fields.Float(
        string='amount_total',
    )


    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE view %s as
                select so.partner_id as id, so.partner_id , sum(product_uom_qty) as product_uom_qty,
                       count(distinct so.id) as order_count, sum(amount_total) as amount_total
                from sale_order_line l
                join sale_order so on so.id = l.order_id
                group by so.partner_id
        """ % (self._table,))


class ResPartner(models.Model):
    _inherit = 'res.partner'

    stats_ids = fields.One2many(
        'res.partner.stat',
        'partner_id',
        string='Stat',
        auto_join=True
    )

    know_us = fields.Text(
        string='How did you know us',
    )
    sale_role = fields.Selection(
        [('revendedor', 'revendedor'), ('comercio', 'comercio'), ],
        string='Role',
        compute='compute_role'
    )
    commerce_categ_ids = fields.One2many(
         'product.category',
         'wkn_partner_id',
         string='Commerce category',
     )

    def action_transform_commerce(self):
        self.user_ids.groups_id = [(3, self.env.ref(
            'wakanda_base.wak_group_revendedor').id), (4, self.env.ref('wakanda_base.wak_group_comercio').id)]

    def action_transform_rev(self):
        self.user_ids.groups_id = [(3, self.env.ref(
            'wakanda_base.wak_group_comercio').id), (4, self.env.ref('wakanda_base.wak_group_revendedor').id)]

    def compute_role(self):
        for record in self:

            if record.user_ids.has_group('wakanda_base.wak_group_revendedor'):
                record.sale_role = 'revendedor'
            elif record.user_ids.has_group('wakanda_base.wak_group_comercio'):
                record.sale_role = 'comercio'
            else:
                record.sale_role = False