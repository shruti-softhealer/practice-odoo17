# from odoo import fields,models,api

# class ShFeesWizard(models.Model):
#     _name="sh.fees.wizard"
#     _description="fees"
#     _rec_name="fees"

#     name_id=fields.Many2one("sh.student.line",string="Name")
#     fees=fields.Float(string="Fees")

#     @api.model_create_multi
#     def create(self,vals_list):
        
#         print("..................self",self)
#         print(".......vals_list:",vals_list)
#         lines = super().create(vals_list)
#         for record in vals_list:
#              self.env['account.move'].create({
#                     'partner_id':record['name_id'],
#                     # 'amount_total_signed':record['fees']
                    
#                 })
#              ids=self.env['account.move'].search([('partner_id','=',record['name_id'])])
#              print(f'\n\n\n>>> 24 | {ids}:  ')
#         return lines
from odoo import api, fields, models

class ShFeesWizard(models.TransientModel):
    _name = 'sh.fees.wizard'
    _description = 'Fees Wizard'

    name = fields.Char('Name', required=True)
    fees = fields.Float('Fees', required=True)
    name_id = fields.Many2one('res.partner', 'Partner')

    def create_product(self):
        product_name = f"{self.name}"
        product = self.env['product.product'].search([('name', '=', self.name)])

        if not product:
            product_vals = {
                'name': self.name,
                'type': 'service',
                'list_price': self.fees,
            }
            product = self.env['product.product'].create(product_vals)

        return product.id

    @api.model_create_multi
    def create(self, vals_list):
        lines = super(ShFeesWizard, self).create(vals_list)

        for record in lines:
            product_id = record.create_product()
            invoice_vals = {
                'partner_id': record.name_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [(0, 0, {
                    'product_id': product_id,
                    'quantity': 1,
                    'price_unit': record.fees,
                })],
            }
            self.env['account.move'].create(invoice_vals)

        return lines

   