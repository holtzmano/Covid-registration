import os

APP_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_DIRS = [
    os.path.join(APP_PATH, 'templates/'),
]

TEMPLATES = [
    {
        # Template backend to be used, For example Jinja
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(APP_PATH, 'templates/'),
        ],
        'APP_DIRS': True,

        # options to configure
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]