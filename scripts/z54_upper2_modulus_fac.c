// z54 UPPER2 cross-check of z54_upper2_modulus.c: mu(p) via factorization of p+x, xp+1 (all words with a
// C_p-coordinate x <= (log p)^3; mu = min product of two smallest coordinates). Base code: z54_upper2_hc.c.
// (original header:) compute HC(p) for primes p = 1 (mod 4), p <= N, from first principles.
// HC(p) = least x in C_p (x = 0 mod 4 or x = -p mod 8) that is a coordinate of a word (t,u,v), tuv-u-v=p.
// Lemma R (memo §1): x is a coordinate iff
//   (U) p+x has a divisor d = -1 (mod x)   [word (t,u,v)=((d+1)/x, x, (p+x)/d)], or
//   (T) x*p+1 has a divisor d = -1 (mod x) [word (x, (d+1)/x, ((xp+1)/d+1)/x)].
// Output: histogram of HC, max HC, max HC/(log p)^3, and which test (U/T) fired; records list.
// usage: z54_upper2_hc N [threads]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime64(u64 n){ if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){if(n%sp[i]==0)return n==sp[i];}
  u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){u64 a=sp[i];u64 x=powmod(a,d,n);if(x==1||x==n-1)continue;int ok=0;
    for(int r=1;r<s;r++){x=mulmod(x,x,n);if(x==n-1){ok=1;break;}} if(!ok)return 0;} return 1;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){ if(n%2==0)return 2; for(u64 c=1;;c++){u64 x=2,y=2,d=1;
  while(d==1){x=(mulmod(x,x,n)+c)%n;y=(mulmod(y,y,n)+c)%n;y=(mulmod(y,y,n)+c)%n;d=gcdu(x>y?x-y:y-x,n);} if(d!=n)return d;}}
static int nf; static u64 fp[64]; static int fe[64];
static void addf(u64 q){for(int i=0;i<nf;i++)if(fp[i]==q){fe[i]++;return;} fp[nf]=q;fe[nf]=1;nf++;}
static void fac(u64 n){ if(n==1)return; if(isprime64(n)){addf(n);return;} u64 d=rho(n); fac(d); fac(n/d);}
static void factor(u64 n){ nf=0; static const int sm[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
  for(int i=0;i<15;i++){while(n%sm[i]==0){addf(sm[i]);n/=sm[i];}} fac(n);}
// does n have a divisor = x-1 mod x ?
static u64 bestmod;
static void consider(u64 a,u64 b,u64 c){u64 s[3]={a,b,c}; for(int i=0;i<3;i++)for(int j=i+1;j<3;j++) if(s[j]<s[i]){u64 t=s[i];s[i]=s[j];s[j]=t;}
  u128 m=(u128)s[0]*s[1]; if(m<bestmod) bestmod=(u64)m;}
static void scan(u64 n,u64 x,int kind){ factor(n); static u64 divs[1<<14]; int nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){int cur=nd; u64 pw=1; for(int e=1;e<=fe[i];e++){pw*=fp[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw;}}
  for(int j=0;j<nd;j++){u64 d=divs[j]; if(d%x!=x-1) continue;
    if(kind==0) consider((d+1)/x,x,(n)/d); else consider(x,(d+1)/x,(n/d+1)/x);} }
static int hasdiv(u64 n,u64 x){ factor(n); u64 divs[1<<14]; int nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){int cur=nd; u64 pw=1; for(int e=1;e<=fe[i];e++){pw*=fp[i]; for(int j=0;j<cur;j++){ if(nd>=(1<<14)){fprintf(stderr,"divs overflow\n");exit(1);} divs[nd++]=divs[j]*pw;}}}
  for(int j=0;j<nd;j++) if(divs[j]%x==x-1) return 1; return 0;}
int main(int argc,char**argv){ u64 N=strtoull(argv[1],0,10);
  char*s=calloc(N+1,1); for(u64 i=2;i*i<=N;i++) if(!s[i]) for(u64 j=i*i;j<=N;j+=i) s[j]=1;
  u64 recmod=0; long np=0; double sume=0;
  for(u64 p=5;p<=N;p+=4){ if(s[p]) continue; np++; bestmod=~0ULL;
    double L=log((double)p); u64 X=(u64)(L*L*L);
    for(u64 x=2;x<=X;x++){ if(!(x%4==0 || (x+p)%8==0)) continue; scan(p+x,x,0); scan(x*p+1,x,1); }
    sume+=log((double)bestmod)/L;
    if(bestmod>recmod){recmod=bestmod;printf("record mu=%llu at p=%llu\n",bestmod,p);} }
  printf("N=%llu primes=%ld max mu=%llu mean log mu/log p=%.4f\n",N,np,recmod,sume/np); return 0;}
