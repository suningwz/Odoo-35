# -*- coding: utf-8 -*-
{
    'name': "Revivre Account",
    'summary': 'Custom Account Management',
    'description': 'Custom Sale Management',
    'version': '14.0.0.0.0',
    'author': 'ArkeUp SAS',
    'website': 'https://arkeup.com',
    'depends': [
        'sale',
        'account',
        'product',
        'sale_stock',
        'revivre_base',
        'stock_packaging_calculator',
    ],
    'data': [
        # data
        # security
        # views
        # wizard
        # reports
        'views/account_move_line.xml',
        'reports/report_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
