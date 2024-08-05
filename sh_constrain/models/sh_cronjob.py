from odoo import fields,models,api

class ShCronjob(models.Model):
    _name="sh.cron"
    _description="cron description"

    name=fields.Char(string="Name")
    name_id=fields.Char(string="Id")
    name_id_two=fields.Char(string="Id two:")
    # partner_id=fields.Many2one("res.partner")

    @api.model 
    def cron_function(self):
        print(f'\n\n\n>>> 12 | hiii :  ')

    @api.model_create_multi
    def create(self, vals_list):
        print(f'\n\n\n>>> 20 |create_self {self}:   ')
        print(f'\n\n\n>>> 21 | create_vals_list {vals_list}:  ')
       
        for record in vals_list:
            print(f'\n\n\n>>> 23 |val_list_record {record}:  ')
            record['name_id']=self.env['ir.sequence'].next_by_code('sh.cron.1')
            record['name_id_two']=self.env['ir.sequence'].next_by_code('sh.cron.2')

        lines = super().create(vals_list)
        return lines
    