/* R249 from-scratch box enumerator for the r-generic line (P and Q types, M17 Lemma 1.1 with r for 17).
 * Usage: review_r249_rbox r Lmax   -> prints "P L residue" and "Q k residue" lines (residues mod r^L / r^k)
 * P (level L, K = 2L-1, N = r^K): N-points (a,b,c,d) of Sigma^II_N: 4abcd = a+b+Nc, r !| cd.
 *   Scan a <= b, ab <= N/2 (from abd <= N/2): 4abd = N + e with 1 <= e <= a+b < 4ab, so e = (-N) mod 4ab;
 *   need e | a+b, c = (a+b)/e, d = (N+e)/(4ab). Boxes -(4acd-1), -(4bcd-1) mod r^L (both orientations).
 * Q (level k odd, F = r^k): N-points of Sigma^I_F with r !| e: 4abd = Fe + 1, e | a+b (equivalently e | 4a^2 d + 1).
 *   With a <= b: ad <= F/2 + 1/4. For each (a,d), e (resp. f = (4a^2d+1)/e) runs over the class -F^{-1} (resp. -F)
 *   mod 4ad up to sqrt(4a^2 d + 1). Boxes -4a^2 d, -4b^2 d mod F.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __int128 i128;
static u64 ipow(u64 r, int k){u64 x=1; while(k--) x*=r; return x;}
static long long inv_mod(long long a, long long m){ long long g=m, x=0, x1=1, a1=a%m; if(a1<0)a1+=m;
  long long b=a1; long long old_r=b, rr=m, old_s=1, s=0; while(rr){ long long q=old_r/rr, t=old_r-q*rr; old_r=rr; rr=t; t=old_s-q*s; old_s=s; s=t;}
  (void)g;(void)x;(void)x1; if(old_r!=1) return -1; old_s%=m; if(old_s<0) old_s+=m; return old_s; }
static u64 negmod(i128 x, u64 M){ i128 y = (-x) % (i128)M; if (y<0) y+=M; return (u64)y; }
int main(int argc, char**argv){
  u64 r = strtoull(argv[1],0,10); int Lmax = atoi(argv[2]);
  for(int L=1; L<=Lmax; L++){
    int K = 2*L-1; u64 N = ipow(r,K), W = ipow(r,L); u64 cnt=0;
    for(u64 a=1; a*a <= N/2; a++){
      for(u64 b=a; a*b <= N/2; b++){
        u64 m = 4*a*b; u64 e = (m - N % m) % m; if(e==0 || e > a+b) continue;
        if((a+b)%e) continue; u64 c=(a+b)/e; u64 d=(N+e)/m;
        if(c%r==0 || d%r==0) continue;
        /* verify */ if((i128)4*a*b*c*d != (i128)a+b+(i128)N*c){ fprintf(stderr,"bad P\n"); return 1; }
        printf("P %d %llu %llu %llu %llu %llu\n", L, negmod((i128)4*a*c*d-1, W), a,b,c,d);
        printf("P %d %llu %llu %llu %llu %llu\n", L, negmod((i128)4*b*c*d-1, W), b,a,c,d);
        cnt++;
      }
    }
    fprintf(stderr,"r=%llu L=%d P-data(a<=b)=%llu\n", r, L, cnt);
  }
  for(int k=1; k<=Lmax; k+=2){
    u64 F = ipow(r,k); u64 cnt=0;
    for(u64 a=1; a <= F/2+1; a++){ if(a%r==0) continue;
      for(u64 d=1; a*d <= F/2+1; d++){ if(d%r==0) continue;
        u64 m=4*a*d; u64 X = 4*a*a*d+1; long long Fi = inv_mod((long long)(F%m),(long long)m); if(Fi<0) continue;
        u64 e0 = (m - (u64)Fi)%m; u64 f0 = (m - F%m)%m; u64 es[4096]; int ne=0;
        for(u64 e=(e0?e0:m); (i128)e*e <= X; e+=m) if(X%e==0) es[ne++]=e;
        for(u64 f=(f0?f0:m); (i128)f*f <= X; f+=m) if(X%f==0) es[ne++]=X/f;
        for(int i=0;i<ne;i++){ u64 e=es[i]; int dup=0; for(int j=0;j<i;j++) if(es[j]==e) dup=1; if(dup) continue;
          if(e%r==0) continue; i128 num=(i128)F*e+1; if(num % m) continue; u64 b=(u64)(num/m);
          if((a+b)%e) { fprintf(stderr,"bad Q\n"); return 1; }
          u64 c=(a+b)/e;
          if((i128)4*a*b*c*d != (i128)F*(a+b)+c){ fprintf(stderr,"bad Q eq\n"); return 1; }
          printf("Q %d %llu %llu %llu %llu %llu\n", k, negmod((i128)4*a*a*d, F), a,b,c,d);
          printf("Q %d %llu %llu %llu %llu %llu\n", k, negmod((i128)4*b*b*d, F), a,b,c,d);
          cnt++; }
      }
    }
    fprintf(stderr,"r=%llu k=%d Q-data=%llu\n", r, k, cnt);
  }
  return 0;
}
