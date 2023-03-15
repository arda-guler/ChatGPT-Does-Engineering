import numpy as np

# Define airfoil properties
chord = 1.0  # chord length
thickness = 0.12  # maximum thickness-to-chord ratio
angle_of_attack = np.deg2rad(5.0)  # angle of attack in radians

# Define air properties
density = 1.225  # air density
velocity = 50.0  # air velocity
viscosity = 1.789e-5  # air viscosity

# Define airfoil coordinates (example using NACA 2412 airfoil)
x = np.array([1.0000, 0.9924, 0.9689, 0.9307, 0.8792, 0.8166, 0.7451, 0.6660, 0.5819, 0.4955, 0.4097, 0.3275, 0.2509, 0.1829, 0.1267, 0.0843, 0.0523, 0.0293, 0.0129, 0.0000])
y = np.array([0.0000, 0.0131, 0.0259, 0.0382, 0.0499, 0.0611, 0.0717, 0.0817, 0.0909, 0.0993, 0.1068, 0.1133, 0.1187, 0.1230, 0.1262, 0.1279, 0.1279, 0.1261, 0.1218, 0.0000])

# Calculate airfoil geometry
y_top = thickness/2 * np.interp(x, x[::-1], y[::-1])
y_bot = -thickness/2 * np.interp(x, x[::-1], y[::-1])
dy_dx = np.gradient(y_top+y_bot, x)

# Calculate angle of attack at each point
alpha = angle_of_attack - np.arctan(dy_dx)

# Calculate lift and drag coefficients
cl = 2*np.pi*alpha
cd = 0.01 + 0.02*np.square(alpha)

# Calculate lift and drag forces
lift = 0.5*density*velocity**2*cl*chord
drag = 0.5*density*velocity**2*cd*chord

print("Lift force:", lift)
print("Drag force:", drag)
