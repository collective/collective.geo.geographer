from setuptools import setup, find_packages
import os

version = '1.4'

setup(name='collective.geo.geographer',
      version=version,
      description="Geographic annotation for Plone",
      long_description=open(
              "collective/geo/geographer/README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
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
      install_requires=[
          'setuptools',
          'Plone',
          'simplejson',
          'geopy',
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'tests': [
            'plone.app.testing',
        ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
