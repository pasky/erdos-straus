/* z48 forestconn: exhaustive checks of the slot lemma
 *   (uv/n) = -1  <=>  4 | one of t,u,v,tu-1,tv-1      (n = tuv-u-v == 1 mod 4, gcd(uv,n)=1)
 * Modes:
 *   prime HI   : every edge of the full forest F_p, every prime p == 1 (mod 4), p < HI.
 *                Edges via the unique-parent rule; colour via Euler's criterion (independent
 *                of the Jacobi/sieve code in z48_forestconn_scan.c).
 *   box T UV   : every triple 1<=t<=T, 1<=u<=v<=UV with n=tuv-u-v>0, n==1 mod 4,
 *                gcd(uv,n)=1 (composite n allowed); Jacobi symbol computed directly.
 * Build: gcc -O2 -fopenmp -Wall -Wextra -Werror scripts/z48_forestconn_slot.c -o /tmp/z48fc_slot
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef uint64_t U;
static U powmod(U a, U e, U m){U r=1;a%=m;while(e){if(e&1)r=(unsigned __int128)r*a%m;a=(unsigned __int128)a*a%m;e>>=1;}return r;}
static int euler(U a, U p){U x=powmod(a%p,(p-1)/2,p);return x==1?1:(x==p-1?-1:0);}
static int jacobi(U a, U n){ /* n odd positive */
  int s=1; a%=n;
  while(a){ while(!(a&1)){a>>=1; U r=n&7; if(r==3||r==5) s=-s;}
    U t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) s=-s; a%=n; }
  return n==1?s:0;
}
static int slot(U t,U u,U v){
  return t%4==0||u%4==0||v%4==0||(t%4*(u%4)+3)%4==0||(t%4*(v%4)+3)%4==0;
}
int main(int argc,char**argv){
  if(argc==3&&!strcmp(argv[1],"prime")){
    U HI=strtoull(argv[2],0,10);
    char*comp=calloc(HI+1,1); for(U i=2;i*i<=HI;i++) if(!comp[i]) for(U j=i*i;j<=HI;j+=i) comp[j]=1;
    U nprimes=0,edges=0,neg=0,slotted=0,fail=0;
    #pragma omp parallel for schedule(dynamic,16) reduction(+:nprimes,edges,neg,slotted,fail)
    for(U p=5;p<HI;p+=4){
      if(comp[p]) continue;
      nprimes++;
      for(U v=2;v<=p+2;v++){
        if(v==p) continue;
        U a=(v-p%v)%v; if(!a) continue;
        if((p+v)%a) continue;
        /* gcd(a,v)=gcd(p,v)=1, so a*v | p+a+v */
        U t=(p+a+v)/(a*v);
        if(t*a*v!=p+a+v){ fail++; continue; }
        int s=euler(a,p)*euler(v,p);
        int sl=slot(t,a,v);
        edges++; if(s==-1) neg++; if(sl) slotted++;
        if((s==-1)!=sl){ fail++;
          #pragma omp critical
          printf("FAIL p=%lu u=%lu v=%lu t=%lu sign=%d slot=%d\n",(unsigned long)p,(unsigned long)a,(unsigned long)v,(unsigned long)t,s,sl);
        }
      }
    }
    printf("prime-mode HI=%lu primes(1 mod 4)=%lu edges=%lu negative=%lu slotted=%lu failures=%lu\n",
      (unsigned long)HI,(unsigned long)nprimes,(unsigned long)edges,(unsigned long)neg,(unsigned long)slotted,(unsigned long)fail);
    return fail?1:0;
  }
  if(argc==4&&!strcmp(argv[1],"box")){
    U T=strtoull(argv[2],0,10), UV=strtoull(argv[3],0,10);
    U cnt=0,neg=0,fail=0,sq=0,sqslot=0;
    #pragma omp parallel for schedule(dynamic,1) reduction(+:cnt,neg,fail,sq,sqslot)
    for(U t=1;t<=T;t++) for(U u=1;u<=UV;u++) for(U v=u;v<=UV;v++){
      U m=t*u*v; if(m<=u+v) continue; U n=m-u-v; if(n%4!=1) continue;
      int s=jacobi(u*v%n,n); if(s==0) continue;   /* gcd(uv,n)>1 */
      int sl=slot(t,u,v); cnt++; if(s==-1) neg++;
      U r=0; { U lo=0,hi=n<4000000000ULL?n:4000000000ULL; while(lo<hi){U mid=(lo+hi+1)/2; if(mid*mid<=n) lo=mid; else hi=mid-1;} r=lo; }
      if(r*r==n){ sq++; if(sl) sqslot++; }
      if((s==-1)!=sl){ fail++;
        #pragma omp critical
        printf("FAIL n=%lu t=%lu u=%lu v=%lu jac=%d slot=%d\n",(unsigned long)n,(unsigned long)t,(unsigned long)u,(unsigned long)v,s,sl);
      }
    }
    printf("box-mode T=%lu UV=%lu triples=%lu negative=%lu failures=%lu square_n=%lu square_n_with_slot=%lu\n",
      (unsigned long)T,(unsigned long)UV,(unsigned long)cnt,(unsigned long)neg,(unsigned long)fail,(unsigned long)sq,(unsigned long)sqslot);
    return fail?1:0;
  }
  fprintf(stderr,"usage: prime HI | box T UV\n"); return 2;
}
