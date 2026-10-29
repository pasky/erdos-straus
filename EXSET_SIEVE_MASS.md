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
it contradicts Theorem A, since (uv/m²) = +1 when gcd(uv, m) = 1. Coprimality (review R1): for W1, gcd(u, M) = 1, so
we may also take m coprime to u; then Mv = m² + u forces gcd(v, m) = 1. For W2, uv | G, so a unit square already
gives gcd(m, uv) = 1. A W2 class with gcd(u, v) > 1 contains no unit at all. Bookkeeping: intersecting a refined W2 class
(mod 4uv) with n ≡ 1 (mod 8) may need modulus 8uv; this only changes the multiplicity constants. `scripts/z50_lsmass_profile.py` confirms this by
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
(b) For every α > 0, S(λ) ≤ log(Q₀/|R|) + 19αλ + C₄ Σ_ℓ p̄_ℓ ℓ^{−α} + E(λ), where E(λ) is THETA's explicit remainder
    (the last two terms of THETA (2.4)). It is O(log²λ) when the truncated mass is μ̄_λ ≤ λ^{O(1)} and s_* ≫ 1.
(b′) (visible-mass bound) S(λ) ≤ log(Q₀/|R|) + mass*(e^λ). *Proof.* A level-λ majorant ν does not depend on n mod ℓ
    for slice primes ℓ > e^λ. Every residue vector avoiding the classes at ℓ ≤ e^λ extends to a point of 𝒜, because
    each p_ℓ < 1 and the slices are independent. So ν ≥ 1 on that event, which has probability
    (|R|/Q₀)e^{−mass*(e^λ)}. ∎
(c) Regimes. Assume the stated cumulative asymptotics for the slice primes ≤ e^λ.
   (i) *Fixed dimension* κ (Σ_{ℓ≤y} p_ℓ log ℓ = κ log y + O(1) and mass*(y) = κ log log y + O(1)):
       S(λ) = κ log λ + O_κ(1). This is the full Euler mass up to e^{λ}, so the sieve gets exp(−mass) up to a
       constant factor (the classical Γ(κ+1)e^{γκ}-type loss).
   (ii) *Log-growing dimension* (mass(y) = a log y + o(log y) and Λ(y) = (a/2 + o(1))log²y, a fixed; then
       κ(y) ∼ (a/2)log y): (1 − o(1))√(aλ) ≤ S(λ) ≤ C√(aλ). The available mass up to e^{λ} is ≍ aλ, so the sieve
       gets only its square root. Under mere comparability p_ℓ ≍ log ℓ/ℓ, only S(λ) = Θ(√λ) is claimed.
   (iii) *Single band* of total mass μ. Band (e^{λ/4}, e^{λ/2}] (two band primes fit in a term, three do not):
       log(1 + μ) − O(1) ≤ S(λ) ≤ 38 log(2 + μ) + C. Here Montgomery/Selberg at Q = e^{λ/2} see each band prime singly,
       L(Q) = 1 + Σ g_ℓ, and the bound is ≈ 1/μ, not e^{−μ}. Band (e^{λ/2}, e^{λ}]: a level-λ majorant is *linear* in the
       hit indicators. Nonnegativity then forces Eν ≥ 1 − max p_ℓ ≥ 3/4, so S(λ) ≤ log(4/3), and L(e^{λ/2}) = 1. Above
       e^{λ}: invisible, S = 0.
   In words: a sieve of level λ collects exp(−mass(y)) exactly up to the y at which *(dimension at y) × (log y)*, the
   log of the typical Euler-product modulus, reaches λ. Beyond that it collects only the Rankin functional
   Ψ(λ) = inf_α[αλ + Σ p_ℓ ℓ^{−α}].

*Proof of (c).* (i) The upper bound is (b′). For the lower bound, in (a) Λ(y) + √(2V) = (κ + √κ)log y + O(1), so
mass*(y) = κ log log y + O_κ(1) with log y ≍ λ/κ. (ii) Σ a log ℓ·ℓ^{−1−α} ≤ C a/α, and μ̄_λ ≪ λ, so E(λ) = O(log²λ).
Optimising 19αλ + Ca/α gives C′√(aλ). In (a), Λ(y) = (a/2 + o(1))log²y and √(2V) = O((log y)^{3/2}), so
log y = (1 − o(1))√(λ/a) and mass* = (1 − o(1))√(aλ). (iii) Quadratic band: the upper bound takes α = (4/λ)log(2 + μ)
in (b). For the lower bound, L(e^{λ/2}) = 1 + Σ_ℓ p_ℓ/(1 − p_ℓ) ≥ 1 + μ. Linear band: after conditioning on the
indicators, ν = c₀ + Σ_ℓ a_ℓx_ℓ with c₀ = ν(0) ≥ 1, and ν ≥ 0 at every 0/1 point forces Σ_ℓ a_ℓ⁻ ≤ c₀. So
Eν = c₀ + Σ a_ℓp_ℓ ≥ c₀(1 − max p_ℓ). ∎

Novelty: none claimed for the criterion as such. (a) is textbook, (b) is THETA's, and (c) is bookkeeping. It is
recorded because the brief asks for the criterion in exactly this form, and because §3 uses it.

