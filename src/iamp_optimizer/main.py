# src/iamp_optimizer/main.py

import sys
import os
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.iamp_optimizer.models.waypoint import Waypoint
from src.iamp_optimizer.models.flight_path import FlightPath
from src.iamp_optimizer.models.threat import Threat
from src.iamp_optimizer.ui.visualization import plot_path
from src.iamp_optimizer.cost_function.fitness_calculator import calculate_fitness

def generate_random_path(start_wp, end_wp, num_intermediate_wps, bounds=(0, 100)):
    """Helper function to create a random path for testing."""
    waypoints = [start_wp]
    for _ in range(num_intermediate_wps):
        rand_x = random.uniform(bounds[0], bounds[1])
        rand_y = random.uniform(bounds[0], bounds[1])
        waypoints.append(Waypoint(x=rand_x, y=rand_y))
    waypoints.append(end_wp)
    return FlightPath(waypoints=waypoints)

def run_step_2():
    """
    Executes Step 2: Creates a random path, evaluates its fitness against a threat,
    and visualizes the scenario.
    """
    print("Running IAMP Static Optimizer - Step 2: Fitness Calculation")
    
    # 1. Define mission parameters
    start_point = Waypoint(x=10, y=50)
    end_point = Waypoint(x=90, y=50)
    
    # 2. Define the environment
    # Let's place a threat right in the middle of the direct path
    threats = [
        Threat(x=50, y=50, radius=15)
    ]
    
    # 3. Generate a random candidate path with 5 intermediate waypoints
    random_path = generate_random_path(start_point, end_point, num_intermediate_wps=5)
    
    # 4. Calculate the fitness (cost) of this random path
    fitness_score = calculate_fitness(random_path, threats)
    
    print(f"Generated a random path with {len(random_path.waypoints)} waypoints.")
    print(f"Calculated Fitness Score: {fitness_score:.2f}")
    if fitness_score > 10000:
        print("This path is considered UNSAFE because it likely entered a threat zone.")
    else:
        print("This path is considered SAFE (but likely not optimal).")
        
    # 5. Visualize the path and the threats
    plot_path(
        flight_path=random_path, 
        threats=threats, 
        title=f"Step 2: Random Path (Fitness: {fitness_score:.2f})"
    )

if __name__ == "__main__":
    run_step_2()