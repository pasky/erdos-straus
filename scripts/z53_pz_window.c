// z53_pz_window.c — truncated counts N_pair(n), N_trial(n) on an integer window [Y, Y+H)
// N_pair(n)  = #{(u,B): gcd(u,B)=1, u+B odd, 4uB <= Q, n ≡ -(u+B) (mod 4uB)}
// N_trial(n) = #{(u,C): m = 4uC-1 <= Q, n ≡ -u (mod m)}      (one trial fibration)
// Reports, over primes p in window (all, and p ≡ 1 mod 24), mean/var of N_pair, N_trial, N_pair+2N_trial,
// and the predicted mean M = sum 1/phi(q). Controls: odd squares in window (N_pair must be 0 by T1).
// usage: z53_pz_window Y H Q
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef long long i64;
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 phi(u64 n){u64 r=n;for(u64 p=2;p*p<=n;p++)if(n%p==0){while(n%p==0)n/=p;r-=r/p;}if(n>1)r-=r/n;return r;}
int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage Y H Q\n");return 1;}
  u64 Y=strtoull(argv[1],0,10), H=strtoull(argv[2],0,10), Q=strtoull(argv[3],0,10);
  uint16_t *np=calloc(H,2), *nt=calloc(H,2); uint8_t *isp=malloc(H);
  if(!np||!nt||!isp){fprintf(stderr,"oom\n");return 1;}
  // segmented sieve for primes in [Y,Y+H)
  memset(isp,1,H); u64 lim=(u64)sqrt((double)(Y+H))+2; uint8_t *sp=calloc(lim+1,1);
  for(u64 i=2;i<=lim;i++) if(!sp[i]){ for(u64 j=i*i;j<=lim;j+=i) sp[j]=1;
      u64 s=((Y+i-1)/i)*i; if(s<i*i) s=i*i; for(u64 j=s;j<Y+H;j+=i) isp[j-Y]=0; }
  for(u64 j=Y;j<Y+H && j<2;j++) isp[j-Y]=0;
  double M=0, Mt=0; u64 npairs=0, ntr=0;
  for(u64 u=1;4*u<=Q;u++) for(u64 B=1;4*u*B<=Q;B++){
    if(((u+B)&1)==0 || gcdu(u,B)!=1) continue;
    u64 q=4*u*B; u64 a=(q-((u+B)%q))%q; M+=1.0/phi(q); npairs++;
    u64 s=Y%q; u64 off=(a>=s)?a-s:a+q-s; for(u64 j=off;j<H;j+=q) np[j]++;
  }
  for(u64 u=1;4*u-1<=Q;u++) for(u64 C=1;4*u*C-1<=Q;C++){
    u64 m=4*u*C-1; u64 a=(m-(u%m))%m; Mt+=1.0/phi(m); ntr++;
    u64 s=Y%m; u64 off=(a>=s)?a-s:a+m-s; for(u64 j=off;j<H;j+=m) nt[j]++;
  }
  // stats
  double S[2][3][2]; u64 cnt[2]={0,0}; memset(S,0,sizeof S);
  u64 sqbad=0, sqn=0;
  for(u64 j=0;j<H;j++){ u64 n=Y+j;
    if(isp[j]){ double x[3]={np[j],nt[j],np[j]+2.0*nt[j]};
      for(int c=0;c<2;c++){ if(c==1 && n%24!=1) continue; cnt[c]++;
        for(int k=0;k<3;k++){S[c][k][0]+=x[k];S[c][k][1]+=x[k]*x[k];} } }
  }
  // odd squares control
  u64 r=(u64)sqrt((double)Y); while(r*r<Y) r++; for(;r*r<Y+H;r++) if(r&1){ sqn++; if(np[r*r-Y]) sqbad++; }
  printf("Y=%llu H=%llu Q=%llu pairs=%llu trials=%llu M_pair=%.6f M_trial=%.6f logQ=%.4f\n",Y,H,Q,npairs,ntr,M,Mt,log((double)Q));
  const char*nm[3]={"Npair","Ntrial","Npair+2Ntrial"};
  for(int c=0;c<2;c++){ printf("class %s: nprimes=%llu\n", c?"p=1(24)":"all", cnt[c]);
    for(int k=0;k<3;k++){ double mu=S[c][k][0]/cnt[c], v=S[c][k][1]/cnt[c]-mu*mu;
      printf("  %-14s mean=%.5f var=%.5f var/mean^2=%.5f\n",nm[k],mu,v,v/(mu*mu)); } }
  printf("odd squares in window: %llu, with Npair>0: %llu\n",sqn,sqbad);
  return 0;
}