**Proposition 2.3 (the prime-local U family; PROVED relative to Bombieri–Vinogradov and Brun–Titchmarsh).** Work in
the fibre n ≡ 1 (mod 8). Let ω_U(ℓ) be the number of distinct residues −u (mod ℓ), u | ℓ + 1, such that the word has an
endpoint in S (u ∈ S, or v ≡ (1+u)ℓ⁻¹ (mod 8) ∈ S). Then c₁ log y ≤ mass_U(y) ≤ c₂ log y and Λ_U(y) ≍ log²y (cumulatively; not
pointwise in ℓ). So, by (a), (b) and partial summation, the *best* saving of a level-λ method that uses only
prime-modulus U classes is Θ(√λ) = Θ(√(log N)), and Montgomery's L(Q) = exp(Θ(√(log Q))). *This confirms orchestrator note §4(a)*, and the same holds verbatim for ES₅'s and I3's
prime-local classes (I3_DEEP_ASTRA Lemma 3.2).

*Proof.* Upper: ω_U(ℓ) ≤ τ(ℓ + 1), and Σ_{x<ℓ≤2x} τ(ℓ + 1) ≪ x by divisor pairing and Brun–Titchmarsh. Lower: keep
u ∈ 4ℤ with u ≤ x^{1/4}. These are U-endpoints for every ℓ ≡ −1 (mod u), and Bombieri–Vinogradov counts those primes
exactly as in I3_DEEP_ASTRA Lemma 3.2. Then use Theorem 2.2(a), (b) with the cumulative bounds. ∎

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
  Single band in (N^{1/4}, N^{1/2}] (the quadratic band of (c)(iii) at λ = log N), ρ = 0.03 (mass 13.5): the true
  saving is 13.9, but Montgomery saves only 2.0 ≈ log(1 + μ) − log 2.

## 3. Work item 2 — nearly prime-local families, and the exact CRT exponent of U and ES₅

### 3.1 How much mass, at what log-level (the question of the brief)

The cost of a class in a CRT majorant is the log of its modulus. Every prime above the fixed W is charged, as in KARY2.
So the relevant profile is the **smooth first moment**

  𝔐_𝔊(y) := Σ_{C ∈ 𝔊, W < P(G(C)) ≤ y} Γ(G)/G,

where Γ is the KARY2 inflation weight: Γ(m) = Π_{p|m} γ′(p), with γ′(p) ≤ 8 for p ≤ W and
γ′(ℓ) = (1 − ℓ^{−1/2})^{−1} for ℓ > W. If 𝔐(y) ≍ (log y)^B, the KARY balance gives the cap λ^{B/(B+1)}. B = 3 for the
ES forced mixture gives 3/4.

**Proposition 3.1 (mass per log-level of U and ES₅; PROVED, elementary plus Shiu).**
(a) *Per unit of log-level.* The classes of 𝔘 ∪ 𝔉₅ whose pivot lies in (Q, eQ] have total Haar mass O(log Q), and
    ≫ log Q (keep the W1 labels u = 4d, M = 4dt − 1). The
    prime-pivot classes there have mass O(1). So no subfamily carries mass ≫ log Q per unit of log-level. Over all pivots
    up to Q the mass is ≍ (log Q)².
