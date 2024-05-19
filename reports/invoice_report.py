from odoo import fields,models,api

class CustomInvoiceReport(models.AbstractModel):
    _name = 'report.trial.report_invoice_report'




    def _get_report_values(self,docids,data):
        report = self.env['ir.actions.report']._get_report_from_name('trial.report_invoice_report')

        selected_modules = self.env['ir.module.module'].browse(docids)
        print("======================================================================================================")
        print("======================================================================================================")

        print("======================================================================================================")

        print("======================================================================================================")

        print("======================================================================================================")

        print("======================================================================================================")

        print("======================================================================================================")

        # for wizard in obj:
            # print("wizard wizard",wizard)
            # for partner in wizard.partner_ids:
            #     accountMove = self.env['account.move'].search([('partner_id','=',partner)])
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("======================================================================================================")
            #     print("======================================================================================================")

            #     print("======================================================================================================")

            #     print("======================================================================================================")

            #     print("======================================================================================================")

            #     print("======================================================================================================")

            #     print("======================================================================================================")
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)
            #     print("accountMove",accountMove)

        return {
            'lines': docids.get_lines(),
            'selected_modules' : selected_modules,
            #'obj':obj,
            #'wizard':wizard,
            #'partner':partner
        }