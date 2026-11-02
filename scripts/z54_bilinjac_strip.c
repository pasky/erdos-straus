/* z54 BILINJAC — balanced-block strip statistics (falsifier for bilinear / additive-twist routes).
   Strip A = {(C,k): W < C <= 2W, S1 < s := 4Ck-n <= S2}, f = s^2 - 4k  (= (u-B)^2 on (*) solutions).
   Per n it prints one line with:
     A      = |A|;  sq = # f nonzero squares;  cnterr = (|A| - sum_C (S2-S1)/(4C)) / sqrt|A|   (short-interval count error)
     SQrms, SQmax = rms, max over pairs q<q' in (P,2P] (first npairs pairs) of |S_Q|/sqrt|A|, Q = q q'
     boxmax = max over pairs and over all 100 grid rectangles (4x4 grid in (C, s)) of |S_Q(rect)|/sqrt(|A(rect)|) (|A(rect)|>=16)
     for the prime q0 (additive analysis, Q = q0):
       Erms   = rms over (c,k) mod q0 of the class-count discrepancy E(c,k) = N(c,k) - |A|/q0^2, divided by sqrt(|A|/q0^2)
       Tmax   = max_{(a,b) != 0} |T(a,b)| / sqrt|A|,  T(a,b) = sum_A e((aC+bk)/q0)
       Trms   = rms_{(a,b) != 0} |T(a,b)| / sqrt|A|
       g1     = sum_{(a,b)} |ghat(a,b)|,  ghat(a,b) = q0^-2 sum_{c,k} (f(c,k)/q0) e(-(ac+bk)/q0)
       addbd  = |ghat(0,0)||A| + sum_{(a,b)!=0} |ghat||T|   (the additive-expansion triangle bound for |S_q0|), / sqrt|A|
       Sq0    = |S_q0| / sqrt|A|
   usage: strip n W S1 S2 P npairs q0                                                       (n < 2^62) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull;
static int jac(ull a, ull n){ int t=1; a%=n; while(a){ while(!(a&1)){ a>>=1; ull r=n&7; if(r==3||r==5) t=-t;} ull tmp=a; a=n; n=tmp; if((a&3)==3 && (n&3)==3) t=-t; a%=n;} return n==1?t:0; }
static int leg(ll a, ll q){ ll r=a%q; if(r<0) r+=q; return jac((ull)r,(ull)q); }
static int isprime(ll q){ if(q<2) return 0; for(ll d=2;d*d<=q;d++) if(q%d==0) return 0; return 1; }
int main(int argc,char**argv){
  if(argc<8){fprintf(stderr,"usage: strip n W S1 S2 P npairs q0\n");return 1;}
  ll n=atoll(argv[1]), W=atoll(argv[2]), S1=atoll(argv[3]), S2=atoll(argv[4]), P=atoll(argv[5]); int npairs=atoi(argv[6]); ll q0=atoll(argv[7]);
  int np=0; ll *pr=malloc(sizeof(ll)*(P+10)); for(ll q=P+1;q<=2*P;q++) if((q&1)&&isprime(q)) pr[np++]=q;
  ll cap=1<<22; ll *Fv=malloc(8*cap),*Kv=malloc(8*cap),*Cv=malloc(8*cap); int *cell=malloc(4*cap); ll m=0, nsq=0; double expct=0;
  for(ll C=W+1;C<=2*W;C++){
    expct += (double)(S2-S1)/(4.0*C);
    ll k=(n+S1)/(4*C); if(k<1) k=1;
    for(;;k++){ ll s=4*C*k-n; if(s>S2) break; if(s<=S1) continue;
      if(m>=cap){fprintf(stderr,"cap\n");return 2;}
      ll f=s*s-4*k; Fv[m]=f; Kv[m]=k; Cv[m]=C;
      int ic=(int)((C-W-1)*4/W), is=(int)((s-S1-1)*4/(S2-S1)); if(ic>3) ic=3; if(is>3) is=3; cell[m]=ic*4+is; m++;
      if(f>0){ ll r=(ll)sqrtl((long double)f); while(r*r>f) r--; while((r+1)*(r+1)<=f) r++; if(r*r==f) nsq++; }
    }
  }
  double sA=sqrt((double)m);
  /* cell populations */
  ll pop[16]={0}; for(ll j=0;j<m;j++) pop[cell[j]]++;
  double ss=0, mx=0, bxmax=0; int done=0;
  for(int i=0;i<np && done<npairs;i++) for(int i2=i+1;i2<np && done<npairs;i2++){
    ll Q=pr[i]*pr[i2]; ll g[16]={0}; ll S=0;
    for(ll j=0;j<m;j++){ int c=leg(Fv[j],Q); S+=c; g[cell[j]]+=c; }
    double a=fabs((double)S)/sA; ss+=a*a; if(a>mx) mx=a; done++;
    for(int c1=0;c1<4;c1++) for(int c2=c1;c2<4;c2++) for(int s1=0;s1<4;s1++) for(int s2=s1;s2<4;s2++){
      ll SS=0, PP=0; for(int x=c1;x<=c2;x++) for(int y=s1;y<=s2;y++){ SS+=g[x*4+y]; PP+=pop[x*4+y]; }
      if(PP>=16){ double r=fabs((double)SS)/sqrt((double)PP); if(r>bxmax) bxmax=r; } }
  }
  /* additive analysis mod q0 */
  int q=(int)q0; ll *N=calloc((size_t)q*q,sizeof(ll)); ll Sq=0;
  for(ll j=0;j<m;j++){ int c=(int)(Cv[j]%q), kk=(int)(Kv[j]%q); N[c*q+kk]++; Sq+=leg(Fv[j],q); }
  double mean=(double)m/((double)q*q), e2=0; for(int i=0;i<q*q;i++){ double d=N[i]-mean; e2+=d*d; }
  double Erms=sqrt(e2/(q*(double)q))/sqrt(mean);
  /* chi(f(c,k)) mod q table */
  int *chi=malloc(sizeof(int)*q*q); ll nq=((n%q)+q)%q;
  for(int c=0;c<q;c++) for(int kk=0;kk<q;kk++){ ll s=((4LL*c*kk-nq)%q+q)%q; ll f=((s*s-4LL*kk)%q+q)%q; chi[c*q+kk]=leg(f,q); }
  double *cs=malloc(sizeof(double)*q), *sn=malloc(sizeof(double)*q); for(int t=0;t<q;t++){ cs[t]=cos(2*M_PI*t/q); sn[t]=sin(2*M_PI*t/q); }
  /* separable DFTs: X(a,kk) = sum_c Y(c,kk) e(ac/q), then over kk */
  double *Tr=malloc(sizeof(double)*q*q), *Ti=malloc(sizeof(double)*q*q), *Gr=malloc(sizeof(double)*q*q), *Gi=malloc(sizeof(double)*q*q);
  double *Xr=malloc(sizeof(double)*q*q), *Xi=malloc(sizeof(double)*q*q), *Yr=malloc(sizeof(double)*q*q), *Yi=malloc(sizeof(double)*q*q);
  for(int pass=0;pass<2;pass++){
    int sgn = pass==0? +1 : -1;  /* T uses e(+), ghat uses e(-) */
    for(int a=0;a<q;a++) for(int kk=0;kk<q;kk++){ double xr=0,xi=0; for(int c=0;c<q;c++){ double v = pass==0? (double)N[c*q+kk] : (double)chi[c*q+kk]; int t=(int)(((ll)a*c)%q); xr+=v*cs[t]; xi+=sgn*v*sn[t]; } Xr[a*q+kk]=xr; Xi[a*q+kk]=xi; }
    for(int a=0;a<q;a++) for(int b=0;b<q;b++){ double yr=0,yi=0; for(int kk=0;kk<q;kk++){ int t=(int)(((ll)b*kk)%q); double c_=cs[t], s_=sgn*sn[t]; yr+=Xr[a*q+kk]*c_-Xi[a*q+kk]*s_; yi+=Xr[a*q+kk]*s_+Xi[a*q+kk]*c_; } Yr[a*q+b]=yr; Yi[a*q+b]=yi; }
    for(int i=0;i<q*q;i++){ if(pass==0){Tr[i]=Yr[i];Ti[i]=Yi[i];} else {Gr[i]=Yr[i]/((double)q*q); Gi[i]=Yi[i]/((double)q*q);} }
  }
  double tmax=0,t2=0,g1=0,addbd=0;
  for(int i=0;i<q*q;i++){ double T=hypot(Tr[i],Ti[i]), G=hypot(Gr[i],Gi[i]); g1+=G; if(i==0){ addbd+=G*T; continue;} if(T>tmax) tmax=T; t2+=T*T; addbd+=G*T; }
  /* consistency: sum ghat*T should equal S_q0 */
  double chk=0; for(int i=0;i<q*q;i++) chk+=Gr[i]*Tr[i]-Gi[i]*Ti[i];
  printf("n=%lld A=%lld sq=%lld cnterr=%.2f | pairs=%d P=%lld SQrms=%.2f SQmax=%.2f boxmax=%.2f | q0=%d Erms=%.2f Tmax=%.2f Trms=%.2f g1=%.2f addbd=%.2f Sq0=%.2f (chk %.1e)\n",
    n,m,nsq,(m-expct)/sA,done,P,sqrt(ss/(done?done:1)),mx,bxmax,q,Erms,tmax/sA,sqrt(t2/(q*(double)q-1))/sA,g1,addbd/sA,fabs((double)Sq)/sA,fabs(chk-(double)Sq));
  return 0;
}
