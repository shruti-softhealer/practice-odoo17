from odoo import fields,models 

class ShTax(models.Model):
    _name="sh.tax"
    _description="tax"
    

    tax=fields.Float(string="Tax")