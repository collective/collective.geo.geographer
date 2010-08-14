import unittest

from Testing import ZopeTestCase as ztc

# from Products.Five import zcml
# from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
# from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

# import collective.geo.geographer
from collective.geo.geographer.tests.base import FunctionalTestCase

# class TestCase(ptc.PloneTestCase):
#     class layer(PloneSite):
#         @classmethod
#         def setUp(cls):
#             fiveconfigure.debug_mode = True
#             zcml.load_config('configure.zcml',
#                              collective.geo.geographer)
#             fiveconfigure.debug_mode = False
# 
#         @classmethod
#         def tearDown(cls):
#             pass


def test_suite():
    return unittest.TestSuite([

        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.geo.geographer',
            test_class=FunctionalTestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
