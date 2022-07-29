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
        'ddmrp',
    ],
    'data': [
        # data
        # security
        # 'security/ir.model.access.csv',
        # views
        'views/res_company_views.xml',
        # wizard
        # reports
        'reports/web_external_layout.xml',
        'views/report_asset.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
