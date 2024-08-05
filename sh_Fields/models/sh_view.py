from odoo import fields,models 

class ShView(models.Model):
    _name="sh.view"
    _description="view"


    name=fields.Char(string="Name")
    city=fields.Char(string="city")
    state=fields.Char(string="state")
    