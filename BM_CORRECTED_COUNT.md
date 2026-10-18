# BM_CORRECTED_COUNT — the Brauer–Manin-corrected count for (★) and its remainder (task O268)

Status: O268 working draft. **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z38_*`, memos `BRAINSTORM/z38_*.md`, tiny logs `logs/z38_*`.
Builds on SINGLE_P_COUNT (O260: pair form, genus split R = M_gen + X, Prop 4.1), Bright–Loughran arXiv:1908.02526 (BL),
PARITY_AUDIT Lemma 3.2 (χ-shadow), B1_LINE Lemma 1.2 (pair genus law), CONDITIONAL_ES Props 2.3, 3.1, 7.3.

## 0. Summary
* §1 (PROVED) **BL's quaternion class = one Kronecker character per pair.** At the rational point P_{u,B} of each (★)-pair,
  inv_p α = χ_{−4uB}(p) = (−uB/p), and χ_{−4uB}(−(u+B)) = −1 identically; principal + χ_{−4uB} in the orthogonality expansion
  is φ(q)^{−1}(1 + inv_∞ inv_p) — a factor of Borovoi–Rudnick *shape* at integral points (no BR theorem applies to U_n, which is not a homogeneous space; at non-hits a heuristic replacement) (R279 repair). The arithmetic of (1),(2),(4) is classical (Yamamoto's condition; BL Cor 1.3; ET Prop 1.6); new is only the expansion reading (3) (R279 repair). O260's "genus indicator = BM invariant" is false (genus = all
  s(q) real characters; BM = exactly one of them). Same on full Type II (χ_{−4ab}), the b = 1 line (χ_{−4xy}), m/n (§4).
* §2 (PROVED) the BM-corrected singular series M_BM(p) = Σ(1 − (−uB/p))/φ(4uB) is ≥ 0, mean-preserving, 0 at squares, and
  **≥ (3/(16π²) − o(1))(log p)² unconditionally** (Burgess; 1/(32π²) with PV); ∼ M₀ ∼ (3/(2π²))(log p)² under GRH
  (board F4 obligation (i), derived).
* §3 (PROVED) two-sided remainder bounds |R − M| ≤ (log p)^{O(1)} (incl. O260's H_X with M_gen) are false infinitely often
  (Linnik). Exact conditional: (★) for p > p₀ (ES for all n given the census below an explicit p₀; R279 repair) ⟸ H⁻_BM: R(p) ≥ εM_BM(p) — no other input; not refuted by T1; no implication
  from a standard conjecture established; ES-(★) in disguise up to ε. EVIDENCE to 10⁶ (all primes, all odd n): zero rate
  ≈ 2× swap-Poisson at fixed M, far tail possibly fatter; Markoff precedent (Loughran–Mitankin Thm 1.5): infinitely many
  integral Hasse failures with non-empty BM set there.
* §4 b = 1 / union: same Brauer character, residuals positively correlated overall; 8/n control passes.
* **ES is not solved; no conditional theorem from a standard conjecture.**

Notation (SINGLE_P_COUNT §1–2). For odd n ≥ 3, 𝒫(n) = {(u, B) ∈ ℕ² : gcd(u, B) = 1, u + B odd, 4uB − u − B ≤ n},
q = 4uB, a = −(u + B) (a unit mod q), R*(n) = Σ_{𝒫(n)} 1[n ≡ a (mod q)] (= R(n), the (★) count, for n prime).
(★) solutions give 4/n = 1/(uBC) + 1/(nBC) + 1/(nuC), C = (n + u + B)/(4uB).

## 1. The dictionary: BL's quaternion class is ONE quadratic character per pair, χ_{−4uB}

For a pair (u, B) and odd n put C := (n + u + B)/(4uB) ∈ ℚ (no integrality) and
P_{u,B} := (x, y, z) = (uBC, nBC, nuC) ∈ U_n(ℚ), U_n : 4xyz = n(xy + xz + yz) (BL (1.2)); P_{u,B} lies in U_n(ℝ)⁺. BL's
generator α = (−x/z, −y/z) of Br U_n/Br ℚ ≅ ℤ/2 (BL Thm 1.6) evaluates on this point family to the constant-coefficient
algebra α(P_{u,B}) = (−B/n, −B/u) (x/z = B/n, y/z = B/u). Let χ_{−4uB} = (−4uB/·) be the Kronecker character: a real,
odd (χ(−1) = −1), non-trivial character modulo q = 4uB.

**Theorem 1.1 (PROVED).** Let n ≥ 3 be odd and (u, B) ∈ 𝒫(n).
1. (local invariants) inv_∞ α(P_{u,B}) = −1; inv_ℓ α(P_{u,B}) = +1 for every prime ℓ ∤ 2nuB; inv_2 α(P_{u,B}) = +1
   whenever C is 2-integral. If n = p is prime (p ∤ uB automatically), inv_p α(P_{u,B}) = (−uB/p) = χ_{−4uB}(p).
2. (value at the target) χ_{−4uB}(a) = χ_{−4uB}(−(u + B)) = −1.
3. (the BM factor in the character expansion) for gcd(n, q) = 1, the contribution of the pair of characters {1, χ_{−4uB}}
   to the orthogonality expansion 1[n ≡ a (q)] = φ(q)^{−1} Σ_{χ (q)} χ(n)χ̄(a) is
   φ(q)^{−1}(1 − χ_{−4uB}(n)), and for n = p prime this equals φ(q)^{−1}(1 + inv_∞ α(P_{u,B})·inv_p α(P_{u,B})).
   Hence for (★) hits (an integral point; then inv_ℓ = 1 at all ℓ ≠ p, ∞ by BL Lemmas 3.5, 3.8) BL's Thm 1.2
   (∏_{ℓ | n} inv_ℓ = −1) is exactly the statement χ_{−4uB}(p) = χ_{−4uB}(a), i.e. the Brauer character is the
   unique character in the expansion whose value at the target class is forced by the BM obstruction.
4. (T1) If n = m² then χ_{−4uB}(n) = +1 for every pair with gcd(n, q) = 1, so the pair term 1 − χ_{−4uB}(n) vanishes
   identically: the BM factor alone kills every pair at every odd square.

*Proof.* (1) inv_∞: −B/n < 0 and −B/u < 0, so (−B/n, −B/u)_∞ = −1. For ℓ ∤ 2nuB both entries are ℓ-adic units, so
the tame symbol is trivial. At 2, if C is 2-integral then x, y, z ∈ ℤ₂ and P_{u,B} ∈ U_n(ℤ₂), where inv₂ = 1 by BL Lemma
3.8 (n odd). At ℓ = p ∤ uB: −B/u is a p-unit and v_p(−B/p) = −1, so (−B/p, −B/u)_p = ((−B/u)/p) = (−uB/p) (u² is a
square). For odd p, (−4uB/p) = (−uB/p). (Also, p | uB is impossible: 4uB − u − B ≤ p forces u, B < p.)
(2) −4uB = (u − B)² − (u + B)² ≡ (u − B)² (mod u + B) and gcd(u − B, u + B) = gcd(2u, u + B) = 1 (u + B odd, gcd(u,B) = 1),
so for the odd positive integer u + B the Jacobi symbol (−4uB/(u + B)) = +1; χ_{−4uB}(−1) = sign(−4uB) = −1.
(3) χ_{−4uB} is real, so χ̄ = χ, and χ(n)χ(a) = −χ(n) by (2). If n = p is prime then by (1), 1 − χ(p) = 1 + inv_∞·inv_p.
For a hit, P_{u,B} is integral, inv_ℓ = 1 for all primes ℓ ≠ p (BL Lemma 3.5 for ℓ ∤ 2p; Lemma 3.8 at 2), so Hilbert
reciprocity and inv_∞ = −1 give inv_p = −1 (BL Thm 1.2), which by (1) reads χ_{−4uB}(p) = −1 = χ_{−4uB}(a).
(4) For gcd(m, 2uB) = 1, (−4uB/m²) = (−4uB/m)² = 1. ∎

(Check: `scripts/z38_bm_dictionary.py 400` — exact rationals and Hilbert symbols at all places for all 9 440 pairs at the 77
primes < 400 and the odd squares < 400: reciprocity, inv_∞ = −1, inv_ℓ = 1 off 2nuB, inv₂ = 1 at the 1 806 2-integral
points, inv_p = χ_{−4uB}(p), (2) and (4), and χ_{−4uB}(p) = −1 at all 372 (★) hits; all pass.)

**What this says about O260's dictionary (goal 1; refutation of the strong form, proof of the corrected form).**
* The O260 guess "genus indicator of Prop 2.2(a) = local BM invariant" is **false as stated**: the genus indicator is the
  conjunction of log₂ s(q) = ω(uB odd) + 2 independent quadratic conditions (all s(q) real characters mod q), the Brauer class
  contributes exactly one of them, χ_{−4uB}. The other real characters mod q are (d/·) with d | q a divisor depending on the
  factorisation of u and B; as functions of the point they are not restrictions of any element of Br U_n (which is ℤ/2
  mod constants), so they are not Brauer–Manin data of U_n (Assessment; an interpretation via Brauer groups of fibres was
  not established).
* The **corrected, exact** dictionary: in the orthogonality expansion of the pair indicator, the principal character gives
  the naive singular series 1/φ(q), and **BL's class is the Kronecker character χ_{−4uB}**, giving the Borovoi–Rudnick-type
  BM density factor 1 + inv_∞ inv_p = 1 − χ_{−4uB}(p). This has the classical BR/CT–Xu shape "density × (1 + Σ_{β ∈ Br/Br₀}
  ∏_v inv_v β)" with Br/Br₀ = ℤ/2 **only at integral points** (hits), where inv_ℓ = 1 for ℓ ≠ p, ∞. At a non-hit
  rational point P_{u,B} the full product is 1 by reciprocity and the factor 1 + inv_∞ inv_p keeps only the places ∞, p
  (e.g. p = 17, (u, B) = (1, 2): inv₂ = −1, inv₁₇ = +1, inv_∞ = −1). So "BM-corrected singular series" below means: naive
  density 1/φ(q) at the places dividing q, times the BM factor at {∞, p} — a heuristic density replacement, not a theorem of
  BR type (R-review repair).
* Thm 1.1(3) also makes BL Cor 1.3 on (★), the χ-shadow of PARITY_AUDIT Lemma 3.2 and the pair genus law of B1_LINE
  Lemma 1.2 one statement: "χ_{−4uB}(target) = −1" (an elementary identity, (2)).

## 2. The BM-corrected singular series M_BM: explicit, ≥ 0, vanishes at squares, ≫ (log p)² UNCONDITIONALLY

**Definition.** For odd n ≥ 3, M_BM(n) := Σ_{(u,B) ∈ 𝒫(n), gcd(n, q) = 1} (1 − χ_{−4uB}(n))/φ(4uB), and
X_BM(n) := R*(n) − M_BM(n) (the contribution of all characters mod q other than 1 and χ_{−4uB}). For n odd,
χ_{−4uB}(n) = (−uB/n) (Jacobi), a character **mod n** in the variable uB.

**Proposition 2.1 (PROVED).** (a) M_BM(n) ≥ 0, and every pair term is 0 or 2/φ(q). (b) M_BM(m²) = 0 = X_BM(m²) for every odd
square. (c) Pair by pair, the average of the pair term over the reduced classes n mod q is 1/φ(q) (= that of
1[n ≡ a (q)]): mean-preserving. (d) For p prime, M_BM(p) = M₀(p) − T(p) with M₀(p) = Σ_{𝒫(p)} 1/φ(4uB) (depends on p only
through its size) and T(p) = Σ_{𝒫(p)} ((−uB)/p)/φ(4uB) — **a single Legendre symbol mod p summed over a hyperbolic region**,
the only arithmetic of p in M_BM. (e) φ(4uB) = 4φ(u)φ(B) (exactly one of u, B is even); for m ≤ n/4 the pairs with uB = m
are the 2^{ω(m)} coprime ordered splittings of even m, so the bulk of T(p) is Σ_{m ≤ p/4, 2|m} (−m/p)2^{ω(m)}/(4φ(m)).
*Proof.* (a) 1 − χ ∈ {0, 2}. (b) Thm 1.1(4) and R*(m²) = 0 (SINGLE_P_COUNT Prop 2.2(b)). (c) χ_{−4uB} is non-trivial
mod q, so it averages to 0. (d) gcd(p, q) = 1 as u, B < p. (e) Direct. ∎

**Relation to O260 and to the board's F4.** M_BM is coarser than O260's M_gen (it keeps 2 of the s(q) real characters);
both vanish at squares, but M_BM is the one that is *geometric* (Thm 1.1). The board's F4 projector "(1 − χ_p(ab))/2" on
the fixed-modulus tube is exactly this factor: (ab/p) = (−ab/p)·(−1/p), and for p ≡ 1 (4) it is χ_{−4ab}(p), i.e. **the F4
projector is BL's Brauer class** (Thm 1.1(1)); for p ≡ 3 (4) the correct projector is (1 + (ab/p))/2 = (1 − (−ab/p))/2.
F4's open obligation (i) is Prop 2.3 below (true under GRH); obligation (ii) (Gevrey-bump Mellin truncation of the tube) is
not needed here, since the pair form is already an exact sharp-cutoff identity with no tube.

**Theorem 2.2 (PROVED; unconditional).** For primes p → ∞, with L = log p,
  M_BM(p) ≥ (1/(32π²) − o(1))·L²   (via Pólya–Vinogradov), and M_BM(p) ≥ (3/(16π²) − o(1))·L² ≈ 0.0190 L² (via Burgess).
For comparison M₀(p) = (3/(2π²) + o(1)) L² ≈ 0.152 L² (Dirichlet-series computation below).
*Proof.* χ := (·/p). All pair terms are ≥ 0 and φ(4uB) ≤ 4uB, so M_BM(p) is at least the sum of (1 − χ(−uB))/(4uB) over
any subfamily. Take 𝒮 = {(u, 2B′) : u odd, u ≤ X = p^δ, B′ ≤ Y_u := p/(8u), gcd(B′, u) = 1} and its image under the swap
(u, B) ↦ (B, u) (disjoint from 𝒮 by parity; χ(−uB) is swap-symmetric). Members of 𝒮 satisfy gcd = 1, u + B odd and
4uB − u − B < 4uB ≤ p, so 𝒮 ⊂ 𝒫(p). Hence, with ε_u = χ(−2u) ∈ {±1},
  M_BM(p) ≥ 2 Σ_{u odd ≤ X} (1/(8u)) [ Σ_{B′ ≤ Y_u, (B′,u)=1} 1/B′ − ε_u Σ_{B′ ≤ Y_u, (B′,u)=1} χ(B′)/B′ ].
By Möbius over d | u: the first sum is Σ_{d|u} μ(d)d^{−1}H(Y_u/d), H(t) = Σ_{k≤t} 1/k = log t + γ + O(1/t) for t ≥ 1. We take
δ ≤ 1/2, so Y_u/d ≥ Y_u/u = p/(8u²) ≥ 1/8; for t ∈ [1/8, 1), |H(t) − log t − γ| ≤ log 8 + γ. Hence the first sum is
(φ(u)/u)(log Y_u + γ) + (φ(u)/u)Σ_{ℓ|u} log ℓ/(ℓ − 1) + O(κ(u)) ≥ (φ(u)/u)·log Y_u − O(κ(u)) (the middle term is ≥ 0). The second is Σ_{d|u} μ(d)χ(d)d^{−1}·G(Y_u/d), G(t) := Σ_{k≤t} χ(k)/k,
so it is at most κ(u)·g(p) in absolute value, κ(u) := ∏_{ℓ|u}(1 + 1/ℓ), g(p) := sup_t |G(t)|.
PV: |Σ_{k≤s} χ(k)| ≤ √p log p for all s, so with T₀ = √p L², |G(t)| ≤ H(T₀) + 2√p log p/T₀ ≤ (1/2)L + 2 log L + 2 for every
t (trivially for t ≤ T₀). Burgess: Σ_{k≤s} χ(k) ≪ s·p^{−η} for s ≥ p^{1/4+ε}, whence g(p) ≤ (1/4 + ε)L + O(1).
So g(p) ≤ βL + o(L) (β = 1/2, or β = 1/4 + ε for fixed ε > 0; for the partial summation, truncate at k ≤ p and use
periodicity of χ beyond). Then
  M_BM(p) ≥ (1/4) Σ_{u odd ≤ X} u^{−1}[(φ(u)/u)(L − log 8u) − κ(u)(βL + o(L))] − O(L).
Standard Dirichlet-series asymptotics (residues of ζ_odd(1+s)·∏_{ℓ odd}(1 ∓ ℓ^{−2−s})): Σ_{u ≤ X odd} φ(u)/u² = (4/π²)log X
+ O(1), Σ_{u ≤ X odd} φ(u) log u/u² = (2/π²) log² X + O(log X), Σ_{u ≤ X odd} κ(u)/u = (6/π²) log X + O(1). With X = p^δ:
  M_BM(p) ≥ (L²/(4π²))·(4δ − 2δ² − 6βδ) − O(L log L).
(the O(κ(u)) errors sum to O(L)). β = 1/2: max at δ = 1/4, value 1/8, giving 1/(32π²). β = 1/4 + ε: on δ ≤ 1/2 the
maximum is at δ = 1/2, value 3/4 − 3ε, giving 3/(16π²) after ε ↓ 0. (R279 repair: the earlier remark that δ > 1/2 "gains < 1 %" was
asserted without derivation and is withdrawn. The o(1) is effective but depends on Burgess's ε, η; at accessible p the O_ε(1) dominates — g(p)/L ≈ 0.41–0.46 at
the (★)-failure primes ≤ 10⁶ — so in range the operative statement is the numerical M_BM ≥ 0.062L², §3.2.) For M₀: the bulk is (1/4)Σ_{m ≤ p/4, 2|m} 2^{ω(m)}/φ(m) and Σ_{2|m} 2^{ω(m)}m^{−1−s}·m/φ(m) has a double pole at s = 0 with
leading coefficient 4·(1/4)·∏_{ℓ odd}(1 + ℓ^{−2}) = 12/π² (2-part 4·Σ_{k≥1}2^{−ks}·2^{k}/2^{k−1}·…, ζ_odd² ~ 1/(4(s−1)²),
local factors (1 − 1/ℓ)² + 2/ℓ = 1 + 1/ℓ²), so the bulk is (1/4)(6/π²)L² + O(L); for the leading term it suffices that the pair set is sandwiched between
{uB ≤ p/4} and {uB ≤ (p+1)/3}, whose bulk sums differ by O(L) (R-review repair: replaces an unjustified O(1) boundary bound). ∎

**Proposition 2.3 (CONDITIONAL on GRH for (·/p); this is F4's obligation (i), now with a derivation).** Under GRH,
T(p) = o(L²), hence M_BM(p) = M₀(p)(1 + o(1)) = (3/(2π²) + o(1))L².
*Proof.* Granville–Soundararajan (Large character sums, JAMS 14 (2001), Theorem 2 (R279 repair: checked; for 1 ≤ x ≤ q, Σ_{n≤x}χ(n) ≪ Ψ(x, log²q (log log q)^{20}))): under GRH, Σ_{n≤x} χ(n) = o(x) uniformly for
log x/log log p → ∞. Hence g(p) ≤ log((log p)^{A}) + o(L) = o(L) (partial summation beyond x₀ = (log p)^{A}, A → ∞ slowly).
Split T(p) = 2Σ_{u<B} (u = B is impossible). For u < B one has u < √p. For fixed u, write 1/φ(B) = B^{−1}Σ_{e|B}μ²(e)/φ(e),
remove gcd(B, u) = 1 by Möbius and the parity of B by B = 2B′ or 1[B odd] = 1 − 1[2|B]; the B-sum becomes an absolutely
convergent combination (total weight ≪ κ(u)) of sums G(t) over intervals, each ≤ 2g(p). The constraint B > u adds one more
G-difference. So |T(p)| ≪ Σ_{u < √p} κ(u)/φ(u)·g(p) ≪ L·g(p) = o(L²). ∎
(Unconditionally the same argument gives only |T(p)| ≤ C·L² with C not small; Theorem 2.2 uses positivity instead.)

**Consequence (CONDITIONAL; R279 repair: one-sided form — the two-sided |R* − M_BM| ≤ E with E ≪ L² is FALSE i.o. by Prop 3.1,
so a conditional from it would be vacuous).** For every function E(n) with E(p) ≤ (3/(16π²) − ε)(log p)² (unconditional) or
E(p) = o(log² p) (GRH): the hypothesis
  H_BM(E): R*(n) − M_BM(n) ≥ −E(n) for all large odd n
implies R(p) ≥ 1 for all large primes p ((★), hence ES given the census below the threshold). **H_BM is not refuted by T1**: at n = m² both R* and M_BM vanish
(Prop 2.1(b)), so the inequality holds trivially there. This is the CONDITIONAL_ES Prop 3.1 obstruction removed at the level of
the hypothesis, with an unconditional main-term lower bound. Whether H_BM is true/natural is §3.

## 3. The remainder X_BM: what hypothesis could close the gap, and is it ES in disguise?

### 3.1 The two-sided hypothesis is false infinitely often (PROVED)

**Proposition 3.1 (PROVED, via Linnik's theorem).** There are infinitely many primes p ≡ 1 (mod 4) with
R(p) ≥ exp((log 2/L_Lin − o(1))·log p/log log p), L_Lin a Linnik exponent (L_Lin = 5 admissible, Xylouris). Since
M_BM(p) ≤ 2M₀(p) ≪ (log p)² and M_gen(p) ≤ Σ_{𝒫(p)} s(q)/φ(q) ≪ (log p)⁴, both |X_BM(p)|/M_BM(p) and |X(p)|/M_gen(p) are
unbounded on these primes. Hence **every two-sided hypothesis |R − M| ≤ E with E = (log p)^{O(1)}, in particular O260's
H_X "|X(p)| < M_gen(p) for all large p", is false infinitely often** (in the harmless direction R ≫ M).
*Proof.* Let Q_k be the product of the first k primes ≡ 3 (mod 4). Choose a prime p ≡ −1 (mod Q_k), p ≡ 1 (mod 4),
p ≪ (4Q_k)^{L_Lin} (Linnik). For every divisor d | Q_k with an odd number of prime factors, d ≡ 3 (mod 4), so C := (d + 1)/4
is an integer and B := (p + 1)/d is an even integer: (u, B, C) = (1, B, C) solves 4uBC − u − B = Bd − 1 = p. These are
2^{k−1} distinct solutions. log Q_k = θ(ℓ_k; 4, 3) ∼ ℓ_k/2 ∼ k log k (ℓ_k ∼ 2k log k the k-th prime ≡ 3 (4)), so log p ≤ (L_Lin + o(1))·k log k
and k ≥ (1/L_Lin − o(1))·log p/log log p. Upper bounds: M_BM ≤ 2M₀ ≍ (log p)² (Thm 2.2 proof) and Σ_{m ≤ p/3} 4^{ω(m)}/φ(m) ≪ (log p)⁴. ∎
(Numerically the upper tail is already visible: at primes p ≡ 1 (4) in [3·10⁵, 10⁶), 764 of 26 195 have R > 2M_BM (R279 repair: was 766, which counted |X_BM| ≥ M_BM incl. the 2 zeros), and
max |X_BM|/M_BM = 2.5; `scripts/z38_hx.py`.)

**So the only meaningful form is one-sided.** For ε ∈ (0, 1):
  H⁻_BM(ε, p₀): R(p) ≥ ε·M_BM(p) for all primes p > p₀, i.e. X_BM(p) ≥ −(1 − ε)M_BM(p).
With Theorem 2.2 this gives R(p) ≥ ε(0.0190 − o(1))(log p)² ≥ 1 for large p, unconditionally in the main term. The same
with M_gen in place of M_BM would additionally need a polylog lower bound for M_gen (O260 spark 2; open beyond log log p).
**H⁻_BM is ES-(★) in disguise up to the constant ε**: H⁻_BM(ε, p₀) ⟹ (★) for p > p₀ ⟹ (trivially) nothing quantitative;
the content of H⁻_BM beyond R(p) ≥ 1 is only that the lower tail is relative to M_BM. It is not a weakening of (★); it is a
quantitative strengthening. What the BM analysis buys is (a) the hypothesis is not refuted by T1 (Prop 2.1(b)) and (b) the
main term is now *unconditionally* of the right size (Thm 2.2) — the R-analogue of CONDITIONAL_ES Prop 3.1(3) (with the
principal term alone, X₀ := R* − M₀ has X₀(m²) = −M₀(m²) ≍ −(log m)², so any bound |X₀| < M₀ fails at every square; with
M_BM the square column is 0 = 0).

### 3.2 Numerics for H⁻_BM (EVIDENCE; `scripts/z38_mbm.c`, `z38_hx.py`, `z38_zero_law.py`, `z38_zero_growth.py`)

All primes 5 ≤ p ≤ 10⁶ (78 496) and all odd n ≤ 10⁶ (500 000) computed (R* exactly; M₀, M_BM, and M_BM8 := M_BM refined
by the characters mod 8, double-precision sums; M_BM8 also vanishes at squares and is mean-preserving). **T1 control: all 499 odd squares ≤ 10⁶ have
R* = M_BM = M_BM8 = 0.** Primes p ≡ 1 (4), M = M_BM:

| range | N | R = 0 | R < M/2 | min R/M | min (R − M)/√(2M) | sd of (R − M)/√(2M) | \|R − M\| ≥ M (incl. R = 0; R279 repair: true R > 2M = 49, 123, 279, 764) |
|---|---|---|---|---|---|---|---|
| [10³, 10⁴) | 529 | 2 | 26 (4.9 %) | 0 (5569) | −1.95 | 1.07 | 51 |
| [3·10⁴, 10⁵) | 3172 | 1 | 110 (3.5 %) | 0 (83449) | −2.76 | 1.24 | 124 |
| [10⁵, 3·10⁵) | 8197 | 1 | 251 (3.1 %) | 0 (102001) | −3.11 | 1.34 | 280 |
| [3·10⁵, 10⁶) | 26195 | 2 | 684 (2.6 %) | 0 (329617, 712321) | −3.31 | 1.41 | 766 |

* Mean M_BM/L² = 0.149 at p > 5·10⁵ (Thm 2.2's M₀ constant 3/(2π²) = 0.152 ✓); min M_BM/L² over all primes ≤ 10⁶ is 0.062
  (at p = 17), far above the proved 0.0190. **(L) is no longer the issue anywhere in range.**
* (★) failures among all primes ≤ 10⁶: 17 (9 with p ≡ 1 (8): 409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321;
  8 with p ≡ 7 (8): 7, 31, 79, 127, 199, 2719, 8191, 861199 — p ≡ 3 (4) is ES-trivial; none ≡ 3, 5 (8)). At the failures
  M_BM ∈ [1.0, 28.3] (R279 repair: p = 7, 31 have M_BM = 1.00, 2.00; ≥ 2.99 for p ≥ 79): H⁻_BM(ε, p₀) needs p₀ ≥ 861 199 (and ≥ 8.9·10⁶ by the (★) census ≤ 10¹⁰, SINGLE_P_COUNT §3).
* **Zero law (odd non-squares n ∈ [10⁵, 10⁶], M = M_BM8):** P(R* = 0 | M) / e^{−M/2} (swap-Poisson: R*/2 ~ Poi(M/2)) =
  1.5–1.6 (M ∈ [4, 10)), 1.5–2.1 ([10, 16)), 1.8–2.8 ([16, 22)), 5–15 ([22, 28), only 6 zeros) (after the R-review fix of
  M_BM8). Empirical decay of log P(0 | M) is ≈ −0.50 per unit M at M ≈ 11–19 (= the Poisson slope, with a constant excess
  factor ≈ 2) and ≈ −0.23 at M ≈ 19–27: the far lower tail is **possibly** fatter than Poisson (6 zeros; cf. the
  overdispersion growth of O260/B1_LINE). Primes and composites show comparable zero rates at
  equal M (small counts; see the M_BM8 table update below) — no sign of a composite-specific obstruction, though the
  counts are too small to exclude one.
* Zero-set growth over all odd non-squares ≤ K: Z(K) = 215, 445, 905, 1743, 3490 for K = 10⁴ … 10⁶ (local exponent
  0.66 → 0.58, decreasing), dominated by small-M composites (M_BM8 < 0.08L²). Restricted to M_BM8 ≥ 0.1L²: 7, 14, 20, 30, 46 (of which prime: 5, 6, 7, 8, 11).
* Reading (Assessment): finiteness of the zero set is heuristically tied to summability of P(R = 0 | M(n)) along n
  (H⁻_BM itself concerns the larger event R < εM). With M ≈ 0.15L²,
  Poisson gives P ≈ e^{−0.075L²} (summable); the measured zero rate at typical M ≈ 25 near 10⁶ is ≈ 2·10⁻⁵ ≈ n^{−0.8} — still a power at this height. Whether log P(0 | M(n))/log n → −∞ (finitely many failures) is exactly the open question; nothing at 10⁶
  decides it.

### 3.3 Is H⁻_BM implied by a standard conjecture? The closest precedent says "be careful"

* **Standard conjectures (Assessment, consistent with CONDITIONAL_ES §5 and SINGLE_P_COUNT §4.2).** X_BM(p) is, at ONE
  argument p, a sum over ≍ p log p moduli 4uB ≤ p of all characters of order ≥ 2 other than the Brauer one. GRH/GLH control
  sums over n at a fixed character; EH/BFI control boxes of (modulus, integer) and the (★) events lie on a line of relative
  density 1/x (O260); Montgomery's conjecture for primes in APs and the Friedlander–Granville limitations are about
  π(x; q, a) at moduli q ≤ x^{1−ε}, i.e. averages over the integer, never one integer; Kuznetsov/θ only after averaging over p
  (O260 §6). None is single-integer. H⁻_BM is a single-integer lower-tail statement with a polylog main term, i.e. of
  Heath-Brown "three cubes" / Hardy–Littlewood-single-N type; no implication from any of them is established here (and
  none is known to us). **So no "ES ⟸ GRH + H" with H a
  standard equidistribution hypothesis results; the best exact statement is "ES ⟸ H⁻_BM" with an unconditional main term.**
* **Markoff precedent (literature; Ghosh–Sarnak, Invent. Math. 229 (2022) 689–749, arXiv:1706.06712; Loughran–Mitankin,
  IMRN 2021, arXiv:1807.10223 = `sources/r202/1807.10223.txt`; Colliot-Thélène–Wei–Xu, Ann. SNS Pisa 2020).** For the log K3
  surfaces U_m : x² + y² + z² − xyz = m, the class numbers h(m) have mean ∼ C(log m)² (GS (1.6)) — the same polylog-square
  scale as (★) — and a product of local densities δ^{(m)} approximates h for almost all m (GS §9, variance averaged over m).
  Yet: infinitely many integral Hasse failures (GS Thm 1.2(i); the method gives ≫ B^{1/2}/(log B)^{1/2}, per LM p. 3);
  **infinitely many Hasse failures with non-empty integral BM set**: LM Thm 1.5 (≫ B^{1/2}/log B), improved by CTWX Thm 5.8
  to ≫ B^{1/2}/(log B)^{1/2}; GS's numerics suggest ≍ B^{γ} failures with γ ≈ 0.89 > 1/2, in which case (with LM Thm 1.4's
  upper bound for BM-explained failures) almost all failures would be non-BM — this last point is conditional on the numerics.
  Browning et al. (Selecta Math. 2025, doi 10.1007/s00029-025-01074-1) record that BM is not always sufficient for log K3.
  **Lesson (Assessment):** in the one well-studied family with the same main-term scale, "BM set non-empty ⟹ integral point"
  is FALSE infinitely often (LM Thm 1.5). Caveat: these theorems concern non-emptiness of the BM set, not a uniformly large
  BM-corrected density along the failures; so the precedent shows H⁻_BM is a strong statement, not that its analogue fails
  at large density. (Difference: (★) failures at primes look finite in the census; GS's failures include structured families
  m = 4 + βν² from the singular Cayley cubic. A structured family for (★) would be a "prime T1"; none is known (z32_prime_T1).)

## 4. The b = 1 line, the union (★) ∪ b = 1, full Type II, and the numerator-8 model

**Proposition 4.1 (PROVED; checks `scripts/z38_typeII_check.py`, `z38_b1.c`).**
(a) (Full Type II.) A Type II solution 4abcd − a − b = cn gives 4/n = 1/(abd) + 1/(nbcd) + 1/(nacd); BL's class is
(−b/(nc), −b/a), with inv_p = (−ab/p) = χ_{−4ab}(p) (p ∤ ab). With s := (a + b)/c the event is n ≡ −s (mod 4ab), and
χ_{−4ab}(−s) = −1 whenever gcd(s, 4ab) = 1. So on the whole Type II family the Brauer character is χ_{−4ab}, independent of
(c, d). (Checked: all 990 Type II solutions at primes < 300, 2.97·10⁶ target identities.)
(b) (b = 1 line.) In B1_LINE's mutual-shift coordinates (S, T) = (4x, y), the b = 1 event is 4xy | p + 4x + y (y odd);
a = (p + T)/S, and BL's inv_p = (−a/p) = (−xy/p) = χ_{−4xy}(p) at the rational point of every pair; χ_{−4xy}(−(4x + y)) = −1
((4x + y) | (4x)² + 4xy). So **(★) and b = 1 are the two shifts −(x + y) and −(4x + y) of the same pair lattice with the same
Brauer character χ_{−4xy}**, and their BM main terms both vanish at squares.
(c) (m/n with 4 | m; BL Rem 1.10.) On the c = 1 line m·uBC = n + u + B the Brauer character is again χ_{−4uB}
(hits at primes < 6000 for m = 8, 12, 16: 6 210, all with (−uB/p) = −1). The restriction 4 | m is needed (R-review:
m = 3, p = 11, (u, B, C) = (1, 7, 1) is a hit with (−uB/p) = +1; BL's 2-adic Lemma 3.8 is for numerator 4).
Domains: (a) for p ∤ ab; (b) for p ≡ 1 (4), pairs in the stated cutoff with p ∤ xy (for y = 1 arbitrarily large x is
allowed and p | x can occur; there the Legendre symbol is 0 and the statement is void). ∎

For the b = 1 line the bare M_BM diverges (the pairs y = 1 have target ≡ −1 (mod 4x) for every x); the natural main term
keeps the mod-4 character as well: M4 := principal + χ_{−4} + χ_{−4xy} + χ_{−4}χ_{−4xy} (still mean-preserving and zero at
squares). EVIDENCE (`z38_b1.c`, `z38_b1_stats.py`):

| sample | line | mean count | mean M4 | mean (count − M4)²/(2M4) (uncentred) | min count/M4 | min (count − M4)/√(2M4) |
|---|---|---|---|---|---|---|
| p ≡ 1 (24), [10⁵, 4·10⁵], 2 991 primes | (★) | 21.2 | 20.2 | 1.53 | 0 (102001) | −3.34 (329617) |
| | b = 1 | 17.3 | 18.3 | 0.85 | 0.062 (241921) | −2.74 |
| | union (sum) | 38.5 | 38.6 | 1.42 | 0.167 (317209) | −3.53 |
| p ≡ 1 (4), [10⁴, 10⁵], 4 174 primes | (★) | 20.0 | 17.6 | 1.61 | 0 (23929) | −2.79 |
| | b = 1 | 16.7 | 14.5 | 1.03 | 0 (66529) | −2.46 |
| | union (sum) | 36.8 | 32.1 | 1.84 | 0.155 (83449) | −3.03 |

* The b = 1 line is close to swap-Poisson (mean squared residual/2M ≈ 0.85–1.0), (★) is overdispersed (1.5–1.6).
* The residuals R − M4★ and N₁ − M4b1 are **positively** correlated overall (see table): no global anti-correlation
  protects the union (complementarity specifically at the rare zeros is not excluded by this statistic). The union's robustness (no failure ≤ 10⁸, B1_LINE) is explained by the doubled main term
  (P(0) ≈ e^{−M/2} with M doubled), not by a forced complementarity. The shared Brauer character makes the two main terms
  positively correlated too (both contain the same Legendre sum Σ(−xy/p)/φ(4xy) over overlapping pair sets).
* Nothing forced: the union's minimum ratio is 0.155–0.167, a ≈ 3σ lower deviation, in line with the single lines.

**Numerator 8 (the soundness check of the brief).** For the 8/p c = 1 line (`z38_mbm.c` with K = 8, all primes ≤ 10⁶):
mean M_BM ≈ 0.067L² (about half the 4/p value, as the bulk is (1/8)·Σ 2^{ω(m)}/φ(m) over m ≤ p/8), and the line fails at
835 primes ≤ 10⁶ (largest 992 903), including 131 and 241 where M_BM = 0.56 and 0.46. So the H⁻ analogue fails at 131 and
241 (as it must: 8/p has no solution at all there, PW Table 1), and fails throughout the range for the single slice. This is
consistent: the BM factor is numerator-blind (same χ_{−4uB}). Finite exceptions do not refute an eventual (p > p₀)
numerator-blind hypothesis; what the control shows is that any argument proving H⁻ with an explicit p₀ must be accurate at
the scale of the main term itself (≈ 0.5 at 131, 241; ≈ 12 at 10⁶ for 8/n), i.e. polylog-accurate (B3).

## 5. Honest assessment (goal 5)

* **New and PROVED.** (i) The exact dictionary (Thm 1.1, Prop 4.1): on every Type II family and on the b = 1 line,
  BL's quaternion class is a single Kronecker character χ_{−4ab} in the orthogonality expansion, whose value at the target
  is forced to −1; principal + Brauer character = a factor of Borovoi–Rudnick shape (1 + inv_∞ inv_p) (R279 repair: no BR theorem
  applies to U_n; the arithmetic of the forcing is classical — Yamamoto, BL Cor 1.3 — the new part is the expansion reading). O260's strong form ("genus =
  BM") is refuted; R277 D3's question is answered. (ii) The BM-corrected singular series M_BM is ≥ 0, mean-preserving,
  vanishes at squares, and is ≫ (log p)² UNCONDITIONALLY (Thm 2.2; constant 3/(16π²) via Burgess), and ∼ M₀ under GRH
  (Prop 2.3 = board F4 obligation (i)). (iii) Two-sided remainder hypotheses are false i.o. (Prop 3.1, Linnik).
* **Exact conditional statement.** ES (indeed (★)) for p > p₀ ⟸ H⁻_BM(ε, p₀): R(p) ≥ ε M_BM(p). No other input is needed
  (main term unconditional). This improves CONDITIONAL_ES only in bookkeeping: the hypothesis is not refuted by T1, and
  the (L) half is now a theorem. It does **not** give "ES ⟸ GRH + (natural non-square-sensitive equidistribution
  hypothesis)": H⁻_BM is a single-integer large-deviation lower bound, ES-(★) in disguise up to the factor ε, with no
  standard conjecture implying it (§3.3), and the closest literature precedent (Markoff surfaces, same (log)² main-term scale)
  has infinitely many failures of the analogous statement.
* **Barrier status.** B3 unchanged (positivity needs the remainder to o(L²) in the lower direction at one p, with typical
  |X| ≈ 0.75L and a possibly fattening far tail). T1 handled (every main term and every hypothesis checked at squares). B6 respected
  (no averaging over p; Thm 2.2 is pointwise). k = 8 control behaves as required.
