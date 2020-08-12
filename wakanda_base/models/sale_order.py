from odoo import models, fields, api, _
from odoo.exceptions import UserError
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
    def wkn_create(self, lines):
        logger.info(lines)
        order_line = []
        for line in lines:
            product = self.env['product.template'].browse(line['id'])
            order_line.append((0, 0, {'product_id': product.product_variant_ids[0].id, 'product_uom_qty': line['qty']}))
        order = {
            'user_id': self.env.user.id,
            'partner_id': self.env.user.partner_id.id,
            'pricelist_id': self.env.user.partner_id.property_product_pricelist.id,
            'wak_order': True,
            'order_line': order_line
        }
        order_id = self.create(order)
        order_id.get_promos()

        return order_id.read(['show_promos', 'promo_line_ids'])

    def compute_promos(self):
        self.get_promos()

    def read_promos(self):
        self.ensure_one()
        self.get_promos(self)
        return self.promo_line_ids.read(['promo_id', 'product_qty' 'product_id', 'discount'])

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
                    if line.product_id.id in promo_id.gift_product_ids.ids \
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
        if self.env.user.has_group('wakanda_base.wak_group_revendedor') or self.env.user.id == 1:
            max_qty = self.env['ir.config_parameter'].get_param(
                'max_qty', default=1)
            max_amount = self.env['ir.config_parameter'].get_param(
                'max_amount', default=1)
            qty = 0
            for line in self.order_line:
                qty += line.qty
            if max_amount < self.total or qty < max_qty:
                raise UserError(_('Order not has min qty.'))

    def _get_wkn_delivery_methods(self):
        address = self.partner_shipping_id
        # searching on website_published will also search for available website (_search method on computed field)
        return self.env['delivery.carrier'].sudo().search([('is_published', '=', True)]).available_carriers(address)

    def read_delivery_methods(self):
        carriers = []

        delivery_methods = self._get_wkn_delivery_methods()
        for delivery_method in delivery_methods:
            vals = self.carrier_id.rate_shipment(self.id)
            if vals.get('success'):
                carrier_tmp = {}
                carrier_tmp['delivery_message'] = vals.get('warning_message', False)
                carrier_tmp['delivery_price'] = vals['price']
                carrier_tmp['display_price'] = vals['carrier_price']
                carrier_tmp['name'] = delivery_method.display_name
                carrier_tmp['id'] = delivery_method.id

        return carriers

    def delivery_confirm(self, carrier_id, delivery_price):
        self.sudo().set_delivery_line(carrier_id, delivery_price)
        self.sudo().write({
            'recompute_delivery_price': False,
            'delivery_message': self.delivery_message,
        })


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

    def AddPromo(self):
        self.ensure_one()
        line = {
            'name': ':::PROMO::: %s' % self.product_id.display_name,
            'product_id': self.product_id.id,
            'product_uom_qty': self.product_qty,
            'order_id': self.order_id.id,
            'promo_id': self.promo_id.id,
            'discount': self.discount,
        }
        self.env['sale.order.line'].create(line)
        self.order_id.get_promos()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    promo_id = fields.Many2one(
        'wak.promo',
        string='Promo',
    )
