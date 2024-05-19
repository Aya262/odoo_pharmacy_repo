from odoo import fields , models , api

from datetime import datetime
class Medicine(models.Model):
	_inherit = 'product.template'

	generic_name = fields.Char('Generatic Name')
	medicine_type = fields.Selection(
          [('Liquid','Liquid'),('Tablet','Tablet'),('Capsules','Capsules'),('Suppositories','Suppositories'),('Drops','Drops'),('Inhalers','Inhalers'),('Injections','Injections'),('Implants','Implants'),('liquids','liquids')]
              ,string='Medicine Type')
	production_date = fields.Date('Production Date')
	expired_date = fields.Date('Expired Date')
	notes = fields.Text('Notes')
	Medicine_description =fields.Text('Description')
	batch_no = fields.Integer('Batch No')
	components = fields.Text('Compontents')
	concentration = fields.Integer('Concentration')
    # #purchases_price = fields.Monetary('Purchases Price')
    # #selling_pricne = fields.Monetary('Selling Price')
	# barcode = fields.Integer('Barcode')
	parcode_image = fields.Binary('Barcode Image')
	manufauctuer = fields.Many2one('res.partner',domain = [('type','=','manuifuctuer')])
	used_for = fields.Char('Used For : ')
	serial_number = fields.Integer('Serial Number')
	sku = fields.Integer('Stock Keeping Unit')
	suppliers = fields.Many2many('res.partner',relation='medicine_suppliers',domain = [('type','=','supplier')])
    # #patients = fields.Many2many('Patient',relation='medicine_customer')
	can_sold_as_parts = fields.Boolean('Can be sold as parts')
	count_of_parts = fields.Integer('Counts of Parts')
	is_damaged = fields.Boolean('Is Damaged ? :')
	reason_for_damage = fields.Char('Reason for Damage')
	is_expired = fields.Boolean('Is Expired ?')


	@api.onchange('expired_date')
	def check_expired(self):
		if self.expired_date:
			if self.expired_date < datetime.today().date():
				self.is_expired = True
