from odoo import fields,models,api

class ShCrm(models.Model):
    _inherit="crm.lead"

    sequence=fields.Char(string="sequence" ,readonly=True)



    @api.model_create_multi
    def create(self, vals_list):
        print(f'\n\n\n>>> 20 |create_self {self}:   ')
        print(f'\n\n\n>>> 21 | create_vals_list {vals_list}:  ')
        for record in vals_list:
            print(f'\n\n\n>>> 23 |val_list_record {record}:  ')
            record['sequence']=self.env['ir.sequence'].next_by_code('crm.seq')
            # record['sequence']=record['name']
        lines = super().create(vals_list)
        return lines
    
    
    # def get_total_leads(self):
    #     total_leads = self.env['crm.lead'].search_count([])
    #     return total_leads
    # def write(self, vals):
    #     if 'sequence' not in vals:
    #         vals['sequence'] = self.env['ir.sequence'].next_by_code('crm.seq')
    #     result = super().write(vals)
    #     return result


