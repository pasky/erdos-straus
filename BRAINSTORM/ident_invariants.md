# BRAINSTORM / ident_invariants — do non-congruence invariants of p steer ES solutions? (O145 (a))

Labels as in DISCOVERIES.md. ES is not solved; nothing here proves any case of it.

## 1. Idea

Theorems M/C (POINTWISE_SIZE) kill every bounded procedure whose inputs are congruence data and
formal factorisations. They leave open (E2) non-formal integers (`n_p`, `⌊p^θ⌋`, orders, units) and
(E3) fixed non-abelian Frobenius information. A *non-polynomial family* would be a rule
"the ES solution of p is built from invariant X(p)" with X outside congruence data, e.g.

* the fundamental unit `ε_p = (x+y√p)/2` of Q(√p) (Pell / Lucas sequences, continued fraction of √p);
* the class number `h(−4p)`;
* non-abelian Frobenius bits: is 2 a 4th power mod p (`p = u²+64v²`), is 2 or 3 a cube mod p;
* the least non-residue `n_p` (E2; already studied in POINTWISE_SIZE §9).

For such a rule to prove ES it would have to (i) produce solutions at every large hard prime, so in
particular (ii) the invariant would have to *predict* where solutions are. Test (ii) first.

## 2. Literature anchor

* Pell-type parametrisations of 4/n: not found in the literature checked by the campaign
  (LITERATURE_2026.md); Schuh, arXiv:2503.11672 rewrites ES(p) for p ≡ 1 (4) as two ternary
  equations ("Pythagorean primes"), with no unit/class-number input and no proof (read 2026-10-12).
* Class number formula `h(−4p) = (2√p/π)·L(1, χ_{−4p})`, `L(1,χ) = ∏_ℓ (1−χ(ℓ)/ℓ)^{−1}` (standard).
* Gauss / Dirichlet: 2 is a quartic residue mod p ≡ 1 (8) iff `p = u² + 64v²`; 2 is a cube mod p ≡ 1 (3)
  iff `p = u² + 27v²` (standard; from memory, not re-verified — used only as computed predicates here).

## 3. Barrier screen

* **Pell/unit families are empty for Type II.** *Lemma 3.1 (PROVED, elementary).* If p is prime and
  `p ≡ 1 (mod 4)`, there is no Type II solution with `f = f'` (i.e. `f² = 4c²dp + 1`,
  `f ≡ −1 (mod 4cd)`). *Proof.* Put `f + 1 = 4cdk`. Then `(f−1)(f+1) = 4c²dp` gives
  `2k(2cdk − 1) = cp`. As `gcd(c, 2cdk−1) = 1`, `c | 2k`; write `2k = cj`, so `j(2cdk−1) = p`.
  `j = p` forces `cdk = 1`, `2 = p`; so `j = 1`, `c = 2k`, `p = 4dk² − 1 ≡ 3 (4)`. ∎
  Solutions `x² − py² = ±1` (powers of ε_p) are exactly the `f = f'` points of the Type II
  identity `ff' − 4c²dp = 1` with `4c²d = y²`, so **units of Q(√p) never give Type II solutions for
  p ≡ 1 (4)**; any unit-based rule must use units of *other* orders/fields, i.e. other slices — B2.
* **Class number = Euler product of congruence data (B1, Haar/CRT).** `χ_{−4p}(ℓ) = (−1/ℓ)(ℓ/p)`, so
  `h(−4p)/√p` is an (infinite) product of Legendre symbols `(ℓ/p)` — a CRT/Haar majorant quantity,
  exactly the kind excluded by Prop A / Thm F as a *certificate*; it can only correlate with solution
  counts through the QR pattern of p. Confirmed numerically (§4: its partial t-statistic falls from
  8.5 to 2.5–2.9 when the QR pattern mod primes ≤ 400 is added to the baseline).
