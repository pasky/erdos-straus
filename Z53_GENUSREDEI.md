# Z53_GENUSREDEI — joint factor-multiset realisation: what can data at p force about ALL prime factors? (z53, lane GENUSREDEI)

**ES is OPEN. Nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. All results are internal and internally reviewed only. Targets FRONTIER §7.6 (full-factor-multiset
realisation, `CLASS_FORCING.md` §6) and the "class beyond parity" part of §7.3, via the lane angle "joint / higher genus
structure" (Rédei matrices, quartic/spin data, governing fields, quaternion dictionaries).
Scripts `scripts/z53_genusredei_*`; data `data/z53/genusredei/` (144 KB).

## 0. Status / iteration log
* cp1 (commit 5be2ad48): precise statement, why not closed, law lemma, falsifier design.
* cp2: falsifier run (§6): the free model (product law only, harmonic-weighted classes) fits the bounded-level event rates of
  primes to |z| ≲ 3 on 30 lines at 10⁷ and 10⁸, with no dependence on non-abelian Frobenius data of p (Σz² = 101 and 124 on
  120 stratum tests); odd squares and near-squares are detected at z down to −80 and −42 (positive controls).
* cp3: full proofs (§3–§5): law lemma (PROVED), Joint Realisation Theorem (CONDITIONAL on HC), unconditional partial
  realisation (PROVED), Dickson-hardness of the exact statement (PROVED), exact bounded-level forcing criterion (CONDITIONAL).
* cp4: hostile review (§10) and repairs.

## 1. The statement attacked (precise)

**Lines.** A *line* is L(x) = (αx + β)/γ with integers α, γ ≥ 1, β ≠ 0, gcd(α, β) = 1, together with a *level* t ≥ 3 (the
modulus of its divisor event). The four ES lines (CLASS_FORCING §1) are p + 4d (α = 1, β = 4d, γ = 1, t = 4d), 4Cp + 1
(α = 4C, β = 1, γ = 1, t = 4C; this is the (★) line), (p + e)/4 and (pe + 1)/4 (γ = 4, t = e). Fix finitely many lines
L_1, …, L_r with pairwise R_{jj′} := α_{j′}β_j − α_jβ_{j′} ≠ 0 (non-proportional).

**Parameters.** n ≥ 1 (an order of power-residue symbols; n = 1 means "no symbols"). B ≥ r + 1, B ≥ n, B ≥ every prime factor of
∏_j α_jβ_jγ_j·∏_{j≠j′}R_{jj′}. T := a B-smooth modulus divisible by 4∏_{q≤B}q and by every level t_j. Ω := a finite Galois
extension of ℚ containing Ω_{B,n} := ℚ(ζ_{4n}, q^{1/n} : q ≤ B prime) (any governing field, Rédei field, Kummer field, ring class
field may be adjoined). M := a B-smooth modulus divisible by T and by the conductor of Ω^{ab} (the maximal abelian subfield),
with exponents e_q large (fixed below).

**p-datum.** Π = (σ, r): an element σ ∈ Gal(Ω/ℚ) fixing ζ_{4n}, and r ∈ (ℤ/M)^× with Art(r)|_{Ω^{ab}} = σ|_{Ω^{ab}}. A prime p
*has datum Π* if p ≡ r (mod M) and Frob_𝔓 = σ for some prime 𝔓 | p of Ω. Π is *admissible* if α_j r + β_j ≢ 0 (mod q^{e_q − v_q(Tγ_j)})
for all j and q ≤ B (for fixed r this holds once the e_q are large; the excluded r have Haar measure → 0 as e_q → ∞); then for x ≡ r (M) the B-smooth part s_j of L_j(x) and g_j := L_j(x)/s_j mod T are constant (CLASS_FORCING
Thm 3.4 uses the same device). For σ fixing μ_n put κ_σ(y) := σ(y^{1/n})/y^{1/n} ∈ μ_n for y ∈ ℚ^× supported on {−1} ∪ {q ≤ B}
(well defined since σ fixes μ_n; κ_σ(y) = (y/𝔭)_n at 𝔭 = 𝔓 ∩ ℚ(ζ_n)).

**Decorated configuration** of a prime p with datum Π (fix 𝔓 with Frob_𝔓 = σ, 𝔭 = 𝔓 ∩ ℚ(ζ_n)): write L_j(p) = s_j·∏_{i=1}^{k_j} ℓ_{j,i}
with primes ℓ_{j,i} > B. For each large factor x = (j, i):
* (D1) its class a_x = ℓ_x mod T;
* (D2) its n-th power symbol ζ_x = (ℓ_x/𝔭)_n ∈ μ_n at p ("spin/quartic data of the factor at p");
* (D3) the mutual Legendre symbols ε(x, y) = (ℓ_x/ℓ_y) for all large factors x ≠ y of all lines (the joint Rédei matrix of the
  factor set; with (D1) it also fixes the symbols against the small primes q ≤ B).
A *configuration* Γ is any such abstract data: k_j ≥ 1, a_x ∈ (ℤ/T)^×, ζ_x ∈ μ_n, ε(x, y) ∈ {±1}.

**Question (§7.6, precise).** Which properties of the decorated configuration hold for *every* large prime with datum Π?
(CLASS_FORCING Thm 5.2: no single large factor has a forbidden class.) Is anything *joint* forced beyond the product of the
classes and the parity links?

**Answer.**
* (PROVED, §3) Five laws hold identically: (L1) product law mod T, (L2) product law for the symbols, (L3) parity link,
  (L4) cross-line law, (L5) quadratic reciprocity.
* (CONDITIONAL on HC, §4, **Theorem JRT**) Every configuration satisfying (L1)–(L5) is realised by infinitely many primes with
  datum Π. Hence the forced joint content of all-factor data is *exactly* (L1)–(L5).
* (PROVED, §5.1, **Theorem U**) Unconditionally, every finite *partial* configuration consistent with (L3), (L5) occurs (as
  exactly-dividing factors) for a positive density of primes with datum Π: the only laws that need the *complete* factor set
  are the product laws (L1), (L2), (L4).
* (PROVED, §5.2) The exact statement of JRT for one line and one configuration is a Hardy–Littlewood prime-pair statement, so
  JRT cannot be made unconditional without new prime-pair input.
* (CONDITIONAL on HC, §5.3, **Corollary F**) A divisor event at finitely many lines/levels is forced on a datum Π iff it is forced
  by the one-large-factor configuration — exactly the B1 criterion of CLASS_FORCING Prop 3.2. This upgrades CLASS_FORCING
  Thm 6.1 (one-sided; only data with trivial abelian shadow) to an exact criterion for every Chebotarev datum, and shows
  that decorations (spins, quartic symbols, Rédei matrices) cannot change it.
* (PROVED, §5.4) At odd squares an extra law (L3□) holds, and it is exactly T1; at near-squares p = m² + k representation laws
  appear (the (J)53 deformation). Joint laws beyond (L1)–(L5) arise only from data of p that are not Frobenius data, and the
  ones known are anti-forcing.

