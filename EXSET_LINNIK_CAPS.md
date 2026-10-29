# EXSET_LINNIK_CAPS — wave z51, lane 2b (`lcaps`)

**Status: working skeleton. ES remains OPEN.** All proofs here are internal and unrefereed.
This lane follows z48–z51 CONTEXT, with z51 binding. No merge without parent approval.

## 0. Outcome and review ledger

| Round | Target | Status | Hostile Opus review |
|---|---|---|---|
| 1 | Quadratic large sieve for confined squarefree products; cap threshold | PENDING | PENDING |
| 2 | Exact scope and endpoint of pointwise confinement | PENDING | PENDING |
| 3 | Restricted-window / restricted-mute relaxations | PENDING | PENDING |
| 4 | Prime census through 10⁸ and independent controls | PENDING | PENDING |

## 1. Definitions, inherited facts, and non-CRT input

**Definitions.** ES^{(y,e)}(n) means 4/n=1/x+1/y+1/z with x,y positive integers,
z positive rational, reduced denominator den(z)=r², r odd, (r,n)=1, rad(r)|y,
and v_s(r)≤e. The y in this notation is a denominator, not a smoothness parameter.
Write e*(n) for the least such e; e*=0 is exactly ES. Below Y denotes a smoothness cutoff.

For p≡1 (8), let q₃(p) be the least prime q≡3 (4) with (q/p)=−1. Write
E(X,Y)={p≤X prime: p≡1 (8), (q/p)=1 for every prime q≤Y, q≡3 (4)}.
These p cannot equal a generating q, since their classes modulo 4 differ.

**Inherited PROVED input, not a new claim.** `CAP_DOWN` Theorem 1.2 and Proposition 1.3
produce a Type II-shaped capped solution at each such q. Put K=(p+q)/4 and choose an odd
prime s with b=v_s(K) odd and (s/q)=−1. Such s exists for p≡1 (8), including even K.
With j=ord_q(s)/2 (odd), d=Ks^j and A=(K+d)/q,

    (x,y,z)=(K,pA,pKA/d),   cap=max(0,(j−b)/2)≤(q−3)/4.          (1.1)

All overflow is at **one odd prime s**. The excluded 2-adic windows for p≡5 (8) are not
used: those p already satisfy classical ES. Therefore

    {p≤X:e*(p)>e} ⊆ E(X,4e+3).                                (1.2)

This is an implication, not an equivalence. Global e* is zero throughout the verified
prime range, so informative numerical quantities are q₃ and *restricted-window* caps.

**Non-CRT input.** Heath-Brown, “A mean value estimate for real character sums”,
Acta Arith. 72 (1995), 235–275, Theorem 1 / Corollary 1, gives for every η>0

    Σ_{m≤X, m odd squarefree} |Σ_{a≤N, a odd squarefree} c_a(a/m)|²
       ≪_η (XN)^η(X+N) Σ_a |c_a|².                            (HB)

Primary PDF checked: https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf, pp. 237–238.
Both squarefreeness restrictions are essential. The prime p is a **row modulus**;
this is not an integer-avoider CRT evaluation, so z51 G1 and the square floor do not cap it.
No claimed strengthening of HB is used. For nonsquarefree columns its Corollary 2
has the square-class energy Σ_{ab=square}|c_a c_b|, not the ordinary ℓ² norm.

**Literature check (Assessment, limited search).** A fresh search for 2026 ES exceptional-set
improvements found no replacement for the published Vaughan bound. Pomerance–Weingartner,
https://arxiv.org/html/2511.16817v2, introduction and Theorem 1.3, still cite Vaughan;
this is not a proof that no later result exists. Liu, https://arxiv.org/html/2505.09637v1,
restates HB with its square-class energy and gives an explicit variant. No new theorem
from that preprint is needed. Retrieved text is in `data/z51_lcaps/literature_*.txt`.

## 2. Round 1: confinement and the quadratic large sieve

### Theorem 2.1 — quadratic Linnik confinement (PROVED relative to HB)

Let S be any set of odd primes, all ≤Y, and let E be odd primes p≤X, p∉S, such that
(q/p)=1 for every q∈S. Let B_S(N) be the number of squarefree positive integers ≤N
supported on S (including 1). For every η>0,

    |E| ≪_η (XN)^η (X+N)/B_S(N).                              (2.1)

