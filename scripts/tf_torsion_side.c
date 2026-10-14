/* TORSION_FIRING Prop 1.2(b), torsion side, independent of the box code (O207).
   For odd n (primes <= NMAX; odd squares as T1 control) find the least prime h = 3 mod 4, h <= HMAX, h∤n, such that
   some d >= 1 and some x with x | (h+1)/2, 2d | x, satisfy x^2 + n d = 0 mod h, i.e. (x,0) is a 2-torsion point of
   y^2 = x^3 + nd x over F_h with 2x | #E(F_h) = h+1.  Then verify the resulting Type II solution exactly:
   c = x/(2d), e = (n + 4c^2 d)/h, X = (n+e)/4, Y = n c d j, Z = n X j / c with j = (h+1)/(4cd); check 4XYZ = n(XY+YZ+ZX).
   Usage: tf_torsion_side NMAX HMAX */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef __int128 i128;
int main(int argc,char**argv){
  long NMAX=atol(argv[1]), HMAX=atol(argv[2]);
  char *comp=calloc(HMAX+NMAX+2,1); long L=HMAX>NMAX?HMAX:NMAX;
  for(long i=2;i*i<=L;i++) if(!comp[i]) for(long j=i*i;j<=L;j+=i) comp[j]=1;
  long *hs=malloc(sizeof(long)*L), nh=0; for(long h=7;h<=HMAX;h+=4) if(!comp[h]) hs[nh++]=h;
  /* precompute even divisors of (h+1)/2 per h */
  long np=0,found=0,bad=0,maxh=0,nsq=0,sqfound=0; long worst_n=0;
  static long dv[4096];
  for(long n=5;n<=NMAX;n+=2){
    long r=(long)llround(sqrt((double)n)); int issq=(r*r==n), isp=!comp[n];
    if(!isp && !issq) continue;
    int ok=0; long H=0;
    for(long t=0;t<nh && !ok;t++){
      long h=hs[t]; if(n%h==0) continue; long m=(h+1)/2; int c=0;
      for(long x=2;x*x<=m;x++) if(m%x==0){ dv[c++]=x; if(x*x!=m) dv[c++]=m/x; } dv[c++]=m;
      for(int i=0;i<c && !ok;i++){ long x=dv[i]; if(x%2) continue; long half=x/2;
        for(long d=1; d<=half && !ok; d++){ if(half%d) continue;
          if(((i128)x*x + (i128)n*d) % h == 0){
            long cc=x/(2*d), j=(h+1)/(4*cc*d); i128 N=(i128)n+(i128)4*cc*cc*d;
            if(N%h){ bad++; continue; } i128 e=N/h; if(((i128)n+e)%4){ bad++; continue; }
            i128 X=((i128)n+e)/4, Y=(i128)n*cc*d*j, Zn=(i128)n*X*j; if(Zn%cc){ bad++; continue; } i128 Z=Zn/cc;
            if(4*X*Y*Z != (i128)n*(X*Y+Y*Z+Z*X)){ bad++; continue; }
            ok=1; H=h; }
        }
      }
    }
    if(isp && !ok) printf("unfired prime %ld\n",n);
    if(isp){ np++; if(ok){ found++; if(H>maxh){maxh=H; worst_n=n;} } }
    else { nsq++; if(ok) sqfound++; }
  }
  printf("NMAX=%ld HMAX=%ld primes=%ld fired(torsion criterion, verified)=%ld verify_failures=%ld max least h=%ld (at n=%ld); odd squares=%ld fired=%ld\n",
         NMAX,HMAX,np,found,bad,maxh,worst_n,nsq,sqfound);
  return 0;
}
