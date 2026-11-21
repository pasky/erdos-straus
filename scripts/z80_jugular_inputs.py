"""Main parity panel and bounded controls. Huge F2 records tabulated separately."""
from z80_square_span import primes_to
from pathlib import Path

def panel():
    P={p for p in primes_to(10**7) if p%840==1}
    S={131,241,17_401_609,105,1465,3865,4545,10305,12145,39361,67425}
    for name in ('star_prime_zeros','composite_zeros_le8e6','gstar_zeros'):
        for line in Path(f'data/z58/screens/{name}.txt').read_text().splitlines():
            if line and not line.startswith('#'):
                n=int(line.split()[0]);
                if n<=20_000_000:S.add(n)
    return sorted(P|S|{m*m for m in range(3,102,2)})
if __name__=='__main__':
    import sys
    kind=sys.argv[1] if len(sys.argv)>1 else 'all'
    if kind=='high':
        rows=Path('data/z58/screens/r8_zeros_1e10.txt').read_text().splitlines()
        out=[2521]+[int(r.split()[0]) for r in rows if r and not r.startswith('#')]+[1590284203561]
    else:
        out=panel()
        if kind!='all':
            assert kind in ('prime','comp')
            P=set(primes_to(max(out)))
            out=[n for n in out if (n in P)==(kind=='prime')]
    print(*out,sep='\n')
