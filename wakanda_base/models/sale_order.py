# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    wak_order = fields.Boolean(
        string='wak order',
    )
    def checkTotal(self):
        pass
