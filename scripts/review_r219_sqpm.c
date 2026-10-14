/* R219 from-scratch check of CONJECTURE SQ_± and related counts (O218 SYNTHESIS_SPARKS4 §2.5).
 * Words w=(t,u,v), tuv-u-v=n, A=tu-1, B=tv-1, AB=tn+1, chi=(-A/n) Jacobi.
 * For each odd non-square n<=N:
 *   ls  = least |t| with a signed (tuv!=0, not all >0) word of chi=-1
 *   lp  = least t>0 with a positive word of chi=-1   (ES-five via three-bit law)
 *   la  = least |t| with any word (signed or positive) of chi=-1
 * Usage: review_r219_sqpm N [mode]   mode 1 = also positive search (slower)
 * Factorisation: spf sieve up to SIEVE_T*N+1, trial division beyond. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

static uint32_t *spf; static int64_t L;
static int jacobi(int64_t a, int64_t n){ /* n odd >0 */
  a%=n; if(a<0)a+=n; int r=1;
  while(a){ while(!(a&1)){ a>>=1; int64_t m=n&7; if(m==3||m==5) r=-r; }
    int64_t tmp=a;a=n;n=tmp; if((a&3)==3&&(n&3)==3) r=-r; a%=n; }
  return n==1?r:0;
}
static int nf; static int64_t pr[64]; static int ex[64];
static void factor(int64_t m){ nf=0;
  if(m<L){ while(m>1){ int64_t p=spf[m]; int e=0; while(m%p==0){m/=p;e++;} pr[nf]=p;ex[nf++]=e;} return; }
  for(int64_t p=2;p*p<=m;p+=(p==2?1:2)){ if(m%p==0){int e=0; while(m%p==0){m/=p;e++;} pr[nf]=p;ex[nf++]=e;} }
  if(m>1){pr[nf]=m;ex[nf++]=1;}
}
static int64_t divs[1<<16]; static int nd;
static void gendiv(){ nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){ int cur=nd; int64_t pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pp; } } }
/* returns bitmask: 1 = signed chi=-1 word exists at this t, 2 = positive chi=-1 word exists */
static int slot(int64_t n,int64_t t){
  int64_t M=t*n+1; if(M==0) return 0; int64_t aM=M<0?-M:M; factor(aM); gendiv(); int res=0; int64_t at=t<0?-t:t;
  for(int i=0;i<nd;i++) for(int sg=-1;sg<=1;sg+=2){ int64_t A=sg*divs[i]; if(A==-1) continue; int64_t B=M/A; if(B==-1) continue;
    if(((A+1)%at)!=0) continue; if(((B+1)%at)!=0){fprintf(stderr,"BUG\n");exit(1);} 
    int64_t u=(A+1)/t, v=(B+1)/t; if(u==0||v==0) continue; if(t*u*v-u-v!=n){fprintf(stderr,"BUG2\n");exit(1);} 
    if(jacobi(-A,n)!=-1) continue; int pos=(t>0&&u>0&&v>0); res|= pos?2:1; }
  return res;
}
int main(int argc,char**argv){
  int64_t N=atoll(argv[1]); int mode=argc>2?atoi(argv[2]):0; int64_t ST=argc>3?atoll(argv[3]):20; L=ST*N+2;
  spf=calloc(L,4); for(int64_t i=2;i<L;i++) if(!spf[i]){ for(int64_t j=i;j<L;j+=i) if(!spf[j]) spf[j]=(uint32_t)i; }
  int64_t g6=0,g12=0,maxls=0,argls=0,maxlp=0,arglp=0, f6=0,f12=0,fp6=0,fp12=0, nfail=0,pfail=0,cnt=0, f6dec[8]={0};
  for(int64_t n=3;n<=N;n+=2){ int64_t r=(int64_t)llround(sqrt((double)n)); if(r*r==n) continue; cnt++;
    int64_t ls=0; for(int64_t s=1;s<=n+3&&!ls;s++){ if(slot(n,s)&1) ls=s; else if(slot(n,-s)&1) ls=s; }
    if(!ls){ nfail++; printf("SIGNED FAIL n=%lld\n",(long long)n);} 
    /* note: least |t| with signed OR positive chi=-1 is what 'failures of |t|<=6' may mean; track both */
    int64_t la=ls; for(int64_t s=1;s<la||(la==0&&s<=n+3);s++){ if(slot(n,s)||slot(n,-s)){la=s;break;} }
    if(la>6||la==0){ f6++; for(int k=0,d=1;k<8;k++,d*=10) if(n<=(int64_t)d*10) f6dec[k]++; }
    if(ls>6||ls==0) g6++; if(ls>12||ls==0) g12++;
    if(la>12||la==0){ f12++; printf("ANY>12 n=%lld la=%lld ls=%lld\n",(long long)n,(long long)la,(long long)ls);} 
    if(ls>maxls){maxls=ls;argls=n; printf("signed record n=%lld |t|=%lld\n",(long long)n,(long long)ls); fflush(stdout);} 
    if(mode){ int64_t lp=0; for(int64_t t=1;t<=n+3;t++) if(slot(n,t)&2){lp=t;break;}
      if(!lp){pfail++; printf("POS FAIL n=%lld\n",(long long)n);} if(lp>6||!lp) fp6++; if(lp>12||!lp) fp12++;
      if(lp>maxlp){maxlp=lp;arglp=n; printf("pos record n=%lld t=%lld\n",(long long)n,(long long)lp); fflush(stdout);} }
  }
  printf("N=%lld nonsq=%lld signedfail=%lld maxls=%lld@%lld | any>6:%lld any>12:%lld",(long long)N,(long long)cnt,(long long)nfail,(long long)maxls,(long long)argls,(long long)f6,(long long)f12);
  printf(" | any>6 cumulative <=1e1..: "); for(int k=0;k<8;k++) printf("%lld ",(long long)f6dec[k]);
  if(mode) printf("\n posfail=%lld maxlp=%lld@%lld pos>6:%lld pos>12:%lld",(long long)pfail,(long long)maxlp,(long long)arglp,(long long)fp6,(long long)fp12);
  printf("\n signed-only>6:%lld signed-only>12:%lld\n",(long long)g6,(long long)g12); return 0;
}
