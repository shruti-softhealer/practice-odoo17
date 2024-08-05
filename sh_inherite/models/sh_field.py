from odoo import models , fields

class Sh(models.Model):
    _description="description"
    _inherit="sale.order"
    
    info = fields.Char(string = "info")

    def action_confirm(self):
        print(f'\n\n\n>>> 10 | {self}:  ')
        res=super().action_confirm()
        print(f'\n\n\n>>> 10 | CONFIRM BUTTON:  ')
        return res