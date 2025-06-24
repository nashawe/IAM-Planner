# src/iamp_optimizer/models/waypoint.py

from collections import namedtuple

"""
A simple data structure to represent a single point in 2D space.
Using a namedtuple is lightweight and makes the coordinates accessible by name (e.g., wp.x).
"""
Waypoint = namedtuple('Waypoint', ['x', 'y'])