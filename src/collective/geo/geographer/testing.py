# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.geo.geographer


CGEO_GEOGRAPHER = PloneWithPackageLayer(
    bases=(PLONE_APP_CONTENTTYPES_FIXTURE, ),
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