## 2. Why this is not already closed
* CLASS_FORCING Thm 5.2 is single-factor. Lemma 3.1's realisability is abstract (integers, not values of a line at primes).
  Thm 6.1 exhibits *one* bad configuration (the p ≡ 1 (M) point, all cofactors prime) and only for data with trivial abelian
  shadow. FRONTIER §3 lists "joint restrictions on all varying prime factors" under *Does NOT rule out*; TWO_POWER_LADDER Thm
  3.1 is scoped to one varying level prime and explicitly "says nothing about joint restrictions".
* Decorations that involve p itself at the factors ((ℓ/p)_n: quartic/spin-type data of the factors) and the joint Rédei
  matrix of all factors across several lines are not treated anywhere in the repository (`git grep` for "joint Rédei",
  "(ℓ/p)_4", "mutual symbol": no hits in CLASS_FORCING / TWO_POWER_LADDER / bsB_redei_oddpart).
* The closed item "bounded-level reciprocity along forced progressions with one varying level prime gives only parity" is the
  one-prime case; here all prime factors vary jointly, across several lines, with p-relative decorations.
* *Novelty (Assessment).* The realisation technique (HC for linear forms after fixing a CRT residue and the small primes) is that
  of CLASS_FORCING Thm 6.1 / B1_LINE Thm 4.2. New here: the complete list of pointwise joint laws for decorated configurations
  (Lemma 3.1, including the p-relative symbols and the cross-line law (L4)), the realisation of *every* law-compatible
  configuration (not one), the abelian-part computation that makes this work for every Chebotarev datum (Step 3(b)), the
  resulting iff-criterion (Corollary F), the unconditional partial theorem (Thm U), and the Dickson-hardness remark (Prop D).

## 3. The five laws (PROVED, elementary)

**Lemma 3.1.** Let p be a prime with datum Π, p > B, p ∤ ∏β_jγ_j, with decorated configuration as in §1. Then:
* (L1) s_j·∏_i a_{j,i} ≡ L_j(p) ≡ s_j·g_j (mod T) for each j;
* (L2) ∏_i ζ_{j,i} = κ_σ(β_j/(γ_j s_j)) for each j;
* (L3) if n is even: ζ_x^{n/2} = χ_j(a_x) for each large factor x of line j, where χ_j(ℓ) := (−α_jβ_j/ℓ) (Jacobi symbol in ℓ,
  a Dirichlet character of ℓ modulo 4·rad(α_jβ_j), which divides T);
* (L4) for j ≠ j′ and each large factor y of line j′: ∏_i ε((j, i), y) = ψ_{jj′}(a_y), where ψ_{jj′}(ℓ) := (R_{jj′}γ_jα_{j′}s_j/ℓ)
  (a character of ℓ modulo 4·rad(R_{jj′}γ_jα_{j′}s_j), which divides T);
* (L5) ε(x, y)ε(y, x) = (−1)^{(a_x−1)(a_y−1)/4} (computed from a_x, a_y mod 4).
*Proof.* (L1): L_j(p) = s_j∏ℓ_{j,i} and reduce mod T; s_j and g_j are constant on p ≡ r (M) by admissibility.
(L2): since p ∤ γ_j, L_j(p) ≡ β_j/γ_j (mod p), so (L_j(p)/𝔭)_n = ((β_j/γ_j)/𝔭)_n; multiplicativity of the symbol gives
∏_i(ℓ_{j,i}/𝔭)_n = ((β_j/(γ_js_j))/𝔭)_n, and for y supported on {−1} ∪ {q ≤ B}, (y/𝔭)_n = κ_σ(y) because Frob_𝔓 = σ acts on y^{1/n}
by y^{1/n} ↦ y^{p/n} (mod 𝔓). (L3): ℓ | α_jp + β_j and ℓ ∤ α_jβ_j give p ≡ −β_j/α_j (mod ℓ), so (p/ℓ) = (−α_jβ_j/ℓ) (multiply
by α_j²); (ℓ/𝔭)_n^{n/2} = (ℓ/p) = (p/ℓ) since p ≡ 1 (mod 4). For fixed D = −α_jβ_j the map ℓ ↦ (D/ℓ) on odd primes ℓ ∤ D is a
Dirichlet character mod 4·rad(D) (quadratic reciprocity; square factors of D do not matter). (L4): ℓ′ := ℓ_y divides
α_{j′}p + β_{j′}, so α_{j′}p ≡ −β_{j′} and γ_jα_{j′}L_j(p) = α_jα_{j′}p + α_{j′}β_j ≡ R_{jj′} (mod ℓ′); ℓ′ ∤ R_{jj′}γ_jα_{j′}
(ℓ′ > B). Hence (L_j(p)/ℓ′) = (R_{jj′}γ_jα_{j′}/ℓ′), and multiplicativity over L_j(p) = s_j∏_iℓ_{j,i} gives the claim
(Jacobi symbols with square factors removed; ψ is a character mod 4·rad(·) by reciprocity). (L5): quadratic reciprocity. ∎
*Remark.* No large prime divides two lines (it would divide R_{jj′}; privacy, SPARKS8 Lemma 2.3), so the factor sets of the
lines are disjoint. (L1)+(L3) is the "product + parity" of CLASS_FORCING; (L2) is the product law in 𝔽_p^×/𝔽_p^{×n}; (L4) is
the parity link of line j′ "seen from" line j; (L5) is reciprocity.

## 4. The Joint Realisation Theorem (CONDITIONAL on HC)

