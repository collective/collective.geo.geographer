from zope.interface import implements
from zope.component.interfaces import IObjectEvent

import logging
logger = logging.getLogger('collective.geo.geographer')


class IObjectGeoreferencedEvent(IObjectEvent):
    """An event signaling that an object has been georeferenced
    """


class ObjectGeoreferencedEvent(object):
    implements(IObjectGeoreferencedEvent)

    def __init__(self, ob):
        self.object = ob


ObjectGeoreferencedEvent.descriptions = {}
logger.info(
    "Patching collective.geo.geographer.events's "
    "ObjectGeoreferencedEvent to have a 'descriptions' "
    "field to handle an issue with p4a.plonevideo."
)
