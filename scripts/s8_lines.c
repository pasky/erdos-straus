// s8_lines.c — O258: line events of ES Type II at a single n (window form) and per-j b=1 events.
// Type II: c n + a + b = 4abcd (x=abd, y=acdn, z=bcdn). Window m = 4abd - n = (a+b)/c, K = (n+m)/4.
// Events (complete for m <= (n+4)/3):
//   II : exists coprime a,b, ab | K, m | a+b           (full Type II)
//   B1 : exists A | K, A == -1 (mod m)                  (b = 1 line)
//   B1s: exists prime s | K, s == -1 (mod m)            (support-1 prime lottery, z24)
//   C1 : exists coprime a,b, ab | K, a + b = m          (c = 1 line)
//   D1 : exists d: n+4d has a divisor == -1 (mod 4d)    (dual form of B1; complete for d <= (n+3)/8)
//   D1p: same with a prime divisor
// Per-j: F_j : exists A | jn+1 with w=(jn+1)/A >= 3, w == -1 (mod 4j);  Fp_j: A prime.
// usage: s8_lines census P   | s8_lines list n1 n2 ... | s8_lines perj P J
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll;
static int *spf; static ll LIM;
static void sieve(ll L){ LIM=L; spf=calloc(L+1,sizeof(int)); for(ll i=2;i<=L;i++) if(!spf[i]){ for(ll j=i;j<=L;j+=i) if(!spf[j]) spf[j]=i; } }
static int fac(ll n, ll *pr, int *ex){ int k=0; ll t=n;
  if(t>LIM){ for(ll q=2;q*q<=t;q++) if(t%q==0){pr[k]=q;ex[k]=0;while(t%q==0){t/=q;ex[k]++;}k++;} if(t>1){pr[k]=t;ex[k]=1;k++;} return k; }
  while(t>1){ ll q=spf[t]; pr[k]=q; ex[k]=0; while(t%q==0){t/=q;ex[k]++;} k++; } return k; }
static int gendiv(ll *pr,int *ex,int k, ll *dv){ int nd=1; dv[0]=1; for(int i=0;i<k;i++){ int cur=nd; ll pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) dv[nd++]=dv[j]*pp; } } return nd; }
static ll gcdl(ll a, ll b){ while(b){ ll t=a%b; a=b; b=t;} return a; }
static ll pr[64]; static int ex[64]; static ll dv[200000];
// window events at (n,m): bitmask 1=II 2=B1 4=B1s 8=C1
static int wev(ll n, ll m){ ll K=(n+m)/4; int k=fac(K,pr,ex); int r=0;
  for(int i=0;i<k;i++) if((pr[i]+1)%m==0) r|=4;
  int nd=gendiv(pr,ex,k,dv);
  for(int i=0;i<nd;i++){ ll a=dv[i]; if((a+1)%m==0) r|=2|1; }
  for(int i=0;i<nd && !((r&1)&&(r&8));i++){ ll a=dv[i]; ll Ka=K/a; for(int j=0;j<nd;j++){ ll b=dv[j]; if(b<a) continue; if(Ka%b) continue; if(gcdl(a,b)!=1) continue; if((a+b)%m==0){ r|=1; if(a+b==m) r|=8; } } }
  return r; }
static int dev(ll n, ll d){ ll N=n+4*d; int k=fac(N,pr,ex); int r=0; for(int i=0;i<k;i++) if((pr[i]+1)%(4*d)==0) r|=2;
  int nd=gendiv(pr,ex,k,dv); for(int i=0;i<nd;i++) if(dv[i]<N && (dv[i]+1)%(4*d)==0) r|=1; return r; }
