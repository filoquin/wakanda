from odoo import fields, models, api


class WakCheap(models.Model):
    _name = 'wak.cheap'
    _description = 'wakanda cheap'
    _order = 'sequence'

    name = fields.Char(
        string='Title',
        required=True,
    )
    sequence = fields.Integer(
        string='sequence',
    )
    from_time = fields.Datetime(
        string='From',
        required=True,
    )
    to_time = fields.Datetime(
        string='to',
        required=True,
    )
    image = fields.Binary(
        string='image',
        attachment=True,
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )

    @api.model
    def list_cheap(self):
        return self.active_cheap().read(['name', 'sequence', 'image'])

    @api.returns('wak.promo')
    def active_promo(self):
        return self.search([
            ('from_time', '<=', fields.Datetime.now()),
            ('to_time', '>=', fields.Datetime.now())
        ], order='sequence', limit=1)
