# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yzdx8kn2)rnsa3a2a%__r9ys(9+4*xz0n1d49^#!pslh%v3t*v'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'capstone_database',
        'USER': 'root',
        'PASSWORD': 'SoftwareDeveloper101!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}