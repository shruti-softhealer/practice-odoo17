from odoo import fields,models 

class ShProduct(models.Model):
    _name="sh.product"
    _description="product"
    _rec_name="product"

    product = fields.Char(string = "Product")
    description=fields.Char(string="Description")
    qty=fields.Integer(string="Qty")
    price=fields.Float(string="Price")
    image=fields.Binary()
    tax_ids=fields.Many2one("sh.tax",string="Tax")
    type_ids=fields.One2many("sh.type","pro_id",string="Type")
    bill_id=fields.Many2one("sh.bill")