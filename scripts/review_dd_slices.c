/* R176 from scratch: primes p = 1 (24) below PMAX NOT covered by any ES slice with cd | 6 (4cd | 24).
   Type II slice (c,d): exists f | 1+4c^2 d p, f = -1 mod 4cd   (DIFF_DEEP Thm 2.1, re-derived).
   Type I  slice (c,d): exists f>0, f | p^2+4c^2 d, f = -p mod 4cd  (re-derived: f=4acd-p, ef=4a^2d+1;
   converse uses gcd(f,4c^2 d)=1 for p not | 6, and b=ce-a=(c+ap)/f>0). */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static int *pr; static int np;
static int has_div(u64 N, u64 M, u64 r){ /* exists divisor f of N with f = r mod M */
  u64 P[64]; int E[64]; int k=0; u64 m=N;
  for(int i=0;i<np && (u64)pr[i]*pr[i]<=m;i++){ if(m%pr[i]==0){P[k]=pr[i];E[k]=0; while(m%pr[i]==0){m/=pr[i];E[k]++;} k++;}}
  if(m>1){P[k]=m;E[k]=1;k++;}
  /* enumerate divisors mod M */
  static u64 D[1<<16]; int nd=1; D[0]=1;
  for(int i=0;i<k;i++){int cur=nd; u64 pw=1; for(int e=1;e<=E[i];e++){pw*=P[i]; for(int j=0;j<cur;j++) D[nd++]=D[j]*pw;}}
  for(int j=0;j<nd;j++) if(D[j]%M==r%M) return 1;
  return 0; }
int main(int argc,char**argv){ u64 PMAX=atoll(argv[1]); u64 L=7000000; char*s=calloc(L+1,1); pr=malloc(sizeof(int)*L);
 for(u64 i=2;i<=L;i++){ if(!s[i]){pr[np++]=i; for(u64 j=i*i;j<=L;j+=i) s[j]=1;}}
 int cs[9][2]={{1,1},{1,2},{1,3},{1,6},{2,1},{2,3},{3,1},{3,2},{6,1}};
 long tot=0, miss=0; int printed=0; u64 marks[]={10000,100000,300000,1000000}; int mi=0; long totm=0,missm=0;
 for(int i=0;i<np && (u64)pr[i]<PMAX;i++){ u64 p=pr[i]; if(p%24!=1) continue;
  while(mi<4 && p>marks[mi]){ printf("  below %llu: %ld/%ld uncovered\n",marks[mi],miss,tot); mi++; }
  tot++; int cov=0;
  for(int t=0;t<9 && !cov;t++){ u64 c=cs[t][0], d=cs[t][1], M=4*c*d;
    if(has_div(1+4*c*c*d*p, M, M-1)) cov=1;
    else if(has_div(p*p+4*c*c*d, M, (M - p%M)%M)) cov=1; }
  if(!cov){ miss++; if(printed<8){printf("uncovered p=%llu\n",p);printed++;} } }
 while(mi<4 && marks[mi]<=PMAX){ printf("  below %llu: %ld/%ld uncovered\n",marks[mi],miss,tot); mi++; }
 printf("p=1 (24), p<%llu: %ld primes, %ld uncovered by the 9+9 slices cd|6\n",PMAX,tot,miss); return 0; }
