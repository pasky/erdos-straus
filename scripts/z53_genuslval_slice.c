// z53_genuslval_slice.c — lane GENUSLVAL (Z53_GENUSLVAL.md §3, Proposition C numerics).
// For odd n = 1 mod 4 and squarefree u = 1 mod 4 (gcd(u,n)=1), the u-slice of M_gen:
//   S_u(n) = sum over B = 2w (w odd, gcd(w,u)=1, (u,B) in P(n)) of the genus weight of the pair (u,B)
// computed directly (square-class test), and the eta-components
//   Sig[d,j] = sum_{w <= X} g(w) eta(w)/w,  g(w) = 2^{omega(w)} [all l|w: (-u n/l) = 1] / phi(w) * w,
//   eta = (./d) chi_{-4}^j, d | u, j in {0,1};  X = floor((n+u)/(2(4u-1))).
// Lemma: S_u = (1/phi(u)) * sum_{d,j} eps_{d,j} Sig[d,j], eps = (-2n/d) * chi_{-4}(w0)^j, w0 = -(n+u)/2 mod 4.
// Output: "S_u <direct> <via-eta>" and one line per (d,j): "d j eps Sig".
// Usage: ./slice n u
#include <stdio.h>
#include <stdlib.h>
static int *spf; 
static int jacobi(long a, long n){ a%=n; if(a<0)a+=n; int r=1;
  while(a){ while(!(a&1)){ a>>=1; long m=n&7; if(m==3||m==5) r=-r; }
    long t=a; a=n; n=t; if((a&3)==3 && (n&3)==3) r=-r; a%=n; }
  return n==1 ? r : 0; }
static long gcdl(long a,long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
int main(int argc,char**argv){
  long n=atol(argv[1]), u=atol(argv[2]);
  long X=(n+u)/(2*(4*u-1));
  spf=calloc(X+2,sizeof(int));
  for(long i=2;i<=X;i++) if(!spf[i]) for(long j=i;j<=X;j+=i) if(!spf[j]) spf[j]=i;
  // divisors of u
  long pr[20]; int np=0; { long m=u; for(long l=3;l*l<=m;l+=2) if(m%l==0){ pr[np++]=l; m/=l; } if(m>1) pr[np++]=m; }
  int nd=1<<np; long dv[1<<12]; for(int s=0;s<nd;s++){ long d=1; for(int i=0;i<np;i++) if(s>>i&1) d*=pr[i]; dv[s]=d; }
  long double *Sig=calloc(2*nd,sizeof(long double)); long double direct=0;
  long w0=((-(n+u)/2)%4+4)%4; int c4w0 = (w0==1)?1:-1;
  long phiu=u; for(int i=0;i<np;i++) phiu=phiu/pr[i]*(pr[i]-1);
  for(long w=1; w<=X; w+=2){ if(gcdl(w,u)!=1) continue;
    // omega, phi, split test
    long m=w, ph=w; int om=0, split=1;
    while(m>1){ long l=spf[m]; om++; ph=ph/l*(l-1); while(m%l==0) m/=l; if(jacobi(-(u%l)*(n%l),l)!=1) split=0; }
    if(!split) continue;
    long double g=(long double)(1L<<om)/ph;  // = g(w)/w
    int c4=(w%4==1)?1:-1;
    for(int s=0;s<nd;s++){ int jd=jacobi(w,dv[s]); Sig[2*s]+=g*jd; Sig[2*s+1]+=g*jd*c4; }
    // direct genus test for pair (u,2w): conditions (ii),(iii) (condition (i) = split)
    int ok = (w%4==w0); for(int i=0;i<np && ok;i++) if(jacobi(w,pr[i])!=jacobi(-2*(n%pr[i]),pr[i])) ok=0;
    if(ok && gcdl(w,n)==1) direct += (long double)(1L<<np)*g/phiu;
  }
  long double via=0;
  for(int s=0;s<nd;s++) for(int j=0;j<2;j++){ long d=dv[s]; int e=1; for(int i=0;i<np;i++) if(d%pr[i]==0) e*=jacobi(-2*(n%pr[i]),pr[i]);
      if(j) e*=c4w0; via += e*Sig[2*s+j]/(2.0L*(1<<np)) * (long double)(1L<<np) / phiu * 2 / 2; }
  // NB: S_u = sum_w weight * [genus], weight = 2^{omega(u)+omega(w)}/(phi(u) phi(w)) for the single ordered pair (u,2w);
  // projector = 2^{-omega(u)-1} sum eps*eta; so S_u = (1/(2 phi(u))) sum eps Sig.  (via computed accordingly)
  printf("X %ld\nS_u %.12Lf %.12Lf\n",X,direct,via);
  for(int s=0;s<nd;s++) for(int j=0;j<2;j++){ long d=dv[s]; int e=1; for(int i=0;i<np;i++) if(d%pr[i]==0) e*=jacobi(-2*(n%pr[i]),pr[i]);
      if(j) e*=c4w0; printf("%ld %d %d %.12Lf\n",d,j,e,Sig[2*s+j]); }
  return 0; }
