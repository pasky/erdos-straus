// z52d Pass 2, batch NC0 — existence / avoidance search for m/N = 1/x+1/y+1/z (x<=y<=z).
// Usage: z52d_p2_NC0_exist m lo hi mode q [primeonly]
//   mode 0: stop at first solution (any)           -> prints N and "F" (fail = no solution) or "S x y z"
//   mode 1: need a solution with q ∤ xyz            -> prints N and status
//   mode 2: need a solution with q | none... (same as 1, kept for clarity)
//   mode 3: count all unordered solutions with q ∤ xyz (full enumeration; prints count)
// Output lines: "N status [x y z] xiters"   status: S=found, F=none
// Factorisation: B = N*X/g and A = (mX-N)/g; primes of B come only from N and X (g | N*X),
// so no global sieve beyond N and X is needed.  Memory: spf up to 3*hi/m + 10.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef __int128 i128; typedef unsigned __int128 u128;

static int *spf; static u64 SPFN;
static u64 gcd(u64 a, u64 b){ while(b){ u64 t=a%b; a=b; b=t; } return a; }

#define MAXP 64
static int np; static u64 pr[MAXP]; static int ex[MAXP];
static u64 A,B,X,Nn,Q; static int mode; static int found; static u64 sx,sy; static u128 sz; static long long cnt;

static void addp(u64 p,int e){ for(int i=0;i<np;i++) if(pr[i]==p){ ex[i]+=e; return; } pr[np]=p; ex[np]=e; np++; }
static void factor_into(u64 v,int sign){ // add sign*factorisation(v) using spf (v <= SPFN)
  while(v>1){ u64 p=spf[v]; int e=0; while(v%p==0){ v/=p; e++; } addp(p,sign*e); } }

static void pr128(u128 v){ char buf[64]; int k=0; if(!v){ printf("0"); return;} while(v){ buf[k++]=(char)('0'+(int)(v%10)); v/=10; } while(k) putchar(buf[--k]); }
static int ok_pred(u64 x,u64 y,u128 z){
  if(mode==0) return 1;
  if(x%Q==0||y%Q==0||(u64)(z%Q)==0) return 0;
  return 1;
}

static void rec(int i,u64 d){
  if(found && mode!=3) return;
  if(i==np){
    if((d+B)%A==0){ u64 y=(d+B)/A;
      if(y>=X){ i128 e=(i128)B*B/d; u128 zz=(u128)((e+B)/A);
        // y<=z by construction (d<=B)
        if(ok_pred(X,y,zz)){ cnt++; if(!found){ found=1; sx=X; sy=y; sz=zz; } } } }
    return; }
  u64 p=pr[i]; u64 dd=d;
  for(int e=0;e<=2*ex[i];e++){
    if(dd>B) break;
    rec(i+1,dd);
    if(found && mode!=3) return;
    if(e<2*ex[i]){ if((u128)dd*p>B) break; dd*=p; }
  }
}

int main(int argc,char**argv){
  if(argc<6){ fprintf(stderr,"usage\n"); return 1; }
  u64 m=strtoull(argv[1],0,10), lo=strtoull(argv[2],0,10), hi=strtoull(argv[3],0,10);
  mode=atoi(argv[4]); Q=strtoull(argv[5],0,10); int primeonly = argc>6? atoi(argv[6]):0;
  SPFN = 3*hi/m + 10; if(SPFN<hi) SPFN=hi;
  spf=calloc(SPFN+1,sizeof(int));
  for(u64 i=2;i<=SPFN;i++) if(!spf[i]) for(u64 j=i;j<=SPFN;j+=i) if(!spf[j]) spf[j]=(int)i;
  for(Nn=lo; Nn<=hi; Nn++){
    if(primeonly && (Nn<2 || spf[Nn]!=(int)Nn)) continue;
    found=0; cnt=0; sx=sy=0; sz=0; long long xit=0;
    u64 xlo=Nn/m+1, xhi=(3*Nn)/m;
    for(X=xlo; X<=xhi && (!found || mode==3); X++){
      if(m*X<=Nn) continue;
      u64 a=m*X-Nn, b=Nn*X; u64 g=gcd(a,b); A=a/g; B=b/g;
      xit++;
      np=0; factor_into(Nn,1); factor_into(X,1);
      // subtract factorisation of g (g | N*X, so its primes are among those of N and X)
      { u64 gg=g; for(int i=0;i<np;i++){ u64 p=pr[i]; while(gg%p==0){ gg/=p; ex[i]--; } } }
      // (exponents may be zero; rec handles e=0)
      rec(0,1);
    }
    if(mode==3) printf("%llu %lld %lld\n",Nn,cnt,xit);
    else if(found){ printf("%llu S %llu %llu ",Nn,sx,sy); pr128(sz); printf(" %lld\n",xit); }
    else printf("%llu F 0 0 0 %lld\n",Nn,xit);
    fflush(stdout);
  }
  return 0;
}
