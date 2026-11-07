# Z61 PIGEON — hostile non-author audit of board finalist F1

**ES remains OPEN.** Lane PIGEON, wave z61. Labels: PROVED (mathematical statement),
CERTIFIED (bounded exhaustive integer computation), EVIDENCE (empirical interpretation),
CONDITIONAL (named unproved hypothesis), CONJECTURE, Assessment.

## Initial bank (audit in progress)

**PROVED.** For n ≡ 1 (4), ρ ≡ 3 (4), M = (n+ρ)/4, let S be the residues of
positive divisors of M coprime to ρ. If |S| > φ(ρ)/2, choose divisors u,v with
u ≡ −v (ρ). With g = gcd(u,v), a = u/g, b = v/g are positive, coprime,
a+b ≡ 0 (ρ), and ab = lcm(u,v)/g divides M. Thus c = (a+b)/ρ and d = M/(ab)
are positive integers satisfying 4abcd = a+b+nc. The coprimality to ρ is essential.

**PROVED.** At prime ρ, a witness at that level exists iff S ∩ (−S) is nonempty
or ρ² divides M. The unit case follows by the preceding gcd cancellation.
Otherwise ρ divides both a,b; conversely ρ² | M permits a=b=ρ,c=2,d=M/ρ².

**CERTIFIED.** Independent script `scripts/z61_pigeon_audit.py` reproduces
18,217/18,507 = 98.4% least witnesses explained by half-density, and 0/9 among
primes with least level ≥50. Extending *all* cutoff failures through the complete
bound ρ ≤ (p+4)/3 confirms exactly 17 primes ≤2,000,000, p ≡1 (24), with no
pigeonhole level anywhere. Data: `data/z61/pigeon/census.csv`, `census_summary.json`.

The original `/tmp/f1_census.py` only scans through ρ=403 when called with cutoff
400; its output alone does not certify global absence. The present independent
extension supplies that missing certification (and uses the actual cutoff 400).

New-lemma checks, separate from the existing z59 equation checks: 41,917 levels,
including prime-level nonunits and squares, plus 12,998 factor-colour comparisons;
all exact assertions pass. See `data/z61/pigeon/checks.json`.

Reproduce (stdlib only; each invocation bounded):

```sh
ulimit -v 4000000
timeout 1800 uv run --no-project python scripts/z61_pigeon_audit.py check --limit 100000
timeout 1800 uv run --no-project python scripts/z61_pigeon_audit.py census
```

Pending this first checkpoint: source-pinned Linnik/Burgess audit, full screen
certificates, detailed novelty map and proposed FRONTIER paragraph. No merge.
