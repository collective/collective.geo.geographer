import unittest
from Testing import ZopeTestCase as ztc
from collective.geo.geographer.tests.base import FunctionalTestCase


def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.geo.geographer',
            test_class=FunctionalTestCase),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
