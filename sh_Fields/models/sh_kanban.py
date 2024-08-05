from odoo import models , fields,api

class ShKanban(models.Model):
    _inherit="product.template"
    
    my_product = fields.Char(default = "PRODUCT ")

    def Product_Button(self):
        print(f'\n\n\n>>> 9 | hiii:  ')