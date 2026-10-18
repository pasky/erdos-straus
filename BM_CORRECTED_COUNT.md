# BM_CORRECTED_COUNT — the Brauer–Manin-corrected count for (★) and its remainder (task O268)

Status: O268 working draft. **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z38_*`, memos `BRAINSTORM/z38_*.md`, tiny logs `logs/z38_*`.
Builds on SINGLE_P_COUNT (O260: pair form, genus split R = M_gen + X, Prop 4.1), Bright–Loughran arXiv:1908.02526 (BL),
PARITY_AUDIT Lemma 3.2 (χ-shadow), B1_LINE Lemma 1.2 (pair genus law), CONDITIONAL_ES Props 2.3, 3.1, 7.3.

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
For a hit, P_{u,B} is integral, inv_ℓ = 1 for ℓ ∤ p (BL Lemma 3.5 for ℓ ∤ 2p; Lemma 3.8 at 2), and Hilbert reciprocity
gives inv_p = −inv_∞^{−1}... i.e. inv_p = −1 (BL Thm 1.2), which by (1) reads χ_{−4uB}(p) = −1 = χ_{−4uB}(a).
(4) For gcd(m, 2uB) = 1, (−4uB/m²) = (−4uB/m)² = 1. ∎

(Check: `scripts/z38_bm_dictionary.py 400` — exact rationals and Hilbert symbols at all places for all 9 440 pairs at the 77
primes < 400 and the odd squares < 400: reciprocity, inv_∞ = −1, inv_ℓ = 1 off 2nuB, inv₂ = 1 at the 1 806 2-integral
points, inv_p = χ_{−4uB}(p), (2) and (4), and χ_{−4uB}(p) = −1 at all 372 (★) hits; all pass.)

**What this says about O260's dictionary (goal 1; refutation of the strong form, proof of the corrected form).**
* The O260 guess "genus indicator of Prop 2.2(a) = local BM invariant" is **false as stated**: the genus indicator is the
  conjunction of s(q) = 2^{ω(uB odd)+2} independent quadratic conditions (all real characters mod q), the Brauer class
  contributes exactly one of them, χ_{−4uB}. The other real characters mod q are (d/·) with d | q a divisor depending on the
  factorisation of u and B; as functions of the point they are not restrictions of any element of Br U_n (which is ℤ/2
  mod constants), so they are not Brauer–Manin data (Assessment: they are "genus of the moving modulus" data —
  the Brauer groups of the individual fibres over (u, B), not of the surface).
* The **corrected, exact** dictionary: in the orthogonality expansion of the pair indicator, the principal character gives
  the naive singular series 1/φ(q), and **BL's class is the Kronecker character χ_{−4uB}**, giving the Borovoi–Rudnick-type
  BM density factor 1 + inv_∞ inv_p = 1 − χ_{−4uB}(p). This is the classical BR/CT–Xu shape "density × (1 + Σ_{β ∈ Br/Br₀}
  ∏_v inv_v β)" with Br/Br₀ = ℤ/2, evaluated pair by pair.
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
  M_BM(p) ≥ (1/(32π²) − o(1))·L²   (via Pólya–Vinogradov), and M_BM(p) ≥ (25/(128π²) − o(1))·L² ≈ 0.0198 L² (via Burgess).
For comparison M₀(p) = (3/(2π²) + o(1)) L² ≈ 0.152 L² (Dirichlet-series computation below).
*Proof.* χ := (·/p). All pair terms are ≥ 0 and φ(4uB) ≤ 4uB, so M_BM(p) is at least the sum of (1 − χ(−uB))/(4uB) over
any subfamily. Take 𝒮 = {(u, 2B′) : u odd, u ≤ X = p^δ, B′ ≤ Y_u := p/(8u), gcd(B′, u) = 1} and its image under the swap
(u, B) ↦ (B, u) (disjoint from 𝒮 by parity; χ(−uB) is swap-symmetric). Members of 𝒮 satisfy gcd = 1, u + B odd and
4uB − u − B < 4uB ≤ p, so 𝒮 ⊂ 𝒫(p). Hence, with ε_u = χ(−2u) ∈ {±1},
  M_BM(p) ≥ 2 Σ_{u odd ≤ X} (1/(8u)) [ Σ_{B′ ≤ Y_u, (B′,u)=1} 1/B′ − ε_u Σ_{B′ ≤ Y_u, (B′,u)=1} χ(B′)/B′ ].
By Möbius over d | u: the first sum is Σ_{d|u} μ(d)d^{−1}(log(Y_u/d) + γ + O(d/Y_u)) ≥ (φ(u)/u)·log Y_u − O(τ(u)/Y_u) (the
extra term (φ(u)/u)Σ_{ℓ|u} log ℓ/(ℓ − 1) is ≥ 0). The second is Σ_{d|u} μ(d)χ(d)d^{−1}·G(Y_u/d), G(t) := Σ_{k≤t} χ(k)/k,
so it is at most κ(u)·g(p) in absolute value, κ(u) := ∏_{ℓ|u}(1 + 1/ℓ), g(p) := sup_t |G(t)|.
PV: |Σ_{k≤s} χ(k)| ≤ √p log p for all s, so with T₀ = √p L², |G(t)| ≤ H(T₀) + 2√p log p/T₀ ≤ (1/2)L + 2 log L + 2 for every
t (trivially for t ≤ T₀). Burgess: Σ_{k≤s} χ(k) ≪ s·p^{−η} for s ≥ p^{1/4+ε}, whence g(p) ≤ (1/4 + ε)L + O(1).
Write g(p) = βL + o(L) (β = 1/2 or 1/4 + ε). Then
  M_BM(p) ≥ (1/4) Σ_{u odd ≤ X} u^{−1}[(φ(u)/u)(L − log 8u) − κ(u)βL] − o(1).
Standard Dirichlet-series asymptotics (residues of ζ_odd(1+s)·∏_{ℓ odd}(1 ∓ ℓ^{−2−s})): Σ_{u ≤ X odd} φ(u)/u² = (4/π²)log X
+ O(1), Σ_{u ≤ X odd} φ(u) log u/u² = (2/π²) log² X + O(log X), Σ_{u ≤ X odd} κ(u)/u = (6/π²) log X + O(1). With X = p^δ:
  M_BM(p) ≥ (L²/(4π²))·(4δ − 2δ² − 6βδ) − O(L log L).
β = 1/2: max at δ = 1/4, value 1/8, giving 1/(32π²). β = 1/4: max at δ = 5/8 (Y_u ≥ p^{3/8}/8, fine), value 25/32, giving
25/(128π²). For M₀: the bulk is (1/4)Σ_{m ≤ p/4, 2|m} 2^{ω(m)}/φ(m) and Σ_{2|m} 2^{ω(m)}m^{−s}/φ(m) has a double pole at s = 1 with
leading coefficient 4·(1/4)·∏_{ℓ odd}(1 + ℓ^{−2}) = 12/π² (2-part 4·Σ_{k≥1}2^{−ks}·2^{k}/2^{k−1}·…, ζ_odd² ~ 1/(4(s−1)²),
local factors (1 − 1/ℓ)² + 2/ℓ = 1 + 1/ℓ²), so the bulk is (1/4)(6/π²)L² + O(L); the boundary pairs (uB > p/4) contribute
Σ_u O(1/u²) = O(1). ∎

**Proposition 2.3 (CONDITIONAL on GRH for (·/p); this is F4's obligation (i), now with a derivation).** Under GRH,
T(p) = o(L²), hence M_BM(p) = M₀(p)(1 + o(1)) = (3/(2π²) + o(1))L².
*Proof.* Granville–Soundararajan (Large character sums, JAMS 14 (2001)): under GRH, Σ_{n≤x} χ(n) = o(x) uniformly for
log x/log log p → ∞. Hence g(p) ≤ log((log p)^{A}) + o(L) = o(L) (partial summation beyond x₀ = (log p)^{A}, A → ∞ slowly).
Split T(p) = 2Σ_{u<B} (u = B is impossible). For u < B one has u < √p. For fixed u, write 1/φ(B) = B^{−1}Σ_{e|B}μ²(e)/φ(e),
remove gcd(B, u) = 1 by Möbius and the parity of B by B = 2B′ or 1[B odd] = 1 − 1[2|B]; the B-sum becomes an absolutely
convergent combination (total weight ≪ κ(u)) of sums G(t) over intervals, each ≤ 2g(p). The constraint B > u adds one more
G-difference. So |T(p)| ≪ Σ_{u < √p} κ(u)/φ(u)·g(p) ≪ L·g(p) = o(L²). ∎
(Unconditionally the same argument gives only |T(p)| ≤ C·L² with C not small; Theorem 2.2 uses positivity instead.)

**Consequence (CONDITIONAL, exact).** For every function E(n) with E(p) ≤ (25/(128π²) − ε)(log p)² (unconditional) or
E(p) = o(log² p) (GRH): the hypothesis
  H_BM(E): |R*(n) − M_BM(n)| ≤ E(n) for all large odd n
implies R(p) ≥ 1 for all large primes p ((★), hence ES). **H_BM is not refuted by T1**: at n = m² both R* and M_BM vanish
(Prop 2.1(b)), so the inequality holds trivially there. This is the CONDITIONAL_ES Prop 3.1 obstruction removed at the level of
the hypothesis, with an unconditional main-term lower bound. Whether H_BM is true/natural is §3.
