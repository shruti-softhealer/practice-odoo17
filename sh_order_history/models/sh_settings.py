from odoo import fields,models 

class ShSettings(models.TransientModel):
    _inherit="res.config.settings"

    last_no_order=fields.Integer(string="Last No of Order")
    stages=fields.Many2many("sale.order",string="Stages")
    last_no_days=fields.Integer(string="Last No of day's order")