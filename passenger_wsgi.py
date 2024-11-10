import os
import sys

# Update path to match your WHC username
path = '/home/fifps320/public_html/Linkedin'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'Linkedin.settings'

# Import the Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 