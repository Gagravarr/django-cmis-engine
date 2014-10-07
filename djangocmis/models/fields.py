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

from django.db.models import fields, SubfieldBase

class CharField(fields.CharField):
    def __init__(self, *args, **kwargs):
        if not 'max_length' in kwargs:
           kwargs['max_length'] = 200
        super(CharField, self).__init__(*args, **kwargs)

# TODO The rest