**Proof.** Take c_a=1 on these squarefree integers and zero elsewhere in HB. Each row
p∈E has inner sum exactly B_S(N), since every factor is a unit quadratic residue.
Its squared contribution is B_S(N)², while the coefficient norm is B_S(N). Drop every
other nonnegative row and divide. ∎

### Corollary 2.2 — cap threshold log^{1+ε}, exponent 1/A (PROVED)

For every fixed A>1,

    #E(X,(log X)^A) ≤ X^{1/A+o(1)},
    #{p≤X:e*(p)>(log X)^A/4} ≤ X^{1/A+o(1)}.                  (2.2)

The meaning of o(1) is: for every δ>0 the bound is O_{A,δ}(X^{1/A+δ}).
No effective uniform dependence of the HB constant on δ is asserted.

**Proof.** Let L=log X, Y=L^A, k=π(Y;4,3) and r=⌊L/log Y⌋. The products of r distinct
primes q≤Y, q≡3 (4), are ≤X and distinct. By the fixed-modulus PNT,

    B_S(X) ≥ binom(k,r) ≥ (k/r)^r,
    log(k/r)=(A−1)log L+O_A(1),
    log B_S(X) ≥ (1−1/A)L−o(L).

Apply (2.1) with N=X, then take any fixed η arbitrarily small. Equation (1.2) transfers
the result to caps. This halves the old exponent 2/A and gives a fixed power saving
for every A>1, not just A>2. No improvement in the pointwise cap identity is required. ∎

### Corollary 2.3 — one overflowing prime and a short window (PROVED)

Outside at most X^{1/A+o(1)} primes p≡1 (8), a solution exists with

    x=(p+q)/4,  q≤(log X)^A prime, q≡3 (4),
    den(z)=s^{2h},  s odd prime dividing x,  0≤h≤(q−3)/4.

Allow den(z)=1 when h=0. This is the actual witness (1.1), not merely a statement
about e*. Thus the improvement still holds after simultaneously imposing a polylog
window and **at most one p-dependent mute prime**. Its relation to ES is discussed
in §4; s is not a fixed prime independent of p.

**Independent checks.** `scripts/z51_lcaps_toy.py` compares the squarefree-product set
with an independent factorization enumeration, checks every confined character sum,
and checks the binomial construction. The analytic constant in HB is unspecified;
a finite calculation cannot certify its asymptotic inequality. The first toy rows had no
confined primes; Opus identified this vacuity, and the retained rows now assert nonempty E.

**Round-1 Opus verdict: SOUND, minor repairs applied.** Reviewer independently rebuilt
4466 exact rational witnesses for p≡1 (8), p≤200000, with zero violations. The tool rejects
`:high` as part of a model ID; the actual review used `anthropic/claude-opus-5-5`, `mode=deep`.
Session: `2026-10-29T22-39-32-614Z_01a189d1-8706-70d6-863f-0bde7e771866.jsonl`.

**Novelty qualification (Assessment).** HB smooth-product amplification is a known
least-nonresidue technique (Baier 2006, also discussed by Lau–Wu 2008); the analytic
argument is not new. What is added here is its complete restricted-prime adaptation,
the cap exponent 1/A, and the simultaneous one-mute/short-window conclusion. This
strengthens CAP_BOUNDED; CAP_INTERPOLATION already sketched the A>1 range by a different
method. Neither the existing sketch nor (2.2) establishes a power saving at A=1.

## 3. Round 2: the forcing threshold and its exact scope

PENDING. Separate a sharp single-window algebraic threshold from any unproved global ES barrier.

## 4. Round 3: intermediate relaxations and further attacks

PENDING. State precise implications to/from ES and cap relaxations; do not label an incomparable
window restriction as an unconditional improvement of ES.

## 5. Computation and controls

PENDING. Scripts `scripts/z51_lcaps_*`; data `data/z51_lcaps/` (<20 MB).
Every run has a timeout and an 8 GB virtual-memory ceiling; no Cartesian-product arrays.
Hard-prime and 14 R-zero controls, odd squares, numerator 8 where applicable.

## 6. Final assessment and exact remaining gap

PENDING. Labelled summary, review verdicts, then WAIT; no merge.
