# -*- coding: utf-8 -*-
{
    'name': "Dynamic snippet",
    
    'summary':"""        
        Website snippet to highlight top partners.
    """,
        
    'description': """ customizable snippet for highlighting partners on the website.  """,

    'author': "Salma Mohamed",
    'category': 'Website',
    'version': '17.0.1.2',
    'depends': ['base','website','crm','contacts'],
    

    'data': [
              'views/snippets/s_res_partner.xml',
              'views/snippets/options.xml',
              'views/res_partner_views.xml',

    ],
    'assets': {
        'web.assets_frontend':[
            'test_highlight_partners/static/src/snippets/s_res_partner.css',
            'test_highlight_partners/static/src/snippets/s_res_partner.js',

        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
   # 'post_init_hook': '_post_init_hook',
   #  "uninstall_hook": 'uninstall_hook',
}
