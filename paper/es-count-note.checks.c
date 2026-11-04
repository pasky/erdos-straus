/* Sanity computations for es-count-note.tex, Section "Numerical remarks".
 *   gcc -O2 -o checks paper/es-count-note.checks.c -lm
 *   ulimit -v 2000000; timeout 600 ./checks zeros 10000000   # primes p = 1 (4) <= N with R(p)=0; odd squares
 *   timeout 600 ./checks mgen 8813281                        # M_gen(n) by direct evaluation of (1.4)
 * R(n) = #{(u,B,C): 4uBC-u-B = n};  M_gen(n) = sum over (u,B), gcd(u,B)=1, u+B odd, 4uB-u-B <= n,
 * of s(q)/phi(q) * 1[n*a is a square unit mod q], q = 4uB, a = -(u+B).            */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int *spf;
static long pw(long b,long e,long m){long r=1;b%=m;if(b<0)b+=m;while(e){if(e&1)r=(long)((__int128)r*b%m);b=(long)((__int128)b*b%m);e>>=1;}return r;}
static int leg(long a,long l){a%=l;if(a<0)a+=l;if(a==0)return 0;return pw(a,(l-1)/2,l)==1?1:-1;}
static double term(long n,long u,long B){ long a=-(u+B); long na=n*a; long q=4*u*B; int v2=0; long m=q;
  while(m%2==0){m/=2;v2++;}
  double s;
  if(v2==2){ long r4=na%4; if(r4<0)r4+=4; if(r4!=1) return 0; s=2; }
  else { long r8=na%8; if(r8<0)r8+=8; if(r8!=1) return 0; s=4; }
  double phi=(double)(1L<<(v2-1));
  long x=m; while(x>1){ long l=spf[x]; long pk=1; while(x%l==0){x/=l;pk*=l;} if(leg(na,l)!=1) return 0; s*=2; phi*=(double)(pk/l)*(l-1); }
  return s/phi; }
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: %s zeros N | mgen n\n",argv[0]);return 1;}
  long N=atol(argv[2]);
  if(!strcmp(argv[1],"zeros")){
    unsigned short *c=calloc(N+1,2); char *comp=calloc(N+1,1);
    for(long u=1;3*u-1<=N;u++) for(long C=1;4*u*C-u-1<=N;C++){ long m=4*u*C-1;
      for(long B=1;;B++){ long n=B*m-u; if(n>N)break; if(c[n]<65535) c[n]++; } }
    for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
    long cnt=0; for(long p=5;p<=N;p+=4) if(!comp[p]&&c[p]==0){printf("%ld ",p);cnt++;}
    printf("\nprimes p=1 mod 4 <= %ld with R(p)=0: %ld\n",N,cnt);
    long bad=0; for(long m=3;m*m<=N;m+=2) if(c[m*m]) bad++; printf("odd squares <= N with R>0: %ld\n",bad);
    return 0; }
  spf=calloc(N+11,sizeof(int)); for(long i=2;i<=N+10;i++) if(!spf[i]) for(long j=i;j<=N+10;j+=i) if(!spf[j]) spf[j]=(int)i;
  double M=0; for(long u=1;3*u-1<=N;u++) for(long B=1;4*u*B-u-B<=N;B++){ if(((u+B)&1)==0) continue;
    long a=u,b=B; while(b){long t=a%b;a=b;b=t;} if(a!=1) continue; M+=term(N,u,B);}
  double L=log((double)N); printf("n=%ld Mgen=%.6f Mgen/log^2 n=%.5f\n",N,M,M/(L*L)); return 0; }
