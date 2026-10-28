#define main model_main
#include "/home/pasky/projects/math/erdos-straus-claude-agent-worktree-0044/scripts/z49_i3fable_crt.c"
#undef main
#include <assert.h>
int main(void) {
    Lspf=256; spf=calloc(Lspf+1,sizeof(int));
    for(long i=2;i<=Lspf;i++) if(!spf[i]) for(long j=i;j<=Lspf;j+=i) if(!spf[j]) spf[j]=i;
    pidx=calloc(Lspf+1,sizeof(int)); plist=calloc(Lspf+1,sizeof(u64)); pw=calloc(Lspf+1,sizeof(u64)); NP=0;
    for(long p=2;p<=Lspf;p++) if(spf[p]==p) {pidx[p]=NP;plist[NP++]=p;u64 q=1;while((u128)q*p<((u128)1<<62))q*=p;pw[p]=q;}
    u64 *R=malloc(NP*sizeof(u64)); FILE *f=fopen("/tmp/z49-i3-xcount_i3.u16","rb");assert(f);
    uint16_t counts[20001];assert(fread(counts,2,20001,f)==20001);fclose(f);
    for(u64 n=3;n<=20000;n++) {
        NOMN=n;u64 X0=(u64)sqrt((double)n)+2;
        for(long i=0;i<NP;i++)R[i]=n%pw[plist[i]];
        int found=0;
        for(u64 v=3;v<=X0;v++) {K_v=fac(v,PR_v,EX_v);int t8,u8;if(test_v(R,v,&t8,&u8))found=1;}
        if(test_tail(R,n,X0))found=1;
        assert(found==(counts[n]>0));
    }
    puts("CRT v-pass plus tail, evaluated at consistent residues of each actual n=3..20000: agrees with exact engine");
    return 0;
}
