# AGENT REPORT O135 — Long shot A: deterministic pigeonhole ("highly composite slices")

Branch `side-agent/longshot-pigeonhole`. Main file `LONGSHOT_PIGEONHOLE.md`; scripts `scripts/lsa_*`; data
`data/lsa/`; tables `logs/lsa_tables.txt`. **ES not proved; no new case of ES proved.**

## Deliverable: a PROVED negative result with exact scope (brief option 2)
1. **Exact covering problem** (Lemma 1.1, PROVED). The single coordinate e parametrises all solutions:
   ES(p) ⟺ ∃ e ≡ −p (4): `−1 ∈ Σ_e(N) := {ab⁻¹ mod e : ab | N}`, with `N = (p+e)/4` (II; consecutive integers above p/4)
   or `(pe+1)/4` (I). This one-coordinate slice has *signed* products, which makes it the best case for pigeonhole
   (3^k rather than 2^k).
2. **Genus** (Lemma 1.2, PROVED incl. ℓ = 2): every prime factor ℓ | N has `χ_{−e}(ℓ) = (ℓ/p)`; −1 lies in the
   non-trivial coset of `K_e = ker χ_{−e}`. This is T1 (odd squares) and T4 (n_p) inside a slice.
3. **Pigeonhole proper gives the wrong sign** (Lemma 1.3, PROVED): collisions (`2^ω > φ(e)`) yield signed solutions
   `4/p = 1/x − 1/y + 1/z`. Positivity is covering of a translate, not zero-sum.
4. **Covering criteria** (Prop 1.4, PROVED from Kneser): structure-only criteria need a number of prime factors
   *linear* in the index of every subgroup H ∌ −1; sharp. Exponential (`log₃ q`) efficiency needs the actual residues.
5. **Forcing** (Lemma 2.1): the brief's estimate is right — CRT forcing costs `e^{(1+o(1))k log k}` vs `3^{k+1}`.
   **Modulus ceiling** (Lemma 2.3): every covering certificate has `e ≤ p^{o(1)}`.
6. **Theorem 2.2 (main, PROVED rel. PNT in APs to a fixed modulus, Brun–Titchmarsh (MV 1973), Shiu 1980,
   Nicolas–Robin).** Covering certificates built from the prime factors of N_e *below the modulus* plus one opaque
   cofactor (any coset of index ≤ e^θ, θ < 1/2) fail for a **positive proportion of primes, in every e-slice of both
   types**: on `p ≡ 1 (mod 8∏_{ℓ≤Y}ℓ)` small e die by genus, and the rest is a Markov bound whose majorant
   `Σ_e (log e)^8 e^{2θ−2}` converges and is independent of p (bounded mass vs solution mass ≍ (log p)³).
   So it is not a log-log near-miss; it is a change of regime.
7. **Scope.** Not excluded: certificates using residues of prime factors *above* the modulus — these are the
   per-slice divisor-in-class events (lottery, H-A/H-B). Two-coordinate rows: analogue of Thm 2.2 asserted only as
   Assessment (same proof, two-parameter sum; not written out).

## Numerics (EVIDENCE; engine validated vs `scripts/rt2_slices.py` brute force for all p ≡ 1 (4) < 200, and flags
re-derived by an independent Python checker on 15000 slices, 0 mismatches)
* Full-coset covers exist at every sampled Mordell-hard prime ≥ 10⁶ (P20 ≥ 2; largest covered |−K_e| = 2339);
  exceptions below 10⁶: 3529, 110881. Hard primes (to 3.7·10⁷) all have covers.
* The deepest cover per prime is transparent in ≥ 99 % of primes; for e ≥ 100, P ≈ TP. Large primes add covers
  almost only at e < 100.
* Covers are a minority of solution slices at e ≥ 500 (≈ 5 % at 10⁸): the growing solution mass is luck.
* Transparent counts still grow up to 10⁸ (pre-asymptotic); the limiting-model DP shows the size-necessary count is
  a large convergent series, so Thm 2.2's failure set is not numerically observable. Thm 2.2 is qualitative.

## Conjecture
PH (Conj 5.1): every large p has a full-coset cover with φ(e) ≥ 40 in some e-slice. CONJECTURE, EVIDENCE above;
by Thm 2.2 any proof must use non-transparent primes on a positive-density set, i.e. the lottery.

## Caveats for the reviewer
* The self-review tool failed twice (service error), so no independent review of Thm 2.2 has been done yet. The parts
  most worth checking: (b2) multiplicative-sum constants and compatibility with `p ≡ 1 (q_0)`; the uniformity of C
  in Y; the Shiu application in (c) (Type I progression mod e).
* The Erdős–Rényi random-covering threshold is quoted only as a heuristic (UNVERIFIED in our citation check).
* Novelty: Lemma 1.1/1.2 are reformulations of ET/Bright–Loughran-type facts; Lemma 1.3 is elementary; Thm 2.2 is,
  as far as the citation check found, new but modest.
