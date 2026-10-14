/* R212 from-scratch slice census on length-3 words (t,u,v): t u v - u - v = n, A = tu-1, A* = tv-1.
 * Five m-slices: m | A, m | A*, m | t, m | u, m | v.  The slice solution (MODEL_SPECIFIC Lemma 3.0 formulas,
 * recomputed here) is built, verified exactly in 128-bit, and its parity (number of odd denominators) recorded.
 * Enumeration is complete: t=1: (u-1)(v-1) = n+1; t=2: (2u-1)(2v-1) = 2n+1; t>=3: wlog u<=v (slices are u<->v
 * symmetric), then tu-1 <= (n+u)/u.  Also t, u arbitrary handled via these three cases.
 * usage: review_r212_slices m mode NMIN NMAX pop
 *   mode: any | odd (exactly one odd denominator) | even (all even)
 *   pop:  p (primes) | c (odd composite non-squares) | s (odd squares)
 * prints every n in the population with NO slice solution of the requested parity. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef __int128 i128;
static int M, MODE; static u64 N;
static int ok_sol(i128 a, i128 b, i128 c){ /* verify M/N = 1/a+1/b+1/c, return #odd */
  if(a<=0||b<=0||c<=0){ fprintf(stderr,"nonpositive\n"); exit(1);}
  if((i128)M*a*b*c != (i128)N*(b*c+a*c+a*b)){ fprintf(stderr,"VERIFY FAIL n=%llu\n",N); exit(1);}
  return (int)(a&1)+(int)(b&1)+(int)(c&1);
}
static int want(int odd){ if(MODE==0) return 1; if(MODE==1) return odd==1; return odd==0; }
static int word(i128 t, i128 u, i128 v){
  i128 A=t*u-1, As=t*v-1, n=N; int hit=0;
  if(A>0 && A%M==0){ i128 d=A/M; if(want(ok_sol(As*d*n, v*d, As*v*d))) hit=1; }
  if(!hit && As>0 && As%M==0){ i128 d=As/M; if(want(ok_sol(A*d*n, u*d, A*u*d))) hit=1; }
  if(!hit && t%M==0){ i128 c=t/M; if(want(ok_sol(u*v*c, u*c*n, v*c*n))) hit=1; }
  if(!hit && u%M==0 && As>0){ i128 w=u/M, f=As; if(want(ok_sol(w*f, t*n*w, t*n*w*f))) hit=1; }
  if(!hit && v%M==0 && A>0){ i128 w=v/M, f=A; if(want(ok_sol(w*f, t*n*w, t*n*w*f))) hit=1; }
  return hit;
}
static int has(u64 n){
  N=n;
  /* t>=3 first (small u), then t=1,2 */
  for(u64 u=1;;u++){
    u64 tmax = ((n+u)/u + 1)/u; if(tmax<3) break;
    for(u64 t=3;t<=tmax;t++){ u64 A=t*u-1; if((n+u)%A) continue; u64 v=(n+u)/A; if(v<u) continue; if(word(t,u,v)) return 1; }
  }
  for(u64 a=1;a*a<=n+1;a++) if((n+1)%a==0){ u64 b=(n+1)/a; if(word(1,a+1,b+1)) return 1; }
  for(u64 a=1;a*a<=2*n+1;a+=2) if((2*n+1)%a==0){ u64 b=(2*n+1)/a; if(word(2,(a+1)/2,(b+1)/2)) return 1; }
  return 0;
}
static int isprime(u64 n){ if(n<2) return 0; for(u64 q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
static int issq(u64 n){ u64 r=1; while(r*r<n) r++; return r*r==n; }
int main(int argc,char**argv){
  M=atoi(argv[1]); MODE = !strcmp(argv[2],"any")?0: !strcmp(argv[2],"odd")?1:2;
  u64 a=atoll(argv[3]), b=atoll(argv[4]); char pop=argv[5][0];
  char *comp = calloc(b+1,1); for(u64 i=2;i*i<=b;i++) if(!comp[i]) for(u64 j=i*i;j<=b;j+=i) comp[j]=1;
  long cnt=0, miss=0;
  for(u64 n=(a|1); n<=b; n+=2){
    if(n<3) continue; if(M%2==1 && n%M==0) continue;
    int pr = !comp[n], sq = issq(n);
    if(pop=='p' && !pr) continue; if(pop=='c' && (pr||sq)) continue; if(pop=='s' && !sq) continue;
    cnt++; if(!has(n)){ miss++; printf("%llu ",n); fflush(stdout);} }
  printf("\nm=%d mode=%s pop=%c range=[%llu,%llu] tested=%ld empty=%ld\n",M,argv[2],pop,a,b,cnt,miss);
  return 0;
}