(b) *Smooth first moment.* 𝔐_{𝔘∪𝔉₅∪selectors}(y) ≤ K(W)(log y)²(log log y)².
(c) *Nearly prime-local subfamilies.* Take classes whose pivot is kℓ, with ℓ the largest prime and smooth part k.
    If k ≤ K₀ is bounded, the profile is Σ_ℓ p̄_ℓ ℓ^{−α} ≪ (log 2K₀)/α. This is regime (ii) of Theorem 2.2, and the cap
    is C√((log 2K₀)λ). If k ≤ ℓ^{C} with fixed C < 1 (a dominant prime), the profile is ≪ α^{−2}, and THETA Thm 2.7 gives the cap
    Cλ^{2/3}. For C ≥ 1, use Theorem 3.2 instead. The multiplier k is exactly what raises B from 1 to 2. Nothing raises it to 3: a third free divisor
    parameter is what U and ES₅ lack, and the full ES family has it (the 3/4 note's ratio labels −u/v, 4uv | kℓ + 1).

*Proof.* (a) A pivot M carries ≤ 8τ(M+1) refined W1 classes of modulus ≥ M, and a pivot m carries ≤ 4τ(m) refined W2
classes. The ordinary means Σ_{Q<M≤eQ} τ(M+1) and Σ_{Q<m≤eQ} τ(m) are ≪ Q log Q. A prime pivot ℓ has ≤ 8τ(ℓ+1) classes,
and Σ_{Q<ℓ≤eQ} τ(ℓ+1)/ℓ ≪ 1 by Brun–Titchmarsh (Prop 2.3).
(b) Classes with pivot M have Γ(G)/G ≤ 8Γ(M)/M and P(G) = P(M) (as y ≥ 2). For W1 we must bound
Σ_{P(M)≤y} τ(M+1)Γ(M)/M; we follow K2 Lemma 3.2 with τ(M+1) in place of τ(A_M²).
  * *Ordinary mean.* Write Γ = 1 ∗ h, with h(p) ≤ 7 for p ≤ W and h(p) ≤ 2p^{−1/2} for p > W. For e ≤ x^{1/2}, Shiu
    (τ in the class 1 mod e) gives Σ_{m≤x/e} τ(em + 1) ≪ (x/φ(e))log x. The terms e > x^{1/2} contribute O(x^{3/4+ε}).
    Σ_e h(e)/φ(e) < ∞, so Σ_{M≤x} τ(M+1)Γ(M) ≪_W x log x, and partial summation gives Σ_{M≤X} τ(M+1)Γ(M)/M ≪ (log X)².
  * *Body.* Take M ≤ X := y^{u₀} with u₀ = 8 log log y, and drop smoothness: the body is ≪ 64(log y)²(log log y)².
  * *Tail.* Split into dyadic blocks (K, 2K] with u = log K/log y ≥ u₀ and use Cauchy–Schwarz. The factor
    (Σ_{P(M)≤y, M∼K} Γ(M)²/M)^{1/2} is ≤ Ce^{−u/2}(log y)^{1/2} (K2 Lemma 3.1, κ = 1). The factor
    (Σ_{M∼K} τ(M+1)²/M)^{1/2} is ≪ (u log y)^{3/2}. Summing over blocks (u-spacing log 2/log y) gives
    ≪ (log y)³u₀^{3/2}e^{−u₀/2} = O((log log y)^{3/2}/log y) = o(1). (Review R1 corrected u₀ = 6 log log y, which
    leaves a divergent (log log y)^{3/2}.) For e > x^{1/2} in the ordinary mean use h(e) ≪_{W,ε} e^{−1/2+ε}.
  For W2, Γ is submultiplicative, so the classes contribute ≤ 32(Σ_{P(m)≤y} Γ(m)/m)² ≪ (log y)² (K2 Lemma 3.1,
  κ = 1). Selectors contribute log log y + O(1) (K2 Lemma 3.3′).
(c) Use THETA's profile p̄_ℓ ≤ Σ_{k} μ(kℓ)(kℓ/φ(kℓ))/(kℓ). Bounded k gives p̄_ℓ ≪ log(2K₀)·τ(ℓ+1)/ℓ (on average), hence
α^{−1}. For k ≤ ℓ^C, Σ_{k≤ℓ^C} τ(kℓ+1)/k ≪ (log ℓ)² on average over ℓ, by Brun–Titchmarsh over ℓ for fixed k (as in
I3_DEEP_ASTRA Lemma 8.7), hence α^{−2}. Then apply THETA Thm 2.5 and 2.7. ∎

*Numerics (EVIDENCE; `scripts/z50_lsmass_smooth.py`, `data/z50_lsmass/smooth.json`, moduli truncated at 10⁷).* These
are local log-log slopes of the smooth first moments in log y. W1 core Σ τ(M+1)/M: 1.86, 1.75, 1.83 at y = 30, 100,
300. W2 core: 1.94, 1.65, 1.48. ES ℛ(M) core Σ τ(A_M²)/M: 3.22, 2.94, 2.86. All slopes are depressed by the truncation at
larger y. The untruncated W1 mass Σ_{M≤X} τ(M+1)/M equals (0.60–0.75)(log X)² for X = 10²…3·10⁵
(`data/z50_lsmass/profile.json`). These are consistent with B = 2 for U/ES₅ and B = 3 for ES.

### 3.2 The cap

**Theorem 3.2 (the 2/3 cap for U and ES₅; PROVED given the KARY/KARY2 framework as reviewed — the same proviso as
KARY3 — and Shiu's theorem).** There are absolute W, C and λ₀ such that the following holds. Let 𝔊 be any finite family
of classes from 𝔘 ∪ 𝔉₅, together with any selector classes 0 (mod p) and any of the classes n ≢ 1 (mod 8). The
moduli are arbitrary: balanced, prime powers, any number of large primes. Let ν = Σ a_i 1[n ≡ b_i (mod d_i)] be ≥ 0 on
ℤ and ≥ 1 on the whole avoider set 𝒜(𝔊), with Σ_{ℓ | d_i, ℓ > W} log ℓ ≤ λ for every i. Then, for λ ≥ λ₀,

    log(1/Eν) ≤ C λ^{2/3} (log λ)^{2/3}.

*Proof.* Run EK Theorem 4.1 (the weighted abstract sequential sieve limit) as in the proof of K2 Theorem 5.1. Only
the four inputs below depend on the family.
1. *Base.* Use the square base R_W^□ (K2 Lemma 2.3). Every W-smooth class of 𝔊 contains no unit square: §1.1 for
   𝔘 ∪ 𝔉₅, and trivially for selectors and for n ≢ 1 (8). Hence (R1) holds, (R2) holds, and the R-term is ≤ 2W.
2. *First moment.* Proposition 3.1(b): 𝔐(y) ≤ K(log y)²(log log y)².
3. *Second moment and leak.* We need K2 Lemma 4.2 (cofactor sums) for the two new shapes. K2 Lemma 4.1 (the reduction
   to Σ_{P(q)<ℓ} μ_{ℓ,v}(q)²τ(q)Γ(q)/q) is arithmetic-free.
   * *W1.* The top prime ℓ of a modulus is the top prime of its pivot M = q′ℓ^v, where q′ is q up to a factor of 8,
     and μ_{ℓ,v}(q) ≤ C·max τ(q′ℓ^v + 1). The ℛ(M) case of K2 Lemma 4.2 goes through verbatim with F = τ⁴ (F(p) = 16)
     in place of τ(·²)⁴ (F(p) = 81). Long blocks K ≥ 4ℓ^{v/3}: Cauchy–Schwarz, Rankin for the smooth factor, and Shiu
     for τ⁴ in the class 1 mod ℓ^v, whose modulus is below the 3/4-power of the interval length. Short blocks: the
     pointwise divisor bound gives ℓ^{κv}. Result: ≤ C(v+1)^c[(log ℓ)^c + ℓ^{κv}].
   * *W2.* μ_{ℓ,v}(q) ≤ C(v+1)τ(q), so the sum is ≤ C(v+1)²Σ_{P(q)<ℓ} τ(q)³Γ(q)/q ≪ (v+1)²(log ℓ)^{c} (K2 Lemma 3.1).
     This is the (a,D) case of K2 Lemma 4.2, verbatim.
   * *Selectors.* As in K2.
   Then K2 Lemma 4.3 gives E p_ℓ² ≤ C(W)ℓ^{−7/4}(log ℓ)^c, and leak 𝔏 ≤ 1/2 for W ≥ W₀. Every class is decided at its
   top prime.
4. *Assembly.* Use singletons W < ℓ ≤ e^{s₁} with s₁ = λ^{1/3}(log λ)^{−2/3}; sequential blocks
   V_i = (e^{2^i s₁}, e^{2^{i+1}s₁}] truncated at e^{λ/2}; a linear block (e^{λ/2}, e^λ]; and zero-cost sequential
   singleton steps above e^λ. Those primes are invisible to ν, but their classes are still processed, so that the
   avoidance and leak argument covers them.
   * Singletons cost ≤ (8/3)𝔐(e^{s₁}) ≤ Cs₁²(log λ)² = Cλ^{2/3}(log λ)^{2/3}.
   * Block V_i (s = 2^i s₁, d_i = ⌊λ/s⌋): EK Cor 2.6 gives E Φ_i ≤ d_i log(C₀(E M_{V_i} + 4d_i)/d_i) + O(d_i). Here
     E M_{V_i} ≤ 𝔐(e^{2s}) ≤ 4Ks²(log λ)², so (E M + 4d)/d ≤ 8K·8^i + 4 because s₁³(log λ)² = λ. Hence
     E Φ_i ≤ (λ/(2^i s₁))(c₁ + i log 8) + O(log λ), and Σ_i ≤ Cλ/s₁ + O(log²λ).
   * The linear block costs 2 log(1 + 3e^{−λ/4}) (ETw Cor 4.3).
   * Total: log(1/Eν) ≤ 2W + log 2 + Cλ^{2/3}(log λ)^{2/3}. ∎

**Remark 3.3 (removing the log).** The (log log y)² in Prop 3.1(b) is K2's Rankin loss. KARY3's local-moment device
(KARY3 §2) removes it. The sibling lane z50-i3ex (`EXSET_I3.md` Lemma 3.3, on its branch) carries out exactly this
computation for Σ_{P(m)≤y} τ(m+1)Γ(m)/m. With it the cap is Cλ^{2/3}. We do not need this, and do not claim it here.

**Corollary 3.4 (PROVED, same proviso).** Let all primes of the family be ≤ N^A.
(a) *Coefficient-sum CRT methods* (Bonferroni, Selberg Λ², β/Rosser, CRT-evaluated moments) with bound
    N·Eν + Σ|a_i| < N save ≤ C_A(log N)^{2/3}(log log N)^{2/3}. Use K2 Cor 6.1's projection and two-case argument:
    the coarsened level is λ ≤ (A+1)log N + S with S = log(1/Eν), not the realised saving s ≤ S. Then
    S ≤ log 2 + C((A+1)log N + S)^{2/3}(log ·)^{2/3} forces S ≪ (log N)^{2/3}(log log N)^{2/3}.
(b) *CRT-admissible large sieves* (Montgomery, Montgomery–Vaughan, any Farey frequencies, fibrewise) at polynomial
    frequency level obey the same bound, with the full hypotheses of LS Thm 3.1 retained. This is LS Thm 2.1: the bound is ≥ N·E|g*|², with |g*|² a level-2λ_Φ majorant.
(c) *Every periodic Bessel / hybrid system* of LS2 Thm 2.4 (additive, multiplicative, Gauss-sum or Kloosterman rows,
    periodic twists, fibrewise mixtures) with row periods ≤ N^A obeys the same bound. LS2's full hypotheses are retained:
    CRT-admissibility, Q₀ ≤ min(N^A, N/2), and λ(Q₀) charged. LS2 Lemma 1.1 is pure LP duality
    and holds with any cap S(λ), here S(λ) = Cλ^{2/3}(log λ)^{2/3}. Its §2 proof uses nothing else. §4 shows that
    Linnik's dual sieve is such a system.

### 3.3 The cap is attained: the exact CRT exponent of U and ES₅ is 2/3

**Theorem 3.5 (PROVED relative to Bombieri–Vinogradov, Brun–Titchmarsh and Mertens, by I3_DEEP_ASTRA §8.7–8.8 with
one restriction; no new method).**
(a) #{p ≤ N : ES₅(p) fails} ≤ #{p ≤ N : U(p) fails} ≪ N exp(−c(log N)^{2/3}).
(b) The same bound holds for #{n ≤ N : (n, P_y) = 1, U(n) fails} with y = B₀(log N)^{2/3}.
(c) E_U(N) ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3}).

