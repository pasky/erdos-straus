/* CONJECTURE_S_MODEL §3: pointwise loads under the class of one at all prime powers <= Y (full powers).
   Events: all coprime pairs a<v<=H (upper bound for the certificate subfamily).
   Live iff s_Y(a) | v+1 and s_Y(v) | a+1; P = 1/(phi(a/s_Y(a)) phi(v/s_Y(v))).
   V_a(l) = sum over live E with l | a, V_v(l) = sum with l | v (l>Y prime).
   Prints S_Y = sum P, S_Y/(L^2 log Y), max_l l*V_a(l), max_l l*V_v(l), normalised by L^2 log Y, and top offenders.
   usage: loads H Y */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long H=atol(argv[1]); int Y=atoi(argv[2]);
  int *spf=calloc(H+2,sizeof(int)); for(long i=2;i<=H+1;i++) if(!spf[i]) for(long j=i;j<=H+1;j+=i) if(!spf[j]) spf[j]=i;
  long *sm=malloc((H+2)*sizeof(long)); double *ip=malloc((H+2)*sizeof(double));
  for(long n=1;n<=H+1;n++){ long m=n,s=1; double ph=1; while(m>1){int p=spf[m]; long pk=1; while(m%p==0){m/=p;pk*=p;} if(p<=Y) s*=pk; else ph*=(double)(pk/p)*(p-1);} sm[n]=s; ip[n]=1.0/ph; }
  double *Va=calloc(H+2,sizeof(double)),*Vv=calloc(H+2,sizeof(double)); double S=0;
  for(long v=2;v<=H;v++){ long B=sm[v];
    for(long a=B-1; a<v; a+=B){ if(a<1) continue; long A=sm[a]; if((v+1)%A) continue;
      long x=a,y=v; while(y){long t=x%y;x=y;y=t;} if(x!=1) continue;
      double P=ip[a]*ip[v]; S+=P;
      long m=a; while(m>1){int p=spf[m]; if(p>Y) Va[p]+=P; while(m%p==0)m/=p;}
      m=v; while(m>1){int p=spf[m]; if(p>Y) Vv[p]+=P; while(m%p==0)m/=p;} } }
  double L=log(H), nrm=L*L*log(Y);
  double ma=0,mv=0; long la=0,lv=0;
  for(long p=Y+1;p<=H;p++) if(spf[p]==p){ if(p*Va[p]>ma){ma=p*Va[p];la=p;} if(p*Vv[p]>mv){mv=p*Vv[p];lv=p;} }
  printf("H=%ld Y=%d L=%.2f  S_Y=%.3f  S_Y/(L^2 logY)=%.4f  max l*Va=%.3f (l=%ld) [/nrm %.4f]  max l*Vv=%.3f (l=%ld) [/nrm %.4f]\n",
    H,Y,L,S,S/nrm,ma,la,ma/nrm,mv,lv,mv/nrm);
  /* max of (Va+Vv) relative to threshold: report l*V and V for l in dyadic ranges */
  for(long lo=Y+1; lo<=H; lo*=2){ double mx=0; long arg=0; double mxV=0; for(long p=lo;p<2*lo && p<=H;p++) if(spf[p]==p){ double V=Va[p]+Vv[p]; if(p*V>mx){mx=p*V;arg=p;} if(V>mxV) mxV=V;}
    printf("  l in [%ld,%ld): max l*V=%.3f (l=%ld)  max V=%.4g\n",lo,2*lo,mx,arg,mxV); }
  return 0; }
