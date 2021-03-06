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

import django
from cmislib import CmisClient

from django.db.backends import (BaseDatabaseClient, BaseDatabaseIntrospection,
                                BaseDatabaseFeatures, BaseDatabaseOperations,
                                BaseDatabaseValidation, BaseDatabaseWrapper)
from django.db.backends.creation import BaseDatabaseCreation

#############################################################################

def complain(*args, **kwargs):
    raise Exception("Sorry, that isn't supported for CMIS")

def todo(*args, **kwargs):
    raise Exception("Sorry, that feature still needs to be implemented")

def ignore(*args, **kwargs):
    pass

#############################################################################

class DatabaseClient(BaseDatabaseClient):
    runshell = complain

class DatabaseCreation(BaseDatabaseCreation):
    create_test_db = ignore
    destroy_test_db = ignore

class DatabaseIntrospection(BaseDatabaseIntrospection):
    get_table_list = complain
    get_table_description = complain
    get_relations = complain
    get_indexes = complain
    get_key_columns = complain

#############################################################################

class DatabaseCursor(object):
    def __init__(self, cmis_connection):
        self.connection = cmis_connection

class DatabaseFeatures(BaseDatabaseFeatures):
    can_introspect_decimal_field = False
    can_introspect_positive_integer_field = False
    can_introspect_small_integer_field = False
    supports_transactions = False 

class DatabaseOperations(BaseDatabaseOperations):
    compiler_module = "djangocmis.backends.compiler"

    def quote_name(self, name):
        return name

class DatabaseWrapper(BaseDatabaseWrapper):
    vender = "cmis"
    operators = {}

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

        self.charset = "utf-8"
        self.features = DatabaseFeatures(self)
        self.ops = DatabaseOperations(self)
        self.client = DatabaseClient(self)
        self.creation = DatabaseCreation(self)
        self.introspection = DatabaseIntrospection(self)
        self.validation = BaseDatabaseValidation(self)

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def ensure_connection(self):
        if self.connection is None:
           self.cmis_client = CmisClient(
                 self.settings_dict['HOST'],
                 self.settings_dict['USER'],
                 self.settings_dict['PASSWORD'],
                 binding=self.cmis_binding()
           )
           repo_name = self.settings_dict['NAME']
           if repo_name == "default" or not repo_name:
              self.connection = self.cmis_client.defaultRepository
           else:
              self.connection = self.cmis_client.getRepository(repo_name)
           if django.conf.settings.DEBUG:
              print "Connected to Repository with ID %s" % self.connection.id

    def _commit(self):
        pass

    def _by_path(self, path):
        self.ensure_connection()
        return self.connection.getObjectByPath(path)

    def _cursor(self):
        self.ensure_connection()
        return DatabaseCursor(self.connection)

    def _query(self, query):
        self.ensure_connection()
        return self.connection.query(query)

    def _rollback(self):
        pass

    # TODO Add the others
