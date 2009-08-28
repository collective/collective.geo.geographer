from zope.component.interfaces import ComponentLookupError
from zgeo.geographer.interfaces import IGeoreferenced
from plone.indexer.decorator import indexer
from zope import interface

@indexer(interface.Interface)
def zgeo_geometry_value(object):
    try:
        geo = IGeoreferenced(object)
        return dict(type=geo.type, coordinates=geo.coordinates)
    except (ComponentLookupError, TypeError, ValueError, KeyError, IndexError):
        # The catalog expects AttributeErrors when a value can't be found
        raise AttributeError

