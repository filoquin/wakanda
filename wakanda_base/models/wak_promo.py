from odoo import fields, models


class WakPromo(models.Model):
    _name = 'wak.promo'
    _description = 'wakanda promo'

    name = fields.Char(
        string='Title',
        required=True,
    )
    sequence = fields.Integer(
        string='sequence',
    )
    html = fields.Html(
        string='Html',
    )
    from_time = fields.Datetime(
        string='From',
    )
    to_time = fields.Datetime(
        string='to',
    )
    active = fields.Boolean(
        string='Active',
    )
    gift_product_ids = fields.Many2many(
        'product.product',
        string='gift',
    )
    gift_discount = fields.Float(
        string='gift discount',
        default=100
    )
    rule_type = fields.Selection(
        [
         ('qty_product', 'qty products'),
         ('multiple_product', 'multiple qyt of products'),
         ('amount', 'amount products'),
        ],
        string='rule type',
        default='qty_product'
    )
    rule_qty = fields.Float(
        string='Rule Qty',
    )
