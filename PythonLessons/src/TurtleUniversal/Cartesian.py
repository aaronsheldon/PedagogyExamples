"""#### Cartesian

Numerical methods to update latitude and longitude based on bearing and distance.

#### Authors and Maintainers
Aaron Sheldon asheldon@bowvalleycollege.ca"""
from math import sin, cos

def updatelatitude(oldlatitude, bearing, distance):
    """Update from the previous latitude and current bearing and distance calculate the new
    latitude using Cartesian Trigonometry. Returns a number:
    * `newlatitude` updated latitude."""
    return oldlatitude + distance * sin(bearing)

def updatelongitude(oldlongitude, bearing, distance):
    """Update from the previous longitude, current and previous latitude and current bearing
    and distance calculate the new longitude using Cartesian Trigonometry. Returns a number:
    * `newlongitude` updated longitude."""
    return oldlongitude + distance * cos(bearing)

def translate(oldlatitude, oldlongitude, bearing, distance):
    """Compute the entire translation. Returns a tuple:
    * `newlatitude` updated vertical.
    * `newlongitude` updated horizontal."""
    newlatitude = updatelatitude(oldlatitude, bearing, distance)
    newlongitude = updatelongitude(oldlongitude, bearing, distance)
    return newlatitude, newlongitude