// Falsifier screens (cross-review fix). Reads n from stdin (first column; '#' lines skipped).
// Prints n, min rho (full family, unrestricted divisibility form: ab | (n+rho)/4, rho | a+b; rho<=(n+4)/3),
// and min rho on the d-even sub-family (8ab | n+rho) together with the c=(a+b)/rho of the first d-even witness.
// -1 = none (exhaustive over the rho range, which is complete by rho <= a+b <= ab+1 <= (n+rho)/4+1).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
static int nd; static u64 dv[1<<15];
static void divisors(u64 N){ u64 pr[64]; int ex[64],k=0; u64 n=N; for(u64 q=2;q*q<=n;q++) if(n%q==0){pr[k]=q;ex[k]=0;while(n%q==0){n/=q;ex[k]++;}k++;} if(n>1){pr[k]=n;ex[k]=1;k++;}
  nd=1; dv[0]=1; for(int i=0;i<k;i++){int m=nd; u64 pw=1; for(int e=1;e<=ex[i];e++){pw*=pr[i]; for(int j=0;j<m;j++) dv[nd++]=dv[j]*pw;}}}
static u64 witc; static int works(u64 N,u64 rho){ divisors(N); for(int i=0;i<nd;i++){u64 a=dv[i],M=N/a; for(int j=0;j<nd;j++){u64 b=dv[j]; if(M%b==0&&(a+b)%rho==0){witc=(a+b)/rho;return 1;}}} return 0;}
int main(){ char line[256]; while(fgets(line,sizeof line,stdin)){ if(line[0]=='#'||line[0]=='\n') continue; u64 n=strtoull(line,0,10);
  long full=-1, dev=-1; u64 cdev=0;
  for(u64 rho=3; rho<=(n+4)/3; rho+=4){ if(full<0 && works((n+rho)/4,rho)) full=rho;
    if(dev<0 && (n+rho)%8==0 && works((n+rho)/8,rho)){dev=rho;cdev=witc;} if(full>=0&&dev>=0) break; }
  printf("%llu full_min_rho=%ld deven_min_rho=%ld deven_c=%llu\n",n,full,dev,cdev); fflush(stdout);} }
