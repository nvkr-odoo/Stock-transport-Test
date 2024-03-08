from odoo import fields, api, models


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    dock_id=fields.Many2one('fleet.dock', string="Dock ID")

    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')

    weight = fields.Float(string="Weight", compute='_compute_weight', store=True)
    volume = fields.Float(string="Volume", compute='_compute_volume', store=True)
    weight_bar = fields.Float(compute="_compute_weight_bar")
    volume_bar = fields.Float(compute="_compute_volume_bar")

    driver_image=fields.Image(related='vehicle_id.driver_id.image_1920')
    transfer = fields.Float("#Transfer", compute="compute_transfer", store=True)
    lines = fields.Float("#Lines", compute="compute_lines", store=True)


    @api.depends('name','weight','volume','driver_image')
    def _compute_display_name(self):
        for record in self:       
            record.display_name =  f"{record.name} {record.weight}kg, {record.volume}m\u00b3 {record.driver_image}"

    @api.depends('picking_ids.weight', 'picking_ids.volume')
    def _compute_weight(self):
        for batch in self:
            batch.weight = sum(move.weight for move in batch.picking_ids)
            batch.volume = sum(move.volume for move in batch.picking_ids)

    @api.depends('vehicle_category_id', 'weight', 'weight_bar')
    def _compute_weight_bar(self):
        for record in self:
            if (record.vehicle_category_id and record.vehicle_category_id.max_weight):
                record.weight_bar = (record.weight/record.vehicle_category_id.max_weight) * 100
            else:
                record.weight_bar = 0.0

    @api.depends('vehicle_category_id', 'volume', 'volume_bar')
    def _compute_volume_bar(self):
        for record in self:

            if (record.vehicle_category_id and record.vehicle_category_id.max_volume):
                record.volume_bar = (record.volume/record.vehicle_category_id.max_volume) * 100
            else:
                record.volume_bar = 0.0

    @api.depends("picking_ids")
    def compute_transfer(self):
        for record in self:
            curr = len(record.picking_ids)
            record.transfer = curr

    @api.depends("move_line_ids")
    def compute_lines(self):
        for record in self:
            curr = len(record.move_line_ids)
            record.lines = curr
    