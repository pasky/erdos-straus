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
if __name__=='__main__': print(*panel(),sep='\n')
