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

from django.db.models.sql.datastructures import Col
from django.db.models.lookups import Exact
import django
import djangocmis.models

class SQLCompiler(object):
    def __init__(self, query, connection, using):
        self.query = query
        self.connection = connection
        self.using = using

    def has_parent(self, node):
        if isinstance(node, Exact):
           if isinstance(node.rhs, djangocmis.models.Model):
              return node.rhs
        return None

    def compile(self, node):
        if isinstance(node, Col):
           return node.target.column, []
        elif isinstance(node, Exact):
           if isinstance(node.lhs, Col):
              return "%s = '%s'" % (node.lhs.target.column, node.rhs), []
           raise Exception("Don't know how to handle %s -> %s" % (node.lhs, node.rhs))
        else:
           return node.as_sql(self, self.connection)

    def results_iter(self):
        "Runs the query, and return an iterator of the results"

        # Does it have a path restriction in the query already?
        parent = self.has_parent(self.query.where)
        if parent:
           parent_id = parent.object_id
        else:
           parent_obj = self.connection._by_path(self.query.model.base_path)
           parent_id = parent_obj.id
           if django.conf.settings.DEBUG:
              print "Found parent at %s as %s" % (self.query.model.base_path, parent_obj)
        extra_where = "IN_FOLDER('%s')" % parent_id

        # Decide on the main filter
        filterstr = 'select * from %s where ' % self.query.model.cmis_class
        where, w_params = self.compile(self.query.where)
        filterstr += where

        # Add the path restriction
        filterstr += " AND %s" % extra_where

        # Query
        results = self.connection._query(filterstr)

        # Work out how to return it
        if len(self.query.select):
           fields = [x.field for x in self.query.select]
        else:
           fields = self.query.model._meta.fields
        attrs = [f.db_column for f in fields if f.db_column]
        for result in results:
            props = result.getProperties()
            row = []
            for attr in attrs:
                row.append(props[attr])
            yield row
