#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

void square(int x)
{
  printf("square: %d", x);
}

int generate_fractal(
    char *x_min,
    char *x_max,
    char *y_min,
    char *y_max,
    char *max_iter,
    char *x_res,
    char *file_name)
{
  {
    /* Parse the command line arguments. */
    // if (argc != 8) {
    //   printf("Usage:   %s <xmin> <xmax> <ymin> <ymax> <maxiter> <xres> <out.ppm>\n", argv[0]);
    //   printf("Example: %s 0.27085 0.27100 0.004640 0.004810 1000 1024 pic.ppm\n", argv[0]);
    //   exit(EXIT_FAILURE);
    // }

    /* The window in the plane. */
    const double xmin = atof(x_min);
    const double xmax = atof(x_max);
    const double ymin = atof(y_min);
    const double ymax = atof(y_max);

    /* Maximum number of iterations, at most 65535. */
    const uint16_t maxiter = (unsigned short)atoi(max_iter);

    /* Image size, width is given, height is computed. */
    const int xres = atoi(x_res);
    const int yres = (xres * (ymax - ymin)) / (xmax - xmin);

    /* The output file name */
    const char *filename = file_name;

    /* Open the file and write the header. */
    FILE *fp = fopen(filename, "wb");
    char *comment = "# Mandelbrot set"; /* comment should start with # */

    /*write ASCII header to the file*/
    fprintf(fp,
            "P6\n# Mandelbrot, xmin=%lf, xmax=%lf, ymin=%lf, ymax=%lf, maxiter=%d\n%d\n%d\n%d\n",
            xmin, xmax, ymin, ymax, maxiter, xres, yres, (maxiter < 256 ? 256 : maxiter));

    /* Precompute pixel width and height. */
    double dx = (xmax - xmin) / xres;
    double dy = (ymax - ymin) / yres;

    double x, y; /* Coordinates of the current point in the complex plane. */
    double u, v; /* Coordinates of the iterated point. */
    int i, j;    /* Pixel counters */
    int k;       /* Iteration counter */
    for (j = 0; j < yres; j++)
    {
      y = ymax - j * dy;
      for (i = 0; i < xres; i++)
      {
        double u = 0.0;
        double v = 0.0;
        double u2 = u * u;
        double v2 = v * v;
        x = xmin + i * dx;
        /* iterate the point */
        for (k = 1; k < maxiter && (u2 + v2 < 4.0); k++)
        {
          v = 2 * u * v + y;
          u = u2 - v2 + x;
          u2 = u * u;
          v2 = v * v;
        };
        /* compute  pixel color and write it to file */
        if (k >= maxiter)
        {
          /* interior */
          const unsigned char black[] = {0, 0, 0, 0, 0, 0};
          fwrite(black, 6, 1, fp);
        }
        else
        {
          /* exterior */
          unsigned char color[6];
          color[0] = k >> 8;
          color[1] = k & 255;
          color[2] = k >> 8;
          color[3] = k & 255;
          color[4] = k >> 8;
          color[5] = k & 255;
          fwrite(color, 6, 1, fp);
        };
      }
    }
    fclose(fp);
    return 0;
  }
}