static int isprime(ll n){ if(n<2) return 0; if(n<=LIM) return spf[n]==n; for(ll q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
// first-success window for each event (0 = never)
static void first(ll n, ll res[6]){ for(int e=0;e<6;e++) res[e]=0; ll mmax=(n+4)/3;
  for(ll m=3;m<=mmax;m+=4){ if((n+m)%4) continue; int r=wev(n,m); for(int e=0;e<4;e++) if(!res[e] && (r>>e&1)) res[e]=m; if(res[0]&&res[1]&&res[2]&&res[3]) break; }
  ll dmax=(n+3)/8; for(ll d=1;d<=dmax;d++){ int r=dev(n,d); if(!res[4]&&(r&1)) res[4]=d; if(!res[5]&&(r&2)) res[5]=d; if(res[4]&&res[5]) break; } }
static void firstB(ll n, ll res[4]){ for(int e=0;e<4;e++) res[e]=0; ll mmax=(n+4)/3;
  for(ll m=3;m<=mmax;m+=4){ if((n+m)%4) continue; int r=wev(n,m); for(int e=0;e<4;e++) if(!res[e] && (r>>e&1)) res[e]=m; if(res[1]&&res[3]) break; } }
static const char *nm[6]={"II","B1","B1s","C1","D1","D1p"};
int main(int argc,char**argv){
  if(!strcmp(argv[1],"census")){ ll P=atoll(argv[2]); sieve(2*P+10); ll cnt=0, fail[6]={0}, mx[6]={0}, mxn[6]={0}; ll mism=0;
    for(ll p=5;p<=P;p+=4){ if(spf[p]!=p) continue; cnt++; ll r[6]; first(p,r);
      if((r[1]!=0)!=(r[4]!=0)) { mism++; printf("MISMATCH B1/D1 p=%lld\n",p);} 
      for(int e=0;e<6;e++){ if(!r[e]){ fail[e]++; if(fail[e]<=40) printf("fail %s p=%lld\n",nm[e],p);} else if(r[e]>mx[e]){mx[e]=r[e];mxn[e]=p;} } }
    printf("primes p=1(4) <= %lld: %lld; B1/D1 existence mismatches: %lld\n",P,cnt,mism);
    for(int e=0;e<6;e++) printf("%-4s fails=%lld  max first=%lld at p=%lld\n",nm[e],fail[e],mx[e],mxn[e]);
  } else if(!strcmp(argv[1],"census2")){ ll P0=atoll(argv[2]), P=atoll(argv[3]); sieve(2*P+10); ll cnt=0;
    for(ll p=P0+((5-P0%4+4)%4);p<=P;p+=4){ if(spf[p]!=p) continue; cnt++; ll r[4]; firstB(p,r);
      if(!r[1]) printf("fail B1 p=%lld\n",p); if(!r[3]) printf("fail C1 p=%lld\n",p); }
    printf("primes p=1(4) in [%lld,%lld]: %lld\n",P0,P,cnt);
  } else if(!strcmp(argv[1],"count840")){ ll P0=atoll(argv[2]), P=atoll(argv[3]); sieve(2*P+10);
    int cls[6]={1,121,169,289,361,529}; double sb[6]={0}, sc[6]={0}; ll nn[6]={0};
    for(ll p=P0+((5-P0%4+4)%4);p<=P;p+=4){ if(spf[p]!=p) continue; int ci=-1; for(int i=0;i<6;i++) if(p%840==cls[i]) ci=i; if(ci<0) continue;
      ll b1=0,c1=0, mmax=(p+4)/3; for(ll m=3;m<=mmax;m+=4){ ll K=(p+m)/4; int k=fac(K,pr,ex); int nd=gendiv(pr,ex,k,dv);
        for(int i=0;i<nd;i++){ ll a=dv[i]; if((a+1)%m==0) b1++; if(a<m){ ll b=m-a; if(b>a && K%(a*b)==0 && gcdl(a,b)==1) c1+=2; else if(b==a && a==1 && K%1==0) c1++; } } }
      nn[ci]++; sb[ci]+=b1; sc[ci]+=c1; }
    for(int i=0;i<6;i++) printf("p=%3d mod 840: n=%lld  mean b1-line count=%.2f  mean c1-line count=%.2f\n",cls[i],nn[i],sb[i]/nn[i],sc[i]/nn[i]);
  } else if(!strcmp(argv[1],"list")){ ll mxn=0; for(int i=2;i<argc;i++){ ll v=atoll(argv[i]); if(v>mxn) mxn=v;} sieve(2*mxn+10);
    for(int i=2;i<argc;i++){ ll n=atoll(argv[i]); ll r[6]; first(n,r); printf("n=%lld",n); for(int e=0;e<6;e++) printf(" %s=%lld",nm[e],r[e]); printf("\n"); }
  } else if(!strcmp(argv[1],"perj")){ ll P=atoll(argv[2]); int J=atoi(argv[3]); sieve((ll)J*P+2);
    static ll f1[65], fp1[65], f2[65][65], cnt=0, allf=0, allfp=0; double lp=0, lpp=0;
    for(ll p=5;p<=P;p+=4){ if(spf[p]!=p) continue; cnt++; int F[65], Fp[65]; int all=1, allp=1;
      for(int j=1;j<=J;j++){ ll N=(ll)j*p+1; int k=fac(N,pr,ex); int nd=gendiv(pr,ex,k,dv); F[j]=0; Fp[j]=0;
        for(int i=0;i<nd;i++){ ll A=dv[i], w=N/A; if(w>=3 && (w+1)%(4*j)==0){ F[j]=1; if(isprime(A)) Fp[j]=1; } }
        if(!F[j]) f1[j]++; else all=0; if(!Fp[j]) fp1[j]++; else allp=0; }
      for(int j=1;j<=J;j++) for(int l=j+1;l<=J;l++) if(!F[j]&&!F[l]) f2[j][l]++;
      allf+=all; allfp+=allp; }
    printf("primes p=1(4) <= %lld: %lld\n j  fail(F_j)  fail(Fp_j)\n",P,cnt);
    for(int j=1;j<=J;j++){ printf("%2d  %.4f  %.4f\n",j,(double)f1[j]/cnt,(double)fp1[j]/cnt); lp+=log((double)f1[j]/cnt); lpp+=log((double)fp1[j]/cnt); }
    double mr=0; int np=0; double mxr=0; int mj=0,ml=0; for(int j=1;j<=J;j++) for(int l=j+1;l<=J;l++){ double e=(double)f1[j]*f1[l]/cnt/cnt; double o=(double)f2[j][l]/cnt; if(e>0){ double r=o/e; mr+=r; np++; if(r>mxr){mxr=r;mj=j;ml=l;} } }
    printf("pairwise joint-fail / product: mean %.3f, max %.3f at (%d,%d)\n",mr/np,mxr,mj,ml);
    printf("all j<=J fail: F %lld (indep. pred %.3g), Fp %lld (indep. pred %.3g)\n",allf,cnt*exp(lp),allfp,cnt*exp(lpp));
  }
  return 0; }
