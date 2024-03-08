{
    'name': 'Stock Transport',
    'depends': ['fleet','stock_picking_batch'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml'
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'stock_transport/static/src/stock_transport_gantt_renderer.xml',
    #         'stock_transport/static/src/stock_transport_gantt_renderer.js',
    #         'stock_transport/static/src/stock_transport_gantt_view.js',
    #     ]
    # },
    "auto_install": True,
}