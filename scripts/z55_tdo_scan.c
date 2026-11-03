// z55 TDO: scan primes p >= p0 (count n), U=floor(p^{1/4}) (or scaled by c), report per p max_h<=H |T(h)|, E1p
// usage: z55_tdo_scan p0 n H c   (U = floor(c*p^{1/4}))
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int isprime(unsigned long long n){ if(n<2)return 0; for(unsigned long long d=2;d*d<=n;d++) if(n%d==0) return 0; return 1;}
int main(int argc,char**argv){
  unsigned long long p=strtoull(argv[1],0,10); int n=atoi(argv[2]); int H=atoi(argv[3]); double c=atof(argv[4]);
  int primeonly = argc>5 ? atoi(argv[5]) : 1;
  double *re=malloc((H+1)*sizeof(double)),*im=malloc((H+1)*sizeof(double));
  for(int t=0;t<n;p++){
    if(primeonly && !isprime(p)) continue; t++;
    long long U=(long long)floor(c*pow((double)p,0.25));
    for(int h=0;h<=H;h++){re[h]=0;im[h]=0;}
    long long E1p=0;
    for(long long m=U*U+1;m<=4*U*U;m++){
      long long r=(long long)((m-(long long)(p%m))%m);
      if(r<=2*U||r>4*U) continue;
      long long D=r*r-4*m; if(D<1) continue; E1p++;
      long double w=sqrtl((long double)D);
      for(int h=1;h<=H;h++){ long double x=h*w; x-=floorl(x); double a=2*M_PI*(double)x; re[h]+=cos(a); im[h]+=sin(a);}
    }
    double mx=0; int hm=0; double s2=0;
    for(int h=1;h<=H;h++){double a=sqrt(re[h]*re[h]+im[h]*im[h]); s2+=a*a; if(a>mx){mx=a;hm=h;}}
    printf("%llu %lld %lld %.3f %d %.3f\n",p,U,E1p,mx,hm,s2/H);
  }
  return 0;
}
