// z58 TRYO (C-variant: "u" below is C, n=4Cp+1): for primes p in Mordell classes M (mod 840) in [lo,hi], compute
// m(p) = least u >= 1 such that p+u has a divisor d == -1 (mod 4u)  (<=> (*) solvable with that u).
// prints histogram of m(p) and the record holders.
// usage: ./minu lo hi [step-sample]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){if(n<2)return 0;static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
 for(int i=0;i<12;i++){if(n%sp[i]==0)return n==sp[i];}
 u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
 for(int i=0;i<12;i++){u64 x=powmod(sp[i],d,n);if(x==1||x==n-1)continue;int ok=0;
  for(int r=1;r<s;r++){x=mulmod(x,x,n);if(x==n-1){ok=1;break;}}if(!ok)return 0;}return 1;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){ if(n%2==0) return 2; for(u64 c=1;;c++){ u64 x=2,y=2,d=1; while(d==1){x=(mulmod(x,x,n)+c)%n; y=(mulmod(y,y,n)+c)%n; y=(mulmod(y,y,n)+c)%n; d=gcdu(x>y?x-y:y-x,n);} if(d!=n) return d; } }
static void addfac(u64 m,u64 M,u64*f,int*e,int*k){ if(m==1)return; if(isprime(m)){ if(M%m==0) return; for(int i=0;i<*k;i++) if(f[i]==m){e[i]++;return;} f[*k]=m;e[*k]=1;(*k)++; return;} u64 d=rho(m); addfac(d,M,f,e,k); addfac(m/d,M,f,e,k);}
static int *pr; static int npr;
// does n have divisor d with gcd(d,4u)=1, d == -1 mod M (M=4u)?
static int hasdiv(u64 n,u64 u,u64 *dout){
 u64 M=4*u; u64 f[64]; int e[64]; int k=0; u64 m=n;
 for(int i=0;i<npr;i++){u64 q=pr[i]; if(q*q>m)break; if(m%q==0){int c=0;while(m%q==0){m/=q;c++;} if(M%q!=0 && q!=2){f[k]=q;e[k]=c;k++;}}}
 addfac(m,M,f,e,&k);
 // enumerate divisors mod M as residues, but also keep actual value for reporting: enumerate actual divisors
 static u64 dv[1<<16]; int nd=1; dv[0]=1;
 for(int i=0;i<k;i++){int cur=nd; u64 pw=1; for(int j=1;j<=e[i];j++){pw*=f[i]; for(int t=0;t<cur;t++){ if(nd>=(1<<16)) {fprintf(stderr,"overflow\n");exit(1);} dv[nd++]=dv[t]*pw;}}}
 for(int t=0;t<nd;t++) if(dv[t]%M==M-1){ *dout=dv[t]; return 1;}
 return 0;
}
int main(int argc,char**argv){
 // z58 TRYO levels: for primes p in M (mod 840) in [lo,hi], success bitmask over u=1..K (p+u has divisor == -1 mod 4u)
 // and C=1..K (4Cp+1 has divisor == -1 mod 4C). Prints per-level failure rates and pairwise co-failure ratios.
 u64 lo=strtoull(argv[1],0,10), hi=strtoull(argv[2],0,10); int K=12;
 int L=200000; char*s=calloc(L+1,1); pr=malloc(sizeof(int)*L); npr=0;
 for(int i=2;i<=L;i++){if(!s[i]){pr[npr++]=i; for(long j=(long)i*i;j<=L;j+=i)s[j]=1;}}
 int cls[6]={1,121,169,289,361,529}; long cnt=0; static long f1[32], f2[32][32]; long allfail=0;
 for(u64 b=lo-lo%840;b<=hi;b+=840) for(int c=0;c<6;c++){u64 p=b+cls[c]; if(p<lo||p>hi||!isprime(p))continue; cnt++;
   int fail[32]; u64 d; int nf=0;
   for(int i=0;i<K;i++){ fail[i]=!hasdiv(p+i+1,i+1,&d); fail[K+i]=!hasdiv(4*(u64)(i+1)*p+1,i+1,&d); }
   for(int i=0;i<2*K;i++){ if(fail[i]){f1[i]++; nf++;} for(int j=0;j<2*K;j++) if(fail[i]&&fail[j]) f2[i][j]++; }
   if(nf==2*K) allfail++;
 }
 printf("count=%ld allfail(24 levels)=%ld\n",cnt,allfail);
 for(int i=0;i<2*K;i++) printf("%c%d fail=%.4f\n", i<K?'u':'C', i%K+1, (double)f1[i]/cnt);
 printf("co-failure ratio P(fi&fj)/(P(fi)P(fj)):\n");
 for(int i=0;i<2*K;i++){ for(int j=0;j<2*K;j++) printf("%5.2f", (double)f2[i][j]*cnt/((double)f1[i]*f1[j])); printf("\n"); }
}
