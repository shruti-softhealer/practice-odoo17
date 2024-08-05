from odoo import fields,models 

class ShShowHide(models.Model):
    _name="sh.show.hide"
    _description="show hide"


    # type=fields.Many2one("sh.type.two",string="Type")
    
    type_two = fields.Selection(
        string='type',
        selection=[('teacher', 'Teacher'), ('student', 'Student')]
    )
    
    student_name=fields.Char(string="student name")
    div=fields.Char(string="Division")
    enroll=fields.Char(string="Enroll Number")

    teacher_name=fields.Char(string="teacher name")
    subject=fields.Char(string="subject")
    teacher_class=fields.Char(string="class")
