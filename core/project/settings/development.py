from decouple import Csv, config

from core.project.settings import BASE_DIR

# Secrete key
SECRET_KEY = config('SECRET_KEY')

# Allowed Host
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

# Debug
DEBUG = config('DEBUG')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Security Settings In Production Environment
X_FRAME_OPTIONS = 'DENY'
