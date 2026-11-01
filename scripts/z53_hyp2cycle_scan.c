/* z53_hyp2cycle_scan.c — Z53_HYP2CYCLE.md: 2-cycles of the remainder map at a single n.
   For each odd n (stdin, one per line) and U (argv[1]; 0 => U = floor(n^{1/4})), let
   f(x) = the unique y in (U,2U] with y = -n (mod x), or bottom.  We enumerate x in (U,2U],
   y = f(x), and keep unordered pairs {u<B} with f(u)=B, f(B)=u and uB | n+u+B (the latter is
   automatic at primes; at composites it is checked).  k = (n+u+B)/(uB).
   Columns: n U N2 N4 N5 Nbi Nodd Nk2 N3cyc Ndef
     N2   = # unordered 2-cycles {u,B} with uB | n+u+B           (the "no 4-condition" count)
     N4   = # of those with 4 | k                                 ((★) balanced block / 2)
     N5   = # with some five-slice condition: 4|k, 4|u, 4|B, 4|ku-1, 4|kB-1
     Nbi  = # bichromatic: jacobi(u,n) != jacobi(B,n) (both units mod n)
     Nodd = # with u+B odd
     Nk2  = # with k == 2 mod 4
     N3cyc= # 3-cycles of f (x->y->z->x, distinct), counted once
     Ndef = # x in (U,2U] with f(x) defined
   Also: if argv[2]=="v", prints each 2-cycle "C n u B k" lines.
   Arithmetic: n < 2^62, U < 2^20.  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static int jacobi(u64 a,u64 n){ int s=1; a%=n; while(a){ while(!(a&1)){ a>>=1; u64 r=n&7; if(r==3||r==5) s=-s; } u64 t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) s=-s; a%=n; } return n==1?s:0; }
static u64 iroot4(u64 n){ u64 r=(u64)floor(pow((double)n,0.25)); while((u128)(r+1)*(r+1)*(r+1)*(r+1)<=n) r++; while((u128)r*r*r*r>n) r--; return r; }
static long *fx; static long fxcap=0;
int main(int argc,char**argv){
  long Ufix = argc>1?atol(argv[1]):0; int verbose = (argc>2 && !strcmp(argv[2],"v"));
  char line[256];
  while(fgets(line,sizeof line,stdin)){
    u64 n=strtoull(line,NULL,10); if(n<5) continue;
    u64 U = Ufix>0 ? (u64)Ufix : iroot4(n);
    if(2*U>=n) continue;
    if((long)(U+1)>fxcap){ fxcap=2*(U+1); fx=realloc(fx,sizeof(long)*(2*fxcap+2)); }
    long Ndef=0;
    for(u64 x=U+1;x<=2*U;x++){
      u64 r=(x - n%x)%x;           /* -n mod x in [0,x) */
      u64 y=r; if(y<=U) y+= x*((U-y)/x+1);
      if(y<=2*U && y>U){ fx[x-U]=(long)y; Ndef++; } else fx[x-U]=0;
    }
    long N2=0,N4=0,N5=0,Nbi=0,Nodd=0,Nk2=0,N3=0;
    for(u64 u=U+1;u<=2*U;u++){
      long B=fx[u-U]; if(!B) continue;
      if((u64)B>u){ long c=fx[B-U]; if(c==(long)u){
          u64 Bu=(u64)B; u64 num=n+u+Bu, q=u*Bu;
          if(num%q==0){ u64 k=num/q; N2++;
            int s4 = (k%4==0), s5 = s4 || (u%4==0) || (Bu%4==0) || ((k*u-1)%4==0) || ((k*Bu-1)%4==0);
            N4+=s4; N5+=s5; if((u+Bu)&1) Nodd++; if(k%4==2) Nk2++;
            int ju=jacobi(u,n), jb=jacobi(Bu,n); if(ju&&jb&&ju!=jb) Nbi++;
            if(verbose) printf("C %llu %llu %llu %llu\n",n,(u64)u,Bu,k);
          } } }
      /* 3-cycles: u -> B -> c -> u with u the minimum */
      long c=fx[B-U]; if(c && c!=(long)u && (u64)c>u && B>(long)u){ long d=fx[c-U]; if(d==(long)u) N3++; }
    }
    printf("%llu %llu %ld %ld %ld %ld %ld %ld %ld %ld\n",n,U,N2,N4,N5,Nbi,Nodd,Nk2,N3,Ndef);
  }
  return 0;
}
