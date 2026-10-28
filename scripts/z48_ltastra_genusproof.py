"""Finite identity checks for the conditional genus-main-term argument.
Reuses the existing square-unit test; independently checks L(1) normalization
by reduced forms versus the exact odd-character class-number sum.
No numerical verification of a zero-free hypothesis is claimed.
"""
from fractions import Fraction
from math import gcd, isqrt, log, pi, sqrt, exp, prod
from pathlib import Path
import csv
import json
from sympy import factorint, jacobi_symbol, isprime
from z30_check_forms import is_sq_unit

DATA = Path(__file__).resolve().parents[1]/'data/z48_ltastra'


def squarefree(n):
    return all(e == 1 for e in factorint(n).values())


def char(a, q):
    return int(jacobi_symbol(a,q))


def chi4(a):
    return 0 if a%2 == 0 else (1 if a%4 == 1 else -1)


def class_number_forms(D):
    assert D < -4 and D%4 == 0
    total = 0
    for a in range(1,isqrt((-D)//3)+1):
        for b in range(0,a+1,2):
            if (b*b-D)%(4*a):
                continue
            c = (b*b-D)//(4*a)
            if c<a or gcd(gcd(a,b),c)>1:
                continue
            total += 1 if b == 0 or b == a or a == c else 2
    return total


def class_number_character(p,u):
    q = 4*p*u
    cp = [char(a,p) for a in range(p)]
    cu = [char(a,u) for a in range(u)]
    total = sum(a*chi4(a)*cp[a%p]*cu[a%u] for a in range(1,q,2))
    assert total%q == 0
    return -total//q


def main():
    tests = 0
    ps = (5,13,29,101,193,409,577,5569,9601,9,25,49,121)
    for p in ps:
        for u in (1,5,13,17,21,29):
            if gcd(p,u)>1:
                continue
            ls = list(factorint(u))
            s = 2**(len(ls)+1)
            is_square = isqrt(p)**2 == p
            if is_square:
                eps_eta0 = -char(2,p)*char(2,u)*prod(char(-2*p,l) for l in ls)
                assert eps_eta0 == -1
            for w in range(1,301,2):
                if gcd(w,p*u)>1 or not squarefree(w):
                    continue
                profile = chi4(w) == -char(2,p)*char(2,u)
                profile &= all(char(w,l)==char(-2*p,l) for l in ls)
                split = all(char(-4*u*p,l)==1 for l in factorint(w))
                if is_square and split:
                    assert chi4(w)*char(w,u) == 1  # B_eta0 = B_principal.
                q = 8*u*w
                a = -u-2*w
                actual = is_sq_unit(p*a%q,q)
                assert actual == (profile and split), (p,u,w)
                # Expand the full quadratic projector, including its 2-adic sign.
                products = [(-char(2,p)*char(2,u))*chi4(w)]
                products += [char(-2*p,l)*char(w,l) for l in ls]
                total = 0
                for mask in range(s):
                    term = 1
                    for j,t in enumerate(products):
                        if mask>>j&1:
                            term *= t
                    total += term
                assert Fraction(total,s) == int(profile)
                tests += 1
    rows = []
    for p in (193,409,577,5569,9601):
        us = [u for u in range(1,isqrt(p)+1,4) if u**8>p and u**3<=p and squarefree(u)]
        av = smoothed = pole = 0.0
        for u in us:
            D = -4*p*u
            h = class_number_forms(D)
            assert h == class_number_character(p,u), (p,u,h)
            L1 = pi*h/sqrt(-D)
            av += L1/u
            # Exact finite Euler-factor residue, then smoothed subcount.
            residue = Fraction(2,3)*Fraction(p,p+1)
            phi = u
            for l in factorint(u):
                residue *= Fraction(l,l+1)
                phi = phi//l*(l-1)
            residue = float(residue)*6/pi**2*L1
            pole += residue/phi*.25*log(p)
            for w in range(1,p//(8*u)+1,2):
                if gcd(w,p*u)>1 or not squarefree(w):
                    continue
                q = 8*u*w
                if not is_sq_unit(p*(-u-2*w)%q,q):
                    continue
                phiw = w
                for l in factorint(w):
                    phiw = phiw//l*(l-1)
                weight = 2*2**(len(factorint(u))+len(factorint(w)))/(phi*phiw)
                smoothed += weight*(exp(-w/p**.5)-exp(-w/p**.25))
        rows.append({'p':p,'u_values':us,'harmonic_L1_sum':av,
            'first_square_asymptotic':2/pi**2*(1/3-1/8)*log(p),
            'smoothed_admissible_subcount':smoothed,'pole_expression':pole})
    sample = [(float(r['Mgen'])/log(int(r['n']))**2,int(r['n']))
              for r in csv.DictReader((DATA/'detail.csv').open()) if isprime(int(r['n']))]
    assert all(value >= 2/pi**4 for value,p in sample)
    result = {'genus_projection_checks':tests,'sample_prime_count':len(sample),
        'minimum_sample_Mgen_over_log2':min(sample),'conditional_asymptotic_constant':2/pi**4,
        'small_p_diagnostics':rows,
        'warning':'finite asymptotic expressions can overestimate subcounts; no finite threshold or zero-free hypothesis is certified'}
    (DATA/'genusproof.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:',tests,'genus/projector identities, class-number cross-checks,',len(sample),'sample genus bounds')


if __name__ == '__main__':
    main()
