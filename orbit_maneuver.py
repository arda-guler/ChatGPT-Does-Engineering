import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67408e-11    # Gravitational constant [m^3/(kg*s^2)]
m_Earth = 5.97e24  # Mass of the Earth [kg]
R_Earth = 6371e3   # Radius of the Earth [m]
h = 1000e3         # Height of the orbit [m]
v_0 = np.sqrt(G * m_Earth / (R_Earth + h))  # Initial velocity [m/s]

# Initial state
r_0 = np.array([R_Earth + h, 0, 0])      # Initial position [m]
v_0 = np.array([0, v_0, 0])              # Initial velocity [m/s]
state = np.concatenate([r_0, v_0])      # Initial state vector

# Time parameters
t_0 = 0           # Initial time [s]
t_end = 60 * 60   # End time [s]
dt = 1            # Time step [s]
times = np.arange(t_0, t_end + dt, dt)

# Function for acceleration due to gravity
def gravity_acceleration(state):
    r = state[:3]
    a_gravity = -G * m_Earth * r / np.linalg.norm(r)**3
    return a_gravity

# Velocity Verlet method
def velocity_verlet(state, dt):
    r, v = state[:3], state[3:]
    a = gravity_acceleration(state)

    # Update position
    r_new = r + v * dt + 0.5 * a * dt**2

    # Update acceleration
    a_new = gravity_acceleration(np.concatenate([r_new, v]))

    # Update velocity
    v_new = v + 0.5 * (a + a_new) * dt

    # Update state vector
    state_new = np.concatenate([r_new, v_new])

    return state_new

# Perform the orbital maneuver
def orbital_maneuver(state):
    # Change in velocity
    delta_v = np.array([0, 0, 100])  # [m/s]

    # Apply the delta-v
    state[3:] += delta_v

    return state

# Simulation loop
states = [state]
for i in range(1, len(times)):
    state = velocity_verlet(state, dt)

    # Perform the maneuver at 30 minutes
    if times[i] == 30 * 60:
        state = orbital_maneuver(state)

    states.append(state)

# Extract position and velocity vectors
positions = np.array([state[:3] for state in states])
velocities = np.array([state[3:] for state in states])

# Plot the orbit
plt.figure()
plt.plot(positions[:, 0], positions[:, 1])
plt.axis('equal')
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Orbit')

# Plot the velocity
plt.figure()
plt.plot(times, np.linalg.norm(velocities, axis=1))
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.title('Velocity over Time')

plt.show()
