from odoo import models, fields, api

class Vehicle(models.Model):
    _name = 'vehicle.model'
    _description = 'Vehicle Model'

    name = fields.Char(string='Name', required=True)
    car_status = fields.Char(string='Car Status')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Year')
    plate_letters = fields.Char(string='Plate Letters')
    plate_numbers = fields.Integer(string='Plate Numbers')
    color = fields.Selection([
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('red', 'Red'),
        ('purple', 'Purple'),
        ('blue', 'Blue'),
        ('white', 'White'),
        ('black', 'Black'),
    ], string='Color')
    license_plates = fields.Char(string='License Plates')
    photo = fields.Binary(string='Photo')
    replacement_original_car = fields.Boolean(string='Replacement Original Car')
    date_of_first_receive = fields.Date(string='Date of First Receive')
    last_action = fields.Char(string='Last Action')
    contract_type = fields.Selection([
        ('yearly', 'Yearly'),
        ('replacement', 'Replacement'),
        ('barq_own_asset', 'BARQ Own Asset'),
    ], string='Contract Type')
    replacement_for = fields.Many2one('vehicle.model', string='Replacement For')
    added_by = fields.Many2one('res.users', string='Added By', default=lambda self: self.env.user)
    type = fields.Selection([
        ('to_courier', 'To Courier'),
        ('to_agency', 'To Agency'),
        ('to_barq', 'To BARQ'),
        ('maintenance', 'Maintenance'),
        ('to_barq_scrap', 'To BARQ Scrap'),
    ], string='Movement Type')
    own_car_plate = fields.Char(string='Own Car Plate')
    own_car_make = fields.Char(string='Own Car Make')
    own_car_model = fields.Char(string='Own Car Model')
    own_car_registration = fields.Binary(string='Own Car Registration')
    passport_attachment = fields.Binary(string='Passport Attachment')
    courier_id = fields.Many2one('courier.model', string='Courier')
