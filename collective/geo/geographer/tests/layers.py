# -*- coding: utf-8 -*-
# from plone.testing.zca import EVENT_TESTING

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class GeographerFixture(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # pylint: disable=W0613
        import collective.geo.geographer
        self.loadZCML(package=collective.geo.geographer)
        self.loadZCML(name="test-overrides.zcml",
                    package=collective.geo.geographer.tests)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.geo.geographer:default')


BASE_FIXTURE = GeographerFixture()

INTEGRATION_TESTING = IntegrationTesting(
                                    bases=(BASE_FIXTURE, ),
                                    name="GeographerFixture:Integration")

FUNCTIONAL_TESTING = FunctionalTesting(
                                    bases=(BASE_FIXTURE, ),
                                    name="GeographerFixture:Functional")
