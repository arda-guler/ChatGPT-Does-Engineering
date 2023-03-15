#include <iostream>
#include <Eigen/Dense>

using namespace Eigen;

int main() {
    // Define object properties
    double mass = 1.0;
    double radius = 1.0;
    double inertia = (2.0/5.0) * mass * radius * radius;  // moment of inertia for a solid sphere
    Vector3d com(0.0, 0.0, 0.0);  // center of mass

    // Define force
    Vector3d force(1.0, 0.0, 0.0);  // applied to the right of the object
    Vector3d force_pos(0.0, 1.0, 0.0);  // applied at a point 1 unit above the center of mass

    // Calculate r vector
    Vector3d r = force_pos - com;

    // Calculate angular acceleration
    Matrix3d I_inv = Matrix3d::Identity() * (1.0/inertia);  // inverse moment of inertia tensor
    Vector3d alpha = I_inv * r.cross(force);

    std::cout << "Angular acceleration: " << alpha.transpose() << std::endl;

    return 0;
}
