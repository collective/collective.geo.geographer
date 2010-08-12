from zope.interface import Attribute, Interface


class IGeoreferenceable(Interface):
    
    """Marks classes that may be annotated with georeferencing properties.
    """


class IGeoInterface(Interface):

    """Provides the Python geo interface.

    See http://trac.gispython.org/projects/PCL/wiki/PythonGeoInterface
    for details.
    """

    __geo_interface__ = Attribute("""Python Geo Interface""")


class IGeoreferenced(Interface):

    """A geographically referenced object.

    The spatial reference system is implicitly long, lat WGS84. Geometry types
    and coordinates shall follow the Python geo interface specification, which
    itself tracks the GeoJSON draft specification at http://geojson.org.
    """

    type = Attribute(
        """The name of the geometry type: 'Point', 'LineString', 'Polygon'"""
        )
    coordinates = Attribute("""A sequence of coordinate tuples""")
    crs = Attribute("""A coordinate reference system as a dict.
        The default is decimal degree longitude and latitude using the 
        WGS 1984 reference system.""")


class IWritableGeoreference(Interface):

    def setGeoInterface(type, coordinates, crs):
        """Set the geometry via the geo interface."""


class IWriteGeoreferenced(IGeoreferenced, IWritableGeoreference):
    """Supports read/write georeferencing.
    """