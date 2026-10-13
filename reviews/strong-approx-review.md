# R167 — hostile review of O167 `STRONG_APPROX_ES.md` (§1–§11)

Reviewer: R167 (side-agent/review-strong-approx). Author branch merged: side-agent/strong-approx.
ES is not solved; nothing in the reviewed document claims otherwise, and nothing here changes that.
From-scratch scripts: `scripts/review_sa_*.py` (none reuse the author's code).

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| §1 literature | SOUND-AFTER-REPAIRS (D1 venue of BKS; D2 Sardari's primitivity hypothesis on the local ball omitted) |
| §3 matrix dictionary, Lemma 10.1 | SOUND (re-derived; symbolic + brute force, `scripts/review_sa_typeII.py`) |
| Lemma 2.2 (no plane) | SOUND |
| Thm 2.3 (rel. Pila Thm A) | SOUND |
| Cor 2.4 | SOUND-AFTER-REPAIRS (D4: `σ_p ≥ N^{−o(1)}` must be an explicit hypothesis; gap near exponent 4 correctly recorded) |
| Prop 3.1 | SOUND |
| Cor 3.2 | GAP (D5 box restriction; D6 recipe must factor through g; D7 definite Eichler orders) |
| Thm 4.1 | SOUND-AFTER-REPAIRS (D4: false as stated without a lower bound on σ_p; numerical counterexample) |
| Cor 4.2 | SOUND-AFTER-REPAIRS (D8: label/contrapositive overclaimed) |
| Prop 5.1 | SOUND-AFTER-REPAIRS (D3: "finitely many n with large v_ℓ(N_n)" is false; D10 Type I/II output) |
| §5 EVIDENCE | SOUND (reproduced independently to n ≤ 3000) |
| Prop 7.1 / Cor 7.2 | SOUND-AFTER-REPAIRS (D11: odd χ are not weight-2 Eisenstein coefficients; D13 label) |
| Thm 9.1 | SOUND (re-derived; numerics `scripts/review_sa_eisen.py`) |
| Cor 9.2 | SOUND-AFTER-REPAIRS (D12: last sentence false — counterexample n·μ²(n)) |
| Cor 9.3 | SOUND; its *Reading* overclaims (D14: maps valid only at primes are not covered) |
| Lemma 10.1 / Prop 10.2 | SOUND (10.2: only the periodicity statement is a theorem, D13) |
| §11 | SOUND as Assessment |

## Checks performed

**§1 literature.** Sardari arXiv:1510.00462 (Duke 168 (2019), DOI 10.1215/00127094-2019-0007 — confirmed via
the arXiv record) — I downloaded the arXiv PDF and read Thm 1.2, Conj 1.3, Thm 1.6, Remark 1.7 directly.
* Thm 1.2 (d = 4): "the same result holds provided that N is odd and N ≫ (r⁻¹m)^{6+δ}", constant depending only on
  Ω and δ (Ω a fixed compact subset of the real quadric F = 1, hence on F). Matches §1. Exponent 6 "cannot be
  replaced with a number smaller than 4" — matches.
* Conj 1.3: d = 4, N odd, N ≫ (r⁻¹m)^{4+δ}. Matches.
* Thm 1.6 (1.4), d = 4: `|V_N(ℤ) ∩ B_{a,r}| ≫ S_B(N)|B|³N(1 + O((|B|³√N)^{−1/2}N^ε))`, `|B| = r/m`. Matches
  §1's main term and relative error. **But** Thm 1.6 is stated for global balls with `gcd(a_p, p) = 1`, i.e. the
  class λ is primitive at every p | m (Sardari reduces the imprimitive case by dividing N by p^{2h_p}). §1/Def 2.1
  allow arbitrary λ. (D2.)
* Remark 1.7: the lower bound `S_B(N) ≥ c_ε N^{−ε}` is asserted by Sardari for d = 4 "if N is odd". This is
  the input behind the document's `σ_p ≥ N^{−o(1)}`; it is *not* true for general quaternary forms with an odd
  anisotropic prime (see D4, numerical counterexample) — Sardari's constants depend on F, and his remark should
  be read for a fixed F with the anisotropic-prime part of N bounded. The document's own caveat ("away from
  anisotropic-prime blowups") is right but is not carried into the theorem statements (D4).
* BKS arXiv:1609.06097, "Twisted Linnik implies optimal covering exponent for S³": abstract confirms a covering
  exponent result conditional on a twisted Linnik conjecture. The DOI on the arXiv record is
  10.1093/imrn/rnx116, i.e. **IMRN**, not Duke as §1 says (D1). Sardari's paper (line "Conjecture 1.3 implies
  K₄ = 4/3") confirms the 4/3 ↔ exponent-4 calibration of §4.
* Sardari arXiv:1511.09340 abstract: diameter of LPS bipartite Ramanujan graphs `> (4/3)log_p n + O(1)`, and an
  infinite family with diameter `≥ ⌊(4/3)log_p n⌋`. Matches §1 (LPS). The LPS upper bound `2log + O(1)` I did
  not re-verify (not accessed); the document flags this itself.
* DSP (Duke–Schulze-Pillot): not accessed; statement as given is the standard one.
* Pila Thm A: not re-accessed by me; the verbatim statement was checked by R124 (`reviews/pointwise-ternary-review.md`):
  irreducible affine V of dim n, degree d in 𝔸^N, `≤ c(n,d,N) H^{n−1+1/d} exp(12√(d log H log log H))`, uniform in V.
  This is what Thm 2.3 uses.

**§3 matrix dictionary and Lemma 10.1 (`scripts/review_sa_typeII.py 3000`).** Enumerates ET Type II quadruples
directly from `c(4abd − n) = a + b` (independent of the author's matrix search). For all odd n ≤ 3000: γ =
[[aM−1, M],[cn, bM−1]] (M = 4cd) has det 1; the 4/n identity holds in exact rationals; every prime 5 ≤ p ≤ 3000
has a quadruple; no odd square has one. The product formula of Lemma 10.1 holds symbolically, and the
decomposition `S = ⊔_M U⁻γ_M U⁻` is a bijection `(a, b) ∈ ℤ²` ↔ elements (γ₁₁ = aM−1, γ₂₂ = bM−1 determine γ₂₁ via
det). Converse (all SL₂ matrices with γ₁₂ = M, γ₁₁ ≡ γ₂₂ ≡ −1 (M), γ₂₁ = cn, c | M/4 ↔ quadruples) verified by
brute force for odd n < 200. Prime n never divides M (n ≤ 3000) — see D9.

## Defects

No FATAL defect: every negative conclusion of the document survives, after the repairs below.

**D1 (MINOR) §1 (BKS).** BKS is IMRN (DOI 10.1093/imrn/rnx116 on the arXiv record of 1609.06097), not Duke 2019.
*Repair:* fix the citation.

**D2 (MINOR) §1 (S4), Def 2.1.** Sardari Thm 1.6 is stated for global balls with `gcd(a_p, p) = 1` (the class λ is
primitive at each p | m); imprimitive classes are reduced by dividing N by `p^{2h_p}` (Remark 1.7). §1 and the
"model case" of Def 2.1 apply (S4) to arbitrary λ. *Repair:* add "λ primitive at every p | q (else rescale N)" to the
(S4) bullet. Nothing downstream changes, because Thm 2.3/Cor 2.4 only use an abstract lower bound `M_p`.

**D3 (MAJOR → repairable) Prop 5.1, "away from the finitely many n with large v_ℓ(N_n) at anisotropic ℓ".** False:
for `N_n = κn + η`, `{n : v_ℓ(N_n) ≥ k}` is a full residue class mod ℓ^k (when ℓ ∤ κ), hence infinite for every k;
and at `n = m²` the valuation `v_ℓ(κm² + η)` is unbounded along m whenever `−η/κ` is a square mod ℓ (e.g. κ = 1,
η = −1, m ≡ ±1 (ℓ^k)). Then the local conditions at `n = m²` and at `p ≡ m² (L)` need not coincide for a *fixed* L.
*Repair:* the T1 argument only needs infinitely many m. State: "for each anisotropic ℓ | 2q·disc Q fix K_ℓ; for every
odd m with `v_ℓ(N_{m²}) < K_ℓ − c_ℓ` for all such ℓ (e.g. all m in a suitable fixed class mod L, which is an infinite
set provided `N_{r²} ≠ 0` for some r) and every prime `p ≡ m² (L)`, `L := q·Π ℓ^{K_ℓ}`, the local conditions
coincide." The conclusion of Prop 5.1 is unaffected.

**D4 (MAJOR) Thm 4.1, Cor 2.4, §4: the lower bound `σ_p ≥ N_p^{−o(1)}` is used as a fact but is false in general.**
Counterexample (`scripts/review_sa_aniso.py`): `Q = x²+y²+3z²+3w²` (norm form of (−1,−3), anisotropic at 3).
Exactly `r_Q(9^k u) = r_Q(u)` for u ∈ {1,2,5,7}, k ≤ 5 (e.g. `r_Q(9^k) = 4` for all k, N up to 59049, N odd), so the
3-adic density is `≍ N^{−1}` along `N = 9^k u`. Thus an encoding with fixed Q and `N_p = 9^{k(p)}u_p`, `k(p) → ∞`,
has `M_p = σ_p N_p/q³` bounded although `N_p` is arbitrarily large, and Thm 4.1's conclusion "`N_p ≤ p^{o(1)}`"
fails as stated (its proof uses `M ≥ σ N^{η/(1+η)} ≥ N^{η/(1+η)−o(1)}`). Note Sardari's own Remark 1.7 asserts
`S(N) ≥ c_ε N^{−ε}` for d = 4 and N odd; the example shows that this needs the anisotropic part of N bounded
(his constants depend on F, but N = 9^k is odd and unbounded). Cor 2.4 does flag the input ("not re-proved here"),
but uses it to conclude "for all p outside that sparse set".
*Repair:* add to Thm 4.1 and Cor 2.4 the explicit hypothesis
`(A) σ_p ≥ N_p^{−o(1)}` (equivalently, for the forms at hand, `Π_{ℓ anisotropic} ℓ^{v_ℓ(N_p)} ≤ N_p^{o(1)}`),
or replace `N_p` by its reduced part `N_p♭ = N_p/Π_{ℓ anis.} ℓ^{2⌊v_ℓ(N_p)/2⌋}` (Sardari's rescaling; points with
`ℓ^h | x` correspond bijectively), and state the conclusion for `N_p♭`. With p-dependent `Q_p` the anisotropic primes
may themselves grow with p, so (A) is a genuine restriction and should appear in §8's table.

**D5 (MAJOR / GAP) Cor 3.2, box restriction.** Def 2.1's `R_p` contains `|x|_∞ ≤ B_p`, and a recipe only has to be
valid on `R_p`. Prop 3.1 produces points `γ = AδD`, δ ∈ Γ(q), with no size control. Inside a box of radius
`B_p ≍ √N_p` (the (S4) model) the first-column content g satisfies `g ≤ B_p`, so **`g = N_p` never occurs** (contrary to
"in particular for g = 1 and g = N_p"), and for g between √N and N it need not occur; heuristically the number of
content-g points in one class and box is ≍ `(B²/N)·(#Hermite cells of type g)/q³`, which can be < 1. So "the set
{g(x) : x ≡ λ (q_p)} is all divisors" is true for the unbounded class but has not been shown for `R_p`.
*Repair:* either (i) restrict Cor 3.2 to recipes valid on the whole (unboxed) class `{x ≡ λ (q_p), Q_p(x) = N_p}`, or
(ii) prove the needed box statement for g = 1 only (existence of a point of `R_p` with primitive first column),
e.g. by Möbius-sieving Sardari's count over sublattices `ℓ | g` — which needs SA uniform over these sublattices and
is not in the literature cited; then drop "g = N_p". §8's row "Prop 3.1 (invisibility)" should carry the same scope.

**D6 (MINOR) Cor 3.2, logic.** "A recipe valid on every point of a congruence class must be valid for every divisor
… ES is then certified by the trivial factorisation alone" presupposes that the recipe's output depends on x only
through g(x) and congruence data. A recipe `Φ(x) = F(g(x), x)` reading other features of x is not reduced to g = 1.
*Repair:* state the factorisation-through-g hypothesis explicitly (it is implicit in "a rule ψ that reads off").

**D7 (MINOR) Cor 3.2, "(or the reduced norm of an Eichler order, by strong approximation for its norm-one group)".**
Strong approximation for the norm-one group fails for **definite** algebras (compact at ∞). The ES-relevant algebras
`(−d,−p)`, `B_{p,∞}` are definite; for them the number of norm-N elements is finite and a class mod q need not contain
every factorisation type. *Repair:* say "indefinite Eichler order"; for definite orders only the pointwise statement
(the Hurwitz unique-factorisation paragraph) holds.

**D8 (MAJOR, label) Cor 4.2 "PROVED, combining 2.3, 3.1, 4.1".** (i) It also invokes Principle 3.3, which is an
Assessment. (ii) Thm 4.1 says "μ ≤ p^{o(1)} ⇒ data p^{o(1)} off density 0"; its contrapositive does not give
"μ(p) ≥ p^{η'}" for a fixed η' > 0, and it omits the alternative "all data `p^{o(1)}`" (the B2 bounded-slice case).
(iii) It inherits D4 and D5. *Repair:* relabel as Assessment (or PROVED for the precise disjunction: "either
`μ(p) ≤ p^{o(1)}` fails on a set of positive upper density, or (under (A)) all data are `p^{o(1)}` off density 0").

**D9 (MINOR) Lemma 10.1, "p ∤ M".** Used to deduce `M | γ'₁₂`, but not proved. `p ∤ d` is easy
(`p | d ⇒ a+b = c(4abd−p) ≥ p(4ab−1) > a+b`); `p | c` is not excluded in the text. Numerically never happens for
primes ≤ 3000 (`review_sa_typeII.py`). *Repair (R167 proof, two lines):* if `c = pc'` then `a + b = pc'(4abd − p) ≥ p`
and `4abd ≤ p + (a+b)/p`; with a ≤ b this gives `4b ≤ p + 2b/p`, so `b < p/3` and `a + b < p`, contradiction. Hence
`p ∤ M` for odd primes p; insert this.


**D10 (MINOR) Prop 5.1, "would therefore give a Type I/II solution of 4/m²".** `Sol(m²)` is nonempty (e.g. from any
solution for m), so the contradiction needs the recipe's output to be a Type I/II certificate (ET parameters
(a,b,c,d) with n entering linearly), not an arbitrary element of Sol(n). *Repair:* say so; with Sol(n) replaced by
the Type I/II certificate set the argument is correct (ET Prop 1.6; reproduced: no odd square ≤ 3000 has a
Type II quadruple).

**D11 (MAJOR, interpretive) Prop 7.1: "The σ_χ(n) are Fourier coefficients of weight-2 Eisenstein series … exactly
the objects that the Siegel–Weil formula attaches to genera of quaternary forms".** False for **odd** χ:
`M_2(Γ₀(N), χ) = 0` unless `χ(−1) = (−1)² = 1`, and on Γ₁(N) the diamond operator ⟨−1⟩ = −I acts trivially in even
weight, so every weight-2 form (in particular every quaternary theta series, shifted or not) has only even-character
components. `σ(n; −1, g) = φ(g)^{−1}Σ_χ χ(−1)σ_χ(n)` contains the odd-χ part with full weight, and the
σ_χ for distinct χ are linearly independent; so `σ(n; −1, g)` is **not** a combination of rank-4 genus/theta
coefficients (only its even part `(σ(n;1,g)+σ(n;−1,g))/2` is, and that is trivially positive: divisor 1). Thus the
§7 heading "the rank-4 dictionary for Type II" is wrong as stated: the Type II positivity statement lives in the odd
part, which no quaternary theta series sees. *Repair:* restrict the Siegel–Weil sentence to even χ, and record that
the Type II indicator needs odd-character divisor sums (weight-1/3-type parity), i.e. it is not a rank-4 genus
statement. This **strengthens** the document's negative reading; Thm 9.1 (elementary, all χ) is unaffected.

**D12 (MAJOR, overclaim) Cor 9.2, last sentence: "The same holds for every n-local object whose values at primes and
at prime squares are quasi-polynomials in the prime."** Counterexample: `h(n) = n·μ(n)²`. `h(p) = p > 0`,
`h(ℓ²) = 0` (and h vanishes at every square > 1): quasi-polynomial at primes and at prime squares, vanishes at all
odd squares, positive at all primes. The proof of 9.1 uses the specific *coupling* between the value at ℓ² and at p
(`E(ℓ²) = Σ C_k(1+ℓ^k+ℓ^{2k})` vs `E(p) = Σ C_k(1+p^k)`, same C_k), not quasi-polynomiality. *Repair:* replace by
"every finite combination of divisor sums `Σ_{d|n} χ(d)ψ(n/d)d^k` (more generally, every function whose value at
p² and at p are given by the same Satake-type polynomial data)".

**D13 (MINOR, labels) Cor 7.2, Prop 10.2, §10 "count PROVED".** Cor 7.2 is labelled PROVED but its "main term
σ(n)/φ(g)" is a heuristic average, not a theorem about σ(n; r, g) at a fixed n; Prop 10.2's proved content is only
"`M ↦ 1[c | M/4]` has exact period 4c"; the sentence about what a congruence subgroup "can impose" is an Assessment;
§10's "expected number of good points ≍ τ(M/4) log p/M" is a heuristic density count. *Repair:* relabel those
sentences Assessment/heuristic; the PROVED parts stand.

**D14 (MAJOR, overclaim in a Reading) Cor 9.3 Reading: "A rank-4 representation count at fixed level … is T1-dead on
the Mordell-hard classes, whatever map to certificates is used."** Cor 9.3 applies to a function W that vanishes at
odd squares, i.e. to the certificate count itself. A representation count R(n) (with `|R − E| ≤ Bn^θ`) that is
mapped to certificates by a map **valid only at primes** has `R(ℓ²) > 0` in general, and Cor 9.3 says nothing about
it; that case is exactly the §5 situation ("the map fails at m²"), handled by Thm 2.3/Prop 5.1 only for bounded
rational or congruence-validated maps. The Reading is correct for maps defined and valid at all odd n (then
`R(ℓ²) ≤ μ·W(ℓ²) = 0`). *Repair:* add "for maps valid at all odd n (so that R vanishes at odd squares)"; maps whose
validity uses primality are not covered (they are §4/Thm 4.1's business). §11 bullet 1 is fine because there the
count is of certificates.

## Re-derivations (brief)

* **Lemma 2.2.** Projective closure `Q(x) − N x₀²` has rank 5 (N ≠ 0, Q nondegenerate) ⇒ smooth quadric threefold;
  maximal linear subspaces have dimension 1. Correct.
* **Thm 2.3.** Fibre `F_s` over each `s ∈ Sol(p)` is a proper closed subset (nondegeneracy + irreducibility of V_p),
  ≤ C(D) components of degree ≤ C(D) (Bézout); affine change `x = λ̃ + q y` preserves dimension/degree/planarity;
  non-real components have real points in a lower-dimensional intersection; real 2-dimensional components have
  degree ≥ 2 by Lemma 2.2, so Pila gives `H^{1+1/2+ε}`. Constants depend only on (J, D, ε) because Pila's is uniform
  in the variety. Correct.
* **Cor 2.4 arithmetic.** `M/H^{3/2} ≍ σN^{1/4}q^{−3/2}`; with `q ≤ N^{1/(6+ε₀)}`, `1/4 − 3/(12+2ε₀) = ε₀/(24+4ε₀)` = κ.
  Correct. The recorded gap (range `q⁴ ≤ N ≤ q⁶f⁴`) is exactly where `σN^{1/4}q^{−3/2} < f`; correctly stated.
* **Prop 3.1.** `γ = AδD`: `γ ≡ A₀D = λ (q)`, det n, first column `g·(Aδ)e₁` with `(Aδ)e₁` primitive. Correct.
* **Thm 4.1 arithmetic.** In range `N/(√D q³) ≥ N^{η/(1+η)}`; rest as stated, modulo D4.
* **Thm 9.1 / Cor 9.3.** For ℓ, p ≡ 1 (L) all characters of conductor | L are 1; `E(ℓ²) = P(ℓ)`,
  `E(p) = Σ C_k(1+p^k)`; the coefficient of `x^{2K}` in P is C_K (a contribution from k' = 2K would need C_{2K} ≠ 0,
  contradicting maximality of K when K ≥ 1). (a), (b) and the three cases K > θ, K = θ, K < θ of 9.3 check out
  (K = θ: `C_K ≤ B`, so `E(p) ≤ Bp^θ + O(p^{θ−1}) < 2Bp^θ`). Numerically (`scripts/review_sa_eisen.py`, L = 35, 24
  characters, complex random combinations, k ≤ 3): `E(ℓ²) = P(ℓ)` and `E(p) = ΣC_k(1+p^k)` to 5e−16 relative; a
  nontrivial combination with all C_k = 0 vanishes at all p ≡ 1 (35) and at ℓ² but is nonzero at 50/50 other primes
  (so the scope restriction to p ≡ 1 (L) is genuine); for 200 random real combinations sign E(ℓ²) = sign E(p) at
  large ℓ, p ≡ 1 (35); the counting version had 0/200 violations.
* **Lemma 10.1.** Symbolic product verified; `S → (M, a, b)` bijective.
