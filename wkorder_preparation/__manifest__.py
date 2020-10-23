# -*- coding: utf-8 -*-
{
    'name': "order preparation",

    'summary': """
       order preparatin and produce""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Filoquin",
    'website': "http://www.sipecu.com.ar",
    'category': 'mpr',
    'version': '13.0.0.1',

    'depends': ['stock', 'mrp', 'sale', 'stock_move_line_auto_fill'],

    'data': [
        'security/ir.model.access.csv',
        'data/seq_order_preparation.xml',
        'views/report.xml',
        'views/order_preparation.xml',
    ],
}
