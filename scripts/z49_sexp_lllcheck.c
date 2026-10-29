/* CONJECTURE_S_MODEL §3 check: non-adaptive class of one Q(Y)=prod_{l<=Y} l^{k_l}, k_l = max k with l^k < Y
   (k_2>=3, k_3>=1). Coordinates: primes l>Y, and for l<=Y the residual digits (modulus m_c = l^{k_l+1}).
   Events: all coprime a<v<=H. Live iff gcd(a,Q) | v+1 and gcd(v,Q) | a+1; P = 1/(phi_Q(a) phi_Q(v)).
   Reports: log Q, S = sum P, S_beta = sum beta^{s(E)} P (beta = 1+1/log L),
     max_c m_c * w_c / L^2 split by (c divides a) / (c divides v),
     and the log-threshold LLL quantity max_E sum_{c in supp E} w_c * L/log(m_c) ... (we report
     max_E sum_{c in supp E} 2 w_c  -- must be <= 1/4 for H4 Lemma 4's LLL with x=2P),
     and max_c beta-weighted load (must be <= eta=(3/4)log beta for OMEGA13 Lemma 1.1).
   usage: lllcheck H Y */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int *spf; static int Y; static long *kpow; /* kpow[l] = l^{k_l} for l<=Y */
static long gQ(long m){ long g=1; while(m>1){int p=spf[m]; long pk=1; while(m%p==0){m/=p;pk*=p;} if(p<=Y){ long t=kpow[p]; g*= (pk<t?pk:t);} } return g; }
static double phiQinv(long m){ double ph=1; long mm=m; while(mm>1){int p=spf[mm]; long pk=1; while(mm%p==0){mm/=p;pk*=p;}
    if(p>Y) ph*=(double)(pk/p)*(p-1); else { long t=kpow[p]; if(pk>t) ph*=(double)pk/t; } } return 1.0/ph; }
/* coordinate id: for p>Y use p; for p<=Y use -p (residual digits) when l^{k+1} | m */
int main(int argc,char**argv){ long H=atol(argv[1]); Y=atoi(argv[2]);
  spf=calloc(H+2,sizeof(int)); for(long i=2;i<=H+1;i++) if(!spf[i]) for(long j=i;j<=H+1;j+=i) if(!spf[j]) spf[j]=i;
  kpow=calloc(Y+1,sizeof(long)); double logQ=0;
  for(int p=2;p<=Y;p++) if(spf[p]==p){ long t=1; while(t*p<Y) t*=p; if(p==2&&t<8)t=8; if(p==3&&t<3)t=3; kpow[p]=t; logQ+=log((double)t);}
  long *gq=malloc((H+2)*sizeof(long)); double *ipq=malloc((H+2)*sizeof(double));
  for(long n=1;n<=H+1;n++){ gq[n]=gQ(n); ipq[n]=phiQinv(n); }
  double L=log(H), beta=1+1/log(L), eta=0.75*log(beta);
  double *Wa=calloc(H+2,sizeof(double)),*Wv=calloc(H+2,sizeof(double)),*Wb=calloc(H+2,sizeof(double));
  double *Wsa=calloc(Y+2,sizeof(double)),*Wsv=calloc(Y+2,sizeof(double)),*Wsb=calloc(Y+2,sizeof(double));
  double S=0,Sb=0;
  for(int pass=0;pass<2;pass++){ double worst=0, worstb=0; long wa=0,wv=0;
  for(long v=2;v<=H;v++){ long B=gq[v]; long Av1=v+1;
    for(long a=B-1;a<v;a+=B){ if(a<1) continue; long A=gq[a]; if(Av1%A) continue;
      long x=a,y=v; while(y){long t=x%y;x=y;y=t;} if(x!=1) continue;
      double P=ipq[a]*ipq[v];
      /* support */
      int s=0; long cs[64]; int side[64]; 
      for(int w=0;w<2;w++){ long m= w? v: a; while(m>1){int p=spf[m]; long pk=1; while(m%p==0){m/=p;pk*=p;}
          if(p>Y){cs[s]=p; side[s]=w; s++;} else if(pk>kpow[p]){cs[s]=-p; side[s]=w; s++;} } }
      if(s==0){ continue; } /* deterministic: only (1,2),(2,3) */
      double xb=pow(beta,s)*P;
      if(pass==0){ S+=P; Sb+=xb;
        for(int i=0;i<s;i++){ long c=cs[i]; if(c>0){ if(side[i]) Wv[c]+=P; else Wa[c]+=P; Wb[c]+=xb;} else { if(side[i]) Wsv[-c]+=P; else Wsa[-c]+=P; Wsb[-c]+=xb;} } }
      else { double sm=0; for(int i=0;i<s;i++){ long c=cs[i]; sm+= 2*(c>0? Wa[c]+Wv[c] : Wsa[-c]+Wsv[-c]); }
        if(sm>worst){worst=sm; wa=a; wv=v;} }
    } }
  if(pass==1) printf("  LLL (x=2P): max_E sum_{c in supp E} 2 w_c = %.4f at (a,v)=(%ld,%ld)  [need <= 1/4 for H4 Lemma 4 form]\n",worst,wa,wv);
  else {
    double ma=0,mv=0,mb=0; long la=0,lv=0,lb=0;
    for(long p=Y+1;p<=H;p++) if(spf[p]==p){ if(p*Wa[p]>ma){ma=p*Wa[p];la=p;} if(p*Wv[p]>mv){mv=p*Wv[p];lv=p;} if(Wb[p]>mb){mb=Wb[p];lb=p;} }
    double msa=0,msv=0,msb=0; int ls=0,lsv=0,lsb=0;
    for(int p=2;p<=Y;p++) if(spf[p]==p){ double m=(double)kpow[p]*p; if(m*Wsa[p]>msa){msa=m*Wsa[p];ls=p;} if(m*Wsv[p]>msv){msv=m*Wsv[p];lsv=p;} if(Wsb[p]>msb){msb=Wsb[p];lsb=p;} }
    printf("H=%ld Y=%d L=%.2f logQ=%.1f  S=%.3f (S/L^2=%.3f)  S_beta=%.3f\n",H,Y,L,logQ,S,S/(L*L),Sb);
    printf("  primes l>Y: max l*w_a/L^2=%.3f (l=%ld)  max l*w_v/L^2=%.3f (l=%ld)  max beta-load=%.4f (l=%ld) [eta=%.4f]\n",ma/(L*L),la,mv/(L*L),lv,mb,lb,eta);
    printf("  residual digits l<=Y: max m*w_a/L^2=%.3f (l=%d)  max m*w_v/L^2=%.3f (l=%d)  max beta-load=%.4f (l=%d)\n",msa/(L*L),ls,msv/(L*L),lsv,msb,lsb);
  } }
  return 0; }
