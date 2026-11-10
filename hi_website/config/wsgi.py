"""
WSGI config for hi_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# This file lives in hi_website/config/. Vercel imports it from the repository
# root, so that folder is not on the path and "import config" fails.
_SITE_ROOT = Path(__file__).resolve().parent.parent
if str(_SITE_ROOT) not in sys.path:
    sys.path.insert(0, str(_SITE_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
