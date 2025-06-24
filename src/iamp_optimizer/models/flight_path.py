# src/iamp_optimizer/models/flight_path.py

from typing import List
from .waypoint import Waypoint

class FlightPath:
    """
    Represents a flight path as a sequence of Waypoint objects.
    This class will be the "chromosome" in our Genetic Algorithm.
    """
    def __init__(self, waypoints: List[Waypoint]):
        """
        Initializes the FlightPath with a list of waypoints.
        
        Args:
            waypoints: A list of Waypoint objects.
        """
        if not waypoints:
            raise ValueError("Flight path cannot be empty.")
        self.waypoints = waypoints

    def __repr__(self):
        return f"FlightPath with {len(self.waypoints)} waypoints"