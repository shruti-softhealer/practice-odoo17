from odoo import fields,models 

class ShSem(models.Model):
    _name="sh.semdata"
    _description="Type of year "
    _rec_name="year"

    year=fields.Integer(string="Acadamic Year ")