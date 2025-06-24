# src/iamp_optimizer/ui/visualization.py

import matplotlib.pyplot as plt
from typing import List
from ..models.flight_path import FlightPath # Use '..' to go up one level from ui to iamp_optimizer

def plot_path(flight_path: FlightPath, title: str = "Flight Path Visualization"):
    """
    Uses matplotlib to create a 2D plot of a given flight path.
    
    Args:
        flight_path: The FlightPath object to plot.
        title: The title for the plot.
    """
    # Extract x and y coordinates from the waypoints
    x_coords = [wp.x for wp in flight_path.waypoints]
    y_coords = [wp.y for wp in flight_path.waypoints]

    # Create the plot
    plt.figure(figsize=(10, 10))
    
    # Plot the path as a blue line with circle markers
    plt.plot(x_coords, y_coords, 'b-o', label="Path")
    
    # Highlight the start and end points
    plt.scatter(x_coords[0], y_coords[0], color='green', s=150, zorder=5, label="Start")
    plt.scatter(x_coords[-1], y_coords[-1], color='red', s=150, zorder=5, label="End")
    
    # Add labels and title for clarity
    plt.title(title)
    plt.xlabel("X Coordinate (km)")
    plt.ylabel("Y Coordinate (km)")
    plt.grid(True)
    plt.legend()
    plt.axis('equal') # Ensure the scale is the same on both axes
    
    # Display the plot
    plt.show()