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

_ContentField_name = "cmis:contentStream"
class ContentField(fields.Field):
   "A CMIS Content Stream"
   name = "cmis:contentStream"
   def __init__(self, *args, **kwargs):
      super(ContentField, self).__init__(*args, **kwargs)
      self.name = _ContentField_name
      self.db_column = self.name
      self.verbose_name = self.name
      self.rel = None
      self.default = None
      self._choices = []
      self.primary_key = False
   pass

_CMISObjectField_name = "cmis:object"
class CMISObjectField(fields.Field):
   "Special field to hold the CMIS Object from cmislib"
   def __init__(self, *args, **kwargs):
      kwargs["db_column"] = _CMISObjectField_name
      super(CMISObjectField, self).__init__(*args, **kwargs)
      #self.db_column = self.name
      #self.verbose_name = self.name
      #self.rel = None
      #self.default = None
      #self._choices = []
      #self.primary_key = False

class ParentField(fields.Field):
   "Special field for representing the parent of a model"
   pass

# TODO The rest
