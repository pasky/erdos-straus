// Existence-only variant of z52b_fingerprint_count.c (same enumeration, early exit at first solution).
// Usage: z52d_p2_TO3_exists m n0 n1 [primeonly]
// Prints for each N in [n0,n1] (primes only if primeonly=1): N exists(1/0) [first x found]
// Solutions of m/N = 1/x+1/y+1/z, x<=y<=z, x in (N/m, 3N/m]  (same convention as the count program).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __int128 i128; typedef unsigned __int128 u128;
static int *spf; static int SPFN;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int np; static u64 pr[64]; static int ex[64];
static void addf(u64 v){ while(v>1){int p=spf[v];int e=0;while(v%p==0){v/=p;e++;}
    int i;for(i=0;i<np;i++)if(pr[i]==(u64)p)break; if(i==np){pr[np]=p;ex[np]=0;np++;} ex[i]+=e;}}
static void subf(u64 v){ while(v>1){int p=spf[v];int e=0;while(v%p==0){v/=p;e++;}
    for(int i=0;i<np;i++)if(pr[i]==(u64)p){ex[i]-=e;break;}}}
static u64 A,B,X,N; static int found; static u64 foundx;
static void rec(int i,u64 d){
  if(found) return;
  if(i==np){ if((d+B)%A==0){u64 y=(d+B)/A; if(y>=X){ i128 e=(i128)B*B/d; u128 zz=(u128)((e+B)/A); (void)zz; found=1; foundx=X; } } return; }
  u64 p=pr[i]; u64 dd=d; for(int e=0;e<=2*ex[i];e++){ if(dd>B)break; rec(i+1,dd); if(found) return; if(dd>B/p+1 && e<2*ex[i]){ if((i128)dd*p>B)break;} dd*=p; }
}
int main(int argc,char**argv){
  u64 m=atoll(argv[1]),n0=atoll(argv[2]),n1=atoll(argv[3]); int primeonly=argc>4?atoi(argv[4]):0;
  SPFN=n1*3+10; spf=calloc(SPFN+1,sizeof(int)); for(int i=2;i<=SPFN;i++)if(!spf[i])for(int j=i;j<=SPFN;j+=i)if(!spf[j])spf[j]=i;
  for(N=n0;N<=n1;N++){
    if(primeonly && spf[N]!=(int)N)continue;
    found=0; foundx=0;
    u64 xlo=N/m+1, xhi=(3*N)/m;
    for(X=xlo;X<=xhi && !found;X++){
      u64 a=m*X-N; if(m*X<=N) continue; u64 b=N*X; if(a==0)continue; u64 g=gcd(a,b); A=a/g; B=b/g;
      np=0; addf(N); addf(X); subf(g);
      int j=0; for(int i=0;i<np;i++) if(ex[i]>0){pr[j]=pr[i];ex[j]=ex[i];j++;} np=j;
      rec(0,1);
    }
    printf("%llu %d %llu\n",N,found,foundx);
    fflush(stdout);
  }
}
