# -*- coding: utf-8 -*-
{
    'name': "Revivre Purchase",
    'summary': 'Custom Purchase Management',
    'description': 'Custom Purchase Management',
    'version': '14.0.0.0.0',
    'author': 'ArkeUp SAS',
    'website': 'https://arkeup.com',
    'depends': [
        'revivre_base',
        'purchase',
        'merge_similar_packaging_product',
    ],
    'data': [
        # data
        # security
        # views
        'views/product_template_views.xml',
        'views/purchase_order_views.xml',
        'reports/purchase_report_templates.xml',
        # wizard
        # reports
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
