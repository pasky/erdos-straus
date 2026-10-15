/* fz_check_bounds.c (O220; copy of fs_check_bounds.c (O216)): compare pattern_bound (fz_sum.c) with exact Case B tuple counts from bsE_famcount print output over F_p. usage: bsE_famcount p 2 SMAX print | fs_check_bounds p */
#define NO_MAIN
#include "fz_sum.c"
#include <string.h>
/* read famcount print lines, count tuples per pattern, compare with exp(pattern_bound) (q = p prime here) */
static long cntp[40][40][40][40];
int main(int argc,char**argv){ int p=atoi(argv[1]); lq=logl((LD)p); init_omstar(p);
  lfact[0]=0; for(int i=1;i<NF;i++) lfact[i]=lfact[i-1]+logl((LD)i);
  char line[4096]; int s,a,b,mu,y,t;
  while(fgets(line,sizeof line,stdin)){ if(sscanf(line,"s=%d a=%d b=%d mu=%d y=%d t=%d",&s,&a,&b,&mu,&y,&t)==6){
      if(s<0||s>=40||a<0||a>=40||mu<0||mu>=40||y<0||y>=40){printf("OUT OF RANGE %s",line); return 2;}
      if(a>b){int x=a;a=b;b=x;} cntp[s][a][mu][y]++; if(y+t!=b) printf("DEGREE VIOLATION %s",line);} }
  int viol=0, pats=0; LD worst=0;
  for(s=3;s<40;s++) for(a=1;a<s;a++) for(mu=0;a+mu<s;mu++) for(y=0;y<40;y++) if(cntp[s][a][mu][y]){
      b=s-a-mu; t=b-y; int am; LD e=pattern_bound(s,a,mu,y,t,&am); LD bd=expl(e);
      long c=cntp[s][a][mu][y]; long cc = (a==b)? c : c/2; /* a<b: both orders counted in famcount */
      pats++; if(cc>bd+1e-9){viol++; printf("VIOL s=%d a=%d z=%d y=%d t=%d count=%ld bound=%.2Lf %s\n",s,a,mu,y,t,cc,bd,rname[am]);}
      if(cc/bd>worst) worst=cc/bd; }
  printf("p=%d patterns=%d violations=%d max count/bound=%.3Lf\n",p,pats,viol,worst); return viol?1:0; }
