from Products.CMFCore.utils import getToolByName

from zgeo.geographer.event import ObjectGeoreferencedEvent

import logging
logger = logging.getLogger('collective.geo.geographer')

ObjectGeoreferencedEvent.descriptions = {}
logger.info("Patching zgeo.geographer.events's ObjectGeoreferencedEvent to have a 'descriptions' field to handle an issue with p4a.plonevideo.")


def reindexDocSubscriber(event):
    """A subscriber to ObjectModifiedEvent"""
    event.object.reindexObject()
