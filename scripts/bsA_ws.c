/* bsA_ws: (W) which n < N have no length-3 HJ word (t,u,v>=2, tuv-u-v=n);
   (S) non-square n = 1 (4) with words but no Jacobi -1 word. gcc -O2 -o /tmp/bsA_ws scripts/bsA_ws.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int jacobi(long a, long n){ int s=1; a%=n; if(a<0)a+=n;
  while(a){ while(!(a&1)){ a>>=1; long r=n&7; if(r==3||r==5) s=-s; }
    long t=a; a=n; n=t; if((a&3)==3&&(n&3)==3) s=-s; a%=n; }
  return n==1?s:0; }
int main(int argc,char**argv){ long N=atol(argv[1]);
  unsigned char *has=calloc(N,1), *neg=calloc(N,1);
  for(long t=2; 4*t-4<N; t++) for(long u=2; 2*t*u-u-2<N; u++){
    long A=t*u-1;
    for(long v=2; t*u*v-u-v<N; v++){ long n=t*u*v-u-v; has[n]=1;
      if((n&3)==1 && !neg[n] && jacobi(A,n)==-1) neg[n]=1; } }
  long cntW=0; printf("(W) exceptions n<%ld:",N);
  for(long n=2;n<N;n++) if(!has[n]){ cntW++; if(cntW<=40) printf(" %ld",n); }
  printf("  [total %ld]\n",cntW);
  long cntS=0; printf("(S) violations (non-square n=1(4), words exist, none -1):");
  for(long n=5;n<N;n+=4){ long r=(long)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++;
    if(r*r==n) { if(neg[n]) printf(" [square with -1: %ld]",n); continue; }
    if(has[n] && !neg[n]){ cntS++; if(cntS<=20) printf(" %ld",n);} }
  printf("  [total %ld]\n",cntS); return 0; }
