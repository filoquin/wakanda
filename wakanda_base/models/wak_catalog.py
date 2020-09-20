from odoo import fields, models, api

import logging
logger = logging.getLogger(__name__)


class WakCatalog(models.Model):

    _name = 'wak.catalog'
    _description = 'wakanda catalog'
    name = fields.Char(
        string='Title',
        required=True,
    )
    from_time = fields.Datetime(
        string='From',
        required=True,
    )
    to_time = fields.Datetime(
        string='to',
        required=True,
    )
    attachment_ids = fields.One2many(
        'ir.attachment',
        'res_id',
        domain=[('res_model', '=', _name)],
        string='PDF'
    )

    images_ids = fields.One2many(
        'wak.catalog.images',
        'catalog_id',
        string='Images',
    )

    @api.model
    def list_catalog(self):
        catalog_id = self.active_catalog()
        if len(catalog_id):
            catalog = catalog_id.read(['name'])

            catalog[0]['pdf'] = catalog_id.sudo().attachment_ids.read([])
            catalog[0]['images'] = catalog_id.images_ids.read(['image'])
            return catalog

    @api.returns('wak.promo')
    def active_catalog(self):
        return self.search([
            ('from_time', '<=', fields.Datetime.now()),
            ('to_time', '>=', fields.Datetime.now())
        ], limit=1)


class WakCatalogImages(models.Model):

    _name = 'wak.catalog.images'
    _description = 'wakanda catalog images'
    _order = 'sequence'

    catalog_id = fields.Many2one(
        'wak.catalog',
        string='catalog',
    )
    sequence = fields.Integer(
        string='sequence',
    )

    image = fields.Binary(
        string='image',
        attachment=True,
    )
