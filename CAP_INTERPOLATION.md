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
the overflow-cube classes at ANY cap, including e = ∞ (Thm 3.1). So the knob saturates at e ≍ log log N, and the
sieve side never reaches "all n ≥ n₀" — not even for ES^{(y)} = e = ∞, which is a pointwise THEOREM.
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
T = Σ(ω_e/ℓ)² ≤ X^{−3/10}S. If S ≥ k² then L ≥ S^k/(2k!) ≥ ½(S/k)^k.
*Choice of u.* Write A_κ := 2 log κ + log log(κ+2) + C₄ (C₄ ≥ log(40(C₂+1)), so u ≥ e^{A_κ} meets the hypothesis of
Prop 1.2) and set log u := A_κ + 1 + λ/(κ+1), i.e. u = e^{C₄+1}κ² log(κ+2)·(log N)^{1/(κ+1)}. Prop 1.2 gives
log S ≥ κ(log u − A_κ) ≥ κ, and log k ≤ λ − log(2u), so
`  log(S/k) ≥ (κ+1) log u − κA_κ − λ = A_κ + κ + 1 ≥ κ + 1.`
*Collisions.* T ≤ max_ℓ(ω_e(ℓ)/ℓ)·S ≤ X^{−3/10}S, so (k choose 2)T S^{k−2} ≤ ½S^k once k² ≤ X^{3/10}, i.e. u ≥ 7λ: for
κ + 1 ≤ λ/log(7λ) this follows from u ≥ (log N)^{1/(κ+1)}, otherwise from u ≥ e^{C₄}κ² ≥ e^{C₄}λ²/log²(7λ).
Hence L ≥ S^k/(2k!) ≥ ½(S/k)^k and log L ≥ (κ+1)k − 1. With k ≥ log N/(2u) − 1:
`  log L ≥ (κ+1)(log N)^{κ/(κ+1)}/(2e^{C₄+1}κ² log(κ+2)) − (κ+2) ≥ c (log N)^{κ/(κ+1)}/(κ log(κ+2))`
(the subtracted κ + 2 ≤ λ + 4 is of lower order for κ ≤ λ + 2). Primes ≤ X number ≤ e^u with
u ≤ e^{C₄+2}λ² log λ = (log N)^{o(1)}, negligible; and u ≤ log N/4, so k ≥ 1. ∎
*Remark 2.2.* (a) **c_e ≍ 1/(e log e)** — polynomial decay, not ((e+1)(e+2))^{−e} (O229's Thm 1.2 calibration: an
artefact of BV's divisor weights and of restricting every coordinate to X^{1/(5(2e+3))}). (b) The saving
(log N)^{κ/(κ+1)}/(κ log κ) = log N·exp(−λ/(κ+1))/(κ log κ) is maximal at κ ≍ λ, with value ≍ log N/(λ log λ):
**the knob saturates at e ≍ log log N.** (c) The d₀-coordinate is included in κ = e + 2; Vaughan's prime-modulus
case is κ = 2 (e = 0), exponent 2/3. (d) T1: all classes are QNRs mod ℓ (CAP_GROWING Thm 1.4 T1, which does not use
exactness), odd squares are never hit; the bound is consistent with the ≍ √N odd squares ≤ N.

## 3. The ceiling: the prime-modulus large sieve cannot beat log N/(log₂N·log₃N), at any cap

Let ω_∞(ℓ) be the number of distinct classes −4V(τ) mod ℓ over ALL cube triples τ at ℓ (any cap, V(τ) < ℓ/4) — the
largest class family of this architecture; every capped/truncated family is a subfamily.

**Theorem 3.1 (ceiling; PROVED, elementary: Rankin + Mertens + PNT).** There is an absolute C such that for N ≥ 16
and any choice of ω(ℓ) ≤ ω_∞(ℓ) classes (from the cube family) at the primes ℓ ≤ N^{1/2}, ℓ ≡ 3 (4):
`  log L ≤ C log N/(log₂N·log₃N),   L := Σ_{q≤N^{1/2}} μ²(q) ∏_{ℓ|q} ω(ℓ)/(ℓ − ω(ℓ)).`
So the large-sieve bound 2N/L for ES^{(y,e)} is ≥ N exp(−C log N/(log₂N log₃N)) for every e ≤ ∞: Theorem 2.1 is
optimal for this architecture up to the constant, and **no cap — not even e = ∞ — gives a power saving, let alone
"all p ≥ p₀"**, although ES^{(y,∞)} = ES^{(y)} is TRUE for every p (FROBENIUS_FIRING Thm 4.2).
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
(p/r) = (r/p)… = (p mod r / r) = 1 for all odd r ≤ R, so every certifying prime is > R ≥ log p/C′. (With Linnik the
constant C′ is absolute; "(1 − o(1)) log p" needs p ≤ W^{1+o(1)}, available for a positive proportion of R by
Bombieri–Vinogradov — I state the weaker log p/C′, which suffices for the (log log p)^{1−o(1)} claim.) The cap
bound is Prop 3.1(c) of EXPONENT_CAP (box ∏(κ_i + e + 1) ≥ (r−1)/2 with ∏ s^{κ_i} ≤ r). ∎
*Reading.* The almost-all saturation scale of §2 (e ≍ log log N) and the pointwise covering threshold
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
almost-all: e ≍ log₂N leaves ≤ N^{1 − c/(log₂N log₃N)} exceptions (Thm 2.1), and the large sieve cannot do better at
any cap (Thm 3.1).
