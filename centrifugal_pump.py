import math

# Define flow parameters
flow_rate = 1.0  # m^3/s
head = 10.0  # m
efficiency = 0.8

# Define pump specific speed
specific_speed = (math.pi * flow_rate / (9.81 * head ** 0.75)) * math.sqrt(head)

# Calculate impeller diameter and width
impeller_diameter = (specific_speed / 0.154) ** (1 / 3) * (flow_rate / head ** 0.5) ** (1 / 6)
impeller_width = 0.16 * impeller_diameter

# Calculate outlet diameter
outlet_diameter = impeller_diameter * math.sqrt(flow_rate / (0.8 * math.pi * impeller_width))

# Print results
print(f"Impeller diameter: {impeller_diameter:.2f} m")
print(f"Impeller width: {impeller_width:.2f} m")
print(f"Outlet diameter: {outlet_diameter:.2f} m")
