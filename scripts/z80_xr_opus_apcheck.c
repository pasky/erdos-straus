/* Opus cross-lab review of notes/z80/EXTREME.md: independent R8 window check.
   For every n == res (mod step) in [lo,hi] that is prime (deterministic
   Miller-Rabin, 12 bases, valid < 3.3e24), search a witness 8uBC-u-B = n:
   first (u,C) with u*C <= 4000, f=8uC-1 | n+u; otherwise exhaustive over the
   smallest of (u,B,C) <= cube bound with the other two by divisibility
   (u<=B orientation, own loops).  Prints primes count and every zero. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long U;typedef unsigned __int128 L;
static U mulm(U a,U b,U m){return (L)a*b%m;}
static U pw(U a,U e,U m){U r=1;a%=m;while(e){if(e&1)r=mulm(r,a,m);a=mulm(a,a,m);e>>=1;}return r;}
static int isprime(U n){if(n<2)return 0;static const U B[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){if(n%B[i]==0)return n==B[i];}U d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){U x=pw(B[i],d,n);if(x==1||x==n-1)continue;int ok=0;for(int r=1;r<s;r++){x=mulm(x,x,n);if(x==n-1){ok=1;break;}}if(!ok)return 0;}return 1;}
/* exhaustive: n = 8uBC-u-B, u<B (u=B impossible). Smallest letter m.
   (i) u smallest (u<=C): f=8uC-1 | n+u with C>=u, B=(n+u)/f>u: loop C from u while (8uC-1)*(u+1)<=n+u.
       -> too long for small u; instead loop over B? use (ii)/(iii) split below. */
static int exhaustive(U n){
  /* Case C is the smallest letter: C<=u<B. (8uC-1)B=n+u, loop C, u with (8uC-1)(u+1)<=n+u. */
  for(U C=1;8*C*C*C<=n+2*C;C++)for(U u=C;(L)(8*u*C-1)*(u+1)<=(L)n+u;u++){U f=8*u*C-1;if((n+u)%f==0&&(n+u)/f>u)return 1;}
  /* Case u smallest, u<C, u<B: for fixed u, C>u, B>u: (8uC-1)B=n+u. Loop B (B>u) with (8u(u+1)-1)B<=n+u:
     B | n+u... loop over B up to (n+u)/(8u(u+1)-1) can be large; loop instead over the smaller of B,C. */
  for(U u=1;8*u*u*u<=n+2*u;u++){
    /* sub-case C<=B: loop C>u while (8uC-1)*C<=n+u */
    for(U C=u+1;(L)(8*u*C-1)*C<=(L)n+u;C++){U f=8*u*C-1;if((n+u)%f==0&&(n+u)/f>=C)return 1;}
    /* sub-case B<C: loop B>u while (8uB-1)*B<n+u ; need (n+u)/B == -1 mod 8u */
    for(U B=u+1;(L)(8*u*(B+1)-1)*B<=(L)n+u;B++){if((n+u)%B)continue;U f=(n+u)/B;if((f+1)%(8*u)==0&&(f+1)/(8*u)>B)return 1;}
  }
  return 0;}
int main(int ac,char**av){U step=strtoull(av[1],0,10),res=strtoull(av[2],0,10),lo=strtoull(av[3],0,10),hi=strtoull(av[4],0,10);
  U n=lo+(res+step-lo%step)%step;long np=0,ex=0,z=0;
  for(;n<=hi;n+=step){if(!isprime(n))continue;np++;int ok=0;
    for(U u=1;u<=4000&&!ok;u++)for(U C=1;u*C<=4000;C++){U f=8*u*C-1;if((n+u)%f==0){ok=1;break;}}
    if(!ok){ex++;if(!exhaustive(n)){z++;printf("ZERO %llu\n",n);}}}
  printf("# step=%llu res=%llu lo=%llu hi=%llu primes=%ld exhaustive=%ld zeros=%ld\n",step,res,lo,hi,np,ex,z);return 0;}
