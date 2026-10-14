// y1_three_squares: test the "three-squares genus" dictionary (O209, memo y1_three_squares_genus).
// For each word w=(t,u,v) of odd n (tuv-u-v=n), A=tu-1, A*=tv-1, chi=(-A/n) (Jacobi; CHI_FLIP normalisation, with
// the n0 convention of SIGN_IDENTITY Lemma 1.1 handled by computing Prod_{l|n}(-A/l)^{v_l} via jacobi(-A mod n, n)
// which is the same since gcd(A,n)=1).  LIFT(w) := exists x,y in Z^3 with x.x=A*, y.y=A, x.y=1.
// Claim tested (TWO_FIBRES Thm A): LIFT(w) <=> Diff(T_w)={2} (all odd eps_l=+1); for prime n this is chi(w)=+1.  Usage: y1_three_squares NMAX [sq|p [NMIN]]  (sq: odd squares only; p: primes only)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int jacobi(ll a, ll n){ a%=n; if(a<0)a+=n; int r=1; while(a){ while(a%2==0){a/=2; if(n%8==3||n%8==5) r=-r;} ll t=a;a=n;n=t; if(a%4==3&&n%4==3) r=-r; a%=n;} return n==1?r:0; }
static ll isq(ll x){ if(x<0) return -1; ll r=(ll)sqrtl((long double)x); while(r*r>x) r--; while((r+1)*(r+1)<=x) r++; return r; }
// exists x in Z^3: x.y=1, x.x=B, given y with y.y=A
static int solve_x(ll y1,ll y2,ll y3,ll B){
  // make y3 != 0 by permutation
  if(y3==0){ if(y2!=0){ ll t=y2;y2=y3;y3=t;} else { ll t=y1;y1=y3;y3=t;} }
  ll R=isq(B);
  for(ll x1=-R;x1<=R;x1++){
    ll rem=B-x1*x1; if(rem<0) continue;
    // x3 = (1 - x1 y1 - x2 y2)/y3 ; x2^2 + x3^2 = rem
    // y3^2 x2^2 + (c - x2 y2)^2 = rem y3^2, c = 1 - x1 y1
    ll c=1-x1*y1;
    // (y3^2+y2^2) x2^2 - 2 c y2 x2 + c^2 - rem y3^2 = 0
    ll a=y3*y3+y2*y2, b=-2*c*y2, cc=c*c-rem*y3*y3;
    ll D=b*b-4*a*cc; if(D<0) continue; ll s=isq(D); if(s*s!=D) continue;
    for(int sg=-1;sg<=1;sg+=2){ ll num=-b+sg*s; if(num%(2*a)) continue; ll x2=num/(2*a);
      ll q=c-x2*y2; if(q%y3) continue; return 1; }
  }
  return 0;
}
static ll Tt; static ll cnt_all, cnt_cong;
static void count_x(ll y1,ll y2,ll y3,ll B, int swapped){
  // enumerate all x with x.y=1, x.x=B (naive over x1,x2), record congruence
  ll R=isq(B);
  for(ll x1=-R;x1<=R;x1++) for(ll x2=-R;x2<=R;x2++){ ll r=B-x1*x1-x2*x2; if(r<0) continue; ll x3=isq(r); if(x3*x3!=r) continue;
    for(int s=-1;s<=1;s+=2){ if(x3==0&&s==1) continue; ll X3=s*x3; if(x1*y1+x2*y2+X3*y3!=1) continue;
      cnt_all++;
      // i = vector of norm A* , j = vector of norm A ; if swapped, x has norm A ... keep (i,j)=(normA*,normA)
      ll i1,i2,i3,j1,j2,j3; if(!swapped){ i1=x1;i2=x2;i3=X3; j1=y1;j2=y2;j3=y3;} else { i1=y1;i2=y2;i3=y3; j1=x1;j2=x2;j3=X3; }
      // z = i x j
      ll z1=i2*j3-i3*j2, z2=i3*j1-i1*j3, z3=i1*j2-i2*j1;
      if(((z1-i1-j1)%Tt==0)&&((z2-i2-j2)%Tt==0)&&((z3-i3-j3)%Tt==0)) cnt_cong++; } }
}
static void countlift(ll A, ll As){
  cnt_all=cnt_cong=0; ll a=A<As?A:As, b=A<As?As:A; int swapped=(A>As); // y has norm a; i must have norm As
  // if A<=As: y norm A (=j), x norm As (=i): swapped=0. else y norm As (=i), x norm A (=j): swapped=1
  ll R=isq(a);
  for(ll y1=-R;y1<=R;y1++) for(ll y2=-R;y2<=R;y2++){ ll r=a-y1*y1-y2*y2; if(r<0) continue; ll y3=isq(r); if(y3*y3!=r) continue;
    for(int s=-1;s<=1;s+=2){ if(y3==0&&s==1) continue; count_x(y1,y2,s*y3,b,swapped);} }
}
static int lift(ll A, ll As){
  // enumerate y with y.y = min(A,As) (symmetric roles), then x with x.x = the other
  ll a=A<As?A:As, b=A<As?As:A; ll R=isq(a);
  for(ll y1=0;y1<=R;y1++) for(ll y2=-R;y2<=R;y2++){ ll r=a-y1*y1-y2*y2; if(r<0) continue; ll y3=isq(r); if(y3*y3!=r) continue;
    for(int s=-1;s<=1;s+=2){ if(y3==0&&s==1) continue; if(solve_x(y1,y2,s*y3,b)) return 1; } }
  return 0;
}
static ll NMIN=0; static ll hist[20],histc[20],dbad=0;
int main(int argc,char**argv){
  ll N=atoll(argv[1]); int sq=argc>2?(argv[2][0]=='p'?2:1):0; NMIN=argc>3?atoll(argv[3]):0;
  ll words=0,bad=0,np=0,nm=0,liftm=0,nolift_p=0;
  for(ll n=1;n<=N;n+=2){
    if(sq==1){ ll r=isq(n); if(r*r!=n) continue; }
    if(sq==2){ int pr=n>2; for(ll d=3;d*d<=n;d+=2) if(n%d==0){pr=0;break;} if(!pr) continue; if(n<NMIN) continue; }
    for(ll t=1;t<=n+2;t++){ ll M=t*n+1;
      for(ll A=t-1;A*A<=M || 1;A+=t){ if(A<1) continue; if(A>M) break; if(M%A) continue; ll As=M/A; if((As+1)%t) continue;
        ll u=(A+1)/t, v=(As+1)/t; if(t*u*v-u-v!=n) continue;
        int chi=jacobi(-A,n); int L=lift(A,As); words++;
        if(getenv("CNT") && L){ Tt=t; countlift(A,As); if(cnt_cong==0) printf("NO-CONG n=%lld w=(%lld,%lld,%lld) all=%lld\n",n,t,u,v,cnt_all); hist[cnt_all/48<20?cnt_all/48:19]++; histc[cnt_cong/48<20?cnt_cong/48:19]++; if(cnt_all%48||cnt_cong%48) printf("non48 n=%lld w=(%lld,%lld,%lld) all=%lld cong=%lld\n",n,t,u,v,cnt_all,cnt_cong);}
        { int odd_ok=1; ll m=n; for(ll l=3;l*l<=m;l+=2){ if(m%l==0){ int e=0; while(m%l==0){m/=l;e++;} if(e%2 && jacobi(-A,l)==-1) odd_ok=0; } } if(m>1 && jacobi(-A,m)==-1) odd_ok=0; if(odd_ok!=L){ dbad++; if(dbad<5) printf("DIFF-MISMATCH n=%lld w=(%lld,%lld,%lld)\n",n,t,u,v);} }
        if(chi==1) np++; else nm++;
        if(chi==-1&&L){ liftm++; bad++; if(bad<10) printf("chi=-1 but lifts: n=%lld w=(%lld,%lld,%lld)\n",n,t,u,v);} 
        if(chi==1&&!L){ nolift_p++; bad++; if(bad<0) printf("chi=+1 no lift: n=%lld w=(%lld,%lld,%lld) A=%lld A*=%lld\n",n,t,u,v,A,As);} 
      } }
  }
  printf("Diff={2}<=>lift mismatches: %lld\n",dbad); if(getenv("CNT")){ printf("hist r/48:"); for(int i=0;i<20;i++) printf(" %lld",hist[i]); printf("\nhist cong/48:"); for(int i=0;i<20;i++) printf(" %lld",histc[i]); printf("\n"); }
  printf("N=%lld squares_only=%d words=%lld chi+=%lld chi-=%lld | chi-&lift=%lld chi+&nolift=%lld\n",N,sq,words,np,nm,liftm,nolift_p);
  return 0;
}
