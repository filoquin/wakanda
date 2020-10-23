# -*- coding: utf-8 -*-
import odoo
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import ensure_db
import werkzeug
import logging
_logger = logging.getLogger(__name__)


class WakandaBase(http.Controller):

    @http.route(['/wkn/json_logout'], type='json', auth="user")
    def json_logout(self):
        request.session.logout()
        datas = {}
        datas['login'] = False
        request.session.db = 'wakandaa'
        return datas

    @http.route('/wkn/json_login', methods=['POST'], type='json', auth="none", csrf=False)
    def json_login(self,  **post):
        request.session.db = 'wakandaa'
        ensure_db()
        datas = {}
        request.params['login_success'] = False

        # Usuario Esta Logueado

        if request.session.uid:
            request.session.logout()
            request.params['login_success'] = False
            data = request.env['res.users'].search_read(
                [('id', '=', request.session.uid)], ['login', 'name'])
            if len(data):
                datas['user'] = data[0]
            datas['logirequestn'] = True
            datas['uid'] = request.session.uid
            return datas

        if not request.uid:
            request.uid = odoo.SUPERUSER_ID
        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None

        login = post.get('login', False)
        password = post.get('password', False)
        request.session.db = 'wakandaa'
        if login and password:
            old_uid = request.uid
            uid = request.session.authenticate(
                request.session.db, login, password)
            if uid is not False:
                data = request.env['res.users'].search_read(
                    [('id', '=', uid)], ['login', 'name'])
                if len(data):
                    datas['user'] = data[0]
                request.params['login_success'] = True
                datas['login'] = True
                datas['uid'] = uid
                return datas

            request.uid = old_uid
            datas['error'] = "Wrong login/password"
            datas['login'] = False
        return datas

    def return_raise(self, error):
        pass

    def check_required_register(self, post_vars):
        req_post_vars = ['user', 'password', 'completename',
                         'email', 'phone', 'address', 'day', 'month', 'year']
        for var in req_post_vars:
            if var not in post_vars:
                return "NO estan definidos todos los campos obligatorios"
        return False

    @http.route('/wkn/json_register', methods=['POST'], type='json', auth="none", csrf=False)
    def register_user(self, **post_vars):
        datas = {}
        check = self.check_required_register(post_vars)
        new_user = request.env['res.users'].with_user(
            2).wkn_register(post_vars)
        if len(new_user):
            request.env.cr.commit()
            request.uid = odoo.SUPERUSER_ID
            _logger.info((request.session.db, post_vars[
                         'user'], post_vars['password']))
            #request.session.db = 'wakandaa'
            uid = request.session.authenticate(
                request.session.db, post_vars['user'], post_vars['password'])
            if uid is not False:
                data = request.env['res.users'].search_read(
                    [('id', '=', uid)], ['login', 'name'])
                if len(data):
                    datas['user'] = data[0]
                request.params['login_success'] = True
                datas['login'] = True
                datas['uid'] = uid
                datas['result'] = {'id': new_user.id,
                                   'msg': 'Su usuario se creo exitosamente'
                                   }

                return datas

        return datas

    @http.route('/wkn/req_confirm_code', methods=['POST'], type='json', auth="none", csrf=False)
    def new_confirm_code(self, **post_vars):
        if 'email' in post_vars and post_vars['email']:
            return request.env['res.users'].with_user(2).wkn_send_confirm_code(post_vars)
        return {'result': False, 'error': 'El email no esta registrado en nuestro sistema.'}

    @http.route('/wkn/send_confirm_code', methods=['POST'], type='json', auth="none", csrf=False)
    def confirm_confirm_code(self, **post_vars):
        if 'token' in post_vars and len(post_vars['token']) == 4:
            partner = request.env['res.partner'].sudo().search(
                [('signup_token', '=', post_vars['token'])])
            if len(partner):
                values = {
                    'login': partner.user_ids[0].login,
                    'name': partner.name,
                    'password': post_vars['password'],

                }
                db, login, password = request.env[
                    'res.users'].sudo().signup(values, post_vars['token'])
                # as authenticate will use its own cursor we need to commit the
                # current transaction
                request.env.cr.commit()
                uid = request.session.authenticate(db, login, password)
                if not uid:
                    return False
                else:
                    datas = {}
                    datas['login'] = True
                    datas['uid'] = uid
                    datas['result'] = {'id': uid,
                                       'msg': 'Su password se actualizo exitosamente'
                                       }
                    data = request.env['res.users'].search_read(
                        [('id', '=', request.session.uid)], ['login', 'name'])
                    if len(data):
                        datas['user'] = data[0]

                    return datas

                    #raise SignupError('Authentication Failed.')

                return True
            else:
                return False
        return False

    @http.route(['/'], type='http', auth="none")
    def home(self, dummie=None, dummie2=None, dummie3=None, dummie4=None, **kw):
        return werkzeug.utils.redirect('/app')

    @http.route(
        ['/app',
         '/app/<string:dummie>',
         '/app/<string:dummie>/<string:dummie2>',
         '/app/<string:dummie>/<string:dummie2>/<string:dummie3>',
         '/app/<string:dummie>/<string:dummie2>/<string:dummie3>/<string:dummie4>'
         ], type='http', auth="none")
    def app(self, dummie=None, dummie2=None, dummie3=None, dummie4=None, **kw):

        if dummie is None or dummie in ['login', 'products', 'prices', 'faq', 'orders']:
            return request.render("wakanda_base.app")
        else:
            current_url = 'https://app.wakanda.com.ar/wakanda_base/static/src/wakanda/' + dummie
            #current_url = '/wakanda_base/static/src/wakanda/' + dummie
            if dummie2:
                current_url += '/' + dummie2
            if dummie3:
                current_url += '/' + dummie3
            if dummie4:
                current_url += '/' + dummie4
            return werkzeug.utils.redirect(current_url)

    @http.route('/wkn/states',  auth="none", csrf=False)
    def get_states(self, **post_vars):
        states_ids = request.env['res.country.state'].with_user(2).search_read([('country_id.code', '=', 'AR')], ['name'])
        _logger.info('states_ids %r' % states_ids)
        return str(states_ids)
