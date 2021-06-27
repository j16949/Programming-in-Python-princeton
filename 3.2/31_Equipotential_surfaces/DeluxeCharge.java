/******************************************************************************
 *  Compilation:  javac DeluxeCharge.java
 *  Execution:    none
 *
 *  Charge data type with bonus methods.
 *
 ******************************************************************************/

public class DeluxeCharge {
    // electrostatic constant (N m^2 / C^2)
    private static final double ELECTROSTATIC_CONSTANT = 8.99E09;

    private double rx, ry;    // position
    private double q;       // charge

    public DeluxeCharge(double rx, double ry, double q) {
        this.rx = rx;
        this.ry = ry;
        this.q = q;
    }

    // return the potential
    public double potentialAt(double x, double y) {
        return ELECTROSTATIC_CONSTANT * q / distanceTo(x, y);   // V = kq / r
    }

    public double fieldX(double x, double y) {
        double dx = x - rx;
        double r = distanceTo(x, y);
        double e = ELECTROSTATIC_CONSTANT * q / (r * r);  // E  = kq / r^2
        return e * dx / r;                                // Ex = E * dx / r
    }

    public double fieldY(double x, double y) {
        double dy = y - ry;
        double r = distanceTo(x, y);               
        double e = ELECTROSTATIC_CONSTANT * q / (r * r);  // E  = kq / r^2
        return e * dy / r;                                // Ey = E * dy / r
    }

    // Euclidean distance between this Charge and (x, y)
    public double distanceTo(double x, double y) {
        double dx = x - rx;
        double dy = y - ry;
        return Math.sqrt(dx*dx + dy*dy);
    }

    // is this charge positive?
    public boolean isPositivelyCharged() {
        return q > 0;
    }

    // return x and y coordinates of this charge
    public double getX() { return rx; }
    public double getY() { return ry; }

    // return string representation of this charge
    public String toString() {
        return "rx = " + rx + "  ry = " + ry + "  q = " + q;
    }

}
