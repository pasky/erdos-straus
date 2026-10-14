/* R217: per-pattern comparison of author fs_sum.c pattern_bound vs R217 review_fs_fin.c lbound; prints patterns where R217 > author (none expected). usage: r S */
#define NO_MAIN
#include "fs_sum.c"
#undef MIN
#define NOMAIN
#define lf lf2
#define L L2_
#define lbound mylb
#define mn mymn
#include "review_fs_fin.c"
int main(int argc,char**argv){int r=atoi(argv[1]);int S=atoi(argv[2]);
 lq=r*logl(3.0L); L2_=lq; lfact[0]=0; for(int i=1;i<NF;i++) lfact[i]=lfact[i-1]+logl((LD)i);
 lf2[0]=0; for(int i=1;i<4000;i++) lf2[i]=lf2[i-1]+logl((LD)i);
 int shown=0;
 for(int s=3;s<=S;s++) for(int a=1;a<s;a++) for(int z=0;a+z<s;z++){int b=s-a-z; if(b<a) continue;
  for(int y=0;y<=b-2;y++){int t=b-y,am; LD e1=pattern_bound(s,a,z,y,t,&am); LD e2=mylb(s,a,z,y,t);
   if(e2-e1>1e-9 && shown<15){shown++; printf("s=%d a=%d z=%d y=%d t=%d theirs=%.6Lf (route %s) mine=%.6Lf\n",s,a,z,y,t,e1,rname[am],e2);}}}
 return 0;}
