{
    'name': 'sh_collage',
    'version': '0.0.1',
    'category': 'course',
    'summary': 'sh_collage',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base','account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sh_type_view.xml',
        'views/sh_person_view.xml',
        'views/sh_semdata_view.xml',
        'views/sh_fees_state_view.xml',
        'views/sh_student_line_view.xml',
        'views/sh_year_view.xml',
        'wizard/sh_fees_wizard_view.xml'
        

               
    ],
    'installable': True,
    'application': True, 
}
