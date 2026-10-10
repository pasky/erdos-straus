/* R128b from-scratch Type II counter (no author code reused).
   f_II(p) = #{(a,b,c,d) in N^4 : 4abcd = a+b+pc, gcd(a,c)=1}  (ordered, both orientations),
   enumerated as p = e*f - 4a^2 d, f = 4acd-1, b = ce - a >= a  (weight 2 if b > a, 1 if b == a).
   Usage: review_r128b_count X  -> prints checks for primes 5 <= p <= X.
   Build: gcc -O2 -o /tmp/r128b_count scripts/review_r128b_count.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static long g(long x, long y){ while(y){ long t=x%y; x=y; y=t;} return x; }
int main(int argc, char **argv){
  long X = atol(argv[1]);
  uint32_t *cnt = calloc(X+1, 4); uint16_t *cnt1 = calloc(X+1, 2);
  unsigned char *comp = calloc(X+1, 1);
  if(!cnt||!cnt1||!comp){ fprintf(stderr,"oom\n"); return 1; }
  for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
  long tuples=0;
  for(long a=1; 4*a*a <= X+2*a; a++)   /* p0 >= 4a^2 d - 2a/c */
    for(long d=1; 4*a*a*d <= X + 2*a; d++)
      for(long c=1; ; c++){
        long f = 4*a*c*d - 1;
        long e0 = (2*a + c - 1)/c;                  /* b = ce - a >= a */
        long p0 = e0*f - 4*a*a*d;
        if(p0 > X) { if(e0==1) break; else continue; }
        if(g(a,c)!=1) { continue; }
        for(long e=e0, p=p0; p<=X; e++, p+=f){
          long b = c*e - a; tuples++;
          int w = (b==a)?1:2;
          cnt[p]+=w; if(d==1) cnt1[p]+=w;
        }
      }
  fprintf(stderr,"tuples %ld\n", tuples);
  long np=0, zero=0; double gmin=1e9; long gargp=0;
  for(int k=2;(1L<<k)<=X;k++){
    long lo=1L<<k, hi=(1L<<(k+1))-1; if(hi>X) hi=X;
    long m=-1, mp=0, d1e=0, nb=0; double rmin=1e9; long rp=0;
    for(long p=lo;p<=hi;p++){ if(p<5||comp[p]) continue; nb++;
      if(m<0||cnt[p]<m){m=cnt[p];mp=p;}
      if(cnt1[p]==0) d1e++;
      double r = cnt[p]/pow(log((double)p),3); if(r<rmin){rmin=r;rp=p;}
    }
    if(nb) printf("2^%d: primes %ld  min f_II %ld (p=%ld)  min f/log^3 %.4f (p=%ld)  d=1 empty %ld%s\n",
                  k,nb,m,mp,rmin,rp,d1e, hi<(1L<<(k+1))-1?" [partial]":"");
  }
  for(long p=5;p<=X;p++){ if(comp[p]) continue; np++; if(cnt[p]==0){zero++; printf("ZERO %ld\n",p);}
    if(p>=100000){ double r=cnt[p]/pow(log((double)p),3); if(r<gmin){gmin=r;gargp=p;} } }
  printf("primes 5..%ld: %ld, with f_II=0: %ld; min f/log^3 over p>=1e5: %.4f at p=%ld (f_II=%u)\n",
         X,np,zero,gmin,gargp,cnt[gargp]);
  if(argc>2) for(long p=5;p<=X;p++) if(!comp[p]) printf("DUMP %ld %u\n",p,cnt[p]);
  /* small-p sanity values */
  long sp[]={5,7,11,13,17,29,73,193,409};
  for(int i=0;i<9;i++) if(sp[i]<=X) printf("f_II(%ld)=%u\n",sp[i],cnt[sp[i]]);
  return 0;
}
