/* R174: from-scratch census of signs on L3(n) (ordered words, i.e. A in L3(n); u!=v counted twice, u=v once)
   for non-square n == 1 (4), n < N.  Parametrisation: n = d*v - u with d = A = tu-1 == -1 (mod u), d >= 2u-1, v >= 2.
   Prints: n with 1<=|L3|<=6 (|L3|, N-), #all -1 among them, #n with N+ > N-, first few, min N-/|L3|.
   gcc -O2 -o /tmp/rhjc scripts/review_hj_census.c -lm ; /tmp/rhjc 200000 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int jac(long a, long n){int s=1;a%=n;while(a){while(!(a&1)){a>>=1;long r=n&7;if(r==3||r==5)s=-s;}
 long t=a;a=n;n=t;if((a&3)==3&&(n&3)==3)s=-s;a%=n;}return n==1?s:0;}
int main(int argc,char**argv){ long N=atol(argv[1]); int *P=calloc(N,4),*Mn=calloc(N,4);
 for(long u=2; 2*(2*u-1)-u<N; u++) for(long d=2*u-1; 2*d-u<N; d+=u) for(long v=2; d*v-u<N; v++){
   long n=d*v-u; if((n&3)!=1) continue; int j=jac(d,n); if(j==1)P[n]++; else if(j==-1)Mn[n]++; else {printf("BUG\n");return 1;} }
 long small=0, smallall=0, plusgt=0; double minr=2; long argmin=0;
 for(long n=5;n<N;n+=4){ long r=(long)sqrt((double)n); while(r*r>n)r--; while((r+1)*(r+1)<=n)r++;
  long np=P[n],nm=Mn[n],L=np+nm;
  if(r*r==n){ if(nm) printf("SQUARE with -1: %ld\n",n); continue; }
  if(L>=1 && L<=6){ small++; if(np==0) smallall++; printf("n=%ld |L3|=%ld N-=%ld\n",n,L,nm); }
  if(np>nm){ plusgt++; if(plusgt<=5) printf("N+>N- at %ld (%ld,%ld)\n",n,np,nm); }
  if(L>0){ double q=(double)nm/L; if(q<minr){minr=q;argmin=n;} }
 }
 printf("small=%ld allminus=%ld  #N+>N-=%ld  min N-/L=%g at %ld (N=%ld)\n",small,smallall,plusgt,minr,argmin,N); return 0; }
