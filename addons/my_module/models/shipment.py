from odoo import models, fields

class Shipment(models.Model):
    _name = 'shipment.model'
    _description = 'Shipment Model'

    name = fields.Char(string='Name', required=True)
    order_ids = fields.One2many('sale.order', 'shipment_id', string='Orders')
    courier_id = fields.Many2one('courier.model', string='Courier')
    hub = fields.Char(string='Hub')
    status = fields.Selection([
        ('ready_for_delivery', 'Ready for Delivery'),
        ('dispatched', 'Dispatched'),
    ], string='Status', default='ready_for_delivery')
    dispatch_date = fields.Date(string='Dispatch Date')
    received_date = fields.Date(string='Received Date')
