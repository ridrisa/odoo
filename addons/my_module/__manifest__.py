{
    'name': 'My Module', 'version': '1.0', 'category': 'Custom',
   'summary': 'Custom Module for Vehicles, Couriers, and Shipments',
   'description': "This module manages vehicles, couriers, and shipments.",
   'author': 'The Great Digalyzer',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle_views.xml',
        'views/courier_views.xml',
        'views/shipment_views.xml',
        'views/sale_order_views.xml',
        'views/menus.xml'
    ],
    'installable': True,
    'application': True
}