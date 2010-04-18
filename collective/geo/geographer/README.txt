Introduction
============

collective.geo.geographer provide geo Annotation for Plone.

This package is based on Sean Gillies's idea; zgeo.geographer and integrates
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


Contributors
============

* Sean Gillies - author
* Giorgio Borelli
