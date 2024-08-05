from odoo import models, fields, api,Command

class ShNewTwo(models.Model):
    _inherit = "sale.order"

    customer_ids = fields.One2many("sh.newway", "field", string="Customer Orders")

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        if self.partner_id:
            record_id = self.partner_id.id
            # records = self.env["sale.order"].search([()])
            records = self.env["sale.order"].search([("partner_id", "=", record_id)])
            for record in records:
                order_lines += [(0, 0, {"field": record.id}) ]
            self.customer_ids = order_lines

# class SaleOrderOption(models.Model):
#     _inherit = 'sale.order'

#     order_history_ids = fields.One2many('sh.invers', 'custom_field_id')

#     @api.onchange('partner_id')
#     def _compute_order_history(self):
#         for order in self:
#             if order.partner_id:
#                 domain = [('order_partner_id', '=', order.partner_id.id), ('state', '!=', 'cancel')]
                
#                 line_ids = self.env['sale.order.line'].search(domain)
#                 print("\n\n\n\n line_ids",line_ids)
#                 invers_records = []
#                 for line in line_ids:
#                     print('line',line)
#                     print(' order',line.order_id)

#                     invers_records.append(Command.create({
#                         'name': line.order_id.name,
#                         'date': order.date_order,
#                         'product': line.product_id.name,
#                         'price': line.price_unit,
#                         'quantity': line.product_uom_qty,
#                         'unit': line.product_uom.name,
#                         'subtotal': line.price_total,
#                         'status': line.state,
#                         'custom_field_id': order.id,
#                     }))
#                 order.order_history_ids = invers_records or False
#             else:
#                 order.order_history_ids = False

  