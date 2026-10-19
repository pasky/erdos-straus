"""Exact checks for BRAUER_TWISTS.md. Memory bounded by the invoking shell."""
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path
from sympy import factorint, divisors


def valuation(a, p):
    a = F(a)
    assert a
    v = 0
    num, den = a.numerator, a.denominator
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v, F(num, den)


def unitmod(a, p, modulus):
    v, u = valuation(a, p)
    return v, (u.numerator * pow(u.denominator, -1, modulus)) % modulus


def hilbert(a, b, p):
    if p == 'inf':
        return -1 if a < 0 and b < 0 else 1
    if p == 2:
        r, u = unitmod(a, 2, 8)
        s, v = unitmod(b, 2, 8)
        e = ((u-1)//2)*((v-1)//2) + r*((v*v-1)//8) + s*((u*u-1)//8)
        return (-1)**(e % 2)
    r, u = unitmod(a, p, p)
    s, v = unitmod(b, p, p)
    e = r*s*((p-1)//2)
    ans = (-1)**(e % 2)
    if s % 2:
        ans *= 1 if pow(u, (p-1)//2, p) == 1 else -1
    if r % 2:
        ans *= 1 if pow(v, (p-1)//2, p) == 1 else -1
    return ans


def local_square(a, p):
    r, u = unitmod(a, p, 8 if p == 2 else p)
    return r % 2 == 0 and (u == 1 if p == 2 else pow(u, (p-1)//2, p) == 1)


def sf(a):
    return int(__import__('functools').reduce(lambda x, pe: x*(int(pe[0]) if pe[1] % 2 else 1), factorint(a).items(), 1))


def dyadic_scan(bound=128):
    rows = []
    for b in range(8):
        n = 2**b
        found = {}
        for x in range(1, bound+1):
            for y in range(x, bound+1):
                den = 4*x*y - n*(x+y)
                if not den:
                    continue
                z = F(n*x*y, den)
                if valuation(z, 2)[0] < 0:
                    continue
                alpha = hilbert(-F(x)/z, -F(y)/z, 2)
                if alpha == -1:
                    e, u = unitmod(x*y*z, 2, 8)
                    found.setdefault(f'{e%2}:{u}', [x, y, str(z)])
        rows.append({'v2_n': b, 'alpha_minus_twist_classes': found})
    return rows


def square_rational(a):
    a = F(a)
    return a >= 0 and isqrt(a.numerator)**2 == a.numerator and isqrt(a.denominator)**2 == a.denominator


def primes_of(*args):
    ans = {2}
    for a in args:
        a = F(a)
        for v in (abs(a.numerator), a.denominator):
            if v:
                ans.update(map(int, factorint(v)))
    return sorted(ans)


def twist_survives(n, d):
    for p in factorint(n):
        p = int(p)
        b = valuation(n, p)[0]
        if p != 2:
            if not local_square(-F(n, d), p):
                return True
        elif b == 1:
            if d % 2:
                return True
        elif not local_square(-F(n, d), 2):
            return True
    return False


def first_solution(m, n):
    # The existing z45 divisor engine, stopped at its first witness.
    for x in range(n//m+1, 3*n//m+1):
        rem = F(m, n)-F(1, x)
        a, b = rem.numerator, rem.denominator
        for h in divisors(b*b):
            h = int(h)
            if h > b:
                break
            if (h+b) % a or (b*b//h+b) % a:
                continue
            y, z = (h+b)//a, (b*b//h+b)//a
            if y >= x:
                return x, y, z
    raise AssertionError(('no witness', m, n))


def check_rational_lift(n, xyz):
    x, y, z = xyz
    d = sf(x*y*z)
    w = isqrt(x*y*z//d)
    A, B, C = F(w, x), F(w, y), F(w, z)
    k = F(n, 4*d)
    f = 1-A*B/k
    assert A*B*C == k*(A+B+C)
    assert (d*B*C, d*A*C, d*A*B) == xyz
    assert twist_survives(n, d)
    beta = [hilbert(-k, f, p) for p in primes_of(k, f)] + [hilbert(-k, f, 'inf')]
    assert beta.count(-1) % 2 == 0
    for p in primes_of(k, f, A, B, C):
        assert hilbert(-k, f, p) == hilbert(-F(x, z), -F(y, z), p)
        if n % p:
            assert hilbert(-k, f, p) == 1
    extra = square_rational(k)
    if extra:
        s = F(isqrt(k.numerator), isqrt(k.denominator))
        arg = 2*A/s
        gamma = [hilbert(arg, f, p) for p in primes_of(arg, f)] + [hilbert(arg, f, 'inf')]
        assert gamma.count(-1) % 2 == 0
        for p in primes_of(arg, f):
            assert hilbert(-arg, f, p) == hilbert(arg, f, p)*hilbert(-k, f, p)
            if n % p:
                assert hilbert(arg, f, p) == 1
    return {'n': n, 'xyz': list(xyz), 'd': d, 'ABC': list(map(str, (A,B,C))), 'extra_generator': extra}


def local_witness(m, n, p, xyz, d=None):
    x,y,z = map(F, xyz)
    assert m*x*y*z == n*(x*y+x*z+y*z)
    assert all(valuation(a,p)[0] >= 0 for a in (x,y,z))
    delta = x*y*z
    if d is None:
        assert delta > 0
        d = sf(delta.numerator*delta.denominator)
    assert local_square(delta/d, p)
    assert hilbert(-x/z,-y/z,p) == -1
    k = F(n,m*d)
    return {'m':m,'n':n,'place':p,'xyz':list(map(str,(x,y,z))), 'd':d,
            'k':str(k),'extra_generator':square_rational(k),
            'beta_at_place':-1,'beta_at_infinity':-1,
            'other_finite_lifts':'(0,1,-1)',
            'gamma_rule':'choose real lift sign to cancel finite gamma sum' if square_rational(k) else 'no extra generator'}


def run():
    dyadic = dyadic_scan(16)
    assert not dyadic[0]['alpha_minus_twist_classes']
    assert set(dyadic[1]['alpha_minus_twist_classes']) == {'0:1','0:3','0:5','0:7'}
    assert set(dyadic[2]['alpha_minus_twist_classes']) == {'0:1','0:3','0:5','1:1','1:3','1:5','1:7'}
    # Higher b follows mathematically by scaling these seven n=4 witnesses.
    rows = [check_rational_lift(n, first_solution(4,n)) for n in list(range(2,2001))+[3361]]
    controls = [local_witness(8,131,131,(F(-131,254),1,1),262),
                local_witness(8,131,131,(F(-131,254),1,1),786),
                local_witness(8,241,241,(F(-1687,1872),1,7),3374)]
    pw15 = [1,2,3,4,8,16,17,19,23,31,34,47,53,61,79,113,122,137,151,197,226,233,271,541,1103,1171,1367,4201,6301,12601,16831,20521]
    for n in pw15:
        b,n0 = valuation(n,2)
        assert n0.denominator == 1
        n0 = int(n0)
        s = 2*n0//15+1
        while s % 4 != (3*n0*pow(15,-1,4)) % 4:
            s += 1
        scale = 2**b
        controls.append(local_witness(15,n,2,(scale*s,scale*s,F(scale*n0*s,15*s-2*n0))))
    controls.append(local_witness(4,3361,3361,(11,10083,F(-110913,9962)),1))
    old = json.loads(Path('data/z45_etale_descent/check.json').read_text())
    trap = next(r for r in old['solutions_and_lifts'] if r['m'] == 4 and r['n'] == 3361)
    assert 1 not in trap['twists']
    assert all(twist_survives(3361,d) for d in trap['twists'])
    for n,d in [(1,1),(2,2),(4,7),(241,241),(3361,3361)]:
        assert not twist_survives(n,d)
    out = {'sanity_count':len(rows),'extra_generator_sanity_count':sum(r['extra_generator'] for r in rows),
           '3361_prior_census_twists_checked':trap['twists'],
           'obstructed_twist_examples':[[1,1],[2,2],[4,7],[241,241],[3361,3361]],
           'sanity_lifts':rows,'dyadic_local_witnesses':dyadic[:3],
           'failure_controls':controls,
           'scope':'Exact witnesses and Hilbert evaluations; all-n and Brauer completeness proofs are in BRAUER_TWISTS.md. Failure counts for 8/n and 15/n are prior certified/literature inputs, not re-enumerated here.'}
    dest=Path('data/z46_brauer_twists/check.json')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'sanity_lifts'},indent=2))


if __name__ == '__main__':
    run()
