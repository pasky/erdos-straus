/* R89 from-scratch complete search for fibre certificates at level L with v_7(k)=b (all a odd, all heights).
   Written independently of scripts/typei4_*.c, from TYPEI2 Lemma 2.4 (2.1) coordinates:
     F = c'k'J - 1, e = c'k'J' - 1, c'JJ' - u = Lam := 2^{L+2} 7^{a+2b}, J+J' = k'u.
   Fibre (F = 7 mod 16, oriented F<e) => J'-J = 16 V delta, V = 7^{a+b}, delta odd >= 1.
   Put m = c'J delta, R = 2^{L-2} 7^b.  Then (reviewer's derivation, see review file):
     u = c'J^2 + 16V(m-R),   u (F-1) = 16V(2R-m)   [F-1 = c'k'J-2]
   so  m < 2R,  m != R (L>=7),  and 16V < R^2.  Enumerate all (delta odd, c' odd 7-free, J>=1) with
   c'J delta < 2R and all odd a with 16*7^{a+b} < R^2; recover F from u | 16V(2R-m), then check everything
   against the definition (N % F == 0, congruences, F = 7 mod 16, Sigma = k'u).
   Output per hit: L a b c' k' F e delta v2(F+9) v2(e+9).
   Usage: review_typei4_jsearch L b */
#include <stdio.h>
#include <stdlib.h>
typedef __int128 i128; typedef long long i64;
static int v2(i128 x){ if(x<0)x=-x; int e=0; while(x>0 && !(x&1)){x>>=1;e++;} return e; }
static void p(i128 x){ char b[64]; int i=63; b[i]=0; int neg=x<0; if(neg)x=-x; if(!x){printf("0");return;}
  while(x){b[--i]='0'+(int)(x%10); x/=10;} if(neg) b[--i]='-'; printf("%s",b+i); }
int main(int argc,char**argv){
  int L=atoi(argv[1]), b=atoi(argv[2]);
  if(L<7){fprintf(stderr,"L>=7 only\n");return 2;}
  i64 p7b=1; for(int i=0;i<b;i++) p7b*=7;
  i64 R=(1LL<<(L-2))*p7b;
  i128 R2=(i128)R*R;
  int amax=-1; i128 Vs[64]; int as[64]; int na=0;
  for(int a=1;;a+=2){ i128 V=1; for(int i=0;i<a+b;i++) V*=7; if(16*V>=R2) break; Vs[na]=V; as[na]=a; na++; amax=a; }
  long long hits=0, triples=0;
  for(i64 delta=1; delta<2*R; delta+=2)
   for(i64 c=1; c*delta<2*R; c+=2){ if(c%7==0) continue;
    for(i64 J=1; c*J*delta<2*R; J++){
      i64 m=c*J*delta; if(m==R) continue; triples++;
      for(int ia=0; ia<na; ia++){
        i128 V=Vs[ia]; int a=as[ia];
        i128 u=(i128)c*J*J + 16*V*((i128)m-R);
        if(u<1) continue;
        i128 W=16*V*((i128)2*R-m);
        if(W%u) continue;
        i128 F=W/u+1;
        if(F%16!=7) continue;
        if((F+1)%((i128)c*J)) continue;
        i128 kp=(F+1)/((i128)c*J);
        if(kp%2==0 || kp%7==0) continue;
        if((i128)2*J+16*V*delta != kp*u) continue;
        if((F-1)%V) continue;
        /* e from (2.1); the definition (F*e == N, congruences) is re-checked with big ints in
           review_typei4_verify.py, since N can exceed 128 bits */
        i128 e=(i128)c*kp*((i128)J+16*V*delta)-1;
        int ok = e%16==7 && (e+1)%((i128)c*kp)==0 && (e-1)%V==0;
        if(!ok){ printf("BUG check L=%d a=%d\n",L,a); continue; }
        hits++;
        printf("HIT L=%d a=%d b=%d c'=%lld k'=",L,a,b,c); p(kp); printf(" F="); p(F); printf(" e="); p(e);
        printf(" delta=%lld v2F9=%d v2e9=%d\n",delta,v2(F+9),v2(e+9));
      }
    }
   }
  printf("DONE L=%d b=%d amax=%d triples=%lld hits=%lld\n",L,b,amax,triples,hits);
  return 0;
}
