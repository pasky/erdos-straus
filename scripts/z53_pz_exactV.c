// z53_pz_exactV.c — exact "BV-model" variance of the truncated pair count N_Q:
//   E N^2 = sum_{P,P'} phi(g) 1[a_P == a_P' mod g] / (phi(q_P) phi(q_P')),  g = gcd(q_P,q_P'),
//   M = sum_P 1/phi(q_P);  prints V/M^2 = E N^2/M^2 - 1.  P = (u,B), gcd(u,B)=1, u+B odd, q=4uB<=Q, a=-(u+B).
// Also splits V by the "type" of g's odd part w.r.t. (u|B) to locate the mass.  usage: exactV Q
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){ u64 Q=strtoull(argv[1],0,10);
  u64 *phit=malloc((Q+1)*sizeof(u64)); for(u64 i=0;i<=Q;i++) phit[i]=i;
  for(u64 i=2;i<=Q;i++) if(phit[i]==i) for(u64 j=i;j<=Q;j+=i) phit[j]-=phit[j]/i;
  u64 n=0, cap=1<<20; u64 *q=malloc(cap*8),*a=malloc(cap*8); double *w=malloc(cap*8);
  for(u64 u=1;4*u<=Q;u++) for(u64 B=1;4*u*B<=Q;B++){ if(((u+B)&1)==0||gcdu(u,B)!=1) continue;
    if(n==cap){cap*=2;q=realloc(q,cap*8);a=realloc(a,cap*8);w=realloc(w,cap*8);}
    q[n]=4*u*B; a[n]=q[n]-(u+B); w[n]=1.0/phit[q[n]]; n++; }
  double M=0; for(u64 i=0;i<n;i++) M+=w[i];
  double E2=0;
  for(u64 i=0;i<n;i++){ double acc=0; for(u64 j=0;j<n;j++){ u64 g=gcdu(q[i],q[j]);
      if((a[i]%g)==(a[j]%g)) acc+=w[j]*(double)phit[g]; } E2+=w[i]*acc; }
  printf("Q=%llu logQ=%.4f pairs=%llu M=%.6f EN2=%.6f V=%.6f V/M^2=%.6f V/logQ^3=%.6f\n",Q,log((double)Q),n,M,E2,E2-M*M,(E2-M*M)/(M*M),(E2-M*M)/pow(log((double)Q),3));
  return 0; }
