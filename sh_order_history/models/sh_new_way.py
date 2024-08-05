from odoo import fields, models,api

class ShNew(models.Model):
    _name = "sh.newway"
    _description = "New Way"

    field = fields.Many2one("sale.order", string="Sale Order")
    order_name = fields.Char(related='field.name', string="Order Reference", readonly=True)
    partner_id = fields.Many2one(related='field.partner_id', string="Customer", readonly=True)
    date_order = fields.Datetime(related='field.date_order', string="Order Date", readonly=True)
    state = fields.Selection(related='field.state', string="Status", readonly=True)




# from odoo import fields,models,api

# class ShNew(models.Model):
#     _name="sh.newway"
#     _description=" wayy"



#     field=fields.Many2one("sale.order")



# class ShNewTwo(models.Model):
#     _inherit="sale.order"


#     customer_ids=fields.One2many("sh.newway","field",string="customer ids")


#     @api.onchange("partner_id")
#     def create_record(self):
#         record_id = self.partner_id.id
#         records = self.env["sale.order"].search([("partner_id", "=", record_id)])
#         print("records : ", records)
#         for record in records:
#             print(f'\n\n\n>>> 25 | {record.id}:  ')
#             partner = self.env['sale.order'].browse(record.id)
#             print(f'\n\n\n>>> 26 partner id| {partner}:  ') 

#             self.env["sh.newway"].create({"field": record.id})
           

    

# from odoo import fields, models,api

# class ShNew(models.Model):
#     _name = "sh.newway"
#     _description = "New Way"

#     field = fields.Many2one("sale.order", string="Sale Order")
#     order_name = fields.Char(related='field.name', string="Order Reference")
#     partner_id = fields.Many2one(related='field.partner_id', string="Customer")
#     date_order = fields.Datetime(related='field.date_order', string="Order Date")
#     state = fields.Selection(related='field.state', string="Status")
#     amount_total = fields.Monetary(related='field.amount_total', string="Total Amount")

# class ShNewTwo(models.Model):
#     _inherit = "sale.order"

#     customer_ids = fields.One2many("sh.newway", "field", string="Customer Orders")

#     @api.onchange("partner_id")
#     def _onchange_partner_id(self):
#         if self.partner_id:
#             records = self.env["sale.order"].search([("partner_id", "=", self.partner_id.id)])
#             order_lines = []

#             for record in records:
#                 order_lines.append((0, 0, {"field": record.id}))

#             self.customer_ids = order_lines


# from odoo import fields,models,api,Command

# class SaleOrderOptionInvers(models.Model):
#     _name = 'sh.invers'

#     name = fields.Char(string="Sale Order")
#     date = fields.Char(string="Order Date")
#     product = fields.Char(string="Product")
#     pricelist = fields.Char(string="Pricelist")
#     price = fields.Char(string="Price")
#     newprice = fields.Float(string="New Price")
#     quantity = fields.Char(string="Quantity")
#     unit = fields.Char(string="Unit")
#     discount = fields.Float(string="Discount")
#     subtotal = fields.Char(string="Subtotal")
#     status = fields.Char(string="Status")
#     custom_field_id = fields.Many2one('sale.order', string="Custom Field")




    

    