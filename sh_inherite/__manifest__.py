{
    'name': 'sh_inherite',
    'version': '1.2',
    'category': 'course',
    'summary': 'sh_inherite',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base','mail','sale'
    ],
    'data': [
        'wizard/sh_wizard_view.xml',
        'wizard/sh_btn_wizard_view.xml',
        'views/sh_custom_view.xml',
        'views/sh_product_view.xml',
        'views/sh_order_line_view.xml',
        'views/sh_fields_view.xml',
        'report/report.xml',
        'security/ir.model.access.csv',
       
               
    ],
    # 'assets': {
    #     'web.report_assets_common': [
    #         'sh_practice_wizard/static/src/style/report_style.css',
    #     ],
    # },
    'installable': True,
    'application': True, 
}
