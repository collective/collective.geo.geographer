from zope import interface
from zope.component.interfaces import ComponentLookupError
from plone.indexer.decorator import indexer

from .interfaces import IGeoreferenceable
from .interfaces import IGeoreferenced


@indexer(interface.Interface)
def zgeo_geometry_value(obj):
    if IGeoreferenceable.providedBy(obj):
        geo = IGeoreferenced(obj)
        if geo.type and geo.coordinates:
            return {
                'type': geo.type,
                'coordinates': geo.coordinates
            }
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError
