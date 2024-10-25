"""
Simulation of a sphere's trajectory under the influence of gravity and air drag.

This script defines a `Sphere` class to calculate the properties of a sphere 
based on its mass and density. It also defines a `Simulation` class that 
simulates the motion of the sphere as it falls through the air, taking into 
account drag forces. The `Plotter` class is responsible for visualizing the 
trajectory of the sphere.

Users can input various materials for the sphere, specify its mass, the 
initial speed of a plane, and the height from which it is dropped. The 
simulation runs and plots the results, indicating the sphere's trajectory 
over time.

Classes:
    Sphere: Represents a sphere with mass and density properties.
    Simulation: Simulates the motion of the sphere with drag and gravity.
    Plotter: Handles the visualization of the simulation results.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

class Sphere:
    """
    Represents a sphere object with mass and density.

    Attributes:
        mass (float): The mass of the sphere in kilograms.
        density (float): The density of the material in kg/m³.
        volume (float): The volume of the sphere in m³.
        radius (float): The radius of the sphere in meters.
        area (float): The cross-sectional area of the sphere in m².
    """

    def __init__(self, mass, dens):
        """
        Initializes the sphere with mass and density.

        Args:
            mass (float): The mass of the sphere.
            dens (float): The density of the material.
        """
        self.mass = mass
        self.density = dens
        self.volume = self.calculate_volume() # Calculate volume based on mass and density
        self.radius = self.calculate_radius() # Calculate radius from volume
        self.area = self.calculate_area() # Calculate cross-sectional area

    def calculate_volume(self):
        """
        Calculates the volume of the sphere.

        Returns:
            float: Volume of the sphere in m³.
        """
        return self.mass / self.density # Volume formula: mass/density

    def calculate_radius(self):
        """
        Calculates the radius of the sphere based on its volume.

        Returns:
            float: Radius of the sphere in meters.
        """
        return ((3 * self.volume) / (4 * math.pi)) ** (1/3) # Radius formula for sphere

    def calculate_area(self):
        """
        Calculates the cross-sectional area of the sphere.

        Returns:
            float: Cross-sectional area of the sphere in m².
        """
        return math.pi * self.radius**2  # Area formula: πr²

class Simulation:
    """
    Simulates the trajectory of the sphere under the influence of gravity and drag.

    Attributes:
        sphere (Sphere): The sphere object being simulated.
        density_air (float): The density of air in kg/m³.
        drag_coefficient (float): The drag coefficient for a sphere.
        g (float): Gravitational acceleration in m/s².
        x_positions (list): List to hold x positions during the simulation.
        y_positions (list): List to hold y positions during the simulation.
        time_stamps (list): List to hold time stamps for each second.
        dt (float): Time step for the simulation in seconds.
        total_time (float): Total time for the simulation in seconds.
    """

    def __init__(self, sph, speed_plane, speed_wind, initial_height):
        """
        Initializes the simulation with sphere and initial conditions.

        Args:
            sph (Sphere): The sphere object being simulated.
            speed_plane (float): Speed of the plane in m/s.
            speed_wind (float): Speed of the wind in m/s.
            initial_height (float): Initial height of the sphere in meters.
        """
        self.sphere = sph
        self.density_air = 1.225  # kg/m³, air density at sea level
        self.drag_coefficient = 0.47  # drag coefficient for a sphere
        self.g = 9.81  # m/s², gravitational acceleration
        self.initial_conditions(speed_plane, speed_wind, initial_height)
        self.x_positions = [0.0] # Starting x position
        self.y_positions = [self.initial_height] # Starting y position (height)
        self.time_stamps = [] # list to record time stamps
        self.dt = 0.1  # time step in seconds
        self.total_time = 500  # total simulation time in seconds

    def initial_conditions(self, speed_plane, speed_wind, initial_height):
        """
        Sets the initial conditions for the simulation.

        Args:
            speed_plane (float): Speed of the plane in m/s.
            speed_wind (float): Speed of the wind in m/s.
            initial_height (float): Initial height of the sphere in meters.
        """
        self.initial_height = initial_height
        self.vx = speed_plane + speed_wind  # initial horizontal velocity
        self.vy = 0.0  # initial vertical velocity

    def run(self):
        """
        Runs the simulation, updating positions and velocities over time.
        """
        for t in np.arange(0, self.total_time, self.dt): # Iterate over time
            self.update(t) # Update positions and velocities
            if self.y_positions[-1] <= 0: #Check if the sphere has hit the ground
                break

    def update(self, t):
        """
        Updates the positions and velocities of the sphere.

        Args:
            t (float): Current time in seconds.
        """
        speed = math.sqrt(self.vx**2 + self.vy**2)  # Calculate current speed
        drag_force = 0.5 * self.density_air * self.drag_coefficient * self.sphere.area * speed**2  # Calculate drag force
        drag_force_x = -drag_force * (self.vx / speed) if speed != 0 else 0  # Horizontal drag force
        drag_force_y = -drag_force * (self.vy / speed) if speed != 0 else 0  # Vertical drag force

        ax = drag_force_x / self.sphere.mass  # Acceleration in x direction
        ay = -self.g + (drag_force_y / self.sphere.mass)  # Acceleration in y direction

        self.vx += ax * self.dt  # Update horizontal velocity
        self.vy += ay * self.dt  # Update vertical velocity

        new_x = self.x_positions[-1] + self.vx * self.dt  # Calculate new x position
        new_y = self.y_positions[-1] + self.vy * self.dt  # Calculate new y position

        self.x_positions.append(new_x)  # Append new x position
        self.y_positions.append(new_y)  # Append new y position

        if int(t) % 1 == 0:  # Record position every second
            self.time_stamps.append(len(self.x_positions) - 1)

class Plotter:
    """
    Handles plotting of the simulation results.
    """
    @staticmethod
    def plot_trajectory(sim):
        """
        Plots the trajectory of the sphere.

        Args:
            sim (Simulation): The simulation object containing the trajectory data.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(sim.x_positions, sim.y_positions, label="Trajectory")  # Plot trajectory
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Distance (m)")
        plt.title("Trajectory of a Sphere with Air Drag")

        for s in sim.time_stamps:  # Plot time stamps as red dots
            plt.scatter(sim.x_positions[s], sim.y_positions[s], color='red', zorder=1)

        plt.grid()
        plt.legend()
        plt.show()

