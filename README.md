Django CMIS Engine
==================

CMIS powered Django ORM Engine backend 

This allows you to access and manipulate content stored within a CMIS 
repository, as if it were a "regular" database. Declaring models using
the CMIS backend is staightforward, you simply inherit from 
`djangocmis.models.Model` and declare the fields in the same way as for
regular models.

django-cmis-engine required Django 1.6.x or 1.7.x.

Configuration
=============

    DATABASES = {
       'default' : {
          'ENGINE' : 'djangocmis.backends.atompub',
          'NAME' : 'my_repository_id',
          'HOST' : 'http://my/atom/binding',
          'USER' : 'username',
          'PASSWORD' : 'password'
       }
    }

Models
======

You need to extend from a different model, in order to pull in the CMIS 
specific functionality. Extend from `djangocmis.models.Model`, and then use
the `db_column` attribute on the field to specify the mapping to the CMIS
attribute.

    class MyCMISThing(djangocmis.models.Model):
       base_path = "/path/to/object/parent"
       cmis_class = "cmis:document"
    
       objectId = CharField(db_column='cmis:objectId', max_length=200, primary_key=True)
       name     = CharField(db_column='cmis:name', max_length=200)
