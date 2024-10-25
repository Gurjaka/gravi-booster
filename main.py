import math
import matplotlib.pyplot as plt

# Input parameters for plane and environmental conditions
speed_plane = int(input("Plane's Speed in meters: "))  # Speed of the plane
direction_plane = int(input("Plane's Direction (0/1): "))  # Direction of the plane (0 or 1)
speed_wind = int(input("Wind's Speed in meters: "))  # Speed of the wind
direction_wind = int(input("Wind's Direction (0/1): "))  # Direction of the wind (0 or 1)
height = int(input("How far is the plane above the ground: "))  # Height from which the plane drops
sphere_radius = int(input('Sphere radius: '))  # Not used in calculations but can be for other purposes

# Calculate the time it takes for the plane to fall to the ground
time_fall = math.sqrt(2 * height / 9.8)  # Derived from the free fall formula: t = sqrt(2h/g)

# Determine the horizontal speed of the plane considering wind effect
# If the wind and plane direction are the same, speeds add; otherwise, they subtract
horizontal_speed = speed_plane + speed_wind if direction_wind == direction_plane else speed_plane - speed_wind

# Calculate the range (horizontal distance traveled) during the fall
r = horizontal_speed * time_fall

# Prepare data for plotting: create time intervals from 0 to the time of fall
time_intervals = [i * 0.01 for i in range(int(time_fall * 100))]  # Time steps at 0.01 seconds
# Calculate vertical positions over time using the free fall equation
y_positions = [height - 0.5 * 9.8 * t**2 for t in time_intervals]  # Height at each time step
# Calculate horizontal positions over the same time intervals
x_positions = [horizontal_speed * t for t in time_intervals]  # Horizontal distance at each time step

# Create a single figure for plotting the trajectory
plt.figure(figsize=(8, 4))

# Plot the trajectory of the plane
plt.plot(x_positions, y_positions, color='blue', label='Trajectory')  # Line representing the motion

# Add time markers for every second of the fall
for t in range(int(time_fall) + 1):  # Loop through each whole second until time of fall
    x = horizontal_speed * t  # Calculate horizontal position at time t
    y = height - 0.5 * 9.8 * t**2  # Calculate vertical position at time t
    plt.scatter(x, y, color='red', zorder=3)  # Add a red marker for the time point
    plt.text(x, y, str(t), fontsize=8, verticalalignment='bottom', horizontalalignment='right')  # Label the marker with time

# Finalize the plot with title and labels
plt.title("Projectile Motion from Plane (Considering Wind)")  # Title of the plot
plt.xlabel("Horizontal Distance (m)")  # Label for the x-axis
plt.ylabel("Height (m)")  # Label for the y-axis
plt.grid(True)  # Enable the grid for better visualization
plt.legend()  # Show the legend indicating the trajectory
plt.show()  # Display the plot in a single window
