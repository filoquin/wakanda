# -*- coding: utf-8 -*-

from odoo import fields, models


class WakFaq(models.Model):
    _name = 'wak.faq'
    _description = 'wakanda faqs'

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
    active = fields.Boolean(
        string='Active',
        default=True
    )
