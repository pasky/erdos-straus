/* O197 (MODEL_SPECIFIC.md): complete search for m/n = 1/x + 1/y + 1/z in positive integers.
 * Method (classical ES finiteness, written from scratch): x <= y <= z, n/m < x <= 3n/m,
 * A = m x - n, B = n x, g = gcd(A,B), A' = A/g, B' = B/g, (A'y - B')(A'z - B') = B'^2,
 * d = A'y - B' a divisor of B'^2 with d <= B', d = -B' (mod A'), y = (d+B')/A' >= x.
 * usage:
 *   ms_census m N p        -> primes 3 <= p <= N, p !| m : list those with NO solution
 *   ms_census m N s        -> odd k, k^2 <= N, gcd(k,2m)=1: list k^2 with NO solution
 *   ms_census m N a        -> all n, 2 <= n <= N : list those with NO solution
 *   optional 4th arg (modes p,s,a): K -> only solutions with exactly K odd denominators count
 *   ms_census m LO c HI    -> primes LO <= p <= HI: print "p count count_alleven count_oneodd count_typeI count_typeII"
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;
static int *spf; static long SPF_N;
static void sieve(long N){ spf = calloc(N+1,sizeof(int)); SPF_N=N;
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i; }
static u64 gcdu(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
/* factor v (<= SPF_N) adding exponent*mult into (pr,ex) */
static int addf(u64 v,u64*pr,int*ex,int k,int mult){
  while(v>1){ u64 q = (u64)spf[v]; int e=0; while(v%q==0){v/=q;e++;}
    int i; for(i=0;i<k;i++) if(pr[i]==q){ex[i]+=e*mult;break;}
    if(i==k){pr[k]=q;ex[k]=e*mult;k++;} }
  return k; }
static int PARFILT=-1; /* if >=0: only count solutions with exactly PARFILT odd denominators */
static long long count_n(int m,u64 n,int stop,long long*cnt_out){
  /* cnt_out: [0]=total [1]=alleven [2]=oneodd [3]=typeI(n|x only) [4]=typeII(n|y,z, n!|x) */
  long long c=0; if(cnt_out) memset(cnt_out,0,5*sizeof(long long));
  u64 xlo = n/m+1, xhi = 3*n/m;
  for(u64 x=xlo;x<=xhi;x++){
    u64 A = m*x-n; u64 B0 = n*x; u64 g=gcdu(A,B0); u64 Ap=A/g; u128 Bp=(u128)B0/g;
    u64 pr[64]; int ex[64]; int k=0;
    k=addf(n,pr,ex,k,1); k=addf(x,pr,ex,k,1);
    /* subtract g */
    { u64 v=g; while(v>1){ u64 q=(u64)spf[v]; int e=0; while(v%q==0){v/=q;e++;}
        for(int i=0;i<k;i++) if(pr[i]==q){ex[i]-=e;break;} } }
    /* enumerate divisors of Bp^2 that are <= Bp */
    u64 Bpu=(u64)Bp; u64 negB = (Ap - (u64)(Bp % Ap)) % Ap;
    static u64 divs[2000000]; int nd=1; divs[0]=1;
    for(int i=0;i<k;i++){ if(ex[i]==0) continue; int E=2*ex[i]; int cur=nd;
      for(int j=0;j<cur;j++){ u128 d=divs[j]; for(int e=1;e<=E;e++){ d*=pr[i]; if(d>Bp) break; divs[nd++]=(u64)d; } } }
    for(int j=0;j<nd;j++){ u64 d=divs[j]; if(d%Ap!=negB) continue;
      u128 y=((u128)d+Bp)/Ap; if(y<x) continue;
      u128 z=((Bp*Bp)/d+Bp)/Ap;
      /* exact verification m*x*y*z == n*(xy+yz+zx) using 128-bit is risky for overflow; check via fractions mod 2^128 is not proof,
         so verify with long division: m/n - 1/x - 1/y = 1/z  <=>  (m x y - n y - n x) * z == n x y */
      u128 xy=(u128)x*y; u128 lhs = (u128)m*xy - (u128)n*y - (u128)n*x; /* > 0 */
      if(lhs*z != (u128)n*xy){ fprintf(stderr,"VERIFY FAIL n=%llu x=%llu\n",n,x); exit(2);} 
      if(PARFILT>=0){ int od=(x&1)+(int)(y&1)+(int)(z&1); if(od!=PARFILT) continue; }
      c++;
      if(cnt_out){ cnt_out[0]++; int odd=(x&1)+(int)(y&1)+(int)(z&1);
        if(odd==0) cnt_out[1]++; else if(odd==1) cnt_out[2]++;
        int dx = x%n==0, dy=(y%n)==0, dz=(z%n)==0;
        if(dx+dy+dz==1) cnt_out[3]++; else if(dx+dy+dz==2) cnt_out[4]++; }
      if(stop) return c; }
  }
  return c; }
static int isprime(u64 n){ return n>=2 && (u64)spf[n]==n; }
int main(int argc,char**argv){
  int m=atoi(argv[1]); u64 N=strtoull(argv[2],0,10); char mode=argv[3][0];
  u64 hi = (mode=='c')? strtoull(argv[4],0,10) : N;
  if(mode!='c' && argc>4) PARFILT=atoi(argv[4]);
  sieve((long)(hi+10));
  if(mode=='p'||mode=='a'){ long cnt=0,fails=0; printf("m=%d mode=%c N=%llu failures:",m,mode,N);
    for(u64 n=(mode=='p'?3:2);n<=N;n++){ if(mode=='p'&&(!isprime(n)||m%n==0)) continue; cnt++;
      if(count_n(m,n,1,0)==0){printf(" %llu",n);fails++;fflush(stdout);} }
    printf("\nchecked %ld, failures %ld\n",cnt,fails); }
  else if(mode=='s'){ long cnt=0,fails=0; printf("m=%d odd squares <= %llu failures:",m,N);
    for(u64 k=3;k*k<=N;k+=2){ if(gcdu(k,2*(u64)m)!=1) continue; cnt++; if(count_n(m,k*k,1,0)==0){printf(" %llu",k*k);fails++;} }
    printf("\nchecked %ld, failures %ld\n",cnt,fails); }
  else if(mode=='c'){ long long co[5];
    for(u64 p=N;p<=hi;p++){ if(!isprime(p)||m%p==0||p<3) continue; count_n(m,p,0,co);
      printf("%llu %lld %lld %lld %lld %lld\n",p,co[0],co[1],co[2],co[3],co[4]); } }
  return 0; }
