import unittest2 as unittest
import simplejson
from geopy.geocoders.google import GQueryError

from zope.interface import alsoProvides
from zope.component import getUtility

from plone.testing.z2 import Browser
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import setRoles

from collective.geo.geographer.tests.base import test_params
from collective.geo.geographer.interfaces import IGeoreferenceable
from collective.geo.geographer.interfaces import IGeoCoder

from layers import FUNCTIONAL_TESTING


class TestGeocoder(unittest.TestCase):
    layer = FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.oid = self.portal.invokeFactory('Document', 'doc')
        setRoles(self.portal, TEST_USER_ID, ['Member'])

        self.obj = self.portal[self.oid]
        self.geo = getUtility(IGeoCoder)
        alsoProvides(self.obj, IGeoreferenceable)

    def test_geocoder_base(self):
        for item in test_params:
            locations = self.geo.retrieve(item['address'])
            self.assertEquals([loc for loc in locations], item['output'])

    def test_geocoder_error(self):
        self.assertRaises(GQueryError,
                          self.geo.retrieve,
                          "not existent place aklhj asaas")

    def test_geocoder_view(self):
        browser = Browser(self.layer['app'])
        browser.addHeader('Authorization',
                'Basic %s:%s' % (TEST_USER_NAME, TEST_USER_PASSWORD,))

        for item in test_params:
            obj_url = "%s/@@geocoderview?address=%s" % \
                            (self.portal.absolute_url(), item['address'])
            browser.open(obj_url)
            view_contents = simplejson.loads(browser.contents)

            i = 0
            for place, (lat, lon) in view_contents:
                test_place, (test_lat, test_lon) = item['output'][i]
                self.assertEquals(test_place, place)
                self.assertEquals(test_lat, lat)
                self.assertEquals(test_lon, lon)
                i += 1


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeocoder))
    return suite
