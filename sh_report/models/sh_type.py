from odoo import fields,models 

class ShType(models.Model):
    _name="sh.type"
    _description="description"


    product_type=fields.Char(string="Product type")
    dom=fields.Date(string="Date of manufacture")
    doe=fields.Date(string="Date of expied")
    
    pro_id=fields.Many2one("sh.product")