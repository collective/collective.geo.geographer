from zope.interface import implements

from Products.Five.browser import BrowserView

from collective.geo.geographer.interfaces import IGeoreferenceable
from collective.geo.geographer.interfaces import IGeoView


class GeoView(BrowserView):
    implements(IGeoView)

    def __init__(self, context, request):
        super(GeoView, self).__init__(context, request)

    def isGeoreferenceable(self):
        return IGeoreferenceable.providedBy(self.context)
