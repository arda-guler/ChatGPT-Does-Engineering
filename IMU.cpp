#include <iostream>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

int main() {
    // Define initial state of object
    Vector3d r0(0, 0, 0); // initial position
    Quaterniond q0(1, 0, 0, 0); // initial orientation

    // Define constants
    double dt = 0.01; // time step (in seconds)
    Vector3d g(0, 0, -9.81); // acceleration due to gravity (in m/s^2)

    // Define variables for linear and angular accelerations
    Vector3d a_local(0, 0, 0); // local linear acceleration (in m/s^2)
    Vector3d alpha_local(0, 0, 0); // local angular acceleration (in rad/s^2)

    // Loop through time steps
    while (true) {
        // Get local linear and angular accelerations from input
        cout << "Enter local linear accelerations (in m/s^2): ";
        cin >> a_local(0) >> a_local(1) >> a_local(2);

        cout << "Enter local angular accelerations (in rad/s^2): ";
        cin >> alpha_local(0) >> alpha_local(1) >> alpha_local(2);

        // Calculate local acceleration and angular velocity vectors
        Vector3d a_global = q0.conjugate() * (a_local - g);
        Vector3d omega_local = q0.conjugate() * alpha_local;

        // Integrate local acceleration and angular velocity to obtain change in position and orientation
        Vector3d dr = q0.toRotationMatrix() * (a_global * dt + 0.5 * g * dt * dt);
        Vector3d domega = omega_local * dt;
        Quaterniond dq(1, 0.5 * domega(0), 0.5 * domega(1), 0.5 * domega(2));

        // Update position and orientation
        r0 += dr;
        q0 = (q0 * dq).normalized();

        // Print current position and orientation
        cout << "Current position: " << r0.transpose() << endl;
        cout << "Current orientation (as quaternion): " << q0.w() << " " << q0.vec().transpose() << endl;
        cout << endl;
    }

    return 0;
}
