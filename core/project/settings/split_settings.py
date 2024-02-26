from decouple import config
from split_settings.tools import include

# Include the base settings file
include('base.py')

# Include the environment-specific settings file based on the environment
if config('DJANGO_ENV') == 'Development':
    include('development.py')
elif config('DJANGO_ENV') == 'Production':
    include('production.py')
