from odoo import models,fields,api 

class ShSaleOrderLine(models.Model):
    _name="sh.sale.order.line"
    _description="description"


    name=fields.Char(string="Name")
    product_id=fields.Many2one("sh.product.product",string="product")
    qty=fields.Integer(string="Qty")
    price=fields.Float(string="Price")
    tax_ids=fields.Many2many("sh.account.tax")
    total=fields.Float(string="Total Rs: ",compute="total_price")
    order_id=fields.Many2one("sh.sale.order")
    # concat_name=fields.Many2many("sh.sale.order")

    @api.depends('qty', 'price', 'tax_ids')
    def total_price(self):
        for record in self:
            base_total = record.qty * record.price
            tax_total = 0.0

            for tax in record.tax_ids:
                tax_amount = (base_total * tax.name) / 100
                tax_total += tax_amount

            record.total = base_total + tax_total