/* O92 (POINTWISE_TYPEI5.md): relaxed L-level system with 7^b replaced by an arbitrary odd u.
   Same search as typei4_lb.c (Cor 3.2 of TYPEI4) but u arbitrary; a odd with 7^a factor kept.
   Prints: L u a c' g delta P1 X rho j   where rho = z/P1, j = T u/2 - y (signed).
   Usage: typei5_relax L umin umax [amax]  (only odd u) */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
int main(int argc,char**argv){
  int L=atoi(argv[1]); ll umin=atoll(argv[2]),umax=atoll(argv[3]); int amax=argc>4?atoi(argv[4]):59;
  ll T=1LL<<(L-4); ll Ymax=T*umax;
  int *spf=calloc(Ymax+1,sizeof(int)); for(ll i=2;i<=Ymax;i++) if(!spf[i]) for(ll j=i;j<=Ymax;j+=i) if(!spf[j]) spf[j]=(int)i;
  static ll dv[1<<16]; long cnt=0;
  for(ll u=umin|1;u<=umax;u+=2){ ll Y=T*u;
  for(ll y=1;y<Y;y+=2){ ll z=Y-y; i128 twoy=(i128)2*y-Y;
    int nd=1; dv[0]=1; { ll m=y; while(m>1){ int q=spf[m],e=0; while(m%q==0){m/=q;e++;} int n0=nd; ll pw=1;
        for(int k=1;k<=e;k++){ pw*=q; for(int i=0;i<n0;i++) dv[nd++]=dv[i]*pw; } } }
    for(int ic=0;ic<nd;ic++){ ll cp=dv[ic]; ll r=y/cp;
      for(int ig=0;ig<nd;ig++){ ll g=dv[ig]; if(r%g)continue; ll dl=r/g;
        i128 cg2=(i128)cp*g*g; i128 p7a=7; 
        for(int a=1;a<=amax;a+=2,p7a*=49){ i128 p=p7a*u;
          if(twoy>0){ if(2*p7a>=T)break; } else { if(4*p7a>=(i128)T*T*u)break; }
          i128 P1=cg2+p*twoy; if(P1<1)continue; if(z%P1)continue;
          i128 num=1+p*(z/P1); if(num%(4*(i128)cp*g))continue; i128 X=num/(4*(i128)cp*g);
          if(X%2==0)continue;
          printf("%d %lld %d %lld %lld %lld %lld %lld %lld %lld\n",L,u,a,cp,g,dl,(ll)P1,(ll)X,(ll)(z/P1),(ll)(Y/2-y));cnt++;
        }}}}}
  fprintf(stderr,"L=%d u in [%lld,%lld]: %ld solutions\n",L,umin,umax,cnt); return 0;}
