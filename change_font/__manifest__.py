# -*- coding: utf-8 -*-
{
    'name': "ChangeFont",

    'summary': """
        Small module for changing font of the back-end side of Odoo to Cairo. It can also be extended to include other 
        fonts by changing the source code.
        """,

    'description': """
        Small module for changing font of the back-end side of Odoo to Cairo. It can also be extended to include other 
        fonts by changing the source code.
    """,

    'author': "Waleed",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': []
}
