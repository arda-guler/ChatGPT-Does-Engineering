import numpy as np
import matplotlib.pyplot as plt

# Define airfoil properties
c = 1.0  # chord length
n = 101  # number of points on airfoil
x = np.linspace(0, c, n)  # x coordinates
t = 0.12  # maximum thickness ratio
yc = 0.2  # maximum camber ratio
p = 0.4  # location of maximum camber
dzdx = 0.0  # slope of camber line at leading edge

# Calculate camber line and thickness distribution
yc_x = np.piecewise(x, [x<p, x>=p], [lambda x: yc/p**2*(2*p*x - x**2), lambda x: yc/(1-p)**2*((1-2*p) + 2*p*x - x**2)])
dycdx_x = np.piecewise(x, [x<p, x>=p], [lambda x: 2*yc/p**2*(p - x), lambda x: 2*yc/(1-p)**2*(p - x)])
yt_x = 5*t*c*(0.2969*np.sqrt(x/c) - 0.1260*(x/c) - 0.3516*(x/c)**2 + 0.2843*(x/c)**3 - 0.1015*(x/c)**4)

# Calculate upper and lower surfaces
xu = x - yt_x*np.sin(np.arctan(dycdx_x))  # upper surface x coordinates
yu = yc_x + yt_x*np.cos(np.arctan(dycdx_x))  # upper surface y coordinates
xl = x + yt_x*np.sin(np.arctan(dycdx_x))  # lower surface x coordinates
yl = yc_x - yt_x*np.cos(np.arctan(dycdx_x))  # lower surface y coordinates

# Plot airfoil
fig, ax = plt.subplots()
ax.plot(xu, yu, 'k-', label='Upper surface')
ax.plot(xl, yl, 'k-', label='Lower surface')
ax.fill_between(xu, yu, yl, where=yu>=yl, color='gray', alpha=0.5)
ax.set_aspect('equal')
ax.legend()
ax.set_title('Airfoil geometry')
ax.set_xlabel('x/c')
ax.set_ylabel('y/c')
plt.show()
