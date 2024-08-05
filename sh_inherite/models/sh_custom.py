from odoo import fields,models 
class ShCustom(models.Model):
    _name="sh.custom"
    _description="custom"


    info = fields.Char(string = "info")
    my_product = fields.Char(string = " HI")


