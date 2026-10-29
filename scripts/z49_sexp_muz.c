/* CONJECTURE_S_MODEL §2 check (d): conditional mass mu(z) of the Janson family is ~uniform in the small-prime
   residues z, including the class of one. Scaled-down parameters (asymptotic ones are infeasible):
   small primes 5,7,11,13 (Y=13; s coprime to 6), s<=S0, rough parts squarefree with primes >13,
   u=s1 r1 in [U0,U1], u≡3 mod 4, v=s2 r2 in [V0,V1], gcd(u,v)=1. P(E|z)=[z≡-u-v mod s1s2]/phi(R).
   Also reports the z-average prediction sum 1/(phi(s1 s2) phi(R)) and max_p p*w_p(z).
   usage: muz U0 U1 V0 V1 S0 nz */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static int *spf;
int main(int argc,char**argv){
  long U0=atol(argv[1]),U1=atol(argv[2]),V0=atol(argv[3]),V1=atol(argv[4]),S0=atol(argv[5]); int nz=atoi(argv[6]);
  spf=calloc(V1+1,sizeof(int));
  for(long i=2;i<=V1;i++) if(!spf[i]) for(long j=i;j<=V1;j+=i) if(!spf[j]) spf[j]=i;
  /* per n: smooth part s (primes<=13, need gcd(s,6)=1), rough part R squarefree, phi(R), largest rough prime list */
  long *sm=malloc((V1+1)*sizeof(long)); double *iphi=malloc((V1+1)*sizeof(double)); char *ok=calloc(V1+1,1);
  for(long n=1;n<=V1;n++){ long m=n,s=1,R=1; double ph=1; int good=1;
    while(m>1){int p=spf[m]; int e=0; while(m%p==0){m/=p;e++;}
      if(p<=3){good=0;break;} if(p<=13){for(int k=0;k<e;k++)s*=p;} else { if(e>1){good=0;break;} R*=p; ph*=(p-1);} }
    if(good && s<=S0){ok[n]=1; sm[n]=s; iphi[n]=1.0/ph;} }
  const uint64_t M = 625ULL*343*121*169; /* covers all smooth s<=S0 if S0<=... (exponents bounded) */
  srand(12345);
  printf("# U=[%ld,%ld] V=[%ld,%ld] S0=%ld\n",U0,U1,V0,V1,S0);
  /* z-average prediction */
  double avg=0;
  for(long u=U0;u<=U1;u++){ if(!ok[u]||u%4!=3) continue;
    for(long v=V0;v<=V1;v++){ if(!ok[v]) continue; long a=u,b=v; while(b){long t=a%b;a=b;b=t;} if(a!=1) continue;
      long s=sm[u]*sm[v]; /* phi(s) */ long m=s; double ps=1; while(m>1){int p=spf[m]; ps*=(p-1); m/=p; while(m%p==0){ps*=p;m/=p;}}
      avg += iphi[u]*iphi[v]/ps; } }
  printf("z-average prediction  E_z mu = %.5f\n",avg);
  double *w=calloc(V1+1,sizeof(double));
  for(int iz=0;iz<nz;iz++){
    uint64_t z; if(iz==0) z=1; else { do{ z=((uint64_t)rand()<<31 ^ rand())%M; }while(z%5==0||z%7==0||z%11==0||z%13==0); }
    double mu=0; for(long i=0;i<=V1;i++) w[i]=0;
    for(long u=U0;u<=U1;u++){ if(!ok[u]||u%4!=3) continue;
      for(long v=V0;v<=V1;v++){ if(!ok[v]) continue;
        uint64_t s=(uint64_t)sm[u]*sm[v]; if((z+u+v)%s) continue;
        long a=u,b=v; while(b){long t=a%b;a=b;b=t;} if(a!=1) continue;
        double P=iphi[u]*iphi[v]; mu+=P;
        long m=u; while(m>1){int p=spf[m]; if(p>13) w[p]+=P; while(m%p==0)m/=p;}
        m=v; while(m>1){int p=spf[m]; if(p>13) w[p]+=P; while(m%p==0)m/=p;} } }
    double mx=0; long arg=0; for(long p=17;p<=V1;p++) if(w[p]*p>mx){mx=w[p]*p;arg=p;}
    printf("z=%s%llu  mu(z)=%.5f  ratio=%.4f  max_p p*w_p=%.3f (p=%ld)\n", iz==0?"1 (class of one) ":"", (unsigned long long)(iz==0?1:z), mu, mu/avg, mx, arg);
  }
  return 0; }
