import unittest
import doctest

from zope.component import eventtesting
from plone.testing import layered
from ..testing import CGEO_GEOGRAPHER_FUNCTIONAL


def setUp(self):  # pylint: disable=W0613
    eventtesting.setUp()


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('README.rst',
                    package='collective.geo.geographer',
                    setUp=setUp,
                ), layer=CGEO_GEOGRAPHER_FUNCTIONAL),
    ])
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
