Introduction
============

collective.geo.geographer provides geo annotation for Plone.

This package is based on Sean Gillies's idea (zgeo.geographer) and integrates
its functionalities in collective.geo project.


Requirements
------------

* simplejson
* geopy
* Plone >= 4

How it work
-----------

Any object that implements zope.annotation.interfaces.IAttributeAnnotatable and
collective.geo.geographer.interfaces.IGeoreferenceable can be adapted and geo-referenced.
The former marker is standard for Zope content objects, and the latter can be
easily configured via ZCML.

Let's test with an example placemark, which provides both of the marker
interfaces mentioned above.

    >>> from zope.interface import implements
    >>> from zope.annotation.interfaces import IAttributeAnnotatable
    >>> from collective.geo.geographer.interfaces import IGeoreferenceable

    >>> class Placemark(object):
    ...     implements(IGeoreferenceable, IAttributeAnnotatable)

    >>> placemark = Placemark()

Adapt it to IGeoreferenced

    >>> from collective.geo.geographer.interfaces import IGeoreferenced
    >>> geo = IGeoreferenced(placemark)

Its properties should all be None

    >>> geo.type is None
    True
    >>> geo.coordinates is None
    True
    >>> geo.crs is None
    True

Now set the location geometry to type "Point" and coordinates 105.08 degrees
West, 40.59 degrees North using setGeoInterface()

    >>> geo.setGeoInterface('Point', (-105.08, 40.59))

A georeferenced object has "type" and "coordinates" attributes which should
give us back what we put in.

    >>> geo.type
    'Point'
    >>> geo.coordinates
    (-105.08, 40.590000000000003)
    >>> geo.crs is None
    True

An event should have been sent

    >>> from zope.component.eventtesting import getEvents
    >>> from zope.lifecycleevent.interfaces import IObjectModifiedEvent
    >>> events = getEvents(IObjectModifiedEvent)
    >>> len(events)
    1
    >>> events[0].object is placemark
    True


Plone integration
-----------------

Make a topic in our folder

    >>> self.setRoles(('Manager',))

    >>> folder = self.folder
    >>> oid = self.folder.invokeFactory('Topic', 'topic')
    >>> topic = self.folder[oid]
    >>> c = topic.addCriterion('getGeometry', 'ATBooleanCriterion')

Add geo-referenced content

    >>> oid = self.folder.invokeFactory('Document', 'doc')
    >>> doc = self.folder[oid]

If content type doesn't implements IGeoreferenceable interfaces we need to provide it
    >>> from zope.interface import alsoProvides
    >>> alsoProvides(doc, IGeoreferenceable)

now we can set the coordinates
    >>> from collective.geo.geographer.interfaces import IWriteGeoreferenced
    >>> geo = IWriteGeoreferenced(doc)
    >>> geo.setGeoInterface('Point', (-100, 40))

Check the topic

    >>> brain = [b for b in topic.queryCatalog() if b.id == 'doc'][0]
    >>> brain.zgeo_geometry['type']
    'Point'
    >>> brain.zgeo_geometry['coordinates']
    (-100, 40)


A simple view notify us if a context is geo referenceable
    >>> doc.restrictedTraverse('@@geoview').isGeoreferenceable()
    True

    >>> topic.restrictedTraverse('@@geoview').isGeoreferenceable()
    False


Contributors
============

* Sean Gillies
* Giorgio Borelli
