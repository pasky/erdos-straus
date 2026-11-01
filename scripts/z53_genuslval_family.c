// z53_genuslval_family.c — lane GENUSLVAL (Z53_GENUSLVAL.md), falsifier F1 for Theorem U.
// For a prime p (or odd n) and integer windows U0<u<=U1 (u squarefree, u = 1 mod 4) and Y<w<=X
// (w odd squarefree, gcd(w,u p)=1), compute per u:
//   F_u  = sum_w 2 * 2^{omega(u)+omega(w)} / (phi(u) phi(w)) * [pair (u,2w) genus-matched]   (both orders (u,2w),(2w,u))
//   S1_u = sum_w 2^{omega(w)} [all l|w: (-u n/l)=1] / phi(w)                                (eta = 1 sum)
// and checks Lemma 1: direct square-class test == conditions (i)-(iii); counts mismatches (must be 0).
// Optionally (flag M) computes Mgen(n) over the whole pair set P(n) and checks family pairs lie in P(n).
// Usage: ./family n U0 U1 Y X [M]      output: lines "u F_u S1_u nw", then "TOTAL ..." line.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int *spf, *phi; static long NS;
static int jacobi(long a, long n){ a%=n; if(a<0)a+=n; int r=1;
  while(a){ while(!(a&1)){ a>>=1; long m=n&7; if(m==3||m==5) r=-r; }
    long t=a; a=n; n=t; if((a&3)==3 && (n&3)==3) r=-r; a%=n; }
  return n==1 ? r : 0; }
static long gcdl(long a,long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
static int sqfree_odd(long m, int *om){ if(!(m&1)) return 0; int w=0; while(m>1){ long l=spf[m]; m/=l; if(m%l==0) return 0; w++; } *om=w; return 1; }
// direct genus test: n*a square unit mod q=4uB (a=-(u+B)); returns omega(odd part of uB) or -1
static int genus_ok(long n, long u, long B){ long a=-(u+B);
  if(gcdl(n,4*u*B)!=1) return -1;
  if(((n-a)%8+8)%8) return -1; int w=0; long ms[2]={u,B};
  for(int i=0;i<2;i++){ long m=ms[i]; while(!(m&1)) m>>=1;
    while(m>1){ long l=spf[m]; while(m%l==0) m/=l; w++;
      if(jacobi(((n%l)*(((a%l)+l)%l))%l,l)!=1) return -1; } }
  return w; }
int main(int argc,char**argv){
  if(argc<6){ fprintf(stderr,"usage\n"); return 1; }
  long n=atol(argv[1]),U0=atol(argv[2]),U1=atol(argv[3]),Y=atol(argv[4]),X=atol(argv[5]); int doM=argc>6;
  NS = X; if(U1>NS) NS=U1; if(doM && n/3+3>NS) NS=n/3+3; NS+=2;
  spf=malloc(sizeof(int)*(NS+1)); phi=malloc(sizeof(int)*(NS+1));
  for(long i=0;i<=NS;i++){ spf[i]=0; phi[i]=i; }
  for(long i=2;i<=NS;i++) if(!spf[i]) for(long j=i;j<=NS;j+=i){ if(!spf[j]) spf[j]=i; phi[j]-=phi[j]/i; }
  long mism=0, outside=0; long double Ftot=0;
  for(long u=U0+1;u<=U1;u++){ int ou; if(u%4!=1 || !sqfree_odd(u,&ou) || n%u==0 && u>1) continue;
    long double F=0,S1=0; long nw=0;
    for(long w=Y+1; w<=X; w+=1){ int ow; if(!sqfree_odd(w,&ow)) continue; if(gcdl(w,u)!=1 || w%n==0) continue;
      if(n%w==0 && w>1) continue;
      // condition (i): all l|w split in Q(sqrt(-u n)), i.e. (-u n / l) = 1
      int c1=1; { long m=w; while(m>1){ long l=spf[m]; m/=l; if(jacobi(-(u%l)*(n%l),l)!=1){ c1=0; break; } } }
      if(c1) S1 += (long double)(1L<<ow)/phi[w];
      int c2=1; { long m=u; while(m>1){ long l=spf[m]; m/=l; if(jacobi(w,l)!=jacobi(-2*(n%l),l)){ c2=0; break; } } }
      long w0 = ((-(n+u)/2)%4+4)%4; int c3 = (w%4)==w0;
      int lem = c1&&c2&&c3;
      int g = genus_ok(n,u,2*w); int dir = g>=0;
      if(lem!=dir) mism++;
      if(doM && 8*u*w-u-2*w>n) outside++;
      if(dir){ F += 2.0L*(long double)(1L<<(ou+ow))/((long double)phi[u]*phi[w]); nw++; }
    }
    Ftot+=F;
    printf("%ld %.12Lf %.12Lf %ld\n",u,F,S1,nw);
  }
  long double Mg=0;
  if(doM){ for(long u=1;3*u-1<=n;u++) for(long B=1;4*u*B-u-B<=n;B++){ if(((u+B)&1)==0||gcdl(u,B)!=1) continue;
      int g=genus_ok(n,u,B); if(g>=0) Mg+=(long double)(4L<<g)/(4.0L*phi[u]*phi[B]); } }
  printf("TOTAL n=%ld F=%.12Lf Mgen=%.12Lf mismatches=%ld outside=%ld\n",n,Ftot,doM?Mg:(long double)NAN,mism,outside);
  return 0; }
