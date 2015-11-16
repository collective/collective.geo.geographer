# -*- coding: utf-8 -*-
import unittest
from Products.CMFCore.utils import getToolByName

from ..testing import CGEO_GEOGRAPHER_INTEGRATION


class TestSetup(unittest.TestCase):
    layer = CGEO_GEOGRAPHER_INTEGRATION

    def setUp(self):
        self.cat = getToolByName(self.layer['portal'], 'portal_catalog')

    def test_catalog_metadata(self):
        schema = self.cat.schema()
        self.assertTrue('zgeo_geometry' in schema, schema)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
