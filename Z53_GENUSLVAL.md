# Z53_GENUSLVAL — the full genus layer at one prime: unconditional log² lower bound and slice closed forms

Status: z53 depth lane GENUSLVAL, **checkpoint 1 (skeleton)**. Internal only. **ES is OPEN; nothing here proves or
disproves ES or (★) at any infinite set of primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z53_genuslval_*`, data `data/z53/genuslval/`.

## (a) Statements attacked

Notation as in `SINGLE_P_COUNT.md` §2 / FRONTIER §2.1: for a prime p, 𝒫(p) = {(u, B) : gcd(u, B) = 1, u + B odd,
4uB − u − B ≤ p}, q = 4uB, a = −(u + B), s(q) = |(ℤ/q)^×/□|,
  M_gen(p) = Σ_{𝒫(p)} (s(q)/φ(q))·1[p·a ∈ ((ℤ/q)^×)²]   (the order-≤2 character layer of R(p)).

**Target 1 (FRONTIER §7.4).** An unconditional lower bound M_gen(p) ≥ c·log²p, p ≡ 1 (4), p → ∞.

**Theorem U (claimed PROVED here; full proof §2 of the final memo).** There is an absolute, *effective* p₀ such that for
every prime p ≡ 1 (mod 4), p ≥ p₀,
  **M_gen(p) ≥ c_U·(log p)²,  c_U = 75/(224π⁴) − ε ≈ 0.00343** (any fixed ε > 0; p₀ = p₀(ε)).
Input: Burgess' bound for primitive characters to *cube-free* moduli, all r ≥ 1 (Burgess 1963; Iwaniec–Kowalski Thm 12.6;
restated in Hasanalizade–Lin–Martin–Luna Martínez–Treviño arXiv:2511.17778, abstract), and Pólya–Vinogradov. No zero-free
region, no Siegel. With Burgess for r ≤ 3 only (any modulus) the same proof gives c = 1/(9π⁴) ≈ 0.00114.

**Target 2 (brief (b)/(c), FRONTIER §7.3 flavour).** Closed form of the genus layer: for a fixed odd squarefree
u ≤ p^α, the u-slice of M_gen is a finite signed sum over the real characters η mod 4u of
  [η = 1]·A_u·(log of the B-range) + L(1, η)·L(1, η·χ_{−4up})·H_{u,η}(1)  (+ power saving),
with A_u ∝ L(1, χ_{−4up}). These L(1, χ_pψ)·L(1, ψ′) products are exactly the "other genus characters" of §7.3.

## (b) Why this is not already closed

* (J)98 (`SINGLE_P_COUNT` Prop 4.1) uses prime witnesses (u, B) = (1, 2ℓ) only → log log p under GRH.
* `LOWERTAIL_DEEP_ASTRA` Thm 5.4 proves 2/π⁴·log²p **CONDITIONAL on a fixed zero-free strip**, used for two things:
  (i) the windowed w-sums Σ_w η(w)2^{ω(w)}1[split]/φ(w) with characters of modulus up to 4up ≈ p^{1+α₁}, and
  (ii) the average over u of L(1, χ_{−4up}). FRONTIER §7.4 lists the unconditional version as open.
* New ingredient: both uses only need **power savings for character sums of length ≥ (conductor)^{1/4+ε}**, which Burgess
  gives unconditionally for cube-free conductors (all ours are 4·squarefree), provided the exponent windows are moved:
  w ∈ (p^β, p^γ] with β > (1 + 2α₁)/4 (hyperbola for L(s, η)L(s, ηχ_D)), and u ∈ (p^{α₀}, p^{α₁}] with
  α₀ > (1 + α₁)/8 (Burgess tail of L(1, χ_{−4up}) at p^ν, ν > (1 + α₁)/4, plus Pólya–Vinogradov averaging over u needing
  ν < 2α₀). Sharp windows replace Mellin smoothing; the window difference kills every constant (cross) term, so only the
  η = 1 log-term survives. Optimising (γ − β)(α₁ − α₀) gives 75/1792 at α₁ = 9/28; c_U = (8/π⁴)·75/1792.
* None of the closed items (hyperbola dualisation, ET/Fejér, CS, low-conductor universality, inverse lemma, menus) is used
  or reopened: this is main-term (B3) work on the explicit genus term, as the brief says.

## (c) First lemma and first falsifier (status)

* **Lemma 1 (PROVED; = Thm 5.4 (19)–(20), rechecked).** For squarefree u ≡ 1 (4), odd squarefree w coprime to up, the pairs
  (u, 2w), (2w, u) lie in 𝒫(p) when 8uw ≤ p, have genus weight 2^{ω(u)+ω(w)}/(φ(u)φ(w)) each, and are genus-matched iff
  (i) every ℓ | w splits in ℚ(√−up) [χ_{−4up}(ℓ) = 1], (ii) (w/ℓ) = (−2p/ℓ) for ℓ | u, (iii) w ≡ −(p + u)/2 (mod 4).
  Hence M_gen(p) ≥ Σ_u φ(u)⁻¹ Σ_{η real mod 4u} ε_η S_η(u), S_η(u) = Σ_{w ∈ window} η(w)·Σ_{b|w}χ_{−4up}(b)/φ(w).
* **Falsifier F1 (to run):** at the 14 (★)-zero primes, 10³…10⁸ samples and odd-square controls, (1) check every family
  pair is genus-matched by the direct square-class test (any failure kills Lemma 1); (2) check the family sum ≤ M_gen;
  (3) compare the windowed family sum with its predicted main term (γ − β)log p·Σ_u A_u/φ(u) (A_u from exact class
  numbers). Result: see §4 (pending at checkpoint).
