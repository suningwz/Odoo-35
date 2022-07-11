# -*- coding: utf-8 -*-
{
    'name': "Revivre Base",
    'summary': 'Custom Base',
    'description': 'Custom Base Module for Revivre',
    'version': '14.0.0.0.0',
    'author': 'ArkeUp SAS',
    'website': 'https://arkeup.com',
    'depends': [
        'web',
        'merge_similar_packaging_product',
        'ddmrp',
    ],
    'data': [
        # data
        # security
        # views
        'views/res_company_views.xml',
        # wizard
        # reports
        'reports/web_external_layout.xml',
        'reports/report_deliveryslip.xml',
        'reports/report_invoice.xml',
        'reports/report_picking.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
