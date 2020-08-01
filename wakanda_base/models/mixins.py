from odoo import api, fields, models, _

import logging
logger = logging.getLogger(__name__)


class WakPublishedMixin(models.AbstractModel):

    _name = "wak.published.mixin"
    _description = 'wak Published Mixin'

    wak_published = fields.Boolean('Visible on app', related='wak_is_published', readonly=False)
    wak_is_published = fields.Boolean('Is Published in app', copy=False, default=lambda self: self._default_is_published())
    wak_can_publish = fields.Boolean('Can Publish', compute='_compute_can_publish')

    def _default_is_published(self):
        return True

    def wak_publish_button(self):
        self.ensure_one()
        return self.write({'wak_published': not self.wak_published})

    def _compute_can_publish(self):
        """ This method can be overridden if you need more complex rights management than just 'website_publisher'
        The publish widget will be hidden and the user won't be able to change the 'website_published' value
        if this method sets can_publish False """
        for record in self:
            record.can_publish = True

    @api.model
    def _get_can_publish_error_message(self):
        """ Override this method to customize the error message shown when the user doesn't
        have the rights to publish/unpublish. """
        return _("You do not have the rights to publish/unpublish")
