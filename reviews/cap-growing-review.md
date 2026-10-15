# R230 — hostile review of O229 (CAP_GROWING.md, BRAINSTORM/z5_*.md)

Reviewer: R230 side agent. Author branch merged: side-agent/cap-growing. From-scratch scripts: scripts/review_r230_*.py.
Status: in progress.

## Summary verdicts (filled in as checked)

### Prop 1.3 (overflow cube) — SOUND
Re-derived: 4(x + c₀²d₀R²) = E(ℓ+1) = 4EK ⇒ x + c₀²d₀R² = EK ⇒ 1/y + 1/z = (x + c₀²d₀R²)/(p c₀d₀j x) = E/(px) = 4/p − 1/x.
Integrality: Eℓ ≡ p (mod 4c₀d₀) and ℓ ≡ −1 ⇒ 4c₀d₀ | p + E. Valuations at s | R: s ∤ E (Eℓ ≡ p ≢ 0 mod s), v_s(x) = σ
because 2σ + 2ρ > σ, so v_s(z) = −2ρ; for s ∤ R, c₀ | x gives v_s(z) ≥ 0. All ES^{(y,e)} side conditions (s odd, s ∤ p,
s | y, even valuation ≥ −2e) hold. `scripts/review_r230_cube.py 2000`: sympy residual 0; brute force over EVERY prime
ℓ ≡ 3 (4) < 2000, every factorisation K = c₀d₀j (c₀, d₀ arbitrary), every odd R with rad R | c₀, v_s(R) ≤ 3, three primes
p per class: 78 852 hypothesis-satisfying cases, den z = R² and rad R | y in all. Negative control: all 20 250 cases
violating v_s(c₀) = v_s(K) have den z ≠ R² (smaller), so that hypothesis is genuinely needed for the *exact* den
claim (still harmless: the identity holds and the solution remains in ES^{(y,e)}). No defect.

