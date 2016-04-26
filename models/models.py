# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AccountInvoiceRelatedDocuments_inherit(models.Model):
    _inherit = 'account.invoice'
    
    related_document_ids = fields.One2many('account.invoice.related_documents', 'invoice_id', string='Related Documents', oldname='related_document',
        readonly=True, states={'draft': [('readonly', False)]}, copy=True)

class AccountInvoiceRelatedDocuments(models.Model):
    _name = 'account.invoice.related_documents'
    _description = 'Invoice Related Documents'
    _order = 'sequence'

    document_type = fields.Selection([
                                      ('factura','Factura'),
                                      ('fac_no_afecta','Factura no Afecta'),
                                      ('boleta_exenta','Boleta exenta'),
                                      ('liq_factura','Liq. Factura'),
                                      ('fac_compra','Factura de Compra'),
                                      ('guia_despacho','Guía de Despacho'),
                                      ('nota_debito','Nota de Débito'),
                                      ('nota_credito','Nota de Crédito'),
                                      ('liq_com_dis','Liq. com. dis.'),
                                      ('fac_elec','Factura elec.'),
                                      ('fac_no_afecta_elec','Factura no afecta ele.'),
                                      ('boleta_elec','Boleta elec.'),
                                      ('fac_compra_elec','Factura Compra elec.'),
                                      ('nota_debito_elec','Nota Débito elec.'),
                                      ('nota_credito_elec','Nota de Crédito elec.'),
                                      ('guia_despacho_elec','Guía de Despacho elec.'),
                                      ('orden_compra','Orden de Compra'),
                                      ('nota_pedido','Nota de Pedido'),
                                      ('contrato','Contrato'),
                                      ('resolucion','Resolución'),
                                      ('proc_chilecompra','Proceso ChileCompra'),
                                      ('ficha_chilecompra','Ficha ChileCompra'),
                                      ('hoja_ent_servicio','Hoja Entrada Servicio')],
                                      string = 'Tipo de Documento',
                                      )
    name = fields.Char( size = 60, string = 'Referencia', help = 'Documento de Referencia' )
    folio = fields.Integer(string = 'Folio', help = 'Indicar Número de Folio')
    fecha = fields.Date( string = 'Fecha del documento')
    invoice_id = fields.Many2one('account.invoice', string='Invoice Reference',
        ondelete='cascade', index=True)
    sequence = fields.Integer(help="Gives the sequence order when displaying a list of invoice Related Document.")    