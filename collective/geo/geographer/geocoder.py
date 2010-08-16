import simplejson
from geopy import geocoders
from geopy.geocoders.google import GQueryError

from Products.Five.browser import BrowserView


class GeoCoder(object):
    """Wrapper class for geopy"""
    def __init__(self, google_api = None):
        if google_api:
            self.geocoder = geocoders.Google(str(google_api),
                                           output_format='json')
        else:
            self.geocoder = geocoders.Google(output_format='json')

    def retrieve(self, address = None):
        if not address:
            raise GQueryError

        return self.geocoder.geocode(address, exactly_one=False)


class GeoCoderView(BrowserView):

    def __init__(self, context, request):
        super(GeoCoderView, self).__init__(context, request)
        self.geocoder = GeoCoder()

    def __call__(self, address = None):
        try:
            locations = self.geocoder.retrieve(address)
        except GQueryError:
            return 'null'
        return simplejson.dumps([loc for loc in locations])
