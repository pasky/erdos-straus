/* O154(b): global (non-local) invariants of primes p (p = 1 mod 4, p < 2^31):
   h(-4p) exactly, via the rapidly convergent series
     h(D) = sum_{n>=1} chi(n) [ erfc(n sqrt(pi/|D|)) + sqrt|D|/(pi n) exp(-pi n^2/|D|) ]   (w = 2, D = -4p)
   with chi = Kronecker (D/.) built multiplicatively from its values at primes (spf sieve);
   checked against brute-force reduced-form counting for p < 20000 (mode "check").
   Also: continued-fraction period length of sqrt(p) and R = log of the unit read off one period.
   stdin: one p per line; stdout: p h(-4p) per R
   Build: gcc -O2 -o /tmp/bs_adv_global scripts/bs_adv_global.c -lm */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
#define NMAX 2000000
static int spf[NMAX+1]; static signed char chi[NMAX+1];
static ll pw(ll a, ll e, ll m){ ll r=1; a%=m; if(a<0) a+=m; while(e){ if(e&1) r=r*a%m; a=a*a%m; e>>=1;} return r; }
static ll gcd3(ll a, ll b, ll c){ ll g=llabs(a), x=llabs(b); while(x){ ll t=g%x; g=x; x=t; } x=llabs(c); while(x){ ll t=g%x; g=x; x=t; } return g; }
static ll hbrute(ll p){ ll D=-4*p,h=0; for(ll b=0;3*b*b<=-D;b+=2){ ll ac=(b*b-D)/4; for(ll a=(b>1?b:1);a*a<=ac;a++){ if(ac%a) continue; ll c=ac/a; if(c<a) continue; if(gcd3(a,b,c)!=1) continue; h+=(b==0||b==a||a==c)?1:2; } } return h; }
static ll hseries(ll p){ double AD=4.0*p; ll n_max=(ll)(6*sqrt(AD))+10; if(n_max>NMAX){ fprintf(stderr,"NMAX\n"); exit(1); }
  chi[1]=1; for(ll n=2;n<=n_max;n++){ ll q=spf[n]; if(q==n){ /* prime */
        if(q==2) chi[n]=0; /* D=-4p even */ else if(q==p) chi[n]=0; else { ll v=pw(-4*p,(q-1)/2,q); chi[n]=(v==1)?1:-1; } }
      else chi[n]=chi[q]*chi[n/q]; }
  double s=0, c=sqrt(M_PI/AD); for(ll n=1;n<=n_max;n++) if(chi[n]) s+=chi[n]*(erfc(n*c)+sqrt(AD)/(M_PI*n)*exp(-M_PI*(double)n*n/AD));
  return llround(s); }
int main(int argc,char**argv){
  for(int i=2;i<=NMAX;i++) if(!spf[i]) for(int j=i;j<=NMAX;j+=i) if(!spf[j]) spf[j]=i;
  if(argc>1 && !strcmp(argv[1],"check")){ int bad=0,n=0; for(ll p=5;p<20000;p+=4){ int pr=1; for(ll d=2;d*d<=p;d++) if(p%d==0){pr=0;break;} if(!pr) continue; n++; if(hbrute(p)!=hseries(p)){ bad++; printf("bad %lld %lld %lld\n",p,hbrute(p),hseries(p)); } } printf("checked %d bad %d\n",n,bad); return 0; }
  ll p; while(scanf("%lld",&p)==1){ ll h=hseries(p);
    ll a0=(ll)sqrtl((long double)p); while(a0*a0>p) a0--; while((a0+1)*(a0+1)<=p) a0++;
    ll m=0,d=1,a=a0,per=0; double R=0; long double sp=sqrtl((long double)p);
    do { m=d*a-m; d=(p-m*m)/d; a=(a0+m)/d; per++; R+=logl((m+sp)/d); } while(d!=1);
    printf("%lld %lld %lld %.6f\n",p,h,per,R); }
  return 0; }
