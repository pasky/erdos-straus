// z52c_rh_count.c: copy of z52b_fingerprint_count.c with mode 2 = primes p = 1 (mod 4) only, mode 3 = all 13-rough n = 1 (mod 4)
// (prime or composite; the rough-integer evaluation of the local-density model, RESIDUE_HARDNESS.md §1).
// Count solutions of m/n = 1/x+1/y+1/z, x<=y<=z, for n in [n0,n1] (optionally primes only).
// Output per n: n U D O minz minz_x minz_y maxx minx nx k1 k2 k3 minlcm
// U=#unordered, D=#distinct (x<y<z), O=#ordered, minz=min over sols of z, maxx=max x, minx=min x,
// nx=#distinct x values, kj=#unordered sols with exactly j denominators divisible by n, minlcm=min lcm(x,y,z) (0 if overflow)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __int128 i128;
static int *spf; static int SPFN;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
typedef unsigned __int128 u128;
static u64 mod128(u128 z,u64 m){ return (u64)(z%m); }
static u64 gcdz(u128 z,u64 m){ return gcd(m, mod128(z,m)); }

static int np; static u64 pr[64]; static int ex[64];
static void addf(u64 v){ // factor v (<=SPFN) and add exponents
  while(v>1){int p=spf[v];int e=0;while(v%p==0){v/=p;e++;}
    int i;for(i=0;i<np;i++)if(pr[i]==(u64)p)break; if(i==np){pr[np]=p;ex[np]=0;np++;} ex[i]+=e;}}
static void subf(u64 v){ while(v>1){int p=spf[v];int e=0;while(v%p==0){v/=p;e++;}
    for(int i=0;i<np;i++)if(pr[i]==(u64)p){ex[i]-=e;break;}}}
static u64 A,B,X,N; static long long U,D,O,K[4],nx_cur; static u64 minz,mzx,mzy,maxx,minx; static u64 minlcm; static int gotx;
static void sol(u64 x,u64 y,u128 z){
  U++; if(x<y&&y<z)D++; if(x<y&&y<z)O+=6; else if(x==y&&y==z)O+=1; else O+=3;
  int k=(x%N==0)+(y%N==0)+(mod128(z,N)==0); K[k]++;
  if(z<=(u128)(~0ULL)){ u64 zl=(u64)z;
    if(zl<minz||(zl==minz&&x<mzx)){minz=zl;mzx=x;mzy=y;}
    u64 g=gcd(x,y); u128 l=(u128)(x/g)*y; u64 gg=gcd(zl,(u64)(l%zl)); u128 L2=l/gg*zl;
    if(L2<(u128)(~0ULL) && (u64)L2<minlcm) minlcm=(u64)L2; }
  if(x>maxx)maxx=x; if(x<minx)minx=x; gotx=1;
}
static void rec(int i,u64 d){ // enumerate divisors d of B^2 with d<=B
  if(i==np){ if((d+B)%A==0){u64 y=(d+B)/A; if(y>=X){ i128 e=(i128)B*B/d; u128 zz=(u128)((e+B)/A); sol(X,y,zz);} } return; }
  u64 p=pr[i]; u64 dd=d; for(int e=0;e<=2*ex[i];e++){ if(dd>B)break; rec(i+1,dd); if(dd>B/p+1 && e<2*ex[i]){ if((i128)dd*p>B)break;} dd*=p; }
}
int main(int argc,char**argv){
  u64 m=atoll(argv[1]),n0=atoll(argv[2]),n1=atoll(argv[3]); int primeonly=argc>4?atoi(argv[4]):0;
  SPFN=n1*3+10; spf=calloc(SPFN+1,sizeof(int)); for(int i=2;i<=SPFN;i++)if(!spf[i])for(int j=i;j<=SPFN;j+=i)if(!spf[j])spf[j]=i;
  for(N=n0;N<=n1;N++){
    if(primeonly && primeonly!=3 && spf[N]!=(int)N)continue;
    if(primeonly==2 && (N%4)!=1)continue; /* z52c: p = 1 (mod 4) only */
    if(primeonly==3 && ((N%4)!=1 || N%3==0 || N%5==0 || N%7==0 || N%11==0 || N%13==0))continue; /* z52c: 13-rough n = 1 (mod 4), primes or not */
    U=D=O=0;K[0]=K[1]=K[2]=K[3]=0;minz=~0ULL;mzx=mzy=0;maxx=0;minx=~0ULL;minlcm=~0ULL; long long nx=0;
    u64 xlo=N/m+1, xhi=(3*N)/m; 
    for(X=xlo;X<=xhi;X++){
      u64 a=m*X-N, b=N*X; if(a==0)continue; u64 g=gcd(a,b); A=a/g; B=b/g;
      np=0; addf(N); addf(X); { u64 gg=g; // remove g from N*X factorization
        subf(gg);} 
      // compact
      int j=0; for(int i=0;i<np;i++) if(ex[i]>0){pr[j]=pr[i];ex[j]=ex[i];j++;} np=j;
      // need 1/y+1/z=A/B with y>=X: y<=2B/A
      long long before=U; gotx=0; rec(0,1); if(U>before)nx++;
    }
    printf("%llu %lld %lld %lld %llu %llu %llu %llu %llu %lld %lld %lld %lld %llu\n",N,U,D,O,minz==~0ULL?0:minz,mzx,mzy,maxx,minx==~0ULL?0:minx,nx,K[1],K[2],K[3],minlcm==~0ULL?0:minlcm);
    fflush(stdout);
  }
}
