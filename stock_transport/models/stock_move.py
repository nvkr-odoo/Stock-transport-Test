from odoo import fields, models, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    weight = fields.Float(string="Weight", compute='_compute_weight', store=True)
    volume = fields.Float(string="Volume", compute='_compute_volume', store=True)
    

    @api.depends('product_id', 'product_id.weight', 'product_id.volume', 'product_uom_qty')
    def _compute_weight(self):
        for move in self:
            move.weight = move.product_id.weight * move.product_uom_qty
            move.volume = move.product_id.volume * move.product_uom_qty


    
