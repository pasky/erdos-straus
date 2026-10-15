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

### Lemma 3.1 (prime-modulus SQ_± words, χ = (n/ℓ)) — SOUND
v = (n+u)/A, t = (A+1)/u; A = ±ℓ ≠ −1 so t ≠ 0, u ≠ −n so v ≠ 0. (−1/n) = 1 and Jacobi reciprocity with n ≡ 1 (4) give
χ = (±ℓ/n) = (n/ℓ) = (−u/ℓ). The "iff" has a potential edge case (the only u ≡ −n (mod ℓ) in ±div(ℓ±1) being u = −n,
which gives v = 0); it is vacuous: then ℓ ≡ ±1 (mod n) and (n/ℓ) = (ℓ/n) = (±1/n) = 1. Worth one sentence (D7).
u | ℓ ± 1 automatic for |u| ∈ {1,2,3,4,6}, ℓ ≥ 5 (24 | ℓ² − 1); the ψ_u table checked.

### Prop 3.2 (SQ_± prime-modulus layer, exponent 1/2) — SOUND-AFTER-REPAIRS (D5: the mass proof as written is wrong)
The written justification "the class u = 1 for ℓ ≡ 3 (4) together with u = 2, ±3, 4, ±6 gives ≫ 1 per dyadic block of
log ℓ" proves only S(X) = Σ_{X^{1/2}<ℓ≤X} ω_±/ℓ ≫ 1: a FIXED set of u contributes Σ_{X^{1/2}<ℓ≤X} O(1)/ℓ = O(1)
(Mertens: log 2), i.e. dimension 0, which gives no saving at all in the Thm 1.2 machinery (needs S/k → ∞ with
k ≍ log N/log X). The claim S ≫ log X is nevertheless TRUE, with a proof the document should give: for ℓ ≡ 3 (4) and
odd u | ℓ + 1 (⟺ ℓ ≡ −1 mod 4u), every odd prime q | u has (q/ℓ) = 1 (same reciprocity as the T1 line of Thm 1.4),
so (−u/ℓ) = −1 and −u is a firing class; classes −u (u < ℓ) are distinct. BV exactly as in Lemma 1.1 gives
S(X) ≥ Σ_{u ≤ X^{1/5} odd} (log 2)/φ(4u) − O(1) ≫ log X. (By the same reciprocity: for ℓ ≡ 1 (4) and u | ℓ − 1 odd,
(−u/ℓ) = +1 — those classes NEVER fire; for the mixed cases about half do.) The upper bound ω_± ≪ τ(ℓ²−1) = ℓ^{o(1)} is
the divisor bound (needed only for T); "Titchmarsh divisor bound" is needed only for the upper estimate Σω_±/ℓ ≪ log X
used in the Calibration. From-scratch `scripts/review_r230_sqpm.py`: Σ_{ℓ≤N} ω_±(ℓ)/ℓ = 1.92·log N (N = 10⁵),
2.04·log N (10⁶) (author: 1.95, 2.06 — small definitional offset, immaterial).

