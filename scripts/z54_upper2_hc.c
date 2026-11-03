// z54 UPPER2: compute HC(p) for primes p = 1 (mod 4), p <= N, from first principles.
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
static int hasdiv(u64 n,u64 x){ factor(n); u64 divs[1<<14]; int nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){int cur=nd; u64 pw=1; for(int e=1;e<=fe[i];e++){pw*=fp[i]; for(int j=0;j<cur;j++){ if(nd>=(1<<14)){fprintf(stderr,"divs overflow\n");exit(1);} divs[nd++]=divs[j]*pw;}}}
  for(int j=0;j<nd;j++) if(divs[j]%x==x-1) return 1; return 0;}
int main(int argc,char**argv){ u64 N=strtoull(argv[1],0,10);
  char*s=calloc(N+1,1); for(u64 i=2;i*i<=N;i++) if(!s[i]) for(u64 j=i*i;j<=N;j+=i) s[j]=1;
  long hist[4096]={0}; long cntU=0,cntT=0,cntBoth=0; u64 maxhc=0,argmax=0; double maxratio=0; u64 argratio=0; long nprimes=0; long viol=0; long nohc=0; /* NOHC counts as a violation and forces exit 2 */
  for(u64 p=5;p<=N;p+=4){ if(s[p]) continue; nprimes++;
    u64 hc=0; int how=0;
    for(u64 x=1;x<4096;x++){ if(!(x%4==0 || (x+p)%8==0)) continue;
      int U=hasdiv(p+x,x), T=hasdiv(x*p+1,x);
      if(U||T){hc=x;how=(U?1:0)|(T?2:0);break;} }
    if(!hc){printf("NOHC p=%llu\n",p);viol++;nohc++;continue;}
    hist[hc]++; if(how==1)cntU++; else if(how==2)cntT++; else cntBoth++;
    if(p%8==5 && hc!=3) printf("ANOMALY p=%llu hc=%llu\n",p,hc);
    if(hc>maxhc){maxhc=hc;argmax=p;printf("record HC=%llu at p=%llu (how=%d)\n",hc,p,how);fflush(stdout);}
    double L=log((double)p); double r=hc/(L*L*L); if(r>maxratio){maxratio=r;argratio=p;}
    if(r>1.0) viol++;
  }
  printf("N=%llu primes(1mod4)=%ld maxHC=%llu at p=%llu ; max HC/(log p)^3=%.4f at p=%llu ; #violations HC>(log p)^3: %ld\n",N,nprimes,maxhc,argmax,maxratio,argratio,viol);
  printf("fired: U only %ld, T only %ld, both %ld\n",cntU,cntT,cntBoth);
  for(int i=0;i<4096;i++) if(hist[i]) printf("HC=%d count=%ld\n",i,hist[i]);
  if(nohc){fprintf(stderr,"FAIL: %ld primes with no C-coordinate below 4096\n",nohc);return 2;}
  return 0;}
