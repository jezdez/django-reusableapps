import os
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

app_name = 'reusableapps'
version = '0.1.1'

setup(name='django-'+app_name,
      version=version,
      description='Reusable Django apps with setuptools',
      long_description=open('docs/overview.rst').read(),
      author='Jannis Leidel',
      author_email='jannis@leidel.info',
      url='http://code.google.com/p/django-%s/' % app_name,
      packages=['reusableapps'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
