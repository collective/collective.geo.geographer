from zope.component import eventtesting
from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup():
    """Set up the additional products required for the Pleiades site policy.
    
    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    # Load the ZCML configuration for the optilux.policy package.
    
    fiveconfigure.debug_mode = True
    import collective.geo.geographer
    zcml.load_config('configure.zcml', collective.geo.geographer)
    fiveconfigure.debug_mode = False
    
    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML.
    
    ## Plone don't like this
    #ztc.installPackage('zgeo.geographer') 
    #ztc.installPackage('collective.geo.geographer')
    
# The order here is important: We first call the (deferred) function which
# installs the products we need for the Pleiades package. Then, we let 
# PloneTestCase set up this product on installation.

setup()
ptc.setupPloneSite(products=['collective.geo.geographer','zgeo.geographer'])

class GeographerTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """

class GeographerFunctionalTestCase(ptc.FunctionalTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """
    
    def setUp(test):
        super(GeographerFunctionalTestCase, test).setUp()
        eventtesting.setUp()

    def afterSetUp(test):
        lpf = test.portal.portal_types['Topic']
        lpf_allow = lpf.global_allow
        lpf.global_allow = True
