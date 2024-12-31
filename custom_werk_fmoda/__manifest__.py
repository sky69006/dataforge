# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    #  Information
    'name': 'Custom werk Federicomoda - Dataforge',
    'version': '18.0.0.1',
    'summary': 'Custom werk Federicomoda - Dataforge',
    'description': '''
        OCustom werk epdm - Dataforge
    ''',
    'category': 'Customization',

    # Author
    'author': 'Odoo PS',
    'license': 'LGPL-3',

    # Dependency
    'depends': ['sale'],

    'assets': {
        'point_of_sale._assets_pos': [
            'web/fmoda.js',
            'web/fmoda.xml',
        ],

        },
    # Other
    'installable': True,
    'auto_install': False,
}
