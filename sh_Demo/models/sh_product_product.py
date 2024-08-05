from odoo import fields,models 

class ShProductProduct(models.Model):
    _name="sh.product.product"
    _description="description"


    name=fields.Char(string="Product Name")
    