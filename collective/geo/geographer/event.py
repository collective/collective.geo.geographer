from Products.CMFCore.utils import getToolByName

def reindexDocSubscriber(event):
    """A subscriber to ObjectModifiedEvent"""
    event.object.reindexObject()
