from odoo import fields,models 

class ShResPartner(models.Model):
    _name="sh.res.partner"
    _description="description"

    name=fields.Char(string="Name")
    city=fields.Char(string="City")
