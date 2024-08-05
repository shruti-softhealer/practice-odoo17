from odoo import models , fields,api

class ShOrderLine(models.Model):
    _inherit="sale.order.line"
    
    my_product = fields.Char(string = " HI")

