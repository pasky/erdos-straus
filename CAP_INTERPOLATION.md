# CAP_INTERPOLATION — the exponent cap as a sieve-dimension knob, uniformly in e (task O234, spark relay Z4)

Status: in progress (O234). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on CAP_GROWING (O229: Prop 1.3 overflow cube, Thm 1.4), EXPONENT_CAP ((J)34: Def 1.1, Prop 1.2, Prop 3.1,
Dictionary 3.3), PHASE_DIAGRAM ((J)43: Thm 5.1), FROBENIUS_FIRING (Thm 4.2, Thm 4.4), the 3/4 note
(paper/es-threequarter-note.tex, §"heuristic mass-driven ceiling"). Scripts `scripts/z10_*`, outputs `data/z10/`.

Notation. λ := log log N, log₃ := log log log. For a prime ℓ ≡ 3 (mod 4), K := (ℓ+1)/4. A *cube triple* is
τ = (c₀, d₀, R) with c₀, d₀ odd, squarefree, coprime, c₀d₀ | K, rad R | c₀; V(τ) := c₀²d₀R²; the triple has
*cap e* if v_s(R) ≤ e for all s. Its class is −4V(τ) mod ℓ (CAP_GROWING Prop 1.3).
κ := e + 2 (the number of local options per prime of c₀d₀: s | d₀, or s | c₀ with v_s(R) ∈ {0, …, e}).

## 0. Iteration log

(Z4-1) Goal 1, first pass. O229's c_e came from Lemma 1.1 of CAP_GROWING (Bombieri–Vinogradov with divisor-bounded
weights h(q) ≤ κ^{ω(q)}). That step is NOT uniform: Cauchy–Schwarz against BV needs Σ h(q)²/q ≤ (log x)^{A}, i.e.
κ² ≪ A. Barrier hypothesis identified: "BV with fixed A". Modification: the moduli 4c₀d₀ only need to be
≤ X^{1/(10κ)}, and then log x/log q ≥ 5κ → ∞: Gallagher's prime number theorem gives a *relative* error
exp(−cκ) per modulus, with no weight problem. Result: c_e ≍ 1/(e log e), uniformly (§1–2, Thm 2.1).
(Z4-2) Letting e = e(N) grow: the bound (log N)^{κ/(κ+1)}/(κ log κ) is maximised at κ ≍ log log N, where it
equals log N/(log₂N·log₃N). A Rankin computation shows this is the CEILING of the prime-modulus large sieve with
the overflow-cube classes *truncated to V < ℓ/4* at any cap (Thm 3.1). So within the truncated family the knob
saturates at e ≍ log log N. (R237 repair D1: the truncation is NOT forced by the architecture — Prop 1.3/Prop 5.1 have
no size condition on D — and with the full family 𝒟_e(ℓ) the prime-modulus large sieve gives a power saving at
e = ∞ and at e ≥ (log N)^{1+ε}; see Remark 3.2. The large sieve never reaches "all n ≥ n₀" in any case.)
(Z4-3) Goal 1 from the pointwise side: … (§4).
(Z4-0, after R230) Calibration fixed by R230 D1: "e = 0 is Vaughan's 2/3" is a statement about the *prime-modulus*
large sieve only; ES's record is (log N)^{3/4} (composite multipliers kℓ, 3/4 note) and KARY3 caps CRT methods for
ES at 3/4. Everything in §§1–3 is prime-modulus large sieve; §5 treats composite moduli.

## 1. A uniform class supply (no Bombieri–Vinogradov weights)

**Input (G) (Gallagher's prime number theorem; Gallagher, Invent. Math. 11 (1970) 329–339, Thm 7; cited, not
re-derived).** There are absolute c₁, c₂ > 0, C₁ such that for x ≥ 3 and 1 ≤ T ≤ x^{c₂}:
Σ_{q≤T} Σ*_{χ mod q} |ψ(x, χ)| ≤ C₁ x (exp(−c₁ log x/log T) + exp(−c₁ √log x)), where Σ* runs over primitive
non-principal characters other than the (at most one) exceptional real character χ₁ of conductor q₁ ≤ T.
Consequence (standard): for every q ≤ T with q₁ ∤ q and (a, q) = 1,
`  |ψ(x; q, a) − x/φ(q)| ≤ (x/φ(q))·η(x, T),   η := C₁(exp(−c₁ log x/log T) + exp(−c₁√log x)) + O(log²(qx)/x^{1/2}).`
(ψ(x;q,a) = φ(q)^{−1}Σ_χ χ̄(a)ψ(x,χ); χ₁ does not occur mod q when q₁ ∤ q; each χ ≠ χ₀ is induced by a primitive
χ* of conductor d | q, d ≤ T, and |ψ(x,χ) − ψ(x,χ*)| ≤ log²(qx).)

