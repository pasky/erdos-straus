/* Opus round-2 cross-check of EXTREME §7 (independent of z52d/z80_gap_sieve).
   For every prime p in [lo,hi] with p mod 840 in {1,121,169,289,361,529}
   compute g(p)=4*xmin-p by brute force over windows m=3,7,11,... (no AP crossing).
   Criterion used here (different from the legacy divisor-pair DP): with x=(p+m)/4,
   s=p*x, the window has a solution iff some divisor h of s^2 has h = -s (mod m)
   (then y=(s+h)/m, z=(s+s^2/h)/m).  Residues of divisors of s^2 by DP over the
   factorisation of s with doubled exponents.  Factorisation: own trial division +
   Pollard-Brent + deterministic Miller-Rabin (bases 2..37, exact for n<3.3e24).
   Primes p found by own segmented Eratosthenes on the six classes.
   Usage: lo hi  -> prints strict records (relative to lo) and a g-histogram.
   Aborts loudly if a window m>=MAXM would be needed. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
typedef uint64_t u64; typedef __uint128_t u128;
#define MAXM 2048
static u64 mm(u64 a,u64 b,u64 n){return (u128)a*b%n;}
static u64 pw(u64 a,u64 e,u64 n){u64 r=1;a%=n;while(e){if(e&1)r=mm(r,a,n);a=mm(a,a,n);e>>=1;}return r;}
static int mr(u64 n){if(n<2)return 0;static const u64 b[]={2,3,5,7,11,13,17,19,23,29,31,37};
 for(int i=0;i<12;i++){if(n==b[i])return 1;if(n%b[i]==0)return 0;}
 u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
 for(int i=0;i<12;i++){u64 x=pw(b[i],d,n);if(x==1||x==n-1)continue;int ok=0;for(int r=1;r<s;r++){x=mm(x,x,n);if(x==n-1){ok=1;break;}}if(!ok)return 0;}return 1;}
static u64 g64(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 brent(u64 n){ if(!(n&1))return 2; for(u64 c=3;;c+=2){u64 y=2,x,q=1,g=1,ys=2;u64 r=1,m=64;
  do{x=y;for(u64 i=0;i<r;i++)y=(mm(y,y,n)+c)%n;u64 k=0;
     do{ys=y;for(u64 i=0;i<m&&i<r-k;i++){y=(mm(y,y,n)+c)%n;q=mm(q,x>y?x-y:y-x,n);}g=g64(q,n);k+=m;}while(k<r&&g==1);
     r<<=1;}while(g==1);
  if(g==n){do{ys=(mm(ys,ys,n)+c)%n;g=g64(x>ys?x-ys:ys-x,n);}while(g==1);}
  if(g!=n)return g;}}
static int nf;static u64 F[80];static int E[80];
static void add(u64 q,int e){for(int i=0;i<nf;i++)if(F[i]==q){E[i]+=e;return;}F[nf]=q;E[nf]=e;nf++;}
static void rec(u64 n){if(n==1)return;if(mr(n)){add(n,1);return;}u64 d=brent(n);rec(d);rec(n/d);}
static int sp[200],nsp;
static void factor(u64 n){nf=0;for(int i=0;i<nsp;i++){u64 q=sp[i];if(q*q>n)break;if(n%q==0){int e=0;while(n%q==0){n/=q;e++;}add(q,e);}}rec(n);}
static unsigned char S[MAXM],T[MAXM];
/* does window m (m=3 mod 4) have a solution for prime p? */
static int window(u64 p,u64 m){u64 x=(p+m)/4;factor(x);add(p,1);
 memset(S,0,m);S[1%m]=1;
 for(int i=0;i<nf;i++){u64 q=F[i]%m;if(q==0){fprintf(stderr,"gcd fail %llu %llu\n",(unsigned long long)p,(unsigned long long)m);exit(2);}
  memcpy(T,S,m);u64 qq=1;for(int e=1;e<=2*E[i];e++){qq=qq*q%m;for(u64 r=0;r<m;r++)if(S[r])T[r*qq%m]=1;}memcpy(S,T,m);}
 u64 t=(m-mm(p%m,x%m,m))%m; return S[t];}
static int gap(u64 p){for(u64 m=3;m<MAXM;m+=4){if(m>=p){fprintf(stderr,"m>=p %llu\n",(unsigned long long)p);exit(4);}if(window(p,m))return (int)m;}
 fprintf(stderr,"UNRESOLVED %llu\n",(unsigned long long)p);exit(3);}
int main(int ac,char**av){if(ac!=3)return 1;u64 lo=strtoull(av[1],0,10),hi=strtoull(av[2],0,10);
 for(int q=2;nsp<200;q++){int ok=1;for(int i=0;i<nsp&&sp[i]*sp[i]<=q;i++)if(q%sp[i]==0){ok=0;break;}if(ok)sp[nsp++]=q;}
 u64 R=(u64)sqrtl((long double)hi)+2;unsigned char*c=calloc(R+1,1);u64*bp=malloc(sizeof(u64)*(R/2+10));long nb=0;
 for(u64 i=2;i<=R;i++)if(!c[i]){bp[nb++]=i;for(u64 j=i*i;j<=R;j+=i)c[j]=1;}free(c);
 const u64 SEG=1ULL<<24;unsigned char*b=malloc(SEG);long hist[MAXM]={0};int cur=0;u64 cnt=0;
 for(u64 L=lo;L<=hi;L+=SEG){u64 H=L+SEG;if(H>hi+1)H=hi+1;memset(b,0,H-L);
  for(long t=0;t<nb;t++){u64 q=bp[t];if(q*q>=H)break;u64 st=((L+q-1)/q)*q;if(st<q*q)st=q*q;for(u64 j=st;j<H;j+=q)b[j-L]=1;}
  for(u64 p=L;p<H;p++){if(b[p-L]||p<2)continue;u64 r=p%840;if(!(r==1||r==121||r==169||r==289||r==361||r==529))continue;
   cnt++;int g=gap(p);hist[g]++;if(g>cur){cur=g;printf("REC %llu %d\n",(unsigned long long)p,g);fflush(stdout);}}}
 printf("DONE lo=%llu hi=%llu Mprimes=%llu max=%d hist:",(unsigned long long)lo,(unsigned long long)hi,(unsigned long long)cnt,cur);
 for(int i=0;i<MAXM;i++)if(hist[i])printf(" %d:%ld",i,hist[i]);printf("\n");return 0;}
