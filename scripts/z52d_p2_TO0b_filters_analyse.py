"""z52d pass2 TO0b: analysis of scripts/z52d_p2_TO0b_filters.c output (data/z52b/pass2/TO0b/filters_2e4.tsv).
Columns: p, total, #no-den-1mod3 (Z0200), #p not | x (Z0202), #z<=p^2/8 (Z0201), #chain x|y|z (Z0216), min z/p^2."""
rows = [l.split() for l in open('data/z52b/pass2/TO0b/filters_2e4.tsv')]
R = [dict(p=int(a), tot=int(b), n13=int(c), pnx=int(d), sz=int(e), chain=int(f), best=float(g)) for a, b, c, d, e, f, g in rows]
isprime = lambda n: n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
print('primes 5..20000 (all):', len(R))
# Z0200
z200 = [r['p'] for r in R if r['n13'] == 0]
print('Z0200 primes with NO solution avoiding denominators = 1 mod 3:', z200)
# Z0201
z201 = [r['p'] for r in R if r['sz'] == 0]
print('Z0201 primes with NO solution with max denominator <= p^2/8: count', len(z201), 'first', z201[:20])
print('   min ratio c(p)=min max/p^2 over solutions: smallest 8:', sorted(((r['best'], r['p']) for r in R))[:8])
print('   c(p) for p in {5,13,17,29}:', [(r['p'], round(r['best'], 4)) for r in R if r['p'] in (5, 13, 17, 29, 1201, 21169)])
# Z0202
z202 = [r['p'] for r in R if r['pnx'] == 0]
print('Z0202 primes where every solution has p | x (count of p with no solution with p not| x):', len(z202), z202[:12])
# Z0216 chain world
chain_fail = [r['p'] for r in R if r['chain'] == 0]
print('Z0216 chain-world failures (no x|y|z solution), count', len(chain_fail), 'residues mod 24:', {m: sum(1 for p in chain_fail if p % 24 == m) for m in sorted({p % 24 for p in chain_fail})})
p1 = [r['p'] for r in R if r['p'] % 24 == 1]
print('   primes = 1 mod 24 below 2e4:', len(p1), ' of which chain-fail:', sum(1 for p in p1 if p in chain_fail))
