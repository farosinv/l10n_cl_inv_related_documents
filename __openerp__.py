# -*- coding: utf-8 -*-
{
    'name': "Odoo Invoice related Documents for Chilean DTE's",

    'summary': """
        Documentos relacionados para facturación electrónica Chilena""",

    'description': """
        Éste módulo agrega la funcionalidad de relacionar documentos a factura para la generación
        de factura electrónica de acuerdo a la normativa Chilena. PArte del proyecto de Documentos
        Tributarios electrónicos Chile mediante Odoo.
    """,

    'author': "Faros Inversiones Ltda.",
    'website': "http://www.farosinv.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}