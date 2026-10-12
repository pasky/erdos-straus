# BRAINSTORM (O146 b): parity-breaking at fixed p (hatch H-B) — the sign layer and the size layer

Status: brainstorm memo. **ES is not solved here.** Labels as in DISCOVERIES.md.

## 1. Idea

H-B (redteam-automorphic-2 §3): a slice is empty when `N_θ(p)` is prime, or when the prime factors of
`N_θ(p)` lie in a subgroup missing the target class. ¬ES(p) is the conspiracy "every slice of the full ET
family is bad". If "bad" were a parity/sign-pattern condition, a Friedlander–Iwaniec / Heath-Brown /
Maynard bilinear ("Type II sums") argument over the family at fixed p might break it.

Exact formulation, row II{a,d} (the other rows are analogous): `N = p + 4a²d`, `q = 4ad`, target
`f | N`, `f ≡ −1 (mod q)` (Lemma 2.1). Note `N ≡ p (mod q)`. Let `H_θ ≤ (ℤ/q)^×` be the subgroup generated
by the prime factors of N that are coprime to q. Every slice falls into exactly one class:
* **hit**: some divisor f ≡ −1 (a solution);
* **prime**: N prime (and not a hit);
* **Q (quadratic sign obstruction)**: some quadratic character χ mod q has χ = 1 on all prime factors of N
  and χ(−1) = −1. Equivalently, the sign vector of −1 (Legendre symbols at the odd r | q, and χ₋₄, χ₈ at
  2) is not in the F₂-span of the sign vectors of the prime factors ℓ | N;
* **Q′ (higher-order obstruction)**: −1 ∉ H_θ, but not of type Q;
* **A (size/accidental)**: −1 ∈ H_θ, but no divisor of N (exponents bounded by those in N) hits.

The conspiracy is: every θ in Q ∪ Q′ ∪ A ∪ prime. Type Q is literally a parity/sign pattern, a condition
on the Jacobi symbols `(ℓ/r)` with `ℓ | N_θ`, `r | q_θ`. This is the kind of "spin" that Friedlander–Iwaniec
(`X² + Y⁴`) and Friedlander–Iwaniec–Mazur–Rubin control by bilinear sums of Jacobi symbols. Type A is not a
sign pattern: it is a size condition, since the τ(N) divisors simply miss one class of a group of order φ(q).

## 2. Literature anchor

* Friedlander–Iwaniec, Ann. of Math. 148 (1998) 945–1040; Heath-Brown, Acta Math. 186 (2001) 1–84;
  Maynard, Forum Math. Pi 8 (2020) e3. All count primes in thin polynomial sequences with a **power-size
  main term**, via Type I/II sums with power savings (citations as verified by the O132 research
  subagent; not re-read here).
* FI's "spin"/Jacobi-symbol bilinear sums: Friedlander–Iwaniec–Mazur–Rubin, Invent. Math. 193 (2013)
  697–749 (from memory, unverified here).
* Parity principle: Friedlander–Iwaniec, *Opera de Cribro*, ch. 16 (as cited in O132).
* ET Prop 1.6 (checked): at odd squares every slice is empty, by reciprocity.

## 3. Experiment: which class does the would-be conspiracy live in? (`scripts/bs_corr_badclass.c`, `logs/bs_corr_badclass.txt`)

All II{a,d} slices with `4a²d ≤ p + 2a`, `q = 4ad ≤ 3·10⁴`; exact factorisation, subgroup closure by BFS,
quadratic test by F₂ elimination.

| n | n mod 840 | slices | hit | prime | Q | Q′ | A |
|---|---|---|---|---|---|---|---|
| 100057 (prime) | 97 | 20620 | 38 | 3868 | 11943 | 413 | 4358 |
| 1002121 (prime) | 1 | 37422 | 82 | 6267 | 23762 | 760 | 6551 |
| 4000081 (prime) | 1 | 47082 | 74 | 7268 | 30672 | 1117 | 7951 |
| 1002001 = 1001² (control) | 1 | 37421 | **0** | 5459 | 31962 | **0** | **0** |

(Q = charexpl − higher-order in the log.) Per dyadic scale of q, the hit counts are O(1)–O(10) in every
block, while the A counts grow like the number of slices. The hit rate inside A ∪ hit falls roughly like
1/q (log table).

