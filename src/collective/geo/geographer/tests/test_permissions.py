from collective.geo.geographer.testing import CGEO_GEOGRAPHER_INTEGRATION
from operator import itemgetter
from unittest import TestCase


class TestViewPermissionRegression(TestCase):

    layer = CGEO_GEOGRAPHER_INTEGRATION

    def test_view_permission(self):
        # The message-id of the translated title of the "View" permission
        # is "view-permission".
        # The literal "view-permission" should never be listed
        # in manage_access, only "View" should.
        # Loading the ZCML in a wrong way results in having both registered,
        # which is wrong.

        app = self.layer['portal']

        # contains a list of tuples, e.g.
        # ('Modify portal content', (), ('Editor'))
        permission_tuples = app.ac_inherited_permissions(1)

        permission_names = map(itemgetter(0), permission_tuples)

        self.assertNotIn(
            'view-permission', permission_names,
            'The string "view-permission" should never be in manage_acces.'
            ' Something went wrong while loading ZCML.')
