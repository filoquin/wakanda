# -*- coding: utf-8 -*-
{
    'name': "sale picking state",

    'summary': """
        Show picking state in sale order""",

    'description': """
        This module show and filter sale order by picking state.
    """,

    'author': "Filoquin",
    'website': "http://www.sipecu.com.ar",
    'category': 'sale',
    'version': '13.0.0.1',

    'depends': ['sale'],

    'data': [
        'views/sale_order.xml',
    ],
}
