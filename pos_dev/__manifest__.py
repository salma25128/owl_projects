{
    'name': 'pos',
    'installable':True,
    'application':True,
'depends': ['point_of_sale'],
    'author':'Salma Mohamed',

    'data': [

    ],
    'assets': {
        'web.assets_qweb':[
            'pos_dev/static/src/xml/pos_edits.xml'

        ],
        'web.assets_backend': [
            'pos_dev/static/src/js/pos_edits.js',
        ],
    },
}