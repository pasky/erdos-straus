/* z62 INVERSE test 3 (C engine): for primes p = 1 (24) in [lo,hi] and u = 1..U, print per slice a 4-char code:
   hit(0/1), m1 = [-1 in Div(s_u) mod 4u] (0/1), w = min(omega(c_u),3), k = #{d in Div(s_u): chi_{-4u}(d) = -chi_{-4u}(c_u)}
   (k printed as a base-36 digit, capped at 35), where p+u = s_u c_u, s_u = z-smooth part (primes not dividing 4u), c_u = rest.
   Line: p code_1 ... code_U (space separated). Same conventions as scripts/z62_inverse_private.py coarse mode. */
#include <stdio.h>
#include <stdlib.h>
static int jac(long a,long n){ int t=1; a%=n; if(a<0)a+=n; while(a){ while(!(a&1)){ a>>=1; long r=n&7; if(r==3||r==5)t=-t; }
  long x=a; a=n; n=x; if((a&3)==3&&(n&3)==3)t=-t; a%=n; } return n==1?t:0; }
int main(int argc,char**argv){ long lo=atol(argv[1]),hi=atol(argv[2]); int U=atoi(argv[3]); long z=atol(argv[4]); long M=hi+U+1;
 int *spf=calloc(M+1,sizeof(int)); if(!spf){fprintf(stderr,"oom\n");return 1;}
 for(long i=2;i<=M;i++) if(!spf[i]){ for(long j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i; }
 long divs[8192], dm[8192]; const char *B36="0123456789abcdefghijklmnopqrstuvwxyz";
 for(long p=lo+((1-lo)%24+24)%24;p<=hi;p+=24){ if(spf[p]!=p) continue; printf("%ld",p);
  for(int u=1;u<=U;u++){ long N=p+u, m=4L*u, x=N; int nd=1; divs[0]=1; int nds=1; dm[0]=1; long c=1; int om=0;
   while(x>1){ long q=spf[x]; int e=0; while(x%q==0){x/=q;e++;}
     int cur=nd; long pw=1; for(int k=1;k<=e;k++){ pw*=q; for(int t=0;t<cur;t++) divs[nd++]=divs[t]*pw; }
     if(m%q==0) continue;
     if(q<=z){ int cs=nds; long pw2=1; for(int k=1;k<=e;k++){ pw2=pw2*q%m; for(int t=0;t<cs;t++) dm[nds++]=dm[t]*pw2%m; } }
     else { om+=e; for(int k=0;k<e;k++) c*=q; } }
   int hit=0; for(int t=0;t<nd;t++) if(divs[t]%m==m-1){hit=1;break;}
   /* dedupe dm residues */
   static char seen[4096]; for(int t=0;t<nds;t++) seen[dm[t]]=0; int m1=0,k=0; int chic = c>1? jac(-u,c):1;
   for(int t=0;t<nds;t++){ long r=dm[t]; if(seen[r]) continue; seen[r]=1; if(r==m-1)m1=1; if(jac(-u,r>0?r:r+m)==-chic) k++; }
   /* jac(-u, r) with r < m is not chi_{-4u}(r) unless computed as Kronecker on odd residue: r odd, coprime to u -> ok */
   if(k>35)k=35; printf(" %d%d%d%c",hit,m1,om>3?3:om,B36[k]); }
  printf("\n"); }
 return 0;}
