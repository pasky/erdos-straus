// R267 from-scratch f_k(p) = #{x<=y<=z : k/p = 1/x+1/y+1/z}, primes p in [N0,N1); prints mean f/log^3 p, min f,
// and the same restricted to Mordell classes p mod 840 in {1,121,169,289,361,529}.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static int *spf; static u64 A_,B_,X_; static u64 pr[64]; static int ex[64],nf; static long cnt;
static u64 g(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static void rec(int i,u128 u){ if(u>B_) return; if(i==nf){ if((u+B_)%A_==0 && (u+B_)/A_>=X_) cnt++; return; }
  u128 v=u; for(int e=0;e<=2*ex[i];e++){ if(v>B_) break; rec(i+1,v); v*=pr[i]; } }
static void fac(u64 n,u64 p){ nf=0; if(n%p==0){int e=0; while(n%p==0){n/=p;e++;} pr[nf]=p;ex[nf]=e;nf++;} while(n>1){ u64 q=spf[n]; int e=0; while(n%q==0){n/=q;e++;} pr[nf]=q;ex[nf]=e;nf++; } }
int main(int c,char**v){ u64 k=atoll(v[1]),N0=atoll(v[2]),N1=atoll(v[3]); long S=3*N1+10; spf=calloc(S,sizeof(int));
  for(long i=2;i<S;i++) if(!spf[i]) for(long j=i;j<S;j+=i) if(!spf[j]) spf[j]=i;
  double sm=0,smM=0; long n=0,nM=0,mn=1<<30,mnM=1<<30; int M[6]={1,121,169,289,361,529};
  for(u64 p=N0;p<N1;p++){ if(spf[p]!=(int)p||k%p==0) continue; cnt=0;
    for(u64 x=p/k+1;x*k<=3*p;x++){ u64 A=k*x-p,B=p*x,d=g(A,B); A/=d;B/=d; A_=A;B_=B;X_=x; fac(B,p); rec(0,1); }
    double L=log((double)p); sm+=cnt/(L*L*L); n++; if(cnt<mn) mn=cnt;
    int isM=0; for(int i=0;i<6;i++) if(p%840==(u64)M[i]) isM=1;
    if(isM){ smM+=cnt/(L*L*L); nM++; if(cnt<mnM) mnM=cnt; } }
  printf("k=%llu [%llu,%llu): primes=%ld mean f/log3=%.4f min=%ld | Mordell: n=%ld mean=%.4f min=%ld\n",k,N0,N1,n,sm/n,mn,nM,nM?smM/nM:0,mnM);
}
