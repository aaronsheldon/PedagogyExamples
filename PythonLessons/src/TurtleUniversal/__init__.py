"""#### Turtle Universal

This package contains spherical and cartesian Turtle navigators. Note the use of relative
imports from the modules.

#### Authors and Maintainers
Aaron Sheldon asheldon@bowvalleycollege.ca"""
from .Spherical import translate as sphericaltranslate
from .Cartesian import translate as cartesiantranslate
from .Navigator import Navigator

NAUTICALMILESPERDEGREE = 60
"""Any name can have auto-detected comments. This is meant to be a constant."""

class SphericalNavigator(Navigator):
    """Specialize the Navigator class to spherical translations."""

    def __init__(self, latitude=0, longitude=0):
        """Dependency inject the spherical translation method."""
        super().__init__(
            sphericaltranslate,
            latitude,
            longitude
        )

class CartesianNavigator(Navigator):
    """Specialize the Navigator class to cartesian translations."""

    def __init__(self, latitude=0, longitude=0):
        """Dependency inject the cartesian translation method."""
        super().__init__(
            cartesiantranslate,
            latitude,
            longitude
        )