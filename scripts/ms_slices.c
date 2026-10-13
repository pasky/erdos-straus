/* O197: the five length-3 HJ slices for numerator m (DEDEKIND_ES Thm 4.5 generalised).
 * For n >= 3 enumerate all (t,u,v) in Z_{>=1}^3 with t*u*v - u - v = n and test the five m-slice conditions
 *   (I)  m | tu-1 : m/n = 1/(A* d n) + 1/(v d) + 1/(A* v d), A = tu-1, A* = tv-1, d = A/m
 *   (I') m | tv-1 : same with u <-> v
 *   (T)  m | t    : m/n = 1/(u v c) + 1/(u c n) + 1/(v c n), c = t/m
 *   (U)  m | u    : m/n = 1/(w f) + 1/(t n w) + 1/(t n w f), w = u/m, f = tv-1
 *   (V)  m | v    : same with u <-> v
 * Every hit's triple is verified exactly (128-bit).  Degenerate denominators (0) are skipped and counted.
 * usage: ms_slices m N P      -> primes p <= N (p !| m): print primes with NO slice hit (and counts per p mod 8*m)
 *        ms_slices m N S      -> odd squares k^2 <= N: print number with a hit
 *        ms_slices m n1 one   -> details for a single n
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef __int128 i128;
static int M; static long degenerate=0;
static int verify(u64 n,u128 x,u128 y,u128 z){ if(!x||!y||!z){degenerate++;return 0;}
  /* m/n == 1/x+1/y+1/z  <=>  m*x*y*z == n*(yz+xz+xy) ; sizes: x,y,z < 2^40 for n<2^20-ish; use u128 carefully */
  u128 lhs=(u128)M*x*y; u128 rhs=(u128)n*(y+x); /* m/n - 1/z = (x+y)/(xy)  <=> (m z - n) x y == n z (x+y) */
  u128 a=(u128)M*z; if(a<=n) return 0; a-=n; return a*x*y == (u128)n*z*(x+y) ? 1 : (lhs==rhs && 0); }
/* returns number of slice hits; flags[k] counts per slice */
static long slices(u64 n,long*fl,int stop,int show){ long hits=0; if(fl) memset(fl,0,5*sizeof(long));
  for(u64 t=1;t<=n+2;t++){
    for(u64 u=1;;u++){ u64 tu=t*u; if(tu<2) continue; if(t*u*u>n+2*u) break; /* u<=v region */
      if((n+u)%(tu-1)) continue; u64 v=(n+u)/(tu-1); if(v<u) continue;
      for(int sw=0;sw<2;sw++){ u64 U=sw?v:u, V=sw?u:v; if(sw&&u==v) break;
        u64 A=t*U-1, As=t*V-1; int ok[5]={0,0,0,0,0};
        if(A%M==0){ u64 d=A/M; ok[0]=verify(n,(u128)As*d*n,(u128)V*d,(u128)As*V*d);
          if(!ok[0]&&d&&As){fprintf(stderr,"slice I verify FAIL n=%llu t=%llu u=%llu v=%llu\n",n,t,U,V);exit(2);} }
        if(t%M==0){ u64 c=t/M; ok[2]=verify(n,(u128)U*V*c,(u128)U*c*n,(u128)V*c*n);
          if(!ok[2]){fprintf(stderr,"slice T verify FAIL n=%llu\n",n);exit(2);} }
        if(U%M==0){ u64 w=U/M, f=As; ok[3]=verify(n,(u128)w*f,(u128)t*n*w,(u128)t*n*w*f);
          if(!ok[3]&&f){fprintf(stderr,"slice U verify FAIL n=%llu t=%llu u=%llu v=%llu\n",n,t,U,V);exit(2);} }
        /* (I') and (V) are the u<->v images: counted via sw loop as slots 0 and 3 of the swapped triple */
        int any=ok[0]||ok[2]||ok[3];
        if(fl){ fl[0]+=ok[0]; fl[2]+=ok[2]; fl[3]+=ok[3]; }
        if(any){ hits++; if(show) printf("  t=%llu u=%llu v=%llu A=%llu  I:%d T:%d U:%d\n",t,U,V,A,ok[0],ok[2],ok[3]); if(stop) return hits; }
      } } }
  return hits; }
static int isprime(u64 n){ if(n<2) return 0; for(u64 q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
int main(int argc,char**argv){ M=atoi(argv[1]); u64 N=strtoull(argv[2],0,10); char mode=argv[3][0];
  if(mode=='o'){ long fl[5]; long h=slices(N,fl,0,1); printf("n=%llu m=%d hits=%ld (I:%ld T:%ld U:%ld)\n",N,M,h,fl[0],fl[2],fl[3]); return 0; }
  if(mode=='P'){ long cnt=0,fails=0; printf("m=%d primes<=%llu with no five-slice hit:",M,N);
    for(u64 p=3;p<=N;p++){ if(!isprime(p)||M%p==0) continue; cnt++; if(!slices(p,0,1,0)){ fails++; if(fails<=400) printf(" %llu",p);} }
    printf("\nchecked %ld primes, no-hit %ld, degenerate %ld\n",cnt,fails,degenerate); }
  if(mode=='S'){ long cnt=0,hit=0; for(u64 k=3;k*k<=N;k+=2){ u64 a=k,b=2*(u64)M; while(b){u64 r=a%b;a=b;b=r;} if(a!=1) continue; cnt++; if(slices(k*k,0,1,0)) hit++; }
    printf("m=%d odd squares<=%llu: %ld checked, %ld with a five-slice hit\n",M,N,cnt,hit); }
  return 0; }
