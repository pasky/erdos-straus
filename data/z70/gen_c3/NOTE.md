# Quick check of REVIEW_GEN open candidate 3 (representation-neighbour seeds) — orchestrator, 2026-11-10

EVIDENCE only (small range, one engine, Python). d = 1, primes p ≡ 1 (8), 1000 < p < 40000 with G₁(p) ≠ ∅ (977 primes;
G₁ enumerated with a ≤ 3√p, so possibly incomplete → hit rates are lower bounds).
Rule: p = x² + 4a_c²; for a = a_c ± 1 take the least odd prime q | p + 4a² with (p/q) = −1; output the classes of
[q, ±4a, (p + 4a²)/q]. Hit = some output class lies in G₁(p).

| seed a | hit rate |
|---|---|
| a_c ± 1 (candidate 3) | 0.743 |
| two random a ≤ √p (control) | 0.702 |
| a_c + 5, a_c + 9 (control) | 0.752 |

Verdict (Assessment): the representation neighbourhood carries no information; the ~70–75 % rate is generic to
"least non-residue prime factor of p + 4a²" seeds; coverage < 1, so not a generative map. Candidate 3 can be dropped.
Scripts: `scripts/z70_c3_repneighbour.py`, `scripts/z70_c3_control.py`.
