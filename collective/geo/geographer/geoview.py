import pkg_resources
from zope.interface import implements

from Products.Five.browser import BrowserView

try:
    pkg_resources.get_distribution('plone.dexterity')
except pkg_resources.DistributionNotFound:
    HAS_DEXTERITY = False
else:
    HAS_DEXTERITY = True
    from plone.dexterity.interfaces import IDexterityContent

from .interfaces import IGeoreferenceable
from .interfaces import IGeoreferenced
from .interfaces import IGeoView

class GeoView(BrowserView):
    """A simple view to know if an object is geo referenceable.

    See: :class:`collective.geo.geographer.interfaces.IGeoView`
    """
    implements(IGeoView)

    def __init__(self, context, request):
        super(GeoView, self).__init__(context, request)

    def isGeoreferenceable(self):
        return IGeoreferenceable.providedBy(self.context)

    def isDexterityContentType(self):
        if HAS_DEXTERITY:
            return IDexterityContent.providedBy(self.context)
        return False

    def showCoordinatesTab(self):
        # Dexterity content types don't need Coordinates Tab
        return self.isGeoreferenceable() and not self.isDexterityContentType()

    def getCoordinates(self):
        if self.isGeoreferenceable():
            geo = IGeoreferenced(self.context)
            return geo.type, geo.coordinates
