from odoo import fields,models,api

class ShSaleOrder(models.Model):
    _name="sh.sale.order"
    _description="description"

    name=fields.Char(string="Name")
    date=fields.Datetime(string="Date")
    partner_id=fields.Many2one("sh.res.partner",string="Partner")
    order_line_ids=fields.One2many("sh.sale.order.line","order_id",string="Order line")
    add=fields.Many2many("sh.tag",striing="add")
    # final_total=fields.Float("Total",compute="compute_final_total")


 
    # @api.depends('order_line_ids.total')
    # def compute_final_total(self):
    #     print(f'\n\n\n>>> 18 | Final Total:  ') 
    #     print(f'\n\n\n>>> 19 | {self.order_line_ids}  ')
    

    def add_tag(self):
        print(f'\n\n\n>>> 14 | hiiii: ')
        for data in self:
            print(f'\n\n\n>>> 17 | {self}:  ')
            data.add = [(0, 0, {"tags": data.name  + 'ABC'})]
            print(f'\n\n\n>>> 19 | {data.add}:  ')

    def update_tag(self):
        print(f'\n\n\n>>> 21 |  update:  ')
        for data in self:
            new_list=[]
            for tags in data.add:
                new_list.append((1,tags.id,{"tags":data.name+'-'+data.name}))
            data.add=new_list
            print(f'\n\n\n>>> 24 | {data.add}:  ')

    def delete_tag(self):
        print(f'\n\n\n>>> 24 |  delete:  ')
        for data in self:
            for tag in data.add:
                del_list=[(2,tag.id)]
            data.add=del_list
            print(f'\n\n\n>>> 35 | {data.add}:  ')


    def clear_tag(self):
        print(f'\n\n\n>>> 27 |  clear:  ')
        for data in self:
            for tag in data.add:
                clear_list=[(5,tag.id)]
                data.add=clear_list
                print(f'\n\n\n>>> 44 | {data.add}:  ')