/* Independent positive-only census for n=1 mod 24. Does not use primary AP
   sieve, its CRT code, its congruences in two coordinates, or its prime sieve.
   Directly tabulate the one-modulus word predicate on the AP over a period,
   cross small composites, MR-test residual candidates, certify each by a
   literal word identity. Upper bound on maximum f when no unknowns. */
#define main unused_old_panel_main
#include "z75_obstruct_panels.c"
#undef main
#define SMALL 8191
#define CH 524288
static unsigned char x[CH];
static struct period {unsigned start,step;} per[100000];static int np,isa;
static void add(unsigned f,unsigned j,U lo){assert(np<100000);per[np++]=(struct period){(j+f-lo%f)%f,f};}
static int word(U n,unsigned f){unsigned r=f-n%f;if(isa)return (r%4==0||r==1)&&(f+1)%r==0;return (f+1)/4%r==0;}
int main(int ac,char **av){assert(ac==4);isa=atoi(av[1]);U low=atoll(av[2]),hi=atoll(av[3]),lo=low/24+(low%24>1);assert(low>1000&&hi<1000000000000ULL);
 for(unsigned f=3;f<=SMALL;f+=4){unsigned per=f/gcd(f,24);for(unsigned j=0;j<per;j++)if(word((24*j+1)%f,f))add(per,j,lo);}
 for(unsigned j=0;j<sizeof(q)/sizeof(*q);j++)for(unsigned i=0;i<q[j];i++)if((24*i+1)%q[j]==0)add(q[j],i,lo);
 U hiidx=(hi-1)/24,rest=0,npres=0,unk=0,mx=0,mxn=0;
 for(U base=lo;base<=hiidx;base+=CH){int sz=(hiidx-base+1<CH)?hiidx-base+1:CH;
 for(int j=0;j<sz;j++)x[j]=0;
 for(int j=0;j<np;j++){int i=per[j].start;for(;i<sz;i+=per[j].step)x[i]=1;per[j].start=i-sz;}
 for(int j=0;j<sz;j++)if(!x[j]){U n=(base+j)*24+1;rest++;if(!prime(n))continue;npres++;int found=0;
 for(unsigned f=SMALL+4;f<=200000003;f+=4){if(!word(n,f))continue;U u=f-n%f;if(isa&&u==1)u=f+1;U t=(f+1)/u,v=(n+u)/f;assert(t*u*v==n+u+v&&(isa?u:t)%4==0);if(f>mx){mx=f;mxn=n;}found=1;break;}
 if(!found){printf("UNK %"PRIu64"\n",n);unk++;}}}
 printf("%s n=1mod24 input %"PRIu64" %"PRIu64" early_limit %d MR_inputs %"PRIu64" late_primes %"PRIu64" max_late_f %"PRIu64" at %"PRIu64" unknown %"PRIu64"\n",isa?"A":"R",low,hi,SMALL,rest,npres,mx,mxn,unk);return unk!=0;}
