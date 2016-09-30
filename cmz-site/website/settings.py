#IDEAS

# Languages: tuples with code/name and options
# FIRST ONE IS THE BASE ONE

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
    "link" : "/example-cookie-policy/",
    "dismiss" : "OK!",
    "learnMore" : "More Info"
}
