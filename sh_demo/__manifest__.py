{
    'name': 'sh_product',
    'version': '1.2',
    'category': 'course',
    'summary': 'sh_product',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv' ,
        'views/sh_product_view.xml'
               
    ],
    'installable': True,
    'application': True, 
}