**Hypothesis HC** (verbatim from CLASS_FORCING §6, R272-corrected). Let f₀, …, f_s ∈ ℤ[k] be linear, Ω′/ℚ finite Galois,
C′ ⊂ Gal(Ω′/ℚ) a conjugacy class, Ω′₀ := Ω′ ∩ ℚ^{ab} of conductor m, and A ⊂ (ℤ/m)^× the residues whose Artin symbol on Ω′₀
lies in C′|_{Ω′₀}. If there is k₀ with f₀(k₀) mod m ∈ A such that the system j ↦ f_i(k₀ + mj) (0 ≤ i ≤ s) is admissible, then
there are infinitely many k ≡ k₀ (mod m) with all f_i(k) prime and Frob_{f₀(k)}|_{Ω′} ∈ C′.
(Ω′ = ℚ is Dickson's conjecture. HC is a standard Bateman–Horn–Chebotarev heuristic, not a published theorem.)

**Theorem JRT.** Assume HC. Let the lines, n, B, T, Ω, M and an admissible datum Π = (σ, r) be as in §1. Let Γ be a configuration
satisfying (L1)–(L5) (with s_j, g_j, κ_σ taken from Π). Then there are infinitely many primes p with datum Π whose decorated
configuration is Γ; i.e. L_j(p) = s_j·∏_{i≤k_j}ℓ_{j,i} with distinct primes ℓ_{j,i} > B, ℓ_x ≡ a_x (mod T), (ℓ_x/𝔭)_n = ζ_x at a
prime 𝔭 = 𝔓 ∩ ℚ(ζ_n) with Frob_𝔓|_Ω = σ, and (ℓ_x/ℓ_y) = ε(x, y) for all x ≠ y.

*Proof.* Call x = (j, i) *chosen* if i < k_j and *last* if i = k_j. Let Y > B·max|R_{jj′}|·disc-primes(Ω).

*Step 1 (choose the chosen primes; Dirichlet, unconditional).* Enumerate the chosen indices x₁, x₂, …. Choose ℓ_{x₁} > Y prime,
unramified in Ω, with ℓ_{x₁} ≡ a_{x₁} (mod T). Having chosen ℓ_{x₁}, …, ℓ_{x_{m−1}}, choose ℓ_{x_m} > Y, ℓ_{x_m} ∉ {ℓ_{x_1}, …},
unramified in Ω, with ℓ_{x_m} ≡ a_{x_m} (mod T) and (ℓ_{x_m}/ℓ_{x_h}) = ε(x_m, x_h) for h < m (a congruence condition modulo each
ℓ_{x_h}; Dirichlet in a progression modulo T∏_hℓ_{x_h}, coprime moduli). By (L5) also (ℓ_{x_h}/ℓ_{x_m}) = ε(x_h, x_m). Put
Q_j := ∏_{i<k_j}ℓ_{j,i}.

*Step 2 (congruences on p).* For each chosen x = (j, i) pick a residue c_x mod ℓ_x² with: α_jc_x + β_j ≡ 0 (mod ℓ_x), and
L_j(c_x)/ℓ_x ≡ w_x (mod ℓ_x) where w_x ≢ 0 is chosen with (w_x/ℓ_x) = ε((j, k_j), x)·((s_jQ_j/ℓ_x)/ℓ_x) (possible: writing
c = c₁ + ℓ_xu, γ_jL_j(c)/ℓ_x = (α_jc₁ + β_j)/ℓ_x + α_ju runs over all residues mod ℓ_x as u does, α_jγ_j being a unit mod ℓ_x).
Let W := M·∏_xℓ_x², and p₀ mod W the CRT solution of p₀ ≡ r (M), p₀ ≡ c_x (ℓ_x²).

*Step 3 (the Galois datum).* Let K := ℚ(ζ_n, ℓ_x^{1/n} : x chosen) and Ω_tot := ΩK. Facts (proved below): (a) Ω ∩ K = ℚ(ζ_n)
and Gal(K/ℚ(ζ_n)) ≅ μ_n^{(#chosen)}; (b) the maximal abelian subfield is Ω_tot^{ab} = Ω^{ab}·ℚ(√ℓ_x : x chosen) if n is even,
and Ω^{ab} if n is odd. By (a), Gal(Ω_tot/ℚ) = Gal(Ω/ℚ) ×_{Gal(ℚ(ζ_n)/ℚ)} Gal(K/ℚ), so there is σ₀ ∈ Gal(Ω_tot/ℚ) with σ₀|_Ω = σ
and σ₀(ℓ_x^{1/n}) = ζ_xℓ_x^{1/n} for every chosen x (σ fixes ζ_n, and Gal(K/ℚ(ζ_n)) is the full μ_n^{(#chosen)}). Let C′ be the
conjugacy class of σ₀.
*Proof of (a).* Ω ∩ K ⊇ ℚ(ζ_n). Every intermediate field ℚ(ζ_n) ⊊ F ⊆ K is, by Kummer theory, ℚ(ζ_n)(Δ^{1/n}) for a nontrivial
subgroup Δ ⊂ ⟨ℓ_x⟩K₀^{×n}/K₀^{×n} (K₀ := ℚ(ζ_n)), so contains β^{1/n} for some β = ∏ℓ_x^{e_x} with some n ∤ e_x; at a prime λ | ℓ_x of
K₀ (unramified, v_λ(β) = e_x, ℓ_x ∤ n) the extension K₀(β^{1/n})/K₀ has ramification index n/gcd(n, e_x) > 1. Ω is unramified at ℓ_x,
so F ⊄ Ω. The same valuation argument shows the ℓ_x are independent in K₀^×/K₀^{×n}, so Gal(K/K₀) ≅ μ_n^{(#chosen)}. ∎
*Proof of (b).* G := Gal(Ω_tot/ℚ), V := Gal(Ω_tot/Ω) ≅ Gal(K/K₀) ≅ μ_n^{(#chosen)} (by (a)), normal in G, with G acting on V through
G → Gal(K₀/ℚ) ≅ (ℤ/n)^× by v ↦ v^u (as σ̃(ζ^a) = ζ^{ua} for the Kummer values). Then [G, V] ∋ v^{u−1} for every u ∈ (ℤ/n)^×
(G → (ℤ/n)^× is onto). For n odd, u = 2 gives [G, V] = V, so G^{ab} = Gal(Ω/ℚ)^{ab}. For n even, the u − 1 generate 2ℤ/n (u = −1),
so [G, V] ⊇ V², and G^{ab} is a quotient of G/V² = Gal(Ω(√ℓ_x)/ℚ). Finally, for Galois L and abelian A, (LA)^{ab} = L^{ab}A: in
Gal(LA/ℚ) = Gal(L/ℚ) ×_{Q} Gal(A/ℚ) (Q abelian) the commutator subgroup is {([g, h], 1)}. Apply with L = Ω, A = ℚ(√ℓ_x : x),
and note Ω_tot^{ab} ⊇ Ω^{ab}(√ℓ_x) trivially. ∎

*Step 4 (the forms).* Put f₀(k) := p₀ + Wk and f_j(k) := L_j(p₀ + Wk)/(s_jQ_j) (1 ≤ j ≤ r). By admissibility,
ν_{j,q} := v_q(α_jr + β_j) < e_q − v_q(Tγ_j) for all q ≤ B, so v_q(α_jx + β_j) = ν_{j,q} for every x ≡ r (mod M) and
v_q(s_j) = ν_{j,q} − v_q(γ_j). Then:
(i) f_j ∈ ℤ[k]: s_jQ_jγ_j | α_jp₀ + β_j by construction, and s_jQ_jγ_j | α_jW (q-adically for q ≤ B since
v_q(s_jγ_j) = ν_{j,q} < e_q − v_q(T) ≤ v_q(W); and ℓ_x² | W). Indeed v_q(α_jW/(γ_js_jQ_j)) ≥ v_q(T) + 1 for q ≤ B.
(ii) Constancy: for q | M (q ≤ B) and for q = ℓ_x, f_j(k) ≡ f_j(0) (mod q) and f₀(k) ≡ p₀ (mod q), because q divides the leading
coefficient α_jW/(γ_js_jQ_j) (for q = ℓ_x with x on line j: v_{ℓ_x}(W) = 2 > 1 = v_{ℓ_x}(Q_j)). Moreover T | α_jW/(γ_js_jQ_j), so
f_j(k) ≡ f_j(0) (mod T).
(iii) Admissibility: q ≤ B: f₀(0) = p₀ is a q-unit; f_j(0) = (L_j(p₀)/s_j)/Q_j is a q-unit because s_j is the full B-smooth part.
q = ℓ_x, x on line j: ℓ_x ∥ L_j(p₀) by Step 2, so ℓ_x ∤ f_j(0); ℓ_x ∤ L_{j′}(p₀) for j′ ≠ j (else ℓ_x | R_{jj′}, but ℓ_x > Y); ℓ_x ∤ p₀.
q > B, q ∉ {ℓ_x}: every form has q-unit leading coefficient (W, α_j have no such prime factor), so each of the r + 1 forms
vanishes at one residue mod q and r + 1 < q (B ≥ r + 1).
(iv) The forms are pairwise non-proportional (R_{jj′} ≠ 0, β_j ≠ 0) and of positive leading coefficient.
(v) The HC local condition: m := conductor of Ω_tot^{ab} divides W (it divides lcm(cond Ω^{ab}, n, 4∏ℓ_x), all dividing W). So
f₀(k) ≡ p₀ (mod m) for all k, and we need Art(p₀)|_{Ω_tot^{ab}} = σ₀|_{Ω_tot^{ab}}. On Ω^{ab}: Art(r) = σ|_{Ω^{ab}} (datum). On
ℚ(√ℓ_x) (n even): Art(p₀) = χ_{ℓ_x}(p₀) = (p₀/ℓ_x) (p₀ ≡ 1 mod 4) = (−α_jβ_j/ℓ_x) = χ_j(a_x) (Step 2 and (L3)'s computation), while
σ₀(√ℓ_x)/√ℓ_x = (σ₀(ℓ_x^{1/n})/ℓ_x^{1/n})^{n/2} = ζ_x^{n/2}; these agree by (L3) for Γ.
Apply HC with Ω′ = Ω_tot, C′, k₀ = 0: f₀(0) = p₀ mod m lies in A, and the system j ↦ f_i(mj) is admissible (for q | m every
f_i is constant mod q by (ii), with unit value by (iii); for q ∤ m the substitution k = mj permutes residues mod q).
HC now gives infinitely many k with f₀(k) =: p and every f_j(k) =: ℓ_{j,k_j} prime, and Frob_p|_{Ω_tot} ∈ C′.

*Step 5 (read off the configuration).* Fix 𝔓_tot | p with Frob = σ₀; 𝔓 := 𝔓_tot ∩ Ω has Frob_𝔓 = σ, and p ≡ r (M): p has datum Π.
For k large, ℓ_{j,k_j} > Y is distinct from all chosen primes and from the other last factors (non-proportional forms coincide
for at most one k). By (ii), v_q(L_j(p)) = ν_{j,q} − v_q(γ_j) for q ≤ B, so L_j(p) = s_j·Q_j·ℓ_{j,k_j} is the factorisation
into the smooth part and the primes > B, with k_j large factors. Decorations: chosen classes by Step 1; last classes:
ℓ_{j,k_j} ≡ f_j(0) = (L_j(p₀)/s_j)/Q_j ≡ g_j·∏_{i<k_j}a_{j,i}⁻¹ ≡ a_{j,k_j} (mod T) by (ii) and (L1) for Γ. Chosen symbols:
(ℓ_x/𝔭)_n = σ₀(ℓ_x^{1/n})/ℓ_x^{1/n} = ζ_x. Last symbols: Lemma 3.1 (L2) holds for p, and Γ satisfies (L2) with the same right
side κ_σ(β_j/(γ_js_j)), so the last symbol equals ζ_{j,k_j}. Mutual symbols: chosen–chosen by Step 1; (last of line j, chosen x of
line j) by Step 2: (ℓ_{j,k_j}/ℓ_x) = (L_j(p)/ℓ_x / ℓ_x)·((s_jQ_j/ℓ_x)/ℓ_x) = (w_x/ℓ_x)((s_jQ_j/ℓ_x)/ℓ_x) = ε((j,k_j), x), and the
reverse symbol by (L5). Every remaining mutual symbol involves a last factor and a factor of another line, and is determined
by (L4)+(L5) from the symbols already fixed and the classes: (last of j, chosen y of j′) by (L4)[j over y]; (last of j, last of
j′) by (L4)[j over last of j′] after the symbols (chosen of j, last of j′) are fixed by (L5) from (L4)[j′ over chosen of j]. Both the
realised configuration (Lemma 3.1) and Γ satisfy (L4), (L5) with identical inputs, so these symbols agree with Γ. ∎

**Corollary 4.1 (the forced joint content; CONDITIONAL on HC).** A property P of decorated configurations holds for every
sufficiently large prime with datum Π iff P holds for every configuration satisfying (L1)–(L5). In particular, given *all*
decorations (D2), (D3) — all n-th power symbols of the factors at p, the full joint Rédei matrix — the classes of the large
factors are constrained by nothing except (L1) and the parity links (L3)/(L4): the "class beyond parity" is jointly free.
*Proof.* ⇐ by Lemma 3.1 (every realised configuration satisfies the laws); ⇒ by JRT (a configuration violating P is realised
infinitely often). ∎

**Remark 4.2 (non-abelian decorations of the factors).** Prescribing also Frob_{ℓ_x} in a fixed non-abelian Galois Ω′ works
for chosen factors (Chebotarev in Step 1) and needs, for the last factors, a version of HC with Frobenius conditions on
several values (HC⁺: Frob_{f_i(k)} ∈ C_i for all i); with HC⁺ the theorem extends with the abelian product law in
Gal(Ω′^{ab}/ℚ) added to (L1). Not needed for ES events, which depend on classes only. *(Assessment.)* Rédei symbols
[a, b, ℓ] of the chosen factors relative to fixed a, b are Frobenius data of ℓ (Step 1 handles them); Rédei/4-rank data of
p-dependent fields such as ℚ(√−Cp) are functions of the mutual symbols with the primes of Cp and of the classes, i.e. of
(D1)–(D3) plus Frobenius data of p in fields depending on the chosen factors — the HC construction accommodates the latter
(adjoin them to K in Step 3), but the abelian-part computation (b) would have to be redone for each such field; not done here.

## 5. Unconditional companions, the hardness of JRT, and the exact forcing criterion

### 5.1 Theorem U (finite partial configurations; PROVED, unconditional)
Let the lines, n, B, T, Ω, M, Π be as in §1 (Π admissible). Specify for each j a number m_j ≥ 0 of factors with decorations
a_x, ζ_x and mutual symbols ε(x, y) among the specified factors, satisfying (L3) and (L5). Then the set of primes p with datum Π
for which there are distinct primes ℓ_x > Y (x = (j, i), i ≤ m_j) with ℓ_x ∥ L_j(p) and the prescribed (D1)–(D3) data (at a
prime 𝔭 = 𝔓 ∩ ℚ(ζ_n) with Frob_𝔓|_Ω = σ) has positive lower natural density among all primes, for every Y.
*Proof.* Steps 1–3 of JRT with all specified factors "chosen" (no last factor; in Step 2 drop the w_x condition and only ask
ℓ_x ∥ L_j(c_x)). Consider Ω_tot·ℚ(ζ_W) and the set S of τ in its Galois group with τ|_{Ω_tot} conjugate to σ₀ and
τ|_{ℚ(ζ_W)} = Art(p₀). S is non-empty: the Galois group is the fibre product over Ω_tot ∩ ℚ(ζ_W) ⊆ Ω_tot^{ab}, and σ₀ and Art(p₀) agree
on Ω_tot^{ab} (Step 4(v), which uses only (L3) and the datum). S is a union of conjugacy classes (ℚ(ζ_W) is abelian), so by Chebotarev
the primes with Frobenius in S — i.e. p ≡ p₀ (mod W) with Frob_p|_{Ω_tot} ∋ σ₀ up to conjugacy — have density |S|/[Ω_tot(ζ_W) : ℚ] > 0.
Each such p has datum Π (as in Step 5), ℓ_x ∥ L_j(p) (congruence mod ℓ_x²), the classes (Step 1), the mutual symbols among the
specified factors (Step 1) and the symbols ζ_x at 𝔭 (as in Step 5). ∎
*Reading.* Any law that constrains only boundedly many large factors (rather than the complete factor set) is already implied
by (L3) and (L5); the laws that bind the classes beyond parity — (L1), (L2), (L4) — all involve the *complete* factorisation.
This is why the realisation question is a prime-tuple question (5.2).

### 5.2 Proposition D (JRT is Dickson-hard; PROVED)
Take one line L(p) = p + 4 (level 4), n = 1, Ω = ℚ(ζ₄) = Ω_{B,1}, B = 5, T = 120, M = 3600, and Π = (σ, r) with σ = id, r ≡ 1 (mod 4),
r ≢ 0, −4 (mod 3) and (mod 5); then ν_{q} = 0 for q ≤ 5 (Π admissible) and s = 1. The one-factor configuration (k = 1) satisfies (L1)–(L5). Its realisation by infinitely many p is the statement
"p and p + 4 are both prime for infinitely many p" (cousin primes), which is open. Hence JRT, even for one line and one
configuration, contains an open Hardy–Littlewood pair; no unconditional proof is possible without new prime-pair input.
*Proof.* Realisation means L(p) = s·ℓ with ℓ prime, s = 1. ∎
*(Assessment.)* For a *single* line and a datum that is a congruence class, unconditional infinitude of *some* event-avoiding
configuration (e.g. "all prime factors of p + 4 are ≡ 1 (4)", which kills the d = 1 event) is plausibly within reach of
Iwaniec's semi-linear sieve (primes of the form φ(x, y) + A, Acta Arith. 21 (1972)) — not verified here; for several lines at
once the sieve dimension grows and this route closes. Corollary F below is therefore stated relative to HC.

### 5.3 Corollary F (exact bounded-level forcing criterion; CONDITIONAL on HC)
For each line j let E_j be its divisor event at level t_j (some divisor of L_j(p) is ≡ −1 (mod t_j); or the signed
e-slice version −1 ∈ Σ^±). For an admissible datum Π, the disjunction ⋁_j E_j holds for all sufficiently large primes with
datum Π iff for some j:  −1 ∈ Σ(s_j) ∪ Σ(s_j)·g_j  (signed: −1 ∈ Σ^±(s_j)·{1, g_j, g_j⁻¹}), where Σ(s_j) is the set of classes mod t_j
of divisors of s_j. In particular, the answer depends only on p mod M (B1), and no additional Frobenius datum of p (any governing
field, Rédei field, Kummer field) and no knowledge of the factors' decorations (D2), (D3) changes it.
*Proof.* ⇐: a divisor of s_j, possibly times L_j(p)/s_j (whose class is g_j), lies in the class −1. ⇒: the configuration with
k_j = 1 for every j, a_{j,1} = g_j, ζ_{j,1} := κ_σ(β_j/(γ_js_j)) and the forced mutual symbols satisfies (L1), (L2), (L4), (L5)
by construction (mutual symbols ε((j,1),(j′,1)) := ψ_{jj′}(g_{j′})); (L3) and (L5) hold because they hold for the integers
N_j := L_j(p)/s_j of any prime p with datum Π (such p exist by Chebotarev): N_j ≡ g_j (mod T) is odd, positive, a product of primes
> B, and the N_j are pairwise coprime (privacy). Hence χ_j(g_j) = ∏_{ℓ|N_j}χ_j(ℓ) = ∏_{ℓ|N_j}(ℓ/p) = (N_j/p) = ((β_j/(γ_js_j))/p) = ζ_{j,1}^{n/2}
((L3) for each ℓ; N_j ≡ β_j/(γ_js_j) mod p), and the Jacobi symbols satisfy (N_j/N_{j′}) = ∏_{ℓ′|N_{j′}}ψ_{jj′}(ℓ′) = ψ_{jj′}(g_{j′}) ((L4) for each
ℓ′), so Jacobi reciprocity for N_j, N_{j′} is exactly (L5) for the prescribed symbols. By JRT the configuration is realised by
infinitely many p, at which L_j(p) = s_j·ℓ_j and Σ(L_j(p)) = Σ(s_j) ∪ Σ(s_j)·g_j. ∎
*Reading.* This is CLASS_FORCING Prop 3.2 (forced criterion, "L prime is compatible") promoted from abstract integers to
values at primes, uniformly over every Chebotarev datum, and simultaneously for all lines. It removes Thm 6.1's restriction
C|_{Ω₀} = 1 and turns its one-sided statement into an iff. Combined with CLASS_FORCING Thm 3.4 (at p ≡ 1 (mod M) the criterion
fails on every ES line at levels ≤ D): no Frobenius datum compatible with p ≡ 1 (M) forces any bounded-level ES event.

### 5.4 Squares and near-squares: where joint laws beyond (L1)–(L5) do appear (PROVED; known in substance)
**Proposition 5.4.** (a) (*square law L3□*) Let m be odd with gcd(m, β_j) = 1 and L_j(m²) an odd integer. Every prime ℓ | L_j(m²)
satisfies ℓ ∤ α_jβ_jm and χ_j(ℓ) = 1. For the four ES lines χ_j is defined modulo the level t_j and is odd (χ_j(−1) = −1:
(−4d/·), (−4C/·), (−e/·) with e ≡ 3 (4) are characters of negative discriminants), so every divisor (and every ratio ab⁻¹ of
divisors) lies in ker χ_j ∌ −1: no event at that level. This is T1 (B5) in configuration language.
(b) (*near-square law*, (J)53) If p = m² + k, α_jk + β_j = c² (c ≥ 1) and gcd(m, c) = 1, then every odd prime ℓ | L_j(p) with
ℓ ∤ α_j satisfies (−α_j/ℓ) = 1, i.e. χ_j(ℓ) = (β_j/ℓ); for the (★) line (α = 4C, β = 1) χ_j(ℓ) = 1, and for p + 4d (k + 4d = c²)
every prime factor is ≡ 1 (mod 4): no event at that level.
*Proof.* (a) ℓ | α_jm² + β_j; ℓ | α_j or ℓ | m would give ℓ | β_j, contradicting gcd(α_j, β_j) = gcd(m, β_j) = 1; ℓ | β_j would give
ℓ | α_jm². So −α_jβ_j ≡ (α_jm)² (mod ℓ). (b) γ_jL_j(p) = α_jm² + c²; ℓ | m would give ℓ | c; so −α_j ≡ (c/m)² (mod ℓ). ∎
*Reading.* (a) is the law that separates odd squares from primes at a bounded set of lines: at primes the left side
(ℓ/p) of (L3) is free (JRT), at squares it is identically 1; (L1), (L4), (L5) hold verbatim at squares. That (a) is the *only*
extra law at squares would need a polynomial analogue of JRT along p = m² (Hypothesis H) — plausible, not proved here (Assessment). (b) shows that *data of p which are not Frobenius data* — here the
polynomial representation p = m² + k — can impose joint laws beyond (L1)–(L5). Both laws are subgroup restrictions
("all factors in ker χ"), which can only remove configurations. *(Assessment.)* Under Hypothesis H, if p = φ(u) is a polynomial
parametrisation and every L_j(φ(u)) is irreducible, the one-factor configuration should survive along the family, so the
criterion of Corollary F (now evaluated on the restricted classes) still decides bounded-level forcing — compare POINTWISE_SIZE
Thm C (formal odd-square principle, CONDITIONAL on H); reducible L_j∘φ is the thin-family mechanism ((J)74, (J)84 Thm A).

### 5.5 Theorem P (pointwise twisting: 2-power data never decide the class, at any number of levels; PROVED)
JRT/Corollary F vary p. This section fixes the integer and asks the information question directly: is the event at a level
a function of the *2-power profile* of the factors (everything quadratic/Rédei/spin-type about them), jointly over any —
possibly growing — family of levels?

*Setting.* Fix an odd integer n ≥ 3 (e.g. a prime p), a finite set J of lines with levels t_j and N_j := L_j(n),
gcd(N_j, t_j) = 1, G_j := (ℤ/t_j)^×. A prime ℓ is *private to j* if ℓ ∥ N_j, ℓ ∤ N_{j′} and ℓ ∤ t_{j′} for all j′ ≠ j. Choose private
primes ℓ_{j,1}, …, ℓ_{j,k_j} of N_j (any subset) and put s_j := N_j/∏_iℓ_{j,i}, g_j := ∏_iℓ_{j,i} mod t_j, Σ(s_j) ⊂ G_j the classes of
divisors of s_j. Let H_j ≤ G_j be a subgroup. An *H-profile-compatible assignment* gives each ℓ_{j,i} a class a′_{j,i} ∈ ℓ_{j,i}H_j with
∏_ia′_{j,i} = g_j (and leaves everything else unchanged).

**Theorem P.** If −1 ∉ Σ(s_j) ∪ Σ(s_j)·g_j and (2^{k_j} − 2)·|Σ(s_j)| < |H_j|, then some H-profile-compatible assignment has
−1 ∉ Σ(s_j)·Σ(a′_{j,1}, …, a′_{j,k_j}) (Σ(·) = subset products). The choices at different j are independent, so this holds
simultaneously at every j ∈ J satisfying the hypothesis, however large J is.
*Proof.* V := {(h_1, …, h_k) ∈ H^k : ∏h_i = 1} ≅ H^{k−1}; a′_i := a_ih_i. The fake subset products are a′_S = a_S·h_S (S ⊆ {1..k},
h_S := ∏_{i∈S}h_i); a′_∅ = 1 and a′_{full} = g_j are fixed and excluded by hypothesis. For ∅ ≠ S ≠ full, h ↦ h_S is a surjective
homomorphism V → H (take i ∈ S, i′ ∉ S, h_i = x, h_{i′} = x⁻¹, others 1), so the h ∈ V with −1 ∈ Σ(s_j)·a_Sh_S, i.e. h_S ∈ a_S⁻¹·(−Σ(s_j)⁻¹),
number at most |Σ(s_j)|·|V|/|H|. Summing over the 2^k − 2 subsets leaves a good h when (2^k − 2)|Σ(s_j)| < |H|. ∎

**Corollary P′ (what the fake shares with the truth).** Take H_j = G_j² (resp. H_j = the odd-order part of G_j). Every h ∈ H_j lifts
to h̃ ∈ ∏_{q|t_j}ℤ_q^× that is a square (resp. a 2^E-th power for every E): take h = x², h̃ := x̃² (resp. for odd q, the Teichmüller
part of h has odd order and its 1 + qℤ_q-part lies in a uniquely 2-divisible group; for q = 2 the odd part is trivial). Defining
the fake residue of ℓ_{j,i} modulo any m by CRT — ℓ_{j,i}·h̃ on the t_j-primary components, ℓ_{j,i} itself on the components prime to
t_j — the fake data agree with the true data on: (i) the value at every factor of every quadratic character (resp. every character
of 2-power order) of every conductor; (ii) every residue modulo moduli prime to t_j — in particular the symbols (ℓ/p)_n at n = p,
all mutual Legendre symbols (ℓ/ℓ′) and (ℓ′/ℓ) between factors (the joint Rédei matrix of all N_j; the reverse symbols via (ii)
and ℓ mod 4, which is unchanged since squares are 1 mod 4 and odd-order elements are trivial mod 4), and all data of the other
lines; (iii) the product law at every level and the smooth parts. Hence **at every level satisfying the hypothesis the event
"some divisor of N_j is ≡ −1 (mod t_j)" is not a function of these data**, jointly over all levels.
*Reading.* This is the pointwise (fixed-n, unconditional, any number of levels) version of "reciprocity forces parity, never
class": no argument whose input about the factors is their quadratic / 2-power profile (genus characters, Rédei symbols,
4-/8-ranks expressed through such symbols, spins and quartic symbols at p, governing-field Frobenii that are functions of these)
plus the product laws can decide the B2 event at a level with |G_j²| > (2^{k_j} − 2)|Σ(s_j)| (resp. |G_j,odd| > …). It cannot
fail at levels where G_j² is tiny — e.g. the exponent-2 levels t | 24 (C | 6 on the (★) line), where the class *is* its quadratic
profile; that is exactly CLASS_FORCING's X2 tier. It does not say the event is undecidable — the actual odd-part classes of the
factors decide it — only that they are the irreducible input (B2). It does not cover non-abelian Frobenius data of the factors
that are not functions of residues (cf. Remark 4.2).

## 6. Computation (EVIDENCE): does any hidden joint law show up at bounded levels?

**6.1 Free-model event test.**

`scripts/z53_genusredei_freemodel.c` (gcc -O2 -lm; ulimit -v 6000000; all runs < 30 s). Lines: A_C: N = 4Cn + 1 (t = 4C,
C ≤ 15) and B_d: N = n + 4d (t = 4d, d ≤ 15); 30 lines. B = 61 (all factors > 61 are "large"; every large prime exceeds every
level). For every n and line: factor N; event E = [−1 ∈ Σ(N) mod t]; **free model** = small part with its actual classes, large
factors' classes drawn i.i.d. from the harmonic prime weights w_t(a) = Σ_{61<ℓ≤2·10⁵, ℓ≡a(t)} 1/ℓ and conditioned *only* on the
product law (L1) (exact enumeration for k ≤ 3 large factors, 16 384-sample importance sampling for k ≥ 4); instances with a
large square factor are skipped (≤ 0.4 %). z = (O − E)/√Σ P(1 − P). Stratum tests compare the residual per instance between
complementary strata of non-abelian Frobenius data of p: p ≡ 1 vs 5 (8); 2 a quartic residue or not (p ≡ 1 (8)); p = x² + 32y²
or not (⟺ 8 | h(−4p), Barrucand–Cohn; p ≡ 1 (8)); 2 a cubic residue or not (p ≡ 1 (3)).

| run (data file) | n | per-line z (30 lines) | Σz² stratum tests (120 tests) | law checks |
|---|---|---|---|---|
| primes p ≡ 1 (4) in [10⁷, 1.2·10⁷], uniform classes (`freemodel_P_1e7_1.2e7_uniform.txt`) | 61 812 | −5.5 … +7.4 | 100.3 | 0 / 2 760 681 (L3), 0 / 1 848 806 (L2, n = 4) |
| same, harmonic classes (`…_harmonic.txt`) | 61 812 | −1.1 … +2.2 | 101.4 | same |
| primes in [10⁸, 1.04·10⁸], harmonic (`freemodel_P_1e8_1.04e8_harmonic.txt`) | 108 397 | −3.1 … +3.3 | 123.9 | 0 / 5 199 388 (L3), 0 / 3 242 096 (L2) |
| odd squares m² in [10⁶, 4·10⁸] (`freemodel_S_oddsquares_1e6_4e8.txt`) | 9 500 | O = 0 on all 30 lines; z = −22 … −80 | — | — |
| near-square primes m² + k, 0 < |k| ≤ 12, in [10⁶, 4·10⁸] (`freemodel_N_nearsquares_1e6_4e8.txt`) | 13 220 | −1.3 … −42.5 (all negative) | 1283 | 0 / 618 052 (L3) |

*Readings.* (1) The uniform model's deviations (|z| up to 7) are Chebyshev-type bias of the small large primes (61 < ℓ < 10³
dominate Σ1/ℓ); harmonic weighting removes them at 10⁷ (all |z| ≤ 2.2; Σz² over the 330 overlapping per-line strata = 343). At 10⁸
residual |z| ≤ 3.3 (Σz² = 517/330) remain, consistent with the cruder fit of fixed weights to larger N; no line stands out across
both ranges. (2) Non-abelian Frobenius data of p have no detectable effect: 120 stratum-difference tests give Σz² = 101 and 124
(χ²₁₂₀ mean 120, sd 15.5); the largest single |z| (3.74 at 10⁷, B_d=15 quartic stratum; 3.56 at 10⁸, A_C=3 x² + 32y² stratum) do
not recur in the other range. (3) Decorations behave freely: among large factors ℓ with (ℓ/p) = 1 on lines with ≥ 2 large
factors, P(ℓ is a 4th power mod p) is 0.494–0.503 on every line at 10⁸, homogeneous across the classes ℓ mod t (pooled χ² 178
on 170 dof); the mutual symbol (ℓ₁/ℓ₂) for two-factor N is +1 at rate 0.493–0.500, homogeneous across classes (χ² 0.2–32 per
line on 1–23 dof). For one-factor N the symbol is forced by (L2) (e.g. A-lines with s = 1: ℓ = N ≡ 1 (mod p) is always a 4th
power; the bracketed k = 1 rates in the data files deviate from 1/2 exactly as (L2) predicts). (4) Positive controls: the test
detects the square law L3□ (T1) at z ≈ −22 … −80 with only 9 500 squares, and the near-square laws (Prop 5.4(b)) at up to
−42σ (e.g. B_d = 3, i.e. k + 12 = □ for k = 4, −3, −8, …). So the test has power against joint laws of exactly the kind §7.6 asks
about; at primes it sees none beyond (L1) (and the Chebyshev bias). (5) Test primes (`testprimes_summary.txt`): 409, 577, 5569,
9601, 23929, 83449, 102001, 329617, 712321, 8813281 miss all 15 A-lines (C ≤ 15) and the free model gives them probability
10^{−0.07} … 10^{−0.58} of doing so — their failure is not visible at bounded levels; 193, 2521, 66529, 3361 miss all 15 B-lines, at
model probability ≈ 1 (their small parts force it: B1). Bounded-level data neither predict nor explain the test primes.
**6.2 Configuration census (EVIDENCE for JRT).** `scripts/z53_genusredei_configcensus.py 3000000`
(`configcensus_12p1_3e6.txt`): the (★) line 12p + 1 (C = 3, level 12) at primes p ≡ 1 (4), p < 3·10⁶, restricted to N = ℓ₁ℓ₂
(two distinct primes > 61, s = 1; 17 932 instances). Decorations: classes a₁, a₂ mod 12, whether ℓ₁, ℓ₂ are 4th powers mod p,
and (ℓ₁/ℓ₂). The laws predict a₂ = a₁⁻¹ = a₁, (ℓ/p) = (−3/ℓ) (L3), ζ₁ζ₂ = 1 (L2, so the two 4th-power flags agree and are 0 for
non-residues), ε free: exactly 12 law-compatible configurations. Observed: 0 law violations, exactly the 12 configurations,
with counts 1010–1188 for each of the 8 residue-class configurations (a₁ ∈ {1, 7}) and 2169–2328 for each of the 4 non-residue ones
(a₁ ∈ {5, 11}), i.e. close to equal frequency within each class type, as the free (HC-type) heuristic predicts.

**6.3 Theorem P at actual primes (CERTIFIED for the stated ranges by exhaustive search; scripts `z53_genusredei_twist.py`,
`…_twistscan.py`, `…_twistlevels.py`; data `twist_X100_1e7_1.04e7.txt`, `twist_levels_X100.txt`).** For all 12 370 primes
p ≡ 1 (4) in [10⁷, 1.04·10⁷] and the (★) levels C ≤ X = 100 (t = 4C), private primes = primes > X dividing 4Cp + 1 exactly once
(automatically private: ℓ | N_C, N_{C′} ⟹ ℓ | C − C′). Each level with the event is classified as B1 (−1 ∈ Σ(s) ∪ Σ(s)g: visible
from the X-smooth part and the product law), *protected* (a product-1 twist by squares kills the event: by Theorem P's bound, or
by exhaustive search over (G²)^{k−1} where the bound is not met), or Q (every such twist keeps the event: determined by the
quadratic profile). Result: 12 287 primes have a B1 level; of the other 83, one has no event at C ≤ 100, **23 have every event
level protected** (their (★) certificates at C ≤ 100 are invisible to all quadratic data of the factors), and 59 have a Q-level;
the 88 Q-levels sit at C = 1 (21), 2 (16), 3 (22), 6 (15) — the exponent-2 levels, 74 of 88 — and sporadically at
C ∈ {4, 5, 8, 11, 12, 14, 20, 21} (14), versus 256 protected levels spread over C = 4…100. With X = 300 (bound only, no exhaustive
search; `twist_X300_1e7_1.04e7_boundonly.txt`): 8 primes lack a B1 level, 1 has all event levels protected by the bound alone.
*Reading.* Pointwise, quadratic data decide the (★) event essentially only at the exponent-2 levels; everywhere else the odd part
of the private factors' classes is the irreducible input.

*Scope.* EVIDENCE only; finite ranges, one weighting scheme; the event model ignores sizes of divisors (irrelevant here: every
large prime exceeds every level).

## 7. What the theorem leaves open (escape hatches) and the push on them

1. **Growing families of levels at fixed p** (the B2 lottery itself). JRT/Corollary F are statements about finitely many lines;
   HC with a number of forms growing with p is meaningless. At fixed p the levels C ≤ X(p) have private large primes (SPARKS8
   Lemma 2.3), and each level separately is free; any forcing mechanism must be an *existential* statement over a growing level
   family. The only such mechanism known is the BM layer ((J)103 Prop 2.2: some level with a non-residue factor) — a parity
   statement. *Push:* is there an ∃-level statement at the next (quartic or odd) layer? Corollary 4.1 says that at each fixed
   level the quartic/odd layer is jointly free even given all decorations, so such a statement would have to come from
   counting across levels (a lower-tail statement of (★)-type), not from algebra at any level. **Assessment:** this hatch is B2.
2. **Non-Frobenius data of p.** Prop 5.4(b): representation data (p = m² + k) do impose joint laws — always subgroup restrictions,
   i.e. anti-forcing; under H with irreducible lines they leave Corollary F's criterion unchanged; reducibility is the
   thin-family mechanism, unavailable at a general prime ((J)84 Thm A). Class groups of fields depending on p and the level
   (ℚ(√−Cp), its Rédei matrix, its 4-rank) are functions of (D1)–(D3) together with Frobenius data of p in fields generated by the
   factors (Remark 4.2) — covered by the same construction modulo the abelian-part computation. Concrete class/ideal data on the
   divisor hypercube determine the divisor itself (CLASS_FORCING Cor 5.3(iii)) — factorisation data, B2.
3. **Unconditional versions.** Prop D: the exact theorem contains an open prime pair. Theorem U is the unconditional content.
   A sieve version for one line (Iwaniec semi-linear sieve) is plausible but does not reach several lines (§5.2).
4. **Spins / governing fields (B6).** Equidistribution of spins (FIMR) or of Smith/Koymans–Pagano governing data is an average
   over primes; the *pointwise* content of all such data, as far as factor classes are concerned, is exactly (L1)–(L5) (Lemma 3.1 is
   pointwise; Corollary 4.1 says nothing else is pointwise-forced). So the answer to "find what is pointwise" is: the product laws,
   one quadratic link per factor, the cross-line links, and reciprocity — nothing at the quartic or odd layer.

## 8. Verdict
**Narrowed** (with a strengthening of CLASS_FORCING §6). FRONTIER §7.6 is answered as a scoped no-go: at every finite set of
lines/levels and for every Chebotarev datum of p, the joint law of the classes of *all* prime factors, even decorated by all
n-th power symbols at p and the full joint Rédei matrix, is exactly product + parity + cross-line parity + reciprocity
(Lemma 3.1 PROVED; Theorem JRT CONDITIONAL on HC; Theorem U PROVED for partial configurations); bounded-level forcing by any such
data is exactly the B1 congruence criterion (Corollary F, CONDITIONAL on HC). What survives: (i) growing level families (= B2),
(ii) non-Frobenius representation data of p (anti-forcing only, as far as known). The unconditional exact theorem is
Dickson-hard (Prop D), so "CONDITIONAL on HC" is the honest ceiling for this kind of no-go.
What it buys: §7.6 can be removed from the open list (or demoted to "closed relative to HC"); the "class beyond parity" question
of §7.3 is shown to be jointly free at every fixed level (Corollary 4.1), so any progress on §7.3 must be a counting/lower-tail
statement across growing level families, not an algebraic law.

## 9. FRONTIER §4 hard screens (for the best idea here, "joint algebraic forcing at bounded levels")
* **T1 (squares):** passes as a diagnostic — Prop 5.4(a) isolates T1 as the single extra law at squares; the mechanism itself
  (forcing) is shown not to exist, so there is nothing that could "work at squares".
* **8/131:** not applicable to a no-go; Lemma 3.1/JRT are numerator-blind (they concern divisor events of lines), as a no-go
  should be.
* **Tied modulus:** the result is precisely that fixed (bounded) moduli carry no forced class beyond parity; the tied/moving
  modulus remains (B2).
* **Fixed p:** Lemma 3.1 is pointwise at fixed p; JRT/Theorem U are existence statements over p (Chebotarev/HC) used only as
  no-go — they do not and cannot certify a given p (B6 respected).

## 10. Review
(pending)

## 11. Proposed FRONTIER §7.6 text (do not edit FRONTIER here)
> 6. **Full-factor-multiset realisation** — *closed relative to HC* (z53, `Z53_GENUSREDEI.md`). For finitely many lines
> (the four ES lines at bounded levels, or any non-proportional linear forms) and any Frobenius datum of p in a fixed Galois
> field (governing, Rédei, Kummer, ring class fields), the decorated configuration of all large prime factors — classes mod T,
> n-th power symbols at p, the full joint Rédei matrix — obeys exactly five pointwise laws (product mod T, product of symbols,
> one parity link per factor, cross-line parity, reciprocity; PROVED), and under the Bateman–Horn–Chebotarev hypothesis HC every
> configuration obeying them occurs infinitely often (Theorem JRT, CONDITIONAL). Hence bounded-level forcing from any such data
> is exactly the B1 criterion of CLASS_FORCING Prop 3.2 (Corollary F), in every Chebotarev class (upgrading Thm 6.1).
> Unconditionally: every finite partial configuration occurs with positive density (Theorem U); the exact statement contains an
> open prime pair (Prop D). Odd squares differ from primes by exactly one extra law (T1); near-squares by representation laws
> (anti-forcing). EVIDENCE: a free model with only the product law fits bounded-level event rates of primes to 10⁸, with no
> dependence on non-abelian Frobenius data, and detects squares/near-squares at 20–80σ. What remains is growing level families,
> i.e. B2.

## 12. Bottom line
Data at a fixed prime — Frobenius in any fixed field, quartic/spin symbols of the factors at p, the joint Rédei matrix of all
factors — constrain the classes of all prime factors of p + 4d / 4Cp + 1 / the e-slice integers jointly by exactly the product law,
one quadratic link per factor, the cross-line links and reciprocity (PROVED), and nothing else at any bounded set of levels
(CONDITIONAL on HC; the unconditional exact form is as hard as cousin primes, and the unconditional partial form is PROVED).
Consequently the joint/higher-genus angle cannot force the B2 class: §7.6 closes as a scoped no-go, odd squares are separated
from primes by exactly the T1 law, and the only remaining freedom is across growing families of levels — B2 itself. ES remains open.
