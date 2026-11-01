/* z52d_p2_TO5_certs.c — structure of (★) certificates per prime (Pass 2, batch TO5).
   Pairs (u,B): gcd(u,B)=1, u+B odd, 4uB-u-B <= p, and 4uB | p+u+B  (= the z38 R* definition, R = R*(p)).
   Identities used (checked in code by assertion): with C=(p+u+B)/(4uB):
     d := 4uC-1 = (p+u)/B,  e := 4BC-1 = (p+B)/u,  d*e = 4Cp+1,  d ≡ e ≡ -1 (mod 4C).
   Output per prime (stdout): p R Rbox minuB nBcount1 nDprime nEprime minDprime
     Rbox   = #certs with uB <= sqrt(p)     minuB = min uB over certs (0 if none)
     nDprime = #certs with d=(p+u)/B prime  nEprime = #certs with e=(p+B)/u prime  minDprime = least such prime d (0 if none)
   stderr: histograms of B/sqrt(p) and u/sqrt(p) over all certs (deciles 0..10, 10 = >=1).
   usage: ./z52d_p2_TO5_certs lo hi   (odd primes in [lo,hi])  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
static long gcdl(long a,long b){ while(b){ long t=a%b; a=b; b=t; } return a; }
int main(int argc,char**argv){
  long lo=atol(argv[1]), hi=atol(argv[2]);
  long N=2*hi+10;
  char *comp=calloc(N+1,1); comp[0]=comp[1]=1;
  for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  long hB[11]={0}, hU[11]={0};
  for(long p=(lo|1); p<=hi; p+=2){
    if(comp[p]) continue;
    long R=0,Rbox=0,minuB=0,n1=0,nD=0,nE=0,minD=0; double sp=sqrt((double)p);
    for(long u=1; 3*u-2 <= p; u++){
      for(long B=1; B*(4*u-1) <= p+u; B++){
        if((u+B)%2==0) continue;
        if(gcdl(u,B)!=1) continue;
        long q=4*u*B; long s=p+u+B;
        if(s%q) continue;
        long C=s/q; (void)C;
        long d=(p+u)/B, e=(p+B)/u;
        if(d*e != 4*C*p+1 || (d+1)%(4*C)||(e+1)%(4*C)){ fprintf(stderr,"identity fail p=%ld u=%ld B=%ld\n",p,u,B); exit(1);} 
        R++;
        if((double)u*B <= sp) Rbox++;
        if(minuB==0 || u*B<minuB) minuB=u*B;
        if(B==1) n1++;
        if(d<=N && !comp[d]) { nD++; if(minD==0||d<minD) minD=d; }
        if(e<=N && !comp[e]) nE++;
        int bi=(int)floor(10.0*B/sp); if(bi>10) bi=10; hB[bi]++;
        int ui=(int)floor(10.0*u/sp); if(ui>10) ui=10; hU[ui]++;
      }
    }
    printf("%ld %ld %ld %ld %ld %ld %ld %ld\n",p,R,Rbox,minuB,n1,nD,nE,minD);
  }
  fprintf(stderr,"hist B/sqrt(p) deciles:"); for(int i=0;i<=10;i++) fprintf(stderr," %ld",hB[i]); fprintf(stderr,"\n");
  fprintf(stderr,"hist u/sqrt(p) deciles:"); for(int i=0;i<=10;i++) fprintf(stderr," %ld",hU[i]); fprintf(stderr,"\n");
  return 0;
}
