#include <stdio.h>
int main() {
    char a;
    unsigned char b;
    signed char c;
    int d ;
    unsigned int e;
    signed int f;
    short int g;
    unsigned short int h;
    signed short int i;
    long int j;
    long long int k;
    signed long int l;
    unsigned long int m;
    unsigned long long int n;
    float o;
    double p;
    long double q;
  printf("size of char                  = %d bytes\n", sizeof(a));
  printf("size of unsigned char         = %d bytes\n", sizeof(b));
  printf("size of signed char           = %d bytes\n", sizeof(c));
  printf("size of int                   = %d bytes\n", sizeof(d));
  printf("size of unsigned int          = %d bytes\n", sizeof(e));
  printf("size of signed int            = %d bytes\n", sizeof(f));
  printf("size of short int             = %d bytes\n", sizeof(g));
  printf("size of unsigned short int    = %d bytes\n", sizeof(h));
  printf("size of signed short int      = %d bytes\n", sizeof(i));
  printf("size of long int              = %d bytes\n", sizeof(j));
  printf("size of long long int         = %d bytes\n", sizeof(k));
  printf("size of signed long int       = %d bytes\n", sizeof(l));
  printf("size of unsigned long int     = %d bytes\n", sizeof(m));
  printf("size of unsigned long long int= %d bytes\n", sizeof(n));
  printf("size of float                 = %d bytes\n", sizeof(o));
  printf("size of double                = %d bytes\n", sizeof(p));
  printf("size of long double           = %d bytes\n", sizeof(q));
  return 0;
}
