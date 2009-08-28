import unittest
from collective.geo.geographer.tests.base import GeographerTestCase
from Products.CMFCore.utils import getToolByName


class TestSetup(GeographerTestCase):

    def afterSetUp(self):
        self.cat = getToolByName(self.portal, 'portal_catalog')
    
    def test_catalog_metadata(self):
        self.failUnless('zgeo_geometry' in self.cat.schema(), self.cat.schema())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
