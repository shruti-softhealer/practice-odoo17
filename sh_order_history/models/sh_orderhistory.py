from odoo import fields,models ,api

class ShOrderHistory(models.Model):
    _inherit="sale.order"

    # customer_ids=fields.One2many("sale.order","partner_id",string="customer ids",compute="show_data")

    
    # @api.depends('partner_id')
    # def show_data(self):
    #     print(f'\n\n\n>>> 14 | {self.partner_id.id}:  ')
    #     record_id=self.partner_id.id 
    #     self.customer_ids=self.env['sale.order'].search([("partner_id","=",record_id)]) 




   
    # def btn_show(self):
    #     print("...............Button clicked...........")
    #     self.ensure_one() 
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'sale order',
    #         'res_model': 'sale.order',
    #         'view_mode': 'form',
    #         'view_id': self.env.ref('sale.view_order_form').id,
    #         'res_id': self.id,
    #         'target': 'current',
    #     }
       
