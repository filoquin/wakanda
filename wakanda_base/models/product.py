# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _


class ProductTemplate(models.Model):

    _inherit = ["product.template", "wak.published.mixin"]
    _name = 'product.template'

    wak_sequence = fields.Integer(help="Gives the sequence order when displaying a list of product.", index=True)
