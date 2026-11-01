// Z0779: SEGMENTED word sieve, per-n counts for n = 1 (mod 4) (classes identical to scripts/z52b_fingerprint_words.c):
//   I3 = #{ordered (t,u,v) >= 3}, R = #{t in 4Z}, Uv = #{v >= 3, v in 4Z or v = -n mod 8}, over n = t*u*v - u - v.
// Windowed: for a window [A, A+W) every pair (t,u) is visited once with v restricted to v >= u (unordered in (u,v)); the
// ordered counts are rebuilt from both orders (t,u,v), (t,v,u).  v is further restricted by n = 1 (mod 4).  uint16 saturating.
// Per window: segmented prime sieve; for primes p = 1 (mod 4) emit stats (zeros, minima, histogram of small values,
// dyadic-window quantiles via a value histogram), optional per-prime dump.
// Per-window histogram lines (WX=2^j ...) are flushed after each window; the final X= block is then empty.
// usage: ./a.out A_start N_end W NPROC K [dumpfile]   (windows [A_start + i*W, ...) with i % NPROC == K)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef long long ll; typedef unsigned long long u64;
#define CAPV 65535
#define HB 4096
int main(int argc,char**argv){
  ll A0=atoll(argv[1]), NE=atoll(argv[2]), W=atoll(argv[3]); int NP=atoi(argv[4]), K=atoi(argv[5]);
  FILE *dump = argc>6 ? fopen(argv[6],"w") : NULL;
  ll sq=(ll)sqrtl((long double)NE)+2; char *bs=calloc(sq+1,1); ll *bp=malloc(sizeof(ll)*(sq/2+10)); ll nb=0;
  for(ll i=2;i<=sq;i++) if(!bs[i]){ bp[nb++]=i; for(ll j=i*i;j<=sq;j+=i) bs[j]=1; }
  ll L4=W/4+2; uint16_t *c=malloc(sizeof(uint16_t)*3*L4); char *pr=malloc(W+8);
  // stats: per dyadic window X=2^j: histograms of I3, R, Uv (capped at HB-1)
  static u64 H[64][3][HB]; static u64 cnt[64]; u64 sat=0, triples=0;
  #define BUMP(idx,k) do{ uint16_t *q_=c+3*(idx)+(k); if(*q_<CAPV) (*q_)++; else sat++; }while(0)
  ll iw=0;
  for(ll A=A0; A<NE; A+=W, iw++){
    if(iw%NP!=K) continue;
    ll B=A+W; if(B>NE) B=NE;      // window [A,B)
    memset(c,0,sizeof(uint16_t)*3*L4);
    // index of n (n = 1 mod 4) : (n - a1)/4 where a1 = first n>=A with n%4==1
    ll a1=A+((1-A%4)+4)%4;
    for(ll t=1;;t++){
      // smallest n for this t over u>=1 (v>=u): u=1: n=v(t-1)-1 with v>=1 -> t-2 ; need t*u>=2
      if(t>=3 && t-2 >= B) break;
      for(ll u=1;;u++){
        ll m=t*u-1; if(m<1) continue;
        ll nmin=u*m-u;            // v=u
        if(nmin>=B) break;
        // v >= u, v*m - u in [A,B) and = 1 mod 4
        ll vlo=(A+u+m-1)/m; if(vlo<u) vlo=u;
        ll vhi=(B-1+u)/m; if(vhi<vlo) continue;
        // congruence: v*m = 1+u (mod 4)
        ll g=m%4==0?4:(m%2==0?2:1); if(((1+u)%g)!=0) continue;
        ll st=4/g, v0=-1;
        { ll target=(1+u)%4; for(ll r=0;r<4;r++) if(((r*m-target)%4+4)%4==0){ v0=r; break; } }
        if(v0<0) continue;   // solutions of r*m = 1+u (mod 4) form the class v0 mod 4/g
        ll v=vlo + (((v0 - vlo)%st)+st)%st;
        int tR=(t%4==0), tI=(t>=3&&u>=3);
        for(; v<=vhi; v+=st){
          ll n=v*m-u; ll idx=(n-a1)>>2; triples++;
          int same=(u==v);
          if(tR){ BUMP(idx,1); if(!same) BUMP(idx,1); }
          if(tI){ BUMP(idx,0); if(!same) BUMP(idx,0); }
          if(v>=3 && ((v%4==0)||((v+n)%8==0))) BUMP(idx,2);
          if(!same && u>=3 && ((u%4==0)||((u+n)%8==0))) BUMP(idx,2);
        }
      }
    }
    // primes in [A,B)
    memset(pr,1,B-A);
    for(ll i=0;i<nb;i++){ ll q=bp[i]; if(q*q>=B) break; ll s=((A+q-1)/q)*q; if(s<q*q) s=q*q; for(ll j=s;j<B;j+=q) pr[j-A]=0; }
    for(ll n=a1;n<B;n+=4){ if(n<5||!pr[n-A]) continue; ll idx=(n-a1)>>2; uint16_t *r=c+3*idx;
      int j=63-__builtin_clzll((u64)n); cnt[j]++;
      for(int k=0;k<3;k++){ int x=r[k]<HB?r[k]:HB-1; H[j][k][x]++; }
      if(r[0]==0||r[1]==0||r[2]==0) printf("ZERO %lld I3=%u R=%u Uv=%u\n",n,r[0],r[1],r[2]);
      if(dump) fprintf(dump,"%lld %u %u %u\n",n,r[0],r[1],r[2]); }
    fprintf(stderr,"window [%lld,%lld) done\n",A,B);
    printf("#W [%lld,%lld) triples_so_far=%llu sat=%llu\n",A,B,triples,sat);
    for(int j=0;j<64;j++) if(cnt[j]){ printf("WX=2^%d cnt=%llu",j,cnt[j]); const char *nm[3]={"I3","R","Uv"};
      for(int k=0;k<3;k++){ printf(" | %s",nm[k]); for(int x=0;x<HB;x++) if(H[j][k][x]) printf(" %d:%llu",x,H[j][k][x]); } printf("\n"); }
    fflush(stdout); memset(cnt,0,sizeof(cnt)); memset(H,0,sizeof(H));
  }
  printf("# A0=%lld NE=%lld W=%lld K=%d/%d triples=%llu saturated=%llu\n",A0,NE,W,K,NP,triples,sat);
  for(int j=0;j<64;j++) if(cnt[j]){ printf("X=2^%d cnt=%llu",j,cnt[j]);
    const char *nm[3]={"I3","R","Uv"};
    for(int k=0;k<3;k++){ printf(" | %s",nm[k]); for(int x=0;x<HB;x++) if(H[j][k][x]) printf(" %d:%llu",x,H[j][k][x]); }
    printf("\n"); }
  if(dump) fclose(dump);
}
