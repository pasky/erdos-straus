// z59 MSPF: R(n), Rodd(C odd), Reven(C even), dmin for a single n (trial-division factoring of n+k, k<=sqrt(n/2)).
// Usage: ./single n1 n2 ...
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static void factor(long long m,long long*pr,int*ex,int*np){ *np=0; for(long long p=2;p*p<=m;p+= (p==2?1:2)){ if(m%p==0){int e=0;while(m%p==0){m/=p;e++;} pr[*np]=p;ex[*np]=e;(*np)++;} } if(m>1){pr[*np]=m;ex[*np]=1;(*np)++;} }
int main(int argc,char**argv){
  for(int a=1;a<argc;a++){ long long n=atoll(argv[a]);
    long long R=0,Rodd=0,Reven=0,dmin=0,kmin=0; long long kmax=(long long)sqrt((double)n/2)+1;
    for(long long k=1;k<=kmax;k++){ long long pr[64];int ex[64],np; factor(n+k,pr,ex,&np);
      long long divs[8192];int nd=1;divs[0]=1;
      for(int i=0;i<np;i++){int cur=nd;long long pp=1;for(int e=1;e<=ex[i];e++){pp*=pr[i];for(int j=0;j<cur;j++)divs[nd++]=divs[j]*pp;}}
      for(int i=0;i<nd;i++){long long d=divs[i]; if((d+1)%(4*k)==0){ long long B=(n+k)/d,C=(d+1)/(4*k); int mult=(B>kmax)?2:1;
        R+=mult; if(C%2)Rodd+=mult; else Reven+=mult; if(dmin==0||d<dmin){dmin=d;kmin=k;} if(B>kmax){long long d2=(n+B)/k; if(d2<dmin){dmin=d2;kmin=B;}} }}
    }
    printf("%lld R=%lld Rodd=%lld Reven=%lld dmin=%lld kmin=%lld\n",n,R,Rodd,Reven,dmin,kmin); fflush(stdout);
  }
}
