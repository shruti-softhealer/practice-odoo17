{
    'name': 'sh_order_history',
    'version': '1.2',
    'category': '',
    'summary': 'sh_order_history',
    'description': "This module is sh_order_history",
    'depends': [
        'base','sale'
    ],
    'data': [
        # views 
        #'views/',
        'security/ir.model.access.csv',
        'views/sh_orderhistory.xml',    
        'views/sh_settings_view.xml',
    ],
    'installable': True,
    'application': True, 

}