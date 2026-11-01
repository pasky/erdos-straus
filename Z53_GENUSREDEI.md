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
* cp3b: a twisting statement (§5.5) and its census at actual primes (§6.3); after review it is Lemma P (formal) + Corollary P″
  (CONDITIONAL on HC).
* cp4: hostile deep review (§10): 2 FATAL, 11 MAJOR, 3 MINOR; all repaired in place (marked "(R-rev)"). The FATAL ones: (L1)
  had an illegal cancellation (fixed: the law is ∏a = g with g = L(p)/s mod T); the unconditional *arithmetic* reading of Theorem
  P was false (data at all moduli determine the prime) — P is now a formal finite-group lemma, its arithmetic realisation is
  CONDITIONAL on HC (Corollary P″).

## 1. The statement attacked (precise)

**Lines.** A *line* is L(x) = (αx + β)/γ with integers α, γ ≥ 1, β ≠ 0, gcd(α, β) = 1, together with a *level* t ≥ 3 (the
modulus of its divisor event). The four ES lines (CLASS_FORCING §1) are p + 4d (α = 1, β = 4d, γ = 1, t = 4d), 4Cp + 1
(α = 4C, β = 1, γ = 1, t = 4C; this is the (★) line), (p + e)/4 and (pe + 1)/4 (γ = 4, t = e, e ≡ 3 (mod 4)). Fix finitely many lines
L_1, …, L_r with pairwise R_{jj′} := α_{j′}β_j − α_jβ_{j′} ≠ 0 (non-proportional).

**Parameters.** n ≥ 1 (an order of power-residue symbols; n = 1 means "no symbols"). B ≥ r + 1, B ≥ n, B ≥ every prime factor of
∏_j α_jβ_jγ_j·∏_{j≠j′}R_{jj′}. T := a B-smooth modulus divisible by 4∏_{q≤B}q and by every level t_j. Ω := a finite Galois
extension of ℚ containing Ω_{B,n} := ℚ(ζ_{4n}, q^{1/n} : q ≤ B prime) (any governing field, Rédei field, Kummer field, ring class
field may be adjoined). M := a B-smooth modulus divisible by T and by the conductor of Ω^{ab} (the maximal abelian subfield),
with exponents e_q large (fixed below).

**p-datum.** Π = (σ, r): an element σ ∈ Gal(Ω/ℚ) fixing ζ_{4n}, and r ∈ (ℤ/M)^× with Art(r)|_{Ω^{ab}} = σ|_{Ω^{ab}} and (R-rev)
γ_j | α_jr + β_j for every j (γ_j | M; this makes every L_j(x), x ≡ r (M), an integer). A prime p
*has datum Π* if p ≡ r (mod M) and Frob_𝔓 = σ for some prime 𝔓 | p of Ω. Π is *admissible* if α_j r + β_j ≢ 0 (mod q^{e_q − v_q(Tγ_j)})
for all j and q ≤ B (for fixed r this holds once the e_q are large; the excluded r have Haar measure → 0 as e_q → ∞); then for x ≡ r (M) the B-smooth part s_j of L_j(x) and g_j := L_j(x)/s_j mod T are constant (CLASS_FORCING
Thm 3.4 uses the same device). For σ fixing μ_n put κ_σ(y) := σ(y^{1/n})/y^{1/n} ∈ μ_n for y ∈ ℚ^× supported on {−1} ∪ {q ≤ B}
(well defined since σ fixes μ_n; κ_σ(y) = (y/𝔭)_n at 𝔭 = 𝔓 ∩ ℚ(ζ_n)).

**Decorated configuration** of a prime p with datum Π (fix 𝔓 with Frob_𝔓 = σ, 𝔭 = 𝔓 ∩ ℚ(ζ_n)): write L_j(p) = s_j·∏_{i=1}^{k_j} ℓ_{j,i}
with primes ℓ_{j,i} > B. (R-rev) Throughout, decorated configurations are defined only for primes whose *rough parts*
L_j(p)/s_j are squarefree (so the ℓ_{j,i} are distinct and (D3) is ±1-valued); repeated large prime factors are NOT covered by
§§3–4 (they occur for infinitely many p in admissible data, e.g. 7² ∥ p + 4). For each large factor x = (j, i):
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
  datum Π. Hence the forced joint content of all-factor data (squarefree rough parts) is *exactly* (L1)–(L5).
* (PROVED, §5.1, **Theorem U**) Unconditionally, every finite *partial* configuration consistent with (L3), (L5) occurs (as
  exactly-dividing factors) for a positive density of primes with datum Π: the only laws that need the *complete* factor set
  are the product laws (L1), (L2), (L4).
* (PROVED, §5.2) The exact statement of JRT for one line and one configuration is a Hardy–Littlewood prime-pair statement, so
  JRT cannot be made unconditional without new prime-pair input.
* (CONDITIONAL on HC, §5.3, **Corollary F**) A divisor event at finitely many lines/levels is forced on a datum Π iff it is forced
  by the one-large-factor configuration — exactly the B1 criterion of CLASS_FORCING Prop 3.2. This upgrades CLASS_FORCING
  Thm 6.1 (one-sided; only data with trivial abelian shadow) to an exact criterion for every Chebotarev datum: adding Frobenius
  data of p in any fixed field to the congruence datum does not change forcing. (R-rev: prescribing decorations *of the factors*
  can change forcing — e.g. two factors with (ℓ/p) = −1 on p + 4 force the level-4 event; then Corollary 4.1's finite check over
  law-compatible configurations applies.)
