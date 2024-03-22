from pathlib import Path

from decouple import config
from split_settings.tools import include

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Build paths inside the project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

# Include the base settings file
include('base.py')

# Include the environment-specific settings file based on the environment
if config('DJANGO_ENV') == 'Development':
    include('development.py')
elif config('DJANGO_ENV') == 'Production':
    include('production.py')
