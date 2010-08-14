import unittest
import simplejson
from geopy.geocoders.google import GQueryError

from zope.interface import alsoProvides

from Products.Five.testbrowser import Browser
from Products.PloneTestCase.setup import portal_owner
from Products.PloneTestCase.setup import default_password

from collective.geo.geographer.tests.base import FunctionalTestCase
from collective.geo.geographer.interfaces import IGeoreferenceable
from collective.geo.geographer.geocoder import GeoCoder


test_params = [{'address': "Torino Italy",
                'output' : [(u'Turin, Italy', (45.070562099999997, 7.6866186000000001))]},
               {'address': "Serravalle Italy",
                 'output': [(u'Serravalle di Chienti Macerata, Italy', (43.075758700000002, 12.957291700000001)),
                    (u'46030 Serravalle a Po Mantua, Italy', (45.071769699999997, 11.0986653)),
                    (u'Serravalle, 50019 Sesto Fiorentino Florence, Italy', (43.847528799999999, 11.2683242)),
                    (u'Serravalle, 12026 Piasco Cuneo, Italy', (44.5675697, 7.4256900000000003)),
                    (u'Serravalle, 06046 Norcia Perugia, Italy', (42.785488399999998, 13.022334499999999)),
                    (u'Serravalle, 54023 Filattiera Massa-Carrara, Italy', (44.367425699999998, 9.9383029000000001)),
                    (u'Serravalle, Berra Ferrara, Italy', (44.967833300000002, 12.044703699999999)),
                    (u'Serravalle, Asti, Italy', (44.947478799999999, 8.1465417999999996)),
                    (u'Serravalle, Bibbiena Arezzo, Italy', (43.7736485, 11.8429064)),
                    (u'Serravalle, 38061 Ala Trento, Italy', (45.811786499999997, 11.0141562))]}]


class TestGeocoder(FunctionalTestCase):

    def afterSetUp(self):
        self.geo = GeoCoder()
        self.oid = self.folder.invokeFactory('Document', 'doc')
        self.obj = self.folder[self.oid]
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
            obj_url = "%s/@@geocoderview?address=%s" % (self.obj.absolute_url(), item['address'])
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
