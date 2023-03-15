import math

# constants
kb = 1.38064852e-23  # Boltzmann constant
Na = 6.02214076e23   # Avogadro constant
T0 = 298.15          # reference temperature (K)

# inputs
fuel_name = "methane"
oxidizer_name = "oxygen"
stoichiometry = 1.0   # fuel to oxidizer stoichiometry
pressure = 1.0e5      # pressure (Pa)
temperature = 300.0   # temperature (K)

# data
fuel_dict = {"methane": {"C": 1, "H": 4}, "hydrogen": {"H": 2}, "ethanol": {"C": 2, "H": 5, "O": 1}}
oxidizer_dict = {"oxygen": {"O": 2}, "air": {"N": 2.0, "O": 1.0}}
ignition_dict = {"methane": 0.28, "hydrogen": 0.02, "ethanol": 0.19}  # ignition temperature (K)

# compute MIE
fuel_atoms = fuel_dict[fuel_name]
oxidizer_atoms = oxidizer_dict[oxidizer_name]

fuel_mass = sum([fuel_atoms[atom] * 1.00784 / Na for atom in fuel_atoms])   # molar mass (kg/mol)
oxidizer_mass = sum([oxidizer_atoms[atom] * 15.999 / Na for atom in oxidizer_atoms])   # molar mass (kg/mol)

a = 4 * math.pi * (fuel_mass + oxidizer_mass) * kb * T0 / (3 * pressure)   # coefficient
b = 0.25 * (stoichiometry * fuel_mass + 1.5 * oxidizer_mass) * 1.0e-3    # factor

MIE = a * b * math.exp(ignition_dict[fuel_name] / temperature)

print("Minimum Ignition Energy:", MIE, "Joules")
