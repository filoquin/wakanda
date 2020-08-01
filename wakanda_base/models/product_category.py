
from odoo import models, fields, api


class ProductCategory(models.Model):

    _inherit = "product.category"

    wkn_publish = fields.Boolean(
        string='Field Label',
    )

    wkn_categ_id = fields.Many2one(
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

            if len(childs) > 2:
                categ.wkn_categ_id = childs[-3]
            else:
                categ.wkn_categ_id = categ.id
