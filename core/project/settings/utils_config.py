from core.project.settings import BASE_DIR, ENV, PROJECT_DIR

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = f'{BASE_DIR}/static'
STATICFILES_DIRS = [f'{PROJECT_DIR}/static']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# # Media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = f'{BASE_DIR}/media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email settings
EMAIL_BACKEND = ENV.config('EMAIL_BACKEND')
EMAIL_PORT = ENV.config('EMAIL_PORT')
EMAIL_HOST = ENV.config('EMAIL_HOST')
EMAIL_HOST_USER = ENV.config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = ENV.config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = ENV.config('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = ENV.config('SERVER_EMAIL')
EMAIL_SUBJECT_PREFIX = ENV.config('EMAIL_SUBJECT_PREFIX')
EMAIL_USE_TSL = ENV.config('EMAIL_USE_TSL')
