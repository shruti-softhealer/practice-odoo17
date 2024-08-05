from odoo import fields,models 

class ShStudentLine(models.Model):
    _name="sh.student.line"
    _description="student details"
    _rec_name="name_id"


    name_id=fields.Many2one("sh.person",string="Name")
    fees_state=fields.Selection([
        ('not paid','not paid'),
        ('paid',' paid'),
        ('partialy paid','partialy paid')

    
    ],string="Fees status")
    year_id=fields.Many2one("sh.year")