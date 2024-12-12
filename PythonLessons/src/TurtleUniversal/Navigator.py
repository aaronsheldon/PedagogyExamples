"""#### Navigator

Generic class to track the waypoints as the Turtle is translated using bearing and distance
updates.

#### Authors and Maintainers
Aaron Sheldon asheldon@bowvalleycollege.ca"""

class Navigator:
    """Each instance holds a unique list of waypoints, initialized to different starting
    points. The instance encapsulates all the methods used to consistently maintain the
    waypoints."""

    def __init__(self, translate, latitude = 0, longitude = 0):
        """Initializer method that initializes the waypoints storage to the start location.
        It is expected that you override this `__dunder__` with your constructor code.
        Returns nothing."""
        self.translate = translate
        self.waypoints = [ ( latitude, longitude) ]

    def move(self, bearing, distance):
        """Instance method to update the waypoints list with the new position based on the
        direction and distance traveled. Returns noting."""
        newlatitude, newlongitude = self.translate(
            self.waypoints[-1][0],
            self.waypoints[-1][1],
            bearing,
            distance
        )
        self.waypoints.append(( newlatitude, newlongitude ))

    def recenter(self, latitude = 0, longitude = 0):
        """"Instance method to Empty the waypoints and start and the new position. Returns
        nothing."""
        self.waypoints = [ ( latitude, longitude) ]