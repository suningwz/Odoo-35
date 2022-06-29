# -*- coding: utf-8 -*-
{
    'name': "Revivre Sale",
    'summary': 'Custom Sale Management',
    'description': 'Custom Sale Management',
    'version': '14.0.0.0.0',
    'author': 'ArkeUp SAS',
    'website': 'https://arkeup.com',
    'depends': [
        'revivre_base',
        'merge_similar_packaging_product',
    ],
    'data': [
        # data
        # security
        # views
        # wizard
        # reports
        'reports/sale_report_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
