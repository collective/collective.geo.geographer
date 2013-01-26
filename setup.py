from setuptools import setup, find_packages
import os

version = '1.5dev'
install_requires = [
    'setuptools',
    'Plone',
    'geopy',
]

# Test if we have built-in JSON - Python 2.6+, 3.0+.
# Older Python versions require simplejson.
try:
    import json  # pylint: disable=W0611
except ImportError:
    install_requires.append('simplejson')

setup(name='collective.geo.geographer',
      version=version,
      description="Geographic annotation for Plone",
      long_description=open(
          "collective/geo/geographer/README.rst").read() + "\n" + open(
              os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Framework :: Plone",
          "Topic :: Internet",
          "Topic :: Scientific/Engineering :: GIS",
          "Programming Language :: Python",
      ],
      keywords='Zope Plone GIS KML Google Maps Bing Yahoo OpenLayers',
      author='Giorgio Borelli',
      author_email='giorgio@giorgioborelli.it',
      url="http://plone.org/products/collective.geo",
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.geo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'test': [
              'plone.app.testing',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
