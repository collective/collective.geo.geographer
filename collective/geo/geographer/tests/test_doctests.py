import unittest2 as unittest
import doctest

from zope.component import eventtesting
from plone.testing import layered
from layers import FUNCTIONAL_TESTING


def setUp(self):  # pylint: disable=W0613
    eventtesting.setUp()


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('README.txt',
                    package='collective.geo.geographer',
                    setUp=setUp,
                ), layer=FUNCTIONAL_TESTING),
    ])
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
