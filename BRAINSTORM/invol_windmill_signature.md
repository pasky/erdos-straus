# Brainstorm O152(a): the "windmill signature" of a parity proof, and a test on all n

Status: **ES is not solved here.** Labels as in DISCOVERIES.md. Builds on `WINDMILL.md` (earlier wave,
all negative); this memo does not repeat its catalogue but adds (i) a precise statement of *why* a
parity proof escapes B1/B3/B5 and what single property it would still need, and (ii) a new test that uses
composite n (the earlier wave tested primes only).

## 1. Idea

**1.1 What a windmill proof actually proves.** Zagier: `S(n)={(x,y,z)∈ℤ³_{>0}: x²+4yz=n}`, the
windmill σ is piecewise in `O(x²+4yz)(ℤ)` and `τ:(x,y,z)↦(x,z,y)`. For *every* n (not only primes),

  `#{x²+4y²=n, x,y>0} ≡ #Fix τ ≡ |S(n)| ≡ #Fix σ = #{n=u·v: u<v, u≡v (mod 4)}  (mod 2)`   (Z)

(σ fixes exactly `x=y`, where `n=x(x+4z)`; squares `n=u²` contribute nothing since z>0). Primality is
used **only** in evaluating the right side: for `n=p≡1 (4)` it has exactly one term `1·p`.

General shape (folklore, elementary). If σ is piecewise integral-affine with pieces preserving a quadratic
Q, each piece's fixed set is an affine sublattice L on which Q restricts to a form of lower rank; on a
rank-2 piece this is a binary form `F_i`, so `#Fix σ = Σ_i r_{F_i}(n; congruence/positivity conditions)`.
If `F_i` has square discriminant (Zagier: `x(x+4z)`), `r_{F_i}(n)` is a **divisor-type** count
`D_φ(n)=Σ_{n=uv, u<v} φ(u mod M, v mod M)` (+ a square term). A windmill proof of a statement about
weighted ES counts `W(n)=Σ_{sol of 4/n} w(sol)` therefore has the form

  `W(n) ≡ D_φ(n)  (mod 2)  for all n in a congruence-defined family`,                (W)

and concludes `W(p)≥1` for primes p with `φ(1,p mod M)=1`.

**1.2 Why such a proof is not ruled out by the barrier map.**
* *B1 / Theorem C.* (W) is not a congruence covering and produces no polynomial identity family. The
  conclusion at a single prime p is `W(p) odd`, deduced from `D_φ(p)=φ(1,p)` — a statement that uses the
  **global factorisation** of p (p has exactly the factorisations 1·p, p·1). Theorem C's mechanism
  (square-mimicking primes: p agrees locally with an odd square m² modulo every witness modulus) does not
  apply, because `D_φ(p)` and `D_φ(m²)` differ although p ≡ m² locally: m² has the extra factorisations
  `ℓ·(m²/ℓ)`. Parity of a *global* divisor count is not a local invariant.
* *B5 (odd squares).* For Type I/II weights, `W(m²)=0`. (W) then only says `D_φ(m²)` is even — no
  contradiction. **The step that fails at n=m² is "D_φ(n) is odd"**, i.e. the evaluation of #Fix σ, which
  uses primality. So a windmill route passes T1 automatically, in a principled way.
* *B2/Theorem M (finite slice sets).* Zagier's σ moves between slices: it maps a factorisation
  `yz=(p−x²)/4` to a factorisation of `(p−x'²)/4` with x'≠x. A windmill is a **cross-slice coupling** of
  the per-slice divisor lotteries, using *all* ≍√p slices; Theorem M (fixed finite slice set) is irrelevant.
* *B3 (scale), B6 (average leak).* No main term; the statement is pointwise in p.

