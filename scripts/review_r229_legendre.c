/* R229 from-scratch recomputation of z1_legendre_levels EVIDENCE.
   mode 0: primes p = 1 mod 4 below N: report primes with no word (t,u,v) at any Legendre level t <= p+2
           (tp = 4^a(8b+7)); word at level t <=> tp+1 = A*A', A = A' = -1 mod t, A,A' >= t-1.
           Also counts primes where no Legendre-level word with t <= TL has 8 | some pentagon entry.
   mode 1: odd squares n = m^2 <= N, levels t <= TL: count words at Legendre levels (must be 0).
   usage: review_r229_legendre N TL mode */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
static int legendre_level(u64 x){ while(x%4==0) x/=4; return x%8==7; }
/* returns 1 if level t carries a word; if want8, sets *has8 when some word at this level has 8 | entry */
static int level_words(u64 t, u64 n, int want8, int *has8){
  u64 N = t*n+1; int found=0;
  for(u64 u=1;;u++){
    u64 A = t*u-1; if(A==0) continue;
    if(A*A > N) break;
    if(N%A) continue;
    u64 As = N/A; if((As+1)%t) continue;
    u64 v=(As+1)/t; found=1;
    if(!want8) return 1;
    if(t%8==0||u%8==0||v%8==0||A%8==0||As%8==0){*has8=1; return 1;}
  }
  return found;
}
int main(int argc,char**argv){
  u64 NN=strtoull(argv[1],0,10), TL=strtoull(argv[2],0,10); int mode=atoi(argv[3]);
  if(mode==0){
    char*sv=calloc(NN+1,1); for(u64 i=2;i*i<=NN;i++) if(!sv[i]) for(u64 j=i*i;j<=NN;j+=i) sv[j]=1;
    long np=0,fail=0,fail8=0; u64 maxleast=0,argmax=0;
    for(u64 p=5;p<=NN;p+=4){ if(sv[p]) continue; np++;
      u64 least=0;
      for(u64 t=1;t<=p+2;t++){ if(!legendre_level(t*p)) continue;
        int h=0; if(level_words(t,p,0,&h)){least=t;break;} }
      if(!least){fail++; printf("FAIL %llu\n",p);} else if(least>maxleast){maxleast=least;argmax=p;}
      int ok8=0; for(u64 t=1;t<=TL && !ok8;t++){ if(!legendre_level(t*p)) continue; int h=0; level_words(t,p,1,&h); if(h) ok8=1; }
      if(!ok8) fail8++;
    }
    printf("primes p=1 mod 4 <= %llu: %ld; no Legendre-level word: %ld; max least level %llu at p=%llu; no 8-word at levels<=%llu: %ld\n",NN,np,fail,maxleast,argmax,TL,fail8);
  } else {
    long words=0,sq=0;
    for(u64 m=3;m*m<=NN;m+=2){ u64 n=m*m; sq++;
      for(u64 t=1;t<=TL;t++){ if(!legendre_level(t*n)) continue; int h=0; if(level_words(t,n,0,&h)) words++; } }
    printf("odd squares 9..%llu: %ld squares, Legendre-level words at levels <= %llu: %ld\n",NN,sq,TL,words);
  }
  return 0;
}
