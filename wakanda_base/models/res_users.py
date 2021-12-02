from odoo import models, fields, api, _
from odoo.exceptions import UserError
from math import floor
from random import randint
from odoo.tools.image import image_data_uri
import logging
logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    wkn_confirm_code = fields.Char(
        string='Confirm code',
    )

    @api.model
    def get_token(self):
        access_token = '%s' % (hex(randint(0x1111, 0xffff))[2:])
        exists = self.search_count(
            [('wkn_confirm_code', '=', access_token)])
        if exists:
            return self.get_token()
        return access_token

    @api.model
    def welcomevideo(self):
        return self.env['ir.config_parameter'].sudo().get_param('welcomevideo', 'https://www.youtube.com/embed/iAPwOPzD20k')

    @api.model
    def wkn_my_profile(self):
        user_id = self.env.user
        image = image_data_uri(
            user_id.partner_id.image_256) if user_id.partner_id.image_256 else ''
        profile = {
            'partner_id': user_id.partner_id.id,
            'name': user_id.partner_id.name,
            'email': user_id.partner_id.email,
            'image': image,
            'phone': user_id.partner_id.phone,
            'street': user_id.partner_id.street,
            'product_uom_qty': 0,
            'order_count': 0,
            'amount_total': 0,
        }
        if user_id.partner_id.birthdate_date:
            profile['year'] = user_id.partner_id.birthdate_date.year
            profile['month'] = user_id.partner_id.birthdate_date.month
            profile['day'] = user_id.partner_id.birthdate_date.day

        if len(user_id.partner_id.stats_ids):
            profile['product_uom_qty'] = user_id.partner_id.stats_ids[
                0]['product_uom_qty']
            profile['order_count'] = user_id.partner_id.stats_ids[
                0]['order_count']
            profile['amount_total'] = user_id.partner_id.stats_ids[
                0]['amount_total']

        return profile

    @api.model
    def wkn_send_confirm_code(self, post):
        user_id = self.search([('email', '=', post['email'])], limit=1)
        if len(user_id):
            token = self.get_token()
            #user_id.wkn_confirm_code = token
            user_id.partner_id.write({
                'signup_token': token,
                'signup_type': 'reset',
                'signup_expiration': False
            })

            template = self.env.ref('wakanda_base.send_confirm_code')
            template.sudo().send_mail(user_id.id)

            return True
        else:
            return False

    def wkn_register(self, post):
        birthdate = "%s-%s-%s" % (post['year'], post['month'], post['day'])
        group_revendedor = self.env.ref('wakanda_base.wak_group_revendedor')
        group_public = self.env.ref('base.group_public')
        token = self.get_token()
        partner_info = {'name':  post['completename'],
                        'email':   post['email'],
                        'phone': post['phone'],
                        'street': post['address'],
                        'birthdate_date': birthdate,
                        'state_id': post['state_id'],
                        'know_us': post['know_us'],
                        }
        if 'documento' in post and 'tipo_documento' in post:
            partner_info['vat'] = post.get('documento').replace('.', '') 
            tipo_documento = post.get('tipo_documento')
            partner_info['tipo_documento'] = self.ref('l10n_ar.it_cuit').id if tipo_documento == '2' else self.ref('l10n_ar.it_dni').id

        new_partner = self.env['res.partner'].with_context(mail_create_nosubscribe=True).create(
            [partner_info]
        )
        new_user = self.with_context(mail_create_nosubscribe=True).create(
            [{
                'login': post['user'],
                'password': post['password'],
                'partner_id': new_partner.id,
                'wkn_confirm_code':token,
                'groups_id':[(4, group_revendedor.id)]
            }]
        )
        return new_user
