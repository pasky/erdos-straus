/* z38_b1.c (O268): (★) and the b = 1 line as two pair events with the SAME Brauer character, for primes p ≡ 1 (mod 4).
   Pairs (x,y), gcd(x,y) = 1, modulus q = 4xy.
     (★):   target a = -(x+y),  hit iff q | p+x+y    (x+y odd; region 4xy-x-y <= p)
     b = 1: target a = -(4x+y), hit iff q | p+4x+y   (y odd; region 4xy-4x-y <= p, y >= 3)   [B1_LINE Lemma 1.1, S = 4x, T = y]
   Brauer character in both cases chi_{-4xy} (BL class at the rational point: inv_p = (-xy/p); chi(a) = -1 identically).
   Main term M4 = principal + chi_{-4} + chi_{-4xy} + chi_{-4}chi_{-4xy}  (conditions mod 4 and the Brauer character):
     pair term = (|H|/phi(q)) * 1[p == a mod 4] * 1[(-xy/p) = -1],  |H| = 4 (2 if chi_{-4xy} is a mod-4 character, i.e. xy = 2^k
     with ... handled: if odd part of xy is 1 and v2(xy) even then chi_{-4xy} = chi_{-4}).
   (For the b = 1 line the mod-4 condition is needed: without it the y = 1 pairs give a divergent main term.)
   output per prime: p R N1 M4star M4b1 ; summary to stderr.
   usage: ./z38_b1 lo hi [mod24class or 0]
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int *spf;
static int jac(long a,long m){ a%=m; if(a<0)a+=m; int t=1; while(a){ while(!(a&1)){a>>=1; long r=m&7; if(r==3||r==5)t=-t;} long x=a;a=m;m=x; if((a&3)==3&&(m&3)==3)t=-t; a%=m;} return m==1?t:0; }
static long gcdl(long a,long b){ while(b){long t=a%b;a=b;b=t;} return a; }
static double phi(long m){ double r=m; while(m>1){ long l=spf[m]; r=r/l*(l-1); while(m%l==0) m/=l; } return r; }
static int hsize(long m){ /* |<chi_{-4}, chi_{-4m}>| */ long o=m; int v=0; while(!(o&1)){o>>=1;v++;} if(o==1 && (v%2==0)) return 2; return 4; }
int main(int argc,char**argv){
  long lo=atol(argv[1]), hi=atol(argv[2]); int cls = argc>3? atoi(argv[3]) : 0; long N=4*hi+10;
  spf=calloc(N+1,sizeof(int)); for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i;
  long np=0, f1=0, fs=0, fu=0;
  for(long p=lo|1; p<=hi; p+=2){
    if(spf[p]!=p || (p&3)!=1) continue; if(cls && p%24!=cls) continue;
    long R=0,N1=0; double Ms=0,Mb=0;
    /* (★) */
    for(long x=1;3*x-1<=p;x++) for(long y=1;4*x*y-x-y<=p;y++){ if(((x+y)&1)==0||gcdl(x,y)!=1) continue; long q=4*x*y;
      if((p+x+y)%q==0) R++;
      if(((p+x+y)&3)==0 && jac(-x*y,p)==-1) Ms += hsize(x*y)/phi(q); }
    /* b = 1 */
    for(long y=3; 3*y-4<=p; y+=2) for(long x=1; 4*x*y-4*x-y<=p; x++){ if(gcdl(x,y)!=1) continue; long q=4*x*y;
      if((p+4*x+y)%q==0) N1++;
      if(((p+y)&3)==0 && jac(-x*y,p)==-1) Mb += hsize(x*y)/phi(q); }
    np++; if(N1==0) f1++; if(R==0) fs++; if(R+N1==0) fu++;
    printf("%ld %ld %ld %.4f %.4f\n",p,R,N1,Ms,Mb);
  }
  fprintf(stderr,"# primes p≡1(4)%s in [%ld,%ld]: %ld; R=0: %ld, N1=0: %ld, R+N1=0: %ld\n", cls?" (class)":"", lo,hi,np,fs,f1,fu);
  return 0;
}