# Main execution
if __name__ == "__main__":
    materials = {
        'else': None,
        'rubber': 1100,
        'polyethylene': 900,
        'leather': 900,
        'foam': 60,
        'steel': 7850,
        'composite materials': 1700,
        'ceramic': 2600,
        'glass': 2500,
        'silicone': 1100,
        'bamboo': 700,
        'copper': 8960,
    }

    for i, j in enumerate(materials):
        print(f'{i}) {j}')

    while True:
        try:
            density_input = input('Material of the ball: ')
            density = materials.get(density_input)  # Get density from material dictionary

            if density is None:
                density = int(input('Density of material (kg/m³): '))  # Input custom density

            MASS = int(input("Mass of the ball (kg): "))  # Input mass
            if MASS <= 0:
                raise ValueError("Mass must be a positive value.")

            SPEED_PLANE = int(input("Plane's speed (m/s): "))  # Input plane speed
            SPEED_WIND = int(input("Wind's speed (neg or pos): "))  # Input wind speed
            INITIAL_HEIGHT = int(input("How far is the plane above the ground (m): "))  # Input height
            if INITIAL_HEIGHT < 0:
                raise ValueError("Height must be a non-negative value.")

            break  # Exit the loop if all inputs are valid

        except ValueError as e:
            print(f"Error: {e}. Please enter valid numeric values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    sphere = Sphere(MASS, density) # Create a Sphere object with the specified mass and density
    simulation = Simulation(sphere, SPEED_PLANE, SPEED_WIND, INITIAL_HEIGHT) # Initialize the Simulation with the created sphere, plane speed, wind speed, and initial height
    simulation.run() # Run the simulation to compute the sphere's trajectory
    Plotter.plot_trajectory(simulation) # Plot the trajectory of the sphere using the Plotter class