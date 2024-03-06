from odoo import fields, api, models


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking'

    weight = fields.Float(string="Weight", compute='_compute_weight', store=True)
    volume = fields.Float(string="Volume", compute='_compute_volume', store=True)


    @api.depends('move_ids.weight', 'move_ids.volume')
    def _compute_weight(self):
        for batch in self:
            batch.weight = sum(move.weight for move in batch.move_ids)
            

    @api.depends('move_ids.weight', 'move_ids.volume')
    def _compute_volume(self):
        for batch in self:
            batch.volume = sum(move.volume for move in batch.move_ids)
            

    
    