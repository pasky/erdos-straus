# bsC_parity_quadratic_only — Diff-parity over ANY base field sees a rational prime only through one quadratic character (O176; O172 spark 4)

**ES is not solved here.** Labels as in DISCOVERIES.md. Scripts `scripts/bsC_quadratic_slices.py`,
`scripts/bsC_quad_slices_fast.py`.

## Idea
T1 is the oddness of Diff(T) (KUDLA_ES §1; repaired per R172 D3/D4: the ES congruences are *sufficient* to clear the
places ℓ ∤ n, only their genus shadow is needed). Parity of a set of places is the one *deterministic existence engine*
in the dictionary ("|Diff| odd ⇒ some prime of n is in Diff"). Spark 4 asks whether a unitary / big-CM version over
F = ℚ(ζ_M)⁺ (hermitian spaces over E = ℚ(ζ_M)) lets parity see the order-≥3 characters that the ray condition
`f ≡ −1 (mod M)` needs. Answer: no, for a structural reason that applies to every base field.

## Literature
Hasse invariants of hermitian spaces: Jacobowitz, *Hermitian forms over local fields*, Amer. J. Math. 84 (1962)
(local hermitian spaces over E_λ/F_λ are classified by dimension and det ∈ F_λ^×/N E_λ^×: a ±1 invariant);
Kudla–Rapoport (unitary Diff), Li–Zhang, *On the arithmetic Siegel–Weil formula for GSpin / unitary Shimura varieties*
(Invent. 2022); Bruinier–Kudla–Yang (big CM); Neukirch, ANT VI §5 (Hecke characters, restriction to ℚ^×).

## Statement
**Prop 1 (parity over any base is a quadratic Dirichlet character; PROVED).** Let F be a number field and η a
quadratic Hecke character of F (e.g. η_{E/F}, or any (α, ·)_λ Hilbert-symbol character). For a rational prime ℓ
unramified in F and coprime to cond(η), and t ∈ ℚ^× with v_ℓ(t) = 1, the number of places λ | ℓ of F with
"λ ∈ Diff" := "η_λ(t) = −1" satisfies
`#{λ | ℓ : η_λ(t) = −1} ≡ [η((ℓ)O_F) = −1]  (mod 2)`,
and `ℓ ↦ η((ℓ)O_F) = η|_{ℚ^×}`-restriction is a **quadratic Dirichlet character of ℓ** (conductor | N_{F/ℚ}cond(η)·∞).
In particular the parity of any Diff-set built from local ±1 invariants (orthogonal Hasse invariants, hermitian
determinants) of **ℚ-rational** data at a rational prime ℓ depends on ℓ only through one quadratic character.
*(R176 repair D2: the hypothesis t ∈ ℚ^× is essential. For F-rational data the local Diff above ℓ can see higher-order
characters: F = ℚ(ζ₁₃)⁺, E = ℚ(ζ₁₃), hermitian ⟨π⟩ with (π) = λ | ℓ has λ ∈ Diff iff ord(ℓ mod 13) is even, i.e. iff ℓ
is not a 4th power mod 13 — ℓ = 3 and ℓ = 17 are both squares mod 13 with opposite answers. Only the parity over the
whole fibre {λ | ℓ} is quadratic.)*
*Proof.* For λ | ℓ unramified with λ ∤ cond η, η_λ(t) = η(λ)^{v_λ(t)} = η(λ). So the count mod 2 is the number of
λ with η(λ) = −1, whose parity is read off ∏_{λ|ℓ} η(λ) = η((ℓ)O_F). The ideal (ℓ)O_F is principal with generator ℓ;
for an idelic η, η((ℓ)) = ∏_{v | cond·∞} η_v(ℓ)^{−1}, a character of ℓ ∈ ℚ^× through (ℤ/N)^× × {±1}, of order ≤ 2. ∎
**Cor 2 (when parity can see the ES ray condition; PROVED, elementary).** The event `f ≡ −1 (mod M)` is a Boolean
function of the quadratic characters of f mod M iff (ℤ/M)^× is an elementary abelian 2-group iff **M | 24**.
*Assessment (not PROVED; "mechanism" is not a defined object — R176 D2):* so a mechanism whose information about the
divisor f comes from Diff-parities of ℚ-rational data (over any base, any dimension) can certify ES only through slices with `4cd | 24`, i.e. through the **fixed finite** slice set (c, d) with cd | 6
(Type I: f | p² + 4c²d, f ≡ −p; Type II: f | 1 + 4c²dp, f ≡ −1 (mod 4cd)), and such sets fail infinitely often under H
(redteam-automorphic-2 Thm 2.2, CONDITIONAL). *(Scope: parity used as the source of the ray information; it says
nothing about mechanisms using parity only for the sign layer — cf. PARITY_FIXED_P.)*

## Barrier screen
* **Spark 4 (unitary R-part).** Hermitian local invariants are ±1 (Jacobowitz), so Prop 1 applies verbatim with
  F = ℚ(ζ_M)⁺: a unitary Diff over F sees ℓ only through η_{E/F}|_{ℚ^×} = a quadratic character (here the one cut
  out by E/F restricted to ℚ — the sign is lost exactly as in KUDLA_ES log 4 / R172 re-derivation "σ_f^{[F:ℚ]}").
  R172 D9: the R-part *is* Siegel–Weil-visible via coset Schwartz functions, but then it is the split-plane coset
  count (B2), not a parity statement. Consistent.
* **B2** (Cor 2) and **B1** (the M | 24 slices are the Mordell-type congruence world; ET's quadratic covering).
* **T1** passes trivially (Diff-parity is T1).
* **B6** not engaged.

## Cheap numerics (EVIDENCE)
`scripts/bsC_quad_slices_fast.py 1000000 20000` (7 s; divisor forms cross-checked against the tuple enumerator for all
primes < 2·10⁴: 0 mismatches). Primes p ≡ 1 (24) **not** covered by any Type I/II slice with 4cd | 24:
1/143 (p < 10⁴), 8/1181 (< 10⁵), 33/3202 (< 3·10⁵), 71/9732 (< 10⁶); first ones 3361, 31081, 34897, 62497, 66889.
All primes p ≢ 1 (24) below 5·10⁴ are covered (`bsC_quadratic_slices.py 50000`); odd squares: 0 tuples.
So the "parity-visible" part of ES is large (≈ 99.3% of the hard class at 10⁶) but provably not all of it
(conditionally), and its existence step inside each slice is still a divisor event, not a parity consequence.

## Assessment
**PROVED: Prop 1 (for ℚ-rational Diff data) and the group-theoretic half of Cor 2 (ES's ray condition is quadratic only
for M | 24). Assessment: parity/incoherence mechanisms built on ℚ-rational data carry only quadratic information about
the divisor (R176 repair D2: F-rational data escape Prop 1).** Spark 4 collapses.
Promise 1 (clean negative; a sharp "why" for the Mordell ceiling in Kudla language).