* (PROVED, §5.5, **Lemma P**, formal finite-group statement) If the event holds and is not forced by the fixed part, and
  |H| > (2^k − 2)|Σ(s)| (k private factors, H = G² or the odd-order part of G), then some product-preserving twist of the private
  classes by H kills it: the images of the factor classes in G/G² (all quadratic characters of the level group), resp. in G/G_odd
  (all 2-power-order characters of the level group), plus the product law do not determine the event. (R-rev: this is a formal
  statement about classes; data of an actual prime at *all* moduli determine the prime, so no unconditional pointwise arithmetic
  non-determination is claimed.) Under HC the twisted configurations are realised by primes with the same datum and the same
  decorations (Corollary P″, CONDITIONAL). In the exact census at 12 370 primes near 10⁷, C ≤ 100 (§6.3; sample-specific), the
  quadratic images decided the (★) event mostly at the exponent-2 levels C | 6 (75 of 89 such levels). Lemma P is about unsigned
  events and its inequality is a *sufficient* condition, not a classification of levels.
* (PROVED, §5.4) At odd squares (under coprimality/parity hypotheses) an extra law (L3□) holds, which yields T1 on those lines;
  at near-squares p = m² + k representation laws appear (the (J)53 deformation). (CONDITIONAL on HC, via JRT — not a consequence
  of §5.4:) Frobenius data of p add no joint laws beyond (L1)–(L5); the extra joint laws known (squares, near-squares) come from
  data of p that are not Frobenius data and are anti-forcing.

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

**Lemma 3.1.** Let p be a prime with datum Π, p > B, p ∤ ∏β_jγ_j, with squarefree rough parts and decorated configuration as in
§1. Then:
* (L1) ∏_i a_{j,i} ≡ g_j (mod T) for each j, where g_j := (L_j(p)/s_j) mod T (constant on the datum class; R-rev: obtained by
  dividing the integer identity L_j(p) = s_j∏ℓ_{j,i} by s_j *before* reducing — s_j need not be invertible mod T);
* (L2) ∏_i ζ_{j,i} = κ_σ(β_j/(γ_j s_j)) for each j;
* (L3) if n is even: ζ_x^{n/2} = χ_j(a_x) for each large factor x of line j, where χ_j(ℓ) := (−α_jβ_j/ℓ) (Jacobi symbol in ℓ,
  a Dirichlet character of ℓ modulo 4·rad(α_jβ_j), which divides T);
* (L4) for j ≠ j′ and each large factor y of line j′: ∏_i ε((j, i), y) = ψ_{jj′}(a_y), where ψ_{jj′}(ℓ) := (R_{jj′}γ_jα_{j′}s_j/ℓ)
  (a character of ℓ modulo 4·rad(R_{jj′}γ_jα_{j′}s_j), which divides T);