So the windmill route is a genuine gap in the barrier map. Its whole content is the existence of an
identity (W) with ES on the left. The earlier wave (WINDMILL §2.1) proved that no piece can preserve the
multilinear ES equation as an *integral affine map identically*, and found no weight w with `W(p)` odd for
all hard primes. Both leave open set-theoretic pieces and identities valid on primes only.

**1.3 New necessary condition, testable on composites.** If (W) holds for all n coprime to M (as every
Zagier-type identity does), then the parity vector `(W(n) mod 2)_{n≤X}` lies in the F₂-span of the
divisor-type vectors `D_{r,s}(n)=#{n=uv, u<v, u≡r, v≡s (M)}` and square vectors
`Q_r(n)=[n=u², u≡r (M)]`. Over all n this is a **strong** constraint (≈X equations, 2φ(M)²... unknowns),
much stronger than "W(p) odd for p in a class", which needs only ≈φ(M) unknowns. The test is GF(2) linear
algebra on the span of many candidate weights at once.

## 2. Literature anchor

* D. Zagier, "A one-sentence proof that every prime p ≡ 1 (mod 4) is a sum of two squares", Amer. Math.
  Monthly 97 (1990) 144 (from memory; standard). Heath-Brown's earlier three-involution version
  (Invariant, 1984) (from memory).
* C. Elsholtz, "A combinatorial approach to sums of two squares and related problems" (2010): windmill
  partitions close only for special forms (as summarised in WINDMILL.md §5; not re-verified here).
* Campaign: `WINDMILL.md` (reduction Lemma 1; Prop 2: integral affine symmetries of the ES equation form a
  group of order 4; §2.4: identities `#{x²+my²}≡#{uv, u≡v (m)}` hold exactly for m | 24; §3: ~7,000
  weights tested on primes); Jiang arXiv:2609.09204 Thm 5.3(iii) (ordered f_I, f_II even), as cited there.
* No published parity/involution approach to ES is known to me (from memory; LITERATURE_2026.md has none).

## 3. Barrier screen

* **B1 / Thm C, B3, B6, B2-finite (Thm M):** passed in principle (§1.2): the deduction uses p's global
  factorisation, no main term, pointwise, all slices.
* **B5 / T1 (odd squares):** passed in principle; the failing step at n=m² is the evaluation "#Fix σ is
  odd", which needs primality.
* **B2 (per-slice lottery):** the *only* way a windmill escapes B2 is cross-slice coupling (a bijection
  between divisor sets of different slice integers `N_θ(p)`). For x²+4yz this coupling is the action of
  the infinite group `O(x²+4yz)(ℤ)`. For ES the equation is multilinear and its integral affine symmetry
  group is finite (WINDMILL Prop 2), so there is no *algebraic* source of coupling; any coupling would have
  to be an ad hoc set map. This is the real obstruction, but it is not a theorem.
* **What remains testable:** whether the parity of some natural ES count *behaves like* the left side of
  a windmill identity. That is §4.

## 4. Experiments (`scripts/bs_invol_enum.cpp`, `scripts/bs_invol_signature{,2}.py`)

Data: all unordered positive solutions of 4/n for every n ≤ X with gcd(n,6)=1 (composites included),
enumerated exactly; checked against brute force for n ≤ 49 (f(5..49) = 2,7,9,4,…,18). Weights use both
the crude type (number of denominators divisible by n) and Elsholtz–Tao's types (ETI: n divides one
denominator and is coprime to the other two; ETII: n divides two and is coprime to the third). With ET's
convention `f_I(m²)=f_II(m²)=0` (checked for all m² ≤ 7921, gcd(m,6)=1; ET Prop 1.6).

**E1 (all n ≤ 8000, gcd(n,6)=1; 2666 rows; M=24).** 288 nonzero weighted counts (type × residues of
x,y,z mod 2,3,4,5,8, divisibility, gcd, squareness, `4x−n` residues; rank 163) against the 72
divisor-type vectors. `dim(span W ∩ span D) = 1`, spanned by the count of solutions with a repeated
denominator (`x=y=(n+1)/2`, n≡3 (4)) — a trivial fixed-point count, zero on primes p≡1 (4).
Controls: Zagier's |S(n)| and `#{x²+4y²=n}` lie in span D (as (Z) predicts); a random vector does not.

