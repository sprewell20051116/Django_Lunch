from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wvp9bbglf7(#8wsbrm*im6$u*sr#%xf^oa!n7f5n_ff$3328at'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}