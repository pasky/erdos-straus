"""Replay at the cut grid around N^(5/12). No floating-point decisions."""
from pathlib import Path
import sys,subprocess
for r in map(int,sys.argv[2:]):
    for k in (9,11,13,15,17):
        n=r**k;b=n.bit_length()
        if b>121:continue
        j=b*5//12
        print(subprocess.check_output([sys.argv[1],'data/z78/r2/log16.txt',str(r),str(k),'5',str(j-2),str(j+3)],text=True,timeout=1750).strip(),flush=True)
