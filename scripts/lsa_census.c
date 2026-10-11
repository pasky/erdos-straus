/* O135 LONGSHOT_PIGEONHOLE §3: e-slice census.
 * For each prime p (p = 1 mod 4) read from stdin, for e = 3,7,11,... <= E (p does not divide e),
 * T in {I,II}: N = (pe+1)/4 (I) or (p+e)/4 (II).  Factor N; then
 *   fib   = #{(a,b) ordered : ab | N, e | a+b}   (fibre size, Lemma 1.1)
 *   P     = [Sigma_e(N) contains the whole coset -K_e]              (full pigeonhole, all primes)
 *   TP    = [Sigma_e(L) * {M^-1,1,M} contains -K_e], L = prime powers of N with prime < e  (transparent)
 *   KN    = [Omega-type Kneser H={1} necessary test  sum_i(min(2v_i+1, ord g_i)-1) >= phi(e)-1]
 * Output one line per p:
 *   p nsliceI nsliceII fibI fibII nP nTP nKN maxomega minEsol minEP maxratio maxPphi maxTPphi nP20 nTP20
 * (maxPphi = largest |−K_e| = phi(e)/2 fully covered; nP20 = #P slices with phi(e)/2 >= 20)
 * where nslice = #e with fib>0, maxratio = max_e tau(N^2)/(phi(e)/2).
 * Usage: lsa_census E [verbose] < primes
 * verbose=1 prints per-slice lines "S p e T fib P TP omega tau2 phi" for slices with fib>0 or P or TP.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){ if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){if(n%sp[i]==0)return n==sp[i];}
  u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){u64 a=sp[i];u64 x=powmod(a,d,n);if(x==1||x==n-1)continue;int ok=0;
    for(int r=1;r<s;r++){x=mulmod(x,x,n);if(x==n-1){ok=1;break;}} if(!ok)return 0;} return 1;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){ if(n%2==0)return 2; for(u64 c=1;;c++){u64 x=2,y=2,d=1;
  while(d==1){x=(mulmod(x,x,n)+c)%n;y=(mulmod(y,y,n)+c)%n;y=(mulmod(y,y,n)+c)%n;d=gcdu(x>y?x-y:y-x,n);} if(d!=n)return d;}}
static int nf; static u64 fp[64]; static int fv[64];
static void addf(u64 q){for(int i=0;i<nf;i++)if(fp[i]==q){fv[i]++;return;} fp[nf]=q;fv[nf]=1;nf++;}
static void fac_rec(u64 n){ if(n==1)return; if(isprime(n)){addf(n);return;} u64 d=rho(n); fac_rec(d); fac_rec(n/d);}
static int smallp[200]; static int nsmall;
static void factor(u64 n){ nf=0; for(int i=0;i<nsmall;i++){u64 q=smallp[i]; if((u64)q*q>n)break; while(n%q==0){addf(q);n/=q;}} if(n>1)fac_rec(n);
  /* sort */ for(int i=0;i<nf;i++)for(int j=i+1;j<nf;j++)if(fp[j]<fp[i]){u64 t=fp[i];fp[i]=fp[j];fp[j]=t;int s=fv[i];fv[i]=fv[j];fv[j]=s;}}
/* Kronecker symbol (D/n), n>0 */
static int jacobi(long long a,long long n){ /* n odd positive */ int t=1; a%=n; if(a<0)a+=n;
  while(a){ while(!(a&1)){a>>=1; long long r=n&7; if(r==3||r==5)t=-t;} long long tmp=a;a=n;n=tmp; if((a&3)==3&&(n&3)==3)t=-t; a%=n;} return n==1?t:0;}
static int kron(long long D,long long n){ int t=1; while(!(n&1)){ n>>=1; long long r=((D%8)+8)%8; if(r%2==0) return 0; if(r==3||r==5)t=-t; } if(n==1)return t; return t*jacobi(D,n);}

static u64 phi_u(u64 n){u64 r=n; for(u64 q=2;q*q<=n;q++) if(n%q==0){while(n%q==0)n/=q; r-=r/q;} if(n>1)r-=r/n; return r;}
static unsigned char *bufA,*bufB; static int *chi; static int maxE;
static u64 inv_mod(u64 a,u64 m){ long long t=0,nt=1; long long r=m,nr=a%m; while(nr){long long q=r/nr; long long tmp=t-q*nt;t=nt;nt=tmp; tmp=r-q*nr;r=nr;nr=tmp;} if(t<0)t+=m; return (u64)t;}
/* BFS product set: start {1}; multiply by {g^t: |t|<=v} for each (g,v); returns set in bufA */
static void prodset(int e,int k,u64 *g,int *v){ memset(bufA,0,e); bufA[1%e]=1;
  for(int i=0;i<k;i++){ u64 gi=g[i]%e, ginv=inv_mod(gi,e); memset(bufB,0,e);
    for(int r=0;r<e;r++) if(bufA[r]){ bufB[r]=1; u64 x=r,y=r; for(int t=1;t<=v[i];t++){x=mulmod(x,gi,e);y=mulmod(y,ginv,e);bufB[x]=1;bufB[y]=1;} }
    unsigned char *tmp=bufA;bufA=bufB;bufB=tmp; } }
