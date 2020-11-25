# -*- coding: utf-8 -*-
# from odoo import http


# class SalesTeamImage(http.Controller):
#     @http.route('/sales_team_image/sales_team_image/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_team_image/sales_team_image/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_team_image.listing', {
#             'root': '/sales_team_image/sales_team_image',
#             'objects': http.request.env['sales_team_image.sales_team_image'].search([]),
#         })

#     @http.route('/sales_team_image/sales_team_image/objects/<model("sales_team_image.sales_team_image"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_team_image.object', {
#             'object': obj
#         })
