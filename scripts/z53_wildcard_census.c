// z53_wildcard_census.c — census of representability of n <= N by
//   (*)      n = 4uBC - u - B                      (u,B,C>=1)            [h=1 Type II]
//   TypeII   n*h = 4ahkC - a - k, i.e. n = 4akC - (a+k)/h with h | a+k   (a,k,C>=1)
//   TypeI    n*t = 4abC - 1 with t | a+b                                 (a,b,C,t>=1)
// Marks bit arrays and prints, for n ≡ 1 (mod 24), n <= N, those missing each family,
// flagging primes and squares.  Memory: 3 bit arrays of N bits.
// usage: ./a.out N
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static unsigned char *star, *t2, *t1, *comp;
#define SET(A,i) (A[(i)>>3] |= (1u<<((i)&7)))
#define GET(A,i) ((A[(i)>>3]>>((i)&7))&1)
int main(int argc,char**argv){
  u64 N = argc>1? strtoull(argv[1],0,10): 1000000;
  size_t bytes=(N>>3)+2;
  star=calloc(bytes,1); t2=calloc(bytes,1); t1=calloc(bytes,1); comp=calloc(bytes,1);
  // sieve composites
  for(u64 i=2;i*i<=N;i++) if(!GET(comp,i)) for(u64 j=i*i;j<=N;j+=i) SET(comp,j);
  // (*) and Type II: n = 4akC - s/h, s=a+k, h|s.  (h=1 -> star)
  for(u64 a=1; 4*a-1-a<=N; a++){
    for(u64 k=a; ; k++){
      u64 s=a+k; u64 base=4*a*k;
      if(base - s > N) break;
      for(u64 h=1; h<=s; h++){
        if(s%h) continue;
        u64 sub=s/h;
        for(u64 C=1;;C++){ u64 v=base*C; if(v<=sub) continue; v-=sub; if(v>N) break;
          if(h==1) SET(star,v); SET(t2,v); }
      }
    }
  }
  // Type I: n t = 4abC - 1, t | a+b, a<=b WLOG.  Then t | 4a^2 C + 1, b = t m - a (m >= ceil(2a/t)),
  // n = 4 a m C - e, e = (4a^2C+1)/t.  a<=b forces aC <= N/2.  We restrict a <= AMAX (partial census).
  u64 AMAX = argc>2? strtoull(argv[2],0,10): 300;
  for(u64 a=1; a<=AMAX && 2*a<=N; a++){
    for(u64 C=1; a*C*2<=N; C++){
      u64 M=4*a*a*C+1;
      // enumerate divisors t of M by trial division
      for(u64 r=1; r*r<=M; r++){ if(M%r) continue;
        u64 ts[2]={r, M/r}; int nt = (r*r==M)?1:2;
        for(int i=0;i<nt;i++){ u64 t=ts[i]; u64 e=M/t;
          u64 m0=(2*a+t-1)/t; if(m0==0) m0=1;
          for(u64 m=m0;;m++){ u64 v=4*a*m*C; if(v<=e) continue; v-=e; if(v>N) break; SET(t1,v); }
        }
      }
    }
  }
  // report
  u64 c_all=0,c_nostar=0,c_not2=0,c_not1=0,c_none=0, p_all=0,p_nostar=0,p_not2=0,p_not1=0,p_none=0;
  printf("# n  prime? square? star t2 t1   (only n ≡ 1 mod 24 missing some family)\n");
  for(u64 n=25;n<=N;n+=24){
    int pr=!GET(comp,n), sq=((u64)sqrt((double)n))*((u64)sqrt((double)n))==n || ((u64)sqrt((double)n)+1)*((u64)sqrt((double)n)+1)==n;
    int s=GET(star,n), a=GET(t2,n), b=GET(t1,n);
    c_all++; if(pr)p_all++;
    if(!s){c_nostar++; if(pr)p_nostar++;}
    if(!a){c_not2++; if(pr)p_not2++;}
    if(!b){c_not1++; if(pr)p_not1++;}
    if(!a&&!b){c_none++; if(pr)p_none++;}
    if(!s||!a||!b) printf("%llu %d %d %d %d %d\n",n,pr,sq,s,a,b);
  }
  printf("# totals n≡1(24)<=%llu: all=%llu nostar=%llu noT2=%llu noT1=%llu none=%llu\n",N,c_all,c_nostar,c_not2,c_not1,c_none);
  printf("# primes: all=%llu nostar=%llu noT2=%llu noT1=%llu none=%llu\n",p_all,p_nostar,p_not2,p_not1,p_none);
  return 0;
}
