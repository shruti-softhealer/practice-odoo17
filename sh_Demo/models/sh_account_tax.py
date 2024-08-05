from odoo import fields,models 

class ShAccountTax(models.Model):
    _name="sh.account.tax"
    _description="description"


    name=fields.Integer(string="Tax")
    # color=fields.Integer(string="Colour")