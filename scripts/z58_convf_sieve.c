// z58 CONVF: sieve the full count R(n) = #{(a,b,c,d): 4abcd = a+b+nc} restricted to a<=b (existence only),
// via n = B*f - 4a^2 d, f = 4acd-1, B>=1 (B = 4bcd-1). Tags per n: bit0 c=1, bit1 a=1, bit2 d=1, bit3 c=2, bit4 c=3, bit5 c>=4 only
// usage: ./sieve N  -> prints n = 1 (mod 4) with R(n)=0 and (for primes) the sub-family failure table
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
 unsigned char *T=calloc(N+1,1); unsigned char *R=calloc(N+1,1);
 for(long a=1;4*a*a<=N+2*a;a++) for(long d=1;4*a*a*d<=N+2*a;d++){ long s=4*a*a*d;
   for(long c=1;;c++){ long f=4*a*c*d-1; if(f-s>N) break;
     unsigned char tag = (c==1?1:0)|(a==1?2:0)|(d==1?4:0)|(c==2?8:0)|(c==3?16:0);
     for(long B=1;;B++){ long n=B*f-s; if(n>N) break; if(n>0){ if(R[n]<255)R[n]++; T[n]|=tag; } } } }
 char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
 long zc=0, c1z=0, a1z=0, d1z=0, c12z=0, c123z=0, a1c1z=0;
 for(long n=1;n<=N;n+=4){ long s=0; while((s+1)*(s+1)<=n)s++; int sq=(s*s==n);
   if(R[n]==0){ if(!sq){ printf("ZERO %ld %s\n",n,!comp[n]?"P":"C"); zc++; } continue; }
   if(comp[n]||sq) continue;
   if(!(T[n]&1)){ c1z++; printf("c1fail %ld tags=%d R=%d\n",n,T[n],R[n]); }
   if(!(T[n]&2)){ a1z++; printf("a1fail %ld tags=%d R=%d\n",n,T[n],R[n]); }
   if(!(T[n]&4)){ d1z++; }
   if(!(T[n]&9)){ c12z++; printf("c12fail %ld tags=%d\n",n,T[n]); }
   if(!(T[n]&25)){ c123z++; printf("c123fail %ld tags=%d\n",n,T[n]); }
   if(!(T[n]&3)){ a1c1z++; printf("a1c1fail %ld tags=%d\n",n,T[n]); }
 }
 printf("N=%ld nonsq zeros=%ld | prime zeros: c=1:%ld a=1:%ld d=1:%ld c<=2:%ld c<=3:%ld (a=1 or c=1):%ld\n",N,zc,c1z,a1z,d1z,c12z,c123z,a1c1z);
 return 0;}
