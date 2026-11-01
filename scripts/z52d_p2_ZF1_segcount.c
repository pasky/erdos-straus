// z52d Pass-2 ZF1 (Z0762): exact U(n) = # unordered solutions x<=y<=z of 4/n = 1/x+1/y+1/z for ONE (possibly
// composite) n up to ~4e9, same enumeration as scripts/z52b_fingerprint_count.c but with a SEGMENTED factor sieve
// over x (the original needs an spf array of 3n ints, > 8 GB at n ~ 1e9).  x runs over (n/4, 3n/4]; for each x,
// 4/n - 1/x = A/B in lowest terms, and the (y,z) with y>=x are divisors d | B², d <= B, d ≡ -B (mod A), y=(d+B)/A.
// Usage: segcount n [part nparts]   (splits the x-range into nparts interleaved blocks; prints n part U O k1 k2 k3)
// Build: gcc -O2 -o segcount z52d_p2_ZF1_segcount.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef uint64_t u64; typedef __uint128_t u128;
static u64 gcdu(u64 a,u64 b){ while(b){ u64 t=a%b; a=b; b=t;} return a; }
#define MAXF 24
typedef struct { uint32_t q[12]; uint8_t k; } fent;
static uint32_t *sp; static int nsp;
static u64 N, X, A, B; static long long U, O, K[4];
static int np; static u64 pr[MAXF]; static int ex[MAXF];
static void addq(u64 q,int e){ for(int i=0;i<np;i++) if(pr[i]==q){ ex[i]+=e; return; } pr[np]=q; ex[np]=e; np++; }
static void rec(int i,u64 d){
  if(i==np){ if((d+B)%A==0){ u64 y=(d+B)/A; if(y>=X){ u128 z=((u128)B*B/d + B)/A; U++;
        int c=(X%N==0)+(y%N==0)+(z%N==0); K[c]++; if(X<y && y<z) O+=6; else if(X==y && y==z) O+=1; else O+=3; } } return; }
  u64 p=pr[i]; u64 dd=d; for(int e=0;e<=2*ex[i];e++){ if(dd>B) break; rec(i+1,dd); if((u128)dd*p > B) break; dd*=p; }
}
int main(int argc,char**argv){
  N=strtoull(argv[1],0,10); int part=argc>2?atoi(argv[2]):0, nparts=argc>3?atoi(argv[3]):1;
  u64 xlo=N/4+1, xhi=(3*N)/4; u64 S=(u64)sqrt((double)xhi)+10;
  { char *c=calloc(S+1,1); sp=malloc(sizeof(uint32_t)*(S/2+10)); nsp=0; for(u64 i=2;i<=S;i++){ if(c[i]) continue; sp[nsp++]=i; for(u64 j=i*i;j<=S;j+=i) c[j]=1; } free(c); }
  // factor N by trial division
  u64 nf[MAXF]; int ne[MAXF]; int nnf=0; { u64 r=N; for(u64 q=2;q*q<=r;q++) if(r%q==0){ nf[nnf]=q; ne[nnf]=0; while(r%q==0){ r/=q; ne[nnf]++; } nnf++; } if(r>1){ nf[nnf]=r; ne[nnf]=1; nnf++; } }
  const u64 L=1<<18; fent *T=malloc(sizeof(fent)*L); u64 *rem=malloc(sizeof(u64)*L);
  U=O=0; K[0]=K[1]=K[2]=K[3]=0; long long blk=0;
  for(u64 base=xlo; base<=xhi; base+=L, blk++){ if(blk%nparts!=part) continue;
    u64 len=L; if(base+len>xhi+1) len=xhi+1-base;
    for(u64 i=0;i<len;i++){ T[i].k=0; rem[i]=base+i; }
    for(int j=0;j<nsp;j++){ u64 q=sp[j]; if(q*q>base+len) break; u64 st=((base+q-1)/q)*q;
      for(u64 x=st;x<base+len;x+=q){ u64 i=x-base; T[i].q[T[i].k++]=q; while(rem[i]%q==0) rem[i]/=q; } }
    for(u64 i=0;i<len;i++){ X=base+i; u64 a=4*X-N, b; if(4*X<=N) continue; u128 bb=(u128)N*X; u64 g=gcdu(a, (u64)(bb%a)); A=a/g; B=(u64)(bb/g);
      np=0; for(int t=0;t<nnf;t++) addq(nf[t],ne[t]);
      { u64 r=X; for(int t=0;t<T[i].k;t++){ u64 q=T[i].q[t]; int e=0; while(r%q==0){ r/=q; e++; } addq(q,e); } if(r>1) addq(r,1); }
      { u64 r=g; for(int t=0;t<np && r>1;t++){ while(r%pr[t]==0){ r/=pr[t]; ex[t]--; } } if(r>1){ fprintf(stderr,"g residue %llu\n",(unsigned long long)r); exit(1);} }
      int j=0; for(int t=0;t<np;t++) if(ex[t]>0){ pr[j]=pr[t]; ex[j]=ex[t]; j++; } np=j; (void)b;
      rec(0,1); } }
  printf("%llu %d %lld %lld %lld %lld %lld\n",(unsigned long long)N,part,U,O,K[1],K[2],K[3]); return 0; }
