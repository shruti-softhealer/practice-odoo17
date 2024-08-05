{
    'name': 'sh_sequence_change',
    'version': '1.2',
    'category': '',
    'summary': 'sh_sequence_change',
    'description': "This module is sh_sequence_change",
    'depends': [
        'base','purchase'
    ],
    'data': [
        # views 
        #'views/',
        'security/ir.model.access.csv', 
        'views/sh_sequence_change_view.xml',   
    ],
    'installable': True,
    'application': True, 

}