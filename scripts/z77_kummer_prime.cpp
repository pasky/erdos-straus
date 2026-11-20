// Positive certificates above the z76 floor. Emit every input (compressed in replay).
// Larger f or a zero field does not mean the equation has no solution.
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <numeric>
using I=int64_t;
static constexpr I floor_n=1590284203561, max_m=100000000;
static bool mordell(I n){switch(n%840){case 1:case 121:case 169:case 289:case 361:case 529:return true;default:return false;}}
static I mul(I a,I b,I n){return (__int128)a*b%n;}
static I power(I a,I d,I n){I z=1;for(;d;d/=2,a=mul(a,a,n))if(d%2)z=mul(z,a,n);return z;}
// First 12 prime bases deterministic at all heights here (Sorenson-Webster).
static bool prime(I n){constexpr int small[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67};
 for(int p:small)if(n%p==0)return n==p;
 I d=n-1;int s=0;while(d%2==0)d/=2,s++;
 for(int j=0;j<12;j++){I x=power(small[j],d,n);if(x==1||x==n-1)continue;
 int h=1;while(h<s&&x!=n-1)x=mul(x,x,n),++h;if(x!=n-1)return false;}return true;}
static constexpr int cap=2000000;
static I modhit(I n,int k,char mode){for(int f=k-1;f<=cap;f+=k){int u=f-n%f;
 if(mode=='A'){if((f+1)%u==0&&(u==1||u%4==0))return f;}
 else if(((f+1)/k)%u==0)return f;
 }return 0;}
// Composite compatible stacks: 13,17,29,37 all split; 11 and 19 force common
// factors in both summands; 3 and 7 likewise on the 105 stack.
static void composites(){for(I c:{4,16,36,64,100,4*209*209,4*418*418,4*21*21,4*42*42}){
 I prod=c%(209*209)==0?11*13*17*19:c%(21*21)==0?105:13*17*29*37;
 for(I m=1;m<=max_m;m+=2){I n=m*m+c;if(n<=floor_n||n%prod)continue;
 if(prod!=105&&!mordell(n+(c%8==4?420:0)))continue;
 I R=modhit(n,4,'R'),G=0;for(int f=7;f<=cap;f+=8){int u=f-n%f;if((f+1)%u==0){G=f;break;}}
 printf("%ld %ld %ld %ld\n",c,m,R,G);
 }}}
int main(int ac,char **av){if(ac==2&&!strcmp(av[1],"composites")){composites();return 0;}assert(ac==1);
 for(I c:{1,4,16,36,64,100})for(I r=0;r<840;r++){
 // All classes, not just Mordell. Small primes dividing p exclude it here.
 if(std::gcd(r*r+c,I(210))!=1)continue;
 for(I m=r;m<=max_m;m+=840){I n=m*m+c;if(n<=floor_n||!prime(n))continue;
 printf("%ld %ld %ld %ld %ld\n",c,m,modhit(n,8,'8'),modhit(n,4,'R'),modhit(n,4,'A'));
 }} }
