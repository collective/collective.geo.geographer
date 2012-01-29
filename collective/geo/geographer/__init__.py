from zope.component.interfaces import ComponentLookupError
from collective.geo.geographer.interfaces import IGeoreferenced
from plone.indexer.decorator import indexer
from zope import interface


@indexer(interface.Interface)
def zgeo_geometry_value(object):
    try:
        geo = IGeoreferenced(object)
        if not (geo.type and geo.coordinates):
            return None

        return dict(type=geo.type,
                coordinates=geo.coordinates,
                style=geo.geo.get('style'),
                )

    except (ComponentLookupError, TypeError, ValueError, KeyError, IndexError):
        # The catalog expects AttributeErrors when a value can't be found
        raise AttributeError