*Proof.* Use I3_DEEP_ASTRA Lemma 8.7 and Theorem 8.8 (with its prime/rough-input refinement), with the atoms (k, q, u)
restricted to **u ≡ 0 (mod 4)** and odd multipliers k.
* The atom event n ≡ −u (mod kq) gives the word ((kq+1)/u, u, (n+u)/(kq)). Its endpoint u lies in 4ℤ ⊂ S, so it is a
  U-certificate, and 4 | u is directly an ES₅ slot. The other endpoint is ≥ 2 for n ≥ 3KX.
* The restriction changes only constants in (8.11). Since u | kq + 1 forces gcd(u, k) = 1, the multipliers are odd, and
  h(B ∩ odd) ≍ h(B) for the two choices actually used (B = [1, K], and B = the y-rough multipliers). It is false for
  arbitrary B, e.g. B = {1} ∪ 2ℤ. The elementary progression sums Σ_{U₀<u≤z, u≡0 (4), u≡−c (k)} 1/u are Λ/(4k) + O(U₀^{−1}). Primes
  q ≡ −k⁻¹ (mod u) are counted by BV at moduli u ≤ x^{1/6}, as there. Distinctness, conditional independence and the
  coefficient ledger are unchanged.
* For (a): p ≡ 5 (mod 8) satisfies U (Lemma 1.1) and ES₅ (endpoint 3 ≡ −p mod 8, Theorem B), and a prime p > y is
  y-rough.
