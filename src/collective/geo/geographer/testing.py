# -*- coding: utf-8 -*-
import collective.geo.geographer
import pkg_resources
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

try:
    pkg_resources.get_distribution('plone.app.contenttypes')
except pkg_resources.DistributionNotFound:
    BASES = None
else:
    from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
    BASES = (PLONE_APP_CONTENTTYPES_FIXTURE, )


CGEO_GEOGRAPHER = PloneWithPackageLayer(
    bases=BASES,
    zcml_package=collective.geo.geographer,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.geo.geographer:default',
    name="CGEO_GEOGRAPHER")

CGEO_GEOGRAPHER_INTEGRATION = IntegrationTesting(
    bases=(CGEO_GEOGRAPHER, ),
    name="CGEO_GEOGRAPHER_INTEGRATION")

CGEO_GEOGRAPHER_FUNCTIONAL = FunctionalTesting(
    bases=(CGEO_GEOGRAPHER, ),
    name="CGEO_GEOGRAPHER_FUNCTIONAL")
