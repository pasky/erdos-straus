// Z1013 helper: print ALL unordered ES solutions x<=y<=z of 4/n = 1/x+1/y+1/z for prime n (m=4), one line per solution:
// n x y z.  Same enumeration as scripts/z52b_fingerprint_count.c (divisors of B^2, x in (n/4, 3n/4]).
// Usage: ./z52d_p2_NC0_Z1013 nmax   (primes n = 1 mod 4 up to nmax)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __int128 i128;
static int *spf;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int np; static u64 pr[64]; static int ex[64];
static void addf(u64 v){ while(v>1){int p=spf[v];int e=0;while(v%p==0){v/=p;e++;}
  int i;for(i=0;i<np;i++)if(pr[i]==(u64)p)break; if(i==np){pr[np]=p;ex[np]=0;np++;} ex[i]+=e;}}
static void subf(u64 v){ while(v>1){int p=spf[v];int e=0;while(v%p==0){v/=p;e++;}
  for(int i=0;i<np;i++)if(pr[i]==(u64)p){ex[i]-=e;break;}}}
static u64 A,B,X,N;
static void sol(u64 x,u64 y,u64 z){ u64 t; if(y>z){t=y;y=z;z=t;} if(x>y){t=x;x=y;y=t;} if(y>z){t=y;y=z;z=t;}
  printf("%llu %llu %llu %llu\n",N,x,y,z); }
static void rec(int i,u64 d){
  if(i==np){ if((d+B)%A==0){u64 y=(d+B)/A; if(y>=X){ i128 e=(i128)B*B/d; u64 zz=(u64)((e+B)/A); sol(X,y,zz);} } return; }
  u64 p=pr[i]; u64 dd=d; for(int e=0;e<=2*ex[i];e++){ if(dd>B)break; rec(i+1,dd); if(dd>B/p+1 && e<2*ex[i]){ if((i128)dd*p>B)break;} dd*=p; }
}
int main(int argc,char**argv){
  u64 nmax=atoll(argv[1]); u64 m=4;
  spf=calloc(3*nmax+10,sizeof(int)); for(u64 i=2;i<=3*nmax+9;i++) if(!spf[i]) for(u64 j=i;j<=3*nmax+9;j+=i) if(!spf[j]) spf[j]=i;
  for(N=5;N<=nmax;N+=4){ if(spf[N]!=(int)N) continue;
    u64 xlo=N/m+1, xhi=(3*N)/m;
    for(X=xlo;X<=xhi;X++){
      u64 a=m*X-N, b=N*X; if(a==0)continue; u64 g=gcd(a,b); A=a/g; B=b/g;
      np=0; addf(N); addf(X); subf(g);
      int j=0; for(int i=0;i<np;i++) if(ex[i]>0){pr[j]=pr[i];ex[j]=ex[i];j++;} np=j;
      rec(0,1);
    }
  }
  return 0;
}