* *Architecture (for Cor 3.6).* The majorant is ν(n) = 1[n ≡ 1 (8)]·1[(n, P_y) = 1]·Q_r(H(n)), with r even and H the atom
  count. It is ≥ 0 on all of ℤ and ≥ 1 on the whole avoider set of (atoms ∪ selectors ∪ {n ≢ 1 (8)}). Every atom
  intersected with the fibre is a refined W1 class of 𝔘. Its level is ≪ r log(KX) + log P_y = O(T³), and its
  coefficient sum is exp(O(T³)). The conditioning on n mod L_B is an analysis device only; it is not expanded. ∎

**Corollary 3.6 (the exact CRT exponent; PROVED as the conjunction of Theorems 3.2 and 3.5).** *Within the architectures
of Corollary 3.4*, the best exceptional-set exponent for U and for ES₅ at primes is exactly 2/3, up to the
(log log N)^{2/3} of the cap. Those architectures are:
* nonnegative-on-ℤ CRT majorants that are ≥ 1 on the whole avoider set of a family of U/ES₅ word classes plus
  selectors, with coefficient-sum rounding and family primes ≤ N^A;
* or CRT-admissible large sieves and periodic Bessel/hybrid systems at polynomial level.

Theorem 3.5's majorant lies in this class, and it attains (log N)^{2/3} (for primes and y-rough inputs). For all
n ≡ 1 (mod 4) the attained exponent loses (log log N)^{1/3}. Not excluded: interval-only or prime-only positivity
(majorants ≥ 0 only at primes ≤ N), signed cancellation in the rounding errors, classes that are not word classes, and
any non-CRT input (§7).

**Reading (Assessment).**
* z50 target 3 for ES₅/U ("beat 3/4") is two steps beyond CRT, not one. Even reaching 3/4 for U or ES₅ requires a
  non-CRT ingredient. 3/4 for ES comes from the third divisor parameter, which these families lack.
* The CONTEXT's "α = 1/2 needed for a power saving with the ES₅ two-endpoint family" is now a theorem in its CRT
  form: CRT methods transfer only α ≤ 1/3 (L ≤ (log N)^{1/3}).
* The cap is a property of the class profile, not of ES₅'s colour. It holds verbatim for any union of word families
  with the square base: the (★) line, the b = 1 line, U, ES₅. The sibling result for I3 (z50-i3ex, zero base) is the
  same phenomenon.
* *Controls.* Odd squares coprime to the selector primes lie in 𝒜(𝔊) for every 𝔊, which is exactly the square base. So Theorem 3.2 is T1-consistent,
  and Theorem 3.5(c) is consistent with |E_U(N)| ≥ √N/2. Numerator 8: replacing 4ℤ by 8ℤ in Theorem 3.5 gives the
  analogous weak bound for the 8 | endpoint family. It asserts nothing at n = 17 or 241, so no false statement follows
  (cf. I3_DEEP_ASTRA §3). The hard primes 193, …, 8 813 281 are irrelevant to an exceptional-set count: U holds at
  every prime ≤ 10⁹ (z49 census).

## 4. Work item 3 — Linnik duality

### 4.1 (i) ES-type exceptionality forces no free character data

