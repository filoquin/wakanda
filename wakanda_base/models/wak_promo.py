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
        required=True,
    )
    to_time = fields.Datetime(
        string='to',
        required=True,
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
    gift_product_ids = fields.Many2many(
        comodel_name='product.product',
        relation='promo_gift_rel',
        column1='promo_id',
        column2='product_id',
        string='Gift',
    )
    gift_discount = fields.Float(
        string='Gift discount',
        default=100
    )
    gift_qty = fields.Integer(
        string='gift Qty',
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
    required_product_ids = fields.Many2many(
        comodel_name='product.product',
        relation='promo_req_product_rel',
        column1='promo_id',
        column2='product_id',
        string='required product',
    )
