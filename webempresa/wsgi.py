# DESPLEGAR APP EN PYTHONANYWHERE

import os
import sys
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

# Raiz donde va el proyecto y se encuentra el archivo manage.py
path = os.path.expanduser("~/web-empresa")
if path not in sys.path:
    sys.path.insert(0, path)

# nombre del proyecto
os.environ["DJANGO_SETTINGS_MODULE"] = "webempresa.settings"


application = StaticFilesHandler(get_wsgi_application())