**Lemma 1.1 (Rankin lower bound for κ^{ω}; PROVED, elementary + Mertens).** There are absolute C₂, C₃ such that for
every integer κ ≥ 1, every set 𝒫' of primes containing all odd primes except at most one, and Z with
log Z ≥ 4(C₂κ + 1):
`  F_Z := Σ_{m ≤ Z, μ²(m)=1, p|m ⇒ p∈𝒫'} κ^{ω(m)}/m  ≥  ½ exp{κ (log log Z − log κ − log log(κ+2) − C₃)}.`
*Proof.* For σ ∈ (0, ½] put F(σ) := ∏_{p∈𝒫'}(1 + κp^{−1−σ}) = Σ_m κ^{ω(m)} m^{−1−σ}. Then
F_Z ≥ Σ_{m≤Z} κ^{ω}m^{−1−σ} ≥ F(σ) − Z^{−σ/2}F(σ/2). Per prime, (1+aX)/(1+aY) ≤ 1 + a(X − Y) for X ≥ Y, so
log(F(σ/2)/F(σ)) ≤ κ Σ_p p^{−1−σ/2}(1 − p^{−σ/2}) ≤ κ[Σ_{p ≤ e^{2/σ}} (σ/2)(log p)/p + Σ_{p > e^{2/σ}} p^{−1−σ/2}]
≤ C₂κ (Mertens Σ_{p≤y} log p/p = log y + O(1); the tail is ≤ ∫_{2/σ}^∞ e^{−σt/2}dt/t + O(1) = O(1)). Choose
σ := 2(C₂κ + 1)/log Z ≤ ½; then Z^{−σ/2}F(σ/2) ≤ e^{−1}F(σ) and F_Z ≥ ½F(σ). Lower bound: for p > κ,
log(1 + κp^{−1−σ}) ≥ κp^{−1−σ} − κ²p^{−2}/2, and Σ_{p>κ} p^{−2} ≤ 1/κ; Σ_p p^{−1−σ} = log(1/σ) + O(1)
(log ζ(1+σ) = log(1/σ) + O(σ)); removing p ≤ κ, p = 2 and the one excluded prime costs log log(κ+2) + O(1). Hence
log F(σ) ≥ κ(log(1/σ) − log log(κ+2) − C) and 1/σ = log Z/(2(C₂κ+1)) ≥ log Z/(2(C₂+1)κ). ∎

**Proposition 1.2 (uniform cube supply; PROVED relative to (G)).** There are absolute κ₀, C₄ such that for every
e ≥ κ₀ − 2 (κ = e + 2), and X ≥ X₀ with u := log X ≥ 40(C₂+1)κ²:
`  S_e(X) := Σ_{X^{1/2}<ℓ≤X, ℓ≡3 (4)} ω_e(ℓ)/ℓ ≥ exp{κ(log u − 2 log κ − log log(κ+2) − C₄)},`
where ω_e(ℓ) counts the distinct classes −4V(τ) mod ℓ of cap-e cube triples with V(τ) ≤ X^{1/5}. Moreover
ω_e(ℓ) ≤ X^{1/5} ≤ ℓ^{2/5}.
*Proof.* Put Y := X^{1/5}, Z := Y^{1/(2e+2)} (log Z = u/(10(e+1))), T := 4Z. For squarefree odd m ≤ Z, every
assignment "s | d₀" or "s | c₀ with v_s(R) = ρ_s ∈ [0, e]" (s | m) is a cap-e triple with c₀d₀ = m and
V ≤ m^{2+2e} ≤ Y: κ^{ω(m)} triples, whose classes are pairwise distinct (CAP_GROWING Thm 1.4: τ ↦ V(τ) is
injective) and are valid at every prime ℓ ≡ −1 (mod 4m) (ℓ > 4Y; CAP_GROWING Prop 1.3 — the hypothesis
v_s(c₀) = v_s(K) for s | R is NOT needed for cap e, see Remark 1.3). If the exceptional modulus q₁ (w.r.t. T) exists,
its odd part m₁ is > 1 for T ≥ T₀ (χ₋₄, χ_{±8} have no real zero near 1), and we drop one prime s₁ | m₁ from 𝒫'.
For x ∈ [X^{1/2}, X]: log x/log T ≥ (u/2)/(u/(10(e+1)) + 2) ≥ 4κ, so η ≤ 1/6 for κ ≥ κ₀; dyadic summation of
θ(2y; q, −1) − θ(y; q, −1) ≥ (1 − 3η)y/φ(q) gives Σ_{ℓ∈(X^{1/2},X], ℓ≡−1 (q)} 1/ℓ ≥ 1/(5φ(q)) for q = 4m. So
S_e(X) ≥ Σ_m κ^{ω(m)}/(10m) = F_Z/10 with 𝒫' = odd primes ∖ {s₁}. Lemma 1.1 (log Z ≥ 4(C₂κ+1) by the hypothesis on u)
and log log Z = log u − log(10(e+1)) give the claim. ω_e(ℓ) ≤ #{V ≤ Y} ≤ Y. ∎

**Remark 1.3 (the exactness condition is unnecessary; PROVED).** In CAP_GROWING Prop 1.3 drop "v_s(c₀) = v_s(K) for
s | R". With σ := v_s(K) ≥ 1 = v_s(c₀), ρ := v_s(R) ≥ 1: v_s(E) = 0 and x = EK − c₀²d₀R², z = p·x·j/(c₀R²),
v_s(j) = σ − 1. If σ < 2 + 2ρ: v_s(x) = σ, v_s(z) = 2σ − 2 − 2ρ ∈ [−2ρ, 0) ∪ [0, ∞) — even, ≥ −2ρ. If σ ≥ 2 + 2ρ:
v_s(x) ≥ 2 + 2ρ and v_s(z) ≥ σ − 2 ≥ 0 (if σ > 2+2ρ, v_s(x) = 2+2ρ exactly; if σ = 2+2ρ, v_s(x) ≥ σ). In all cases
v_s(z) is even when negative, ≥ −2e, and s | y = p c₀ d₀ j. So every cap-e triple with c₀d₀ | K gives an
ES^{(y,e)}(p) solution (den z = ∏ s^{2 max(0, 1+ρ_s−σ_s)}). Checked numerically in §6 (z10_cube_check).

## 2. Uniform exceptional-set bound: c_e ≍ 1/(e log e), saturation at e ≍ log log N

**Theorem 2.1 (ES^{(y,e)} almost always, uniformly in e; PROVED relative to (G), Bombieri–Vinogradov (for the
finitely many e < κ₀ − 2, via CAP_GROWING Thm 1.4 as repaired by R230 D2) and Montgomery's large sieve;
ineffective).** There are absolute c > 0 and N₀ such that for N ≥ N₀ and every integer 0 ≤ e ≤ log log N,
`  #{p ≤ N prime : ES^{(y,e)}(p) has no solution} ≤ N·exp{−c·(log N)^{(e+2)/(e+3)}/((e+2)·log(e+3))}.`
Consequently, by monotonicity in e (ES^{(y,e)} ⊆ ES^{(y,e')} for e ≤ e'), for every e ≥ log log N (including e = ∞):
`  #{p ≤ N : ES^{(y,e)}(p) fails} ≤ N·exp{−c′·log N/(log₂N·log₃N)}    (take e = ⌊log log N⌋, κ ≍ λ).`
*Proof.* e < κ₀ − 2: finitely many cases, each CAP_GROWING Thm 1.4 (exponent (e+2)/(e+3), constant c_e > 0); take
c ≤ min c_e·(e+2)log(e+3). Let κ = e + 2 ≥ κ₀. *Large sieve.* Montgomery: the set 𝒩 of exceptional primes in (X, N]
avoids, for each prime ℓ ∈ (X^{1/2}, X], the ω_e(ℓ) classes of Prop 1.2 (they are nonzero mod ℓ, and p > X > R, so
p ∤ R; every hit is an ES^{(y,e)}(p) solution by Prop 1.3 + Remark 1.3). Hence |𝒩| ≤ 2N/L, L ≥ Σ over q = products
of k distinct such ℓ (X^k ≤ N^{1/2}, k := ⌊log N/(2u)⌋) of ∏ω_e(ℓ)/ℓ ≥ (S^k − (k choose 2)T S^{k−2})/k!, with S = S_e(X),
T = Σ(ω_e/ℓ)² ≤ X^{−3/10}S.
*Choice of u.* Write A_κ := 2 log κ + log log(κ+2) + C₄ (C₄ ≥ log(40(C₂+1)), so u ≥ e^{A_κ} meets the hypothesis of
Prop 1.2) and set log u := A_κ + 1 + λ/(κ+1), i.e. u = e^{C₄+1}κ² log(κ+2)·(log N)^{1/(κ+1)}. Prop 1.2 gives
log S ≥ κ(log u − A_κ) ≥ κ, and log k ≤ λ − log(2u), so
`  log(S/k) ≥ (κ+1) log u − κA_κ − λ = A_κ + κ + 1 ≥ κ + 1.`
*Collisions.* T ≤ max_ℓ(ω_e(ℓ)/ℓ)·S ≤ X^{−3/10}S, so (k choose 2)T S^{k−2} ≤ ½S^k once k² ≤ X^{3/10}, i.e. u ≥ 7λ: for
κ + 1 ≤ λ/log(7λ) this follows from u ≥ (log N)^{1/(κ+1)}, otherwise from u ≥ e^{C₄}κ² ≥ e^{C₄}λ²/log²(7λ).
Hence L ≥ S^k/(2k!) ≥ ½(S/k)^k and log L ≥ (κ+1)k − 1. With k ≥ log N/(2u) − 1:
`  log L ≥ (κ+1)(log N)^{κ/(κ+1)}/(2e^{C₄+1}κ² log(κ+2)) − (κ+2) ≥ c (log N)^{κ/(κ+1)}/(κ log(κ+2))`
(the subtracted κ + 2 ≤ λ + 4 is of lower order for κ ≤ λ + 2). Primes ≤ X number ≤ e^u, and u ≤ e^{C₄+1}κ² log(κ+2)(log N)^{1/(κ+1)} ≤ ½ log N − (saving) for
2 ≤ κ ≤ λ + 2 and N ≥ N₀ (at κ ≍ λ, u ≍ λ² log λ), so they are negligible; and u ≤ log N/4, so k ≥ 1. ∎
*Remark 2.2.* (a) **c_e ≍ 1/(e log e)** — polynomial decay, not ((e+1)(e+2))^{−e} (O229's Thm 1.2 calibration: an
artefact of BV's divisor weights and of restricting every coordinate to X^{1/(5(2e+3))}). (b) The saving
(log N)^{κ/(κ+1)}/(κ log κ) = log N·exp(−λ/(κ+1))/(κ log κ) is maximal at κ ≍ λ, with value ≍ log N/(λ log λ):
**the knob saturates at e ≍ log log N** — for the truncated family D < ℓ/4 used here (R237 repair D1; Remark 3.2). (c) The d₀-coordinate is included in κ = e + 2; Vaughan's prime-modulus
case is κ = 2 (e = 0), exponent 2/3. (d) T1: all classes are QNRs mod ℓ (CAP_GROWING Thm 1.4 T1, which does not use
exactness), odd squares are never hit; the bound is consistent with the ≍ √N odd squares ≤ N.

## 3. The ceiling: the prime-modulus large sieve with TRUNCATED cube classes cannot beat log N/(log₂N·log₃N), at any cap

Let ω_∞(ℓ) be the number of distinct classes −4V(τ) mod ℓ over ALL cube triples τ at ℓ (any cap, V(τ) < ℓ/4) — the
largest *truncated* class family; every capped family truncated to V < ℓ/4 is a subfamily. (R237 repair D1: it is
NOT the largest class family of the architecture: the certificates at ℓ are all −4D, D ∈ 𝒟_e(ℓ), of any size —
Prop 5.1 — and V < ℓ/4 only serves distinctness. See Remark 3.2.)

**Theorem 3.1 (ceiling; PROVED, elementary: Rankin + Mertens + PNT).** There is an absolute C such that for N ≥ 16
and any choice of ω(ℓ) ≤ ω_∞(ℓ) classes (from the cube family) at the primes ℓ ≤ N^{1/2}, ℓ ≡ 3 (4):
`  log L ≤ C log N/(log₂N·log₃N),   L := Σ_{q≤N^{1/2}} μ²(q) ∏_{ℓ|q} ω(ℓ)/(ℓ − ω(ℓ)).`
So the large-sieve bound 2N/L for ES^{(y,e)} with truncated classes is ≥ N exp(−C log N/(log₂N log₃N)) for every
e ≤ ∞: Theorem 2.1 is optimal for the truncated family up to the constant. (R237 repair D1: the former claim "no cap —
not even e = ∞ — gives a power saving" is FALSE for the untruncated family, Remark 3.2.)
*Proof.* The classes are distinct non-residues (Remark 2.2(d)), so ω ≤ (ℓ−1)/2 and ω/(ℓ−ω) ≤ 2ω/ℓ. Rankin with
σ ∈ (0, ½]: L ≤ N^{σ/2}∏_ℓ(1 + 2ω(ℓ)ℓ^{−1−σ}) ≤ N^{σ/2}exp(2Σ_ℓ ω_∞(ℓ)ℓ^{−1−σ}). Each class comes from a triple
with q_τ := 4c₀d₀ | ℓ + 1 and ℓ > 4V(τ) ≥ q_τ, so
Σ_ℓ ω_∞(ℓ)ℓ^{−1−σ} ≤ Σ_τ Σ_{n ≡ −1 (q_τ), n > 4V} n^{−1−σ} ≤ Σ_τ 2(4V)^{−σ}/(σq_τ) ≤ σ^{−1}Σ_τ V(τ)^{−σ}/(c₀d₀).
The last sum is the Euler product ∏_{s odd}(1 + s^{−1−σ} + s^{−1−2σ}/(1 − s^{−2σ})) (s | d₀; or s | c₀ with
v_s(R) = ρ ≥ 0, weight s^{−1−2σ(1+ρ)}). Its logarithm is ≤ Σ_s s^{−1−σ} + Σ_s log(1 + 1/(2σ s log s)) (using
s^{2σ} − 1 ≥ 2σ log s) ≤ log(1/σ) + O(1) + Σ_{s≤1/σ}[log 2 + log(1/(σs))] + (2σ)^{−1}Σ_{s>1/σ} 1/(s log s)
≤ log(1/σ) + C/(σ log(1/σ)) (PNT: Σ_{p≤y} log(y/p) = ∫₁^y π(t)dt/t ≪ y/log y; Σ_{p>y} 1/(p log p) ≪ 1/log y).
Hence log L ≤ (σ/2) log N + exp(C′/(σ log(1/σ))) for σ ≤ σ₀. Take σ := 2C′/(λ log λ): then
C′/(σ log(1/σ)) = λ log λ/(2 log(λ log λ/(2C′))) ≤ 0.6λ for large N, so log L ≤ C′ log N/(λ log λ) + (log N)^{0.6}. ∎
*Remarks.* (a) Where the mass sits: the optimum of Thm 2.1 at κ ≍ λ uses X = exp(≍ λ² log λ) and moduli
4m ≤ exp(≍ λ log λ); the dual Rankin parameter σ ≍ 1/(λ log λ) is the reciprocal of log(modulus). (b) The ceiling
is about the large-sieve bound L, not about the true exceptional set: heuristically the probability of avoiding all
cube classes at ℓ ≤ N^{1/2} is ≈ exp(−S_∞(N^{1/2})) = exp(−exp(c√(log N/log₂N))) (de Bruijn's Σ 1/rad), far below
the sieve's output. The sieve's loss is structural (B6 made quantitative): one prime ℓ per factor of q, each
contributing only ω(ℓ)/ℓ = ℓ^{−1+o(1)}. (c) Scope: prime moduli. Composite moduli (3/4-note multipliers) add
dimension at bounded e (§5) but do not change log S by more than O(log u) at e ≍ λ, so the ceiling's order should
persist (Assessment).

**Remark 3.2 (R237 repair D1: the untruncated family beats the "ceiling"; (a) PROVED, elementary; (b) reviewer sketch).** Prop 5.1 (and
CAP_GROWING Prop 1.3) certify every class −4D mod ℓ with D ∈ 𝒟_e(ℓ), with NO size condition on D. For ℓ ≡ 11 (mod 12),
3 | K = (ℓ+1)/4, so D = 9^j ∈ 𝒟_∞(ℓ) for all j ≥ 0 (and ∈ 𝒟_e(ℓ) for j ≤ e + v₃(K)); these give ord_ℓ(9) ≥ ord_ℓ(3)/2
distinct classes. The primes ℓ ∈ (y, 2y] with ord_ℓ(3) ≤ T divide ∏_{j≤T}(3^j − 1), so there are ≤ T² log 3/(2 log y) of
them; with T = y^{1/2}/log y almost all ℓ ≡ 11 (12) in (y, 2y] have ω(ℓ) ≥ ℓ^{1/2}/(2 log ℓ). (a) e = ∞: the single-prime
part of L already gives L ≥ Σ_{ℓ ≤ N^{1/2}, ℓ ≡ 11 (12)} ω(ℓ)/ℓ ≫ N^{1/4}/log²N, so the prime-modulus large sieve with
the full family yields #{p ≤ N : ES^{(y)}(p) fails} ≪ N^{3/4} log²N — a POWER saving (of course ES^{(y)} is a theorem;
the point is that Thm 3.1's "ceiling" is a property of the truncation, not of the architecture). Numerically ω(ℓ) =
(ℓ−1)/2 for most ℓ ≡ 11 (12) and Σ_{ℓ<3·10⁵} ω/(ℓ−ω) ≈ 5900 ≍ Q/log Q (R237 `scripts/review_r237_fullfamily.py`).
(b) e ≥ (log N)^{1+ε} (reviewer sketch): ω(ℓ) ≥ e + 1 for almost all ℓ ≡ 11 (12) in (e³, 2e³]; with q = products of
k ≍ log N/(6 log e) such primes, log(S/k) ≫ ε log log N, so log L ≫_ε log N: again a power saving.
(c) OPEN: whether the ceiling log N/(log₂N log₃N) persists for the full 𝒟_e(ℓ) when log log N ≤ e ≤ (log N)^{1+ε}
(for finite e the full family is finite, |𝒟_e(ℓ)| ≤ ∏_{s^σ∥K}(2σ+1+e), but its members are not < ℓ/4, so the
proof of Thm 3.1 (which uses ℓ > 4V) does not apply as written).

## 4. The pointwise side: the minimal cap e*(n), and where it meets the sieve

Define **e*(n)** := min{e : ES^{(y,e)}(n) has a solution} ∈ ℤ_{≥0} ∪ {∞}. ES(n) ⟺ e*(n) = 0; FROBENIUS_FIRING
Thm 4.2 gives e*(n) < ∞ for every odd n > 1 (ineffective: no bound in terms of n). PHASE_DIAGRAM Thm 5.1 is a
*family-form* statement (for fixed n, solutions at every large scale y with e ≤ y^{o(1)}); it bounds e*(n) only by
the ineffective x₀(n)^{o(1)}. The almost-all statements of §2 are bounds on #{p ≤ N : e*(p) > e}.

**Proposition 4.1 (covering barrier at the log log scale; PROVED, elementary + EXPONENT_CAP Prop 3.1(c)).** For
infinitely many primes p, every shot certificate (Q, r) of p with PRIME modulus r has r > log p/C′; hence any argument that
proves ES^{(y,e)}(p) by *covering* (F_r^*)² with the cap-e box at a single certifying prime r (EXPONENT_CAP Prop 3.1)
needs e ≥ (log r)^{1−o(1)} ≥ (log log p)^{1−o(1)} for these p.
*Proof.* A shot (Q, r) with r prime needs (−p/r) = 1 with r ≡ 3 (4), i.e. (p/r) = −1 for p ≡ 1 (4). Let
W := 8∏_{3≤r≤R} r; by Dirichlet/Linnik there are primes p ≡ 1 (mod W) with log p ≤ C log W ≤ C′R; for them
(p/r) = (1/r) = 1 (as p ≡ 1 mod r) for all odd r ≤ R, so every certifying prime is > R ≥ log p/C′. (Linnik: C′ absolute; log W = (1+o(1))R by the PNT.) The cap
bound is Prop 3.1(c) of EXPONENT_CAP (box ∏(κ_i + e + 1) ≥ (r−1)/2 with ∏ s^{κ_i} ≤ r). ∎
*Reading.* The almost-all saturation scale of §2 (e ≍ log log N; for the truncated class family — R237 repair D5) and the pointwise covering threshold
((log log p)^{1−o(1)}, for some p) are the SAME scale. So "ES^{(y, C log log p)} for every prime p" is the natural
pointwise target where the two sides meet (CONJECTURE-level target; numerically trivial, since e*(p) = 0 for all
tested p by ES itself).

**Theorem 4.2 (pointwise cap under GRH; CONDITIONAL on GRH for the Dedekind zeta functions of the fields
L = ℚ(ζ_{4P}, √p, ζ_m, s₁^{1/m}, …, s_k^{1/m}); proof at citation level (Hooley/Lenstra + Lagarias–Odlyzko), to be
hostile-reviewed).** There is an absolute C such that for every prime p,
`  (a) e*(p) ≤ C_ε (log p)^{2+ε}        (k = 1, S = {3}, p ≠ 3; every ε > 0);`
`  (b) e*(p) ≤ exp(C √(log log p · log log log p))      (k ≍ √(log₂p/log₃p) mute primes).`
*Proof sketch.* p ≡ 3 (4): e* = 0 (shot Q = 1). Let p ≡ 1 (4); S = first k odd primes ≠ p, P = ∏S. Count primes
r ∈ (x/2, x] with (i) r ≡ −1 (mod 4P), (ii) (p/r) = −1, (iii) for no odd prime q | r − 1 are all s ∈ S q-th powers
mod r, (iv) λ₁(Λ_r) > B (k ≥ 2 only; Λ_r as in PHASE_DIAGRAM Thm 5.1). For such r: each s is a QR (as in
FROBENIUS_FIRING Thm 4.2), so (iii) gives ⟨S⟩ = (F_r^*)², and (ii) makes −p/4 a square; hence r | p + 4Q² with
Q ∈ ⟨S⟩, rad Q | (r+1)/4, and the overflow exponents are ≤ v_s(Q). For k = 1 take Q = s^a, a < (r−1)/2: e ≤ r/2.
For k ≥ 2 Minkowski II gives exponents ≤ 2kλ_k ≤ 2k·x/B^{k−1} (PHASE_DIAGRAM Thm 5.1 Step 4).
Counting (Hooley's scheme, GRH): *small q ≤ ξ₁ = ε′ log x*: inclusion–exclusion over m | ∏_{q≤ξ₁} q, 2^{π(ξ₁)} ≤ x^{ε′}
fields, each with |C| = 1 and Lagarias–Odlyzko error ≪ √x log(pPmx); main term δ·x/(φ(4P)·2·log x) with
δ = ∏_{q≤ξ₁, q∤2P}(1 − 1/(q^k(q−1))) ≥ 0.3 (linear disjointness as in FROBENIUS_FIRING Thm 4.4; m sharing a prime with
the conductor of ℚ(√p) only kills terms). *Medium q ∈ (ξ₁, ξ]*: upper bound #{r ≡ −1 (4P) split in ℚ(ζ_q, s₁^{1/q})}
≤ li(x)/(φ(4P)q(q−1)) + O(√x log(Pqx)) — no p-dependence. *Large q > ξ*: k = 1: Hooley (BT on (ξ, √x log x], and
r | s^t − 1 with t ≤ √x/log x beyond), total ≪ x log₂x/log²x; k ≥ 2: index ≥ ξ ⇒ |Γ_r| ≤ x/ξ, and
#{r : |Γ_r| ≤ Y} ≤ 6^k Y^{1+1/k}·3 log P (PHASE_DIAGRAM Thm 5.1 Step 2). *(iv)*: #{r : λ₁ ≤ B} ≤ (3B)^{k+1} log P.
Parameters. (a) k = 1, P = 3: main ≍ x/log x; the small range needs x^{1/2−ε′} ≫ log p·log²x, i.e. x ≥ C_ε(log p)^{2+ε};
the medium/large ranges are p-free (they need only ξ₁ log ξ₁ ≫ 1/δ and log x ≫ log₂x/δ). So r ≤ C_ε(log p)^{2+ε}, e ≤ r/2. (b) ξ := √x/(P log³x): medium error ≪ x/(φ(P) log² x);
large range needs (x/ξ)^{1+1/k}6^k log P ≪ x/(φ(P) log² x), true when log x ≥ C k log k (as P = e^{(1+o(1))k log k});
B := (x/(P log³x))^{1/(k+1)}/3. Small range: x ≥ (P log p)^{2.1}. Take log x := 2.1(log₂p + log P) + Ck log k with k := ⌊√(log₂p/log₃p)⌋:
log x ≍ log₂p, and x/B^{k−1} = x^{2/(k+1)}(P log³x)^{(k−1)/(k+1)}3^{k−1}, so
e ≤ 2k·x/B^{k−1} ≤ exp(2 log x/(k+1) + O(k log k)) = exp(O(√(log₂p·log₃p))). ∎
*Remarks.* (1) Min-form vs family-form: (b) bounds the SMALLEST solution's cap (y ≈ p·(log p)^{O(1)}, so also
e ≤ exp(O(√(log₂y log₃y)))). In family form (scale y → ∞ at fixed p) the same argument gives only
e ≤ exp(O(√(log y·log₂y))) — PHASE_DIAGRAM Thm 5.1 Remark (2)'s prediction, now under GRH; the cell
"ES^{(y,polylog)}" (family form) stays OPEN even under GRH by this method. (2) General odd n: the same with S =
first k odd primes not dividing n; (a)/(b) hold with log p replaced by log n as long as P(n) := ∏S stays
≤ (log n)^{O(1)} (resp. e^{O(k log k)}); for n divisible by all primes ≤ w, S must start above w (Def 1.1 forbids
mute primes dividing n), and the bound degrades — the same issue as R210 m8. (3) Unconditionally nothing of this
shape is known: Thm 4.2 of FROBENIUS_FIRING needs BV/Siegel–Walfisz at modulus 4 rad(n)P, i.e. x ≥ exp(n^{ε}).
**The gap.** GRH pointwise: exp(O(√(log₂p log₃p))); covering barrier: (log₂p)^{1−o(1)} i.o.; unconditional
almost-all: e ≍ log₂N leaves ≤ N^{1 − c/(log₂N log₃N)} exceptions (Thm 2.1), and the large sieve with truncated classes
cannot do better at any cap (Thm 3.1); with the untruncated family see Remark 3.2 (R237 repair D5).

## 5. The exact class family 𝒟_e(M): the cube is redundant, the cap adds exactly e dimensions (goals 2, 3)

**Proposition 5.1 (exact dictionary at any modulus; PROVED, elementary).** Let M ≡ 3 (mod 4) (prime or composite),
A := (M+1)/4, D ≥ 1, p a prime with p ∤ DM and **p ≡ −4D (mod M)**. Put E := (p + 4D)/M,
`  x := (p + E)/4,   y := pA,   z := p·x·A/D.`
Then x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0} and 4/p = 1/x + 1/y + 1/z. This is an ES^{(y,e)}(p) solution iff **D ∈ 𝒟_e(M)**:
`  rad D | A,  and for every prime s | D with t := v_s(D), σ := v_s(A):  t ≤ 2σ,  or (s odd, t even, t ≤ 2σ + 2e).`
In particular 𝒟_0(M) = {D : D | A²}, which is exactly the ES class family ℛ(M) = {−4D : D | A²} of the 3/4 note
(§"ceiling"); and the overflow cube (c₀R², d₀/R², j) of CAP_GROWING is the parametrisation D = c²d = c₀²d₀R²:
**the solution depends only on D, so (c, d, j) is a redundant coordinate system and "further overflow parameters"
R₁, R₂, … can only produce further D's of 𝒟_e(M).**
*Proof.* E ∈ ℤ; M ≡ 3 (4) gives E ≡ −(p + 4D) ≡ −p (mod 4), so 4 | p + E. x + D = (p + E + 4D)/4 = E(M+1)/4 = EA,
hence 1/y + 1/z = (x + D)/(pxA) = E/(px) = 4/p − 1/x. Valuations at s | D (s ≠ p; s ∤ M, since s | M and M | p + 4D
would give s | p): v_s(E) = 0 (EM ≡ p mod s). If σ = 0 then v_s(x) = v_s(EA − D) = 0 and v_s(z) = −t < 0 while
s ∤ y = pA: forbidden. If 1 ≤ σ < t: v_s(x) = σ (v_s(EA) = σ < t), v_s(z) = 2σ − t; this is ≥ 0 iff t ≤ 2σ, and
otherwise Def 1.1 asks t even (s = 2 is never allowed in den z) and 2σ − t ≥ −2e. If t ≤ σ: v_s(x) ≥ t and
v_s(z) ≥ σ ≥ 0. Primes s ∤ D have v_s(z) ≥ 0. And s | den z ⇒ s | A | y. ∎
*Check (`scripts/z10_rfamily_check.py`, data/z10/rfamily_check.txt):* random M < 3·10⁵ (half of them with
9·25-type square factors in A, i.e. σ ≥ 2), random D in and outside 𝒟_e(M) (exponents up to 2σ + 2e + 2, plus
foreign primes), random prime p ≡ −4D: the predicate "D ∈ 𝒟_e(M)" agreed with Def 1.1 (exact rationals) in
**3000/3000 cases at e = 2 and 2000/2000 at e = 0**. (`z10_cube_check.py`: 2000 cube solutions with exactness
violated in 486 cases, composite M in 1505, all valid — Remark 1.3.)

*T1 (PROVED).* For D ∈ 𝒟_e(M), (−D/M) = −1 (Jacobi): write D = f²d, d squarefree; d | A (odd parts of t > 2σ are
even, so the squarefree part comes from t ≤ 2σ ⇒ d | A); for odd q | d, M ≡ −1 (q) and reciprocity give (q/M) = 1;
2 | d forces 8 | M + 1, (2/M) = 1; so (−D/M) = (−1/M) = −1. Hence no class −4D contains a square (any e, any M):
`scripts/z10_t1.py 3000 3`: all 7820 classes with M < 3000, e = 3, exhaustively — 0 contain a square.

**Corollary 5.2 (supply dimension; PROVED, elementary).** Let F_e(M) := #{D ∈ 𝒟_e(M) : 4D < M} (distinct classes
−4D mod M). The local count at a prime s ∥^σ A, s odd, is N(σ, e) = 2σ + 1 + e (t ∈ [0, 2σ] ∪ {2σ+2, …, 2σ+2e}), so
`  Σ_{M≤Q, M≡3 (4)} F_e(M)/M ≍_e (log Q)^{e+3},     Σ_{ℓ≤X prime} F_e(ℓ)/ℓ ≫_e (log X)^{e+2}.`
*Proof.* Upper: F_e(M) ≤ ∏_{s^σ∥A} N(σ, e) (N(σ,0) := 2σ+1 at s = 2), and Σ_{A≤Q} ∏N(σ,e)/A ≪ (log Q)^{e+3} (the
Dirichlet series is ζ(w)^{e+3}·H(w), H absolutely convergent near w = 1). Lower: swap sums, Σ_D Σ_{A≤Q, A > D,
core conditions} 1/A over D ≤ √Q with D = c₀²d₀R² (c₀, d₀ odd squarefree coprime, rad R | c₀, v(R) ≤ e), for which
c₀d₀ | A suffices: ≥ ½ log Q·Σ_{D≤√Q} 1/(c₀d₀) ≫ (log Q)^{e+3}. Prime moduli: Prop 1.2 / CAP_GROWING Thm 1.4. ∎
*Answers.* (i) **No unbounded tower of overflow dimensions at fixed e** (goal 2): within the shot form y = pA every
ES^{(y,e)} certificate at every modulus is a class of 𝒟_e(M), whose total supply has dimension exactly e + 3 (upper
bound above). Several overflow parameters are reparametrisations of D. (ii) Exponent table (prime-modulus large
sieve / composite multipliers à la 3/4 note / mass-driven CRT ceiling):
`  e:                  0      1      2      e`
`  prime-modulus LS:   2/3    3/4    4/5    (e+2)/(e+3)    PROVED (CAP_GROWING Thm 1.4; Thm 2.1 uniform)`
`  3/4-note multipliers: 3/4  4/5    5/6    (e+3)/(e+4)    Assessment: only the class supply changes (Cor 5.2)`
`  KARY3-type ceiling:  3/4    4/5    5/6    (e+3)/(e+4)    Assessment (KARY3 itself does NOT apply for e ≥ 1)`
KARY3 / LARGESIEVE3–4 / the sieve-limits note cap mixtures of ℛ(M), (a,D), Case-A and selector classes; 𝒟_e(M) ⊋
𝒟_0(M) = ℛ(M) for e ≥ 1 (odd even-excess exponents), so those theorems do not apply to ES^{(y,e)} — exactly why
Thm 1.4 can exceed 3/4 at e = 2 without contradiction (R230 D1). Their proofs are mass-driven (θ = 𝓑/(𝓑+1) with
mass (log)^𝓑), so the analogue with 𝓑 = e + 3 is expected (Assessment, not re-proved). (iii) At e ≥ c log log N the
supply is no longer polylogarithmic and the ceiling is Thm 3.1's log N/(λ log λ) (prime moduli; composite: Assessment).

**Proposition 5.3 (what e = 0 lacks: the extra dimensions are exactly non-integrality of z; PROVED, from Prop 5.1).**
For D ∈ 𝒟_e(M): z ∈ ℤ_{(s)} for all s iff D | A². The e additional local values t ∈ {2σ+2, …, 2σ+2e} are precisely
those with v_s(z) = 2σ − t < 0. So at e = 0 the family is 𝒟_0 = ℛ(M) with no hidden overflow, and every integral
solution of this shape is in ℛ(M).
*Reading (Assessment, goal 3).* "R must be 1 at e = 0" is not a technical artefact: the overflow dimension IS the
non-integrality. An overflow "into x" is impossible in this family (x = EA − D is always integral); a family with
x ∉ ℤ is a different relaxation, not ES. For ES itself the full supply of integral solutions (Type I and II) has
average count ≍ log³ p (Elsholtz–Tao Thm 1.1), and KARY3 caps every CRT architecture over ℛ(M), (a,D), Case-A,
selector classes at 3/4: there is no fourth dimension to unlock at e = 0 inside CRT architectures. Escaping needs
non-CRT input (STATUS "Exceptional-set exponent": tuple counts TC^alt, weights < 1, residue-dense (A*)) — none
supplied by the cap.

## 6. PM-SQ_± to 10⁷ (goal 4) and the numerics ledger

**PM-SQ_± (CONJECTURE, EVIDENCE extended).** `scripts/z10_sqpm.c` (C; least |u| with an odd prime ℓ | n + u,
|u| | ℓ ± 1, (−u/ℓ) = −1 — CAP_GROWING Lemma 3.1): **all 1 248 419 non-squares n ≡ 1 (mod 8), n ≤ 10⁷, have a
prime-modulus χ = −1 word with |u| ≤ 41; 0 exceptions; all 1580 odd squares ≡ 1 (8) unfired (T1).**
Least-|u| histogram: 1: 833 904, 2: 349 852, 3: 53 078, 4: 5555, 5: 2618, 6: 2497, 7: 333, 8: 203, 9: 91, 10: 159,
11: 42, 12: 21, 13: 5, 14: 28, 15: 15, 16: 3, 18: 5, 19: 4, 21: 1, 23: 1, 24: 2, 27: 1, **41: 1 (n = 8 452 161)**.
To 10⁶ the max is 19 (n = 33 201; O229's "max |u| 10" was a 300-sample). Independent check (sympy, exact word
identity tuv − u − v = n and Jacobi (−A/n) = −1): n = 33 201 → least u ∈ {19, 20}; n = 8 452 161 → word
(t, u, v) = (4, 41, 51 854), A = 163, χ = −1. *Reading (Assessment).* The record least |u| grows slowly (19 → 41
from 10⁶ to 10⁷); the tail P(least |u| > U) is roughly geometric in the number of usable slots, consistent with
O229's heuristic that no finite u-set suffices (Dickson-type), while exceptions stay absent.

**Numerics ledger (all EVIDENCE; exact rational identities wherever a solution is produced).**
* `z10_cube_check.py 400000 2000 4 3`: 2000 overflow-cube solutions (1505 at composite M, 486 violating O229's
  exactness hypothesis), all valid ES^{(y,4)} (Remark 1.3, §5).
* `z10_rfamily_check.py` (random, e = 2 / 0) and `z10_rfamily_exh.py 1200 e` (**exhaustive: all M ≡ 3 (4) < 1200, all
  D < M/4 coprime to M, e = 0, 1, 3: 36 458/36 458 agreements each**): "D ∈ 𝒟_e(M)" ⟺ Def 1.1 (Prop 5.1).
* `z10_t1.py 3000 3`: no 𝒟_e class contains a square (7820 classes, exhaustive).
* `z10_mass.py 4000000 6`: prime-modulus supply S_e(X) (V < ℓ/4, no cuts), X = 2^{10} … 4·10⁶, e = 0…6, ∞:
  `X = 2^20: 5.06 5.83 6.12 6.22 6.25 6.25 6.25 | ∞ 6.25     X = 4·10^6: 5.84 6.87 7.30 7.47 7.53 7.54 7.54 | ∞ 7.54`
  — at these X the knob saturates at e ≈ 4–5 ≈ log X/(2 log 3)/… (the cap is invisible once 9^{e+1} > ℓ); this is the
  small-X shadow of Remark 2.2(b) — and an artefact of the truncation V < ℓ/4 (R237 repair D1: without it, the e = ∞
  supply at ℓ ≡ 11 (12) is typically (ℓ−1)/2, Remark 3.2).
* `z10_leastmod.py 1000000 3000`: least prime certifying modulus ℓ ≤ 3000 of 𝒟_e, all 78 496 primes 5 ≤ p ≤ 10⁶:
  uncovered 1654 (e = 0), 1502 (e = 1), 1499 (e ≥ 2); odd squares hit: 0 for every e (T1).
* `z10_grh_r.py 1000000 40`: the Thm 4.2(a) certifying prime (least r ≡ 11 (12), (p/r) = −1, ⟨3⟩ ⊇ squares) is ≤ 251 for
  all primes p ≡ 1 (4) below 10⁶ (max r/log²p = 8.9, at p = 5); adversarial p ≡ 1 (mod 8∏_{3≤q≤40} q) (log p ≈ 31–34):
  r = 47 or 71; 391 + 5 shot solutions Q = 3^a verified exactly (den z a power of 9).

## 7. Verdict (O234 checkpoint 1)

1. **Uniformity (Thm 2.1, PROVED rel. Gallagher's PNT + BV + large sieve):** ES^{(y,e)} fails for
   ≤ N exp(−c(log N)^{(e+2)/(e+3)}/((e+2)log(e+3))) primes, uniformly in 0 ≤ e ≤ log log N: c_e ≍ 1/(e log e).
   Saturation at e ≍ log log N: exceptions ≤ N exp(−c log N/(log₂N log₃N)).
2. **Ceiling (Thm 3.1, PROVED, elementary):** the prime-modulus large sieve with cube classes TRUNCATED to V < ℓ/4 gives
   no better at any cap. (R237 repair D1: without the truncation — which the architecture does not require — the
   e = ∞ family gives a power saving N^{3/4+o(1)}, as does e ≥ (log N)^{1+ε}; Remark 3.2. The range
   log log N ≤ e ≤ (log N)^{1+ε} is OPEN for the full family.) The sieve never meets "all n ≥ n₀".
3. **Pointwise (§4):** covering barrier e ≥ (log log p)^{1−o(1)} for infinitely many p (Prop 4.1, PROVED) — the same
   scale as the sieve saturation; under GRH e*(p) ≤ C_ε(log p)^{2+ε} and e*(p) ≤ exp(O(√(log₂p log₃p)))
   (Thm 4.2, CONDITIONAL, citation-level proof sketch). Unconditionally no bound of e*(n) in terms of n is known.
4. **Exact family (Prop 5.1, PROVED):** at every modulus M ≡ 3 (4) the ES^{(y,e)} certificates of shot shape are the
   classes −4D, D ∈ 𝒟_e(M) (D | A² lifted by even excess ≤ 2e); the cube is a redundant parametrisation; supply
   dimension exactly e + 3 (Cor 5.2) — no tower at fixed e; composite-multiplier exponent (e+3)/(e+4) and its CRT
   ceiling are Assessments (KARY3 does not literally apply for e ≥ 1). At e = 0 the family is ℛ(M): the extra
   dimensions are exactly non-integrality of z (Prop 5.3).
5. **PM-SQ_±:** 0 exceptions to 10⁷, record least |u| = 41.
ES untouched; no infinite case of ES is claimed.
