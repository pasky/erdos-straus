// z52d audit A2 Z3155: Sun-style VARIANT-3 counter (copy of z52b_fingerprint_variants2.c, new predicates) (generated from z52b_fingerprint_count.c): per n print n U V0..V15 (see sol()).
// Count solutions of m/n = 1/x+1/y+1/z, x<=y<=z, for n in [n0,n1] (optionally primes only).
// Output per n: n U D O minz minz_x minz_y maxx minx nx k1 k2 k3 minlcm
// U=#unordered, D=#distinct (x<y<z), O=#ordered, minz=min over sols of z, maxx=max x, minx=min x,
// nx=#distinct x values, kj=#unordered sols with exactly j denominators divisible by n, minlcm=min lcm(x,y,z) (0 if overflow)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
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
static long long V[16];
static int issqf(u64 v){ for(u64 p=2;p*p<=v;p++){ if(v%(p*p)==0) return 0; if(v%p==0) v/=p; } return 1; }
static int ispow2(u64 v){ return v && !(v&(v-1)); }
static int isprm(u64 v){ if(v<2) return 0; for(u64 p=2;p*p<=v;p++) if(v%p==0) return 0; return 1; }
static int issq128(u128 v){ long double r=sqrtl((long double)v); u128 t=(u128)r; while(t*t>v) t--; while((t+1)*(t+1)<=v) t++; return t*t==v; }
static int isprm128(u128 v){ if(v<=(u128)(~0ULL)) return isprm((u64)v); return 0; }
static void sol(u64 x,u64 y,u128 z){
  U++;
  if(issq128((u128)x+y)) V[0]++;                       // x+y square
  if(issq128((u128)x+y+z)) V[1]++;                     // x+y+z square
  if(issq128((u128)(y-x))) V[2]++;                     // y-x square (incl 0)
  if(isprm((u64)(x+y))) V[3]++;                        // x+y prime
  if(issq128(z-y)) V[4]++;                             // z-y square (incl 0)
  if(issq128((u128)8*x+1)) V[5]++;                     // x triangular
  if(mod128((u128)x+y+z,N)==0) V[6]++;                 // n | x+y+z
  if(issq128(z+x)) V[7]++;                             // x+z square
  if(x==(N+3)/4) V[8]++;                               // x = ceil(n/4) (greedy first term)
  if(issqf(x)&&issqf(y)) V[9]++;                       // x,y squarefree
  if(x%2==1) V[10]++;                                  // smallest denominator odd
  if(x%4==1) V[11]++;                                  // x = 1 mod 4
  if(x%3==1) V[12]++;                                  // x = 1 mod 3
  if(isprm128(z/ (u128)1) ) V[13]++;                   // z prime (only z<2^64)
  if(isprm(y)) V[14]++;                                // y prime
  if((u128)y*y >= z*(u128)x && 1) V[15]++;             // y >= sqrt(xz) (y geometric-mean-or-above)
}
static void rec(int i,u64 d){ // enumerate divisors d of B^2 with d<=B
  if(i==np){ if((d+B)%A==0){u64 y=(d+B)/A; if(y>=X){ i128 e=(i128)B*B/d; u128 zz=(u128)((e+B)/A); sol(X,y,zz);} } return; }
  u64 p=pr[i]; u64 dd=d; for(int e=0;e<=2*ex[i];e++){ if(dd>B)break; rec(i+1,dd); if(dd>B/p+1 && e<2*ex[i]){ if((i128)dd*p>B)break;} dd*=p; }
}
int main(int argc,char**argv){
  u64 m=atoll(argv[1]),n0=atoll(argv[2]),n1=atoll(argv[3]); int primeonly=argc>4?atoi(argv[4]):0;
  SPFN=n1*3+10; spf=calloc(SPFN+1,sizeof(int)); for(int i=2;i<=SPFN;i++)if(!spf[i])for(int j=i;j<=SPFN;j+=i)if(!spf[j])spf[j]=i;
  for(N=n0;N<=n1;N++){
    if(primeonly && spf[N]!=(int)N)continue;
    U=D=O=0; for(int i=0;i<16;i++)V[i]=0;K[0]=K[1]=K[2]=K[3]=0;minz=~0ULL;mzx=mzy=0;maxx=0;minx=~0ULL;minlcm=~0ULL; long long nx=0;
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
    printf("%llu %lld",N,U); for(int i=0;i<16;i++) printf(" %lld",V[i]); printf("\n");
    fflush(stdout);
  }
}
