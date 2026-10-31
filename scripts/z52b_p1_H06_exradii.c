// Z1930: ES solutions 4/p = 1/X+1/Y+1/Z as exradii of a triangle with inradius p/4.
// s^2 = XY+YZ+ZX (= 4XYZ/p). Rational triangle iff s^2 is a square; integer sides iff s | X(Y+Z), Y(X+Z), Z(X+Y).
// For each prime p ≡ 1 (4) <= P: count all solutions X<=Y<=Z, #with s^2 square, #with integer sides.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static int isprime(u64 n){ if(n<2)return 0; for(u64 d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
static u64 isqrt(u64 n){ u64 r=(u64)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r; }
int main(int argc,char**argv){
  u64 P=atoll(argv[1]); u64 n=argc>2?atoll(argv[2]):0; // argv[2]=1: all n>=2 (print n with no rational triangle); else primes p≡1(4)
  long tot_sq=0, tot_int=0, nprimes=0, fail_sq=0, fail_int=0;
  for(u64 p=(n?2:5);p<=P;p+=(n?1:4)){ if(!n && !isprime(p)) continue; nprimes++;
    long cnt=0,csq=0,cint=0;
    for(u64 x=p/4+1;4*x<=3*p;x++){ u64 m=4*x-p, M=p*x;
      // factor M^2
      u64 pr[32]; int ex[32]; int k=0; u64 t=M;
      for(u64 d=2;d*d<=t;d++) if(t%d==0){ pr[k]=d; ex[k]=0; while(t%d==0){t/=d;ex[k]++;} ex[k]*=2; k++; }
      if(t>1){pr[k]=t;ex[k]=2;k++;}
      // enumerate divisors
      u64 divs[200000]; int nd=1; divs[0]=1;
      for(int i=0;i<k;i++){ int cur=nd; u64 pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
      u128 M2=(u128)M*M;
      for(int j=0;j<nd;j++){ u64 d=divs[j]; if(d>M) continue; if((d+M)%m) continue;
        u64 y=(d+M)/m; u128 zz=(M2/d+M); if(zz%m) continue; u64 z=(u64)(zz/m); if(y<x) continue;
        cnt++;
        u128 e2=(u128)x*y+(u128)y*z+(u128)z*x; if(e2>>64){ continue; }
        u64 s=isqrt((u64)e2); if((u128)s*s!=e2) continue; csq++;
        if(((u128)x*(y+z))%s==0 && ((u128)y*(x+z))%s==0 && ((u128)z*(x+y))%s==0){ cint++;
          if(!n && p<200) printf("  p=%llu X=%llu Y=%llu Z=%llu s=%llu\n",p,x,y,z,s);} }
    }
    if(csq==0) fail_sq++; if(cint==0) fail_int++;
    tot_sq+=csq; tot_int+=cint;
    if((!n && (p<300 || csq==0)) || (n && cint==0)) printf("p=%llu sols=%ld rational=%ld integer=%ld\n",p,cnt,csq,cint);
  }
  printf("primes=%ld  primes_with_no_rational=%ld primes_with_no_integer=%ld  tot_rational=%ld tot_int=%ld\n",nprimes,fail_sq,fail_int,tot_sq,tot_int);
}
