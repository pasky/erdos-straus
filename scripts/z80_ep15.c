/* Only the two factored domains of the z79 endpoint. The live modes below
   never evaluate 5*N in uint128. Compiler must leave assertions enabled. */
#define main historical_main
#include "z79_endpoint.c"
#undef main
int main(int argc,char**argv){assert(argc==7);int L=atoi(argv[1]);p=atoi(argv[2]);q=atoi(argv[3]);C=atoll(argv[5]);gen=atoi(argv[6]);assert((L==15||L==16)&&p*q==5&&p+q==6&&C<=150000&&C>0);W=1;for(int i=0;i<L;i++)W*=17;B=W/17;N=W*B;
 U lo=0,hi=1ULL<<34;while(hi-lo>1){U m=(lo+hi)/2;if((Z)m*m>=W)hi=m;else lo=m;}emax=466*(Z)hi;
 if(!strcmp(argv[4],"e")){for(U e=4-(U)(N%4);e<=C;e+=4)if(e%17){keys++;Z M=(N+e)/4;int n=factors(M,A);for(int i=0;i<n;i++){Z a=A[i];if(a>M/a)continue;Z rest=M/a;for(int j=0;j<n;j++){Z b=A[j];if(b>=a&&rest%b==0)test(a,b,rest/b);}}}}
 else{assert(!strcmp(argv[4],"HZ"));for(U H=1;H<=C;H++)for(U z=1;z<=C/H;z++){if(B*z<=q*H)continue;Z n=B*z-q*H;if(n%p)continue;keys++;int nd=factors(n/p,A);for(int j=0;j<nd;j++)at_a(H,A[j]);}}
 if(!gen){assert(getchar()==EOF);printf("end %d %lu %lu %s %lu %lu %lu %lu\n",L,p,q,argv[4],C,keys,vis,hits);}}
