# -*- coding: utf-8 -*-
{
    'name': "wakanda",

    'summary': """
        Modulo base para la implementacion de la app Wakanda""",

    'description': """
        WAKANDA
        Este modulo implementa los conceptos necesarios apa servir a la app Wakanda
        - Server de PWA.
        - Panel de control de app
        - Rol usuario de app comercio, revendedor
        - Categorías relacionadas con partner comercio
        - Reglas base de acceso a los productos, órdenes de venta para los usuarios de la app.
        - Promoción. Regalo de productos.
        - Creación de campo publish app que defina los productos que estarán visibles en la app.
        - No permitirá el cierre de una sale order a los usuarios de la app si no cumple con el mínimo de pedido (configurable).
        - Creará las listas de precios. Precio de venta final. y precio por defecto de la app (revendedor).
        - Modelo de datos FAQ: Modelo con campos name, html, activo
        - Modelo de datos Promociones: Modelo con campos name, html y fecha desde hasta.
        - Rest para registro y recuperar la clave.
        - Vista qweb de la Lista de precios para revendedores
    """,

    'author': "filoquin",
    'website': "http://www.sipecu.com.ar",
    'category': 'wakanda',
    'version': '0.1',

    'depends': ['sale'],

    'data': [
        'data/wak_base_data.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/sale_order.xml',
        'views/product_views.xml',
        'views/wak_faq.xml',
        'views/wak_app.xml',
        'views/wak_promo.xml',
        'views/product_category.xml',
    ],
    'demo': [
    ],
}
