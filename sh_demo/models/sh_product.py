from odoo import fields,models

class ShProduct(models.Model):
    _name="sh.product"
    _description="this is a product "

    product_name=fields.Char(string="Product")
    product_description=fields.Text(string="Product Details")
    product_price=fields.Float(string="Product price")
    