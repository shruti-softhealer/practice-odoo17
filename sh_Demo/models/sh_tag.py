from odoo import fields,models 

class ShTags(models.Model):
    _name="sh.tag"
    _description="tags"
    _rec_name="tags"


    tags=fields.Char(string="name")
    