from odoo import models, fields

class Vehicle(models.Model):
    _name = 'my_module.vehicle'
    _description = 'Vehicle'

    name = fields.Char(
        string='Name',
        required=True,
    )
    model = fields.Char(
        string='Model',
     )
    year = fields.Integer(
        string='Year',
    )
