// z52d Pass-2 ZF1 (Z0885/Z0929/Z0685): model-guided candidate selection for small U(p)/log³p.
// For all primes p in [lo,hi) in the Mordell-hard classes mod 840, compute the partial Euler-product proxy
//   S(p) = Σ_{q ≤ 400 prime} −log(1 − χ_p(q)/q),  χ_p(q) = (q/p)  (= (p mod q / q) by reciprocity, p ≡ 1 mod 8),
// a proxy for log L(1, χ_p); on all 17 504 hard-class primes in [1e6,1e7] Spearman(U/log³p, S) = −0.63.
// Prints the top-K primes by S (p S leastQNR).  Usage: Lproxy_top lo hi K      Build: gcc -O2 -o Lproxy_top ... -lm
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
typedef uint64_t u64;
typedef struct { double s; u64 p; int lq; } ent;
static int cmp(const void*a,const void*b){ double x=((ent*)a)->s, y=((ent*)b)->s; return x<y?1:x>y?-1:0; }
int main(int argc,char**argv){ u64 lo=strtoull(argv[1],0,10), hi=strtoull(argv[2],0,10); int K=atoi(argv[3]);
  int qs[100], nq=0; for(int q=3;q<=400;q++){ int pr=1; for(int d=2;d*d<=q;d++) if(q%d==0){pr=0;break;} if(pr) qs[nq++]=q; }
  unsigned char *qr[100]; for(int i=0;i<nq;i++){ int q=qs[i]; qr[i]=calloc(q,1); for(int x=1;x<q;x++) qr[i][(x*x)%q]=1; }
  double cp[100], cm[100]; for(int i=0;i<nq;i++){ cp[i]=-log(1-1.0/qs[i]); cm[i]=-log(1+1.0/qs[i]); }
  double c2=-log(1-0.5); // p ≡ 1 (8): (2/p)=1
  u64 S=(u64)sqrt((double)hi)+2; char *c=calloc(S+1,1); u64 *sp=malloc(8*(S/2+10)); u64 ns=0;
  for(u64 i=2;i<=S;i++){ if(c[i]) continue; sp[ns++]=i; for(u64 j=i*i;j<=S;j+=i) c[j]=1; }
  int cap=K*4+1000; ent *top=malloc(sizeof(ent)*cap); int nt=0; double thr=-1e9; u64 nprimes=0;
  const u64 L=1<<24; char *seg=malloc(L);
  static const int hard[6]={1,121,169,289,361,529}; char ish[840]; memset(ish,0,840); for(int j=0;j<6;j++) ish[hard[j]]=1;
  for(u64 b=lo;b<hi;b+=L){ u64 len=L; if(b+len>hi) len=hi-b; memset(seg,1,len);
    for(u64 k=0;k<ns;k++){ u64 q=sp[k]; if(q*q>=b+len) break; u64 st=((b+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 x=st;x<b+len;x+=q) seg[x-b]=0; }
    for(u64 i=0;i<len;i++){ if(!seg[i]) continue; u64 p=b+i; if(p<2||!ish[p%840]) continue; nprimes++;
      double s=c2; int lq=0; for(int j=0;j<nq;j++){ int r=(int)(p%qs[j]); if(qr[j][r]) s+=cp[j]; else { s+=cm[j]; if(!lq) lq=qs[j]; } }
      if(s>thr || nt<K){ top[nt].s=s; top[nt].p=p; top[nt].lq=lq; nt++; if(nt>=cap){ qsort(top,nt,sizeof(ent),cmp); nt=K; thr=top[K-1].s; } } } }
  qsort(top,nt,sizeof(ent),cmp); if(nt>K) nt=K;
  fprintf(stderr,"hard-class primes in [%llu,%llu): %llu\n",(unsigned long long)lo,(unsigned long long)hi,(unsigned long long)nprimes);
  for(int i=0;i<nt;i++) printf("%llu %.4f %d\n",(unsigned long long)top[i].p,top[i].s,top[i].lq);
  return 0; }
