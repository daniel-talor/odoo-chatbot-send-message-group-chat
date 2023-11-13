# -*- coding: utf-8 -*-
# from odoo import http


# class CoSocial(http.Controller):
#     @http.route('/co_social/co_social/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/co_social/co_social/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('co_social.listing', {
#             'root': '/co_social/co_social',
#             'objects': http.request.env['co_social.co_social'].search([]),
#         })

#     @http.route('/co_social/co_social/objects/<model("co_social.co_social"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('co_social.object', {
#             'object': obj
#         })
