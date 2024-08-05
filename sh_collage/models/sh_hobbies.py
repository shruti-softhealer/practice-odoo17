from odoo import fields,models 

class ShHobbies(models.Model):
    _name="sh.hobby"
    _description="hobbies description"
    _rec_name="hobbies"

    hobbies=fields.Char(string="Hobbies")