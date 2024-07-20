from odoo import models, fields

class CourierMasterSheet(models.Model):
    _name = 'courier.master.sheet'
    _description = 'Courier Master Sheet'

    name = fields.Char(string='Name', required=True)
