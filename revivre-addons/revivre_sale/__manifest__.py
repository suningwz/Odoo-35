# -*- coding: utf-8 -*-
{
    'name': "Revivre Sale",
    'summary': 'Custom Sale Management',
    'description': 'Custom Sale Management',
    'version': '14.0.0.0.0',
    'author': 'ArkeUp SAS',
    'website': 'https://arkeup.com',
    'depends': [
        'sale',
        'product',
        'revivre_base',
    ],
    'data': [
        # data
        # security
        # views
        # wizard
        # reports
        'reports/sale_report_templates.xml',
        # 'reports/report_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