Reading (EVIDENCE):
1. At the square, everything is Q or prime, and Q is exactly the genus character χ₋₄d lifted to q, as in ET's
   proof. At primes, ≈ 20% of slices are **sign-compatible** (A ∪ Q′ ∪ hit), uniformly across scales.
   So the T1 distinction between p and m² lives entirely in the sign layer, and there it has
   **power-size mass** (≍ #slices ≍ p).
2. The hits are a vanishing fraction of the sign-compatible slices (82 of 7393 at p = 1002121, q ≤ 3·10⁴).
   The polylog scarcity of solutions lives in the size layer A, not in the sign layer.

## 4. Barrier screen

Heuristic factorisation (Assessment): `P(hit) ≈ P(sign-compatible) · P(divisor lands | sign-compatible)`.
The first factor is ≍ 1 on average (data: ≈ 0.2). The second is ≍ τ(N)/φ(q) up to constants. So
`Σ_θ P(hit) ≍ log³p` comes entirely from the second factor.

* **B5/T1: PASSES in the sign layer.** A sign-layer theorem ("for every large prime p, a positive
  proportion of slices are sign-compatible") is false at squares (row 4 of the table), as T1 requires. It has
  a power-size main term, so FI-type bilinear technology is *not* excluded by B3 there.
* **B3: COLLAPSES in the size layer.** Even an oracle deciding the sign layer exactly (perfect
  parity-breaking) leaves "some divisor of N_θ lands in −1 mod q_θ" for ≍ p sign-compatible θ, each of
  probability ≍ τ/q. That count is polylogarithmic, Planck-scale and moving-modulus: H-A verbatim. In
  numbers, at p ≈ 10⁶: 7393 sign-compatible slices with q ≤ 3·10⁴, 82 hits. For any long family of V ≍ p^{1+o(1)}
  slices (e.g. all I{c,d} with cd < p, or all II{a,d}), square-root cancellation in V gives an error
  ≍ V^{1/2} ≈ p^{1/2} against a main term ≍ log³p. A family with main term ≥ V^{1/2} has V ≤ f(p)² ≪ log⁶p
  members, too short for bilinear structure (its moduli reach p^{1−o(1)} by redteam-2 §3.1). This is the scale
  constraint B3 (CONDITIONAL_ES Prop 2.3) in bilinear language; Assessment, not theorem.
* **Parity is mis-targeted.** Parity obstructs detecting primes or Ω-parity. The conspiracy is mostly
  composite N_θ (the prime class is ≈ 17% of slices at p ≈ 10⁶). Sieve information on the number of prime
  factors of N_θ does not decide class A. The quadratic part (class Q) is a genuine sign pattern, but it is
  not the bottleneck.
* B1/B2: a fixed finite set of θ is Thm 2.2(iii) (CONDITIONAL on H). B4: class A is the regime of
  LONGSHOT_PIGEONHOLE Prop 1.4 / Thm 2.2 (structure-only certificates need many prime factors).
  B6/T7: nothing is averaged over p here; the family is over θ at fixed p.

## 5. Viability Assessment

**COLLAPSES to B3 at the size layer; PARTIAL as a reformulation.** The H-B target splits exactly into:
* (sign layer) a parity/Jacobi-symbol conspiracy that is exactly where primes and squares differ (T1), with
  power-size mass, plausibly within reach of spin/bilinear methods, but **not sufficient**;
* (size layer) a Planck-scale divisor-in-moving-class event with polylog mass, untouched by parity
  breaking. This is H-A, and B3 applies.

So H-B, as framed, cannot be the missing ingredient. At best it supplies the genus-awareness that every
route already gets cheaply from (·/p) (POINTWISE_SPECTRAL Lemma 2.4; GEOMETRY_ES Prop 5.2).

Concrete next step, only if someone wants a by-product theorem: prove "a positive proportion of II{a,d}
slices with q ≤ p^η are sign-compatible, for every large prime p" (a fixed-p statement about Legendre
symbols of prime factors of `p + 4a²d`). It would be a clean T1-passing fixed-p theorem, but it says
nothing about ES.

By-products: the five-class decomposition (definitions; PROVED trivially to be a partition); the class
table (EVIDENCE, 3 primes + 1 square control); "square ⇒ all composite slices are Q" (PROVED: every prime
`ℓ ∤ 2adm` of `m² + 4a²d` has `χ₋₄d(ℓ) = 1`, while `χ₋₄d(−1) = −1`, which is ET Prop 1.6's argument).

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-B.md (§0.2, §0.3 and the
per-memo paragraph). Counterexamples, where computational, re-verified by `scripts/errata_check.py` (tag in brackets).

* **§1 partition is not a partition as literally defined:** the classes "prime" and Q overlap. Example [parity]:
  p = 13, a = d = 1: N = 17 is prime (and not a hit), q = 4, and χ₋₄(17) = 1 while χ₋₄(−1) = −1, so it is also Q.
  Repair: define the classes by priority (hit > prime > Q > Q′ > A), as the implementation already does.
* §4's √V error and pointwise f(p) ≪ log³p are methodological/heuristic assumptions, not consequences of B3:
  CONDITIONAL_ES Prop 2.3 gives no lower bound on error, and its Remark 2.4 keeps "small main term + smaller
  error" open. **Corrected verdict:** PARTIAL → H-B (sign-only oracles are insufficient; parity-breaking input coupled
  to actual divisor incidence remains untested).
