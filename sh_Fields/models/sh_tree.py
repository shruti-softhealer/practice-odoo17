from odoo import models , fields

class ShTree(models.Model):
    # _name = "sh.field"
    _inherit="sale.order"
    
    my_product = fields.Char(string = "Product info")

   