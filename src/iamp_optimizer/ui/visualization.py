# src/iamp_optimizer/ui/visualization.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import List, Optional
from ..models.flight_path import FlightPath
from ..models.threat import Threat

def plot_path(flight_path: FlightPath, threats: Optional[List[Threat]] = None, title: str = "Flight Path Visualization"):
    """
    Uses matplotlib to create a 2D plot of a given flight path and optional threats.
    
    Args:
        flight_path: The FlightPath object to plot.
        threats: An optional list of Threat objects to display.
        title: The title for the plot.
    """
    # Extract x and y coordinates from the waypoints
    x_coords = [wp.x for wp in flight_path.waypoints]
    y_coords = [wp.y for wp in flight_path.waypoints]

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Plot threats first so they are in the background
    if threats:
        for threat in threats:
            # Create a circle patch for the threat zone
            threat_circle = patches.Circle(
                (threat.x, threat.y), threat.radius, 
                color='red', alpha=0.3, label='Threat Zone'
            )
            ax.add_patch(threat_circle)

    # Plot the path as a blue line with circle markers
    ax.plot(x_coords, y_coords, 'b-o', label="Path")
    
    # Highlight the start and end points
    ax.scatter(x_coords[0], y_coords[0], color='green', s=150, zorder=5, label="Start")
    ax.scatter(x_coords[-1], y_coords[-1], color='red', s=150, zorder=5, label="End")
    
    # Add labels and title for clarity
    ax.set_title(title)
    ax.set_xlabel("X Coordinate (km)")
    ax.set_ylabel("Y Coordinate (km)")
    ax.grid(True)
    ax.axis('equal') # Ensure the scale is the same on both axes
    
    # Handle legends carefully to avoid duplicate labels for multiple threats
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())
    
    # Display the plot
    plt.show()