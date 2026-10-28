"""Certify zero-genus anchors against ALL 19-smooth certificate moduli.
A finite anchor n only permits q<=3(n+3)/2, so finite marking proves the
absence of any smooth-modulus hit, with no exponent cap on later Q.
Memory O(N); marks APs by bounded bytearray slices. Standard library only.
"""
from bisect import bisect_right
from math import gcd
from pathlib import Path
import json
from s8_check_b1 import b1_solutions, c1_solutions

DATA = Path(__file__).resolve().parents[1] / 'data/z48_ltastra'
PRIMES = (2,3,5,7,11,13,17,19)
ODD = PRIMES[2:]


def smooth_numbers(limit):
    values = [1]
    for p in PRIMES:
        old = values[:]
        power = p
        while power <= limit:
            values.extend(a*power for a in old if a <= limit//power)
            power *= p
    return sorted(values)


def mark(a, start, step, N):
    assert 0 < start <= N
    length = (N-start)//step+1
    a[start:N+1:step] = b'\x01'*length


def direct_hits(n, values):
    """Recheck one anchor by divisibility, not by AP marking."""
    r,b = [],[]
    for u in values:
        if 4*u*(u+1)-2*u-1 > n:
            break
        lo = bisect_right(values,u)
        hi = bisect_right(values,(n+u)//(4*u-1))
        for v in values[lo:hi]:
            if (u+v)%2 and gcd(u,v)==1 and (n+u+v)%(4*u*v)==0:
                r.append((u,v))
    for y in values:
        if 3*y-4 > n:
            break
        if y < 3 or y%4 != 3:
            continue
        for x in values[:bisect_right(values,(n+y)//(4*(y-1)))]:
            if gcd(x,y)==1 and (n+4*x+y)%(4*x*y)==0:
                b.append((x,y))
    return r,b


def main():
    N = 1000000
    # Both endpoint families have x,y,u,v <= (N+4)/3 (except absent y=1).
    values = smooth_numbers((N+4)//3)
    R = bytearray(N+1)
    T = bytearray(N+1)
    rpairs = bpairs = 0
    for u in values:
        if 4*u*(u+1)-2*u-1 > N:
            break
        for v in values[bisect_right(values,u):bisect_right(values,(N+u)//(4*u-1))]:
            if (u+v)%2 == 0 or gcd(u,v)>1:
                continue
            q = 4*u*v
            mark(R,q-u-v,q,N)
            rpairs += 1
    T[:] = R
    for y in values:
        if 3*y-4 > N:
            break
        if y < 3 or y%4 != 3:
            continue
        for x in values[:bisect_right(values,(N+y)//(4*(y-1)))]:
            if gcd(x,y)>1:
                continue
            q = 4*x*y
            mark(T,q-4*x-y,q,N)
            bpairs += 1
    sign = {p:[0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
               for a in range(p)] for p in ODD}
    ra,ta = {},{}
    for n in range(1,N+1,24):
        bits = 0
        for j,p in enumerate(ODD):
            s = sign[p][n%p]
            if s == 0:
                break
            if s == -1:
                bits |= 1<<j
        else:
            if not R[n]:
                ra.setdefault(bits,n)
            if not T[n]:
                ta.setdefault(bits,n)
    # All sixteen union fibres are theorem-critical; missing star-only fibres
    # are reported, not asserted covered.
    assert set(ta) == set(range(0,64,4)), sorted(ta)
    def smooth(q):
        for prime in PRIMES:
            while q%prime == 0:
                q //= prime
        return q == 1
    for mask,n in ra.items():
        r,b = direct_hits(n,values)
        assert not r, (mask,n,r)
    # Existing (u,C) enumeration, independent of the smooth-pair/AP engine.
    # Include union anchors as well: their first witnesses differ from ra's.
    for n in sorted(set(ra.values()) | set(ta.values())):
        assert all(not smooth(4*u*v) for u,v,c in c1_solutions(n)), n
    for mask,n in ta.items():
        r,b = direct_hits(n,values)
        assert not r and not b, (mask,n,r,b)
        # Convert existing ET b=1 triples back to q=4*d*g, g=(a+1)/c.
        for a,c,d in b1_solutions(n):
            assert (a+1)%c == 0
            assert not smooth(4*d*((a+1)//c)), (mask,n,a,c,d)
    result = {'N':N,'smooth_primes':PRIMES,'character_primes':ODD,
        'star_unordered_pairs_marked':rpairs,'B_pairs_marked':bpairs,
        'R_anchors':ra,'T_anchors':ta,'missing_R_masks':sorted(set(range(64))-set(ra)),
        'missing_T_Mordell_masks':sorted(set(range(0,64,4))-set(ta)),
        'max_R_anchor':max(ra.values()),
        'max_T_anchor':max(ta.values()),
        'meaning':'absence of ALL smooth-modulus hits at each anchor, not merely q|one finite Q'}
    (DATA/'smooth_anchors.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:',len(ra),'star and',len(ta),'union anchors; maxima',max(ra.values()),max(ta.values()))
    print('Missing masks:',result['missing_R_masks'],result['missing_T_Mordell_masks'])


if __name__ == '__main__':
    main()
