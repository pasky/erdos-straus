// Search for a p-free denominator z in (2t,p) shared by two signed vertices.
// By the reduction in WINDMILL.md §2.7 such a pair must be
//   (t+d, z, -pt)  and  (t+d+1, z, p*m2) positive,  z = t+u, u = t^2/d, d<t,
// with f = 3u-2t-d-1 > 0, f | (t+u)^2, f | (2t+d+u+1), H=(2t+d+u+1)/f >= 3.
// We scan ALL t <= T (not only t with 4t+1 prime) and, for hits, re-verify the
// positive vertex by exact rational arithmetic.  Prints hits and a summary.
#include <cstdio>
#include <cstdlib>
#include <vector>
typedef long long ll; typedef __int128 i128;
int main(int argc,char**argv){
  ll T=atoll(argv[1]);
  std::vector<int> spf(T+2,0);
  for(ll i=2;i<=T+1;i++) if(!spf[i]) for(ll j=i;j<=T+1;j+=i) if(!spf[j]) spf[j]=(int)i;
  ll cand=0,hits=0,hitsprime=0;
  for(ll t=1;t<=T;t++){
    std::vector<ll> divs{1}; ll m=t;
    while(m>1){ ll r=spf[m]; int e=0; while(m%r==0){m/=r;e++;} size_t n=divs.size(); ll pw=1;
      for(int k=1;k<=2*e;k++){ pw*=r; for(size_t i=0;i<n;i++){ i128 v=(i128)divs[i]*pw; if(v<(i128)t) divs.push_back((ll)v);} } }
    ll p=4*t+1;
    for(ll d:divs){ if(d>=t) continue; ll u=(ll)((i128)t*t/d);
      if(u-t > (d+1)/2) continue;           // needed for H>=3
      if(u>=3*t+1) continue;                 // z<p
      cand++;
      ll f=3*u-2*t-d-1; if(f<=0) continue;
      i128 z=t+u; ll s=2*t+d+u+1;
      if(((i128)z*z)%f) continue; if(s%f) continue; ll H=s/f; if(H<3) continue;
      // exact verification: 4/p - 1/(t+d+1) - 1/z = 1/(p*m2), m2>0 integer
      i128 x2=t+d+1; i128 num=4*x2*z - (i128)p*(z+x2); i128 den=(i128)p*x2*z; // R=num/den
      bool ok = num>0 && den%num==0 && (den/num)%p==0;
      hits++; bool pr=true; for(ll q=2;q*q<=p;q++) if(p%q==0){pr=false;break;}
      if(pr) hitsprime++;
      printf("HIT t=%lld p=%lld prime=%d p%%24=%lld d=%lld u=%lld f=%lld H=%lld verified=%d\n",t,p,(int)pr,p%24,d,u,f,H,(int)ok);
    }
  }
  printf("T=%lld candidates(d,u near t)=%lld hits=%lld hits_with_p_prime=%lld\n",T,cand,hits,hitsprime);
}
