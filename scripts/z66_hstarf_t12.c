// z66 HSTARF: Type I / Type II / (star) counts for primes p = 1 (mod 4).
//  Type II : 4abcd = a+b+pc  <=>  exists a,d>=1, q | 4a^2 d + p with q = -1 (mod 4ad)   (q = 4acd-1, WLOG a<=b <=> q <= sqrt)
//  (star)  : c = 1           <=>  4ad-1 | a+p
//  Type I  : p | exactly one denominator: t = -p (mod 4), X=(pt+1)/4, e | X^2, 4e = -1 (mod t)
// usage: ./t12 p1 p2 ...        -> per-prime counts (II, star, I)
//        ./t12 -range N         -> list primes p=1(4) <= N with Type II count 0 (and star count 0 separately)
//        ./t12 -range N -all    -> also test composites n = 1 (4) (Type II count 0)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef __int128 i128;

static int isprime(u64 n){ if(n<2) return 0; for(u64 d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }

// count Type II solutions (a,b,c,d) with a<=b (as a parametrised set), also count star (c=1)
static long count_t2(u64 p, long *star, int stop_first){
    // enumerate (a,d) with 4a^2 d <= p + 2a  (this is a<=b, since (4acd-1)^2 <= (4acd-1)(4bcd-1) = 4c^2 d p + 1),
    // then c with q = 4acd-1 <= N = 4a^2 d + p, test q | N.  Every Type II solution with a<=b is hit exactly once.
    long cnt=0; *star=0;
    // order: by m = a*d increasing (stop_first finds the smallest modulus n = 4ad first)
    for(u64 m=1; 4*m <= p + 2*m; m++){
        for(u64 a=1; a*a<=m; a++){ if(m%a) continue; for(int sw=0; sw<2; sw++){
            u64 aa = sw? m/a : a; u64 d = m/aa; if(sw && aa==a) continue;
            if(4*aa*aa*d > p + 2*aa) continue;
            u64 n=4*aa*d; u64 N=4*aa*aa*d+p;
            if(N/n > 2*(u64)sqrtl((long double)N)){
                // divisor enumeration by trial division (cheaper when the class is sparse)
                for(u64 r=1; r*r<=N; r++) if(N%r==0){
                    u64 r2=N/r;
                    if((r+1)%n==0){ cnt++; if(r==n-1) (*star)++; if(stop_first) return cnt; }
                    if(r2!=r && (r2+1)%n==0){ cnt++; if(r2==n-1) (*star)++; if(stop_first) return cnt; }
                }
            } else
            for(u64 q=n-1; q<=N; q+=n){
                if(N%q==0){ cnt++; if(q==n-1) (*star)++; if(stop_first) return cnt; }
            }
        }}
    }
    return cnt;
}
// Type I count (as pairs (t,e) with e<=X^2/e)
static long count_t1(u64 p, int stop_first){
    long cnt=0;
    // t = -p mod 4; X=(pt+1)/4; need e | X^2 with 4e = -1 (mod t), e <= X. y=(X+e)/t must be >= ... any
    // bound on t: y = (X+e)/t >= (X+1)/t, z=(X+f)/t; x = pX. For x<=y<=z not needed; count all. t up to? y>=1 always.
    // We need a finite enumeration: e | X^2, e<=X, 4e=-1 mod t => e >= (t-1)/4 ... e<=X=(pt+1)/4 always true. So t unbounded a priori;
    // but e | X^2 and e = (kt-1)/4; also f=X^2/e >= X => fine. Use bound t <= 4X ... circular. Restrict: in ES solution x=pX, y,z >= p/4 trivially;
    // Standard: Type I exists iff exists it with t | ... we cap t by 4p (empirical, flagged).
    for(u64 t=(4 - p%4)%4; t<=4*p; t+=4){
        if(t==0) continue;
        u64 X=(p*t+1)/4;
        // enumerate divisors e of X^2 with e <= X: e = g*h where ... do trial over divisors of X via factorization of X
        // factor X
        u64 x=X; u64 pr[64]; int ex[64]; int k=0;
        for(u64 d=2; d*d<=x; d++){ if(x%d==0){ pr[k]=d; ex[k]=0; while(x%d==0){x/=d; ex[k]++;} k++; } }
        if(x>1){ pr[k]=x; ex[k]=1; k++; }
        // divisors of X^2: exponents 0..2ex
        int idx[64]; memset(idx,0,sizeof(idx));
        while(1){
            i128 e=1; for(int i=0;i<k;i++){ for(int j=0;j<idx[i];j++) e*=pr[i]; }
            if(e<=X && ((4*e+1)%t)==0){ cnt++; if(stop_first) return cnt; }
            int i=0; while(i<k){ idx[i]++; if(idx[i]<=2*ex[i]) break; idx[i]=0; i++; } if(i==k) break;
        }
    }
    return cnt;
}
int main(int argc,char**argv){
    if(argc>=3 && !strcmp(argv[1],"-range")){
        u64 N=strtoull(argv[2],0,10); int all = (argc>=4 && !strcmp(argv[3],"-all"));
        long nz2=0,nz1=0,nzs=0,np=0;
        for(u64 n=5;n<=N;n+=4){
            int pr=isprime(n); if(!all && !pr) continue; np++;
            long st; long c2=count_t2(n,&st,1);
            if(c2==0){ nz2++; printf("TYPEII_ZERO %llu %s\n",n,pr?"P":"C"); }
            if(pr && st==0){ nzs++; } // (star count unreliable with stop_first)
            if(pr && c2==0){ long c1=count_t1(n,1); if(c1==0){ nz1++; printf("NO_TYPE_I_OR_II %llu\n",n);} }
        }
        printf("done N=%llu tested=%ld typeII_zero=%ld star_zero(primes)=%ld both_zero=%ld\n",N,np,nz2,nzs,nz1);
        return 0;
    }
    for(int i=1;i<argc;i++){ u64 p=strtoull(argv[i],0,10); long st; long c2=count_t2(p,&st,0); long c1=(p<20000)?count_t1(p,0):-1;
        printf("p=%llu prime=%d typeII=%ld star=%ld typeI=%ld\n",p,isprime(p),c2,st,c1); }
    return 0;
}
