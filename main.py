import math
import numpy as np
import matplotlib.pyplot as plt

material = {
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

for i,j in enumerate(material):
    print(f'{i}) {j}')

# Constants
density = input('Material of the ball: ')
if density == 'else':
    density = int(input('Density of material: '))
MASS = int(input("Mass of the ball (kg): "))  # kg
DENSITY_AIR = 1.225  # kg/m^3, air density at sea level
DRAG_COEFFICIENT = 0.47  # drag coefficient for a sphere
volume = MASS / density
radius = ((3 * volume) / (4 * math.pi) ** (1/3))  # m, sphere radius
AREA = math.pi * radius**2  # m^2, cross-sectional area of the sphere
G = 9.81  # m/s^2, gravitational acceleration

# Initial conditions
SPEED_PLANE = int(input("Plane's speed (m/s): "))
SPEED_WIND = int(input("Wind's speed (neg or pos): "))
INITIAL_HEIGHT = int(input("How far is the plane above the ground (m): ")) 
INITIAL_VELOCITY_X = SPEED_PLANE + SPEED_WIND
INITIAL_VELOCITY_Y = 0.0  # m/s, initial vertical velocity

# Time step and total simulation time
DT = 0.1  # time step in seconds
TOTAL_TIME = 500  # total simulation time in seconds

# Lists to hold positions and velocities
x_positions = [0.0]  # starting x position
y_positions = [INITIAL_HEIGHT]  # starting y position (height)
time_stamps = []  # time stamps
vx = INITIAL_VELOCITY_X  # initial horizontal velocity
vy = INITIAL_VELOCITY_Y  # initial vertical velocity

# Simulation loop
for t in np.arange(0, TOTAL_TIME, DT):
    # Calculate the speed
    speed = math.sqrt(vx**2 + vy**2)

    # Calculate drag force components
    drag_force = 0.5 * DENSITY_AIR * DRAG_COEFFICIENT * AREA * speed**2
    drag_force_x = -drag_force * (vx / speed)  # horizontal component
    drag_force_y = -drag_force * (vy / speed)  # vertical component

    # Update accelerations considering gravity and drag
    ax = drag_force_x / MASS
    ay = -G + (drag_force_y / MASS)

    # Update velocities
    vx += ax * DT
    vy += ay * DT

    # Update positions
    new_x = x_positions[-1] + vx * DT
    new_y = y_positions[-1] + vy * DT

    # Check if the new height is below ground level
    if new_y <= 0:
        break

    x_positions.append(new_x)
    y_positions.append(new_y)

    # Record time stamps for every second
    if int(t) % 1 == 0:
        time_stamps.append(len(x_positions) - 1)

# Plot the trajectory
plt.figure(figsize=(10, 6))
plt.plot(x_positions, y_positions, label="Trajectory")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Trajectory of a 1 kg Copper Sphere with Air Drag")

# Add dots for each second
for i in time_stamps:
    plt.scatter(x_positions[i], y_positions[i], color='red', zorder=1)

plt.grid()
plt.legend()
plt.show()
