import simplejson
from geopy import geocoders
from geopy.geocoders.google import GQueryError

from zope.interface import implements
from zope.component import getUtility
from Products.Five.browser import BrowserView

from collective.geo.geographer.interfaces import IGeoCoder


def get_geocoder():
    return GeoCoderUtility()


class GeoCoderUtility(object):
    """Wrapper class for geopy
    """
    implements(IGeoCoder)

    def retrieve(self, address=None, google_api=None):
        if google_api:
            self.geocoder = geocoders.Google(str(google_api))
        else:
            self.geocoder = geocoders.Google()

        if not address:
            raise GQueryError
        return self.geocoder.geocode(address, exactly_one=False)


class GeoCoder(object):

    def __init__(self, context):
        self.context = context

    def retrieve(self, address=None, google_api=None):
        import warnings
        import textwrap
        warnings.warn(textwrap.dedent(
            "IGeoCoder adapter is deprecated" \
            " use corresponding utility instead"
        ), DeprecationWarning, 2)
        geocoder = GeoCoderUtility()
        return geocoder.retrieve(address, google_api)


class GeoCoderView(BrowserView):
    """A simple view which provides a json
    output from geopy query
    """

    def __init__(self, context, request):
        super(GeoCoderView, self).__init__(context, request)
        self.geocoder = getUtility(IGeoCoder)

    def __call__(self, address=None, google_api=None):
        try:
            locations = self.geocoder.retrieve(address)
        except GQueryError:
            return 'null'
        return simplejson.dumps([loc for loc in locations])
