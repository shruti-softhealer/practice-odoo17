{
    'name': 'sh_Fields',
    'version': '1.2',
    'category': 'fields',
    'summary': 'sh_Fields',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base','sale','product'
    ],
    'data': [
         # views 
        'security/ir.model.access.csv',     
        'wizard/sh_wizard_view.xml',
        'views/sh_view_view.xml',
        'views/sh_order_line_view.xml',
        'views/sh_fields_view.xml',
        # 'views/sh_kanban_view.xml',

               
    ],
    'installable': True,
    'application': True, 
}
