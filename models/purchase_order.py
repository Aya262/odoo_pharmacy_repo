from odoo import fields,models

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    partner_id = fields.Char(string = 'Supplier')