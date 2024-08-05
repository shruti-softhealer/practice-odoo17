from odoo import models , fields

class Sh(models.Model):
    # _name = "sh.field"
    _description="description "
    _inherit="sale.order"
    
    info = fields.Char(string = "info")