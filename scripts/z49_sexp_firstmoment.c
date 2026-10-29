/* E N_H in the prime-Haar model (n ≡ 1 mod 24): sum over coprime a<v<=H of
   P(n ≡ -a-v mod av) * [certificate], certificate iff Jacobi(-a-v, odd part of av) = -1 (Thm A, (2/n)=1).
   P = [ -a-v ≡ 1 mod gcd(av,24) ] * phi(gcd(av,24))/phi(av).  Prints E N_H at H = 2^k. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int jac(long a,long n){ int t=1; a%=n; if(a<0)a+=n; while(a){ while(a%2==0){a/=2; long r=n%8; if(r==3||r==5)t=-t;} long tmp=a;a=n;n=tmp; if(a%4==3&&n%4==3)t=-t; a%=n;} return n==1?t:0; }
int main(int argc,char**argv){ long H=atol(argv[1]); int *spf=calloc(H+1,sizeof(int));
  for(long i=2;i<=H;i++) if(!spf[i]) for(long j=i;j<=H;j+=i) if(!spf[j]) spf[j]=i;
  double *phi=malloc((H+1)*sizeof(double)); for(long n=1;n<=H;n++){ long m=n; double p=1; while(m>1){int q=spf[m]; long qk=1; while(m%q==0){m/=q;qk*=q;} p*=(double)(qk/q)*(q-1);} phi[n]=p; }
  double mu=0; long next=16;
  for(long v=2;v<=H;v++){
    for(long a=1;a<v;a++){ long x=a,y=v; while(y){long t=x%y;x=y;y=t;} if(x!=1) continue;
      long m=a*v; long g=1; long mm=m; int e2=0; while(mm%2==0){mm/=2;e2++;} g*= (e2>=3?8:(1<<e2)); if(m%3==0) g*=3;
      long b=-(a+v); long br=((b% g)+g)%g; if(br!=1%g) continue;
      long mo=m; while(mo%2==0) mo/=2;
      int col = (mo==1)? 1 : jac(-(a+v),mo);
      if(col!=-1) continue;
      double pg = (g==1?1:(g==2?1:(g==4?2:(g==8?4:(g==3?2:(g==6?2:(g==12?4:(g==24?8:0))))))));
      mu += pg/(phi[a]*phi[v]); }
    if(v==next-1){ printf("H=%ld  E N_H=%.4f  (ln H)^2=%.3f  ratio=%.4f\n",v,mu,log(v)*log(v),mu/(log(v)*log(v))); next*=2; } }
  printf("final H=%ld  E N_H=%.6f\n",H,mu); return 0; }
