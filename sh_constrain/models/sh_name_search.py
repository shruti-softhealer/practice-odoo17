from odoo import fields,models,api 

class ShSearch(models.Model):
    _name="sh.search"
    _description="name search"


    partner_id=fields.Many2one("res.partner",string="Name")


class ResPartner(models.Model):
   _inherit = 'res.partner'

   @api.model
   def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None,order=None,):
       args = list(args or [])
       if name:
           args += ['|', '|', ('name', operator, name), ('email', operator, name),
                    ('phone', operator, name)]
           return self._search(args, limit=limit, access_rights_uid=name_get_uid)

