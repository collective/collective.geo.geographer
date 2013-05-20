from zope.interface import Attribute
from zope.interface import Interface


class IGeoreferenceable(Interface):
    """Marks classes that may be annotated with georeferencing properties.
    """


class IGeoreferenced(Interface):
    """A geographically referenced object.

    The spatial reference system is implicitly long, lat WGS84. Geometry types
    and coordinates shall follow the Python geo interface specification, which
    itself tracks the GeoJSON draft specification at http://geojson.org.
    """

    type = Attribute(
        """The name of the geometry type: 'Point', 'LineString', 'Polygon'""")
    coordinates = Attribute("""A sequence of coordinate tuples""")

    crs = Attribute("""A coordinate reference system as a dict.
        The default is decimal degree longitude and latitude using the
        WGS 1984 reference system.""")


class IWritableGeoreference(Interface):

    def setGeoInterface(type, coordinates, crs):
        """Set the geometry via the geo interface.

        :param type: Point or LineString or Polygon
        :type type: string
        :param coordinates: a sequence of coordinates
        :type coordinates: tuple
        :param crs: A coordinate reference system as a dict
        :type crs: dict
        """

    def removeGeoInterface(self):
        """Remove the geometry via the geo interface."""


class IWriteGeoreferenced(IGeoreferenced, IWritableGeoreference):
    """Supports read/write georeferencing.
    """


class IGeoView(Interface):
    """View to access coordinates
    """

    def isGeoreferenceable():
        """Returns True if an object is Georeferenceable

        :returns: return True if context can be geo referenced
        :rtype: boolean
        """

    def getCoordinates():
        """Public function to get object coordinates

        :returns: (coordinate type, (a sequence of coordinates)) or None
        :rtype: tuple
        """

    def hasCoordinates():
        """Return whether context has been georeferenced or not

        :returns: return True if context coordinates are not null
        :rtype: boolean
        """
