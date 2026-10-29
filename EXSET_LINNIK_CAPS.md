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

PENDING. Audit squarefreeness, diagonal loss, length optimization and smooth-number counting.

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
