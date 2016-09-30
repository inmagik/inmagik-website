#TEMPLATES WILL BE INFERRED BY NAMES

SITE_PAGES = {

    'home' : {
        'url' : ''
    },

    'technology' : {
        'url' : 'tech',
    },

    'projects' : {
        'url' : 'projects',
    },

    'blog' : {
        'url' : 'blog',
    },

    'article' : {
         'url' : 'blog/(?P<pk>\w+)',
         'template' : 'blog-detail.html'
    },

    'contact' : {
        'url' : 'contact',
    },

    'terms-and-condition' : {
        'url' : 'terms-and-condition',
    },

    'copyright-notice' : {
        'url' : 'copy',
    },

    'cookie-policy' : {
        'url' : 'cookie-policy',
    },


    # 'items' : {
    #     'url' : 'items',
    #     'extra_modules' : []
    # },

    # 'item-detail' : {
    #     'url' : 'items/(?P<pk>\w+)',

    # },



}
