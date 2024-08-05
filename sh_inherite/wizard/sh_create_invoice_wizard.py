from odoo import fields,models 

class ShBtnWizard(models.TransientModel):
    _name="sh.btn.wizard"
    _description="btn wizard"

    
    create_invoice = fields.Selection(
        string='create_invoice',
        selection=[('cod', 'COD'), ('card', 'CARD')]
    )
    total=fields.Integer(string="Total")