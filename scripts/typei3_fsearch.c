/* O72 (POINTWISE_TYPEI3.md, Lemma 1.1): search certificates at the sign point x = (w at 2; -1 at r; 1 elsewhere)
   graded by one complementary divisor f (either F or e = N/F).  Complete for all certificates having a
   divisor f in [Ylo, Yhi) -- in particular all certificates with min(F,e) in that range -- at ANY height ck.
   Conditions (Lemma 1.1): m' | f+1, r^v | f-1, t <= v_2(f+w) [role F] or t <= v_2(w f+1) [role e],
   2^(t+gamma) * r^(v+b) * k' * m' = -1 (mod f), with m' = c'k', v = a+b, a odd, 0 <= gamma <= t-2.
   Output: CERT lines "c k F role f t gamma" (role F: F=f; role e: F=N/f), and a summary.
   Mass mode (5th arg present, e.g. "mass"): for f = 7 (16) record t_min(f), the least admissible t>=4 over all
   (m',k',v,a,s) with (iii); per dyadic f-bin print sum of 2*2^(4-t_min) = upper bound for the Haar measure of
   w in 9+16Z_2 killed by certificates with this f (two roles), t capped at 40.  w is ignored there.
   Hits print c,k as u128; for t+gamma > ~80 these can overflow -- every hit must be re-verified (typei3_verify.py).
   Usage: typei3_fsearch r w Ylo Yhi [mass]  (r = 3 mod 4 prime, w = 1 mod 4; f ranges over f=1 (r), f=-w (4)) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull; typedef unsigned __int128 u128; typedef __int128 i128;
#define S 1048576
#define MAXF 16
static ull rem_[S]; static int nf_[S]; static ull pr_[S][MAXF]; static int ex_[S][MAXF];
static ull *primes; static int np;
static void pru(u128 v){char b[50];int i=49;b[i]=0;if(!v){putchar('0');return;}while(v){b[--i]='0'+(int)(v%10);v/=10;}fputs(b+i,stdout);}
static ull mulm(ull a, ull b, ull m){return (ull)((u128)a*b%m);}
static int ctz64(ull x){return x?__builtin_ctzll(x):62;}

int main(int argc,char**argv){
  ll r=atoll(argv[1]); ll w=atoll(argv[2]); ull Ylo=strtoull(argv[3],0,10), Yhi=strtoull(argv[4],0,10);
  ull lim=(ull)sqrtl((long double)(Yhi+2))+2;
  char *comp=calloc(lim+1,1); primes=malloc(sizeof(ull)*(lim/2+10)); np=0;
  for(ull i=2;i<=lim;i++){ if(comp[i])continue; if(i>2&&i!=(ull)r)primes[np++]=i; for(ull j=i*i;j<=lim;j+=i)comp[j]=1; }
  ull M=4*(ull)r; /* f = f0 (mod M): f=1 (r), f = -w (4) */
  ull f0=0; for(ull x=0;x<M;x++) if(x%r==1 && ((x+w)%4+4)%4==0){f0=x;break;}
  ull start = Ylo<=f0?f0:Ylo+((f0+M-Ylo%M)%M);
  ll ncert=0; ull nf_tested=0; int mass=argc>5; double mbin[64]={0}; ll nbin[64]={0};
  for(ull base=start; base<Yhi; base+=(ull)S*M){
    ull cnt=S; if(base+(cnt-1)*M>=Yhi) cnt=(Yhi-base+M-1)/M;
    for(ull i=0;i<cnt;i++){ ull g=base+i*M+1; while(!(g&1))g>>=1; rem_[i]=g; nf_[i]=0; }
    for(int j=0;j<np;j++){ ull p=primes[j]; if(p*p>Yhi+2)break;
      /* indices i with base+i*M+1 = 0 mod p */
      ull Mp=M%p; if(Mp==0)continue;
      ull need=(p-(base+1)%p)%p; /* i*M = need mod p */
      ull Minv=1; { ll g0=p,x=0,x1=1,b=Mp; while(b){ll q=g0/b,t=g0-q*b;g0=b;b=t;t=x-q*x1;x=x1;x1=t;} x%=(ll)p; if(x<0)x+=p; Minv=x; }
      ull i0=mulm(need,Minv,p);
      for(ull i=i0;i<cnt;i+=p){ int e=0; while(rem_[i]%p==0){rem_[i]/=p;e++;} if(e){ pr_[i][nf_[i]]=p; ex_[i][nf_[i]]=e; nf_[i]++; } }
    }
    for(ull i=0;i<cnt;i++){
      ull f=base+i*M; if(f<Ylo||f>=Yhi||f<3)continue; nf_tested++;
      if(rem_[i]>1){ pr_[i][nf_[i]]=rem_[i]; ex_[i][nf_[i]]=1; nf_[i]++; }
      int TF=ctz64((ull)f+(ull)w), Te=ctz64((ull)w*(ull)f+1ULL); if(TF>60)TF=60; if(Te>60)Te=60;
      if(mass){ if(f%16!=7)continue; TF=Te=40; } /* mass mode: Haar-random w in 9+16Z_2, t capped at 40 */
      int tmin=99;
      int T=TF>Te?TF:Te; if(T<2)continue;
      int V=0; { ull q=f-1; while(q%r==0){q/=r;V++;} }
      if(V<1)continue;
      ull rp[130]; rp[0]=1%f; for(int s=1;s<=2*V+2;s++) rp[s]=(rp[s-1]*(ull)r)%f; /* f < 2^56 */
      /* all pairs (m',k') with k' | m' | A, built prime by prime */
      static ull pm[400000], pk[400000]; int nd=1; pm[0]=1; pk[0]=1;
      for(int q=0;q<nf_[i];q++){ int cur=nd; ull p=pr_[i][q]; int E=ex_[i][q];
        for(int z=0;z<cur;z++){ ull px=1; for(int x=0;x<=E;x++){ ull py=1; for(int y=0;y<=x;y++){ if(x||y){ pm[nd]=pm[z]*px; pk[nd]=pk[z]*py; nd++; } py*=p; } px*=p; } } }
      for(int x=0;x<nd;x++){ ull mp=pm[x], kp=pk[x], cp=mp/kp; {
          ull base_mk=mulm(mp%f,kp%f,f);
          for(int v=1;v<=V;v++) for(int a=1;a<=v;a+=2){ int b=v-a;
            ull R=mulm(base_mk,rp[v+b],f);
            ull xs=R; xs=xs*2; if(xs>=f)xs-=f; /* xs = 2^s R mod f, by doubling */
            for(int s=2;s<=2*T-2;s++){ xs=xs*2; if(xs>=f)xs-=f; if(xs!=f-1)continue;
              if(mass){ int tm=(s+3)/2; if(tm<4)tm=4; if(tm<tmin)tmin=tm; continue; }
              for(int role=0;role<2;role++){ int TR=role?Te:TF;
                for(int t=2;t<=TR;t++){ int gam=s-t; if(gam<0||gam>t-2)continue;
                  u128 c=((u128)1<<(t-2-gam)); for(int z=0;z<a;z++)c*=r; c*=cp;
                  u128 k=((u128)1<<gam); for(int z=0;z<b;z++)k*=r; k*=kp;
                  u128 N=1+4*c*k*k; u128 F= role? N/f : f;
                  ncert++; printf("CERT c="); pru(c); printf(" k="); pru(k); printf(" F="); pru(F);
                  printf(" role=%c f=%llu t=%d gamma=%d ck=",role?'e':'F',f,t,gam); pru(c*k); putchar('\n');
                }}}}}}
      if(mass && tmin<99) printf("B %llu %d\n",f,tmin);
      if(mass && tmin<99){ int bn=63-__builtin_clzll(f); nbin[bn]++; mbin[bn]+=2.0*ldexp(1.0,4-tmin); }
    }
  }
  if(mass){ double cum=0; for(int b=0;b<64;b++) if(nbin[b]){ cum+=mbin[b]; printf("f in [2^%d,2^%d): f with near misses (t>=4) %lld, mass %.6f, cumulative %.6f\n",b,b+1,nbin[b],mbin[b],cum);} }
  printf("r=%lld w=%lld f in [%llu,%llu): f tested %llu, certificate hits %lld\n",r,w,Ylo,Yhi,nf_tested,ncert);
  return 0;
}
