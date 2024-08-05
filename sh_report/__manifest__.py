{
    'name': 'sh_report',
    'version': '1.2',
    'category': 'report ',
    'summary': 'sh_report',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base','sale'
    ],
    'data': [
        'views/sh_product_view.xml',
        'report/sh_reportt.xml',
        'views/sh_bill_view.xml',
        'views/sh_loop_view.xml',
        'views/sh_loop_two_view.xml',
        'views/sh_type_view.xml',
        'views/sh_inherit_report_view.xml',
        'views/sh_show_hide_view.xml',
        'views/sh_typetwo.xml',
        'security/ir.model.access.csv' ,

               
    ],
    'installable': True,
    'application': True, 
}
