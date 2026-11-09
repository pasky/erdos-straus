// Cascade by minimal letter: for primes p = 1 (8) in [N0, N1], compute m(p) = min over U7 words (x,y,z),
// xyz - x - z = p, 8 | xy, of min(x,y,z).  Letter-C words:
//   x = C : p + C has a divisor d = -1 mod lcm(8,C)                  (word (C,(d+1)/C,(p+C)/d))
//   z = C : p + C has a divisor e = -1 mod C with 8 | x*y, x=(p+C)/e, y=(e+1)/C
//   y = C : C p + 1 has a divisor D = -1 mod lcm(8,C)                (word ((D+1)/C, C, (E+1)/C), E=(Cp+1)/D)
// argv[4] (optional, default 16): print DEEP lines for m(p) >= this.
// Outputs histogram of m(p), survivors S(C) = #{m(p) > C}, max m(p) and its p.  Optional filter: only primes in the
// Lemma-N norm chain (i)-(iv) (argv[3] = 1).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
static int *pr; static int npr;
static int factor(u64 n, u64 *ps, int *es){ int k=0; for(int i=0;i<npr;i++){ u64 q=pr[i]; if(q*q>n) break; if(n%q==0){ int e=0; while(n%q==0){n/=q;e++;} ps[k]=q; es[k]=e; k++; } } if(n>1){ps[k]=n;es[k]=1;k++;} return k; }
static int ndiv; static u64 divs[1<<16];
static void gen(u64 *ps,int *es,int k){ ndiv=1; divs[0]=1; for(int i=0;i<k;i++){ int cur=ndiv; u64 m=1; for(int e=1;e<=es[i];e++){ m*=ps[i]; for(int j=0;j<cur;j++) divs[ndiv++]=divs[j]*m; } } }
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int v2(u64 a){int v=0; while(!(a&1)){a>>=1;v++;} return v;}
static int word_with_letter(u64 p, u64 C){
  u64 L = 8*C/gcdu(8,C); u64 ps[64]; int es[64];
  int k=factor(p+C,ps,es); gen(ps,es,k);
  for(int i=0;i<ndiv;i++){ u64 d=divs[i];
    if((d+1)%L==0) return 1;                                    // x = C
    if((d+1)%C==0){ u64 x=(p+C)/d, y=(d+1)/C; if(v2(x)+v2(y)>=3) return 2; } // z = C
  }
  k=factor(C*p+1,ps,es); gen(ps,es,k);
  for(int i=0;i<ndiv;i++){ u64 D=divs[i]; if((D+1)%L==0) return 3; }   // y = C
  return 0;
}
int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage: N0 N1 chainonly\n");return 1;}
  u64 N0=atoll(argv[1]), N1=atoll(argv[2]); int chain=atoi(argv[3]); int deep=argc>4?atoi(argv[4]):16;
  int PL=2000000; char*s=calloc(PL+1,1); pr=malloc(sizeof(int)*200000); npr=0;
  for(int i=2;i<=PL;i++){ if(!s[i]){ pr[npr++]=i; for(long j=(long)i*i;j<=PL;j+=i) s[j]=1; } }
  // segmented primality for [N0,N1] via trial division by pr (N1 <= 4e12)
  long hist[100000]; memset(hist,0,sizeof hist); long cnt=0; u64 maxm=0, argm=0;
  // segmented Eratosthenes over [N0, N1] in blocks of 2^24 (needs N1 <= 4e12)
  const u64 B=1ull<<24; unsigned char *seg=malloc(B);
  for(u64 lo=N0; lo<=N1; lo+=B){ u64 hi=lo+B-1; if(hi>N1) hi=N1; memset(seg,1,hi-lo+1);
    for(int i=0;i<npr;i++){ u64 q=pr[i]; if(q*q>hi) break; u64 st=((lo+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<=hi;j+=q) seg[j-lo]=0; }
  for(u64 p=lo+((9+8-lo%8)%8); p<=hi; p+=8){ if(p<17) continue; if(p%8!=1) {fprintf(stderr,"bug\n");return 1;}
    if(!seg[p-lo]) continue;
    if(chain){ u64 ps[64]; int es[64]; int ok=1; int k=factor((p+1)/2,ps,es); for(int i=0;i<k;i++) if(ps[i]%4!=1) ok=0;
      k=factor(p+4,ps,es); for(int i=0;i<k&&ok;i++) if(ps[i]%4!=1) ok=0;
      k=factor(p+2,ps,es); for(int i=0;i<k&&ok;i++) if(ps[i]%8!=1&&ps[i]%8!=3) ok=0;
      int h3=0,h5=0,h7=0; k=factor(p+8,ps,es); for(int i=0;i<k;i++){int t=ps[i]%8; h3|=t==3; h5|=t==5; h7|=t==7;}
      if(!ok||h7||(h3&&h5)) continue; }
    cnt++;
    u64 C; for(C=1;C<100000;C++) if(word_with_letter(p,C)) break;
    hist[C]++; if(C>maxm){maxm=C;argm=p; printf("REC p=%llu m=%llu\n",p,C); fflush(stdout);}
    if(C>=(u64)deep){ printf("DEEP p=%llu m=%llu\n",p,C); fflush(stdout);}
  }}
  printf("primes=%ld max m=%llu at p=%llu\n",cnt,maxm,argm);
  long surv=cnt; for(u64 C=1;C<=maxm;C++){ surv-=hist[C]; if(hist[C]||C<=16) printf("C=%llu hits=%ld survivors=%ld\n",C,hist[C],surv); }
}
