// z55 TDO: compute T(h) = sum over m in (U^2,4U^2] with r=(-p mod m) in (2U,4U], r^2-4m>=1 of e(h sqrt(r^2-4m))
// usage: z55_tdo_T p U H   -> prints |E1|, |E1+|, N2 (integer w with (r±w)/2 in (U,2U]), then h Re Im |T|/sqrt(E1+)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  unsigned long long p=strtoull(argv[1],0,10); long long U=atoll(argv[2]); int H=atoi(argv[3]);
  double *re=calloc(H+1,sizeof(double)),*im=calloc(H+1,sizeof(double));
  long long E1=0,E1p=0,N2=0;
  for(long long m=U*U+1;m<=4*U*U;m++){
    long long r=(long long)((m-(long long)(p%m))%m);
    if(r<=2*U||r>4*U) continue;
    E1++;
    long long D=r*r-4*m; if(D<1) continue; E1p++;
    long double w=sqrtl((long double)D);
    long long wi=(long long)llroundl(w); if(wi*wi==D && (r-wi)%2==0){long long u=(r-wi)/2,B=(r+wi)/2; if(u>U&&B<=2*U&&u<B) N2++;}
    for(int h=1;h<=H;h++){ long double x=h*w; x-=floorl(x); double a=2*M_PI*(double)x; re[h]+=cos(a); im[h]+=sin(a);}
  }
  printf("p=%llu U=%lld E1=%lld E1p=%lld N2=%lld\n",p,U,E1,E1p,N2);
  for(int h=1;h<=H;h++) printf("%d %.4f %.4f %.4f\n",h,re[h],im[h],sqrt(re[h]*re[h]+im[h]*im[h])/sqrt((double)E1p));
  return 0;
}
