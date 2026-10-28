// z49 ltfable2: the (★)-line genus decomposition at single primes (LOWERTAIL_DEEP_ASTRA (1)).
// For p = 1 (mod 4) prime, over ordered pairs (u,B), gcd(u,B)=1, u+B odd, 4uB-u-B <= p, q = 4uB, a = -(u+B):
//   R      = #{p = a (mod q)}                         (the (★) count, ordered)
//   M0     = Σ 1/φ(q)
//   M_BM   = Σ (1 - χ_{-4uB}(p))/φ(q),  χ_{-4uB}(p) = (uB/p) for p = 1 (4)
//   M_gen  = Σ (s(q)/φ(q)) · 1[p a^{-1} ∈ (Z/q)^{×2}]    (all real characters)
//   G      = #{genus-admissible pairs} (unweighted)
// Genus test: p = a (mod 4) if uB odd, p = a (mod 8) if uB even; and for each odd prime ℓ | uB, (p/ℓ) = (a/ℓ),
// where (p/ℓ) = (ℓ/p) (reciprocity, p = 1 (4)) is read from a quadratic-residue table mod p and (a/ℓ) is a Jacobi
// symbol of -B (ℓ | u) or -u (ℓ | B).  s(q) = 2^{ω(odd part)} × (2 if uB odd, 4 if uB even).
// usage: mgen N [list of extra primes]   -> stdout lines "p R M0 MBM Mgen G"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint32_t *spf; static long LIM;
static void sieve(long N){ spf=calloc(N+1,sizeof(uint32_t)); if(!spf){fprintf(stderr,"oom\n");exit(1);}
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
  LIM=N; }
static int jacobi(long a,long n){ // n odd positive
  a%=n; if(a<0) a+=n; int r=1;
  while(a){ while((a&1)==0){ a>>=1; long m=n&7; if(m==3||m==5) r=-r; }
    long t=a; a=n; n=t; if((a&3)==3 && (n&3)==3) r=-r; a%=n; }
  return n==1? r : 0; }
static long gcdl(long a,long b){ while(b){ long t=a%b; a=b; b=t; } return a; }
static long phi_from(long n){ long r=n; long m=n; while(m>1){ long p=spf[m]; r=r/p*(p-1); while(m%p==0) m/=p; } return r; }

int main(int argc,char**argv){
  long N=atol(argv[1]); long extra[64]; int nx=0; long maxp=N;
  for(int i=2;i<argc;i++){ extra[nx++]=atol(argv[i]); if(extra[nx-1]>maxp) maxp=extra[nx-1]; }
  sieve(2*maxp+100); // q = 4uB <= p+u+B+... < 2p
  unsigned char *qr=malloc(maxp+1);
  printf("# p R M0 MBM Mgen G  (R = ordered (star)-count; M0 = Σ1/φ; MBM = BM main term; Mgen = genus main term; G = #genus-admissible pairs)\n");
  for(long p=5;;p+=4){
    long pp;
    if(p<=N){ if(spf[p]!=(uint32_t)p) continue; pp=p; }
    else { if(nx==0) break; pp=extra[--nx]; if(pp<=N) continue; }
    // QR table mod pp
    memset(qr,0,pp+1); for(long x=1;x<pp;x++){ qr[(x*x)%pp]=1; }
    long R=0; double M0=0,MBM=0,Mgen=0; long G=0;
    for(long u=1; 4*u-u-1<=pp; u++){
      for(long B=1; ; B++){ long n0=4*u*B-u-B; if(n0>pp) break;
        if(((u+B)&1)==0) continue; if(gcdl(u,B)!=1) continue;
        long q=4*u*B; long a=-(u+B); long am=((a%q)+q)%q;
        long ph=phi_from(q);
        if(pp%q==am) R++;
        M0+=1.0/ph;
        // chi_{-4uB}(p) = (uB/p) Legendre: multiplicative over prime factors of uB
        long ub=u*B; int chi=1; { long m=ub; while(m>1){ long l=spf[m]; int e=0; while(m%l==0){m/=l;e++;} if(e&1){ if(l==2){ chi*= ((pp&7)==1||(pp&7)==7)?1:-1; } else chi*= qr[l%pp]?1:-1; } } }
        MBM+=(1-chi)/(double)ph;
        // genus test
        int ok=1; int k2=(ub&1)?4:8; if(((pp-a)%k2+k2)%k2!=0) ok=0;
        int omega=0;
        if(ok){ long m=u; while(m>1){ long l=spf[m]; while(m%l==0) m/=l; if(l==2) continue; omega++; int pl=qr[l%pp]?1:-1; int al=jacobi(-B,l); if(pl!=al){ok=0;break;} } }
        if(ok){ long m=B; while(m>1){ long l=spf[m]; while(m%l==0) m/=l; if(l==2) continue; omega++; int pl=qr[l%pp]?1:-1; int al=jacobi(-u,l); if(pl!=al){ok=0;break;} } }
        if(ok){ long s=(1L<<omega)*((ub&1)?2:4); Mgen+=(double)s/ph; G++; }
      }
    }
    printf("%ld %ld %.4f %.4f %.4f %ld\n",pp,R,M0,MBM,Mgen,G);
    if(p>N && nx==0) break;
  }
  return 0;
}
