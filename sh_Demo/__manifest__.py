{
    'name': 'sh_Demo',
    'version': '1.2',
    'category': 'course',
    'summary': 'sh_Demo',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv' ,
        'views/sh_sale_order_view.xml',
        'views/sh_product_product_view.xml',
        'views/sh_res_partner_view.xml',
        'views/sh_sale_order_line_view.xml',
        # 'views/sh_fees_view.xml',
        # 'views/sh_dupe_view.xml'

               
    ],
    'installable': True,
    'application': True, 
}