### Calibration "SQ_± provably HARDER on average" — overclaim (D6)
Only the PRIME-MODULUS layer (A = ±ℓ) of SQ_± was sieved, and only the prime-modulus layer of ES (Vaughan's classes)
is compared. An upper estimate on what one method yields for one layer proves nothing about which problem is harder
on average; the campaign's own ES record (3/4, composite multiplier moduli, paper/es-threequarter-note) already shows
that the prime-modulus exponent is method-dependent, and SQ_± words with composite A were not sieved at all. Must be
"Assessment: by the prime-modulus large sieve, SQ_± has class dimension 1 vs 2 for ES", with "provably" removed here
and in §5 item 3 ("signed twin harder on average than ES").

### CONJECTURE PM-SQ_± — EVIDENCE label correct; numerics reproduced
`scripts/review_r230_sqpm.py 1000000 40000` (independent: spf sieve, direct Jacobi (−A/n) on the constructed word,
exact tuv − u − v = n): **0 exceptions among all 124 500 non-squares n ≡ 1 (8) ≤ 10⁶**, least |u| ≤ 19 throughout;
odd squares ≤ 4·10⁴: no ticket in the COMPLETE search |u| ≤ n + 1 (T1 control; trivially forced by (n/ℓ) = 1).
Adversarial (`scripts/review_r230_sqpm_adv.py Q 20 300 7`, n ≡ 1 mod 8∏_{3≤q≤Q}q): Q = 13, 23, 31 → min 14, 16, 22
tickets (u, ℓ) with |u| ≤ 300, n up to 6.8·10¹⁶, least |u| ≤ 6 — consistent with the author's 10, 11, 21.
(Note: the search is finite, |u| ≤ n + 1, since ℓ | n + u and u | ℓ ± 1; worth stating so "exception" is decidable.)

### §4 negative constructions — labels essentially correct (MINOR D8)
§4 claims nothing positive. Spot checks: fixed-field memo's no-free-point lemma holds (norms of rβ^iε^j are
±(16n)^i r²; −E with E ≡ 3 (4), gcd(E, n) = 1 is impossible for non-square n — for i odd it would force n | E after
clearing denominators). Pell memo: "order ⊂ ℚ(√n) ⇒ n | μ" is right for squarefree n (μ²b² = n(a² + b²) ⇒ p ∤ b ⇒ p | μ),
though the written "iff n | μ²" is only the needed direction. But the memo's verdict "Negative, PROVED in the stated
scope" attaches PROVED to an informal claim ("the unit never acts on an ES^{[2]} fibre"); only the order lemma is PROVED.
§4 bullet 4 ("k-free values of binary recurrences are open for every fixed k") is uncited, and what is needed is ONE
(e+1)-free orbit element, not infinitely many/density — label Assessment and cite or soften.

## Numbered defects

**D1 (MAJOR, calibration/scope).** CAP_GROWING Thm 1.2 Calibration ("e ≥ 2 beats Vaughan (and the loglog note)"),
Thm 1.4 line "e = 0 is Vaughan's 2/3; e = 1 gives 3/4", §1 Reading ("ES itself is the case e = 0"), §5 item 1, and
AGENT_REPORT_O229 l. 11 ("every e ≥ 1 beats it"). The campaign's own ES record is N exp(−c(log N)^{3/4})
(paper/es-threequarter-note, internally proved; composite multiplier moduli, cubic class mass), and EXCEPTIONAL_KARY3
Thm 4.1/Cor 4.2 caps ES-certificate CRT methods at (log N)^{3/4}. So e = 1 merely ties ES's record, the relaxation
strictly exceeds what is known for ES only for e ≥ 2 (4/5), and "ES is the case e = 0" is true only for the
prime-modulus large-sieve architecture. Repair: say "prime-modulus large sieve" wherever e = 0 ↔ 2/3 is asserted; add
one sentence: "No conflict with KARY3's 3/4 cap: overflow classes with R > 1 certify ES^{(y,e)}, not ES, so they lie
outside the K2 class family; their mass (log)^{e+2} exceeding the ES cubic mass for e ≥ 2 is the signature of the
relaxation. Combining the overflow with the 3/4 note's multipliers should give (e+3)/(e+4) (Assessment)." Fix the agent
report line accordingly.

**D2 (MINOR, proof precision).** Thm 1.4 proof, "restrict all three to ≤ X^{1/(5(2e+3))}". With R constrained to ≤ Z
separately, the lower bound (log)^{e+2} is not immediate. Repair: restrict to m := c₀d₀ ≤ W := X^{1/(10(e+1))}; then
R ≤ c₀^e, M = c₀²d₀R² ≤ m^{2e+2} ≤ X^{1/5} automatically, and the sum is ≥ ½·Σ_{m≤W odd} μ²(m)∏_{s|m}(2/(s−1) + e/s)
≥ ½Σ μ²(m)(e+2)^{ω(m)}/m ≫_e (log X)^{e+2}.

