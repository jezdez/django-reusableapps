====================================
Reusable Django apps with setuptools
====================================

This is yet another approach on enabling Django to load reusable, pluggable,
egg-based applications without changing the Django sourcecode. Think of
plugins or components, e.g. django-registration, django-voting or django-tagging.

It uses setuptools for finding, handling and loading egg-based Python modules
with a certain "entry point" (``'django.apps'``).

Egg-based Python modules (a.k.a. eggs) are compressed packaged Python modules
like Django apps. Every Django app can be converted to an egg distribution by
using a special setup.py file.

Installation
============

Get the source from the application site at::

    http://code.google.com/p/django-reusableapps/

To install *reusableapps*, follow these steps:

1. Follow the instructions in the `INSTALL file`_.
2. Add ``import reusableapps`` to the top of your `settings file`_.
3. Add a new setting to your `settings file`_, a list of locations of
   reusable apps, in search order. Note that these paths should use
   Unix-style forward slashes, even on Windows.
   
   For example::
   
     REUSABLE_APPS_DIRS = (
         '/home/jannis/django/reusable_apps',
         '/usr/share/django/apps',
         'C:/www/django/apps'
     )
   
4. Add to the last line of your settings file (after the INSTALLED_APPS_ 
   and REUSABLE_APPS_DIRS setting)::
   
     INSTALLED_APPS = reusableapps.search(REUSABLE_APPS_DIRS, INSTALLED_APPS)

Putting it together
-------------------

Once you finished with above installation instructions, your `settings file`_
should look something like this::

    REUSABLE_APPS_DIRS = (
        '/home/jannis/django/reusable_apps',
        '/usr/share/django/apps',
        'C:/www/django/apps',
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'myproject.myapp',
    )

    INSTALLED_APPS = reusableapps.search(REUSABLE_APPS_DIRS, INSTALLED_APPS)

You can then put reusable, pluggable, egg-based Django apps in one of the
directories in ``REUSABLE_APPS_DIRS``.

Using templates from egg-based Django apps
------------------------------------------

If you want to use templates from a egg-based Django app please add
``'django.template.loaders.eggs.load_template_source'`` to the TEMPLATE_LOADERS_
setting.

.. _INSTALL file: http://django-reusableapps.googlecode.com/svn/trunk/INSTALL.rst
.. _settings file: http://docs.djangoproject.com/en/dev/ref/settings/
.. _INSTALLED_APPS: http://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
.. _TEMPLATE_LOADERS: http://docs.djangoproject.com/en/dev/ref/settings/#template-loaders

Adding support for reusable applications to your own Django app
===============================================================

If you want to support django-reusableapps in your own Django app, you need
to modify your existing setup.py to import the setup function from the
setuptools instead the from the distutils::

    from setuptools import setup

Furthermore you need to add an 'entry point' to the setup keywords::

    entry_points={'django.apps': 'myapp = myapp'},

where my ``myapp`` is the name of your Django app, e.g. ``registration``.
A full example can be found at setup-example.py_ and should be copied to
the parent directory of your app as ``setup.py``.

.. _setup-example.py: http://django-reusableapps.googlecode.com/svn/trunk/docs/setup-example.py

Building egg-based Django apps
==============================

Once you have a proper setup.py in the parent directory of your Django app,
you can run::

    python setup.py bdist_egg

to build a egg file of it. It will be created in the ``dist`` directory and
have a filename like ``dummyapp-0.1-py2.5.egg``. You can then distribute it
and use it by placing it in one of the ``REUSABLE_APPS_DIRS`` of your Django
project.

Support
=======

Please leave your `questions and problems`_ on the `designated Google Code site`_.

.. _designated Google Code site: http://code.google.com/p/django-reusableapps/
.. _questions and problems: http://code.google.com/p/django-reusableapps/issues/
