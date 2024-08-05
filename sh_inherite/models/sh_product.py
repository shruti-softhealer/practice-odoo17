from odoo import fields,models 

class ShProduct(models.Model):
    # _name="sh.product"
    _description="product"
    _inherit="product.template"

    description=fields.Text(string="Product Description")