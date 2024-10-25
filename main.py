import math
import matplotlib.pyplot as plt

v_plane = int(input("Plane's Speed in meters: "))
d_plane = int(input("Plane's Direction (0/1): "))
v_wind = int(input("Wind's Speed in meters: "))
d_wind = int(input("Wind's Direction (0/1): "))
h = int(input("How far is the plane above the ground: "))
sphere_radius = int(input('Sphere radius: '))

'''
s = 1/2at**2
s = h (Height)
h = 1/2at**2
a = g (9.8m/s**2)
h = 1/2gt**2
2h = gt**2
t**2 = 2h/g
t = sqrt(2h/g)
'''
t_fall = math.sqrt(2*h/9.8)

drag_coefficient = 0.47  
air_density = 1.225 

cross_sectional_area = math.pi * sphere_radius**2

drag_force = 0.5 * drag_coefficient * air_density * cross_sectional_area * (v_plane+v_wind*d_wind)**2
adjusted_vertical_velocity = -9.8 * t_fall + drag_force

if d_wind == d_plane:
    horizontal_speed = v_plane + v_wind
elif d_wind != d_plane:
    horizontal_speed = v_plane - v_wind

r = horizontal_speed * t_fall

# Prepare data for plotting (horizontal distance over time)
time_intervals = [i * 0.01 for i in range(int(t_fall * 100))]  # Time steps from 0 to t_fall
y_positions = [h - 0.5 * 9.8 * t**2 for t in time_intervals]  # Vertical position (height) over time
x_positions = [horizontal_speed * t for t in time_intervals]  # Horizontal distance over time

y1_positions = [h + adjusted_vertical_velocity * t for t in time_intervals]  # სიმაღლე დროის მიხედვით
x1_positions = [horizontal_speed * t for t in time_intervals]  # ჰორიზონტალური მანძილი დროის მიხედვით

# Plotting the trajectory
plt.figure(figsize=(8, 4))
plt.plot(x_positions, y_positions)
plt.plot(x1_positions, y1_positions)
plt.title("Projectile Motion from Plane (Considering Wind)")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()
