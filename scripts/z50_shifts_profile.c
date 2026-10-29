// z50 shifts (profile variant): joint failure vs product of marginals conditioned on the quadratic profile of n mod 3,5,7,11,13.
// z50 shifts: marginal and joint failure of the shift events for U.
// For n ≡ 1 (mod 4), n <= N, and v in C_n = 4Z ∪ (8Z - n), 3 <= v <= VMAX (VMAX <= 128):
//   hit(n,v) = 1 iff n+v has a divisor d ≡ -1 (mod v)   (any d >= 1, including d = n+v).
// Output (per class n mod 8 in {1,5}):
//   per v: #n with hit(n,v)=0 (marginal failure count),
//   per V: J(V) = #n with hit(n,v)=0 for all v in C_n, v <= V (joint failure),
//   and the list of n with J(VMAX) failure that are not squares (up to a cap).
// Usage: z50_shifts_joint N [VMAX]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

static int is_sq(long n){ long r=(long)llround(sqrt((double)n)); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r*r==n; }

int main(int argc,char**argv){
  long N=atol(argv[1]); int VMAX = argc>2? atoi(argv[2]):128; if(VMAX>128) VMAX=128;
  long M=N+VMAX;            // largest m = n+v
  long nidx=N/4+1;          // n = 4i+1
  uint64_t *hit=calloc(2*nidx,sizeof(uint64_t)); // bit v-1 ... store v in [1,128] as bit (v-1)
  if(!hit){fprintf(stderr,"oom\n");return 1;}
  // for each d, list of v<=VMAX with v | d+1, v>=3
  for(long d=1; d<=M; d++){
    long dp1=d+1;
    for(int v=3; v<=VMAX; v++){
      if(dp1%v) continue;
      // v must be in C_n: v%4==0 (any n≡1 mod 4) or v odd with v ≡ -n mod 8 (i.e. n ≡ -v mod 8)
      int vodd = v&1;
      if(!vodd && (v%4)) continue;      // v ≡ 2 mod 4 never in C_n
      if(vodd && ((v%8)!=3 && (v%8)!=7)) continue; // need -v mod 8 in {1,5}
      // multiples m = d*e, n = m - v, need n>=1, n ≡ 1 (4); if v odd need n ≡ -v (8)
      long target_mod = vodd? 8:4;
      long nres = vodd? ((8-(v%8))%8) : 1;      // required n mod target_mod
      long mres = (nres + v) % target_mod;       // required m mod target_mod
      // m = d*e ≡ mres (mod target_mod): iterate e and test (cheap filter)
      long emin = (v+1 + d-1)/d; if(emin<1) emin=1;
      for(long e=emin; d*e<=M; e++){
        long m=d*e; if((m%target_mod)!=mres) continue;
        long n=m-v; if(n<1||n>N) continue;
        long i=n>>2; int b=v-1; hit[2*i+(b>>6)] |= (1ULL<<(b&63));
      }
    }
  }

  // profile analysis, class n ≡ 1 mod 8 only. profile = ((n/p) in {0,+1,-1}) for p in PR[]
  int PR[]={3,5,7,11,13}; int NP=5; int NPROF=243;
  long *pc=calloc(NPROF,sizeof(long)); long *pmf=calloc((long)NPROF*(VMAX+1),sizeof(long)); long *pJ=calloc((long)NPROF*(VMAX+1),sizeof(long));
  for(long n=1; n<=N; n+=8){
    if(is_sq(n)) continue;                 // squares removed: we study the non-square joint law
    int prof=0;
    for(int j=0;j<NP;j++){ int p=PR[j]; int r=n%p; int s=0; if(r==0) s=0; else { s=2; for(int x=1;x<p;x++) if((x*x)%p==r){s=1;break;} } prof=prof*3+s; }
    long i=n>>2; pc[prof]++;
    int firsthit=VMAX+1;
    for(int v=3; v<=VMAX; v++){
      int inC = (v%4==0) || ((v&1) && ((n+v)%8==0)); if(!inC) continue;
      int b=v-1; int h=(hit[2*i+(b>>6)]>>(b&63))&1;
      if(!h) pmf[(long)prof*(VMAX+1)+v]++; else if(v<firsthit) firsthit=v;
    }
    for(int V=3; V<firsthit && V<=VMAX; V++) pJ[(long)prof*(VMAX+1)+V]++;
  }
  long tot=0; for(int a=0;a<NPROF;a++) tot+=pc[a];
  printf("# nonsquare n≡1 mod 8, N=%ld, count=%ld; profiles over p=3,5,7,11,13\n",N,tot);
  printf("# V  -lnJ  -ln(prod marginals)  -ln(sum_prof w*prod cond marginals)  -ln(sum_prof w*Jprof)\n");
  double *lp=calloc(NPROF,sizeof(double)); double lpg=0;
  for(int V=3; V<=VMAX; V++){
    int inC1 = (V%4==0) || ((V&1) && ((1+V)%8==0));
    long J=0, mf=0; for(int a=0;a<NPROF;a++){ J+=pJ[(long)a*(VMAX+1)+V]; mf+=pmf[(long)a*(VMAX+1)+V]; }
    if(inC1){ lpg += log((double)mf/tot); for(int a=0;a<NPROF;a++) if(pc[a]) { long m=pmf[(long)a*(VMAX+1)+V]; lp[a] += (m>0? log((double)m/pc[a]) : -1e9); } }
    if(!inC1) continue;
    double mix=0; for(int a=0;a<NPROF;a++) if(pc[a]) mix += (double)pc[a]/tot*exp(lp[a]);
    printf("%d %.4f %.4f %.4f\n", V, J>0? -log((double)J/tot): 99.0, -lpg, -log(mix));
  }
  return 0;
}
