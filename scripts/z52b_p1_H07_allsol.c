// Z2771: enumerate all unordered solutions x<=y<=z of 4/p = 1/x+1/y+1/z for primes p ≡ 1 (mod 4), p <= N.
// Output: "p x y z" lines (x,y,z may exceed 2^64? z <= p*x*(..) ~ p^2 x^2 small for p<=1e5: fits in unsigned __int128 -> print as u64 checked)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static int spf[2000000];
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  long N=atol(argv[1]); long X=N+2;
  for(long i=2;i<=X;i++) if(!spf[i]) for(long j=i;j<=X;j+=i) if(!spf[j]) spf[j]=i;
  for(long p=5;p<=N;p+=4){ if(spf[p]!=p) continue;
    for(u64 x=p/4+1; 4*x<=3*(u64)p; x++){
      u64 t=4*x-p; u64 B=(u64)p*x; u64 g=gcdu(t,B); u64 A=t/g; B/=g;
      // factor B: B = p^a * x', remove
      u64 pr[32]; int ex[32]; int k=0; u64 m=B;
      if(m%p==0){pr[k]=p;ex[k]=0;while(m%p==0){m/=p;ex[k]++;}k++;}
      while(m>1){u64 q=spf[m];pr[k]=q;ex[k]=0;while(m%q==0){m/=q;ex[k]++;}k++;}
      // enumerate divisors delta of B^2 with delta<=B
      u64 divs[200000]; int nd=1; divs[0]=1;
      for(int i=0;i<k;i++){int cur=nd; u64 pw=1; for(int e=1;e<=2*ex[i];e++){pw*=pr[i]; for(int j=0;j<cur;j++){u128 v=(u128)divs[j]*pw; if(v<=B) divs[nd++]=(u64)v;}}}
      for(int j=0;j<nd;j++){u64 d=divs[j]; if((B+d)%A) continue; u128 B2=(u128)B*B; u64 e2=(u64)(B2/d); if((B+e2)%A) continue;
        u64 y=(B+d)/A, z=(B+e2)/A; if(y<x) continue; if(y>z) continue;
        printf("%ld %llu %llu %llu\n",p,x,y,z);}
    }
  }
}
