/* z52c_rh_star.c (RESIDUE_HARDNESS.md): the (★) count R*(n) = #{(u,B,C): 4uBC - u - B = n} for all n <= hi, and the
   prime-local-density weighted count RW(n) = sum over the same triples of w(u,B), w = prod_{l | uB, l odd, l > 13} l/(l-1).
   (For a prime p the AP {4uBC - u - B : C >= 1} is prime with relative density prod_{l | 4uB} l/(l-1); the factors at
   l | 2*3*5*7*11*13 are dropped so that the conditional mean given p mod Q (Q | 2^k*3*5*7*11*13) is the tuple count in
   the class weighted by the remaining local factors; RESIDUE_HARDNESS §1.3.)
   usage: ./z52c_rh_star hi outprefix   -> outprefix_R.u16, outprefix_RW.f32 (index n = 0..hi)            */
#include <stdio.h>
#include <stdlib.h>
static long gcdl(long a,long b){ while(b){long t=a%b;a=b;b=t;} return a; }
int main(int argc,char**argv){
  long hi=atol(argv[1]); char fn[512];
  long N=hi/3+10; int *spf=calloc(N+1,sizeof(int));
  for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i;
  float *wl=malloc((N+1)*sizeof(float)); wl[1]=1;            /* wl[k] = prod_{l | k, l > 13} l/(l-1) */
  for(long k=2;k<=N;k++){ long l=spf[k], r=k; while(r%l==0) r/=l; wl[k]=wl[r]*(l>13 ? (float)l/(float)(l-1) : 1.0f); }
  unsigned short *R=calloc(hi+1,sizeof(unsigned short)); float *RW=calloc(hi+1,sizeof(float));
  long ntrip=0;
  for(long u=1;3*u-1<=hi;u++) for(long B=1;4*u*B-u-B<=hi;B++){
    if(((u+B)&1)==0||gcdl(u,B)!=1) continue;
    long q=4*u*B; float w=wl[u]*wl[B];
    for(long n=q-u-B;n<=hi;n+=q){ R[n]++; RW[n]+=w; ntrip++; }
  }
  sprintf(fn,"%s_R.u16",argv[2]); FILE*f=fopen(fn,"wb"); fwrite(R,sizeof(unsigned short),hi+1,f); fclose(f);
  sprintf(fn,"%s_RW.f32",argv[2]); f=fopen(fn,"wb"); fwrite(RW,sizeof(float),hi+1,f); fclose(f);
  fprintf(stderr,"hi=%ld triples=%ld\n",hi,ntrip); return 0;
}
