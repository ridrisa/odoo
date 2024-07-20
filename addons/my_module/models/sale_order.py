from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    shipment_id = fields.Many2one('shipment.model', string='Shipment')
