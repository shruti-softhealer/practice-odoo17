from odoo import fields,models 

class ShBtnWizard(models.TransientModel):
    _name="sh.btn.wizard"
    _description="btn wizard"


    type = fields.Selection(
        string='Payment Type',
        selection=[('cod', 'COD'), ('card', 'CARD')]
    )
    
    total=fields.Char(string="Total")