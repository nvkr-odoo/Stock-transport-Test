from odoo import models, fields,api

class Dock(models.Model):
    _name='fleet.dock'

    name=fields.Char('Name')
    