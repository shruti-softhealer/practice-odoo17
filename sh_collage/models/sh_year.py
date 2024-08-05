from odoo import fields,models 

class ShYear(models.Model):
    _name="sh.year"
    _description="data of acadamic record"

    name=fields.Char(string="Name")
    year=fields.Selection([
        ('1 st year','1 st year'),
        ('2 st year','2 st year'),
        ('3 st year','3 st year'),
        ('4 st year','4 st year'),
    ],string="Current studing year")
    current_year=fields.Char(string="Year")
    fees=fields.Float(string="Acadamic Fees")
    
    sh_student_line=fields.One2many("sh.student.line","year_id",string="Student line")

    def create_product(self):
        product_name = f"{self.name}"
        print(f'\n\n\n>>> 20 | {self.name}:  ')
        product = self.env['product.product'].search([('name', '=', self.name)])

        if not product:
            product_vals = {
                'name': product_name,
                'type': 'service',
                'list_price': self.fees,
            }
            product = self.env['product.product'].create(product_vals)

        return product