* **E3 bits.** Chebotarev: for K = Q(i, 2^{1/4}) (or the S₃-fields of x³−2, x³−3), the Frobenius of p in K
  is asymptotically independent of `p mod L` once `K ∩ Q(ζ_L)` is fixed, and the e-slice events are
  congruence events on p (divisibility of `(p+e)/4`, `(pe+1)/4` by fixed primes ℓ ⇔ `p mod ℓ`). So the
  *expected* influence on any bounded-parameter success indicator is zero (Assessment; a proof would
  need a joint Chebotarev–Bateman–Horn statement over the formal primes, cf. POINTWISE_SIZE (E3)).
* **B5 (odd squares).** None of the invariants is defined at `n = m²` in a way that creates Type I/II
  solutions there (ET Prop 1.6); a rule "solution built from ε_p" must contain the step "the resulting
  integer has a divisor in class −1 mod 4cd", which is the lottery (B2) and is false at squares.
* **B2/B6.** All tested rules, once X(p) is fixed, ask whether a specific integer has a divisor in a
  moving class — B2. The experiment below is a population statistic (B6): even a positive correlation
  would say nothing at a single p; it is used only as a *falsification* screen.

## 4. Experiment (EVIDENCE)

`scripts/bs_ident_features.c` (gcc -O2): for every Mordell-hard prime (p ≡ 1 (24), square mod 5, 7)
computes `n_p`, `h(−4p)` (reduced forms), `log ε` of Z[√p] (continued fraction), the bits
q2 (2 quartic), c2 (2 cubic), c3 (3 cubic), and the e-slice lottery data of LONGSHOT_PIGEONHOLE
Lemma 1.1 for `e ≤ 200`: `S = #{successful e}` (Type I + II), `e_min^{II}`, `e_min^{I}`.
`scripts/bs_ident_analyze.py TSV QMAX` regresses `log(1+S)`, `log e_min` on a congruence baseline
(log p and the QR indicators `(p/q)`, 11 ≤ q ≤ QMAX) and reports each invariant's partial t-statistic
with a within-sample permutation null (200 shuffles). Outputs: `data/bs_ident/analyze_*.txt`.

| sample | target | h/√p | log ε/√p | q2 | c2 | c3 |
|---|---|---|---|---|---|---|
| 6628 primes ≤ 3·10⁶, QMAX 43 | log(1+S) | **+8.47** | −0.86 | −1.65 | +0.95 | −0.11 |
| same, QMAX 400 | log(1+S) | +2.48 | +0.31 | −1.94 | +0.73 | −0.13 |
| 17769 primes in (3·10⁶, 1.2·10⁷], QMAX 400 | log(1+S) | +2.87 | −0.67 | **+1.47** | −0.07 | +1.72 |
| same | log e_min^{II} | −2.10 | +1.28 | −0.26 | −0.43 | −0.91 |
| same | log e_min^{I} | +0.22 | −0.23 | −0.85 | −0.37 | +0.67 |

Reading: only h(−4p) carries signal, and it decays as more of its own Euler factors enter the
baseline (8.5 → 2.5) — it is a proxy for the non-residue pattern, i.e. congruence data. The quartic
bit's marginal effect in the first sample (−1.94, perm-p 0.04) reverses sign on the independent
second sample (+1.47); with 15 tests per sample nothing survives a multiple-testing correction.
Regulator/CF-of-√p and cubic bits: null. Every hard prime ≤ 1.2·10⁷ has S ≥ 9 (mean 24 for e ≤ 200).

## 5. Viability Assessment

**COLLAPSES to B2 (and B1 for h(−4p)).** Step at which it fails: once the invariant is fixed, the
solution still requires a divisor of a specific integer in a moving class (B2); units of Q(√p) give
no Type II solution at all for p ≡ 1 (4) (Lemma 3.1, PROVED); class numbers are Euler products of
congruence data (B1). The data show no non-congruence invariant predicting the ES lottery beyond
the QR pattern (EVIDENCE, 2.4·10⁴ hard primes ≤ 1.2·10⁷).
By-products: Lemma 3.1 (PROVED, trivial; likely folklore). The null result on E3 bits is EVIDENCE
for the Assessment that fixed non-abelian Frobenius information is irrelevant to ES success.
