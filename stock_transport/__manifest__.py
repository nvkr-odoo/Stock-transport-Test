{
    'name': 'Stock Transport',
    'depends': ['fleet','stock_picking_batch'],
    'data': [
        'views/fleet_vehicle_model_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml'
    ],
    "auto_install": True,
}