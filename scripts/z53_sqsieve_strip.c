/* z53 SQSIEVE strip statistics.
   Strip A = {(C,k): W < C <= 2W, S1 < 4Ck-n <= S2}, f = (4Ck-n)^2 - 4k.
   Reports: |A|, #nonzero squares f, BM check (squares at gcd(Ck,n)=1 have jacobi(-k,n) = -1), |A-| = #{(-k/n) = -1},
   S_Q = sum_A (f/Q) for Q = q q' (q<q' primes in (P,2P]): max, rms;
   square-sieve statistics with sigma(a) = sum_{q in Pset} (a/q):  Lambda = sum_A sigma(f)^2, and the values of sigma
   realised by non-squares (min, max, whether 0/1 and +-x0 occur, x0 = least integer >= sqrt(P0) with x0 = P0 mod 2).
   usage: strip n W S1 S2 P            (all integers; n < 2^62) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull;
static int jac(ull a, ull n){ /* n odd positive */ int t=1; a%=n; while(a){ while(!(a&1)){ a>>=1; ull r=n&7; if(r==3||r==5) t=-t;} ull tmp=a; a=n; n=tmp; if((a&3)==3 && (n&3)==3) t=-t; a%=n;} return n==1?t:0; }
static int leg(ll a, ll q){ ll r=a%q; if(r<0) r+=q; return jac((ull)r,(ull)q); }
static ull gcdu(ull a, ull b){ while(b){ull t=a%b;a=b;b=t;} return a; }
int main(int argc,char**argv){
  if(argc<6){fprintf(stderr,"usage\n");return 1;}
  ll n=atoll(argv[1]), W=atoll(argv[2]), S1=atoll(argv[3]), S2=atoll(argv[4]), P=atoll(argv[5]);
  /* primes in (P,2P] */
  int np=0; ll *pr=malloc(sizeof(ll)*(P+10));
  for(ll q=P+1;q<=2*P;q++){ if(q<3) continue; int ok=1; for(ll d=2;d*d<=q;d++) if(q%d==0){ok=0;break;} if(ok && (q&1)) pr[np++]=q; }
  ll cap=1<<22; ll *Fv=malloc(sizeof(ll)*cap); ll *Kv=malloc(sizeof(ll)*cap); ll *Cv=malloc(sizeof(ll)*cap); ll m=0;
  ll nsq=0, nsq_bm_ok=0, nsq_cop=0, nminus=0;
  for(ll C=W+1;C<=2*W;C++){
    ll k=(n+S1)/(4*C)+1; /* smallest k with 4Ck-n > S1 */
    for(;;k++){ ll s=4*C*k-n; if(s>S2) break; if(s<=S1) continue;
      if(m>=cap){fprintf(stderr,"cap\n");return 2;}
      ll f=s*s-4*k; Fv[m]=f; Kv[m]=k; Cv[m]=C; m++;
      int bm = jac((ull)((n - (k%n))%n),(ull)n); if(bm==-1) nminus++;
      if(f>0){ ll r=(ll)sqrtl((long double)f); while(r*r>f) r--; while((r+1)*(r+1)<=f) r++;
        if(r*r==f){ nsq++; if(gcdu((ull)(C%n)*1ULL,(ull)n)==1 && gcdu((ull)(k%n),(ull)n)==1){ nsq_cop++; if(bm==-1) nsq_bm_ok++; } } }
    }
  }
  /* S_Q over pairs */
  double mx=0, ss=0; ll npairs=0;
  int *lg=malloc(sizeof(int)*m*1);
  /* sigma and Lambda */
  int *sig=calloc(m,sizeof(int));
  for(int i=0;i<np;i++){ for(ll j=0;j<m;j++) sig[j]+=leg(Fv[j],pr[i]); }
  for(int i=0;i<np;i++) for(int i2=i+1;i2<np;i2++){ ll S=0; for(ll j=0;j<m;j++) S+=leg(Fv[j],pr[i])*leg(Fv[j],pr[i2]); double a=fabs((double)S); if(a>mx) mx=a; ss+=a*a; npairs++; }
  double Lam=0, Lam_sq=0; int smin=1<<30, smax=-(1<<30); int x0=(int)ceil(sqrt((double)np)); if((x0-np)%2) x0++;
  int has0=0, hasp=0, hasm=0;
  for(ll j=0;j<m;j++){ ll f=Fv[j]; int isq=0; if(f>0){ ll r=(ll)sqrtl((long double)f); while(r*r>f) r--; while((r+1)*(r+1)<=f) r++; isq=(r*r==f);} 
    Lam+= (double)sig[j]*sig[j]; if(isq) Lam_sq+=(double)sig[j]*sig[j];
    if(!isq && f!=0){ if(sig[j]<smin) smin=sig[j]; if(sig[j]>smax) smax=sig[j]; if(abs(sig[j])<=1) has0=1; if(sig[j]==x0) hasp=1; if(sig[j]==-x0) hasm=1; } }
  printf("n=%lld W=%lld s in (%lld,%lld] P=%lld P0=%d |A|=%lld squares=%lld coprime_squares=%lld of_which_BM(-k/n)=-1:%lld |A-|=%lld\n",n,W,S1,S2,P,np,m,nsq,nsq_cop,nsq_bm_ok,nminus);
  printf("  S_Q over %lld pairs: max|S_Q|=%.0f rms=%.1f sqrt|A|=%.1f\n",npairs,mx,sqrt(ss/(npairs?npairs:1)),sqrt((double)m));
  printf("  Lambda=sum sigma^2=%.0f  (P0*|A|=%lld; squares contribute %.0f; (Lambda-P0|A|)/P0^2=%.3f)  nonsquare sigma range [%d,%d], x0=%d: sigma in{0,+-1}:%d sigma=+x0:%d sigma=-x0:%d\n",
    Lam,(ll)np*m,Lam_sq,(Lam-(double)np*m)/((double)np*np),smin,smax,x0,has0,hasp,hasm);
  return 0;
}