**Proposition 4.1 (PROVED; a precise form of the CONTEXT's Assessment).** Let 𝔊 be a finite family of word classes
(𝔘, 𝔉₅) or of ES forced classes (ℛ(M), (a,D), Case A), and let L be the lcm of its moduli.
(a) *Coprime characters.* 𝒜(𝔊) is a union of classes mod L. For every m coprime to L and every character χ mod m, the
    χ-values are exactly equidistributed on 𝒜(𝔊): n ↦ (n mod L, n mod m) is onto, and membership depends on n mod L
    only. So no constraint on χ_n at any modulus coprime to the class moduli.
(b) *Characters at a class modulus.* Let h be a modulus of 𝔊 and F_h ⊂ ℤ/h the union of the classes of 𝔊 at h. Then
    |F_h| ≤ 8τ(h+1) + 4τ(h) for word classes, and ≤ τ₃((h+1)/4)-type counts for ES classes (FIXED_MODULUS_SHOTS
    Thm 6.2(ii)). F_h contains no unit square, by §1.1 and K2 Lemmas 2.1–2.2. Hence F_h contains no coset of a subgroup
    of index ≤ 2 except when |F_h| ≥ φ(h)/2, which happens for only finitely many h. For every nontrivial χ mod h,
    |E_U[1_{F_h} χ]| ≤ |F_h|/h = h^{−1+o(1)}.
(c) *What a "free datum" would be.* A datum such as "(n/q) = +1 forced by exceptionality" is a forbidden set of
    density 1/2 at the modulus q. By (b) this happens only at the finitely many h with τ(h+1) ≍ h. These are the
    Mordell-type moduli 3, 5, 7, …, B1 territory: for U on n ≡ 1 (8), the classes at 3 and 5 forbid all non-residues
    mod 3 and mod 5, and 2 of the 3 non-residues mod 7.

So (i) of the brief holds in the precise form (a)–(b): exceptionality is a CRT event, and the character content of the
forbidden set at modulus h has size h^{−1+o(1)}.

*Proof.* (a) CRT. (b) The counts are §1.1. A coset of index ≤ 2 inside (ℤ/h)^× either contains 1 (the trivial
subgroup) or is the non-square half, of size ≥ φ(h)/2 > |F_h| for h ≥ h₀. The character bound is the triangle
inequality. The examples in (c) were checked in the fibre n ≡ 1 (8); see `scripts/z50_lsmass_primelocal.py`,
`forbidden()`. ∎

**EVIDENCE (`scripts/z50_lsmass_chars.py`, `data/z50_lsmass/chars.json`): exceptional points are QR-biased at small
primes.** All six non-square U-exceptions have least quadratic non-residue ≥ 11. The values are 11, 11, 13, 13, 17, 37;
978145 is a residue mod 92% of the primes ≤ 47. The baseline for n ≡ 1 (8) near 10⁶ is P(lqnr ≥ 11) = 0.23, so six of
six has chance ≈ 1.4·10⁻⁴. Of the ten listed (★)-failure primes, seven have lqnr ≥ 11, against a baseline of 0.125 for
primes ≡ 1 (4). This is the BM-main-term mechanism: M(p) is small when the small primes are residues. Per
Proposition 4.1(c), the forced part of this bias sits at the bounded moduli of B1. Beyond them the bias is
statistical: it comes from the joint structure of many sparse classes, not from forbidden half-cosets.

### 4.2 Linnik's dual sieve is a periodic Bessel system, hence capped

**Proposition 4.2 (PROVED; LS2 Thm 2.4 applied to Linnik's inequality).** Let E ⊂ [1, x] be contained in the avoider
set 𝒜(𝔊) of a forced-class mixture (ES: (D)24/KARY3) or of a word-class family (U/ES₅: Theorem 3.2). Take a finite
𝒜′ ⊂ [1, M] (M ≤ x^A) and real c_a. Any bound of the form

  |E| ≤ Δ·‖c‖² / min_{m∈E} |Σ_{a∈𝒜′} c_a χ_a(m)|²,

with χ_a(m) = (a/m) a Kronecker/Jacobi symbol and Δ from the dual multiplicative large sieve or Heath-Brown's quadratic
large sieve, saves at most S(λ) with λ ≪_A log x, provided the lower bound for the minimum is CRT-admissible (i.e.
justified for every point of 𝒜(𝔊)). Here S(λ) = Cλ^{3/4} for ES and Cλ^{2/3}(log λ)^{2/3} for U/ES₅.

*Proof.* As a function of m, χ_a has period 4a ≤ 4x^A. Linnik's inequality is the adjoint Bessel form
Σ_{m∈I} |Σ_a c_aχ_a(m)|² ≤ Δ‖c‖², valid for every interval I of length x (Montgomery: Δ = x + 16M²; Heath-Brown:
Δ ≪ (xM)^ε(x + M) on squarefree m). With rows φ_a = χ_a and L = min_{𝒜(𝔊)}|Σc_aχ_a|²/‖c‖² ≤ R̃(π) for every probability
π on 𝒜(𝔊) (Cauchy–Schwarz), the bound is LS2's type (i) with ψ ≡ 1. Then LS2 Theorem 2.4/Cor 2.5 applies, with the
comparison measure of LS2 Lemma 1.1 built from the relevant cap. ∎

**Why CAP_BOUNDED Thm 3.2 escapes (Assessment, with the exact computation).** Its exceptional set {p : q₃(p) > y} is
the avoider set of the *dense* family {n : (n/q) = −1}, for q ≡ 3 (4) and q ≤ y = (log X)^A. Here p_q = 1/2 at every
such q, so THETA's hypothesis p_ℓ ≤ 1/4 fails and no cap applies. The Rankin functional is Ψ(λ) ≍ π(y; 4, 3)·log 2,
which beats λ = 2 log X once A > 1. So Linnik's power saving is the primal large sieve on a dense profile, written
dually. It is not a separate door, and it is unavailable to every family covered by Prop 4.1(b).

### 4.3 (ii) Relaxations that force free character data

A relaxation R of ES (R-failure ⇐ ES-failure) whose failure forces (q/p) = +1 for every q ≤ y in a fixed set is
equivalent to the pointwise implication "(q/p) = −1 for some q ≤ y ⟹ R(p)": a family of **fixed-modulus shots** with
firing conditions (q/p) = −1.
* For caps e ≥ 1 these shots exist: CAP_POINTWISE's self-generated mute set gives a capped solution at every prime
  window q with (q/p) = −1, hence CAP_BOUNDED's power saving. The same holds for ES^{(S)}, ES^□ and V_φ.
* For ES itself (cap 0), FIXED_MODULUS_SHOTS Thm 6.2 (PROVED, scope stated there) rules out an infinite family of
  fixed-coefficient affine Type II shots with a common Chebotarev firing condition. Per modulus h, the certified
  residues form a divisor box of size h^{o(1)} containing no coset of a large subgroup. This is Prop 4.1(b) again,
  from the shot side.
* *Type I/II slices whose colour is not determined* do not exist. Every Type II point P_{u,B} has BM character
  χ_{−4uB}(p) = −1 forced by its class (BM_CORRECTED_COUNT Thm 1.1), and every ES₅ edge's colour is a function of its
  word (Theorem A, Lemma 1.2 of LOWERTAIL_DEEP_FABLE).

**Assessment (the answer to (ii)).** Inside the single-affine-shot framework there is no ES-type relaxation that keeps
cap 0 and forces dense character data. The ones that do (caps, ES^□, ES^{(S)}, V_φ) are exactly B-fin's T1-bearing
cousins, and they have power-saving exceptional sets because their profiles are dense. Pushing them through Linnik or
Heath-Brown gives power savings *for the relaxation* (known: CAP_BOUNDED Thm 3.2, V_φ X^{3/4}). It does not give them
for a genuine ES/U/ES₅ exceptional set, by Prop 4.2. Not excluded: joint multi-prime firing conditions (B4 territory),
p-dependent shots, and non-affine shots (the scope gaps of FMS Thm 6.2).

## 5. Work item 4 — the square floor and the (inverse) large sieve

### 5.1 The square floor is the large-sieve limit, for any depletion input

**Lemma 5.1 (PROVED, trivial).** For every odd prime ℓ and N ≥ ℓ², E_U ∩ [1, N] meets every nonzero quadratic-residue
class mod ℓ, because odd squares lie in E_U (Theorem E). So any depletion input satisfies ω(ℓ) ≤ (ℓ − 1)/2, and the
large sieve (and Gallagher's larger sieve) with any true depletion data gives at best ≫ N^{1/2}/log N. Conversely,
depletion ω(ℓ) ≥ (1/2 − o(1))ℓ at almost all ℓ ≤ √N would give the square floor N^{1/2+o(1)} (Montgomery), and
inverse large-sieve theorems (Green–Harper, Helfgott–Venkatesh, Walsh) would then describe E_U. Their hypothesis is
exactly this dense depletion.

### 5.2 CRT information forces only thin depletion (the barrier)

For a finite family 𝔊 ⊂ 𝔘 (any pivots, any size), call a ∈ ℤ/ℓ **CRT-depleted** if the profinite avoider set 𝒜(𝔊)
misses the class a mod ℓ entirely, and let ω_𝔊(ℓ) be the number of such a. These are exactly the depletions that a
CRT method can certify for every point of the avoider set.

**Theorem 5.2 (CRT-forced depletion is thin; PROVED from Theorem 3.2 and LS Thm 2.1).** For every finite 𝔊 ⊂ 𝔘 and
every Q ≥ Q₀,

  Σ_{W<ℓ≤Q} ω_𝔊(ℓ)/(ℓ − ω_𝔊(ℓ)) ≤ L_𝔊(Q) ≤ 2·exp(C(2 log Q)^{2/3}(log log Q)^{2/3}),

where L_𝔊(Q) is Montgomery's sum built from the ω_𝔊(ℓ), ℓ > W. In particular ω_𝔊(ℓ) ≥ ℓ/4 holds for at most
exp(O((log Q)^{2/3+o(1)})) = Q^{o(1)} primes ℓ ≤ Q. The same holds with the U-family replaced by 𝔉₅.

*Proof.* Take an interval I of length N = Q². 𝒜(𝔊) ∩ I misses ω_𝔊(ℓ) classes mod each ℓ. The depletion holds at
every point of 𝒜(𝔊), so Montgomery's bound (N + Q²)/L_𝔊(Q) is a CRT-admissible large-sieve bound in the sense of LS
§1. By LS Thm 2.1 it is ≥ N·E|g*|², where |g*|² is ≥ 0 on ℤ, ≥ 1 on 𝒜(𝔊), and has moduli lcm(q₁, q₂) with
q_i ≤ Q, hence level ≤ 2 log Q (all primes > W charged). Theorem 3.2 gives E|g*|² ≥ exp(−C(2 log Q)^{2/3}(log log Q)^{2/3}).
Hence L_𝔊(Q) ≤ (1 + Q²/N)exp(+…) = 2exp(…). The left inequality keeps only the prime moduli q = ℓ in L. ∎

**Reading.** The large-sieve route to the square floor needs ω(ℓ) ≍ ℓ at ≫ Q/log Q primes ℓ ≤ Q = √N. CRT
information, from word classes of any size, supplies it at Q^{o(1)} primes. So the depletion that inverse large-sieve
theorems would need must come from **finite-interval information about E_U ∩ [1, N]**: door (i) of CONTEXT §3. It
cannot come from congruence data. This is a barrier for a class of methods not covered by (D)17–(D)29, namely
"large sieve / inverse large sieve fed with CRT-certified depletion". It is a corollary of Theorem 3.2, not an
independent mechanism.

### 5.3 What CONTEXT §4(c) gets right and wrong (numerics; `scripts/z50_lsmass_depletion.c`,
`data/z50_lsmass/depletion_N2e7.txt`)

The C program sieves the fibre n ≡ 1 (8), n ≤ N, by every U word class (W1 and W2, strict CONTEXT definition: the
partner endpoint is ≥ 2) with pivot ≤ D. It reports the survivors and their occupancy mod ℓ.

| N | D (max pivot) | survivors | occupied classes mod 101 | occupied mod 1009 |
|---:|---:|---:|---:|---:|
| 2·10⁷ | 10² | 23 514 | 101 | 1009 |
| 2·10⁷ | 10³ | 2 319 | 77 | 544 |
| 2·10⁷ | 10⁴ … 2·10⁷ | 2 241 | 55 | 508 |
| 2·10⁶ | 10³ | 721 | 57 | 514 |
| 2·10⁶ | 10⁴ … 2·10⁶ | 712 | 55 | 507 |

At full level the survivors are exactly the odd squares plus 105, 2961, 3985, 25305, 111969, 978145. This
independently reproduces the z49 census to 2·10⁷ with the strict definition (CERTIFIED). Pivots ≤ 10⁴ already
suffice for every n ≤ 2·10⁷.
* **Wrong, for the actual set (EVIDENCE):** E_U ∩ [1, N] is depleted in ≈ ℓ/2 classes, not ≈ log N. Mod 101 it
  occupies 55 = 51 + 4 classes; mod 1009 it occupies 508 = 505 + 3. The finite set is depleted densely as soon as
  N·δ(D) ≪ √N, which happens at modest pivot levels.
* **Right, for what CRT can certify (PROVED, Theorem 5.2):** the profinite depletion is thin. At pivot level D < ℓ,
  CRT forces no depletion at ℓ at all (the D = 10² row mod 1009). At any level the forced depletion is summably sparse
  in the sense of Theorem 5.2.
* **Too pessimistic, in its consequence:** "at best N/(log N)^{O(1)} from the classical large sieve" understates it.
  Prime-pivot depletion alone gives exp(Θ(√log N)) (Prop 2.3), and CRT architectures reach exp(c(log N)^{2/3})
  (Theorem 3.5).

So the gap between E_U and its CRT shadow is precisely the gap between the finite depletion (≈ ℓ/2, which would give
the floor) and the certified one (Q^{o(1)} dense primes, which gives at most (log N)^{2/3+o(1)}).

## 6. Hostile reviews

**Model note.** The brief asks for `openai-codex/gpt-6-astra:high`. The subagent tool rejected the `:high` suffix
("could not resolve model"), so all reviews use `openai-codex/gpt-6-astra` in `deep` mode.

**R1 (Astra, deep; §§1–3, round 1).** Verdict per claim, and what was repaired:
* *Square base:* SOUND-WITH-MINOR. The ES₅ coprimality step and the W2 mod-8 bookkeeping were missing; both added
  in §1.1.
* *Prop 3.1(b):* SOUND-WITH-MINOR. The tail with u₀ = 6 log log y actually diverges like (log log y)^{3/2}. It is now
  u₀ = 8 log log y, which gives o(1). The large-e tail now cites h(e) ≪ e^{−1/2+ε}; the lower bound in (a) and the C < 1
  in (c) were added.
* *Theorem 3.2:* SOUND-WITH-MINOR. The reviewer found no hidden dependence on the four ES types and confirmed the block
  arithmetic. The blocks are now truncated at e^{λ/2}, and the zero-cost singleton steps above e^λ are made explicit.
* *Theorem 3.5:* SOUND-WITH-MINOR. h(B ∩ odd) ≍ h(B) holds only for the B actually used. Theorem B is unnecessary
  there. The explicit majorant ν = 1[n≡1(8)]·1[(n,P_y)=1]·Q_r(H) was written out, which places it inside Theorem 3.2's
  scope.
* *Cor 3.4:* SOUND-WITH-MINOR. The coarsening now uses S = log(1/Eν) via K2 Cor 6.1's two-case argument, and the
  hypotheses of the large-sieve and Bessel results are retained.
* *Cor 3.6:* MAJOR (overstated scope). "Any CRT method" was replaced by "within the architectures of Cor 3.4", with
  the exclusions listed.
* *Prop 1.3, Lemma 1.1, Lemma 2.1:* SOUND.
* *Theorem 2.2:* MAJOR, three defects, all repaired.
  * (b) lacked THETA's mass hypothesis for its remainder.
  * (c)(i)'s deduction from (b) was invalid. It is now proved from the new visible-mass bound (b′).
  * (c)(ii) needs cumulative asymptotics (counterexample p_ℓ = ⌊b log ℓ⌋/ℓ); under comparability only Θ(√λ) is
    claimed.
  * (c)(iii)'s band (e^{λ/2}, e^λ] is the *linear* regime (saving ≤ log(4/3)). The 1/μ regime is the quadratic band
    (e^{λ/4}, e^{λ/2}]; the statement is now split accordingly. The toy family C was already in the quadratic band.
* *Prop 2.3:* SOUND-WITH-MINOR. The bounds are cumulative, not pointwise; the conclusion now speaks of the "best
  saving".

The reviewer's independent enumeration found no unit square in 2,496 refined U/ES₅ classes with pivot ≤ 150. These
cover 150 u = 1 cases and 116 non-coprime W2 entries.

## 7. Remaining gap

(pending)