**D3 (MINOR, citation route).** Cor 2.2 "PROVED relative to Vaughan 1970 / PW Thm 1.3": Vaughan 1970 is inaccessible
(sources/vaughan-1970-access-log.md) and PW §4 does not display the classes, so "uses only the classes of Lemma 2.1"
is uncheckable from sources. Repair: prove Cor 2.2 as the e = 0 case of Thm 1.4 (R = 1 ⇒ cube lemma at prime modulus
ℓ ⇒ PM-II certificate), label "PROVED relative to BV + large sieve", cite PW Thm 1.3 (m = 4) as consistent.

**D4 (MINOR, label upgrade).** §2 Remark (ii): "only h = 3, 7 have covering class sets (CERTIFIED ≤ 2·10⁴) … no further
covering (B1)". This is PROVED for all h: #classes ≤ τ₃(K) ≤ τ(K)² ≤ (3.5273·K^{1/3})² < 2K − 1 for K > 241, and
τ₃(K) ≥ 2K − 1 only for K ∈ {1, 2} below that (`scripts/review_r230_pmcover.py`).

**D5 (MAJOR, proof gap — repairable).** Prop 3.2 proof: the stated reason for Σ_{X^{1/2}<ℓ≤X} ω_±/ℓ ≫ log X (fixed
u-classes "≫ 1 per dyadic block of log ℓ") only yields ≫ 1, which gives no saving at all. Repair (see verdict above):
for ℓ ≡ 3 (4) and odd u | ℓ + 1, (−u/ℓ) = −1 by reciprocity, so the classes −u, u ≤ X^{1/5} odd with ℓ ≡ −1 (mod 4u),
all fire; BV as in Lemma 1.1 gives ≫ log X. Replace "Titchmarsh divisor bound" in the label by "divisor bound" (only the
upper estimate ≍ log X in the Calibration needs Titchmarsh/Brun–Titchmarsh).

**D6 (MAJOR, overclaim).** §3 Calibration "the signed twin is provably HARDER on average (exponent 1/2 < 2/3)", §0 (Z4)
"provably harder on average by this method", §5 item 3, AGENT_REPORT l. 15. Comparing the exponents one method yields
on one layer (A = ±prime) does not prove a comparison of the problems. Repair: "Assessment: the prime-modulus class
dimension of SQ_± is 1 (vs 2 for ES), so this method gives a weaker exponent for SQ_±"; delete "provably" and "harder".

**D7 (MINOR).** Lemma 3.1 "iff": add the one-line exclusion of the u = −n edge case ((n/ℓ) = (±1/n) = 1), and note
the PM-SQ_± search is finite (|u| ≤ n + 1), so the conjecture's "exception" is decidable.

**D8 (MINOR, labels).** z5_pell_unit_T1 Assessment "Negative, PROVED in the stated scope": PROVED only for the order
lemma; "never acts on a fibre" is an informal reading → Assessment. §4 bullet 4 and memo: k-free-values claim uncited;
mark Assessment.

**D9 (MINOR, stale text/structure).** Thm 1.2 Calibration still says "(Assessment, not proved.) Combining the cap with
Vaughan's d-dimension should give (e+2)/(e+3)" — that is now Thm 1.4; replace by a pointer. §1.2 (Prop 1.3/Thm 1.4)
sits after §3; move it into §1. "Supersedes" is asymptotic only: at X ≤ 4·10⁶ the cube mass (4M < ℓ) is below the
shot mass (Q < ℓ/2) (`scripts/review_r230_mass.py`); a remark that a union of both families is used in practice would
help. The large-sieve-ceiling remark ("ω ≤ (log ℓ)^{O(1)}") is false pointwise (ω can be exp(c log ℓ/log log ℓ)); the
intended hypothesis is Σ_{ℓ≤y} ω(ℓ)/ℓ ≪ (log y)^A, which via Rankin gives L ≤ exp(O((log N)^{A/(A+1)})).
