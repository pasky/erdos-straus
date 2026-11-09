// z69 TWIST triage (I5): census of words (x,y,z), xyz - x - z = n, n <= N, by 2-adic pattern.
// counts[k][n] (uint16 saturating not needed for parity; use uint32)
// patterns: 0 all; 1 OOO; 2 x even; 3 8|xy (U7); 4 4|y; 5 8|y; 6 x even & xy==4 mod 8; 7 x even, xy==2 mod 4;
//           8 x<=z all ; 9 x<z & 4|y ; 10 x even & 8|xy & y odd ; 11 16|xy & x even
// usage: words N  -> prints table of parity statistics over classes of n
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define NP 12
int main(int argc,char**argv){
  long N=atol(argv[1]); uint32_t *c[NP]; for(int k=0;k<NP;k++) c[k]=calloc(N+1,4);
  for(long x=1;x<=N+2;x++) for(long y=1;;y++){
    long f=x*y-1; if(f<=0) continue;            // x=y=1: z*0 - 1 - ... n = -1-... skip
    // n = f*z - x >= 1 -> z >= (x+1)/f ; n<=N -> z <= (N+x)/f
    long zmax=(N+x)/f; if(zmax<1) break;
    long zmin=(x+1+f-1)/f; if(zmin<1) zmin=1;
    for(long z=zmin;z<=zmax;z++){ long n=f*z-x; if(n<1||n>N) continue;
      c[0][n]++; int xe=!(x&1), ze=!(z&1); long xy=x*y;
      if(!xe&&!ze) c[1][n]++;
      if(xe) c[2][n]++;
      if(xy%8==0) c[3][n]++;
      if(y%4==0) c[4][n]++;
      if(y%8==0) c[5][n]++;
      if(xe && xy%8==4) c[6][n]++;
      if(xe && xy%4==2) c[7][n]++;
      if(x<=z) c[8][n]++;
      if(x<z && y%4==0) c[9][n]++;
      if(xe && xy%8==0 && (y&1)) c[10][n]++;
      if(xe && xy%16==0) c[11][n]++;
    }
  }
  // classify n: prime / odd square / other, by n mod 8
  char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  const char *nm[NP]={"all","OOO","xeven","8|xy","4|y","8|y","xe,xy=4(8)","xe,xy=2(4)","x<=z","x<z,4|y","xe,8|xy,yodd","xe,16|xy"};
  for(int r=1;r<8;r+=2){
    printf("== n == %d (mod 8), n<=%ld\n",r,N);
    for(int k=0;k<NP;k++){
      long cnt[3][4]; memset(cnt,0,sizeof cnt); long zero[3]={0,0,0};
      for(long n=r;n<=N;n+=8){ if(n<3) continue; int t; long s=(long)(__builtin_sqrt((double)n)+0.5);
        if(!comp[n]) t=0; else if(s*s==n) t=1; else t=2;
        cnt[t][c[k][n]&3]++; if(c[k][n]==0) zero[t]++; }
      printf("%-13s prime mod4:[%ld %ld %ld %ld] zero=%ld | sq:[%ld %ld %ld %ld] zero=%ld | comp:[%ld %ld %ld %ld] zero=%ld\n",nm[k],
        cnt[0][0],cnt[0][1],cnt[0][2],cnt[0][3],zero[0],cnt[1][0],cnt[1][1],cnt[1][2],cnt[1][3],zero[1],cnt[2][0],cnt[2][1],cnt[2][2],cnt[2][3],zero[2]);
    }
  }
  if(argc>2){ FILE*f=fopen(argv[2],"w"); for(long n=1;n<=N;n+=8){ fprintf(f,"%ld",n); for(int k=0;k<NP;k++) fprintf(f," %u",c[k][n]); fprintf(f,"\n"); } fclose(f); }
  return 0;
}
