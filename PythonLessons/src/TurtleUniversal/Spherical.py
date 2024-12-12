"""#### Spherical

Numerical methods to update latitude and longitude based on bearing and distance.

#### Authors and Maintainers
Aaron Sheldon asheldon@bowvalleycollege.ca"""
from math import sin, cos, acos, pi

def updatelatitude(oldlatitude, bearing, distance):
    """Update from the previous latitude and current bearing and distance calculate the new
    latitude using Spherical Trigonometry. Returns a number:
    * `newlatitude` updated latitude."""
    return pi/2 - acos(
        (
            cos(pi/2 - oldlatitude) *
            cos(distance)
        ) + (
            sin(pi/2 - oldlatitude) *
            sin(distance) *
            cos(bearing)
        )
    )

def updatelongitude(oldlatitude, oldlongitude, newlatitude, bearing, distance):
    """Update from the previous longitude, current and previous latitude and current bearing
    and distance calculate the new longitude using Spherical Trigonometry. Returns a number:
    * `newlongitude` updated longitude."""

    # Heading due North. No change in longitude.
    if bearing == 0:
        return oldlongitude
    
    # Heading due South. No change in longitude.
    if bearing == pi:
        return oldlongitude
    
    # Heading East is positive.
    easterly = 1 if bearing > 0 else -1

    # Update the longitude
    return oldlongitude + easterly * acos(
        (
            cos(distance) - (
                cos(pi/2 - newlatitude) *
                cos(pi/2 - oldlatitude)
            )
        ) / (
            sin(pi/2 - newlatitude) *
            sin(pi/2 - oldlatitude)
        )
    )

def translate(oldlatitude, oldlongitude, bearing, distance):
    """Compute the entire translation. Returns a tuple:
    * `newlatitude` updated vertical.
    * `newlongitude` updated horizontal."""
    newlatitude = updatelatitude(oldlatitude, bearing, distance)
    newlongitude = updatelongitude(oldlatitude, oldlongitude, newlatitude, bearing, distance)
    return newlatitude, newlongitude