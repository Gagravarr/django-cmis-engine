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

import django.db.models
from djangocmis.models.fields import CharField, ParentField, CMISObjectField

class Model(django.db.models.base.Model):
   """
   Base class for all CMIS backed Models.
   """

   # Common fields
   object_id = CharField(db_column="cmis:objectId", max_length=200, primary_key=True)
   cmis_object = CMISObjectField()
   parent = ParentField()

   # Metadata
   cmis_class = None
   base_path = None

   def __init__(self, *args, **kwargs):
       super(Model, self).__init__(*args, **kwargs)
       self.saved_pk = self.pk

   class Meta:
       abstract = True

