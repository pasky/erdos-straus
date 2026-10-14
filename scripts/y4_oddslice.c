/* O212 (BRAINSTORM/y4_oneodd_slices): census of the ONE-ODD five slices of ES and of S_8.
 * Words (t,u,v) of odd n: t u v - u - v = n, A = tu - 1, A* = tv - 1 (gcd(A,n)=1 automatic for prime n not | A).
 * One-odd slice: some slot X in {A, A*, t, u, v} with v2(X) = 2.  S_8: some slot with 8 | X.
 * The slice solution is verified exactly in 128-bit (m/n == sum) and its parity is checked.
 * usage: y4_oddslice N P  -> primes 3 <= p <= N: list p with S4odd(p) empty, and p with S8(p) empty
 *        y4_oddslice N A  -> all odd non-squares n <= N: list n with S8 but no S4odd; S4-empty n on stderr
 *        y4_oddslice N S  -> odd squares k^2 <= N, k > 1: count with S4odd nonempty / S8 nonempty
 */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static int v2(u64 x){ int e=0; while(!(x&1)){x>>=1;e++;} return e; }
static void chk(u64 n,u64 x,u64 y,u64 z,int want_odd){
  /* 4/n = 1/x+1/y+1/z  <=>  4xyz = n(yz+xz+xy) */
  u128 l=(u128)4*x*y*z, r=(u128)n*((u128)y*z+(u128)x*z+(u128)x*y);
  int od=(x&1)+(y&1)+(z&1);
  if(l!=r || (want_odd? od!=1 : od!=0)){ fprintf(stderr,"CHECK FAIL n=%llu\n",n); exit(2);} }
/* examine slot X with given solution builder; returns bit0 = one-odd hit, bit1 = S8 hit */
static int word(u64 n,u64 t,u64 u,u64 v){
  u64 A=t*u-1, As=t*v-1; int r=0;
  if(A%4==0){ u64 d=A/4; int e=v2(A); chk(n,As*d*n,v*d,As*v*d,e==2); r|= e==2?1:2; }
  if(As%4==0){ u64 d=As/4; int e=v2(As); chk(n,A*d*n,u*d,A*u*d,e==2); r|= e==2?1:2; }
  if(t%4==0){ u64 c=t/4; int e=v2(t); chk(n,u*v*c,u*c*n,v*c*n,e==2); r|= e==2?1:2; }
  if(u%4==0){ u64 w=u/4; int e=v2(u); chk(n,w*As,t*n*w,t*n*w*As,e==2); r|= e==2?1:2; }
  if(v%4==0){ u64 w=v/4; int e=v2(v); chk(n,w*A,t*n*w,t*n*w*A,e==2); r|= e==2?1:2; }
  return r; }
static int gcdu(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a==1; }
/* returns bits: 1 if S4odd nonempty, 2 if S8 nonempty (early stop when both found) */
static int scan(u64 n){ int have=0;
  for(u64 t=1;t<=n+2 && have!=3;t++){
    for(u64 u=1;;u++){ if(t*u*u>n+2*u) break; if(t*u<2) continue;
      if((n+u)%(t*u-1)) continue; u64 v=(n+u)/(t*u-1); if(v<u) continue;
      if(!gcdu(t*u-1,n)) continue;
      have|=word(n,t,u,v); if(have==3) break; } }
  return have; }
int main(int argc,char**argv){ u64 N=strtoull(argv[1],0,10); char mode=argv[2][0];
  if(mode=='P'){ char*c=calloc(N+1,1); for(u64 i=2;i*i<=N;i++) if(!c[i]) for(u64 j=i*i;j<=N;j+=i) c[j]=1;
    long cnt=0,f4=0,f8=0; printf("S4odd empty at primes:");
    static u64 l8[100000]; long n8=0;
    for(u64 p=3;p<=N;p+=2){ if(c[p]) continue; cnt++; int h=scan(p);
      if(!(h&1)){ printf(" %llu",p); f4++; } if(!(h&2)){ if(n8<100000) l8[n8++]=p; f8++; } }
    printf("\nS8 empty at primes:"); for(long i=0;i<n8;i++) printf(" %llu",l8[i]);
    printf("\nprimes %ld, S4odd empty %ld, S8 empty %ld\n",cnt,f4,f8); }
  else if(mode=='A'){ long cnt=0,a=0,b=0; printf("odd n<=N (k^2 excluded): S4 nonempty but S4odd empty:");
    for(u64 n=3;n<=N;n+=2){ u64 k=1; while((k+1)*(k+1)<=n) k++; if(k*k==n) continue; cnt++; int h=scan(n);
      if(h==2){ printf(" %llu",n); a++; } if(h==0){ b++; fprintf(stderr,"S4 empty: %llu\n",n);} }
    printf("\nchecked %ld, S4odd-empty-but-S8 %ld, S4 empty %ld\n",cnt,a,b); }
  else { long cnt=0,h1=0,h2=0; for(u64 k=3;k*k<=N;k+=2){ cnt++; int h=scan(k*k); h1+=h&1; h2+=(h>>1)&1; }
    printf("odd squares %ld: S4odd nonempty %ld, S8 nonempty %ld\n",cnt,h1,h2); }
  return 0; }
