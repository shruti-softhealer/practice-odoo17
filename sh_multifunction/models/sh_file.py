from odoo import fields,models 
from odoo.tools import html2plaintext

class ShFile(models.Model):
    _inherit="product.template"



    def import_office_manually(self):
        for record in self:
            print(f'\n\n\n>>> 11 | : {record.description} ')
            record.description_sale=html2plaintext(record.description)
            print(f'\n\n\n>>> 13 | : {record.description_sale} ')
           
           








