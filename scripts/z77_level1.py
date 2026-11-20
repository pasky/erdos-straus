"""Instrument the reviewed ZL joint sweep to take the union, not the sum. Run from root."""
from pathlib import Path
import subprocess, tempfile, os
src=Path('scripts/zl_sweep.c').read_text()
def repl(a,b):
    global src
    assert src.count(a)==1
    src=src.replace(a,b)
repl('static void sweepP(void)',r'''static unsigned **ev, *sz, *cap;
static void hit(u64 n,u64 x){
  size_t i=(n-X0)/2; if(!isp[i])return;
  if(sz[i]==cap[i]){cap[i]=cap[i]?cap[i]*2:16; ev[i]=realloc(ev[i],cap[i]*sizeof(unsigned)); if(!ev[i])abort();}
  ev[i][sz[i]++]=x%n;
}
static void sweepP(void)''')
repl('inc(JP, N);','{ inc(JP,N); if(a%N && d%N && c%N && (f%N)) hit(N,N-f%N); }')
repl('inc(JQ, n);','{inc(JQ,n); if(c%n && (m/f)%n) hit(n,n-(m-1)%n);}')
repl('if(!getenv("ZL_NOP")) sweepP();','ev=calloc(M,sizeof(*ev));sz=calloc(M,sizeof(*sz));cap=calloc(M,sizeof(*cap)); if(!ev||!sz||!cap)abort(); sweepP();')
repl('/* cells */',r'''/* Reflect each event by inversion; retain only nonsquares. */
  unsigned *sq=calloc(X1,sizeof(unsigned)),*seen=calloc(X1,sizeof(unsigned)); if(!sq||!seen)abort();
  for(u64 n=X0;n<X1;n+=2){u64 i=(n-X0)/2;if(!isp[i])continue;
    unsigned count=0;for(u64 h=1;h<=n/2;h++)sq[h*h%n]=n;
    for(unsigned k=0;k<sz[i];k++){u64 x=ev[i][k];if(!x||sq[x]==n||seen[x]==n)continue;
      u64 y=inv_mod(x,n); if(x*y%n!=1)abort(); count+=1+(x!=y);seen[x]=seen[y]=n;}
    if(JP[i]==65535||JQ[i]==65535)abort(); printf("%llu %u %u %u\n",n,JP[i],JQ[i],count);
  }return 0; /* cells */''')
with tempfile.TemporaryDirectory(dir='data/z77') as tmp:
    c=Path(tmp)/'union.c'; c.write_text(src); exe=Path(tmp)/'union'
    subprocess.run(['gcc','-O3',str(c),'-lm','-o',str(exe)],check=True)
    for i in range(4,18):
        hi=min(181392,2<<i)
        subprocess.run([str(exe),str(1<<i),str(hi),str(hi+1),'0','32'],check=True,
                       env={k:v for k,v in os.environ.items() if not k.startswith('ZL_')}|{'ZL_SHORT':'4'})
