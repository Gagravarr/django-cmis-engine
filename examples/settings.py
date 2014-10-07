#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

"""
Test Django Settings, used to allow you to run the examples
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path = [BASE_DIR] + sys.path

# Dummy security key and logging
SECRET_KEY = 'spw7u)avoq8(4(3d##-rsuo_xd!pxkcc+f$1awbqjass3u4$dh'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# Dummy apps definitions
INSTALLED_APPS = ()
MIDDLEWARE_CLASSES = ()
#ROOT_URLCONF = 'examples.urls'
#WSGI_APPLICATION = 'examples.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Import the database to use
from settings_alfresco import *
