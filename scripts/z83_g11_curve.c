/* Integer outward bounds for the asymmetric Buchstab tree, with optional
   per-colour caps above BV. Reads scaled z82 beta tables from stdin. */
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <stdint.h>
#define S 100000000LL
#define N 1000
#define T 25000
typedef long long ll; typedef __int128 Z;
static ll hf[T+1],hF[T+1],lf[T+1],lF[T+1],h2[T+1],h4[T+1];
static ll cd(Z n,Z d){assert(d>0&&n>=0);return (n+d-1)/d;}
static ll mx(ll a,ll b){return a>b?a:b;}static ll mn(ll a,ll b){return a<b?a:b;}
static ll rt(ll n,ll d){Z a=(Z)n*S*S/d;ll v=(ll)sqrtl((long double)a);while((Z)v*v>a)--v;while((Z)(v+1)*(v+1)<=a)++v;return v;}
static int ix(ll n,ll d){assert(n>=0&&d>0);return mn(T,n*N/d);}
static ll hi(ll n,ll d){int k=ix(n,d);return k?hF[k]:cd((Z)151000000*S,rt(n,d));}
int main(int ac,char **av){if(ac!=7)return 1;
 int G=atoi(av[1]),J=atoi(av[2]),B=atoi(av[3]),C3=atoi(av[4]),C7=atoi(av[5]),jmin=atoi(av[6]);
 assert(B>1&&J>0&&J<=G&&G<=12000&&T*B>=G*N&&C3<=J&&C7<=J);
 for(int k=1;k<=T;k++)assert(scanf("%lld%lld%lld%lld%lld%lld",hf+k,hF+k,lf+k,lF+k,h2+k,h4+k)==6);
 ll Au,Eu;assert(scanf("%lld%lld",&Au,&Eu)==2);assert(Au<151000000);
 int I=G/2,sz=I+1,JB=G/2-1;
 ll *L=calloc((J+1)*(size_t)sz,sizeof(ll)),*U=calloc((J+1)*(size_t)sz,sizeof(ll)),*root=calloc(sz,sizeof(ll));assert(L&&U&&root);
 for(int i=B;i<=I;i++)root[i]=rt(B,i);
 // With no shape cap, one run gives a curve in j. If capped, j is a
 // residual level at total charged pin cost J-j: output only the top row.
 int rect=(C3<J||C7<J);
 for(int j=1;j<=J;j++){
 ll best=-100*S;int ib=0;ll bestL=0,bestC=0,bestH=0;
 int bv=JB-(J-j),d3cap=C3-(J-j),joint=rect?mx(bv,mn(d3cap,C7)):j;joint=mn(joint,j);
 int k=ix(mx(0,joint),B);ll l=k?lf[k]:0,u=k?lF[k]:1000000*S;
 for(int i=B;i<=I;i++){
 if(i>B){ll den=2LL*(i-1);int c=j-i;
 // log(1+1/(i-1))/2 between x/2 - x^2/4 and x/2.
 l=c>0&&U[c*sz+i-1]<1000000*S?mx(0,L[j*sz+i-1]-cd(U[c*sz+i-1],den)):0;
 u=U[j*sz+i-1];if(c>0&&u<1000000*S)u-=(Z)L[c*sz+i]*(den-1)/(den*den);}
 for(int n=0;n<=15;n++){int cand[]={0,5,7,9,10,11,12,13,14,15,17,20,4,6,8,16};
 ll d7=n? (ll)cand[n]*B:5LL*j/2,d3=5LL*j-d7;int lim=rect?2:1;
 for(int ph=0;ph<lim;ph++){ll x=d3,y=d7;if(rect){if(ph){x=mn(x,5LL*bv-y);}else{x=mn(x,5LL*d3cap);y=mn(y,5LL*C7);}}if(x<=0||y<=0)continue;
 ll FL=hi(x,5*i),FR=hi(y,5*B);ll prod=cd((Z)FL*FR,S); ll ml=(Z)hf[ix(x,5*i)]*FR/S+(Z)hf[ix(y,5*B)]*FL/S-prod;
 l=mx(l,(Z)root[i]*mx(0,ml)/S);u=mn(u,cd((Z)(root[i]+1)*prod,S));}}
 L[j*sz+i]=l;U[j*sz+i]=u;
 if(j>=jmin&&(!rect||j==J)&&i>G/4&&i<I&&i>=B&&JB> B){
 ll lower=(Z)rt(i,B)*l/S;
 // Pan tau'= .49999 throughout ; always slack for fixed 840.
 int t=49999;ll c3=cd((Z)Au*(rt(i,G)+1)*2*h2[cd(G*N,i)]*100000*G,(Z)S*S*(t*G-100000*B));
 ll c7=cd((Z)3*Eu*200000*(rt(200000LL*i*B,(ll)t*G*G)+1)*h4[cd(G*N,B)],(Z)2*t*S*S);
 if(lower-c3-c7>best)best=lower-c3-c7,ib=i,bestL=lower,bestC=c3,bestH=c7;
 }}
 if(j>=jmin&&(!rect||j==J))printf("%d %d %d %d %d %d %lld %lld %lld %lld\n",G,j,ib,B,rect?C3:j,rect?C7:j,bestL,bestC,bestH,best);
 }
}
