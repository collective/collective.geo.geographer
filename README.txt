Introduction
============

collective.geo.geographer provide geo annotation for Plone.

This package is based on Sean Gillies's zgeo.plone.geographer and integrates
its functionalities in collective.geo project.

Requirements
------------

* zgeo.geographer >= 0.3

How it work
-----------

Make a topic in our folder

    >>> self.setRoles(('Manager',))

    >>> folder = self.folder
    >>> oid = self.folder.invokeFactory('Topic', 'topic')
    >>> topic = self.folder[oid]
    >>> c = topic.addCriterion('getGeometry', 'ATBooleanCriterion')

Add geo-referenced content

    >>> oid = self.folder.invokeFactory('Document', 'doc')
    >>> doc = self.folder[oid]
    >>> from zgeo.geographer.interfaces import IWriteGeoreferenced
    >>> geo = IWriteGeoreferenced(doc)
    >>> geo.setGeoInterface('Point', (-100, 40))

Check the topic

    >>> brain = [b for b in topic.queryCatalog() if b.id == 'doc'][0]
    >>> brain.zgeo_geometry['type']
    'Point'
    >>> brain.zgeo_geometry['coordinates']
    (-100, 40)

Conflicts
=========

There's a conflict with an event registration from Plone4ArtistsVideo
(p4a.plonevideo, specifically).  A method from P4A Video gets called
to try and update a 'ObjectGeoreferencedEvent' from zgeo.geographer
when one tries to assign coordinates to a file marked with the p4a
video subtype.  A monkey patch in this package works around the issue
at present.

Contributors
============

* Sean Gillies
* Giorgio Borelli
* David Breitkreutz - rockdj
