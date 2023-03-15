import numpy as np
import time

# Initialize the orientation matrix and angular velocity vector
R = np.identity(3)
w = np.zeros((3,))

# Set the time step for updates (in seconds)
dt = 0.01

# Continuously update the orientation based on angular accelerations
while True:
    # Get the angular accelerations (in radians per second squared)
    alpha = np.array(input("Enter angular accelerations (in radians per second squared): ").split(), dtype=float)

    # Integrate the angular accelerations to obtain the angular velocities
    w += alpha * dt

    # Integrate the angular velocities to obtain the orientation matrix
    theta = np.linalg.norm(w) * dt
    if theta != 0:
        w_hat = w / np.linalg.norm(w)
        R_delta = np.array([[0, -w_hat[2], w_hat[1]],
                            [w_hat[2], 0, -w_hat[0]],
                            [-w_hat[1], w_hat[0], 0]])
        R += np.sin(theta) * R_delta + (1 - np.cos(theta)) * R_delta @ R_delta

    # Print the current orientation matrix
    print("Current orientation:")
    print(R)
    print()

    # Wait for the next update
    time.sleep(dt)
