// z53_genuslval_decomp.c — lane GENUSLVAL (Z53_GENUSLVAL.md §4): exact genus-character decomposition of the
// u = 1 (mod 4), u squarefree part of M_gen at a prime p = 1 (mod 4).
// For each such u (all u with X_u >= 1) the slice S_u = (1/(2 phi(u))) sum_{eta=(./d)chi4^j} eps_eta Sig_eta(X_u)
// (Lemma 2.3 / Prop C, exact).  Accumulates over u:
//   P    : eta = 1                      (principal genus: class-number term L(1,chi_{-4up}) log X_u)
//   C4   : d = 1, j = 1                 (chi_{-4} twist)
//   CBM  : d = u > 1, j = 1             (eta chi_D = chi_p: BM-like)
//   CU0  : d = u > 1, j = 0
//   CMIX : 1 < d < u
// and also SL = sum over u <= 50 of the same split (small-u slices) for reference.
// Usage: ./decomp p1 p2 ...   output one line per p: p P C4 CBM CU0 CMIX total
#include <stdio.h>
#include <stdlib.h>
static int *spf; static long NS;
static int jacobi(long a, long n){ a%=n; if(a<0)a+=n; int r=1;
  while(a){ while(!(a&1)){ a>>=1; long m=n&7; if(m==3||m==5) r=-r; }
    long t=a; a=n; n=t; if((a&3)==3 && (n&3)==3) r=-r; a%=n; }
  return n==1 ? r : 0; }
static long gcdl(long a,long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
int main(int argc,char**argv){
  long pmax=0; for(int i=1;i<argc;i++){ long p=atol(argv[i]); if(p>pmax) pmax=p; }
  NS=pmax/6+10; spf=calloc(NS+1,sizeof(int));
  for(long i=2;i<=NS;i++) if(!spf[i]) for(long j=i;j<=NS;j+=i) if(!spf[j]) spf[j]=i;
  printf("p\tP\tC4\tCBM\tCU0\tCMIX\ttotal\n");
  for(int ai=1;ai<argc;ai++){ long p=atol(argv[ai]);
    long double P=0,C4=0,CBM=0,CU0=0,CMIX=0;
    for(long u=1;;u+=4){ long X=(p+u)/(2*(4*u-1)); if(X<1) break;
      // squarefree check & primes of u
      long pr[16]; int np=0; long m=u; int sf=1; while(m>1){ long l=spf[m]; m/=l; if(m%l==0){sf=0;break;} pr[np++]=l; }
      if(!sf || u%p==0) continue;
      long phiu=1; for(int i=0;i<np;i++) phiu*=pr[i]-1;
      int nd=1<<np; long w0=((-(p+u)/2)%4+4)%4; int c4w0=(w0==1)?1:-1;
      int epsd[1<<10]; for(int s=0;s<nd;s++){ int e=1; for(int i=0;i<np;i++) if(s>>i&1) e*=jacobi(-2*(p%pr[i]),pr[i]); epsd[s]=e; }
      long double Sig[2<<10]={0};
      for(long w=1;w<=X;w+=2){ if(gcdl(w,u)!=1) continue;
        long mm=w, ph=w; int om=0, split=1;
        while(mm>1){ long l=spf[mm]; om++; ph=ph/l*(l-1); while(mm%l==0) mm/=l; if(jacobi(-(u%l)*(p%l),l)!=1){ split=0; break; } }
        if(!split) continue;
        long double g=(long double)(1L<<om)/ph; int c4=(w%4==1)?1:-1;
        int jl[16]; for(int i=0;i<np;i++) jl[i]=jacobi(w,pr[i]);
        for(int s=0;s<nd;s++){ int jd=1; for(int i=0;i<np;i++) if(s>>i&1) jd*=jl[i]; Sig[2*s]+=g*jd; Sig[2*s+1]+=g*jd*c4; }
      }
      long double nrm=1.0L/(2.0L*phiu);
      for(int s=0;s<nd;s++) for(int j=0;j<2;j++){ long double v=nrm*epsd[s]*(j?c4w0:1)*Sig[2*s+j];
          if(s==0&&j==0) P+=v; else if(s==0) C4+=v; else if(s==nd-1&&j==1) CBM+=v; else if(s==nd-1) CU0+=v; else CMIX+=v; }
    }
    printf("%ld\t%.6Lf\t%.6Lf\t%.6Lf\t%.6Lf\t%.6Lf\t%.6Lf\n",p,P,C4,CBM,CU0,CMIX,P+C4+CBM+CU0+CMIX); fflush(stdout);
  }
  return 0; }
