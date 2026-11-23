/* Read horder.txt on stdin. For each unresolved odd-order p=17 mod24,
   recursively split *starting positions* whose next doubling stays high.
   Keep only an interval and its affine image (slope 2^j); disjoint children.
   No list of all intervals in memory. n<=1e9 => 64-bit intermediates. */
#include <stdint.h>
#include <stdio.h>
#include <assert.h>
static int p,m,T,obs[8],cnt,h;
static int powi(int a,int n){uint64_t b=a,r=1;for(;n;n>>=1,b=b*b%p)if(n&1)r=r*b%p;return (int)r;}
static void solve(int L,int R,int image,int64_t slope){
    if(R-L<=7){for(int x=L;x<=R;x++){int y=2*x%p,j=1;while(y>x){y=2*y%p;j++;}
        if(y==x&&powi(x,(p-1)/2)==p-1){if(cnt<8)obs[cnt]=x;if(cnt)assert(h==j);h=j;cnt++;}}return;}
    int64_t s=2*slope,v=2LL*image;
    for(int k=0;k<=1;k++){
        int64_t base=v-(int64_t)p*k;
        /* T<=base+s*i<=p-1, 0<=i<=R-L; avoid negative / truncation */
        if(base>=p)continue;
        int64_t a=(base>=T)?0:(T-base+s-1)/s,b=(p-1-base)/s;
        if(b>R-L)b=R-L;
        if(a<=b)solve(L+(int)a,L+(int)b,(int)(base+s*a),s);
    }
}
int main(void){int in=0,n=0,total=0;char line[256];while(fgets(line,sizeof(line),stdin)){
    int idx,f;if(sscanf(line,"uncertified %d final index %d oddcase %d",&p,&idx,&f)!=3||!f)continue;
    assert(p<=1000000000&&p%24==17);in++;m=powi(5,p/2)==1?5:powi(7,p/2)==1?7:9;T=(2*p)/m+1;cnt=h=0;
    solve(T,p-1,T,1);
    if(cnt){n++;total+=cnt;printf("p %d m %d negative orbits %d order %d minima (up to 8):",p,m,cnt,h);
        for(int i=0;i<cnt&&i<8;i++){printf(" %d",obs[i]);}puts("");}
}printf("inputs %d sealed primes %d negative orbits %d\n",in,n,total);return 0;}