### Lemma 1.1 (shot class mass ≫ (log X)^{e+1}) — SOUND
Re-derived: Q^{(e)} | K ⟺ ℓ ≡ −1 (mod 4Q^{(e)}); h(R) ≤ (e+1)^{ω(R)} (exponent r ≥ 2 of R forces v_s(Q) = r + e; r = 1
allows v_s(Q) ∈ [1, e+1]); moduli 4R ≤ 4X^{1/5} < y^{1/2}(log y)^{−B} for y ≥ X^{1/2}; BV with divisor-bounded weights
(Cauchy–Schwarz against the trivial/Brun–Titchmarsh bound) + partial summation gives Σ_R h(R)|E_R| ≪ (log X)^{−B'}.
Lower bound: Q = r₁r₂²⋯r_{e+1}^{e+1} has Q^{(e)} = rad Q and Q ≤ Z^{(e+1)(e+2)/2} = X^{1/5}; distinct splittings are
distinct Q. Euler factor of the full shot weight: 1 + (e+1)/(s−1) + O(s^{−2}) — dimension e+1 confirmed. Distinctness of
the classes −4Q² (Q < ℓ/2) and T = Σ(ω/ℓ)² ≤ X^{−1/2+o(1)}S (ω_e(ℓ) ≤ τ(K)(e+1)^{ω(K)} = ℓ^{o(1)} for FIXED e) checked.

### Thm 1.2 (exponent (e+1)/(e+2)) — SOUND
Re-derived the large-sieve step for general class dimension a: q = product of k distinct primes of (X^{1/2}, X] with
k = ⌊log N/(2 log X)⌋ ⇒ q ≤ N^{1/2}; L ≥ e_k(ω/ℓ) ≥ (S^k − C(k,2)S^{k−2}T)/k!; k! ≤ e√k(k/e)^k; with
log X = C(log N)^{1/(a+1)}, S/k ≥ 2c C^{a+1} — choosing C = C(c_e) large gives |𝒩| ≤ 2N/L ≪ N√k e^{−k},
k ≍ (log N)^{a/(a+1)}. All constants depend on e only through c_e and X₀(e). p > X ≥ ℓ > Q guarantees gcd(Q,p) = 1 and
p ≢ 0 (mod ℓ). The statement for fixed e is correct; non-uniformity in e is correctly flagged.

### Thm 1.4 (exponent (e+2)/(e+3)) — SOUND-AFTER-REPAIRS (presentation/calibration only; see D1, D2)
Re-derived: (i) for triples with c₀ squarefree, s² ∤ K ⟺ v_s(c₀) = v_s(K) = 1, so Prop 1.3 applies; (ii) density of
{ℓ ≡ −1 (4c₀d₀), ℓ ≢ −1 (4s²) ∀ s | R}: the s lifts of −1 mod 4c₀d₀ to mod 4c₀d₀s are all units, one is excluded ⇒
∏(1 − 1/s)/φ(4c₀d₀) (inclusion–exclusion over t | rad R, moduli ≤ 4c₀²d₀ ≤ 4X^{1/5}, 2^{ω(R)} terms — BV-admissible);
(iii) injectivity: gcd(d₀, c₀R) = 1 so d₀ = squarefree kernel of M = d₀(c₀R)², c₀ = rad(c₀R) — and 4M < ℓ makes the
classes distinct residues; (iv) Euler factor 1 + 2/(s−1) + e·(1−1/s)/(s−1) = 1 + (e+2)/s + O(s^{−2}); (v) T1:
(−4M/ℓ) = −(d₀/ℓ) and (q/ℓ) = (ℓ/q)(−1)^{(q−1)/2} = (−1/q)(−1)^{(q−1)/2} = 1 for odd q | ℓ+1. All correct.
`scripts/review_r230_cube.py`: for all ℓ ≡ 3 (4) < 2·10⁴, e ≤ 3, the Thm 1.4 classes are pairwise distinct and all
quadratic non-residues (max ω'_e = 60). c_e depends only on e (via the Euler product and the size restriction).
*Evidence note.* `scripts/review_r230_mass.py 4000000 3` (from scratch): with the natural range 4M < ℓ the cube mass S'_e
is BELOW the shot mass S_e at every X ≤ 4·10⁶ (e = 3: 6.67 vs 10.53), and both have local log-log slope ≈ 2.0 at
X ≈ 2²⁰–4·10⁶. The extra dimension is purely asymptotic (the shots range over Q < ℓ/2, the cube only over M < ℓ/4); no
numerics for S'_e are given in the document. Not a defect of the proof, but "supersedes" is asymptotic only.
*Sieve-limit consistency.* No contradiction: EXCEPTIONAL_KARY3 Thm 4.1/Cor 4.2 caps savings at C(log N)^{3/4} for
mixtures of ES-certificate classes (ℛ(M), (a,D), Case A, selector), whose mass is ≪ (log y)³ (KARY3 Cor 3.3). Overflow
classes with R > 1 certify only ES^{(y,e)} (den z = R² ≠ 1); they are outside that family, and indeed their mass
(log)^{e+2} exceeds the cubic ES cap for e ≥ 2 — which is exactly the expected signature of a relaxation. See D1 for the
wording that must make this scope explicit.

### Lemma 2.1 (Vaughan's classes are PM-II certificates) — SOUND
4uvw ≡ 1 (mod ℓ) ⇒ v^{−1} ≡ 4uw ⇒ −uv^{−1} ≡ −4u²w; (c,d,j) = (u,w,v) is a cube point (FIXED_MODULUS_SHOTS Lemma 1.1)
with h = 4uwv − 1 = ℓ prime: exactly BRIDGE_WORLDS §5's prime-modulus Type II certificate.

### Cor 2.2 (PM-II exceptions ≪ N exp(−c(log N)^{2/3})) — SOUND-AFTER-REPAIRS (D3: citation route)
The deduction is right, but as written it rests on Vaughan 1970, which the campaign could NOT access
(sources/vaughan-1970-access-log.md), and on PW Thm 1.3 (sources/pw.txt l. 69ff), whose §4 only says "as shown in [12]
… at least f(p) residue classes mod p" without displaying them — so "Vaughan's sieve uses only the classes of Lemma
2.1" cannot be checked against either source text. Better: Cor 2.2 is literally Thm 1.4 at e = 0 of this very document
(R = 1: classes −4c₀²d₀ mod ℓ, Prop 1.3 with R = 1 is the cube lemma at the PRIME modulus ℓ — a PM-II certificate),
which is PROVED relative to BV + large sieve only, and checked here. PW Thm 1.3 (m = 4) then serves as a consistency
check, not as the proof.

### Remark (ii), covering moduli {3, 7} — SOUND, and can be upgraded from CERTIFIED to PROVED (D4)
`scripts/review_r230_pmcover.py 20000` (from scratch): among primes h ≡ 3 (4) ≤ 2·10⁴ exactly h = 3, 7 have class sets
{−4c²d : cd | (h+1)/4} equal to all (h−1)/2 non-residues; every class is a QNR (T1). Residue facts checked: h = 7 classes
{3, 5, 6} = QNRs mod 7; h = 3 class {2}; 3361 ≡ 1 (mod 84), ≡ 1 (mod 5). Moreover the number of classes is ≤ τ₃(K)
(K = (h+1)/4) and τ(n) ≤ C₃n^{1/3}, C₃ = ∏_p max_a (a+1)p^{−a/3} = 3.5273, so τ₃(K) ≤ τ(K)² < 2K − 1 for K > 241;
direct check K ≤ 242: τ₃(K) ≥ 2K − 1 only for K = 1, 2. Hence **h = 3, 7 are the only covering primes, for all h**
(PROVED, elementary) — the "B1" assessment becomes a theorem.
