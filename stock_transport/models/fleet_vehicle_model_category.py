
from odoo import fields, models, api


class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'
    # _rec_name = 

    max_weight = fields.Float(string='Max Weight (kg)')
    max_volume = fields.Float(string='Max Volume (m³)')


    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            name=record.name
            if(record.max_volume or record.max_weight):
                name = name+"({}kg, {}m³)".format(record.max_weight,record.max_volume)
            record.display_name = name
    
    