* (L5) ε(x, y)ε(y, x) = (−1)^{(a_x−1)(a_y−1)/4} (computed from a_x, a_y mod 4).
*Proof.* (L1): L_j(p)/s_j = ∏ℓ_{j,i} as integers; reduce mod T. g_j is constant on p ≡ r (M): v_q(α_jp + β_j) = ν_{j,q} and
(α_jp + β_j)/q^{ν_{j,q}} mod q^{e_q − ν_{j,q}} is constant, with e_q − ν_{j,q} > v_q(Tγ_j) by admissibility.
(L2): since p ∤ γ_j, L_j(p) ≡ β_j/γ_j (mod p), so (L_j(p)/𝔭)_n = ((β_j/γ_j)/𝔭)_n; multiplicativity of the symbol gives
∏_i(ℓ_{j,i}/𝔭)_n = ((β_j/(γ_js_j))/𝔭)_n, and for y supported on {−1} ∪ {q ≤ B}, (y/𝔭)_n = κ_σ(y) because Frob_𝔓 = σ acts on y^{1/n}
by σ(y^{1/n}) ≡ (y^{1/n})^p (mod 𝔓), and dividing by y^{1/n} gives κ_σ(y) ≡ y^{(p−1)/n} (mod 𝔓) (X-rev repair). (L3): ℓ | α_jp + β_j and ℓ ∤ α_jβ_j give p ≡ −β_j/α_j (mod ℓ), so (p/ℓ) = (−α_jβ_j/ℓ) (multiply
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
there are infinitely many k ≡ k₀ (mod m) with all f_i(k) prime and Frob_{f₀(k)}|_{Ω′} ∈ C′. (R-rev: the f_i are assumed to have
positive leading coefficients; the forms used below do.)
(Ω′ = ℚ is Dickson's conjecture. HC is a standard Bateman–Horn–Chebotarev heuristic, not a published theorem.)

**Theorem JRT.** Assume HC. Let the lines, n, B, T, Ω, M and an admissible datum Π = (σ, r) be as in §1. Let Γ be a configuration
satisfying (L1)–(L5) (with s_j, g_j, κ_σ taken from Π; Γ has distinct factors, i.e. squarefree rough parts). Then there are
infinitely many primes p with datum Π whose decorated configuration is Γ; i.e. L_j(p) = s_j·∏_{i≤k_j}ℓ_{j,i} with distinct primes ℓ_{j,i} > B, ℓ_x ≡ a_x (mod T), (ℓ_x/𝔭)_n = ζ_x at a
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
(i) f_j ∈ ℤ[k]: s_jQ_jγ_j | α_jp₀ + β_j by construction (γ_j | α_jr + β_j is part of the datum), and s_jQ_jγ_j | α_jW (q-adically for q ≤ B since
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
sufficiently large prime with datum Π and squarefree rough parts iff P holds for every configuration satisfying (L1)–(L5).
In particular a divisor event is forced *given prescribed decorations* iff it holds for every law-compatible configuration
carrying those decorations (a finite check per number of factors). In particular, given *all*
decorations (D2), (D3) — all n-th power symbols of the factors at p, the full joint Rédei matrix — the classes of the large
factors are constrained by nothing except (L1), the parity links (L3)/(L4), and (L5) (fixed mutual symbols also constrain the
classes mod 4; X-rev repair): the "class beyond parity" is jointly free.
*Proof.* ⇐ by Lemma 3.1 (every realised configuration satisfies the laws); ⇒ by JRT (a configuration violating P is realised
infinitely often). ∎

**Remark 4.2 (non-abelian decorations of the factors).** Prescribing also Frob_{ℓ_x} in a fixed non-abelian Galois Ω′ works
for chosen factors (Chebotarev in Step 1) and needs, for the last factors, a version of HC with Frobenius conditions on
several values (HC⁺: Frob_{f_i(k)} ∈ C_i for all i). (R-rev) An extension would need, besides an abelian product law in
Gal(Ω′^{ab}/ℚ), the *individual* compatibility of each prescribed Frob_{ℓ_x} with ℓ_x's residue class on Ω′ ∩ ℚ^{ab} (e.g. in the
S₃ field of x³ − 2 a transposition is nontrivial on ℚ(√−3), so it is incompatible with ℓ ≡ 1 (12) — a product check misses
this); not proved here. Not needed for ES events, which depend on classes only. *(Assessment.)* Rédei symbols
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
r ≢ 0, −4 (mod 3) and (mod 5); then ν_{q} = 0 for q ≤ 5 (Π admissible) and s = 1. The one-factor configuration (k = 1) satisfies (L1)–(L5). Its realisation by infinitely many p means: infinitely many p ≡ r (mod 3600) with p and p + 4 both
prime — which implies the (open) infinitude of cousin primes. Hence JRT, even for one line and one configuration, implies an
open Hardy–Littlewood pair statement; an unconditional proof would need new prime-pair input.
*Proof.* Realisation means L(p) = s·ℓ with ℓ prime, s = 1. ∎
*(Assessment.)* For a *single* line and a datum that is a congruence class, unconditional infinitude of *some* event-avoiding
configuration (e.g. "all prime factors of p + 4 are ≡ 1 (4)", which kills the d = 1 event) is plausibly within reach of
Iwaniec's semi-linear sieve (primes of the form φ(x, y) + A, Acta Arith. 21 (1972)) — not verified here; for several lines at
once the sieve dimension grows and this route looks closed (Assessment, not a proved impossibility). Corollary F below is
therefore stated relative to HC.

### 5.3 Corollary F (exact bounded-level forcing criterion; CONDITIONAL on HC)
For each line j let E_j be its divisor event at level t_j (some divisor of L_j(p) is ≡ −1 (mod t_j); or the signed
e-slice version −1 ∈ Σ^±). For an admissible datum Π, the disjunction ⋁_j E_j holds for all sufficiently large primes with
datum Π iff for some j:  −1 ∈ Σ(s_j) ∪ Σ(s_j)·g_j  (signed: −1 ∈ Σ^±(s_j)·{1, g_j, g_j⁻¹}), where Σ(s_j) is the set of classes mod t_j
of divisors of s_j. In particular, the answer depends only on p mod M (B1), and no additional Frobenius datum of p (any governing
field, Rédei field, Kummer field) changes it. (R-rev: this concerns conditioning on Π alone; conditioning additionally on
decorations of the factors is handled by Corollary 4.1 and can change forcing.)
*Proof.* ⇐: a divisor of s_j, possibly times L_j(p)/s_j (whose class is g_j), lies in the class −1. ⇒: the configuration with
k_j = 1 for every j, a_{j,1} = g_j, ζ_{j,1} := κ_σ(β_j/(γ_js_j)) and the forced mutual symbols satisfies (L1), (L2), (L4), (L5)
by construction (mutual symbols ε((j,1),(j′,1)) := ψ_{jj′}(g_{j′})); (L3) and (L5) hold because they hold for the integers
N_j := L_j(p)/s_j of any prime p with datum Π (such p exist by Chebotarev): N_j ≡ g_j (mod T) is odd, positive, a product of primes
> B, and the N_j are pairwise coprime (privacy). Hence, for n even, χ_j(g_j) = ∏_{ℓ^e∥N_j}χ_j(ℓ)^e = ∏_{ℓ^e∥N_j}(ℓ/p)^e = (N_j/p) =
((β_j/(γ_js_j))/p) = ζ_{j,1}^{n/2} ((L3)'s computation for each ℓ, which needs no squarefreeness; N_j ≡ β_j/(γ_js_j) mod p), and the
Jacobi symbols satisfy (N_j/N_{j′}) = ∏_{ℓ′^e∥N_{j′}}ψ_{jj′}(ℓ′)^e = ψ_{jj′}(g_{j′}) ((L4)'s computation for each ℓ′), so Jacobi reciprocity
for N_j, N_{j′} is exactly (L5) for the prescribed symbols. (R-rev: multiplicities added.) By JRT the configuration is realised by
infinitely many p, at which L_j(p) = s_j·ℓ_j and Σ(L_j(p)) = Σ(s_j) ∪ Σ(s_j)·g_j. ∎
*Reading.* This is CLASS_FORCING Prop 3.2 (forced criterion, "L prime is compatible") promoted from abstract integers to
values at primes, uniformly over every Chebotarev datum, and simultaneously for all lines. It removes Thm 6.1's restriction
C|_{Ω₀} = 1 and turns its one-sided statement into an iff. Combined with CLASS_FORCING Thm 3.4 (at p ≡ 1 (mod M) the criterion
fails on every ES line at levels ≤ D): no Frobenius datum compatible with p ≡ 1 (M) forces any bounded-level ES event.

### 5.4 Squares and near-squares: where joint laws beyond (L1)–(L5) do appear (PROVED; known in substance)
**Proposition 5.4.** (a) (*square law L3□*) Let m be odd with gcd(m, β_j) = 1 and L_j(m²) an odd integer. Every prime ℓ | L_j(m²)
satisfies ℓ ∤ α_jβ_jm and χ_j(ℓ) = 1. For the four ES lines χ_j is defined modulo the level t_j and is odd (χ_j(−1) = −1:
(−4d/·), (−4C/·), (−e/·) with e ≡ 3 (4) are characters of negative discriminants), so every divisor (and every ratio ab⁻¹ of
divisors) lies in ker χ_j ∌ −1: no event at that level. This is T1 (B5) in configuration language, *under the stated
hypotheses* (R-rev: they are genuine restrictions — e.g. for e ≡ 7 (8) the e-slice value (m² + e)/4 is even; the full T1 needs
the Kronecker symbol at 2 and non-unit cases, not treated here).
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

### 5.5 Lemma P (formal twisting) and Corollary P″ (its realisation under HC)
*(R-rev: this section replaces an earlier "Theorem P / Corollary P′" whose unconditional arithmetic reading was false: residues
of an actual prime modulo all moduli prime to t — or the values of all quadratic characters of all conductors — determine the
prime itself, so no "fake" assignment is arithmetic at a fixed integer. What survives is a formal statement about classes in the
level group, plus its realisation by varying p under HC.)*

*Setting.* G := (ℤ/t)^× for a level t; a fixed part with divisor-class set Σ(s) ⊂ G; k ≥ 2 private classes a_1, …, a_k ∈ G with
product g. H ≤ G a subgroup. An *H-twist* is (a_ih_i) with h_i ∈ H and ∏h_i = 1 (same images in G/H, same product).

**Lemma P (PROVED, finite groups; unsigned event −1 ∈ Σ only — the signed e-slice event −1 ∈ Σ^± is not treated).** If −1 ∉ Σ(s) ∪ Σ(s)·g and (2^k − 2)·|Σ(s)| < |H|, some H-twist satisfies
−1 ∉ Σ(s)·Σ(a_1h_1, …, a_kh_k) (Σ(·) = subset products). Consequently, if the untwisted configuration has the event (−1 ∈ Σ(s)·Σ(a))
then the event is not a function of (Σ(s), g, the images of the a_i in G/H).
*Proof.* V := {(h_i) ∈ H^k : ∏h_i = 1} ≅ H^{k−1}. Fake subset products are a_Sh_S, h_S := ∏_{i∈S}h_i; S = ∅ and S = full give 1 and g,
excluded by hypothesis. For ∅ ≠ S ≠ full, h ↦ h_S is a surjective homomorphism V → H (i ∈ S, i′ ∉ S, h_i = x, h_{i′} = x⁻¹), so
{h ∈ V : −1 ∈ Σ(s)a_Sh_S} = {h : h_S ∈ a_S⁻¹·(−Σ(s)⁻¹)} has at most |Σ(s)|·|V|/|H| elements. Summing over the 2^k − 2 subsets leaves
a good h. The second sentence: the twisted and untwisted configurations share (Σ(s), g, images mod H) and differ in the event. ∎
*Which data are "images mod H".* H = G²: the images in G/G² are exactly the values of all quadratic characters of G (the genus-type
characters of the level, e.g. χ_{−4}, (·/q) for q | t). H = G_odd (odd-order part; note G_odd ⊆ G²): the images in G/G_odd are the
values of all characters of G of 2-power order. (R-rev: the earlier text conflated these; with H = G² only *quadratic* characters
of G are preserved. Example: p = 1901, C = 8, t = 32, N = 60833 = 127·479, G a 2-group, so G_odd = 1 and the 2-power profile
determines the classes and the event, although |G²| = 4 > (2² − 2)·1.)

**Corollary P″ (CONDITIONAL on HC).** Fix lines, n, B, T, Ω, M and an admissible datum Π as in §1, and a level t_j | T of line j.
Let p be a prime with datum Π and squarefree rough parts whose line j has the event, is not forced by s_j (−1 ∉ Σ(s_j) ∪ Σ(s_j)g_j),
and satisfies (2^{k_j} − 2)|Σ(s_j)| < |G_{t_j}²|. Then there are infinitely many primes with the same datum Π, the same
decorations ζ_x, ε(x, y), the same classes on every line ≠ j, and on line j classes with the same images in G_{t_j}/G_{t_j}² and
the same product, at which the line-j event fails.
*Proof.* Take the H-twist of Lemma P (H = G_{t_j}², lifted to (ℤ/T)^× by acting only on the t_j-primary components — the lift of
h = x² is x̃² for any lift x̃, and lifts may be chosen with product 1 by taking the last as the inverse product of the others).
The twisted configuration satisfies (L1) (product unchanged), (L2) (symbols unchanged), (L3), (L4) (χ_j and ψ_{jj′} are quadratic
characters mod T, unchanged by square twists), (L5) (squares are ≡ 1 mod 4 when 4 | t_j; when t_j is odd the 2-component is not
touched). Apply JRT. ∎
*Reading.* At a level with large G², knowing the genus-type (quadratic) characters of every factor at that level, all symbols at
p and the whole joint Rédei matrix, plus the datum of p, does not determine the event — CONDITIONAL on HC, realised by actual
primes. It is the joint, all-factor version of CLASS_FORCING Prop 4.2 / bsB_redei_oddpart ("2-power objects see only the
2-primary component"), with an explicit size condition. It says nothing about a single fixed p (where the factors are what they
are), and it cannot hold where G² is tiny — e.g. the exponent-2 levels t | 24 (C | 6 on the (★) line), where the class *is* its
quadratic image (CLASS_FORCING's X2 tier).

## 6. Computation (EVIDENCE): does any hidden joint law show up at bounded levels?

**6.1 Free-model event test.**

`scripts/z53_genusredei_freemodel.c` (gcc -O2 -lm; ulimit -v 6000000; all runs < 30 s). Lines: A_C: N = 4Cn + 1 (t = 4C,
C ≤ 15) and B_d: N = n + 4d (t = 4d, d ≤ 15); 30 lines. B = 61 (all factors > 61 are "large"; every large prime exceeds every
level). For every n and line: factor N; event E = [−1 ∈ Σ(N) mod t]; **free model** = small part with its actual classes, large
factors' classes drawn i.i.d. from the harmonic prime weights w_t(a) = Σ_{61<ℓ≤2·10⁵, ℓ≡a(t)} 1/ℓ and conditioned *only* on the
product law (L1) (exact enumeration for k ≤ 3 large factors, 16 384-sample importance sampling for k ≥ 4, cached per key).
(R-rev) Exclusions: instances with a large square factor are skipped (≤ 0.4 % in the prime runs, but up to 12.7 % on some lines of
the near-square run, e.g. 1682/13220 on B_2), and for composite n instances with gcd(N, t) > 1 are skipped (in the square run up
to 46.65 % on B_15, which keeps 5056 of 9500); per-line counts N are in the data files; the controls are filtered samples. z = (O − E)/√Σ P(1 − P). Stratum tests compare the residual per instance between
complementary strata of non-abelian Frobenius data of p: p ≡ 1 vs 5 (8); 2 a quartic residue or not (p ≡ 1 (8)); p = x² + 32y²
or not (⟺ 8 | h(−4p), Barrucand–Cohn; p ≡ 1 (8)); 2 a cubic residue or not (p ≡ 1 (3)).

| run (data file) | n | per-line z (30 lines) | Σz² stratum tests (120 tests) | law checks |
|---|---|---|---|---|
| primes p ≡ 1 (4) in [10⁷, 1.2·10⁷], uniform classes (`freemodel_P_1e7_1.2e7_uniform.txt`) | 61 812 | −5.5 … +7.4 | 100.3 | 0 / 2 760 681 (L3), 0 / 1 848 806 (L2, n = 4) |
| same, harmonic classes (`…_harmonic.txt`) | 61 812 | −1.1 … +2.2 | 101.4 | same |
| primes in [10⁸, 1.04·10⁸], harmonic (`freemodel_P_1e8_1.04e8_harmonic.txt`) | 108 397 | −3.1 … +3.3 | 123.9 | 0 / 5 199 388 (L3), 0 / 3 242 096 (L2) |
| odd squares m² in [10⁶, 4·10⁸] (`freemodel_S_oddsquares_1e6_4e8.txt`) | 9 500 | O = 0 on all 30 lines; z = −22 … −80 | — | — |
| near-square primes m² + k, 0 < |k| ≤ 12, in [10⁶, 4·10⁸] (`freemodel_N_nearsquares_1e6_4e8.txt`) | 13 220 | −1.3 … −42.5 (all negative) | 1283 | 0 / 618 052 (L3) |

*Readings* (R-rev: the z's and Σz² below are descriptive residual diagnostics — the 120 contrasts share primes, strata overlap,
and the model probabilities carry importance-sampling error — not calibrated joint significance tests). (1) The uniform model's deviations (|z| up to 7) are Chebyshev-type bias of the small large primes (61 < ℓ < 10³
dominate Σ1/ℓ); harmonic weighting removes them at 10⁷ (all |z| ≤ 2.2; Σz² over the 330 overlapping per-line strata = 343). At 10⁸
residual |z| ≤ 3.3 (Σz² = 517/330) remain, consistent with the cruder fit of fixed weights to larger N; no line stands out across
both ranges. (2) Non-abelian Frobenius data of p show no clear effect in these diagnostics: the 120 stratum-difference contrasts give
Σz² = 101.4 and 123.9 (harmonic runs; for independent contrasts the mean would be 120); the largest single |z| (3.79 at 10⁷,
B_d=15 quartic stratum; 3.56 at 10⁸, A_C=3 x² + 32y² stratum) do not recur in the other range. (3) Decorations behave freely: among large factors ℓ with (ℓ/p) = 1 on lines with ≥ 2 large
factors, P(ℓ is a 4th power mod p) is 0.4971–0.5024 (pooled per line) at 10⁸, homogeneous across the classes ℓ mod t (sum of the
per-line homogeneity χ² 157.6 on 160 dof at 10⁸, 178.0 on 160 at 10⁷; observations within one N are linked by (L2), so again
descriptive); the mutual symbol (ℓ₁/ℓ₂) for two-factor N is +1 at rate 0.493–0.500, homogeneous across classes (χ² 0.2–32 per
line on 1–23 dof). For one-factor N the symbol is forced by (L2) (e.g. A-lines with s = 1: ℓ = N ≡ 1 (mod p) is always a 4th
power; the bracketed k = 1 rates in the data files deviate from 1/2 exactly as (L2) predicts). (4) Positive controls: the test
detects the square law L3□ (T1) at z ≈ −22 … −80 with only 9 500 squares, and the near-square laws (Prop 5.4(b)) at up to
−42σ (e.g. B_d = 3, i.e. k + 12 = □ for k = 4, −3, −8, …). So the test has power against joint laws of exactly the kind §7.6 asks
about; at primes it shows none beyond (L1) (and the Chebyshev bias). (5) Test primes (`testprimes_summary.txt`): 409, 577, 5569,
9601, 23929, 83449, 102001, 329617, 712321, 8813281 miss all 15 A-lines (C ≤ 15) and the free model gives them probability
10^{0} (409: forced by the small parts) … 10^{−0.58} of doing so — their failure is not anomalous at bounded levels; 193, 2521,
3361 miss all 15 B-lines with model probability 1 (forced by small parts: B1) and 66529 with model probability 0.91 (the d = 13
line has model event probability 0.086). Bounded-level data neither predict nor explain the test primes.
**6.2 Configuration census (EVIDENCE for JRT).** `scripts/z53_genusredei_configcensus.py 3000000`
(`configcensus_12p1_3e6.txt`): the (★) line 12p + 1 (C = 3, level 12) at primes p ≡ 1 (4), p < 3·10⁶, restricted to N = ℓ₁ℓ₂
(two distinct primes > 61, s = 1; 17 932 instances). Decorations: classes a₁, a₂ mod 12, whether ℓ₁, ℓ₂ are 4th powers mod p,
and (ℓ₁/ℓ₂). The laws predict a₂ = a₁⁻¹ = a₁, (ℓ/p) = (−3/ℓ) (L3), ζ₁ζ₂ = 1 (L2, so the two 4th-power flags agree and are 0 for
non-residues), ε free: exactly 12 law-compatible *projected* configurations (the boolean 4th-power flag merges the two non-residue symbols ±i,
so this is not a census of full D2 configurations; X-rev). Observed: 0 law violations, exactly the 12 projected configurations,
with counts 1010–1225 for each of the 8 residue-class configurations (a₁ ∈ {1, 7}) and 2169–2328 for each of the 4 non-residue ones
(a₁ ∈ {5, 11}), i.e. close to equal frequency within each class type, as the free (HC-type) heuristic predicts.

**6.3 Lemma P at actual configurations (exact computation, one engine; independently re-run by the reviewer for the X = 100
scan; scripts `z53_genusredei_twist.py`, `…_twistscan.py`, `…_twistlevels.py`; data `twist_X100_1e7_1.04e7.txt`,
`twist_levels_X100.txt`).** For all 12 370 primes p ≡ 1 (4) in [10⁷, 1.04·10⁷] and the (★) levels C ≤ X = 100 (t = 4C): private
primes = primes > X dividing 4Cp + 1 exactly once (ℓ | N_C, N_{C′} ⟹ ℓ | C − C′ < X). Each level with the event is classified
(R-rev: categories corrected) as **B1** (−1 ∈ Σ(s₀) ∪ Σ(s₀)g₀ with s₀ the genuine X-smooth part: visible from congruence data),
**R** (not B1, but decided by the fixed part including repeated large primes q^e, q > X, e ≥ 2), **protected** (not B1/R; some
product-1 twist of the private classes by squares kills the event — Lemma P's bound, or exhaustive search over (G²)^{k−1}), or
**Q** (every such twist keeps the event: the event is a function of the quadratic images in G/G²). Result: 12 286 primes have a
B1 level; of the other 84, one has no event at C ≤ 100, 23 have every event level protected, and 60 have a Q-level; the 89
Q-levels sit at C = 1 (22), 2 (16), 3 (22), 6 (15) — the exponent-2 levels, 75 of 89 — and sporadically at C ∈ {4, 5, 8, 11, 12,
14, 20, 21} (14); there are 258 protected levels spread over C = 4 … 98 and one R level (p = 10 310 329, C = 5:
20p + 1 = 3·7·113²·769, certificate 3·113).
*Reading.* Formal (Lemma P) and, via Corollary P″, CONDITIONAL on HC: at the levels C ≤ 100 of these primes, the quadratic images
of the factor classes decided the (★) event mostly at the exponent-2 levels (75 of 89 Q-levels; sample-specific); at the
protected levels information beyond the quadratic quotient G/G² — higher 2-primary or odd-order information — is necessary.
(X-rev repair: the earlier "the odd-order part is the irreducible input" was false — at p = 1901, t = 32, N = 127·479, the classes
(31, 31) have the event, the product-preserving square twist by (9, 25) gives (23, 7) without it, and G is a 2-group.) This is not an unconditional statement about the given primes (their factors are what
they are), only about what the quadratic profile at the level can see.

*Scope.* EVIDENCE only; finite ranges, one weighting scheme; the event model ignores sizes of divisors (irrelevant here: every
large prime exceeds every level).

## 7. What the theorems leave open (escape hatches) and the push on them

1. **Growing families of levels at fixed p** (the B2 lottery itself). JRT/Corollary F concern a fixed finite family of lines;
   HC with a number of forms growing with p is meaningless. At fixed p the levels C ≤ X(p) have private large primes (SPARKS8
   Lemma 2.3); any forcing mechanism must be an *existential* statement over a growing level family. The only such mechanism
   known is the BM layer ((J)103 Prop 2.2: some level with a non-residue factor) — a parity statement. *Push:* is there an
   ∃-level statement at the next (quartic or odd) layer? Corollary 4.1 says that at each fixed finite family the quartic/odd layer
   is jointly free even given all decorations, and Lemma P / Corollary P″ quantify, level by level, that quadratic images of the
   level group cannot decide the event once |G²| > (2^k − 2)|Σ(s)| (CONDITIONAL on HC for the realisation). So such a statement
   *(Assessment, not a theorem)* plausibly have to come from counting across levels (a lower-tail statement of (★)-type) rather
   than from algebra at a fixed family of levels; JRT does not exclude algebraic growing-family mechanisms. (R-rev: the earlier claim that this hatch is closed "pointwise and unconditionally" is withdrawn — at a fixed p the data
   determine the factors.) **Assessment:** what remains of this hatch is the counting (lower-tail) form of B2.
2. **Non-Frobenius data of p.** Prop 5.4(b): representation data (p = m² + k) do impose joint laws — subgroup restrictions, i.e.
   anti-forcing; whether they leave Corollary F's criterion unchanged along a polynomial family is a Hypothesis-H question
   (Assessment, §5.4); reducibility is the thin-family mechanism, unavailable at a general prime ((J)84 Thm A). Class groups of
   fields depending on p and the level (ℚ(√−Cp), its Rédei matrix, its 4-rank) involve Frobenius data of p in fields generated by
   the factors; the JRT construction can accommodate such fields for the *chosen* factors, but the abelian-part computation of
   Step 3(b) would have to be redone for each (Remark 4.2) — not done. Concrete class/ideal data on the divisor hypercube
   determine the divisor itself (CLASS_FORCING Cor 5.3(iii)) — factorisation data, B2.
3. **Unconditional versions.** Prop D: the exact theorem implies an open prime-pair statement. Theorem U and Lemma 3.1 are the
   unconditional content. A sieve version for one line (Iwaniec's semi-linear sieve) is plausible but not verified, and looks out
   of reach for several lines (Assessment).
4. **Spins / governing fields (B6).** Equidistribution of spins (FIMR) or of Smith/Koymans–Pagano governing data is an average
   over primes. For the decorations treated here — Frobenius of p in any fixed Galois field, n-th power symbols of the factors at
   p, mutual Legendre symbols — the pointwise identities are exactly (L1)–(L5) (Lemma 3.1), and nothing else is forced
   (Corollary 4.1, CONDITIONAL on HC). (R-rev: this is not claimed for every governing-field datum of p-dependent fields; see 2.)

## 8. Verdict
**Narrowed**, with a strengthening of CLASS_FORCING §6. FRONTIER §7.6 is answered as a scoped no-go *relative to HC*: for every
fixed finite set of lines/levels and every Frobenius datum of p in a fixed Galois field, the joint law of the classes of all
large prime factors (squarefree rough parts), even decorated by all n-th power symbols at p and the full joint Rédei matrix, is
exactly product + symbol product + parity + cross-line parity + reciprocity (Lemma 3.1 PROVED; Theorem JRT CONDITIONAL on HC;
Theorem U PROVED for partial configurations); bounded-level forcing from a Frobenius datum of p is exactly the B1 congruence
criterion (Corollary F, CONDITIONAL on HC), in every Chebotarev class. Lemma P (PROVED, formal) and Corollary P″ (CONDITIONAL)
give a sufficient condition (|G²| > (2^k − 2)|Σ(s)|, depending on k and Σ(s)) under which quadratic images of the level group do
not decide the (unsigned) event; in the §6.3 sample the quadratically decided levels were mostly t | 24 (EVIDENCE, sample-specific).
Scope (X-rev): this is a no-go for forcing from the datum Π alone; prescribed decorations of the factors *can* force the event
(p = 73: p + 4 = 7·11, both (ℓ/73) = −1, so (L3) forces both factors ≡ 3 (4) although B1 fails) — Corollary 4.1's finite check
applies then.
The unconditional exact theorem implies an open prime-pair statement (Prop D), so "CONDITIONAL on HC" is the honest ceiling
for this kind of no-go. What survives: (i) growing level families (B2; whether only counting arguments can work there is an
Assessment, not proved), (ii) non-Frobenius data of p
(representation data: anti-forcing as far as known; p-dependent class-group data: not treated), (iii) repeated large prime
factors (outside the squarefree domain of JRT).
*What it buys:* §7.6 can be demoted to "closed relative to HC for fixed finite families" (not removed); the "class beyond parity"
question of §7.3 is jointly free at every fixed finite family of levels (Corollary 4.1, CONDITIONAL on HC, squarefree rough
parts), so progress on §7.3 cannot come from an algebraic law of the datum at bounded levels; *(Assessment)* a counting/lower-tail
statement across growing level families is the natural remaining direction.

## 9. FRONTIER §4 hard screens (for the best idea here, "joint algebraic forcing at bounded levels")
* **T1 (squares):** used as a diagnostic — Prop 5.4(a) exhibits the extra law at squares (under its hypotheses) that the free
  test detects at 20–80σ; the forcing mechanism itself is shown not to exist at bounded levels (relative to HC).
* **8/131:** not applicable to a no-go; Lemma 3.1/JRT concern divisor events of lines and are numerator-blind, as a no-go may be.
* **Tied modulus:** the result is that fixed (bounded) moduli carry no forced class beyond parity (relative to HC); the
  tied/moving modulus remains (B2).
* **Fixed p:** Lemma 3.1 is pointwise at fixed p; JRT/Theorem U/Corollary P″ are existence statements over p (Chebotarev/HC) used
  only as no-go — they do not and cannot certify a given p (B6 respected); no pointwise non-determination at a fixed p is claimed.

## 10. Review
Hostile deep-mode reviewer subagent (full report `data/z53/genusredei/review_hostile.md`): **2 FATAL,
11 MAJOR, 3 MINOR**, all repaired in place (marks "(R-rev)"):
* FATAL 1 — (L1) cancelled the non-invertible s_j mod T (counterexample p + 4, s = 5, a = 49 satisfied the old laws but is never
  realised). Fixed: (L1) is ∏a = g := L(p)/s mod T; JRT Step 5 already used this form.
* FATAL 2 — the unconditional arithmetic reading of "Theorem P / Corollary P′" was false (all-moduli data determine the prime).
  Replaced by Lemma P (formal) + Corollary P″ (CONDITIONAL on HC); all summaries (§§1, 7, 8, 11, 12) revised.
* MAJOR — G² vs 2-power characters conflated (counterexample t = 32); "bad assignment exists" ≠ "not determined" (needs the
  event at the true configuration); integrality of (p + 1)/3-type lines (datum now requires γ_j | α_jr + β_j); repeated large
  prime factors (domain restricted to squarefree rough parts); Corollary F's decoration claim (removed; Corollary 4.1 handles
  decorations); Remark 4.2 compatibility; overclaims about squares' "exactly one extra law", governing fields and closure of §7.6
  (scoped); §6.3 "B1" included repeated large primes (genuine X-smooth B1 now computed: 84 not 83 exceptional primes, new R
  category); control-sample exclusions (now stated); χ² calibration (now descriptive).
* MINOR — multiplicities in Corollary F's Jacobi products; Prop 5.4(a) hypotheses scoped; numbers corrected (3.79, 0.4971–0.5024,
  157.6/160 and 178.0/160, 1010–1225, test-prime ranges incl. 409 = forced and 66529 = 0.91); HC positivity; Prop D phrased as an
  implication.
The reviewer re-ran all free-model runs, the test-prime summary, the configuration census and the twist scans and found the raw
outputs reproduced; after the (L1)/integrality/squarefree repairs it found no further defect in JRT Steps 1–5, Theorem U, the
union bound of Lemma P, or Prop 5.4 under its hypotheses. **Cross-model review** (`data/z53/xreview/REVIEW_GENUSREDEI.md`): ACCEPT-WITH-FIXES. Independently re-derived JRT Steps 1–5,
Theorem U, Prop D, Corollary F, Prop 5.4, Lemma P and Corollary P″ (all CORRECT, conditional ones as conditional); reproduced
all free-model runs, the configuration census and the twist scans byte-for-byte. Required fixes applied (marked "X-rev"): the
§6.3 odd-part conflation (false; counterexample p = 1901, t = 32); the Π-only vs decoration-conditioned forcing distinction and the
squarefree domain carried into §§8, 11, 12; sufficient bounds and sample statistics no longer read as classifications; the
growing-family "counting only" claim labelled Assessment; the §1 bullet's HC-dependence made explicit; L2 Frobenius formula;
(L5) kept in Corollary 4.1; "projected" configurations in §6.2; Lemma P scoped to unsigned events; the generated stratum-sum line
no longer says "chi2 … under H0".

## 11. Proposed FRONTIER §7.6 text (do not edit FRONTIER here)
> 6. **Full-factor-multiset realisation** — *closed relative to HC for fixed finite families of levels* (z53,
> `Z53_GENUSREDEI.md`). For finitely many lines (the four ES lines at bounded levels, or any non-proportional integral linear
> forms) and any Frobenius datum of p in a fixed Galois field, the decorated configuration of the large prime factors (squarefree
> rough parts) — classes mod T, n-th power symbols at p, the joint Rédei matrix of all factors — obeys five pointwise laws
> (product of classes, product of symbols, one parity link per factor, cross-line parity, reciprocity; PROVED), and under the
> Bateman–Horn–Chebotarev hypothesis HC every configuration obeying them occurs for infinitely many p (Theorem JRT,
> CONDITIONAL). Hence bounded-level forcing from a Frobenius datum of p is exactly the B1 criterion of CLASS_FORCING Prop 3.2
> (Corollary F), in every Chebotarev class (upgrading Thm 6.1). Unconditionally, every finite partial configuration occurs with
> positive density (Theorem U); the exact statement implies an open prime-pair statement (Prop D). A formal twisting lemma
> (Lemma P, unsigned events) plus JRT give a sufficient condition (|G²| > (2^k − 2)|Σ(s)|) under which quadratic images of the
> level group do not decide the event (in a sample, quadratically decided levels were mostly t | 24). This is a no-go for forcing
> from the datum of p alone: prescribed factor decorations can force the event (e.g. p = 73, p + 4 = 7·11).
> Odd squares carry an extra law (T1, under coprimality hypotheses), near-squares representation laws (anti-forcing).
> EVIDENCE: a free model with only the product law fits bounded-level event rates of primes to 10⁸ with no clear dependence on
> non-abelian Frobenius data, and detects squares/near-squares at 20–80σ. Open: growing level families (B2), p-dependent
> class-group data, repeated large factors.

## 12. Bottom line
For any fixed finite family of lines/levels, data at p of Frobenius type — Frobenius in any fixed field — together with the
quartic/spin-type symbols of the factors at p and the joint Rédei matrix of all factors, constrain the classes of all prime
factors of p + 4d / 4Cp + 1 / the e-slice integers jointly by exactly the product laws, one quadratic link per factor, the
cross-line links and reciprocity (PROVED), and by nothing else (CONDITIONAL on HC; the unconditional exact form implies an open
prime-pair statement, the unconditional partial form is PROVED), all for primes whose rough parts are squarefree. Consequently
Frobenius-type data of p cannot force the B2 class at bounded levels: §7.6 closes relative to HC as a scoped no-go —
bounded-level forcing from the datum of p alone is exactly B1 in every Chebotarev class (prescribed decorations of the factors
can force the event, e.g. p = 73, and are then a finite check, Corollary 4.1) — odd squares carry the extra T1 law, and the
remaining freedom is across growing families of levels — B2 itself (whether only counting arguments can work there is an
Assessment). ES
remains open.
