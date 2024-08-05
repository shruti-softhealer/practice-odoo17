from odoo import fields,models 

class ShType(models.Model):
    _name="sh.type"
    _description="Type of person"
    _rec_name="type"

    type=fields.Char(string="Type")
  