**E2 (all n ≤ 20000, n≡1 (4), gcd(n,6)=1; 3333 rows).** 385 weights incl. ET types and pairwise ANDs of
32 core features (rank 200). Divisor-type vectors for M = 24, 120, 168 (ranks 40, 778, 1039), and in addition
parities of representation counts by all 1564 positive definite forms `ax²+bxy+cy²` (1≤a≤8, a≤c≤40, 0≤b≤a;
x,y>0) — the possible fixed loci of a piecewise-affine involution with a non-split restricted form.
With forms (M=24) rank D = 1115; combined rank ≤ 1289 ≪ 3333 rows, so a coincidental fit is impossible. **Result in every case:
dim(W∩D)=1, the same trivial repeated-denominator count (0 on all 267 hard primes p ≡ 1 (24)).**

**E3 (prime-only periodicity).** Is some F₂-combination of the 112 core weights, on the 1125 primes
p≡1 (4) below 2·10⁴, a function of p mod L? L=24: none. L=120, 840: only the `gcd(x,y)=1` count, which is
odd only at the single prime p=5 (artefact). (Complements WINDMILL §3.2, which tested constancy and
Legendre/class-number bits.)

**E4 (a Zagier-like odd set built from the divisor form; `scripts/bs_invol_uvt.py`).**
`X(p)={(t,u,v)∈ℤ³_{≥1}: (tu−1)(tv−1)=tp+1}` (equivalently `p=uvt−u−v`) is finite (t ≤ p+2) and contains
every divisor-form ES certificate (`m=tu−1`, 4 | m). The swap u↔v fixes `u(tu−2)=p`, i.e. only
`(p+2,1,1)`; so **|X(p)| is odd for every prime p (PROVED, one line)**, and for general n,
`|X(n)| ≡ #{n=u(tu−2)}` is divisor-type — a genuine windmill-shaped identity. But the odd point has
`m=p+1≡2 (4)`: it is not an ES certificate, and the ES part `#{4 | tu−1}` is odd for only 36/61 primes
p≡1 (24) below 4000. (Observed: no element ever has both `4 | tu−1` and `4 | tv−1`.) Same pattern as every
always-odd set in WINDMILL §3.5: the parity sits on a central non-ES point.

Assessment of E1–E4 (EVIDENCE): no natural ES weight in this (fairly large) span has the parity
signature of a windmill identity, either uniformly in n or periodically on primes.

## 5. Viability

**COLLAPSES (as a research programme, not by a theorem) at the step "find the identity (W)".**
Precisely: a windmill/parity proof of ES evades B1, B3, B5, B6 and Theorem M for structural reasons
(§1.2), so it is one of the few routes the barrier map does not exclude. Its entire content is an
identity `W ≡ D_φ` (mod 2). (i) The algebraic source of such identities (an infinite integral symmetry
group moving between slices) is absent for the multilinear ES equation (WINDMILL Prop 2). (ii) E1–E4 find
no natural weight whose parity is divisor-type or binary-form-type over all n, nor periodic on primes.
Status: **UNCLEAR → leaning COLLAPSES**; what would decide it is a *set-theoretic* cross-slice bijection
between divisor sets of different `N_θ(p)` respecting the ES residue classes, which no one has.

By-products:
* (Observation, PROVED, elementary) Any Zagier-type identity (W) with Type I/II weights forces
  `D_φ(m²)` even for all odd m, and its failure point at n=m² is the evaluation of #Fix σ — so parity
  arguments are *exactly* the kind of non-local input Theorem C leaves open. (This sharpens the meaning
  of T1 for parity routes.)
* (EVIDENCE) E1–E3 above.
