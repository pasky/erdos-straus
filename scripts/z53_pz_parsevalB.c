// z53_pz_parsevalB.c — the Parseval upper bound of Lemma 4.2,
//   B(Q) := sum_{1<D<=Q} phi(D) * sum_{r mod D} (A_r - mean_r A)^2,  A_r = sum_{P: D | m_P, res_P ≡ r (D)} 1/m_P,
// for the trial family (fam=1: P=(u,C), m=4uC-1, res=-u) or the Type II family (fam=2: P=(a,c,d), gcd(a,c)=1,
// m=4acd-1, res=-a c^{-1}).  V <= B.  Streams (D, r, w) triples, sorts, accumulates.  usage: parsevalB Q fam
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
typedef struct { ll D, r; double w; } T;
static ll gcdl(ll a,ll b){while(b){ll t=a%b;a=b;b=t;}return a;}
static ll inv(ll a,ll m){ ll r0=m,r1=a%m,s0=0,s1=1,q,t; while(r1){q=r0/r1;t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;} s0%=m; if(s0<0)s0+=m; return s0; }
static int cmp(const void*x,const void*y){const T*a=x,*b=y; if(a->D!=b->D) return a->D<b->D?-1:1; if(a->r!=b->r) return a->r<b->r?-1:1; return 0;}
ll *ph; ll *spf;
T *arr; ll na=0, cap=1<<22;
static void push(ll D,ll r,double w){ if(na==cap){cap*=2;arr=realloc(arr,cap*sizeof(T));} arr[na].D=D;arr[na].r=r;arr[na].w=w;na++; }
static void adddivs(ll m, ll res, double w){ // all divisors D>1 of m
  ll ps[32],es[32],k=0,x=m; while(x>1){ll p=spf[x],e=0; while(x%p==0){x/=p;e++;} ps[k]=p;es[k]=e;k++;}
  ll divs[4096]; ll nd=1; divs[0]=1; for(ll i=0;i<k;i++){ ll cur=nd, pw=1; for(ll e=1;e<=es[i];e++){ pw*=ps[i]; for(ll j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
  for(ll j=0;j<nd;j++) if(divs[j]>1) push(divs[j], res%divs[j], w); }
int main(int argc,char**argv){ ll Q=atoll(argv[1]); int fam=atoi(argv[2]);
  ph=malloc((Q+2)*8); spf=calloc(Q+2,8); for(ll i=0;i<=Q+1;i++) ph[i]=i;
  for(ll i=2;i<=Q+1;i++) if(spf[i]==0) for(ll j=i;j<=Q+1;j+=i){ if(!spf[j]) spf[j]=i; ph[j]-=ph[j]/i; }
  arr=malloc(cap*sizeof(T)); double M=0;
  if(fam==1){ for(ll u=1;4*u-1<=Q;u++) for(ll C=1;4*u*C-1<=Q;C++){ ll m=4*u*C-1; double w=1.0/m; M+=w; adddivs(m,(m-u%m)%m,w);} }
  else { for(ll a=1;4*a-1<=Q;a++) for(ll c=1;4*a*c-1<=Q;c++){ if(gcdl(a,c)!=1) continue; for(ll d=1;4*a*c*d-1<=Q;d++){ ll m=4*a*c*d-1; double w=1.0/m; M+=w;
        ll r=(m-(a%m)*inv(c%m,m)%m)%m; adddivs(m,r,w);} } }
  qsort(arr,na,sizeof(T),cmp);
  double B=0; ll i=0; while(i<na){ ll D=arr[i].D; double s=0,s2=0; while(i<na&&arr[i].D==D){ ll r=arr[i].r; double A=0; while(i<na&&arr[i].D==D&&arr[i].r==r){A+=arr[i].w;i++;} s+=A; s2+=A*A; }
    B+= (double)ph[D]*s2 - s*s; }
  double L=log((double)Q);
  printf("Q=%lld fam=%d M=%.5f B=%.5f B/M^2=%.5f B/logQ^3=%.5f B/logQ^4=%.5f B/logQ^5=%.6f\n",Q,fam,M,B,B/(M*M),B/pow(L,3),B/pow(L,4),B/pow(L,5));
  return 0; }
