"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

import django
from django.contrib.auth import get_user_model


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.core.management import call_command
call_command('migrate')  # This runs migrations automatically


# Create superuser automatically
User = get_user_model()

SUPERUSER_USERNAME = "admin"
SUPERUSER_EMAIL = "admin@example.com"
SUPERUSER_PASSWORD = "AdminPassword123"


if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    User.objects.create_superuser(
        username="Admin",
        email= "admin@gmail.com",
        password= "adminpassword"
    )
    print("Superuser created successfully!")
else:
    print("Superuser already exists!")



application = get_wsgi_application()
