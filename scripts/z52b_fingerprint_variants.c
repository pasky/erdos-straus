// VARIANT counter (generated from z52b_fingerprint_count.c): per n print n U V0..V15 (see sol()).
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
static void sol(u64 x,u64 y,u64 z){
  U++;
  int ev=(x%2==0)+(y%2==0)+(z%2==0);
  V[ev]++;                                   // V0..V3: number of even denominators
  if(gcd(gcd(x,y),z)==1) V[4]++;             // primitive
  if(z%x==0 && z%y==0) V[5]++;               // x,y | z
  if(y%x==0) V[6]++;                         // x | y
  if(x==y||y==z) V[7]++;                     // isosceles
  if(issqf(x)&&issqf(y)&&issqf(z)) V[8]++;   // all squarefree
  if((double)z <= (double)N*(double)N) V[9]++;  // height z <= n^2
  if((double)z <= 1.0*N*sqrt((double)N)) V[10]++; // z <= n^1.5
  if(ispow2(x)||ispow2(y)||ispow2(z)) V[11]++; // some denominator a power of 2
  if(isprm(x)||isprm(y)) V[12]++;            // smallest or middle denominator prime
  if(gcd(x,y)==1||gcd(y,z)==1||gcd(x,z)==1) V[13]++; // some coprime pair
  if((x%3!=0)&&(y%3!=0)&&(z%3!=0)) V[14]++;  // no denominator divisible by 3
  if(x%4==0||y%4==0||z%4==0) V[15]++;        // some denominator divisible by 4
}
static void rec(int i,u64 d){ // enumerate divisors d of B^2 with d<=B
  if(i==np){ if((d+B)%A==0){u64 y=(d+B)/A; if(y>=X){ i128 e=(i128)B*B/d; u64 z=(u64)((e+B)/A); sol(X,y,z);} } return; }
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
