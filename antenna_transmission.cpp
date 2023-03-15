#include <iostream>
#include <cmath>

using namespace std;

int main() {
    // Define antenna properties
    double tx_power = 20.0;  // transmitted power in watts
    double freq = 2.4e9;  // frequency in hertz
    double gain = 10.0;  // antenna gain in decibels
    double loss = 2.0;  // cable and connector loss in decibels

    // Define path loss parameters
    double distance = 100.0;  // distance in meters
    double freq_mhz = freq/1e6;
    double lambda_m = 299792458/freq;
    double d0 = 1.0;  // reference distance in meters
    double n = 2.0;  // path loss exponent

    // Calculate path loss
    double path_loss = 20*log10(4*M_PI*distance/lambda_m) + 10*n*log10(distance/d0);

    // Calculate received power
    double rx_power = tx_power + gain - loss - path_loss;

    // Convert to milliwatts and decibels
    double rx_power_mw = pow(10, rx_power/10);
    double rx_power_dbm = 10*log10(rx_power_mw);

    cout << "Received power: " << rx_power_dbm << " dBm" << endl;

    return 0;
}
