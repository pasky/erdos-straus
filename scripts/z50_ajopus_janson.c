// z50 ajopus: composite-modulus U-family at n ≡ 1 (mod 8): integer chain vs Haar-model chain vs Janson bound.
// Events: A in [Amin, Amax] with every prime factor >= pmin, v | A+1, v ≡ 0 (4) or v ≡ 7 (8), class n ≡ -v (mod A),
// proper: A < n+v.  (Even A only possible when v is odd; 2-adic consistency with n ≡ 1 (8) is checked.)
// Order: by A, then v.  Integer side: n = 8k+1 <= N.  Model side: Monte Carlo over independent prime-power residues
// (2-adic residue uniform on 1 + 8Z mod 2^k), first-hit index per sample.
// Prints: mu, Delta (bit-sharing compatible pairs), max P, max conflict sum, survival: integer, model (MC), exp(-mu),
// exp(-mu + e^{1/3} Delta), and per-checkpoint chain sums (integer, model).
// Usage: janson N Amin Amax pmin nsamples seed
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef long long ll;
static uint64_t rs=0x9E3779B97F4A7C15ULL; static uint64_t xr(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static ll gcdl(ll a, ll b){ while(b){ ll t=a%b; a=b; b=t; } return a; }
#define MAXE 400000
ll EA[MAXE], EV[MAXE]; double EP[MAXE]; int ne=0;
int ncomp[MAXE]; int cidx[MAXE][8]; ll cmod[MAXE][8]; ll ctar[MAXE][8];
int main(int argc, char**argv){
  if(argc<7){ fprintf(stderr,"usage\n"); return 1; }
  ll N=atoll(argv[1]), Amin=atoll(argv[2]), Amax=atoll(argv[3]), pmin=atoll(argv[4]); ll S=atoll(argv[5]); rs^=(uint64_t)atoll(argv[6])*0xD1B54A32D192ED03ULL;
  // primes and prime powers
  int *spf=calloc(Amax+2,sizeof(int)); for(ll i=2;i<=Amax+1;i++) if(!spf[i]) for(ll j=i;j<=Amax+1;j+=i) if(!spf[j]) spf[j]=i;
  int np=0; ll *P=malloc(sizeof(ll)*(Amax+1)), *PK=malloc(sizeof(ll)*(Amax+1)); int *pidx=calloc(Amax+2,sizeof(int));
  for(ll p=2;p<=Amax;p++) if(spf[p]==p){ ll q=p; while(q*p<=Amax) q*=p; if(p==2 && q<8) q=8; P[np]=p; PK[np]=q; pidx[p]=np; np++; }
  for(ll A=Amin; A<=Amax; A++){
    // roughness
    ll t=A; int ok=1; while(t>1){ ll p=spf[t]; if(p<pmin) ok=0; while(t%p==0) t/=p; } if(!ok) continue;
    ll a=A+1; // divisors of a
    ll ps[32]; int es[32]; int nps=0; t=a; while(t>1){ ll p=spf[t]; int e=0; while(t%p==0){t/=p;e++;} ps[nps]=p; es[nps]=e; nps++; }
    ll all[4096]; int na=1; all[0]=1; for(int i=0;i<nps;i++){ int cur=na; ll pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur;j++) all[na++]=all[j]*pw; } }
    for(int j=0;j<na;j++){ ll v=all[j]; if(!(v%4==0 || v%8==7)) continue;
      // 2-adic part of A
      ll A2=1; t=A; while(t%2==0){ t/=2; A2*=2; } ll Aodd=t;
      ll m2 = A2<8?A2:8; if( (((-v)%m2)+m2)%m2 != 1%m2 ) continue;
      double p2 = (double)m2/(double)A2;
      if(ne>=MAXE){ fprintf(stderr,"too many events\n"); return 1; }
      EA[ne]=A; EV[ne]=v; EP[ne]=p2/(double)Aodd;
      // components
      int nc=0; t=A; while(t>1){ ll p=spf[t]; ll pe=1; while(t%p==0){t/=p; pe*=p;} cidx[ne][nc]=pidx[p]; cmod[ne][nc]=pe; ctar[ne][nc]=(((-v)%pe)+pe)%pe; nc++; }
      ncomp[ne]=nc; ne++; }
  }
  // mu, Delta, local quantities
  double mu=0, Delta=0, maxP=0, maxconf=0;
  double *conf=calloc(ne,sizeof(double));
  for(int i=0;i<ne;i++){ mu+=EP[i]; if(EP[i]>maxP) maxP=EP[i]; }
  for(int i=0;i<ne;i++) for(int j=i+1;j<ne;j++){
    ll g=gcdl(EA[i],EA[j]); if(g==1) continue;
    ll go=g; while(go%2==0) go/=2; ll g2=g/go;
    int share = (go>1) || (g2>=16);
    int compat = ((EV[i]-EV[j])%g==0);
    if(!compat){ conf[i]+=EP[j]; conf[j]+=EP[i]; continue; }
    if(!share) continue;
    ll L = EA[i]/g*EA[j]; ll L2=1, Lo=L; while(Lo%2==0){Lo/=2; L2*=2;} ll m2=L2<8?L2:8;
    Delta += ((double)m2/(double)L2)/(double)Lo;
  }
  for(int i=0;i<ne;i++) if(conf[i]>maxconf) maxconf=conf[i];
  // integer chain
  ll K=(N-1)/8+1; unsigned char *al=malloc(K); memset(al,1,K); al[0]=0; ll nal=K-1;
  double *rhoI=calloc(ne,sizeof(double));
  for(int i=0;i<ne;i++){
    ll A=EA[i], v=EV[i]; ll g=gcdl(A,8), step=A/g; ll k0=-1;
    for(ll k=0;k<step;k++){ if( ((8*k+1+v)%A)==0 ){ k0=k; break; } }
    if(k0<0){ continue; }
    ll excl=-1; if(A>v){ ll n0=A-v; if(n0>=1 && n0%8==1) excl=(n0-1)/8; }
    ll hits=0, before=nal; for(ll k=k0;k<K;k+=step){ if(k==excl) continue; if(al[k]){ al[k]=0; hits++; } }
    nal-=hits; rhoI[i]= before? (double)hits/before:0;
  }
  // model MC: first-hit index
  ll *firsthit=calloc(ne+1,sizeof(ll)); ll *res=malloc(sizeof(ll)*np);
  for(ll s=0;s<S;s++){
    for(int t2=0;t2<np;t2++){ ll q=PK[t2]; if(P[t2]==2){ res[t2]= 1 + 8*(ll)(xr()%(uint64_t)(q/8)); } else res[t2]=(ll)(xr()%(uint64_t)q); }
    int fh=ne;
    for(int i=0;i<ne;i++){ int hit=1; for(int c=0;c<ncomp[i];c++){ if(res[cidx[i][c]]%cmod[i][c]!=ctar[i][c]){ hit=0; break; } } if(hit){ fh=i; break; } }
    firsthit[fh]++;
  }
  // model chain
  double *rhoM=calloc(ne,sizeof(double)); ll aliveM=S;
  for(int i=0;i<ne;i++){ rhoM[i]= aliveM? (double)firsthit[i]/aliveM:0; aliveM-=firsthit[i]; }
  printf("# N=%lld Amin=%lld Amax=%lld pmin=%lld events=%d samples=%lld\n",N,Amin,Amax,pmin,ne,S);
  printf("mu %.5f Delta %.5f maxP %.5f maxconf %.5f\n",mu,Delta,maxP,maxconf);
  printf("surv_integer %.6e (count %lld of %lld)\n",(double)nal/(K-1),nal,K-1);
  printf("surv_model_MC %.6e (alive samples %lld)\n",(double)aliveM/S,aliveM);
  printf("exp(-mu) %.6e  exp(-mu+Delta) %.6e  exp(-mu+e^{1/3}Delta) %.6e\n",exp(-mu),exp(-mu+Delta),exp(-mu+exp(1./3)*Delta));
  // checkpoints: cumulative sums by A
  double cmu=0,cI=0,cM=0; ll nextA=Amin; printf("# A cum_mu cum_rho_int cum_rho_model\n");
  for(int i=0;i<ne;i++){ cmu+=EP[i]; cI+=rhoI[i]; cM+=rhoM[i]; if(i==ne-1 || EA[i+1]>=nextA*1.3){ printf("%lld %.5f %.5f %.5f\n",EA[i],cmu,cI,cM); while(nextA*1.3<=EA[i]) nextA=(ll)(nextA*1.3)+1; nextA=(ll)(EA[i]); } }
  return 0;
}
