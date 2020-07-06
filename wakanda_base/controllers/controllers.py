# -*- coding: utf-8 -*-
# from odoo import http


# class WakandaBase(http.Controller):
#     @http.route('/wakanda_base/wakanda_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wakanda_base/wakanda_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wakanda_base.listing', {
#             'root': '/wakanda_base/wakanda_base',
#             'objects': http.request.env['wakanda_base.wakanda_base'].search([]),
#         })

#     @http.route('/wakanda_base/wakanda_base/objects/<model("wakanda_base.wakanda_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wakanda_base.object', {
#             'object': obj
#         })
