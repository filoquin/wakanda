from odoo import models, fields, api, _
from odoo.exceptions import UserError
from math import floor

import logging
logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    def wkn_register(self, post):
        birtdate = "%s-%s-%s" % (post['year'], post['month'], post['day'])
        group_revendedor = self.env.ref('wakanda_base.wak_group_revendedor')
        group_public = self.env.ref('base.group_public')

        new_parner = self.env['res.partner'].with_context(mail_create_nosubscribe=True).create(
            [{'name':  post['completename'],
              'email':   post['email'],
              'phone': post['phone'],
              'street': post['address']
              }]
        )
        logger.info(new_parner)
        new_user = self.with_context(mail_create_nosubscribe=True).create(
            [{
                'login': post['user'],
                'password': post['password'],
                'partner_id': new_parner.id,
                'groups_id':[(4, group_revendedor.id), (4, group_public.id)]
            }]
        )
        logger.info(new_user)
        return new_user
