# -*- coding: utf-8 -*-
{
    'name': "custom_crm",

    'summary': """
        Modulo creado por Oscar del Amo Diezma""",

    'description': """
        Módulo creado por Oscar del Amo Diezma.
    """,

    'author': "Oscar del Amo Diezma",
    'website': "http://www.indytekservices.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/visit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
