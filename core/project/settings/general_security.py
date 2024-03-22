from core.project.settings import ENV

# Axes Settings
SILENCED_SYSTEM_CHECKS = ENV.config('SILENCED_SYSTEM_CHECKS', cast=ENV.csv())
# Number of failed login before block
AXES_FAILURE_LIMIT = ENV.config('AXES_FAILURE_LIMIT', cast=int)
# Time to wait after lockout(hrs)
AXES_COOLOFF_TIME = ENV.config('AXES_COOLOFF_TIME', cast=int)
# Enable security lockout only for admin site
AXES_ONLY_ADMIN_SITE = ENV.config('AXES_ONLY_ADMIN_SITE', cast=bool)
# Form field that contains your users usernames.
AXES_USERNAME_FORM_FIELD = ENV.config('AXES_USERNAME_FORM_FIELD')
# Reset after success login
AXES_RESET_ON_SUCCESS = ENV.config('AXES_RESET_ON_SUCCESS', cast=bool)
# Whitelist local host
AXES_NEVER_LOCKOUT_WHITELIST = ENV.config('AXES_NEVER_LOCKOUT_WHITELIST', cast=bool)
AXES_IP_WHITELIST = ENV.config('AXES_IP_WHITELIST', cast=ENV.csv())
# Enable writing login failure logs to database
AXES_ENABLE_ACCESS_FAILURE_LOG = ENV.config('AXES_ENABLE_ACCESS_FAILURE_LOG', cast=bool)
# Successful login will reset the number of failed logins
AXES_RESET_ON_SUCCESS = ENV.config('AXES_RESET_ON_SUCCESS', cast=bool)
# lock user using ip address, username and user agent
AXES_LOCKOUT_PARAMETERS = ENV.config('AXES_LOCKOUT_PARAMETERS', cast=ENV.csv())

# captcha settings
RECAPTCHA_PUBLIC_KEY = ENV.config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = ENV.config('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_REQUIRED_SCORE = ENV.config('RECAPTCHA_REQUIRED_SCORE', cast=float)
