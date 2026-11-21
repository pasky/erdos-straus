/* Positive 17-endpoint only: two alternative exhaustive index sectors.
   Reuse the final exact tuple test and GMP conversions, not the z79 loops. */
#define main legacy_main
#include "z79_endpoint.c"
#undef main
static Z sqr(Z x){return x*x;}
static U sr(Z x){U lo=0,hi=1;while((Z)hi*hi<=x){assert(hi<UINT64_MAX/2);hi*=2;}while(hi-lo>1){U z=(lo+hi)/2;if((Z)z*z<=x)lo=z;else hi=z;}return lo;}
static void jrange(U L){Z v=q*B+L;assert(v<((Z)1<<64) && p*v<~(Z)0/v);Z top=p*v*v/4;U Hmax=sr(top/(W-q*emax));
 for(U H=1;H<=Hmax;H++){U step=4*H;Z z=(top/sqr(H)+q*emax)/W;U hi=z<L?z:L;
 for(U J=step-(U)(q*B%step);J<=hi;J+=step){keys++;Z M=(q*B+J)/H;assert(M%4==0);
 for(Z e=M-N%M;e<=emax;e+=M){vis++;if((p*B+J)%e)continue;Z x=W*J-q*e;if(x%(p*M))continue;Z a=x/(p*M);if(a&&(M/4)%a==0)test(a,(N+e)/M,M/4/a);}}}}
static void scanv(U v,U h){Z t=q*B/(4*v),hi=t+2+p*B/(6*h*sqr(v));
 for(Z a=t+1;a<=hi;a++){vis++;Z J=4*v*a-q*B,z=W*J,den=4*p*a*a;assert(J>0&&z>q*emax);Z d0=(z-q*emax+den-1)/den,d1=(z-q)/den;if(!d0)d0=1;if(d1>v/h)d1=v/h;
 for(U d=d0;d<=d1;d++)if(v%d==0){Z H=v/d;if(p*a>=W*H||(W*H-p*a)%q)continue;test(a,(W*H-p*a)/q,d);}}}
static void hdgroup(U Y){mpz_t sq,top,bot,z;mpz_inits(sq,top,bot,z,NULL);
 for(U H=1;H<=Y&&(Z)12*H*H*H<=p*B;H++){Z V=W*H;zset(sq,V);mpz_mul(sq,sq,sq);U vtop=sr(p*B/(12*H));if(vtop>Y)vtop=Y;
 for(U d=1;d<=vtop/H;d++){keys++; /* Separate the quotient before multiplying to fit 128 bits; tiny d handled by GMP. */
 if(d<5){zset(z,N+1);mpz_mul_ui(z,z,5);mpz_cdiv_q_ui(z,z,d);}else{Z x=N+1;zset(z,5*(x/d)+(5*(x%d)+d-1)/d);}mpz_sub(top,sq,z);if(mpz_sgn(top)<0)continue;mpz_sqrt(top,top);Z up=zget(top);
 if(d<5){zset(z,N+emax);mpz_mul_ui(z,z,5);mpz_fdiv_q_ui(z,z,d);}else{Z x=N+emax;zset(z,5*(x/d)+5*(x%d)/d);}mpz_sub(bot,sq,z);Z low=0;if(mpz_sgn(bot)>0){mpz_sqrt(bot,bot);low=zget(bot);}assert(up<V&&low<=up);
 for(int k=0;k<2;k++){Z left=k?V+low:V-up,right=k?V+up:V-low;for(Z a=(left+2*p-1)/(2*p);a<=right/(2*p);a++){if(!a||a>V/(p+q)||(V-p*a)%q)continue;test(a,(V-p*a)/q,d);}}}}
 for(U v=1;v<=Y;v++){Z h=1+p*B/(12*sqr(v));if(h<=v)scanv(v,(U)h);}mpz_clears(sq,top,bot,z,NULL);}
int main(int argc,char**argv){assert(argc==5);int L=atoi(argv[1]);p=atoi(argv[2]);q=6-p;C=atoll(argv[4]);assert((p==1||p==5)&&L>=12&&L<=16&&C<=4000000000ULL&&C>0);W=1;for(int i=0;i<L;i++)W*=17;B=W/17;N=W*B;emax=466*(sr(W-1)+1);
#ifdef Z80_CONTROL
 assert(p==5); if(C==1){W=24;B=3;N=72;emax=4;}else{W=6;B=1;N=6;emax=2;}
#endif
 if(!strcmp(argv[3],"J"))jrange(C);else{assert(!strcmp(argv[3],"Hd"));hdgroup(C);}printf("end %d %lu %lu %s %lu %lu %lu %lu\n",L,p,q,argv[3],C,keys,vis,hits);}
