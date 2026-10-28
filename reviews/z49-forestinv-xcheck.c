// Independent z49 cross-review census: factor n+u with SPF, then test uv | n+u+v.
// Unlike the submitted census, this fixes n and enumerates unordered endpoint pairs.
// Memory O(N); usage: xcheck N, 9 <= N <= 2000000. Output matches nonsquare failures.
#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
static long gcd(long a,long b){while(b){long r=a%b;a=b;b=r;}return a;}
static int jac(long a,long n){int s=1;a%=n;while(a){while(!(a&1)){a/=2;if(n%8==3||n%8==5)s=-s;}long z=a;a=n;n=z;if(a%4==3&&n%4==3)s=-s;a%=n;}return n==1?s:0;}
static int good(long u){return u%4==0||u%8==7;}
int main(int argc,char **argv){
  assert(argc==2);long N=atol(argv[1]);assert(N>=9&&N<=2000000);
  long L=N+(long)sqrt(N+1)+3;int *spf=calloc(L+1,sizeof(*spf));assert(spf);
  for(long i=2;i<=L;i++)if(!spf[i])for(long j=i;j<=L;j+=i)if(!spf[j])spf[j]=(int)i;
  long counts[3]={0},ucfail[3]={0},ufail[3]={0},maxp=0,argp=0,words=0,witnesses=0;
  long classcounts[8]={0},classfails[8]={0};
  for(long n=9;n<=N;n+=8){
    long root=(long)sqrt(n);while((root+1)*(root+1)<=n)root++;
    int cl=root*root==n?2:(spf[n]==n?0:1),bits=0;long least=0;
    for(long u=1;(u-1)*(u-1)<=n+1;u++){
      long divs[4096],nd=1,m=n+u;divs[0]=1;
      while(m>1){long p=spf[m],power=1,old=nd;do{m/=p;power*=p;for(long i=0;i<old;i++){assert(nd<4096);divs[nd++]=divs[i]*power;}}while(m%p==0);}
      for(long i=0;i<nd;i++){
        long v=divs[i];if(v<u||(n+u+v)%(u*v))continue;
        long t=(n+u+v)/(u*v),g=gcd(u,v);words++;
        assert(t>=1&&t*u*v-u-v==n&&gcd(u,n)==g&&gcd(v,n)==g);
        assert(n%g==0&&gcd(u/g,v/g)==1&&(g*t)*(u/g)*(v/g)-u/g-v/g==n/g);
        if(!(good(u)||good(v)))continue;
        witnesses++;assert(root*root!=n);
        long e=good(u)?u:v,A=t*e-1,odd=A;while(!(odd&1))odd/=2;
        assert(A>2&&gcd(A,n)==1&&jac(A,n)==-1&&odd>1&&jac(n,odd)==-1);
        bits|=g==1?1:2;if(g==1&&(!least||e<least))least=e;
      }
    }
    counts[cl]++;ucfail[cl]+=!(bits&1);ufail[cl]+=!bits;
    if(cl==1){int b=(n%3==0)+2*(n%5==0)+4*(n%7==0);classcounts[b]++;classfails[b]+=!(bits&1);}
    if(cl!=2&&!(bits&1))printf("%ld %c %d 4294967295\n",n,"PC"[cl],bits);
    if(cl==0&&least>maxp){maxp=least;argp=n;}
  }
  for(int i=0;i<3;i++)fprintf(stderr,"%c count=%ld U_cop_fail=%ld U_fail=%ld\n","PCS"[i],counts[i],ucfail[i],ufail[i]);
  for(int i=0;i<8;i++)fprintf(stderr,"class_bits=%d count=%ld U_cop_fail=%ld\n",i,classcounts[i],classfails[i]);
  fprintf(stderr,"unordered_words=%ld U_words=%ld max_prime_least_line=%ld at %ld\n",words,witnesses,maxp,argp);
  free(spf);return 0;
}
