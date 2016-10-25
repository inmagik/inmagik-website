
SITE_PAGES = {

    'home' : {
        'url' : ''
    },

    'technology' : {
        'url' : 'tech',
    },

    'apps' : {
        'url' : 'apps',
    },

    'web' : {
        'url' : 'web',
    },

    'projects' : {
        'url' : 'projects',
    },

    'project' : {
        'url' : 'projects/(?P<pk>\w+)',
        'template' : 'portfolio-detail.html'
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

    'test-your-site' : {
        'url' : 'test-your-site',
    },



}
