from odoo import api, fields, models, _


class ProductTemplate(models.Model):

    _inherit = ["product.template", "wak.published.mixin"]
    _name = 'product.template'

    wak_sequence = fields.Integer(
        help="Gives the sequence order when displaying a list of product.",
        index=True
    )

    final_price = fields.Float(
        'Final Price', compute='_compute_final_price',
        digits='Product Price'
    )

    def _compute_final_price(self):
        prices = self._compute_final_price_no_inverse()
        for template in self:
            template.final_price = prices.get(template.id, 0.0)

    def _compute_final_price_no_inverse(self):
        """The _compute_template_price writes the 'list_price' field with an inverse method
        This method allows computing the price without writing the 'list_price'
        """
        prices = {}
        pricelist = self.env.ref('wakanda_base.wak_final_price_list')
        partner = self.env.context.get('partner')
        quantity = self.env.context.get('quantity', 1.0)

        if pricelist:
            quantities = [quantity] * len(self)
            partners = [partner] * len(self)
            prices = pricelist.get_products_price(
                self, quantities, partners)

        return prices
