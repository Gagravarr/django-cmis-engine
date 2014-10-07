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

from django.db.backends import (BaseDatabaseFeatures, BaseDatabaseOperations,
                                BaseDatabaseWrapper)
from django.db.backends.creation import BaseDatabaseCreation

class DatabaseCreation(BaseDatabaseCreation):
    def create_test_db(self, *args, **kwargs):
       "Not supported, sorry"
       pass
    def destroy_test_db(self, *args, **kwargs):
       "Not supported, sorry"
       pass

class DatabaseCursor(object):
    def __init__(self, cmis_connection):
        self.connection = cmis_connection

class DatabaseFeatures(BaseDatabaseFeatures):
    def __init__(self, connection):
        self.connection = connection
        self.supports_transactions = False

class DatabaseOperations(BaseDatabaseOperations):
    compiler_module = "djangocmis.backends.compiler"

    def quote_name(self, name):
        return name

class DatabaseWrapper(BaseDatabaseWrapper):
    vender = "cmis"

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

        self.charset = "utf-8"
        self.creation = DatabaseCreation(self)
        self.features = DatabaseFeatures(self)
        self.ops = DatabaseOperations(self)
        self.settings_dict['SUPPORTS_TRANSACTIONS'] = False

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def ensure_connection(self):
        if self.connection is None:
           # TODO
           pass

    def _commit(self):
        pass

    def _cursor(self):
        self.ensure_connection()
        return DatabaseCursor(self.connection)

    def _rollback(self):
        pass

    # TODO Add the others
