# EXSET_SIEVE_MASS — large sieve / larger sieve / Linnik duality: the mass question and the square floor

*Wave z50, lane (B), slug `lsmass`. Brief: `/home/pasky/projects/math/z50briefs/b_opus_lsmass.md`. ES is OPEN; nothing
here claims it proved or disproved. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z50_lsmass_*`, data `data/z50_lsmass/`.*

## 0. Summary table (filled in as sections land)

| # | claim | label | review verdict |
|---|---|---|---|
| 1 | audit: which barrier, which door | — | — |
| 2 | mass/Rankin criterion for prime-local families | (pending) | (pending) |
| 3 | nearly-prime-local families (one large prime) | (pending) | (pending) |
| 4 | Linnik duality: free character data | (pending) | (pending) |
| 5 | square floor via (inverse) large sieve | (pending) | (pending) |
| 6 | exact remaining gap | (pending) | — |

## 1. Audit

### 1.1 The families

Write S := 4ℤ ∪ (8ℤ + 7). A *word* of n is (t, u, v) ∈ ℕ³ with n = tuv − u − v; then n + u = v(tu − 1) and
n + v = u(tv − 1).

**Lemma 1.1 (PROVED, one line).** Every n ≡ 5 (mod 8) with n > 5 satisfies U. *Proof.* c = 3; the endpoint v = 3 has
n + 3 ≡ 0 (mod 8) and A = 8 ≡ −1 (mod 3), 1 < 8 < n + 3. ∎ Hence E_U := {n ≡ 1 (4) : U(n) fails} ⊂ {5} ∪ {n ≡ 1 (8)},
consistent with the z49 census (all six non-square failures are ≡ 1 mod 8). From now on U is studied on n ≡ 1 (mod 8),
where c = 7 and the U-endpoints are exactly the elements of S.

**Definition 1.2 (word classes).** Two kinds of congruence class carry a whole word:
* **W1** (pivot M = tu − 1 ≥ 2): n ≡ −u (mod M), u | M + 1. Every n ≥ M in it has the word (t, u, (n+u)/M). A
  *refined* W1 class also fixes v = (n+u)/M modulo 8 (a class mod 8M).
* **W2** (pivot uv): n ≡ −(u+v) (mod uv). Every n ≥ uv in it has the word ((n+u+v)/(uv), u, v). A refined W2 class
  also fixes t modulo 4 (a class mod 4uv).

The **U-family** 𝔘 is the set of refined W1/W2 classes, intersected with n ≡ 1 (mod 8), whose word has an endpoint in S
(this includes u = 1 words, as in `scripts/z49_main_ucensus_brute.py`). The **ES₅-family** 𝔉₅ is the set of refined
W1/W2 classes (with n ≡ 1 mod 4) whose word has a slot t, u, v, tu−1, tv−1 ≡ 0 (mod 4). Every member above the class's
threshold satisfies U, resp. has a certificate word (and so satisfies ES₅ when it is a prime; Theorem A). The (★) line
(4 | t) and López's b = 1 line are subfamilies of 𝔉₅. Multiplicities: at most 8τ(M + 1) refined W1 classes per
pivot M, at most 4τ(m) refined W2 classes per pivot m.

**No unit squares (PROVED; CERTIFIED for small moduli).** No class of 𝔘 or 𝔉₅ contains a unit square modulo its
modulus. If c ≡ x² (mod G) with gcd(x, G) = 1, CRT gives an odd m ≡ x (mod G) as large as we like, and m² lies in the
class above its threshold. For 𝔘 this contradicts Theorem E (at an odd square no vertex of S is non-isolated). For 𝔉₅
it contradicts Theorem A, since (uv/m²) = +1 when gcd(uv, m) = 1. `scripts/z50_lsmass_profile.py` confirms this by
brute force for all 525 U-classes of pivot ≤ 200 and every refined ES₅ W1 class of pivot ≤ 200 (0 exceptions;
`data/z50_lsmass/profile.json`). Control: the same test finds a unit square in 251 of 956 unrestricted W1 classes. This is the KARY2 square base (K2 Lemma 2.3) for these families.

### 1.2 Are U and ES₅ subfamilies of the ES forced mixture? (the audit requested in z50 CONTEXT §3)

**Proposition 1.3 (PROVED, elementary).**
(a) A W1 class with u ∈ 4ℤ (pivot M ≡ 3 mod 4) is literally the ℛ(M)-class −4D, D = u/4 | A_M = (M+1)/4.
(b) The (★)/4 | t class −u (mod M), M = 4Cu − 1, is literally the ℛ(M)-class −4D with D = Cu² | A_M² = C²u².
(c) The W1 class certifying an endpoint v ≡ 7 (mod 8) with 4 | tv − 1 =: 4m is n ≡ −v (mod 4m) with v | 4m + 1. It
    lies in the Case-A class −m′⁻¹ (mod 4rh), with m = rh² (r squarefree) and m′ = (4m + 1)/v. It equals that class iff
    h = 1, i.e. iff m is squarefree.
(d) The W2 class with u = 4d is −(4d + v) (mod 4dv). It lies in the (a, D)-class −(4D + a) (mod 4a·g(D)), with
    a = v and D = d. It equals that class iff d is squarefree.

*Proof.* (a) −u = −4(u/4). (b) −4Cu² = −u(4Cu) = −u(M + 1) ≡ −u (mod M). (c) v·m′ = 4m + 1 ≡ 1 (mod 4rh), so
−v ≡ −m′⁻¹ there. (d) g(d) | d. ∎

(At n ≡ 1 (mod 8) an endpoint v ≡ 7 (mod 8) forces u(tv − 1) ≡ 0 (mod 8), so 4 | u or 4 | tv − 1. Hence (a)–(d) cover
every U-certificate up to the choice of pivot.)

**Reading (Assessment).** A method whose classes are of shapes (a)–(d) has its avoider set containing the avoider set of
a KARY mixture, so (D)17–(D)29 apply to it a fortiori: its saving is at most C(log N)^{3/4}. The pivots chosen
*differently* do not literally fall under (D)24. An example is the W1 class n ≡ −u (mod 4M) that certifies 4 | v. So the
CONTEXT's "a fortiori" is correct for the natural U/ES₅ classes, but it is neither literal for all of 𝔘 nor sharp.
Theorem 3.2 below replaces it by a cap that is literal for all of 𝔘 and 𝔉₅, and stronger: (log N)^{2/3}.

### 1.3 Which barrier, which door

**Assessment.** This lane escapes no barrier. Its outputs are of three kinds. First, sharper barrier theorems for exactly
the families the z50 targets name (U, ES₅): §3, the exact CRT exponent 2/3. Second, a placement theorem: Linnik/dual
large sieves lie inside (D)25 (§4). Third, verification or refutation of the orchestrator notes §4(a) and §4(c) (§§2, 5).
§7 lists the doors that remain open for U, stated precisely.

### 1.4 Literature (checked 2026-10-29, web search)

No exceptional-set result for ES after Pomerance–Weingartner (arXiv:2511.16817) was found. The only 2025–26 hits were
claimed proofs already audited in `LITERATURE_2026.md`: Dyachenko arXiv:2511.07465 ("conditional in nature" by its own
§11), and Mballa arXiv:2602.20036 (parametric families of density one, no rate). Nothing was found on U or ES₅
exceptional sets, or on a sieve-limit theorem for growing-dimension prime-local families of this kind. The PYY/BGP
k-wise literature cited in DISCOVERIES (D)9/(D)17 is the relevant prior art for §2.

## 2. Work item 1 — when does a sieve get exp(−mass)?

Setting: a *prime-slice system* (EXCEPTIONAL_THETA §1, "THETA"). It has a small modulus Q₀, admissible residues
R ⊂ ℤ/Q₀, and for each slice prime ℓ a set of ω(ℓ) forbidden classes, p_ℓ = ω(ℓ)/ℓ ≤ 1/4. Put

  mass*(y) = −Σ_{ℓ≤y} log(1 − p_ℓ),   Λ(y) = Σ_{ℓ≤y} p_ℓ log ℓ,   V(y) = Σ_{ℓ≤y} p_ℓ log²ℓ.

Λ(y) is the mean log-modulus of the Euler product ∏_{ℓ≤y}(1 + h_ℓ), h_ℓ = p_ℓ/(1 − p_ℓ). Equivalently it is
κ(y)·log y, with κ(y) the sieve dimension at y. *Saving* means log(N / bound).

**Lemma 2.1 (tilted Chebyshev; PROVED, elementary, standard).** If Λ(y) + √(2V(y)) ≤ log Q, then Montgomery's
L(Q) = Σ_{q≤Q} μ²(q)∏_{ℓ|q} h_ℓ satisfies L(Q) ≥ ½·exp(mass*(y)). Hence the large sieve bound (N + Q²)/L(Q), and
likewise Selberg's Λ² bound with G(√D), saves at least mass*(y) − log 4 at Q = √N.

*Proof.* Σ_{q | P_y} h(q) = ∏_{ℓ≤y}(1 + h_ℓ) = e^{mass*(y)}. Normalised, q is a product of independent factors: ℓ | q
with probability h_ℓ/(1 + h_ℓ) = p_ℓ. Then E log q = Λ(y) and Var log q ≤ V(y), so Chebyshev gives
P(log q > log Q) ≤ 1/2. ∎

**Theorem 2.2 (the mass criterion; PROVED: (a) is Lemma 2.1, (b) is THETA Thm 2.5 / Remark 2.6, and (c) is arithmetic
on (a)–(b)).** Let S(λ) be the best saving of a level-λ method. This covers nonnegative CRT majorants of level λ
(Selberg, Bonferroni, β/Rosser, CRT-evaluated moments) and Montgomery's large sieve with Q = e^{λ/2}. For coefficient-sum
methods, λ ≍ log N by THETA Lemma 2.9.
(a) S(λ) ≥ max{mass*(y) : Λ(y) + √(2V(y)) ≤ λ/2} − log 4.
(b) For every α > 0, S(λ) ≤ log(Q₀/|R|) + 19αλ + C₄ Σ_ℓ p̄_ℓ ℓ^{−α} + O(log²λ).
(c) Three regimes follow.
   (i) *Fixed dimension* κ (p_ℓ ≈ κ/ℓ): S(λ) = κ log λ + O_κ(1). This is the full Euler mass up to e^{cλ/κ}, so the sieve
       gets exp(−mass) up to a constant factor (the classical Γ(κ+1)e^{γκ} loss).
   (ii) *Log-growing dimension* (p_ℓ ≍ a log ℓ/ℓ, so mass(y) ≍ a log y and κ(y) ≍ (a/2)log y):
       (1 − o(1))√(aλ) ≤ S(λ) ≤ C√(aλ). The available mass up to e^{λ} is ≍ aλ, so the sieve gets only its square root.
   (iii) *Single band* (all p_ℓ on (e^{λ/2}, e^{λ}], total mass μ): S(λ) ≤ 38 log(2 + μ) + C. Only one prime per term
       fits, and the bound is ≈ 1/μ, not e^{−μ}.
   In words: a sieve of level λ collects exp(−mass(y)) exactly up to the y at which *(dimension at y) × (log y)*, the
   log of the typical Euler-product modulus, reaches λ. Beyond that it collects only the Rankin functional
   Ψ(λ) = inf_α[αλ + Σ p_ℓ ℓ^{−α}].

*Proof of (c).* (i) Take α = 1/λ in (b): Σ (κ/ℓ)ℓ^{−1/λ} = κ log λ + O(κ). In (a), Λ(y) + √(2V) = (κ + √κ)log y + O(1),
so mass*(y) = κ log log y + O_κ(1) with log y ≍ λ/κ. (ii) Σ a log ℓ·ℓ^{−1−α} ≤ C a/α. Optimising 19αλ + Ca/α gives
C′√(aλ). In (a), Λ(y) = (a/2 + o(1))log²y and √(2V) = O((log y)^{3/2}), so log y = (1 − o(1))√(λ/a) and
mass* = (1 − o(1))√(aλ). (iii) α = (2/λ)log(2 + μ) gives 38 log(2 + μ) + C₄μ/(2 + μ). ∎

Novelty: none claimed for the criterion as such. (a) is textbook, (b) is THETA's, and (c) is bookkeeping. It is
recorded because the brief asks for the criterion in exactly this form, and because §3 uses it.

**Proposition 2.3 (the prime-local U family; PROVED relative to Bombieri–Vinogradov and Brun–Titchmarsh).** Work in
the fibre n ≡ 1 (mod 8). Let ω_U(ℓ) be the number of distinct residues −u (mod ℓ), u | ℓ + 1, such that the word has an
endpoint in S (u ∈ S, or v ≡ (1+u)ℓ⁻¹ (mod 8) ∈ S). Then c₁ log y ≤ mass_U(y) ≤ c₂ log y. So regime (ii) holds: every
level-λ method that uses only prime-modulus U classes saves ≍ √λ ≍ √(log N), and Montgomery's
L(Q) = exp(Θ(√(log Q))). *This confirms orchestrator note §4(a)*, and the same holds verbatim for ES₅'s and I3's
prime-local classes (I3_DEEP_ASTRA Lemma 3.2).

*Proof.* Upper: ω_U(ℓ) ≤ τ(ℓ + 1), and Σ_{x<ℓ≤2x} τ(ℓ + 1) ≪ x by divisor pairing and Brun–Titchmarsh. Lower: keep
u ∈ 4ℤ with u ≤ x^{1/4}. These are U-endpoints for every ℓ ≡ −1 (mod u), and Bombieri–Vinogradov counts those primes
exactly as in I3_DEEP_ASTRA Lemma 3.2. Then Theorem 2.2(c)(ii). ∎

**Numerics (CERTIFIED counts, EVIDENCE for trends; `scripts/z50_lsmass_primelocal.py`,
`data/z50_lsmass/primelocal.json`).**
* Profile: the mean of ω_U(ℓ)/log ℓ over ℓ ≤ 10⁶ is 1.07. mass_U(10^k) = 1.02, 3.08, 5.36, 7.73, 10.15, 12.61 for
  k = 1…6, i.e. a log y + b with a ≈ 1.07, b ≈ −2. Λ(y)/log²y → 0.51 ≈ a/2.
* Exact Montgomery L(Q) against the full Euler mass:

  | Q | log L(Q) | Rankin upper inf_σ[σ log Q + Σ log(1 + h ℓ^{−σ})] | full mass*(Q) |
  |---:|---:|---:|---:|
  | 10² | 1.98 | 3.07 | 3.47 |
  | 10⁴ | 3.52 | 5.10 | 8.16 |
  | 10⁶ | 4.75 | 6.55 | 13.05 |
  | 1.78·10⁶ | 4.89 | 6.71 | 13.67 |

  log L grows like √(log Q); the Rankin–saddle gap 1.8 matches the Gaussian correction log(σ√(2πΦ″(σ))) ≈ 1.9. The full
  mass grows linearly in log Q.
* Sieve bound against true counts. Here N = 10⁸, the fibre n ≡ 1 (8) has M = 1.25·10⁷ integers, and the large sieve
  uses Q = √M with moduli built from primes ≤ z:

  | z | true #avoiders | Haar M·∏(1 − ω/ℓ) | Montgomery (M + Q²)/L | true E_U in fibre |
  |---:|---:|---:|---:|---:|
  | 10 | 3 571 429 | 3 571 429 | 7 141 779 | |
  | 100 | 388 829 | 388 122 | 1 539 169 | |
  | 1000 | 43 891 | 38 282 | 1 075 062 | |
  | 10⁴ = √N | 10 254 | 3 574 | 1 014 684 | 5 005 |

  The true sifted count follows the Haar product (exp(−mass)) until z ≈ 300. After that it stays above the 5 000
  squares, which avoid every class. The large sieve saves log(M/1.01·10⁶) = 2.5, while the true saving is 7.1.
* **Remark (Assessment).** a ≈ 1.07 > 1 means the Haar density of the prime-local family alone at z = √N is
  ≈ N^{−a/2}, *below* the square density N^{−1/2}. The model mass of this thin family already "reaches" the square floor;
  it is the Rankin truncation, not the supply, that limits the sieve to exp(O(√log N)).
* Toy families (`scripts/z50_lsmass_toys.py`, `data/z50_lsmass/toys*.json`; random residues, so the Haar model is
  exact) show the three regimes. Deficit = full mass − log L(Q), at Q = 10³…10⁷: fixed κ = 1: 0.32→0.46
  (→ γ = 0.577); κ = 2: 0.79→1.30 (→ log 2 + 2γ ≈ 1.85); log-growing a = 1: 2.5→9.3; a = 2: 5.0→20.3 (linear in log Q).
  Single band, ρ = 0.03 (mass 13.5): the true saving is 13.9, but Montgomery saves only 2.0 ≈ log(1 + μ) − log 2.

## 3. Work item 2 — nearly prime-local families

(pending)

## 4. Work item 3 — Linnik duality

(pending)

## 5. Work item 4 — the square floor

(pending)

## 6. Hostile reviews

(pending)

## 7. Remaining gap

(pending)
