from zope.component import eventtesting
from Products.Five import zcml
from Products.Five import fiveconfigure

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

# from collective.geo.geographer.interfaces import IGeoCoder
from collective.geo.geographer.geocoder import GeoCoder
from geopy.geocoders.google import GQueryError


@onsetup
def setup():
    """Set up the additional products required for the Pleiades site policy.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    fiveconfigure.debug_mode = True
    import collective.geo.geographer
    zcml.load_config('configure.zcml', collective.geo.geographer)
    import collective.geo.geographer.tests
    zcml.load_config('test.zcml', collective.geo.geographer.tests)

    fiveconfigure.debug_mode = False

setup()
ptc.setupPloneSite(products=['collective.geo.geographer', ])


test_params = [{'address': "Torino Italy",
                'output': [(u'Turin, Italy',
                                (45.070562099999997, 7.6866186000000001))]},
               {'address': "Serravalle Italy",
                 'output': [(u'Serravalle di Chienti Macerata, Italy',
                                    (43.075758700000002, 12.957291700000001)),
                    (u'46030 Serravalle a Po Mantua, Italy',
                                    (45.071769699999997, 11.0986653)),
                    (u'Serravalle, 50019 Sesto Fiorentino Florence, Italy',
                                    (43.847528799999999, 11.2683242)),
                    (u'Serravalle, 12026 Piasco Cuneo, Italy',
                                    (44.5675697, 7.4256900000000003)),
                    (u'Serravalle, 06046 Norcia Perugia, Italy',
                                    (42.785488399999998, 13.022334499999999)),
                    (u'Serravalle, 54023 Filattiera Massa-Carrara, Italy',
                                    (44.367425699999998, 9.9383029000000001)),
                    (u'Serravalle, Berra Ferrara, Italy',
                                    (44.967833300000002, 12.044703699999999)),
                    (u'Serravalle, Asti, Italy',
                                    (44.947478799999999, 8.1465417999999996)),
                    (u'Serravalle, Bibbiena Arezzo, Italy',
                                    (43.7736485, 11.8429064)),
                    (u'Serravalle, 38061 Ala Trento, Italy',
                                    (45.811786499999997, 11.0141562))]}]


class DummyGeoCoder(GeoCoder):

    def retrieve(self, address = None, google_api = None):
        for item in test_params:
            if address == item['address']:
                return item['output']
        raise GQueryError


class TestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """


class FunctionalTestCase(ptc.FunctionalTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """

    def setUp(test):
        super(FunctionalTestCase, test).setUp()
        eventtesting.setUp()

    def afterSetUp(test):
        lpf = test.portal.portal_types['Topic']
        lpf.global_allow = True
