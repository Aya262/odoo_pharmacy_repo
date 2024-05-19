from odoo import models,fields,api
from datetime import datetime , date

class AccountMoveWizard(models.TransientModel):
    _name = 'trial.account.move.wizard'

    partner_ids = fields.Many2many(comodel_name='res.partner')
    invoice_type = fields.Selection([('Invoice','Invoice'),('Refund','Refund'),('both','Both')],string='Invoice Type' , default='both')
    start_date = fields.Date('Start Date' ,default=datetime.today())
    end_date = fields.Date('End Date', default=datetime.today())

    payment_status = fields.Selection([('Paid','Paid'),('Not Paid','Not Paid'),('both','Both')],'Payment Status',default='Not Paid')
    due_status = fields.Selection([('Due','Due'),('Over Due','Over Due'),('both','Both')],'Due Status',default='Over Due')

    journal_ids = fields.Many2many('account.journal')


    def get_multi_pdf(self):
        partner_ids=self.partner_ids
        for partner in partner_ids:
            self.pdf_print((partner.id))

    def pdf_print(self,partner_id):
        #print("self.read()[0]",self.read()[0])
        #data= self.read()[0]
    

        #partner_id=self.read()[0]['partner_ids'][0]
        account_move= self.env['account.move'].search([('partner_id','=',partner_id),('move_type','in',self.move_type()),('invoice_date','>=',self.start_date),('invoice_date','<=',self.end_date)
                                                       ,('payment_state','in',self.get_payment_state()),('invoice_date_due',self.get_due_status(),date.today())])
        print("account_move",account_move)
        move_list = []
        totals=0
        amount_due=0
        for move in account_move:
            move_result={'partner_id':move.partner_id.name,
                         'Date':move.invoice_date,
                         'Invoice_Number':move.name,
                         'Reference':move.payment_reference,
                         'Due_Date':move.invoice_date_due,
                         'Status':move.payment_state,
                         'Total':move.amount_total,
                         'Amount_Due':move.amount_residual}
            totals+=move.amount_total
            amount_due+=move.amount_residual
            move_list.append(move_result)
        
        print("move_list",move_list)
        
        target_moves = []

        if self.invoice_type !='both':
            target_moves.append(self.invoice_type)
        else:
            target_moves.extend(('Invoice','Refund'))

        if self.payment_status !='both':
            target_moves.append(self.payment_status)
        else:
            target_moves.extend(('Paid','Not Paid'))

        if self.due_status !='both':
            target_moves.append(self.due_status)
        else:
            target_moves.extend(('Due','Over Due'))
        
        data={
            'model': 'trial.account.move.wizard',
            'form': self.read()[0],
            'moves':move_list,
            'time_now':datetime.now().strftime("%Y-%m-%d %H:%M"),
            'current_company': self.env.user.company_id.name,
            'start_date':self.start_date.strftime("%Y-%m-%d"),
            'end_date':self.end_date.strftime("%Y-%m-%d"),
            'target_moves':','.join(target_moves),
            'partner':self.partner_ids[0].name,
            'totals':totals,
            'amount_due':amount_due,
        }
        return self.env.ref('trial.invoice_report_pdf').report_action(self,data=data)
    

    def move_type(self):
        if self.invoice_type=='Invoice':
            return ['out_invoice']
        elif self.invoice_type=='Refund':
            return ['out_refund']
        else:
            return ['out_refund','out_invoice']
        
    def get_payment_state(self):
        if self.payment_status == 'Paid':
            return ['paid']
        elif self.payment_status =='not_paid':
            return ['not_paid']
        else:
            return ['paid','not_paid']
        

    def get_due_status(self):

        if self.due_status=='Due':
            return '='
        elif self.due_status=='Over Due':
            return '<'
        else:
            return '<='


        
    




