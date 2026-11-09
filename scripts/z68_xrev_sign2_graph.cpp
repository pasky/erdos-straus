// Independent delta-review checker: streaming HJ enumeration, rebuilt moves,
// BFS components/reverse descent, dynamic greedy endpoints, bottleneck Dijkstra.
// O(n + edges) storage; no Cartesian products or retained word collection.
#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>
using namespace std;
using I = long long;
vector<I> hj(I n, I a) {
    vector<I> w;
    while (a) { I b=(n+a-1)/a; w.push_back(b); I t=b*a-n; n=a; a=t; }
    return w;
}
I cont(const vector<I>& w, size_t start=0) {
    I prev=0, cur=1;
    for (size_t i=start;i<w.size();++i) { I next=w[i]*cur-prev; prev=cur; cur=next; }
    return cur;
}
int jac(I a,I n) {
    int s=1; a%=n;
    while(a) {
        while(a%2==0) { a/=2; if(n%8==3 || n%8==5) s=-s; }
        swap(a,n); if(a%4==3 && n%4==3) s=-s; a%=n;
    }
    return n==1?s:0;
}
I inverse(I a,I n) {
    I b=n,x=1,y=0;
    while(b) { I q=a/b; I t=a-q*b; a=b;b=t;t=x-q*y;x=y;y=t; }
    assert(a==1); return (x%n+n)%n;
}
struct Edge { int b,s; };
void run(int n) {
    assert(n>=9 && n<=1000000 && n%4==1);
    vector<vector<Edge>> adj(n);
    vector<int> len(n),sg(n),vertices,starts,targets;
    I moves=0;
    for(int a=1;a<n;++a) {
        if(gcd(a,n)!=1) continue;
        auto w=hj(n,a); int r=w.size(); len[a]=r; sg[a]=jac(a,n); vertices.push_back(a);
        if(r==3 && sg[a]==-1) targets.push_back(a);
        if(r>=6 && sg[a]==-1 && *max_element(w.begin(),w.end())<=4) starts.push_back(a);
        vector<I> pre(r+1,1),suf(r+2); suf[r]=1;
        for(int j=0;j<r;++j) pre[j+1]=w[j]*pre[j]-(j?pre[j-1]:0);
        for(int j=r-1;j>=0;--j) suf[j]=w[j]*suf[j+1]-suf[j+2];
        for(int j=0;j<r;++j) {
            I b=w[j],x=pre[j],xp=j?pre[j-1]:0,y=suf[j+1],yp=suf[j+2];
            assert(b*x*y-x*yp-xp*y==n);
            vector<I> divs;
            for(I d=1;d*d<=b;++d) if(b%d==0) {
                if(d>=2 && b/d>=2) divs.push_back(d);
                I k=b/d; if(k!=d && k>=2 && b/k>=2) divs.push_back(k);
            }
            for(I k:divs) for(int left=0;left<2;++left) {
                if(!left && !(xp>=1 && yp%k==0 && gcd(k,xp)==1)) continue;
                if(left && !(yp>=1 && xp%k==0 && gcd(k,yp)==1)) continue;
                assert(gcd(k,I(n))==1);
                auto l=hj(left?x:k*x,left?xp/k:xp);
                reverse(l.begin(),l.end()); l.push_back(b/k);
                auto tail=hj(left?k*y:y,left?yp:yp/k);
                l.insert(l.end(),tail.begin(),tail.end());
                assert(cont(l)==n); int dst=cont(l,1);
                assert(dst>0 && dst<n && hj(n,dst)==l);
                assert(dst==(left ? I(a)*k%n : I(a)*inverse(k,n)%n));
                int sign=jac(k,n); assert(jac(dst,n)==sg[a]*sign);
                adj[a].push_back({dst,sign}); adj[dst].push_back({a,sign}); ++moves;
            }
        }
    }
    int s1=1,s2=0;
    for(int a:vertices) if(sg[a]==-1) {s1=a;break;}
    for(int a:vertices) if(sg[a]==-1 && len[a]>=4 && (!s2 || len[a]<len[s2])) s2=a;
    vector<int> order=vertices;
    sort(order.begin(),order.end(),[&](int a,int b){return pair(len[a],a)<pair(len[b],b);});
    vector<vector<int>> ends(2,vector<int>(n)),D(2,vector<int>(n));
    vector<vector<int>> heights(2,vector<int>(n,-1)),comp(2,vector<int>(n,-1));
    int giants[2]={0,0},ncomp[2]={0,0};
    for(int plus=0;plus<2;++plus) {
        // Directed reverse reachability from good L3, strictly uphill.
        queue<int> q;
        for(int a:targets) { D[plus][a]=1; q.push(a); }
        while(!q.empty()) {
            int a=q.front();q.pop();
            for(auto [b,s]:adj[a]) if((!plus || s==1) && len[b]>len[a] && !D[plus][b]) {
                D[plus][b]=1;q.push(b);
            }
        }
        for(int a:order) {
            int best=a;
            for(auto [b,s]:adj[a]) if((!plus || s==1) && len[b]<len[a] && pair(len[b],b)<pair(len[best],best)) best=b;
            ends[plus][a]=(best==a?a:ends[plus][best]);
        }
        for(int root:vertices) if(comp[plus][root]<0) {
            int count=0;comp[plus][root]=root;q.push(root);++ncomp[plus];
            while(!q.empty()) {
                int a=q.front();q.pop();++count;
                for(auto [b,s]:adj[a]) if((!plus || s==1) && comp[plus][b]<0) {comp[plus][b]=root;q.push(b);}
            }
            giants[plus]=max(giants[plus],count);
        }
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> heap;
        for(int a:targets) {heights[plus][a]=3;heap.push({3,a});}
        while(!heap.empty()) {
            auto [h,a]=heap.top();heap.pop(); if(h!=heights[plus][a]) continue;
            for(auto [b,s]:adj[a]) if(!plus || s==1) {
                int nh=max(h,len[b]);
                if(heights[plus][b]<0 || nh<heights[plus][b]) {heights[plus][b]=nh;heap.push({nh,b});}
            }
        }
    }
    auto success=[&](int a,int pl){int e=ends[pl][a];return len[e]==3 && sg[e]==-1;};
    int ng=0,nd=0,ndp=0,sr=0,srp=0,sd=0,sdp=0;
    for(int a:vertices) if(len[a]>=4 && sg[a]==-1) {++ng;nd+=D[0][a];ndp+=D[1][a];}
    for(int a:starts) {sr+=success(a,0);srp+=success(a,1);sd+=D[0][a];sdp+=D[1][a];}
    cout<<"n="<<n<<" COUNTS goodlen4="<<ng<<" inD="<<nd<<" inDp="<<ndp
        <<" S3n="<<starts.size()<<" S3Rmin="<<sr<<" S3Rminp="<<srp<<" S3D="<<sd<<" S3Dp="<<sdp
        <<" S3anyRmin="<<(sr>0)<<" S3anyD="<<(sd>0)<<" S1len="<<len[s1]<<" S1good="<<(sg[s1]==-1)
        <<" S1Rmin="<<success(s1,0)<<" S1Rminp="<<success(s1,1)<<" S1D="<<D[0][s1]<<" S1Dp="<<D[1][s1]
        <<" S2A="<<(s2?s2:-1)<<" S2Rmin="<<success(s2,0)<<" S2Rminp="<<success(s2,1)<<" S2D="<<D[0][s2]<<" S2Dp="<<D[1][s2]
        <<" moves="<<moves<<" V="<<vertices.size()<<'\n';
    cout<<"n="<<n<<" CHECK giant="<<giants[0]<<" giantp="<<giants[1]<<" comps="<<ncomp[0]<<" compsp="<<ncomp[1]
        <<" h1="<<heights[0][s1]<<" h1p="<<heights[1][s1]<<" h2="<<heights[0][s2]<<" h2p="<<heights[1][s2]
        <<" S1="<<s1<<" end1="<<ends[0][s1]<<" end2="<<ends[0][s2]<<" L3="<<count(len.begin(),len.end(),3)<<" goodL3="<<targets.size()
        <<" size1="<<count(comp[0].begin(),comp[0].end(),comp[0][s1])
        <<" size2="<<(s2?count(comp[0].begin(),comp[0].end(),comp[0][s2]):0)<<'\n';
    if(n==409 || n==21841 || n==881) {
        cout<<"n="<<n<<" TARGETS";
        for(int a:targets) cout<<" "<<a<<":"<<(comp[0][a]==comp[0][s2]);
        cout<<"\n";
        if(n==409) { cout<<"n=409 S2COMP"; for(int a:vertices) if(comp[0][a]==comp[0][s2]) cout<<" "<<a;cout<<"\n"; }
        if(n==881) {
            assert(s2==12 && D[0][s2]==0 && heights[0][s2]==4);
            for(auto [a,b]:vector<pair<int,int>>{{12,444},{444,111}}) {
                assert(sg[a]==-1 && sg[b]==-1);
                assert(any_of(adj[a].begin(),adj[a].end(),[&](Edge e){return e.b==b && e.s==1;}));
            }
        }
    }
}
int main(int argc,char** argv) { for(int i=1;i<argc;++i) run(stoi(argv[i])); }
