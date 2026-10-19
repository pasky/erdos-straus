"""Exact, bounded fixtures for z45_interlacing_stable; run with a shell memory cap.
No dense matrix exceeds one nontrivial tree component (asserted <= 150).
"""
import json
from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path

import sympy as s

OUT = Path('data/z45_interlacing_stable')
x, z = s.symbols('x z')


def edges_parent(n):
    out = []
    for v in range(2, n + 3):
        u = (-n) % v
        if u and (n + u + v) % (u * v) == 0:
            out.append((u, v, (n + u + v) // (u * v)))
    return out


def edges_divisors(n):
    out = []
    for u in range(1, n + 3):
        for v in s.divisors(n + u):
            if u < v <= n + 2 and (n + u + v) % (u * v) == 0:
                out.append((u, int(v), (n + u + v) // (u * v)))
    return sorted(out)


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return c


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] += v * w
    return c


def forest_polynomial(n, edges):
    adj = defaultdict(list)
    for u, v, _ in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = set()
    total = [1]
    component_data = []
    for root in sorted(adj):
        if root in seen:
            continue
        order, parent = [root], {root: None}
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    assert v not in parent, 'not a forest'
                    parent[v] = u
                    order.append(v)
        seen.update(order)
        free, allm = {}, {}
        for u in reversed(order):
            children = [v for v in adj[u] if parent.get(v) == u]
            a = [1]
            for v in children:
                a = mul(a, allm[v])
            b = a[:]
            for chosen in children:
                q = free[chosen]
                for v in children:
                    if v != chosen:
                        q = mul(q, allm[v])
                b = add(b, [0] + q)
            free[u], allm[u] = a, b
        coeff = allm[root]
        total = mul(total, coeff)
        # Independent determinant/characteristic polynomial check per component.
        assert len(order) <= 150
        pos = {v: i for i, v in enumerate(order)}
        a = s.zeros(len(order))
        signed = s.zeros(len(order))
        for u in order:
            for v in adj[u]:
                a[pos[u], pos[v]] = 1
                signed[pos[u], pos[v]] = -1 if (u + v) % 3 else 1
        expected = sum((-1)**j * c * x**(len(order) - 2*j)
                       for j, c in enumerate(coeff))
        assert a.charpoly(x).as_expr() == s.expand(expected)
        assert signed.charpoly(x).as_expr() == s.expand(expected)
        component_data.append({'vertices': sorted(order), 'matching_coefficients': coeff})
    assert len(total) == 1 or total[1] == len(edges)
    # Every vertex, including isolates, is included in the x exponent.
    reduced = sum((-1)**j * c * x**(2*(len(total)-1-j))
                  for j, c in enumerate(total))
    return {'matching_coefficients': total,
            'zero_power': n + 2 - 2*(len(total)-1),
            'reduced_characteristic_factorization': str(s.factor(reduced)),
            'nontrivial_components': component_data}


def target_rank(n, t):
    fac = {int(q): int(e) for q, e in s.factorint(t*n + 1).items()}
    coeff = [0] * (sum(fac.values()) + 1)
    hits = []
    for d in s.divisors(t*n + 1):
        if d % t == t - 1:
            rank = sum(s.factorint(d).values())
            coeff[int(rank)] += 1
            hits.append(int(d))
    while len(coeff) > 1 and coeff[-1] == 0:
        coeff.pop()
    poly = s.Poly(sum(c*z**j for j, c in enumerate(coeff)), z)
    # Count real roots with multiplicity using exact isolating intervals.
    real = None if poly.is_zero else sum(m for interval, m in s.polys.polytools.intervals(poly)) == poly.degree()
    tau = int(s.divisor_count(t*n + 1))
    theta = s.Rational(len(hits), tau)
    # Uniform-divisor selection: good root 0, bad root 1.
    linear_expectation = x - (1 - theta)
    # A natural quadratic-character matrix family A_d = chi_4(d) I_2.
    chi_mean = s.Rational(sum(1 if d % 4 == 1 else -1
                             for d in s.divisors(t*n + 1)), tau)
    character_expectation = x*x - 2*chi_mean*x + 1
    return {'t': t, 'N': t*n+1, 'factorization': fac, 'coefficients': coeff,
            'polynomial': str(poly.as_expr()), 'real_rooted': real, 'divisors': hits,
            'tau': tau, 'linear_expectation': str(linear_expectation),
            'character_matrix_expectation': str(character_expectation)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cases = [(4, n) for n in [409, 577, 3361, 193, 2521, 5569, 9601,
                              9, 25, 49, 169, 529, 1089, 1097]]
    cases += [(8, 131), (8, 241)]
    records = []
    for k, n in cases:
        edges = edges_parent(n)
        assert sorted(edges) == edges_divisors(n)
        unit = [e for e in edges if gcd(e[0]*e[1], n) == 1]
        cut = [e for e in unit if int(s.jacobi_symbol(e[0], n))*int(s.jacobi_symbol(e[1], n)) == -1]
        line = [e for e in edges if e[2] % k == 0]
        union = [e for e in edges if any(a % k == 0 for a in e)]
        # Exact certificates for the t = kC line.
        for u, v, t in line:
            c = t // k
            assert s.Rational(k, n) == (s.Rational(1, u*v*c)
                    + s.Rational(1, n*v*c) + s.Rational(1, n*u*c))
        levels = [target_rank(n, t) for t in sorted({e[2] for e in line})]
        assert sum(sum(q['coefficients']) for q in levels) == 2*len(line)
        if isqrt(n)**2 == n or k == 8:
            assert not line
        if isqrt(n)**2 == n:
            assert not cut
        if k == 8:
            assert not union
        # At 4/n, n = 1 mod 4, unit-endpoint sign criterion agrees with five slices.
        if k == 4:
            five = [e for e in unit if any(a % 4 == 0 for a in
                    (*e, e[0]*e[2]-1, e[1]*e[2]-1))]
            assert five == cut
        record = {'k': k, 'n': n, 'is_prime': bool(s.isprime(n)),
                  'edges': len(edges), 'unit_edges': len(unit), 'cut_edges': len(cut),
                  'R_k': 2*len(line), 'two_line_edges': len(union),
                  'forest': forest_polynomial(n, edges),
                  'cut': forest_polynomial(n, cut),
                  'line': forest_polynomial(n, line), 'occupied_levels': levels}
        records.append(record)
        print(k, n, 'E', len(edges), 'cut', len(cut), 'R', 2*len(line),
              'mu_F=', f"x^{record['forest']['zero_power']}*({record['forest']['reduced_characteristic_factorization']})")
        print('  mu_cut=', f"x^{record['cut']['zero_power']}*({record['cut']['reduced_characteristic_factorization']})")
        for level in levels:
            print('  level', level['t'], level['factorization'], level['polynomial'], level['real_rooted'])
    # Arithmetic unstable parity fibre at prime 1097, level 4.
    assert s.isprime(1097)
    toy = target_rank(1097, 4)
    assert toy['polynomial'] == '4*z**3 + 4*z'
    # Two leaves are individually real-rooted but their mixture is not.
    assert s.expand(((x - 1)**2 + (x + 1)**2)/2) == x*x + 1
    (OUT / 'results.json').write_text(json.dumps(records, indent=2) + '\n')
    print('All exact checks passed; records:', len(records))


if __name__ == '__main__':
    main()
