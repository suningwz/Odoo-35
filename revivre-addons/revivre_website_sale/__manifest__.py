# -*- coding: utf-8 -*-
{
    'name': "Revivre Website Sale",
    'summary': 'Custom Website Sale Management',
    'description': 'Custom Website Sale Management',
    'version': '14.0.0.0.0',
    'author': 'ArkeUp SAS',
    'website': 'https://arkeup.com',
    'depends': [
        'revivre_base',
        'purchase',
        'website_display_packaging_options',
    ],
    'data': [
        # data
        'data/data.xml',
        'security/ir.model.access.csv',
        # security
        # views
        'views/sale_order.xml',
        'views/templates.xml',
        # wizard
        # reports
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
