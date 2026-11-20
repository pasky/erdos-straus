/* Controlled prime panels. Inherits round-one deterministic 64-bit MR.
   Emits the first modulus in the specified witness scan (not total #solutions).
   `hard` reads the distinct hard AP primes on stdin, without the R8 scan. */
#include <algorithm>
#include <array>
#include <set>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#define main round1_panel_main
#include "z75_obstruct_panels.c"
#undef main
const U LO=1000000000000ULL,HI=9000000000000ULL;
static std::vector<U> pos,neg;
static std::set<U> used;
static int smooth(U n){for(unsigned l:q){if(l>61)break;while(n%l==0)n/=l;}return n==1;}
static bool near(U n){U m=sqrtl(n-1);return m*m==n-1||(m+1)*(m+1)==n-1;}
static void gen(U v,int i){if(i==18){if(v>=LO&&prime(v+1)&&!near(v+1))(prime(12*(v+1)+1)?pos:neg).push_back(v+1);return;}do{gen(v,i+1);if(v>(HI-1)/q[i])break;v*=q[i];}while(1);}
/* Sample anchor cohort without replacement by a fixed integer rank. */
static U hash64(U x){x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);}
static bool ranks(U x,U y){return hash64(x)<hash64(y);}
static U neighbor(U p,bool sm,bool sh){for(U d=840;d<LO/100;d+=840)for(U n:{p+d,p-d})if(n>=LO&&n<HI&&!used.count(n)&&!near(n)&&sm==smooth(n-1)&&prime(n)&&sh==prime(12*n+1)){used.insert(n);return n;}abort();}
static void emit(const char *tag,U p,U n,bool want8=true){unsigned R=0,A=0,Z=0,T=0,E=0;
 for(unsigned f=3;f<=200000003;f++){unsigned r=f-n%f;if((f+1)%r)continue;
 if((f&3)==3){if(!R&&((f+1)/4)%r==0)R=f;if(!A&&(r==1||r%4==0))A=f;
 if((f&7)==7){if(!Z)Z=f;if(!E&&((f+1)/8)%r==0)E=f;}}
 if(!T&&r>=2){U t=(f+1)/r,b=(n+r)/f;if(t>=2&&b>=2&&((n+t)%8*(t%8)*(r%8)*(b%8))%8==0)T=f;}
 if(R&&A&&Z&&T&&(!want8||E))break;}
 printf("%s %" PRIu64 " %" PRIu64 " %u %u %u %u %u\n",tag,p,n,R,A,Z,T,want8?E:0);}
int main(int ac,char**av){puts("# family anchor n f_R f_A f_U7 f_S f_R8 (0=not certified here)");
 if(ac==2&&std::string(av[1])=="hard"){U n;while(scanf("%" SCNu64,&n)==1)emit("hard",n,n,false);return 0;}
 assert(ac==1&&q[17]==61);gen(840,0);std::sort(pos.begin(),pos.end(),ranks);std::set<U> ns(neg.begin(),neg.end());int bins[8]={};
 for(U p:pos){int j=p/LO-1;if(bins[j]>=256)continue;bins[j]++;emit("sm+",p,p);auto right=ns.lower_bound(p),left=right;bool have=right!=ns.end();if(left!=ns.begin()){--left;if(!have||p-*left<*right-p)right=left;}
 assert(right!=ns.end());U n=*right;ns.erase(right);emit("sm-",p,n);emit("rough+",p,neighbor(p,false,true));emit("rough-",p,neighbor(p,false,false));}
 for(int i:bins)assert(i==256);
 /* Exact n=m²+1; match shift and smoothness statuses in near-pairs. */
 for(U m=420;m*m<HI;m+=420){U p=m*m+1;if(p<LO||!prime(p))continue;emit("sq",p,p);emit("sq_ctl",p,neighbor(p,smooth(p-1),prime(12*p+1)));}
 /* Multiple prime shifts: a separate near-size matched comparison, with same
    12p+1 status, both rough/non-square; comparison kills neither other shift. */
 for(int j=1;j<=8;j++){int cnt=0;for(U i=0;cnt<128;i++){U p=840*((j*LO)/840+hash64(j*LO+i)%(LO/840))+1;if(p<j*LO||p>=(j+1)*LO||near(p)||smooth(p-1)||used.count(p)||!prime(p)||!prime(12*p+1)||!prime((p+3)/4)||!prime((p+7)/8))continue;
 used.insert(p);cnt++;emit("shift3",p,p);U n;do{n=neighbor(p,false,true);}while(prime((n+3)/4)||prime((n+7)/8));emit("shift1",p,n);}}
}
