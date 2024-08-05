from odoo import fields,models 

class ShBill(models.Model):
    _name="sh.bill"
    _description="bill"


    name=fields.Char(string="Name")
    address=fields.Char(string="Address")
    date=fields.Date(string="Date")
    reference=fields.Char(string="Refrence")
    sales_person=fields.Char(string="Sales person")
    payment_term=fields.Char(string="Payment Term")

    bill_ids=fields.One2many("sh.product","bill_id")