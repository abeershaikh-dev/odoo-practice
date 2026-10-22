from odoo import models, fields
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    x_secondary_phone = fields.Char(
        string='Secondary Contact',
        help='Backup phone number for customer delivery or order confirmatiom'
    )