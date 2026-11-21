"""Sum the scaled powers of two in finite octave histograms. One C process at a time."""
import sys,subprocess
from pathlib import Path
for b in map(int,sys.argv[1:]):
    l=subprocess.run(['data/z78/r2/dyad.bin',str(b),'1'],check=True,capture_output=True,text=True,timeout=60).stdout.splitlines();out=[]
    for s in l:
        bb,j,*pairs=s.split();assert int(bb)==b and int(j)==b//2-len(out)
        out.append(sum(int(c)<<int(e) for e,c in (p.split(':') for p in pairs)))
    print(1<<b,int(j),*reversed(out),flush=True)
