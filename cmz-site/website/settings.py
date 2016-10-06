import os
SETTINGS_FOLDER = os.path.dirname(__file__)

LANGUAGES = [
    ('it', 'Italiano'),
    ('en', 'English'),
]

LANGUAGE_CODE = 'it'


#LANGUAGE_SELECTORS = ['prefix'] # 'query_string', 'cookie', 'header', ...


SITE_MODULES = [
    'cms_content',
    'cmz_files',
    'cms_news',
    'cms_cookieconsent',
    'cmz_translations',
    'cmz_blog',
    'cmz_portfolio',
    'technologies',

    'cmz_jwt_auth',

]


COOKIECONSENT_OPTIONS = {
    "message" : "Questo sito web utilizza cookies per garantirti la miglior esperienza utente.",
    "theme" : "dark-bottom",
    "link" : "cookie-policy",
    "dismiss" : "OK",
    "learnMore" : "Maggiori informazioni"
}


try:
    from .secrets import *
    AWS_S3_BUCKET_NAME = "inmagikweb"
    AWS_REGION = "eu-central-1"
    AWS_S3_GZIP = True
    #DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage".
except:
    raise


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter'
    )
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
}
