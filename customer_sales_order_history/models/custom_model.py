from odoo import fields, models, api, Command
from datetime import datetime, timedelta


class SaleOrderOptionInvers(models.Model):
    _name = "sh.invers"

    name = fields.Char(string="Sale Order")
    check = fields.Boolean(string="")
    date = fields.Char(string="Order Date")
    product = fields.Char(string="Product")
    pricelist = fields.Char(string="Pricelist")
    price = fields.Char(string="Price")
    newprice = fields.Float(string="New Price")
    quantity = fields.Char(string="Quantity")
    unit = fields.Char(string="Unit")
    discount = fields.Float(string="Discount")
    subtotal = fields.Char(string="Subtotal")
    status = fields.Char(string="Status")
    custom_field_id = fields.Many2one("sale.order", string="Custom Field")
    
    is_check = fields.Boolean(
        string='is_check',
        compute="compute_is_check"
    )
    def compute_is_check(self):
        self.is_check=self.env.company.reorder
    
    def action_view_order(self):
        print("...............Button clicked...........")
        
        record_id = self.env["sale.order"].search([("name", "=", self.name)])
        # print("record id : ", record_id)
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "sale order",
            "res_model": "sale.order",
            "view_mode": "form",
            "view_id": self.env.ref("sale.view_order_form").id,
            "res_id": record_id.id,
            "target": "current",
        }
       
    def line_record(self):

        pass


    def action_reorder(self):
        pass
        print(f'\n\n\n>>> 42 | {self.name}:  ')
        new_sale_order = self.env['sale.order'].create({
            # 'partner_id': self.custom_field_id.partner_id.id,  
            'date_order': fields.Datetime.now(),
            'order_line': [(0, 0, {
                'product_id': self.env['product.product'].search([('name', '=', self.product)], limit=1).id,
                'price_unit': self.price,
                'product_uom_qty': float(self.quantity),
                'product_uom': self.env['uom.uom'].search([('name', '=', self.unit)], limit=1).id,
                'discount': self.discount,
            })],
})

        

class SaleOrderOption(models.Model):
    _inherit = "sale.order"

    order_history_ids = fields.One2many("sh.invers", "custom_field_id")



    @api.onchange("partner_id")
    def _compute_order_history(self):
        # showing record
        last_record=self.env.company.last_no_order
        # stages record
        stages_record=self.env.company.stages
        stage_list=[]
        
        for record in stages_record:
            if record.name =='Quotation':
                stage_list.append('draft')
            if record.name =='Quotation Sent':
                stage_list.append('sent')
            if record.name =='Sales Order':
                stage_list.append('sale') 
            if record.name =='Cancelled':
                stage_list.append('cancel')
            print(f'\n\n\n>>> 81 | {record.name}:  ')
        # days record
        days_settings_value = self.env.company.last_no_days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_settings_value)

        print(f'\n\n\n>>> 84 | {start_date}:  ')
        print(f'\n\n\n>>> 77 | {stages_record}:  ')
        for order in self:
            if order.partner_id:
                # domain = [("order_partner_id", "=", order.partner_id.id),]
                line_ids = self.env["sale.order.line"].search([
                    ("order_partner_id", "=", order.partner_id.id),
                ])

                print("\n\n\n\n line_ids", line_ids)
                invers_records = []

                for line in line_ids:
                    # print("line", line)

                    print(" order", line.order_id)
                    # date conditions 3 day ago date to  end date- tilldate
                    if start_date.date()<=  line.order_id.date_order.date() <= end_date.date():
                        print("line", line)
                        # stage in record checking in list
                        if line.state in stage_list:
                            if len(invers_records)<last_record:
                                invers_records.append(
                                    Command.create(
                                        {
                                            "name": line.order_id.name,
                                            "date": line.order_id.date_order,
                                            "product": line.product_id.name,
                                            "price": line.price_unit,
                                            "quantity": line.product_uom_qty,
                                            "unit": line.product_uom.name,
                                            "subtotal": line.price_total,
                                            "status": line.state,
                                            "custom_field_id": order.id,
                                        }
                                    )
                                )
                order.order_history_ids = invers_records or False
            else:
                order.order_history_ids = False
