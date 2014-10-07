Django CMIS Engine
==================

CMIS powered Django ORM Engine backend 

This allows you to access and manipulate content stored within a CMIS 
repository, as if it were a "regular" database. Declaring models using
the CMIS backend is staightforward, you simply inherit from 
`djangocmis.models.Model` and declare the fields in the same way as for
regular models.

django-cmis-engine requires:
 * Django 1.6.x or 1.7.x.
 * Apache Chemistry cmislib built from trunk

Status
======

Currently, it's possible to fetch objects and read their non-content
properties, but it isn't pretty.... Creating or updating doesn't yet work.

If the `DEBUG` setting is True, then you'll get quite a bit of CMIS related
debug output in your console, sorry about that.

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
    
       name     = CharField(db_column='cmis:name', max_length=200)

The `base_path` is used as the default path in which to fetch objects from,
but can be overriden by passing a parent or path parameter when performing
query operations. See the examples directory for how to use this.

The opaque CMIS Object ID is available via the `object_id` field on
the based model object.

Inspiration
===========

This is inspired by, and partially modelled on the Django LDAP DB 
(django-ldapdb) engine, which is another Django ORM Engine based
on a non-database backend.
