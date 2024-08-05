from odoo import fields,models 

class ShTypeTwo(models.Model):
    _name="sh.type.two"
    _description="sh student or teacher type"
    _rec_name="type"


    type=fields.Char(string="Type")