
from odoo import models, fields, api


class ProductCategory(models.Model):

    _inherit = "product.category"

    wkn_publish = fields.Boolean(
        string='Publish',
    )

    wkn_main_categ_id = fields.Many2one(
        'product.category',
        string='Wakanda category',
        compute='_compute_supply_categ',
        inverse='_compute_supply_categ_inverse',
        store=True,
    )
    wkn_partner_id = fields.Many2one(
        'res.partner',
        string='category own',
    )

    wkn_categ_image = fields.Binary(
        string='Icon',
        attachment=False,
        default="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"
    )
    price_product_id = fields.Many2one(
        'product.product',
        string='Product from price',
    )
    user_price = fields.Float(
        'User Price',
        related='price_product_id.user_price',
        digits='Product Price'
    )

    final_price = fields.Float(
        'Final Price',
        related='price_product_id.final_price',
        digits='Product Price'
    )

    def _compute_supply_categ_inverse(self):
        pass

    @api.depends('parent_id')
    def _compute_supply_categ(self):
        for categ in self:
            parent = categ
            childs = []
            childs.append(parent.parent_id.id)
            while len(parent):
                parent = self.search(
                    [('id', '=', parent.parent_id.id)], limit=1)
                if len(parent) and parent.parent_id.id != False:
                    childs.append(parent.parent_id.id)

            if len(childs) > 1:
                categ.wkn_main_categ_id = childs[2]
            else:
                categ.wkn_main_categ_id = categ.id