static int covers_negK(int e){ for(int r=1;r<e;r++) if(chi[r]==-1 && !bufA[r]) return 0; return 1; }
static int order_mod(u64 g,int e){ u64 x=g%e; int o=1; while(x!=1%e){x=mulmod(x,g%e,e);o++; if(o>e)return 0;} return o;}

int main(int argc,char**argv){
  int E=atoi(argv[1]); int verbose=argc>2?atoi(argv[2]):0; maxE=E+1;
  for(int q=2;nsmall<200;q++){int ok=1;for(int r=2;r*r<=q;r++)if(q%r==0){ok=0;break;} if(ok)smallp[nsmall++]=q;}
  bufA=malloc(maxE);bufB=malloc(maxE);chi=malloc(sizeof(int)*maxE);
  u64 p;
  while(scanf("%llu",&p)==1){ if(p%4!=1)continue;
    int nsl[2]={0,0}; u64 fib[2]={0,0}; int nP=0,nTP=0,nKN=0,maxom=0,minEsol=-1,minEP=-1; double maxratio=0; u64 maxPphi=0,maxTPphi=0; int nP20=0,nTP20=0;
    for(int e=3;e<=E;e+=4){ if(e%p==0)continue; u64 ph=phi_u(e);
      int chi_ready=0;
      for(int T=0;T<2;T++){ u64 N = T==0 ? (p*(u64)e+1)/4 : (p+(u64)e)/4;
        factor(N); if(nf>maxom)maxom=nf;
        double tau2=1; for(int i=0;i<nf;i++)tau2*=(2*fv[i]+1);
        if(tau2/(ph/2.0)>maxratio)maxratio=tau2/(ph/2.0);
        /* fibre count: enumerate divisors a, then b | N/a */
        static u64 divs[200000]; int nd=1; divs[0]=1;
        for(int i=0;i<nf;i++){int cur=nd; u64 pw=1; for(int t=1;t<=fv[i];t++){pw*=fp[i]; for(int j=0;j<cur;j++)divs[nd++]=divs[j]*pw;}}
        u64 cnt=0;
        for(int i=0;i<nd;i++){ u64 a=divs[i], Na=N/a; for(int j=0;j<nd;j++){u64 b=divs[j]; if(Na%b==0 && (a+b)%e==0)cnt++;}}
        if(cnt){nsl[T]++; fib[T]+=cnt; if(minEsol<0||e<minEsol)minEsol=e;}
        int Pf=0,TPf=0;
        if(tau2 >= ph/2.0){ if(!chi_ready){for(int r=0;r<e;r++)chi[r]=(gcdu(r,e)==1)?kron(-(long long)e,r):0; chi_ready=1;}
          prodset(e,nf,fp,fv); Pf=covers_negK(e); }
        /* transparent part */
        { u64 g[64];int v[64];int k=0; double t2=1; u64 L=1; for(int i=0;i<nf;i++) if(fp[i]<(u64)e){g[k]=fp[i];v[k]=fv[i];k++;t2*=(2*fv[i]+1); for(int t=0;t<fv[i];t++)L*=fp[i];}
          if(3*t2 >= ph/2.0 && Pf){ /* TP implies P, so only test when P holds */
            u64 M=N/L; if(M>1){g[k]=M;v[k]=1;k++;}
            prodset(e,k,g,v); TPf=covers_negK(e);} }
        if(Pf){nP++; if(minEP<0||e<minEP)minEP=e; if(ph/2>maxPphi)maxPphi=ph/2; if(ph/2>=20)nP20++;} if(TPf){nTP++; if(ph/2>maxTPphi)maxTPphi=ph/2; if(ph/2>=20)nTP20++;}
        { long s=0; for(int i=0;i<nf;i++){int o=order_mod(fp[i],e); int m=2*fv[i]+1; s+=(o<m?o:m)-1;} if(s>=(long)ph-1)nKN++; }
        if(verbose && (cnt||Pf||TPf)) printf("S %llu %d %c %llu %d %d %d %.0f %llu\n",p,e,T?'2':'1',cnt,Pf,TPf,nf,tau2,ph);
      }
    }
    printf("%llu %d %d %llu %llu %d %d %d %d %d %d %.3f %llu %llu %d %d\n",p,nsl[0],nsl[1],fib[0],fib[1],nP,nTP,nKN,maxom,minEsol,minEP,maxratio,maxPphi,maxTPphi,nP20,nTP20);
    fflush(stdout);
  }
  return 0;
}
