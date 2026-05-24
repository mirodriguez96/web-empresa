# DESPLEGAR APP EN PYTHONANYWHERE

import os
import sys
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

path = os.path.expanduser("~/web-empresa")
if path not in sys.path:
    sys.path.insert(0, path)
os.environ["DJANGO_SETTINGS_MODULE"] = "web-empresa.settings"


application = StaticFilesHandler(get_wsgi_application())
