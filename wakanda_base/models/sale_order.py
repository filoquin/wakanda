from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    wak_order = fields.Boolean(
        string='wak order',
    )

    def action_confirm(self):
        self.checkTotal()
        return super().action_confirm()

    def checkTotal(self):
        if self.env.user.has_group('wakanda_base.wak_group_revendedor') or self.env.user.id == 1:
            max_qty = self.env['ir.config_parameter'].get_param('max_qty', default=1)
            max_amount = self.env['ir.config_parameter'].get_param('max_amount', default=1)
            qty = 0
            for line in self.order_line:
                qty += line.qty
            if max_amount < self.total or qty < max_qty:
                raise UserError(_('Order not has min qty.'))


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    promo_id = fields.Many2one(
        'wak.promo',
        string='Promo',
    )
