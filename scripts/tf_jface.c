/* O207 Prop 4.3 check: B(p) [Hasse window (c,1): exists c <= 2sqrt(p)+1, divisor h of p+c, h = -1 mod 4c]
   versus J(p) [exists d <= (p+1)/3: 4dp+1 has a divisor h = -1 mod 4d] (the j = 1 face of the cube). Usage: tf_jface P */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static long pr[200000]; static int npr;
static int hasdiv(long N,long M){ long q[40]; int e[40],k=0; long m=N;
  for(int i=0;i<npr && (long)pr[i]*pr[i]<=m;i++){ if(m%pr[i]==0){ int t=0; while(m%pr[i]==0){m/=pr[i];t++;} q[k]=pr[i]; e[k++]=t; } }
  if(m>1){ q[k]=m; e[k++]=1; }
  static long dv[100000]; int c=1; dv[0]=1;
  for(int i=0;i<k;i++){ int c0=c; long pw=1; for(int t=1;t<=e[i];t++){ pw*=q[i]; for(int j=0;j<c0;j++) dv[c++]=dv[j]*pw; } }
  for(int i=0;i<c;i++) if((dv[i]+1)%M==0) return 1; return 0; }
int main(int argc,char**argv){ long P=atol(argv[1]); long L=2*P+10; char*cp=calloc(L,1);
  for(long i=2;i<L;i++) if(!cp[i]){ pr[npr++]=i; for(long j=2*i;j<L;j+=i) cp[j]=1; }
  long n=0,mis=0,nb=0;
  for(long p=5;p<=P;p+=2){ if(cp[p]) continue; n++;
    int B=0; for(long c=1;c-1<=2*sqrt((double)p)&&!B;c++) if(hasdiv(p+c,4*c)) B=1;
    int J=0; for(long d=1;3*d<=p+1&&!J;d++) if(hasdiv(4*d*p+1,4*d)) J=1;
    nb+=B; if(B!=J){ mis++; printf("mismatch p=%ld B=%d J=%d\n",p,B,J); } }
  printf("P=%ld primes=%ld B=%ld mismatches(B vs J)=%ld\n",P,n,nb,mis); return 0; }
