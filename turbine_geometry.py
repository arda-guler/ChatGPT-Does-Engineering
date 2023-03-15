import math

# Define flow parameters
flow_rate = 1.0  # m^3/s
inlet_pressure = 100000  # Pa
inlet_temperature = 300  # K
outlet_pressure = 10000  # Pa
outlet_temperature = 500  # K
power_output = 1000  # kW

# Calculate enthalpy change
specific_heat = 1000  # J/kg-K (for water)
enthalpy_change = specific_heat * (outlet_temperature - inlet_temperature)

# Calculate turbine efficiency
isentropic_efficiency = 0.8  # assumed value
actual_efficiency = isentropic_efficiency * math.sqrt((inlet_pressure / outlet_pressure) * (outlet_temperature / inlet_temperature - 1))

# Calculate mass flow rate
density = inlet_pressure / (specific_heat * inlet_temperature)
mass_flow_rate = flow_rate * density

# Calculate turbine geometry
specific_speed = math.sqrt(power_output / (mass_flow_rate * enthalpy_change * actual_efficiency))
tip_speed = 100  # m/s (assumed value)
diameter = specific_speed / (math.pi * tip_speed)

# Print results
print(f"Turbine diameter: {diameter:.6f} m")
