from odoo import fields,models ,api

class ShSequence(models.Model):
    _inherit="purchase.order"

    sequence=fields.Char(string="sequence")


    def button_confirm(self):
        print(f'\n\n\n>>> 10 | {self}:  ')
        for record in self:
            record['sequence']=record['name']
            # purchase.order has sequence of purchase default model
            record['name']=self.env['ir.sequence'].next_by_code('purchase.order')
        print(f'\n\n\n>>> 10 | CONFIRM BUTTON:  ')
        res=super().button_confirm()
        return res

    @api.model_create_multi
    def create(self, vals_list):
        print(f'\n\n\n>>> 20 |create_self {self}:   ')
        print(f'\n\n\n>>> 21 | create_vals_list {vals_list}:  ')
        for record in vals_list:
            print(f'\n\n\n>>> 23 |val_list_record {record}:  ')
            record['name']=self.env['ir.sequence'].next_by_code('rfq.seq')
            record['sequence']=record['name']
        lines = super().create(vals_list)
        return lines
    
