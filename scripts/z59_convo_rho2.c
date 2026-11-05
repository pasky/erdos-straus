// Minimal rho (=3 mod 4) with ab | N_rho/(e?2:1), rho | a+b; mode e=0 all, e=1 d-even (needs 8|p+rho, uses N/2).
// usage: lo hi mode [verbose]  ; p ranges over primes = 1 mod 24 (or all primes =1 mod 4 if mode>=2: mode-2)
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; if(n%2==0) return n==2; for(u64 i=3;i*i<=n;i+=2) if(n%i==0) return 0; return 1;}
static int ndiv; static u64 dv[1<<14];
static void divisors(u64 N){ u64 pr[64]; int ex[64], k=0; u64 n=N; for(u64 q=2;q*q<=n;q++) if(n%q==0){pr[k]=q;ex[k]=0; while(n%q==0){n/=q;ex[k]++;} k++;} if(n>1){pr[k]=n;ex[k]=1;k++;}
  ndiv=1; dv[0]=1; for(int i=0;i<k;i++){ int m=ndiv; u64 pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(int j=0;j<m;j++) dv[ndiv++]=dv[j]*pw; } } }
static int works(u64 N,u64 rho){ divisors(N); for(int i=0;i<ndiv;i++){u64 a=dv[i]; u64 M=N/a; for(int j=0;j<ndiv;j++){u64 b=dv[j]; if(b<a) continue; if(M%b==0 && (a+b)%rho==0) return 1;}} return 0;}
int main(int argc,char**argv){ u64 lo=atoll(argv[1]),hi=atoll(argv[2]); int mode=atoi(argv[3]); int verb=argc>4; int deven=mode&1; int allp=mode>=2;
  long tot=0; u64 worst=0,wp=0; long hist[64]={0};
  for(u64 p=lo|1;p<=hi;p+=2){ if(allp? (p%4!=1):(p%24!=1)) continue; if(!isprime(p)) continue; tot++;
    u64 rho; for(rho=deven?(8-p%8):3; rho<4*p; rho+=deven?8:4){ u64 N=(p+rho)/4; if(deven) N/=2; if(works(N,rho)) break; }
    if(rho>=4*p){ printf("NOSOL %llu\n",p); continue;}
    int b=0; while((1ULL<<b)<rho) b++; hist[b]++;
    if(rho>worst){worst=rho;wp=p; printf("record p=%llu rho=%llu\n",p,rho); fflush(stdout);}
    if(verb) printf("%llu %llu\n",p,rho);
  }
  printf("tot %ld worst rho %llu at p=%llu\n",tot,worst,wp); for(int i=0;i<40;i++) if(hist[i]) printf("rho<=2^%d:%ld ",i,hist[i]); printf("\n"); }
