import numpy as np
import matplotlib.pyplot as plt

# define a grid
nx, ny = 100, 100
xmin, xmax, ymin, ymax = -1, 1, -1, 1
x = np.linspace(xmin, xmax, nx)
y = np.linspace(ymin, ymax, ny)
X, Y = np.meshgrid(x, y)

# define sources and sinks
strength = 5.0
nsources = 2
xs = np.array([0.5, -0.5])
ys = np.array([0, 0])

# compute velocity and stream-function
u, v = np.zeros_like(X), np.zeros_like(Y)
psi = np.zeros_like(X)
for i in range(nsources):
    xs_i, ys_i = xs[i], ys[i]
    R = np.sqrt((X - xs_i)**2 + (Y - ys_i)**2)
    theta = np.arctan2(Y - ys_i, X - xs_i)
    u += strength/(2*np.pi) * (R*np.cos(theta))/R**2
    v += strength/(2*np.pi) * (R*np.sin(theta))/R**2
    psi += strength/(2*np.pi) * np.arctan2((Y - ys_i), (X - xs_i))

# plot the streamlines
plt.streamplot(x, y, u, v, density=2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
