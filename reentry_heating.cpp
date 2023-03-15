#include <iostream>
#include <cmath>

int main() {
    // Define flow parameters
    double velocity = 7800.0;  // m/s
    double density = 0.015;  // kg/m^3
    double specific_heat = 1000.0;  // J/kg-K
    double temperature = 1000.0;  // K

    // Calculate Mach number
    double speed_of_sound = std::sqrt(1.4 * 287.0 * temperature);  // for air, assuming gamma = 1.4 and R = 287 J/kg-K
    double mach_number = velocity / speed_of_sound;

    // Calculate stagnation temperature
    double stagnation_temperature = temperature + (velocity * velocity / (2 * specific_heat));

    // Calculate heat flux
    double heat_flux = density * specific_heat * velocity * velocity * std::pow(1.4 / (2.0 * 287.0 * temperature), 0.5) * (0.46 + 0.5 * mach_number * mach_number) * std::pow(1.0 - 0.22 * mach_number * mach_number, 3.0);

    // Print results
    std::cout << "Heat flux: " << heat_flux << " W/m^2" << std::endl;

    return 0;
}
