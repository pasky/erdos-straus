"""z56 PRIMET1: read sieve output (uint64 p, uint16 R), assign hash split h(p) = splitmix64(p) mod 4 (or mod 64), write .npy.
Usage: uv run --with numpy python scripts/z56_primet1_split.py SIEVE.bin OUTPREFIX MOD KEEP1[,KEEP2...]
Writes OUTPREFIX_h{k}.npy (structured p,R) for each kept residue k of splitmix64(p) mod MOD."""
import sys
import numpy as np

def splitmix64(x):
    x = x.astype(np.uint64)
    with np.errstate(over='ignore'):
        z = x + np.uint64(0x9E3779B97F4A7C15)
        z = (z ^ (z >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9)
        z = (z ^ (z >> np.uint64(27))) * np.uint64(0x94D049BB133111EB)
        z = z ^ (z >> np.uint64(31))
    return z

if __name__ == '__main__':
    d = np.fromfile(sys.argv[1], dtype=np.dtype([('p', '<u8'), ('r', '<u2')]))
    mod = int(sys.argv[3]); keep = [int(k) for k in sys.argv[4].split(',')]
    h = splitmix64(d['p']) % np.uint64(mod)
    for k in keep:
        sel = d[h == np.uint64(k)]
        np.save(f'{sys.argv[2]}_h{k}.npy', sel)
        print(k, len(sel), 'zeros:', int((sel['r'] == 0).sum()))
