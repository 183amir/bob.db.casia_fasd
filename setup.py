#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Sex 10 Ago 2012 14:22:33 CEST

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='xbob.db.casia_fasd',
    version='1.1.1',
    description='CASIA Face Anti-Spoofing Database Access API for Bob',
    url='http://pypi.python.org/pypi/xbob.db.casia_fasd',
    license='GPLv3',
    author='Andre Anjos, Ivana Chingovska',
    author_email='andre.anjos@idiap.ch, ivana.chingovska@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    namespace_packages = [
      'xbob',
      'xbob.db',
      ],

    install_requires=[
      'setuptools',
      'six',
      'bob >= 1.1.0',
      'antispoofing.utils < 2.0.0',
    ],

    entry_points={

      # declare the database to bob
      'bob.db': [
        'casia_fasd = xbob.db.casia_fasd.driver:Interface',
        ],

      # declare tests to bob
      'bob.test': [
        'casia_fasd = xbob.db.casia_fasd.test:FASDDatabaseTest',
        ],

      # antispoofing database declaration
      'antispoofing.utils.db': [
        'casia_fasd = xbob.db.casia_fasd.spoofing:Database',
        ],
      },

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
      ],

)
