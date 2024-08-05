from odoo import fields,models,api 
from odoo.exceptions import ValidationError

class ShConstrains(models.Model):
    _name="sh.constrain"
    _description="contrains demostration"
    _rec_name="product_name"
    _inherit=['mail.thread','mail.activity.mixin']
    

    # name=fields.Many2one("res.partner",string="name")
    name=fields.Char(string="Name")
    date=fields.Date(string="Date")
    amount=fields.Float(string="Amount")
    product_name=fields.Char(string="Product Name")
    description=fields.Text(string="Product Description")
    
    # sql constraints
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name must be unique!')
    ]

    # python side  adding constrains
    @api.constrains('date','product_name','description','amount')
    def _contrains_code(self):
         for record in self:
            
            if record.date<fields.Date.today():
                raise ValidationError('Date can not be set in past')
            if record.product_name == record.description:
                raise ValidationError('Product Name and Product Description can not be same ')
            if record.amount<0.0:
                raise ValidationError('Amount can not be Negative')
            print(f'\n\n\n>>> 25 | {self}:  ')
            return self
         
    def action_send_email(self):
        mail_template = self.env.ref('sh_constrain.sh_student_mail_view')
        mail_template.send_mail(self.id, force_send=True)