# src/iamp_optimizer/models/threat.py

from collections import namedtuple

"""
A simple data structure to represent a circular threat zone.
It's defined by its center coordinates (x, y) and its radius.
"""
Threat = namedtuple('Threat', ['x', 'y', 'radius'])