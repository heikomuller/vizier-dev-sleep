#! /usr/bin/env python

from setuptools import setup

setup(
    name='vizierdev-sleep',
    version='0.1.0',
    description='Module for Vizier workflows that pauses execution for a given period of time',
    keywords='data curation, vizier ',
    license='apache-2.0',
    packages=['vizierdev_sleep'],
    package_data={'': ['LICENSE']},
)
