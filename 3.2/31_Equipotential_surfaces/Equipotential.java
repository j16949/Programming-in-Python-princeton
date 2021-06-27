/******************************************************************************
 *  Compilation:  javac Equipotential.java
 *  Execution:    java Equipotential n
 *  Dependencies: DeluxeCharge.java Picture.java
 *
 *  Potential value visualization for a set of charges.
 *
 *  % javac-introcs Equipotential.java
 *  % java-introcs  Equipotential 5
 *
 ******************************************************************************/

public class Equipotential  {

    public static void main(String[] args) {
        int SIZE = 800;
        double RADIUS = 500E-12;                     // real size (m)
        double eps = RADIUS / SIZE;                  // real size of 1 pixel
        double CHARGE_OF_ELECTRON = 1.60217733E-19;  // elementary charge (C)
        int n = Integer.parseInt(args[0]);           // number of charges
        DeluxeCharge[] charges;                      // the n random charges

        // n random charges
        charges = new DeluxeCharge[n];
        for (int i = 0; i < n; i++) {
            double x = StdRandom.uniform(0.0, RADIUS);
            double y = StdRandom.uniform(0.0, RADIUS);
            double k = CHARGE_OF_ELECTRON;
            if (StdRandom.bernoulli(0.5)) k = -k;
            charges[i] = new DeluxeCharge(x, y, k);
        }

        Picture picture = new Picture(SIZE, SIZE);

        // draw equipotential lines; compute potential and field strength at (x, y)
        for (int ix = 0; ix < SIZE; ix++) {
            for (int iy = 0; iy < SIZE; iy++) {
                double x = ix * RADIUS / SIZE;
                double y = iy * RADIUS / SIZE;

                // electric potential at (x, y)
                double potential = 0.0;
                for (int i = 0; i < n; i++) {
                    potential += charges[i].potentialAt(x, y);
                }

                // vector field (ex, ey) at (x, y) and total strength E
                double ex = 0.0, ey = 0.0;
                for (int i = 0; i < n; i++) {
                    ex += charges[i].fieldX(x, y);
                    ey += charges[i].fieldY(x, y);
                }
                double e = Math.sqrt(ex*ex + ey*ey);

                // draw if potential is < 1/2 pixel from a multiple of 5*potential (since E = grad V)
                // if ((Math.abs(potential) % 5) < 1.0 * e * eps) {
                if ((potential - Math.floor(potential/5) * 5) <  e*eps) {
                    picture.set(ix, SIZE-1-iy, StdDraw.WHITE);
                }
            }
        }

        picture.show();

    }
}

