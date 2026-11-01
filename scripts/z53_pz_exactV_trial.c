// z53_pz_exactV_trial.c — exact BV-model variance of the truncated TRIAL count
//   N(p) = sum_{(u,C): m=4uC-1<=Q} c_P 1[p ≡ -u mod m],  c_P = phi(m)/m (weighted, w=1) or 1 (unweighted, w=0)
//   E N^2 = sum_{P,P'} c c' phi(g) 1[u≡u' mod g]/(phi(m)phi(m')),  M = E N.  Prints V/M^2 and V/log^3 Q.
// usage: exactV_trial Q w
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){ u64 Q=strtoull(argv[1],0,10); int W=atoi(argv[2]);
  u64 *ph=malloc((Q+2)*8); for(u64 i=0;i<=Q+1;i++) ph[i]=i;
  for(u64 i=2;i<=Q+1;i++) if(ph[i]==i) for(u64 j=i;j<=Q+1;j+=i) ph[j]-=ph[j]/i;
  u64 n=0,cap=1<<20; u64 *m=malloc(cap*8),*u=malloc(cap*8); double *w=malloc(cap*8);
  for(u64 uu=1;4*uu-1<=Q;uu++) for(u64 C=1;4*uu*C-1<=Q;C++){ if(n==cap){cap*=2;m=realloc(m,cap*8);u=realloc(u,cap*8);w=realloc(w,cap*8);}
    m[n]=4*uu*C-1; u[n]=uu; w[n]= W? 1.0/m[n] : 1.0/ph[m[n]]; n++; }
  double M=0; for(u64 i=0;i<n;i++) M+=w[i];
  double E2=0; for(u64 i=0;i<n;i++){ double acc=0; for(u64 j=0;j<n;j++){ u64 g=gcdu(m[i],m[j]);
      if(g==1) acc+=w[j]; else if((u[i]%g)==(u[j]%g)) acc+=w[j]*(double)ph[g]; } E2+=w[i]*acc; }
  double L=log((double)Q);
  printf("Q=%llu w=%d logQ=%.4f P=%llu M=%.6f M/logQ^2=%.5f V=%.6f V/M^2=%.6f V/logQ^3=%.6f\n",Q,W,L,n,M,M/(L*L),E2-M*M,(E2-M*M)/(M*M),(E2-M*M)/(L*L*L));
  return 0; }
