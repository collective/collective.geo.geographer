# -*- coding: utf-8 -*-
import unittest2 as unittest
from Products.CMFCore.utils import getToolByName

from layers import INTEGRATION_TESTING


class TestSetup(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.cat = getToolByName(self.layer['portal'], 'portal_catalog')

    def test_catalog_metadata(self):
        schema = self.cat.schema()
        self.assertTrue('zgeo_geometry' in schema, schema)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
