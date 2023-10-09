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
    text = fields.Html(
        string='Texto',
    )
    cheap_type = fields.Selection(
        string='Tipo',
        selection=[
            ('price_list', 'Price List'),
            ('pop_up', 'Pop-up'),
            ('home_image', 'Home Image'),
        ],
        default='price_list',
)

    @api.model
    def list_cheap(self, filter_type=None):
        domain = [
            ('from_time', '<=', fields.Datetime.now()),
            ('to_time', '>=', fields.Datetime.now())
        ]
    
        if filter_type:
            domain.append(('cheap_type', '=', filter_type))
    
        active_cheap = self.search(domain, order='sequence', limit=1)
        return active_cheap.read(['name', 'sequence', 'image', 'text'])
