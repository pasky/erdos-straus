/* O264 goal 2: hardness scores for all primes p = 1 (mod 4), p <= X.
   Output text lines: p N1 fII m0 Mpts S e0 LI
   N1   = # Type A (b = 1) solutions = #{(c,d) : (4cd-1) | p + 4d}           (B1_LINE Lemma 3.1)
   fII  = # Type II solutions, ordered (a,b), ET form 4abcd = a + b + pc, gcd(a,c)=1 (logic of bs_prob_fII.c)
   m0   = least Type II window 4x - p, x = abd                                   (s7_window_lottery m0)
   Mpts = # ordered d = 1 meeting points (a,b,k), a + b = k(4ab - p)              (LATTICE_MEETING Prop 1.1)
   S    = # distinct slices g carrying a lattice ES point (2k,1), k | h           (both slices 4ka-1, 4kb-1)
   e0   = least Type I level e = 3 (4) with an ES solution containing p(pe+1)/4  (0 if none <= EMAX)
   LI   = # such levels e <= 199
   Usage: z34_scores X EMAX > out.txt      Build: gcc -O2 -o /tmp/z34_scores scripts/z34_scores.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef struct { uint32_t p; uint64_t g; } PG;
static int cmp(const void *x, const void *y){ const PG *a=x,*b=y;
  if(a->p!=b->p) return a->p<b->p?-1:1; if(a->g!=b->g) return a->g<b->g?-1:1; return 0; }
static long gcdl(long x, long y){ while(y){ long t=x%y; x=y; y=t;} return x; }
static uint32_t *spf; static long SL;
static int factor(long n, long *pr, int *ex){ int k=0;
  while(n>1){ long q;
    if(n<=SL) q=spf[n]; else { q=n; for(long r=2;r*r<=n;r+=(r==2?1:2)) if(n%r==0){q=r;break;} }
    int v=0; while(n%q==0){n/=q;v++;} pr[k]=q; ex[k]=v; k++; }
  return k; }
static int level_ok(long p, long e){ /* exists r | H^2 with r = -H mod e */
  long H=(p*e+1)/4; long pr[64]; int ex[64]; int k=factor(H,pr,ex);
  static unsigned char cur[100000], nxt[100000];
  long t=((-H)%e+e)%e; memset(cur,0,e); cur[1%e]=1; if(cur[t]) return 1;
  for(int i=0;i<k;i++){ memcpy(nxt,cur,e); long l=pr[i]%e;
    for(long x=0;x<e;x++) if(cur[x]){ long y=x; for(int j=1;j<=2*ex[i];j++){ y=y*l%e; nxt[y]=1; } }
    memcpy(cur,nxt,e); if(cur[t]) return 1; }
  return 0; }
int main(int argc,char**argv){
  if(argc<3){ fprintf(stderr,"usage: z34_scores X EMAX (EMAX >= 199, < 100000)\n"); return 1; }
  long X=atol(argv[1]), EMAX=atol(argv[2]);
  if(X<5 || EMAX<199 || EMAX>=100000){ fprintf(stderr,"need X >= 5 and 199 <= EMAX < 100000\n"); return 1; }
  unsigned char *comp=calloc(X+1,1);
  for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
  uint32_t *N1=calloc(X+1,4), *F=calloc(X+1,4), *MP=calloc(X+1,4); long *M0=malloc((X+1)*sizeof(long));
  for(long i=0;i<=X;i++) M0[i]=-1;
  /* N1 */
  for(long d=1; 8*d<=X+3; d++) for(long c=1; ; c++){ long w=4*c*d-1; if(w>X+4*d) break;
      long p=w-4*d; while(p<=0) p+=w; for(; p<=X; p+=w) N1[p]++; }
  /* fII, m0 */
  for(long a=1; 4*a*a <= X+2*a; a++) for(long d=1; 4*a*a*d <= X+2*a; d++){
    for(long c=1; ; c++){ long f=4*a*c*d-1; long e0=(2*a+c-1)/c; long p0=e0*f-4*a*a*d;
      if(p0>X){ if(e0==1) break; else continue; }
      if(gcdl(a,c)!=1) continue;
      for(long e=e0,p=p0; p<=X; e++,p+=f){ long b=c*e-a; F[p]+=(b==a)?1:2; long m=4*a*b*d-p;
        if(M0[p]<0||m<M0[p]) M0[p]=m; } } }
  /* d = 1 meeting locus: a <= b, g = 4ka-1 | p+4a^2 */
  long cap=1<<20, n=0; PG *L=malloc(cap*sizeof(PG));
  for(long a=1; 4*a-1 <= 1+2*X; a++){ if((4*a-1)*(4*a-1) > 4*X+1) break;
    for(long g=4*a-1; g<=X+4*a*a; g+=4*a){ long p=g-((4*a*a)%g); if(p==g) p=g; /* p = -4a^2 mod g, >0 */
      for(; p<=X; p+=g){ if(comp[p]||p%4!=1||p<5) continue; long m=(p+4*a*a)/g; if((p+m)%(4*a)) continue;
        long b=(p+m)/(4*a); if(b<a) continue; long k=(g+1)/(4*a); long D=4*k*b-1;
        MP[p]+=(b==a)?1:2;
        if(n+2>cap){ cap*=2; L=realloc(L,cap*sizeof(PG)); }
        L[n].p=p; L[n].g=g; n++; L[n].p=p; L[n].g=D; n++; } } }
  qsort(L,n,sizeof(PG),cmp);
  uint32_t *S=calloc(X+1,4);
  for(long i=0;i<n;i++) if(i==0||L[i].p!=L[i-1].p||L[i].g!=L[i-1].g) S[L[i].p]++;
  /* Type I levels */
  SL=(X*199+1)/4+1; spf=malloc((SL+1)*4); for(long i=0;i<=SL;i++) spf[i]=0;
  for(long i=2;i<=SL;i++) if(!spf[i]){ for(long j=i;j<=SL;j+=i) if(!spf[j]) spf[j]=i; }
  for(long p=5;p<=X;p+=4){ if(comp[p]) continue; long e0=0; int LI=0;
    for(long e=3;e<=EMAX;e+=4){ if(e%p==0) continue; if(e>199 && e0) break;
      if(level_ok(p,e)){ if(!e0) e0=e; if(e<=199) LI++; } }
    printf("%ld %u %u %ld %u %u %ld %d\n",p,N1[p],F[p],M0[p],MP[p],S[p],e0,LI); }
  return 0; }
