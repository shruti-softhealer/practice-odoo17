from odoo import fields,models 

class ShLoop(models.Model):
    _name="sh.loop"
    _description="loops"


    name=fields.Char(string="Name")
    price=fields.Integer(string="Price")
    product = fields.Char(string = "Product")
    description=fields.Char(string="Description")
    qty=fields.Integer(string="Qty")
    image=fields.Binary(string="image")
    tax_ids=fields.Many2many("sh.tax",string="Tax")