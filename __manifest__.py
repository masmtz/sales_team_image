# -*- coding: utf-8 -*-
{
    'name': "sales_team_image",

    'summary': """
        Add an image field in sales team
    """,

    'description': """
        Add an image field in sales team
    """,

    'author': "Morwi Encoders Consulting SA DE CV",
    'website': "http://www.morwi.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sales_team'],

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
