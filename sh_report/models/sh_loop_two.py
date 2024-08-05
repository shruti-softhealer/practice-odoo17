from odoo import fields,models 

class ShLoopsTwo(models.Model):
    _name="sh.loop.two"
    _description="practice all"


    name=fields.Char(string="Name")
    # bill=fields.One2many("sh.bill","bill_id")
    product_name=fields.Many2many("sh.product",string="product name")
    tax_id=fields.Many2one("sh.tax",string="Tax")