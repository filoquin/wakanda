from odoo import fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    is_published = fields.Boolean(
        string='Published',
    )
