AUTHENTICATION_BACKENDS = [
    'apps.base.utils.backends.CustomBackend',
]

# AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = 'token_obtain_pair'
# LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'token_obtain_pair'