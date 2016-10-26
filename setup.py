from setuptools import setup, find_packages
import os

version = '2.1'
install_requires = [
    'setuptools',
    'Products.CMFCore'
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
          "src/collective/geo/geographer/README.rst").read() + "\n" + open(
              os.path.join("docs", "CONTRIBUTORS.txt")).read() + "\n" + open(
                  os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Framework :: Plone",
          "Topic :: Internet",
          "Topic :: Scientific/Engineering :: GIS",
          "Programming Language :: Python",
      ],
      keywords='Zope Plone GIS KML Google Maps Bing OpenLayers',
      author='Giorgio Borelli',
      author_email='giorgio@giorgioborelli.it',
      url="http://plone.org/products/collective.geo",
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.geo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'test': [
              # see. PLONE_APP_CONTENTTYPES_FIXTURE
              'plone.app.testing [robot]',
              'plone.app.robotframework [debug, reload] > 0.9.8'
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
