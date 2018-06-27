# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='annotationz',
    version='0.0.1',
    description='Annotation module for ALKIS Ontology',
    long_description=readme,
    author='Edward Dinu',
    author_email='edward.dinu@fokus.fraunhofer.com',
    url='https://github.com/edward18/annotationz',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

