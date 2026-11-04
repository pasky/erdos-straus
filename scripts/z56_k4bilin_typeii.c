/* z56 K4BILIN: Type II / bilinear falsifier for the dense sequence
     a_n = r(n+4) r(4n+1) 1[n = 97 mod 120]      (and the S-version b_n = 1_S(n+4) 1_S(4n+1) 1[n = 97 mod 120])
   Computes, for n <= X:
     totals  A = sum a_n, sum mu(n) a_n, sum lambda(n) a_n, sum_{p prime} a_p, sum_{n = odd square} a_n;
     the Friedlander-Iwaniec asymptotic-sieve bilinear quantity (B) with gamma = 1:
        B(N) = sum_m | sum_{N < n <= 2N, mn <= X} mu(mn) w_{mn} |    for w = a, w = b, and the parity control
        w = a*(1+lambda)  (Selberg-type: same Type I behaviour, no primes; (B) must fail for it),
     normalised by A(w) = sum_{n<=X} w_n;  also the "trivial" bound T(N) = sum_m sum_n |mu(mn) w_{mn}| / A(w).
   Exact integer arithmetic for a_n (r values from complete factorisation by a segmented sieve).
   Usage: ./typeii X  > out.txt
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

static int *primes; static int np;
static void mkprimes(int L){ char *s=calloc(L+1,1); primes=malloc(sizeof(int)*(L/2+10)); np=0;
  for(int i=2;i<=L;i++){ if(!s[i]){primes[np++]=i; for(long j=(long)i*i;j<=L;j+=i) s[j]=1;} } free(s);}
static long inv_mod(long a,long m){ long g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; long b=a1; /* ext gcd */
  long old_r=b, r=m, old_s=1, s=0; while(r){ long q=old_r/r, t; t=old_r-q*r; old_r=r; r=t; t=old_s-q*s; old_s=s; s=t;} (void)g;(void)x;(void)x1;
  long v=old_s%m; if(v<0)v+=m; return v; }

