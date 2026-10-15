/* z1 (O224): Legendre levels. For odd n and level t with t*n = 4^a(8b+7), every word at level t has chi=-1
   (TWO_FIBRES Thm A + Legendre). Count, for n in a population, the least Legendre level carrying a word.
   usage: z1_legendre N T mode   mode 0: primes p=1 mod 4 <= N ; mode 1: odd squares m^2 <= N; mode 2: the single n = N  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
static int isleg(u64 x){ while(x%4==0) x/=4; return x%8==7; }
static int nf; static u64 pf[64]; static int pe[64];
static void factor(u64 x){ nf=0; for(u64 d=2; d*d<=x; d+= (d==2?1:2)){ if(x%d==0){ pf[nf]=d; pe[nf]=0; while(x%d==0){x/=d; pe[nf]++;} nf++; } } if(x>1){pf[nf]=x;pe[nf]=1;nf++;} }
/* enumerate divisors; return number of admissible A (A=-1 mod t, N/A=-1 mod t); flag8: some with 8 | penta */
static int count_words(u64 t, u64 N, int *has8){
  u64 divs[20000]; int nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){ int cur=nd; u64 pw=1; for(int e=1;e<=pe[i];e++){ pw*=pf[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
  int c=0; *has8=0;
  for(int j=0;j<nd;j++){ u64 A=divs[j], B=N/A; if((A+1)%t==0 && (B+1)%t==0){ u64 u=(A+1)/t, v=(B+1)/t; if(u>=1&&v>=1){ c++;
        if(t%8==0||u%8==0||v%8==0||A%8==0||B%8==0) *has8=1; } } }
  return c;
}
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10), T=strtoull(argv[2],0,10); int mode=atoi(argv[3]);
  char *sv=0; if(mode==0){ sv=calloc(N+1,1); for(u64 i=2;i*i<=N;i++) if(!sv[i]) for(u64 j=i*i;j<=N;j+=i) sv[j]=1; }
  long pop=0, fail=0, fail8=0, words_at_leg=0; u64 worst=0, worstn=0; long hist[64]={0};
  for(u64 k=(mode==2?N:3);k<=N;k++){
    u64 n;
    if(mode==2){ n=k; }
    else if(mode==0){ if(sv[k]||k%4!=1) continue; n=k; }
    else { if(k%2==0) continue; n=k*k; if(n>N) break; }
    pop++; u64 least=0; int got8=0;
    for(u64 t=1;t<=T && t<=n+2;t++){ if(!isleg(t*n)) continue; u64 M=t*n+1; factor(M); int h8; int c=count_words(t,M,&h8);
      if(c){ words_at_leg+=c; if(!least) least=t; if(h8) got8=1; if(mode!=1 && got8) break; } }
    if(!least){ fail++; if(mode!=1 && fail<=10) printf("no Legendre level <= %llu: n=%llu\n",T,n); }
    else { int b=0; u64 x=least; while(x>1){x>>=1;b++;} hist[b]++; if(least>worst){worst=least;worstn=n;} }
    if(!got8) fail8++;
  }
  printf("mode %d N %llu T %llu: population %ld, no-Legendre-word %ld, no-Legendre-S8-word %ld, worst least level %llu at n=%llu, words at Legendre levels (mode1 total) %ld\n",mode,N,T,pop,fail,fail8,worst,worstn,words_at_leg);
  for(int b=0;b<40;b++) if(hist[b]) printf("  least level in [2^%d,2^%d): %ld\n",b,b+1,hist[b]);
  return 0;
}
