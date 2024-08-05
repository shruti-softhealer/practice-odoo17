from odoo import fields, models


# class ShSettings(models.TransientModel):
#     _inherit = "res.config.settings"

#     last_no_order = fields.Integer(string="Last No. of Order")
#     last_no_days = fields.Integer(string="Last No. of Day's Order")
#     reorder = fields.Boolean(string="Enable Reorder" )
#     stages = fields.Many2many(
#      'sh.selection',
        
#         string='Stages',
#     )

class ShCompany(models.Model):
    _inherit = "res.company"
    last_no_order = fields.Integer(string="Last No of Order")
    last_no_days = fields.Integer(string="Last No of day's order")
    reorder = fields.Boolean(string="Reorder")
    stages = fields.Many2many('sh.selection',string='Stages')



class ShSettings(models.TransientModel):
    _inherit = "res.config.settings"

    last_no_order = fields.Integer(
        related="company_id.last_no_order", string="Last No of Order", readonly=False
    )
    last_no_days = fields.Integer(
        related="company_id.last_no_days",
        string="Last No of day's order",
        readonly=False,
    )
    reorder = fields.Boolean(
        related="company_id.reorder", string="Reorder", readonly=False
    )

    stages = fields.Many2many('sh.selection',  related="company_id.stages",string='Stages',readonly=False)




class Selection(models.Model):
    _name="sh.selection"
    _rec_name="name"

    name=fields.Char(string="str")

#     state = fields.Selection(
#         selection=[
#     ('Quotation', "Quotation"),
#     ('Quotation Sent', "Quotation Sent"),
#     ('Sales Order', "Sales Order"),
#     ('Cancelled', "Cancelled"),
# ],
#         )  