int main(int argc,char**argv){
  long X = argc>1? atol(argv[1]) : 10000000L; long n0 = argc>2? atol(argv[2]) : 97;
  long LIM = (long)sqrt(4.0*X+1)+2; mkprimes((int)LIM);
  int32_t *a = calloc(X+1,sizeof(int32_t));   /* a_n */
  int8_t *mu = calloc(X+1,1), *lam = calloc(X+1,1), *bS = calloc(X+1,1), *isp = calloc(X+1,1);
  const long BL = 1<<20;
  uint64_t *rn = malloc(BL*8), *r1 = malloc(BL*8), *r2 = malloc(BL*8);
  int32_t *f1 = malloc(BL*4), *f2 = malloc(BL*4); int8_t *mb = malloc(BL), *lb = malloc(BL), *s1 = malloc(BL), *s2 = malloc(BL), *om = malloc(BL), *w1 = malloc(BL), *w2 = malloc(BL);
  int8_t *wex = calloc(X+1,1); /* omega(N1)+omega(N2) when both in S */
  for(long lo=1; lo<=X; lo+=BL){
    long hi = lo+BL-1; if(hi>X) hi=X; long len=hi-lo+1;
    for(long i=0;i<len;i++){ long n=lo+i; rn[i]=n; r1[i]=n+4; r2[i]=4*n+1; f1[i]=4; f2[i]=4; mb[i]=1; lb[i]=1; s1[i]=1; s2[i]=1; om[i]=0; w1[i]=0; w2[i]=0; }
    for(int k=0;k<np;k++){ long l=primes[k];
      /* n itself */
      if(l*l<=hi || l<=hi){ long st = ((lo + l - 1)/l)*l; for(long n=st;n<=hi;n+=l){ long i=n-lo; int e=0; while(rn[i]%l==0){rn[i]/=l;e++;} if(e>1) mb[i]=0; else mb[i]=-mb[i]; if(e&1) lb[i]=-lb[i]; om[i]+=e; } }
      if(l==2) continue; /* N1, N2 odd */
      /* N1 = n+4 : n = -4 mod l */
      { long c = ((-4)%l + l)%l; long st = lo + ((c - lo%l)%l + l)%l; for(long n=st;n<=hi;n+=l){ long i=n-lo; int e=0; while(r1[i]%l==0){r1[i]/=l;e++;}
          if((l&3)==1){ f1[i]*= (e+1); w1[i]++; } else { if(e&1) f1[i]=0; s1[i]=0; } } }
      /* N2 = 4n+1 : n = -inv(4) mod l */
      { long c = (l - inv_mod(4,l))%l; long st = lo + ((c - lo%l)%l + l)%l; for(long n=st;n<=hi;n+=l){ long i=n-lo; int e=0; while(r2[i]%l==0){r2[i]/=l;e++;}
          if((l&3)==1){ f2[i]*= (e+1); w2[i]++; } else { if(e&1) f2[i]=0; s2[i]=0; } } }
    }
    for(long i=0;i<len;i++){ long n=lo+i;
      if(rn[i]>1){ mb[i]=-mb[i]; lb[i]=-lb[i]; om[i]++; }
      if(r1[i]>1){ if((r1[i]&3)==1){ f1[i]*=2; w1[i]++; } else { f1[i]=0; s1[i]=0; } }
      if(r2[i]>1){ if((r2[i]&3)==1){ f2[i]*=2; w2[i]++; } else { f2[i]=0; s2[i]=0; } }
      mu[n]=mb[i]; lam[n]=lb[i]; isp[n]=(om[i]==1);
      if(n%120==n0){ a[n]=f1[i]*f2[i]; bS[n]=s1[i]&s2[i]; wex[n]=w1[i]+w2[i]; }
    }
  }
  /* totals */
  double A=0, Amu=0, Alam=0, Ap=0, Asq=0, B=0, Bp=0, Bmu=0, Aplog=0; long cntpos=0;
  for(long n=1;n<=X;n++) if(a[n]){ A+=a[n]; Amu+=mu[n]*a[n]; Alam+=lam[n]*a[n]; if(isp[n]){ Ap+=a[n]; Aplog+=a[n]*log((double)n);} cntpos++; if(bS[n]){B+=1; Bmu+=mu[n]; if(isp[n]) Bp+=1;} }
  for(long m=1;m*m<=X;m+=2){ long n=m*m; if(n%120==n0) Asq+=a[n]; }
  printf("# X=%ld\n# sum a_n=%.0f  #{a_n>0}=%ld  sum mu a=%.0f (ratio %.3e)  sum lambda a=%.0f (ratio %.3e)\n",X,A,cntpos,Amu,Amu/A,Alam,Alam/A);
  printf("# sum_{p prime} a_p=%.0f (ratio to A: %.4e; A/log X ratio %.4f)  odd-square part sum a_{m^2}=%.0f (ratio %.3e)\n",Ap,Ap/A,Ap/(A/log((double)X)),Asq,Asq/A);
  { double H=1; for(int k=0;k<np;k++){ long l=primes[k]; if(l<7) { if(n0%l) H*=1.0/(1.0-1.0/l); continue; } double g = (l%4==1)? (double)(l-1)/(l*(double)(l+1)) : (double)(l+1)/(l*(double)(l-1)); H*=(1-g)/(1-1.0/l);} printf("# asymptotic-sieve prediction: sum_p a_p log p = H*A with H=%.5f (primes<=%ld); observed ratio %.4f\n",H,LIM,Aplog/(H*A)); }
  { double As=0, Asmu=0, Asplog=0, Hs=1; for(long n=1;n<=X;n++) if(bS[n]){ double v=16.0*(double)(1L<<wex[n]); As+=v; Asmu+=mu[n]*v; if(isp[n]) Asplog+=v*log((double)n);} for(int k=0;k<np;k++){ long l=primes[k]; if(l<7){ if(n0%l) Hs*=1.0/(1.0-1.0/l); continue;} double g=1.0/(l+((l%4==1)?2.0:-2.0)); Hs*=(1-g)/(1-1.0/l);} printf("# a*-version (r*(N1)r*(N2)=16*2^(w1+w2) on S-pairs): A*=%.0f  sum mu a*/A*=%.3e  sum_p a*_p log p/(H* A*)=%.4f (H*=%.5f)\n",As,Asmu/As,Asplog/(Hs*As),Hs); }
  printf("# S-version: #{b_n=1}=%.0f  sum mu b=%.0f (ratio %.3e)  #{p: b_p=1}=%.0f\n",B,Bmu,Bmu/B,Bp);
  /* (B) quantities */
  double Ac = 0; for(long n=1;n<=X;n++) if(a[n]) Ac += (double)a[n]*(1+lam[n]);
  printf("# B(N) = sum_m |sum_{N<n<=2N, mn<=X} mu(mn) w_mn| / sum_n w_n ;  T(N) = same with |.| inside\n");
  double Ast=0; for(long n=1;n<=X;n++) if(bS[n]) Ast += 16.0*(double)(1L<<wex[n]);
  printf("# logN/logX      N   B_a        T_a       R_a(random-sign ref)  B_b        T_b       B_ctrl     T_ctrl     B_a*       T_a*\n");
  for(int it=0; it<=6; it++){ double t = 0.20 + 0.05*it;
    long N = (it==6)? (long)floor(sqrt((double)X)) : (long)pow((double)X,t);
    double Ba=0,Ta=0,Bb=0,Tb=0,Bc=0,Tc=0,Ra=0,Bs=0,Ts=0;
    for(long m=1; m*(N+1)<=X; m++){
      if(m%2==0||m%3==0||m%5==0) continue;
      long n2 = 2*N; if(m*n2>X) n2 = X/m;
      double sa=0,sb=0,sc=0,qa=0,ss=0;
      for(long n=N+1;n<=n2;n++){ long k=m*n; if(!a[k]) continue; int mm=mu[k]; if(!mm) continue;
        sa += mm*(double)a[k]; Ta += a[k]; qa += (double)a[k]*a[k]; if(bS[k]){ sb+=mm; Tb+=1; double v=16.0*(double)(1L<<wex[k]); ss+=mm*v; Ts+=v; } double c=(double)a[k]*(1+lam[k]); sc += mm*c; Tc += c; }
      Ba+=fabs(sa); Bb+=fabs(sb); Bc+=fabs(sc); Bs+=fabs(ss); Ra += sqrt(2.0/M_PI*qa);
    }
    printf("%6.2f %10ld  %.3e  %.3e  %.3e  %.3e  %.3e  %.3e  %.3e  %.3e  %.3e\n", t, N, Ba/A, Ta/A, Ra/A, Bb/B, Tb/B, Bc/Ac, Tc/Ac, Bs/Ast, Ts/Ast);
  }
  return 0;
}
