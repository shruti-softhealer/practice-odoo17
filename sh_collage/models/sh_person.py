from odoo import models,fields,api
from odoo.exceptions import UserError

class ShPerson(models.Model):
    _name="sh.person"
    _description="General Informations"
    _rec_name="name"


    name=fields.Char(string="Name")
    surname=fields.Char(string="Surname")
    display_name=fields.Char(string="Display name")
    type_id=fields.Many2one("sh.type",string="Type")
    mobile=fields.Char(string="Mobile Number" ,default="")
    email=fields.Char(string="Email")
    city=fields.Char(string="City")
    state=fields.Char(string="State")
    dob=fields.Date(string="Date of Birth")
    hobbies=fields.Many2many("sh.hobby",string="Hobbies")
    

    @api.model_create_multi
    def create(self,vals_list):
        print("..................self",self)
        print("..................vals_list:",vals_list)
        for record in vals_list:
            exist = self.env['res.partner'].search([('phone','=',record['mobile'])])
            
            if not exist:
                self.env['res.partner'].create({
                    'name':record['name'] ,
                    'phone':record['mobile'],
                    'mobile':record['mobile'],
                    'email':record['email']  
                })
                lines = super().create(vals_list)

            else:
                raise UserError("User already exist")

        return lines