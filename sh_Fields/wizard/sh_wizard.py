from odoo import models , fields,api

class ShProductWizard(models.TransientModel):
    _name="sh.wizard"


    my_product_wizard = fields.Many2one("product.product",string = "MY_PRODUCT")

    
    def Replace_value_with_wizard(self):
        print(f'\n\n\n>>> 11 wizard | {self}:  ')
        print(f'\n\n\n>>> 12 | {self.env.context}:  ')
        recordset = self.env[self.env.context['active_model']].browse(self.env.context['active_id'])
        print(f'\n\n\n>>> 14 | {recordset}:  ')
        if recordset:
            print(f'\n\n\n>>> 18 |Before  Record set id   {recordset.product_id}  :  ')
            print(f'\n\n\n>>> 19 |Before  wizard product  {self.my_product_wizard}:  ')
            recordset.product_uom_qty=10
            
            recordset.product_id=self.my_product_wizard

        print(f'\n\n\n>>> 18 | Record set id   {recordset.product_id}  :  ')
        print(f'\n\n\n>>> 19 | wizard product  {self.my_product_wizard}:  ')

            
       
    
