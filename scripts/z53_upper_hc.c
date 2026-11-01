// z53 UPPER: HC(p) census + checks of the lemmas in Z53_UPPER.md.
// usage: z53_upper_hc X KMAX RECIPLIM
//   For every prime p = 1 (mod 4), p <= X:
//     HC(p) = least c in C_p (c = 0 mod 4 or c = -p mod 8) such that p+c or c*p+1 has a divisor = -1 (mod c)
//             (Lemma 1.1: this is exactly the least C_p-coordinate of a word of p);
//     checks Lemma 2.1 (HC=3 iff p=5 mod 8), Lemma 2.2 (for p=1 mod 8: HC=4 iff (p+4)(4p+1) has a prime factor = 3 mod 4);
//     for p <= RECIPLIM: checks Lemma 3.1 (every certificate divisor d, c <= 64, has Legendre (d/p) = -1)
//       by enumerating all divisors d = -1 (mod c) of p+c and c*p+1 for all c in C_p, c <= 64;
//     for p <= RECIPLIM: prime-sieve sets S_K (K = 1..KMAX): p in S_K iff for no k <= K does a prime q = -1 (mod 4k)
//       divide (p+4k)(4kp+1). Lemma 4.1: HC(p) > 4K implies p in S_K (checked).
//   Prints histogram of HC, record HC, counts #S_K and #{HC > 4K}, violations.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){ if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powmod(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){ if(n%2==0) return 2; for(u64 c=1;;c++){ u64 x=2,y=2,d=1;
    while(d==1){ x=(mulmod(x,x,n)+c)%n; y=(mulmod(y,y,n)+c)%n; y=(mulmod(y,y,n)+c)%n; d=gcdu(x>y?x-y:y-x,n);} if(d!=n) return d; } }
static u64 fac[64]; static int nf;
static void factor_rec(u64 n){ if(n==1) return; if(isprime(n)){fac[nf++]=n;return;} u64 d=rho(n); factor_rec(d); factor_rec(n/d); }
static void factor(u64 n){ nf=0; for(u64 q=2;q<200&&q*q<=n;q++){ while(n%q==0){fac[nf++]=q;n/=q;} } if(n>1) factor_rec(n); }
// divisors
static u64 dv[1<<16]; static int nd;
static int cmpu(const void*a,const void*b){u64 x=*(u64*)a,y=*(u64*)b;return x<y?-1:x>y;}
static void divisors(u64 n){ factor(n); qsort(fac,nf,sizeof(u64),cmpu); nd=1; dv[0]=1; int i=0;
  while(i<nf){ u64 q=fac[i]; int e=0; while(i<nf&&fac[i]==q){e++;i++;} int cur=nd; u64 pe=1;
    for(int j=1;j<=e;j++){ pe*=q; for(int k=0;k<cur;k++) dv[nd++]=dv[k]*pe; } } }
static int jacobi(u64 a,u64 n){ // n odd positive
  a%=n; int r=1; while(a){ while(!(a&1)){ a>>=1; u64 m8=n&7; if(m8==3||m8==5) r=-r; } u64 t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) r=-r; a%=n; }
  return n==1?r:0; }
static int inC(u64 x,u64 p){ return (x&3)==0 || ((x+p)&7)==0; }
// does N have a divisor = -1 mod c ?
static int hasdiv(u64 N,u64 c){ divisors(N); for(int i=0;i<nd;i++) if(dv[i]%c==c-1) return 1; return 0; }
// does N have a prime factor = -1 mod m ?
static int hasprimefac(u64 N,u64 m){ factor(N); for(int i=0;i<nf;i++) if(fac[i]%m==m-1) return 1; return 0; }

int main(int argc,char**argv){
  u64 X=atoll(argv[1]); int KMAX=atoi(argv[2]); u64 RL=atoll(argv[3]);
  char*sv=calloc(X+1,1); for(u64 i=2;i*i<=X;i++) if(!sv[i]) for(u64 j=i*i;j<=X;j+=i) sv[j]=1;
  long hist[1024]={0}; u64 recHC=0, recp=0; long np=0, np1=0, viol21=0, viol22=0, viol31=0, viol41=0, ncert31=0;
  long nS[64]={0}, nHCgt[64]={0}, nRL=0, nRL1=0; long hcinf=0;
  for(u64 p=5;p<=X;p+=4){ if(sv[p]) continue; np++;
    u64 hc=0;
    for(u64 c=3;c<2000;c++){ if(!inC(c,p)) continue;
      if(hasdiv(p+c,c) || hasdiv(c*p+1,c)){ hc=c; break; } }
    if(!hc){ hcinf++; fprintf(stderr,"HC>=2000 at p=%llu\n",p); continue; }
    if(hc<1024) hist[hc]++;
    if(hc>recHC){recHC=hc;recp=p; printf("record HC=%llu at p=%llu\n",hc,p); fflush(stdout);}
    if((hc==3)!=((p&7)==5)) viol21++;
    if((p&7)==1){ np1++;
      factor((p+4)*(u64)1); int a=0; for(int i=0;i<nf;i++) if((fac[i]&3)==3) a=1;
      factor(4*p+1); for(int i=0;i<nf;i++) if((fac[i]&3)==3) a=1;
      if((hc==4)!=a) viol22++; }
    if(p<=RL){ nRL++; if((p&7)==1) nRL1++;
      // Lemma 3.1
      for(u64 c=3;c<=64;c++){ if(!inC(c,p)) continue;
        u64 Ns[2]={p+c,c*p+1};
        for(int l=0;l<2;l++){ divisors(Ns[l]); u64 dd[1<<16]; int n2=nd; memcpy(dd,dv,nd*sizeof(u64));
          for(int i=0;i<n2;i++){ u64 d=dd[i]; if(d%c!=c-1) continue; ncert31++;
            if(jacobi(d%p,p)!=-1) viol31++; } } }
      // S_K
      if((p&7)==1){ int inS=1;
        for(int K=1;K<=KMAX;K++){ u64 m=4*(u64)K;
          if(inS && (hasprimefac(p+m,m)||hasprimefac(m*p+1,m))) inS=0;
          if(inS) nS[K]++;
          if(hc>m){ nHCgt[K]++; if(!inS) viol41++; } } }
    }
  }
  printf("X=%llu primes p=1(4): %ld (p=1(8): %ld); HC>=2000: %ld\n",X,np,np1,hcinf);
  printf("record HC=%llu at p=%llu\n",recHC,recp);
  printf("hist:"); for(int i=0;i<1024;i++) if(hist[i]) printf(" %d:%ld",i,hist[i]); printf("\n");
  printf("viol Lemma2.1=%ld Lemma2.2=%ld\n",viol21,viol22);
  printf("RL=%llu: primes p=1(4) %ld, p=1(8) %ld; Lemma3.1 certificates checked %ld, viol %ld; Lemma4.1 viol %ld\n",RL,nRL,nRL1,ncert31,viol31,viol41);
  for(int K=1;K<=KMAX;K++) printf("K=%d (4K=%d): #S_K=%ld  #HC>4K=%ld  (among p=1(8) <= RL)\n",K,4*K,nS[K],nHCgt[K]);
  return 0; }
