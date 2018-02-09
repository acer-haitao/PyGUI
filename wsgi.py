"""
WSGI config for StuProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os,sys

path = '/home/haitao/WorkSpace/DjangoWeb'
if path not in sys.path:
    sys.path.insert(0,'/home/haitao/WorkSpace/DjangoWeb/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StuProject.settings")

application = get_wsgi_application()
