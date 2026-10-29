// Independent full-range recomputation of cap histograms: reachable-set iteration over e
// (no minimax DP), trial-division factoring, Jacobi-based q3.
#include <bits/stdc++.h>
using namespace std; typedef long long ll;
vector<int> P;
vector<pair<ll,int>> fac(ll n){ vector<pair<ll,int>> f; for(int p:P){ if((ll)p*p>n)break; if(n%p==0){int b=0; while(n%p==0){n/=p;b++;} f.push_back({p,b});}} if(n>1)f.push_back({n,1}); return f;}
int jac(ll a,ll n){int t=1;a%=n;while(a){while(a%2==0){a/=2;ll r=n%8;if(r==3||r==5)t=-t;}swap(a,n);if(a%4==3&&n%4==3)t=-t;a%=n;}return n==1?t:0;}
ll pw(ll a,ll b,ll m){ll r=1;a%=m;while(b){if(b&1)r=r*a%m;a=a*a%m;b>>=1;}return r;}
// reachable residues of prod s^{delta}, delta in [-b,b] U {b+2h: 1<=h<=e} (odd s), [-b,b] (s=2)
vector<char> reach(const vector<pair<ll,int>>& f,int m,int e){
  vector<char> R(m,0); R[1%m]=1;
  for(auto [s,b]:f){
    // Inverse of s modulo composite m by extended Euclid.
    ll inv=0; { ll a=s%m, g=m, x0=1,x1=0, aa=a, gg=g; while(gg){ll qq=aa/gg; ll t=aa-qq*gg; aa=gg; gg=t; t=x0-qq*x1; x0=x1; x1=t;} inv=((x0%m)+m)%m; }
    set<ll> o; for(int d=-b; d<=b; d++) o.insert(d>=0?pw(s,d,m):pw(inv,-d,m));
    if(s!=2) for(int h=1;h<=e;h++) o.insert(pw(s,b+2*h,m));
    vector<char> NR(m,0); for(int u=0;u<m;u++) if(R[u]) for(ll v:o) NR[(ll)u*v%m]=1; R.swap(NR);}
  return R;
}
int main(int argc,char**argv){
  if(argc!=2) return 2;
  ll N=atoll(argv[1]); if(N<10000 || N>100000000) return 2;
  vector<char> c(N+1,0);
  for(ll i=2;i*i<=N;i++) if(!c[i]) for(ll j=i*i;j<=N;j+=i) c[j]=1;
  for(int i=2;i<=6000;i++) if(!c[i]) P.push_back(i);
  map<int,ll> hq,hc,hf,he,hw; ll cnt=0;
  for(ll p=17;p<=N;p+=8) if(!c[p]){ cnt++;
    int q=3; while(true){ if(!c[q] && jac(q,p)==-1) break; q+=4; }
    ll K=(p+q)/4; auto f=fac(K);
    int e1=INT_MAX; for(auto [s,b]:f) if(s!=2 && b%2 && jac(s,q)==-1){ int j=1; while(pw(s,j,q)!=q-1) j++; e1=min(e1,max(0,(j-b)/2)); }
    if(e1==INT_MAX){printf("NOONE %lld\n",p);return 1;}
    int tc=-1, fc=-1; ll pinv=pw(p,q-2,q);
    for(int e=0;e<=e1 && (tc<0||fc<0);e++){ auto R=reach(f,q,e);
      if(tc<0 && R[q-1]) tc=e;
      if(fc<0 && (R[q-1]||R[(q-p%q)%q]||R[(q-pinv)%q])) fc=e; }
    if(tc<0||fc<0){printf("NOCAP %lld\n",p);return 1;}
    int win=0; for(int m=3;m<=255;m+=4){ if(__gcd((ll)m,p)!=1) continue; ll Km=(p+m)/4; auto R=reach(fac(Km),m,0); if(R[m-1]){win=m;break;} }
    hq[q]++; hc[tc]++; hf[fc]++; he[e1]++; hw[win]++; }
  printf("count %lld\n",cnt);
  for(auto* h: {&hq,&hc,&hf,&he,&hw}){ for(auto [k,v]:*h) printf("%d:%lld ",k,v); printf("\n"); }
}
