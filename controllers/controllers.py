# -*- coding: utf-8 -*-
from odoo import http

# class OnidaApps(http.Controller):
#     @http.route('/onida_apps/onida_apps/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/onida_apps/onida_apps/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('onida_apps.listing', {
#             'root': '/onida_apps/onida_apps',
#             'objects': http.request.env['onida_apps.onida_apps'].search([]),
#         })

#     @http.route('/onida_apps/onida_apps/objects/<model("onida_apps.onida_apps"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('onida_apps.object', {
#             'object': obj
#         })