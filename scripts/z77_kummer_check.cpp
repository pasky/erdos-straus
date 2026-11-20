// Independent panel enumeration. All primality decisions by Eratosthenes on m,
// not by MR; each prime/candidate certificate sheet is streamed then discarded.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <map>
#include <string>
#include <vector>
using I=int64_t;
static constexpr int M=100000000, a[]={1,2,4,6,8,10};
static constexpr I L=1590284203561;
static std::array<std::vector<bool>,6> dead;
static I power(I a,I e,I p){I v=1;while(e){if(e%2)v=v*a%p;a=a*a%p;e/=2;}return v;}
// Index i stands for m=2i+s, s opposite to the parity of the square offset.
static void strike(int h,int p,int r){int s=(a[h]%2==0);if((r&1)!=s)r+=p;
 for(int j=r/2;j<=(M-s)/2;j+=p)dead[h][j]=true;}
static void sieve(){for(auto &v:dead)v.resize(M/2+1);std::vector<bool> marked(M+1);
 // sqrt(M*M+100) < M+1. Every odd prime dividing m²+a² is <=M if
 // it is the least factor of a composite in the search interval.
 for(int p=3;p<=M;p+=2)if(!marked[p]){
 for(I j=(I)p*p;j<=M;j+=2*p)marked[j]=true;
 I iota=0;if(p%4==1){for(int b=2;;b++){iota=power(b,(p-1)/4,p);if(iota*iota%p==p-1)break;}}
 for(int h=0;h<6;h++){if(a[h]%p==0){strike(h,p,0);continue;}
 if(iota){int r=iota*a[h]%p;strike(h,p,r);strike(h,p,p-r);}}
 }}
static bool Mclass(I n){bool ok=false;for(int r:{1,121,169,289,361,529})ok|=(n%840==r);return ok;}
// Reconstruct direct R8, R, b=1 Type A, or U7 identity. No reliance on the
// candidate's assertion that it found a witness or on its loop stopping rule.
static void verify(I n,I f,char tag){assert(f>=3&&f<=2000000);
 I u=f-n%f;if(tag=='A'&&u==1)u=f+1;I v=(n+u)/f,t=(f+1)/u;
 assert(u>0&&v>0&&t>0&&(__int128)t*u*v-u-v==n);
 if(tag=='8'||tag=='R'){int k=tag=='8'?8:4;assert(t%k==0&&(__int128)k*u*v*(t/k)-u-v==n);}
 if(tag=='A')assert(u%4==0&&(__int128)4*(u/4)*v*t-4*(u/4)-v==n);
 if(tag=='G')assert((t*u)%8==0);}
struct PStats{I rows=0,late=0,hard8=0,hardR=0,hardA=0,above14=0,above15=0;void add(I n,I e,I r,I b){rows++;late+=(e==0||e>1000);hard8+=!e;hardR+=!r;hardA+=!b;above14+=n>100000000000000LL;above15+=n>1000000000000000LL;}};
static void primes(FILE *fp,FILE *jobs){sieve();std::map<std::pair<int,int>,PStats> stats;I c,m,e,r,b;
 // Enumerate (u,C) instead of scanning first f. Independently classify
 // every row reported late at 1000. An early row is checked by its witness.
 static bool cheap[1001][1000]; for(int u=1;8*u-1<=1000;u++)for(int z=1;8*u*z-1<=1000;z++){
 int f=8*u*z-1;cheap[f][f-u]=true;}
 while(fscanf(fp,"%ld%ld%ld%ld%ld",&c,&m,&e,&r,&b)==5){int h=0;while(h<6&&a[h]*a[h]!=c)h++;assert(h<6&&m>=1&&m<=M&&((m+c)&1));I n=m*m+c;
 assert(n>L&&!dead[h][m/2]);dead[h][m/2]=true;
 for(auto [f,t]:{std::pair<I,char>{e,'8'},{r,'R'},{b,'A'}})if(f)verify(n,f,t);else fprintf(jobs,"%c %ld\n",t,n);
 if(!e||e>1000)for(int f=7;f<=1000;f+=8)assert(!cheap[f][n%f]);
 stats[{c,0}].add(n,e,r,b);if(Mclass(n))stats[{c,1}].add(n,e,r,b);
 }
 for(int h=0;h<6;h++){int s=(a[h]%2==0);for(I m=s;m<=M;m+=2)if(m*m+a[h]*a[h]>L)assert(dead[h][m/2]);}
 puts("# prime: offset Mordell_only rows f8_gt_1000 cap8 capR capA above_1e14 above_1e15");
 for(auto [key,v]:stats)printf("P %d %d %ld %ld %ld %ld %ld %ld %ld\n",key.first,key.second,v.rows,v.late,v.hard8,v.hardR,v.hardA,v.above14,v.above15);}
static void composites(FILE *fp,FILE *jobs){puts("# comp: offset rows capR capU7 max_R_below_cap max_U7_below_cap");
 for(I a:{2,4,6,8,10,418,836,42,84}){I rows=0,hr=0,hg=0,mr=0,mg=0;
 for(I m=1;m<=M;m+=2){I c=a*a,n=m*m+c;if(n<=L)continue;
 if(a<=10){if(n%13||n%17||n%29||n%37)continue;}else if(a%209==0){if(n%11||n%13||n%17||n%19)continue;}else if(n%3||n%5||n%7)continue;
 if(a!=42&&a!=84&&(!Mclass((n%8==1?n:n+420))))continue;
 assert(m*m<n&&n<(m+1)*(m+1));I cc,mm,r,g;assert(fscanf(fp,"%ld%ld%ld%ld",&cc,&mm,&r,&g)==4&&cc==c&&mm==m);
 if(r)verify(n,r,'R');else fprintf(jobs,"R %ld\n",n);if(g)verify(n,g,'G');else fprintf(jobs,"G %ld\n",n);
 rows++;hr+=!r;hg+=!g;mr=std::max(r,mr);mg=std::max(g,mg);
 }printf("C %ld %ld %ld %ld %ld %ld\n",a*a,rows,hr,hg,mr,mg);}
 I x;assert(fscanf(fp,"%ld",&x)==EOF);}
int main(int argc,char **argv){assert(argc==4);FILE *p=fopen(argv[1],"r"),*c=fopen(argv[2],"r"),*j=fopen(argv[3],"w");assert(p&&c&&j);primes(p,j);composites(c,j);fclose(j);}
