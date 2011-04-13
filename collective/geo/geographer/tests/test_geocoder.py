import unittest
import simplejson
from geopy.geocoders.google import GQueryError

from zope.interface import alsoProvides

from Testing.testbrowser import Browser
from Products.PloneTestCase.setup import portal_owner
from Products.PloneTestCase.setup import default_password

from collective.geo.geographer.tests.base import FunctionalTestCase
from collective.geo.geographer.tests.base import test_params
from collective.geo.geographer.interfaces import IGeoreferenceable
from collective.geo.geographer.interfaces import IGeoCoder


class TestGeocoder(FunctionalTestCase):

    def afterSetUp(self):
        self.oid = self.folder.invokeFactory('Document', 'doc')
        self.obj = self.folder[self.oid]
        self.geo = IGeoCoder(self.obj)
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
        browser = Browser()
        browser.addHeader('Authorization',
                          'Basic %s:%s' % (portal_owner, default_password))

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
