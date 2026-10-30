// Word-count sieve: for n<=N count ordered triples (t,u,v)>=1 with n = t*u*v - u - v, split by class:
// col0 W: all t,u,v>=1 ; col1 I3: t,u,v>=3 ; col2 R: t in 4Z (the (*) count, t=4C) ;
// col3 Uv: v>=3 and v in 4Z or v = -n mod 8 (U-certificate count incl. cofactor-1) ; col4 ESC: some coordinate of (t,u,v) in 4Z u (8Z-n)
// col5 T1 : t==1 ; col6: t==2
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
  uint32_t *c=calloc((size_t)(N+1)*7,4);
  for(long t=1;t<=N+2;t++) for(long u=1;;u++){ if(t*u<2){continue;} if(t*u-1 > N+u) break; // v>=1: n = v(tu-1)-u >= tu-1-u
     long vmax=(N+u)/(t*u-1); if(vmax<1)break;
     for(long v=1;v<=vmax;v++){ long n=t*u*v-u-v; if(n<1)continue; if(n>N)break;
       uint32_t *r=c+n*7; r[0]++;
       if(t>=3&&u>=3&&v>=3) r[1]++;
       if(t%4==0) r[2]++;
       int vc = (v%4==0)||(((v+n)%8)==0);
       if(v>=3&&vc) r[3]++;
       int tc=(t%4==0)||(((t+n)%8)==0), uc=(u%4==0)||(((u+n)%8)==0);
       if(tc||uc||vc) r[4]++;
       if(t==1) r[5]++; if(t==2) r[6]++;
     }
     if(u> N+2) break;
  }
  for(long n=1;n<=N;n++){uint32_t*r=c+n*7; printf("%ld %u %u %u %u %u %u %u\n",n,r[0],r[1],r[2],r[3],r[4],r[5],r[6]);}
}
