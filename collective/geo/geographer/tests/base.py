from zope.component import eventtesting
from Products.Five import zcml
from Products.Five import fiveconfigure

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup():
    """Set up the additional products required for the Pleiades site policy.
    
    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    fiveconfigure.debug_mode = True
    import collective.geo.geographer
    zcml.load_config('configure.zcml', collective.geo.geographer)
    fiveconfigure.debug_mode = False

setup()
ptc.setupPloneSite(products=['collective.geo.geographer','zgeo.geographer'])

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
        lpf_allow = lpf.global_allow
        lpf.global_allow = True
