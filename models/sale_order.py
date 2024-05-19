from odoo import fields,models

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    partner_id = fields.Char(string='Patient')




    