// z57 BFII: least Type II witness modulus per prime.
// For prime p = 1 (4) in [lo, hi): least f = 3 (mod 4) such that  -p mod f  lies in
//   T_f = { a * c^{-1} : a c | m_f },  m_f = (f+1)/4      (i.e. f = 4acd-1 divides c p + a)
// and the least such f using c = 1 only ((★)-line).  Histogram of least f; records maxima.
// Usage: z57_bfii_witness lo hi FMAX
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static u64 pw(u64 b,u64 e,u64 m){u64 r=1;b%=m;while(e){if(e&1)r=(unsigned __int128)r*b%m;b=(unsigned __int128)b*b%m;e>>=1;}return r;}
static uint32_t *dstart,*dcnt,*divs; static long MM;
static void build(long M){MM=M;dcnt=calloc(M+2,4);for(long e=1;e<=M;e++)for(long m=e;m<=M;m+=e)dcnt[m]++;
  dstart=malloc((M+2)*4);dstart[0]=0;for(long m=1;m<=M+1;m++)dstart[m]=dstart[m-1]+dcnt[m-1];
  divs=malloc((u64)dstart[M+1]*4);memset(dcnt,0,(M+2)*4);
  for(long e=1;e<=M;e++)for(long m=e;m<=M;m+=e){divs[dstart[m]+dcnt[m]]=e;dcnt[m]++;}}
// returns 2 if witness with c=1 exists, 1 if only c>=2, 0 none
static int test(u64 p,long f){long m=(f+1)/4; u64 r=(f-(p%f))%f; int found=0;
  for(uint32_t k=dstart[m];k<dstart[m]+dcnt[m];k++){long c=divs[k]; long a=(long)((r*(u64)c)%f); if(a==0) continue;
    long mc=m/c; if(mc%a==0){ if(c==1) return 2; found=1; }}
  return found;}
int main(int argc,char**argv){
  u64 lo=strtoull(argv[1],0,10),hi=strtoull(argv[2],0,10); long FMAX=atol(argv[3]);
  build((FMAX+1)/4+1);
  // segmented sieve
  u64 sq=(u64)sqrt((double)hi)+2; char*small=calloc(sq+1,1); long*pr=malloc(sizeof(long)*(sq+1)); long np=0;
  for(u64 i=2;i<=sq;i++) if(!small[i]){pr[np++]=i; for(u64 j=i*i;j<=sq;j+=i) small[j]=1;}
  long *hist=calloc(FMAX+2,sizeof(long)), *hist1=calloc(FMAX+2,sizeof(long)); long nprimes=0, none=0, none1=0;
  long viol=0,maxnq=0,bestatnq=0; u64 argr=0,argnq=0; double maxratio=0;
  long maxf=0; u64 argmaxf=0; long maxf1=0; u64 argmaxf1=0;
  u64 SEG=1<<24; char*seg=malloc(SEG);
  for(u64 s=lo;s<hi;s+=SEG){u64 e=s+SEG<hi?s+SEG:hi; memset(seg,0,e-s);
    for(long i=0;i<np;i++){u64 q=pr[i]; if(q*q>=e) break; u64 st=((s+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<e;j+=q) seg[j-s]=1;}
    for(u64 n=s;n<e;n++){ if(n<5||seg[n-s]||(n&3)!=1) continue; nprimes++;
      long best=0,best1=0;
      for(long f=3;f<=FMAX;f+=4){ if((u64)f>=n) break; int t=test(n,f);
        if(t&&!best) best=f; if(t==2){best1=f;break;} }
      { long l; for(l=0;l<np;l++){ if(pw(pr[l],(n-1)/2,n)==n-1) break; } long nq=pr[l];
        if(best && best<nq) viol++; if(best){ double rt=(double)best/nq; if(rt>maxratio){maxratio=rt;argr=n;} if(nq>maxnq){maxnq=nq;argnq=n;bestatnq=best;} } }
      if(best){hist[best]++; if(best>maxf){maxf=best;argmaxf=n;}} else none++;
      if(best1){hist1[best1]++; if(best1>maxf1){maxf1=best1;argmaxf1=n;}} else none1++;
    }}
  printf("range [%llu,%llu) primes=1(4): %ld  FMAX=%ld\n",lo,hi,nprimes,FMAX);
  printf("Type II: none found %ld; max least f = %ld at p=%llu\n",none,maxf,argmaxf);
  printf("c=1 line: none found %ld; max least f = %ld at p=%llu\n",none1,maxf1,argmaxf1);
  printf("least-QNR check: violations (least f < n_p) = %ld; max least f / n_p = %.2f at p=%llu; max n_p = %ld at p=%llu (least f there %ld)\n",viol,maxratio,argr,maxnq,argnq,bestatnq);
  printf("hist least f (TypeII | c=1):\n"); long cum=0,cum1=0;
  for(long f=3;f<=FMAX;f+=4){ if(hist[f]||hist1[f]){cum+=hist[f];cum1+=hist1[f]; if(f<200||hist[f]) printf("%ld %ld %ld  cum %.6f %.6f\n",f,hist[f],hist1[f],(double)cum/nprimes,(double)cum1/nprimes);} }
  return 0;}
