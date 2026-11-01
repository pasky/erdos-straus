// z52d pass2 SK1 (Z0815 proxy): class number h(-4p) of Q(sqrt(-p)) for primes 5<=p<=N via reduced-form count.
// Output: p h   (D=-4p is a fundamental discriminant for p = 1 mod 4 and for p = 3 mod 4 with -p=1 mod 4 ... p>2 prime: D=-4p fundamental when p = 1 or 2 mod 4 => we use -4p for all odd p, check fundamentality: -4p is fundamental iff -p = 2,3 mod 4 => p = 1 mod 4 only? see note)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  char*comp=calloc(N+1,1); comp[0]=comp[1]=1;
  for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  for(long p=3;p<=N;p+=2){ if(comp[p]) continue;
    long D=-4*p; long h=0; long amax=(long)sqrt((double)(-D)/3.0)+1;
    for(long a=1;a<=amax;a++) for(long b=-a+1;b<=a;b++){
      long num=b*b-D; if(num%(4*a)) continue; long c=num/(4*a); if(c<a) continue;
      if(c==a && b<0) continue;
      // primitive
      long g=labs(a); long x=labs(b); while(x){long t=g%x; g=x; x=t;} g=labs(g); x=c; long gg=g; long y=labs(x); while(y){long t=gg%y; gg=y; y=t;} if(gg!=1) continue;
      h++; }
    printf("%ld %ld\n",p,h);
  }
  return 0;
}
