from odoo import models,fields 

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[('patient','Patient'),('admin','Admin'),('doctor','Doctor')
                                           ,('manuifuctuer','Manuifuctuer'),('supplier','Supplier')],
                                           ondelete={'patient':'set default','admin':'set default','doctor':'set default',
                                                      'manuifuctuer':'set default','supplier':'set default'})



    # if it is supplier will have avalible medicine

    # if it is a doctor or  admin should have work time  and days and shift time
     
    #  
