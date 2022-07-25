# -*- coding: utf-8 -*-
{
    'name': "Revivre Stock",
    'summary': 'Custom Stock Management',
    'description': 'Custom Stock Management',
    'version': '14.0.0.0.0',
    'author': 'ArkeUp SAS',
    'website': 'https://arkeup.com',
    'depends': [
        'stock',
        'delivery',
    ],
    'data': [
        'views/stock_move_line.xml',
        'reports/report_deliveryslip.xml',
        'reports/report_picking.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
