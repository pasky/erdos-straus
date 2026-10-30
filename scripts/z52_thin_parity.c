/* z52 deep thin-pointwise: parity / 2-adic distribution of the (★) count R(n) and its level pieces.
   R(n) = #{(u,C): u,C>=1, (4uC-1) | n+u}  (= ordered (★) count; FRONTIER §2.1 trial form).
   D_C(n) = #{u : (4uC-1) | n+u} = #{d | 4Cn+1 : d ≡ -1 (mod 4C)}.
   Usage: z52_thin_parity N0 N1  -> scans odd n in [N0,N1], n ≡ 1 (mod 4); prints per-class statistics. */
#include <stdio.h>
#include <stdlib.h>
static int isprime(long n){ if(n<2) return 0; for(long d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
static int issq(long n){ long r=1; while(r*r<n) r++; return r*r==n; }
int main(int argc,char**argv){
  long N0=atol(argv[1]), N1=atol(argv[2]);
  long cnt[3]={0}, odd_half[3]={0}, v2hist[3][8]={{0}}, lvl_odd[3]={0}, zero[3]={0};
  long bad_even=0;
  for(long n=N0+((1-N0%4+4)%4); n<=N1; n+=4){
    int cls = isprime(n)?0:(issq(n)?2:1);
    long R=0; int lvlodd=0;
    /* accumulate per-level counts D_C via a small array */
    long Cmax=(n+2)/4+1;
    long *D=calloc(Cmax+2,sizeof(long));
    for(long u=1; 4*u-1<=n+u; u++){
      long s=n+u;
      for(long C=1; 4*u*C-1<=s; C++) if(s%(4*u*C-1)==0){ R++; D[C]++; }
    }
    for(long C=1;C<=Cmax;C++){ if(D[C]&1) bad_even++; if((D[C]/2)&1) lvlodd++; }
    free(D);
    cnt[cls]++;
    if(R==0) zero[cls]++;
    if((R/2)&1) odd_half[cls]++;
    if(lvlodd&1) lvl_odd[cls]++;
    int v=0; long r=R; if(r==0) v=7; else { while(!(r&1)&&v<6){ r>>=1; v++; } }
    v2hist[cls][v]++;
  }
  const char*nm[3]={"prime","composite-nonsquare","odd-square"};
  printf("range [%ld,%ld], n≡1 (4); violations of 'every D_C even': %ld\n",N0,N1,bad_even);
  for(int c=0;c<3;c++){
    printf("%-20s count=%ld  R=0:%ld  R/2 odd:%ld (%.3f)  #levels with D_C/2 odd is odd:%ld  v2(R) hist[0..6,zero]:",
      nm[c],cnt[c],zero[c],odd_half[c],cnt[c]?(double)odd_half[c]/cnt[c]:0,lvl_odd[c]);
    for(int v=0;v<8;v++) printf(" %ld",v2hist[c][v]); printf("\n");
  }
  return 0;
}
