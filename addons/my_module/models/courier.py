from odoo import models, fields

class Courier(models.Model):
    _name = 'courier.model'
    _description = 'Courier Model'

    name = fields.Char(string='Name', required=True)
    national_id = fields.Char(string='National ID')
    iqama_number = fields.Char(string='Iqama Number')
    iqama_expiry = fields.Date(string='Iqama Expiry')
    iqama_attachment = fields.Binary(string='Iqama Attachment')
    passport_number = fields.Char(string='Passport Number')
    passport_expiry = fields.Date(string='Passport Expiry')
    passport_attachment = fields.Binary(string='Passport Attachment')
    driving_license_number = fields.Char(string='Driving License Number')
    driving_license_expiry = fields.Date(string='Driving License Expiry')
    driving_license_attachment = fields.Binary(string='Driving License Attachment')
    contact_number = fields.Char(string='Contact Number')
    emergency_contact = fields.Char(string='Emergency Contact')
    emergency_contact_number = fields.Char(string='Emergency Contact Number')
    nationality = fields.Char(string='Nationality')
    vehicle_ids = fields.One2many('vehicle.model', 'courier_id', string='Vehicles')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')
    created_date = fields.Date(string='Created Date', default=fields.Date.today)
