// z49 forestinv — census of U-words for all n ≡ 1 (mod 8), n ≤ N.
// A word is (t,u,v), all ≥ 1, n = tuv − u − v.  V = 4Z ∪ (8Z+7).  Endpoint x ∈ V with gcd(x,n) = 1 ⟺ gcd(u,v) = 1
// (because gcd(u,n) = gcd(u,v)).  Words with gcd(u,v) = g > 1 are the scalings of words of n/g with g | t.
// Per n we record: bit0 = U via a coprime word, bit1 = U via a non-coprime word, and the least V-endpoint (coprime).
// Output: summary + lists.  Usage: ./census N [listmax]
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
static long g_gcd(long a, long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
int main(int argc,char**argv){
  long N=atol(argv[1]); long listmax = argc>2? atol(argv[2]) : 2000000;
  long M = N/8+2;
  unsigned char *fl = calloc(M,1); unsigned int *vmin = malloc(M*sizeof(unsigned int));
  if(!fl||!vmin){fprintf(stderr,"alloc\n");return 1;}
  for(long i=0;i<M;i++) vmin[i]=0xffffffffu;
  for(long u=1; u<=N+2; u++){
    for(long t=1;;t++){ long A=t*u-1; if(A<1) continue; if(A>N+u) break;
      for(long v=1;;v++){ long n=A*v-u; if(n>N) break; if(n<9) continue; if((n&7)!=1) continue;
        int uV = ((u&3)==0)||((u&7)==7), vV = ((v&3)==0)||((v&7)==7);
        if(!(uV||vV)) continue;
        long i=n>>3; long g=g_gcd(u,v);
        if(g==1){ fl[i]|=1; unsigned int e = (unsigned int)(uV? (vV? (u<v?u:v):u) : v); if(e<vmin[i]) vmin[i]=e; }
        else fl[i]|=2;
      }
    }
  }
  // summary
  long cnt[3]={0,0,0}; long c105[8]={0}, f105[8]={0}; static long hist[9][40]; // row 0..7 composite class bits, row 8 primes; column = bit length of least coprime V-line (39 = none) long c105[8]={0}, f105[8]={0}; // composites by (3|n,5|n,7|n) bits: count, U_cop failures // index: 0 prime,1 composite nonsquare,2 square
  long okcop[3]={0,0,0}, okany[3]={0,0,0}, onlyfac[3]={0,0,0};
  // simple primality via sieve
  unsigned char *comp = calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  printf("# n  class(P/C/S)  flags  vmin_coprime\n");
  long listed=0;
  unsigned int vmax_c=0, vmax_p=0; long arg_c=0, arg_p=0;
  for(long n=9;n<=N;n+=8){ long i=n>>3; long m=(long)llround(sqrt((double)n)); int cl = (m*m==n)?2:(comp[n]?1:0);
    cnt[cl]++; if(cl!=2){ int row = (cl==0)?8:((n%3==0)|((n%5==0)<<1)|((n%7==0)<<2)); int col = (fl[i]&1)? (64-__builtin_clzl((long)vmin[i])) : 39; hist[row][col]++; }
    if(cl==1){int b=(n%3==0)|((n%5==0)<<1)|((n%7==0)<<2); c105[b]++; if(!(fl[i]&1)) f105[b]++;} if(fl[i]&1) okcop[cl]++; if(fl[i]) okany[cl]++; if(fl[i]==2) onlyfac[cl]++;
    if(cl!=2 && (fl[i]!=1) && fl[i]!=3 && listed<listmax){ printf("%ld %c %d %u\n", n, "PCS"[cl], fl[i], vmin[i]); listed++; }
    if(cl==2 && fl[i]) printf("SQUARE-VIOLATION %ld %d\n", n, fl[i]);
    if(cl==1 && (fl[i]&1) && vmin[i]>vmax_c){vmax_c=vmin[i];arg_c=n;}
    if(cl==0 && (fl[i]&1) && vmin[i]>vmax_p){vmax_p=vmin[i];arg_p=n;}
  }
  fprintf(stderr,"N=%ld\n",N);
  const char*nm[3]={"prime","composite nonsquare","square"};
  for(int c=0;c<3;c++) fprintf(stderr,"%-20s n: %ld  U_cop: %ld  U_any: %ld  U only via non-coprime words: %ld  FAIL: %ld\n", nm[c], cnt[c], okcop[c], okany[c], onlyfac[c], cnt[c]-okany[c]);
  for(int b=0;b<8;b++) fprintf(stderr,"composites with 3|n:%d 5|n:%d 7|n:%d  count %ld  U_cop failures %ld\n", b&1,(b>>1)&1,(b>>2)&1,c105[b],f105[b]);
  fprintf(stderr,"# histogram: row = class (bits 3|n,5|n,7|n; P = primes), columns = bitlength of least coprime V-line 2..24, then >2^24, none\n");
  for(int r=0;r<9;r++){ if(r<8) fprintf(stderr,"C%d%d%d", r&1,(r>>1)&1,(r>>2)&1); else fprintf(stderr,"P   "); long big=0; for(int c=25;c<39;c++) big+=hist[r][c]; for(int c=2;c<=24;c++) fprintf(stderr," %ld",hist[r][c]); fprintf(stderr," | %ld %ld\n",big,hist[r][39]); }
  fprintf(stderr,"max least coprime V-endpoint: composites %u at %ld; primes %u at %ld\n", vmax_c, arg_c, vmax_p, arg_p);
  return 0;
}
