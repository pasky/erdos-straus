/* R72 naive brute force straight from the definition (POINTWISE_TYPEI2 (2.2)), no Lemma 1.1:
   for all c,k with ck <= H and v_r(c) odd, N = 1+4ck^2, every odd f <= Y with f | N, and F in {f, N/f}:
   test F = -1 mod m' (odd r-free part of ck), F = 1 mod r^{v_r(ck)}, F = -w mod 2^{v_2(4ck)}.
   Prints "c k F" for each certificate.  Usage: review_typei3_naive r w H Y [all] */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128; typedef long long i64; typedef unsigned long long u64;
static void p128(u128 x){char b[60];int i=59;b[i]=0;if(!x){putchar('0');return;}while(x){b[--i]='0'+(int)(x%10);x/=10;}fputs(b+i,stdout);}
int main(int argc,char**argv){
  i64 r=atoll(argv[1]), w=atoll(argv[2]); u64 H=strtoull(argv[3],0,10), Y=strtoull(argv[4],0,10);
  u64 n=0; int all = argc>5; /* "all": any c with squarefree part not in {1,2,3,6} (no v_r(c) parity filter) */
  for(u64 c=1;c<=H;c++){ u64 q=c; int vc=0; while(q%r==0){q/=r;vc++;} if(!all && vc%2==0) continue;
    if(all){ u64 sf=1, x=c; for(u64 p=2;p*p<=x;p++){ int e=0; while(x%p==0){x/=p;e++;} if(e&1) sf*=p; } sf*=x; if(sf==1||sf==2||sf==3||sf==6) continue; }
    for(u64 k=1;c*k<=H;k++){
      u64 ck=c*k; u128 N=1+(u128)4*c*k*k;
      u64 h=4*ck; int t=0; while(!(h&1)){h>>=1;t++;} u64 rv=1; while(h%r==0){h/=r;rv*=r;} u64 mp=h; /* h = m' */
      u128 twot=(u128)1<<t;
      for(u64 f=1;f<=Y;f+=2){ if(N%f) continue;
        u128 Fs[2]={f, N/f};
        for(int z=0;z<2;z++){ u128 F=Fs[z]; if(z==1 && Fs[1]==Fs[0]) continue;
          if((F+1)%mp) continue; if((F-1)%rv) continue;
          /* F = -w mod 2^t: (F + w) mod 2^t == 0, w may be negative */
          i64 wm = ((w % (i64)64) + 64); /* not used */ (void)wm;
          u128 Fw = (w>=0)? F+(u128)w : F-(u128)(-w); /* F > |w| assumed when w<0; else handle */
          if(w<0 && F<(u128)(-w)){ u128 d=(u128)(-w)-F; if(d%twot) continue; }
          else if(Fw%twot) continue;
          n++; p128(c); putchar(' '); p128(k); putchar(' '); p128(F); putchar('\n');
        }
      }
    }
  }
  fprintf(stderr,"naive r=%lld w=%lld H=%llu Y=%llu certs=%llu\n",r,w,H,Y,n);
  return 0;
}
