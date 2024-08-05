{
    'name': 'sh_constrain',
    'version': '1.2',
    'category': '',
    'summary': 'sh_constrain',
    'description': "This module is sh_constrain",
    'depends': [
        'base','mail'
    ],
    'data': [
        'security/ir.model.access.csv',     
        # views 
        'views/sh_basic_constrain.xml',
        'demo/mail_template.xml',
        'demo/demo_data.xml',
        'views/sh_cronjob_view.xml',
        'views/sh_search_name_view.xml',


    ],
    'installable': True,
    'application': True, 

}