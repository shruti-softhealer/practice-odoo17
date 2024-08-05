from odoo import fields,models 

class ShInherit(models.Model):
    _inherit="sale.order"


    info=fields.Char(string="Info.")