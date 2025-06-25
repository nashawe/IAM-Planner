# src/iamp_optimizer/cost_function/fitness_calculator.py

import numpy as np
from typing import List
from ..models.flight_path import FlightPath
from ..models.threat import Threat

def calculate_fitness(flight_path: FlightPath, threats: List[Threat]) -> float:
    """
    Calculates the fitness (cost) of a given flight path.
    A lower score is better.

    The cost is composed of two parts:
    1. The total length of the path (its primary cost).
    2. A massive penalty for each waypoint that falls inside a threat zone.

    Args:
        flight_path: The FlightPath object to evaluate.
        threats: A list of Threat objects in the environment.

    Returns:
        A float representing the total cost of the path.
    """
    total_distance = 0.0
    threat_penalty = 0.0

    # 1. Calculate the total path length (Euclidean distance)
    for i in range(len(flight_path.waypoints) - 1):
        p1 = flight_path.waypoints[i]
        p2 = flight_path.waypoints[i+1]
        
        # Using numpy for efficient distance calculation
        distance = np.linalg.norm(np.array([p1.x, p1.y]) - np.array([p2.x, p2.y]))
        total_distance += distance

    # 2. Calculate the penalty for entering threat zones
    # We check every waypoint to see if it's inside any threat circle.
    for waypoint in flight_path.waypoints:
        for threat in threats:
            dist_to_threat_center = np.linalg.norm(
                np.array([waypoint.x, waypoint.y]) - np.array([threat.x, threat.y])
            )
            
            if dist_to_threat_center < threat.radius:
                # Apply a HUGE penalty. This ensures that any path violating a threat
                # is considered much worse than a safe, even if very long, path.
                threat_penalty += 10000.0

    # The final fitness is the sum of the path's length and any penalties.
    return total_distance + threat_penalty