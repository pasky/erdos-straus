/* R89 from-scratch height-bounded near-miss enumerator at levels L = al+2ga (independent of typei3_nmdump.c).
   Near miss (TYPEI2 §5 / TYPEI4 L1.1): v_7(c)=a odd, F | N = 1+4ck^2, F = -1 mod c'k', F = 1 mod 7^{a+b}.
   For each slice with ck <= X and level L in [Lmin,Lmax] we list the divisors D <= sqrt(N), D != N/D, in the
   class D = -1 (c'k'), 1 (7^{a+b}), D = r16 (mod 16), for r16 in {7,15} (both members of a near-miss pair lie in
   the same odd class; mod 16, a pair with F = 7 has e = 7 too, Lemma 1.1(ii)).
   Output: counts per (L, D mod 16), and every D = 7 mod 16 hit (= fibre certificate).
   Usage: review_typei4_nm X Lmin Lmax */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned __int128 u128; typedef long long i64; typedef unsigned long long u64;
static i64 egcd_inv(i64 a,i64 m){ i64 g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; i64 b=a1; /* inverse of a mod m */
  i64 r0=m,r1=b,s0=0,s1=1; while(r1){ i64 q=r0/r1,t=r0-q*r1; r0=r1;r1=t; t=s0-q*s1; s0=s1; s1=t; } (void)g;(void)x;(void)x1;
  if(r0!=1) return -1; s0%=m; if(s0<0)s0+=m; return s0; }
static u64 isqrt128(u128 n){ u64 x=(u64)sqrtl((long double)n); while((u128)x*x>n)x--; while((u128)(x+1)*(x+1)<=n)x++; return x; }
int main(int argc,char**argv){
  i64 X=atoll(argv[1]); int Lmin=atoi(argv[2]), Lmax=atoi(argv[3]);
  long long cnt[40][2]={{0}}; long long slices=0;
  for(int L=Lmin; L<=Lmax; L++)
  for(int ga=0; 2*ga<=L; ga++){ int al=L-2*ga; i64 two=1LL<<(al+ga); if(two*7>X) continue;
   for(int a=1;;a+=2){ i64 p7a=1; for(int i=0;i<a;i++) p7a*=7; if(two*p7a>X) break;
    for(int b=0;;b++){ i64 p7b=1; for(int i=0;i<b;i++) p7b*=7; if(two*p7a*p7b>X) break;
     i64 rest=X/(two*p7a*p7b);   /* c'k' <= rest */
     for(i64 c=1;c<=rest;c+=2){ if(c%7==0) continue;
      for(i64 k=1;c*k<=rest;k+=2){ if(k%7==0) continue; slices++;
        i64 mp=c*k, V=p7a*p7b; i64 Mod=16*mp*V;
        /* N = 1 + 2^{L+2} c' 7^{a+2b} k'^2 */
        u128 N=1+((u128)1<<(L+2))*(u128)c*(u128)p7a*(u128)p7b*(u128)p7b*(u128)k*(u128)k;
        u64 sq=isqrt128(N);
        for(int ri=0;ri<2;ri++){ i64 r16= ri?15:7;
          /* CRT: x = -1 mod mp, 1 mod V, r16 mod 16 (pairwise coprime moduli) */
          i64 m1=mp, m2=V*16; i64 x2; /* solve mod V*16 first */
          { i64 inv=egcd_inv(16%V==0?16:16,V); i64 t=((1-r16)%V+V)%V; t=(i64)((u128)t*inv%V); x2=r16+16*t; }
          i64 inv=egcd_inv(m1%m2,m2); i64 t=((x2-(m1-1))%m2+m2)%m2; t=(i64)((u128)t*inv%m2);
          u128 xi=(u128)(m1-1)+(u128)m1*t; /* = -1 mod m1, = x2 mod m2 */
          for(u128 D=xi; D<=sq; D+=Mod){ if(D<2) continue; if(N%D) continue; if(D*D==N) continue;
            cnt[L][ri]++;
            if(ri==0){ u128 e=N/D; printf("FIBRE L=%d al=%d ga=%d a=%d b=%d c'=%lld k'=%lld F=%llu e=",L,al,ga,a,b,c,k,(u64)D);
              char bf[64]; int i=63; bf[i]=0; while(e){bf[--i]='0'+(int)(e%10); e/=10;} printf("%s\n",bf+i); }
          }
        }
      }
     }
    }
   }
  }
  printf("slices=%lld\n",slices);
  for(int L=Lmin;L<=Lmax;L++) printf("L=%d  D=7(16): %lld   D=15(16): %lld\n",L,cnt[L][0],cnt[L][1]);
  return 0;
}
