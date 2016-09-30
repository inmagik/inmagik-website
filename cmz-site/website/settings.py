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
    'cms_news',
    'cms_cookieconsent',
    'cmz_translations',
    'cmz_blog',
    'technologies',

]


COOKIECONSENT_OPTIONS = {
    "message" : "This is a custom message from CMZ!",
    "theme" : "dark-bottom",
    "link" : "cookie-policy",
    "dismiss" : "OK!",
    "learnMore" : "More Info"
}


try:
    from .secrets import *
    AWS_S3_BUCKET_NAME = "inmagikweb"
    AWS_REGION = "eu-central-1"
    AWS_S3_GZIP = True
    #DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage".
except:
    raise
