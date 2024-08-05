from odoo import fields,models 

class ShFeesState(models.Model):
    _name="sh.fee.status"
    _description="feees status"
    _rec_name="fees_type"

    fees_type=fields.Char(string="Fees status")