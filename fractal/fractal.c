/*
  This program is an adaptation of the Mandelbrot program
  from the Programming Rosetta Stone, see
  http://rosettacode.org/wiki/Mandelbrot_set
  Compile the program with:
  gcc -o mandelbrot -O4 mandelbrot.c
  Usage:

  ./mandelbrot <xmin> <xmax> <ymin> <ymax> <maxiter> <xres> <out.ppm>
  Example:
  ./mandelbrot 0.27085 0.27100 0.004640 0.004810 1000 1024 pic.ppm
  The interior of Mandelbrot set is black, the levels are gray.
  If you have very many levels, the picture is likely going to be quite
  dark. You can postprocess it to fix the palette. For instance,
  with ImageMagick you can do (assuming the picture was saved to pic.ppm):
  convert -normalize pic.ppm pic.png
  The resulting pic.png is still gray, but the levels will be nicer. You
  can also add colors, for instance:
  convert -negate -normalize -fill blue -tint 100 pic.ppm pic.png
  See http://www.imagemagick.org/Usage/color_mods/ for what ImageMagick
  can do. It can do a lot.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

void main(){}; // dummy main

int generate_fractal(
    double xmin,
    double xmax,
    double ymin,
    double ymax,
    char *max_iter,
    char *x_res,
    char *file_name)
{
  /* Parse the command line arguments. */
  // if (argc != 8) {
  //   printf("Usage:   %s <xmin> <xmax> <ymin> <ymax> <maxiter> <xres> <out.ppm>\n", argv[0]);
  //   printf("Example: %s 0.27085 0.27100 0.004640 0.004810 1000 1024 pic.ppm\n", argv[0]);
  //   exit(EXIT_FAILURE);
  // }

  // print the arguments
  // printf("x_min: %s", x_min);
  // printf("x_max: %s", x_max);
  // printf("y_min: %s", y_min);
  // printf("y_max: %s", y_max);
  // printf("max_iter: %s", max_iter);
  // printf("x_res: %s", x_res);
  // printf("file_name: %s", file_name);

  // /* The window in the plane. */
  // const double xmin = atof(x_min);
  // const double xmax = atof(x_max);
  // const double ymin = atof(y_min);
  // const double ymax = atof(y_max);

  printf("\nxmin: %lf", xmin);
  printf("xmax: %lf", xmax);
  printf("ymin: %lf", ymin);
  printf("ymax: %lf", ymax);

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