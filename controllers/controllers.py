# -*- coding: utf-8 -*-
from openerp import http

# class L10nClInvRelatedDocuments(http.Controller):
#     @http.route('/l10n_cl_inv_related_documents/l10n_cl_inv_related_documents/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_inv_related_documents/l10n_cl_inv_related_documents/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_inv_related_documents.listing', {
#             'root': '/l10n_cl_inv_related_documents/l10n_cl_inv_related_documents',
#             'objects': http.request.env['l10n_cl_inv_related_documents.l10n_cl_inv_related_documents'].search([]),
#         })

#     @http.route('/l10n_cl_inv_related_documents/l10n_cl_inv_related_documents/objects/<model("l10n_cl_inv_related_documents.l10n_cl_inv_related_documents"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_inv_related_documents.object', {
#             'object': obj
#         })