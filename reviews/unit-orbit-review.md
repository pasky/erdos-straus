# R186 — hostile review of O186 UNIT_ORBIT_ES.md (reviewer 1 of 2, full document)

Reviewed: UNIT_ORBIT_ES.md at side-agent/unit-orbit-es 2f229f86 (merged), BRAINSTORM/bsL_finite_mute.md,
BRAINSTORM/bsL_sieve_saturation.md, reviews/agent-reports/AGENT_REPORT_O186.md. From-scratch scripts (none reuse
scripts/uo_*): `scripts/review_uo_common.py` (Hilbert symbols over ℚ, exact ES^{(S)} checker),
`review_uo_evidence.py`, `review_uo_squares.py`, `review_uo_twoprime.py`, `review_uo_misc.py`.

**Bottom line.** No FATAL defect. The headline Theorem 2.4 is **SOUND**: the sifted variable is the prime r
(Gupta–Murty/Artin reading), NOT the S-units Q, so the "only polylog many Q" worry does not arise; I reconstructed the
sieve (Lemma 2.2) and the collision count (Lemma 2.3) in full and every hypothesis holds, with |S| ≥ 4 exactly what
plain Bombieri–Vinogradov (level ½, roughness x^{1/4−ε}) supports. One MAJOR defect concerns the *diagnosis* in §0 (L2)/§4
(Assessment level): for V_φ the forced Kummer condition of Prop 4.1 is free at split ℓ ≡ 3 (mod 4), and the real
barrier is rank 1 (Artin's problem for the single unit φ), not "a real mute place". Several MINOR defects, including a
literal overclaim in Thm 2.4(b) (counterexample found) and a missed strengthening: **ES^{(S)}(n) holds for every
n > 1 coprime to 2S, squares included** (divisibility), which the document never says.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (mute primes, inv_q = 0) | SOUND |
| Cor 1.2 (T1 for ES^{(S)}) | SOUND (definition of Type I/II for the variant to be added, m1) |
| Prop 2.1 (orbit shots solve ES^{(S)}) | SOUND |
| Lemma 2.2 (rough (r−1)/2 in a progression) | SOUND (standard; details below) |
| Lemma 2.3 (few primes with small S-image) | SOUND |
| Thm 2.4(a) (every non-square, |S| ≥ 4, unconditional) | SOUND (ineffective; m3) |
| Thm 2.4(b) (squares) | SOUND-AFTER-REPAIRS ("no solution of Type I/II shape at all" is literally false; m2) |
| Remarks after Thm 2.4 | SOUND as labelled; missed corollary ES^{(S)} for ALL n (m4) |
| Prop 3.1 | SOUND |
| Prop 3.2 | SOUND (hypothesis stronger than needed, m6) |
| Prop 4.1 | SOUND |
| Prop 4.1 Consequence (a), §0 (L2), Assessment 4.2 "hypothesis responsible" | GAP / misdiagnosis (M1) |
| Assessment 4.2, Galois paragraph | Assessment-label correct; one unjustified step (M1(ii)) |
| Thm 5.1 (V_φ, ≪ X^{3/4}log²X, unconditional) | SOUND |
| Thm 5.2 (GRH, exact T1 set) | SOUND (CONDITIONAL); justify by Lenstra Cor. 4.8 (m7) |
| Prop 6.1 | SOUND |
| Thm 6.2 | SOUND (Assessment parts labelled) |
| EVIDENCE (§2, §5) | REPRODUCED exactly by independent code |
| Labels | correct, except M1 narrative and m8 citation |

(details per claim follow)

## Per-claim checks

### C1. Lemma 1.1 — SOUND
Re-derived. Write the three terms 1/x, 1/y, 1/z with 4/n a q-unit (q ∤ n). If v_q(z) = −w < 0, the term 1/z is
≡ 0 (mod q^w), so the q-adic valuations of 1/x, 1/y obey the usual "minimum occurs twice" rule among {1/x, 1/y, 4/n}:
(i) x, y units ⇒ α = (−y/x, −z/x) has tame symbol (−y/x mod q)^{−w}·(sign factor)^{0} = square since w even;
(ii) v(x) = V > 0 forces v(y) = V and v(x + y) ≥ 2V, so −y/x ≡ 1 (mod q) and the symbol is trivial whatever v(b);
(iii) impossible. The odd-w remark is right: case (i) gives ((−y/x)/q), unconstrained.
*Check:* `review_uo_evidence.py` computes inv_q by an independent Hilbert-symbol routine (validated by the product
formula on 2000 random pairs) on all 17 979 + 6 197 Prop 2.1 solutions; 1 847 of the prime solutions have
v_q(z) < 0 for some q ∈ S; inv_q = 0 in all cases. `review_uo_squares.py` also gives inv_q = 0 on all 1 802 box solutions
at 13², 17², 19².

### C2. Corollary 1.2 — SOUND (m1: define the shapes)
For ES^{(S)} the shapes must be defined at ℓ | n, ℓ ∉ S (automatic: gcd(n, S) = 1): with v = v_ℓ(n) = 2s and
z = Z/Q² (so v_ℓ(z) = v_ℓ(Z) is well defined), *Type I* = one of x, y, z has v_ℓ ≥ 2s and the other two are ℓ-units,
*Type II* = one ℓ-unit and two with v_ℓ ≥ 2s — exactly T1_TEMPLATE Thm 2.1(d). The proof uses Thm 2.1(a)–(d) at ∞, 2,
ℓ ∉ S; those are stated for global integral points but their proofs are purely local (need only u_i ∈ O_v), and
x, y, z are v-integral at every v ∉ S (z ∈ ℤ_{(2)}, z ∈ ℤ_{(ℓ)}). Hilbert reciprocity then gives Σ_{ℓ|n} inv_ℓ = ½. Correct.
*Check:* independent box search (`review_uo_squares.py 3 300 169 289 361`, x ≤ 3n, x ≤ y ≤ 300n, third term with
numerator in ⟨S⟩²): 491 / 566 / 745 solutions, **all "other" shape**, invariants (inv_∞, inv_2, inv_S, inv_ℓ) =
(½, 0, 0, ½) on every one — identical counts to the author's. Control without parity (`--noparity`): 4002 / 4922
solutions, of which 1344 + 428 / 1860 + 527 Type I / II, each with inv_ℓ = 0 and exactly one inv_q = ½ — identical to
the author's control.

### C3. Proposition 2.1 — SOUND
Re-derived: e ≡ −n (mod 4) ⇒ x ∈ ℤ; x + Q² = e(r + 1)/4; 1/y + 1/z = e/(nx). Parity: from 4rx = n(r + 1) + 4Q² and
q ∤ r (q ∤ a), v_q(x) = s if s < 2c, so v_q(z) = 2s − 2c (even); if s ≥ 2c, v_q(z) ≥ 0. Shape: ℓ | n ⇒ ℓ ∤ a ⇒ ℓ ∤ e
⇒ ℓ ∤ x; n | y and n | z. All verified exactly (Fraction arithmetic) on every solution in `review_uo_evidence.py`,
including Type II valuations v_ℓ(y), v_ℓ(z) ≥ v_ℓ(n) for composite n. The explicit no-parity example
4/9 = 1/449 + 1/18 + 3125/8082 (9 + 4·5⁵ = 7·1787) checks (`review_uo_misc.py` (a)).

### C4. Lemma 2.2 — SOUND (standard; my reconstruction)
𝒜 = {(r − 1)/2 : r ≤ x, r ≡ a (M)}, sifting primes ℓ ∤ M, ℓ < z. For squarefree d with (d, M) = 1 (so d odd),
d | (r − 1)/2 ⟺ r ≡ 1 (mod d), so |𝒜_d| = π(x; Md, c_d) with c_d given by CRT and coprime to Md. Main term
X = li(x)/φ(M), density g(d) = 1/φ(d), and X g(d) = li(x)/φ(Md) (as (d, M) = 1). Σ_{d<D} |r_d| ≤
Σ_{q ≤ MD} max_{(c,q)=1}|π(x; q, c) − li(x)/φ(q)| ≪_A x/log^A x by BV for MD ≤ x^{1/2}/log^B x (distinct d give
distinct q = Md). Dimension-1 condition holds for g(ℓ) = 1/(ℓ − 1). Jurkat–Richert/Rosser–Iwaniec lower bound
(HR Thm 8.4): S(𝒜, z) ≥ X V(z)(f(s) − o(1)) − Σ|r_d|, s = log D/log z → 2/(1 − 4ε) > 2, f(s) = 2e^γ log(s − 1)/s > 0.
V(z) ≍_M 1/log z, so S ≫_{M,ε} x/log²x for x ≥ x₀(M, ε, A). Primes 2 and ℓ | M never divide (r − 1)/2 (r ≡ 3 (4);
a ≢ 1 (ℓ)). So every prime factor of (r − 1)/2 is ≥ x^{1/4−ε}. This matches Gupta–Murty's Lemma 1 (α = 1/4 − ε, BV +
Iwaniec), as summarised in sources/uo/LITERATURE.md Q2 (the GDZ scan has no text layer; I did not re-read it, but the
argument above is self-contained). Constants depend on M = 4·rad(n), i.e. on n — harmless since Thm 2.4 is pointwise in n.

### C5. Lemma 2.3 — SOUND
Re-derived: (B + 1)^k > y exponent vectors with entries in [0, B] collide mod r when |Γ_r| ≤ y, so r | N_c for a
nonzero c with |c_i| ≤ B (r ∉ S, so cancelling common factors is legitimate); N_c ≠ 0 by unique factorisation; ω(N_c) ≤
log₂|N_c| ≪_S B; (2B + 1)^k ≪ y vectors. Total ≪_S y^{1+1/k}. (Same as Gupta–Murty Lemma 2 / Murty–Petersen Prop 3.2.)

### C6. Theorem 2.4 — (a) SOUND; (b) SOUND-AFTER-REPAIRS (m2)
*Reading.* The sifted set is the set of primes r (≡ a mod M, (r − 1)/2 rough); the S-units only enter through the image
Γ_r ⊂ F_r^*. So the brief's FATAL worry (sieving n + 4Q² over polylog-many Q) does not apply.
*Step-by-step.* n ≡ 3 (4): Q = 1, n + 4 ≡ 3 (4) has a prime factor ≡ 3 (4). ✓. n ≡ 1 (4), non-square: some ℓ₀ ≥ 5 has
odd v_{ℓ₀}(n) (n = 3^{odd}m² would be ≡ 3 (4)) ✓; for ℓ₀ ≥ 5 there are both residues and non-residues ∉ {0, 1}
((ℓ₀ − 3)/2 ≥ 1 resp. (ℓ₀ − 1)/2 ≥ 2), and flipping (a_{ℓ₀}/ℓ₀) flips the Jacobi symbol (a/n) since v_{ℓ₀}(n) is odd ✓.
For r ≡ a (M): (r/n) = (a/n) = −1, (n/r) = (r/n) by reciprocity (n ≡ 1 (4)), (−1/r) = −1 ⇒ −n/4 ∈ (F_r^*)² ✓ (r ∤ n).
Index: [F_r^* : Γ_r] | r − 1 = 2·odd; if ∉ {1, 2} it has an odd prime factor, which divides (r − 1)/2, hence is
≥ x^{1/4−ε}, so |Γ_r| ≤ x^{3/4+ε}; Lemma 2.3: ≪ x^{(3/4+ε)(1+1/k)} ≤ x^{(3/4+ε)5/4} = o(x/log²x) for ε < 1/20 ✓
(exactly the threshold: k = 3 would need roughness x^{1/4+ε}, Heath-Brown's input). Index ≤ 2 ⇒ Γ_r ⊇ (F_r^*)²
(unique index-2 subgroup of a cyclic group), and squaring is onto (F_r^*)² from Γ_r in both cases (odd order
(r − 1)/2) ⇒ −n/4 ≡ Q² for some Q ∈ ⟨S⟩ (non-negative exponents, Γ_r finite) ⇒ r | n + 4Q² ✓. Finitely many r ∈ S are
discarded ✓. T1-sensitive step: for n = m², (a/n) = 1 for every a, so no admissible class exists — consistent.
(b): m² + (2Q)² with gcd(m, 2Q) = 1 has only prime factors ≡ 1 (4) ✓; Cor 1.2 ✓ — but see m2 for the wording.
*Evidence (independent):* `review_uo_evidence.py 200000 30000`: all 17 979 primes 13 ≤ p < 2·10⁵ (p ∉ S) solved,
max Q = 81, Q = 1 for 15 592; all 6 197 odd non-squares n < 3·10⁴ coprime to 2S solved (max Q = 81); every solution
verified exactly; squares have no shot for the first 40 Q (as proved).

### C7. Proposition 3.1 — SOUND
g = a = n + 4η ≡ −1 (mod 4), e = 1, σ_anchor(a) = n + 4σ(η) > 0 for orbit elements positive at the anchor
(φ^{2k+1} at σ₁; Q² in ES^{(S)}); x = (n + 1)/4. Trivial and correct.

### C8. Proposition 3.2 — SOUND (m6)
Re-derived: Hilbert reciprocity for coprime n, a (both prime to 2): (n/a)(a/n) = ∏_{v|2∞}(n, a)_v = 1 because n > 0 and
n ∈ K_v^{*2} at v | 2; (a/n) = (η/n) = ∏_{ℓ|n} (N_{K/ℚ}η/ℓ)^{v_ℓ(n)} (norm compatibility of residue symbols, incl.
ramified ℓ) = (±1/n) = 1. *Check* (`review_uo_misc.py` (c)): 13 944 shots a = n + 4η, η = ±φ^j (ℚ(√5)) and
η = ±(1 + √2)^j (ℚ(√2)), n ≡ 1 (mod 8), n < 2000, j ≤ 13: the total symbol (n/|N a|) = 1 in all cases.

### C9. Proposition 4.1 — SOUND
Re-derived. K(√u)/K for a unit u is unramified outside 2∞, 2-conductor | 4, ramified at real v iff σ_v(u) < 0, and
u ∈ U_𝔪 restricts that to v ∈ P; so χ_u factors through Cl_𝔪. χ_u((g)) = ∏_{v|2∞}(u, g)_v (product formula; odd
v ∤ g contribute 1); real factors are 1 (u > 0 off P, g > 0 on P); at v | 2, (u, g)_v = (u, −1)_v(u, −g)_v and
−g ≡ 1 (mod 4) gives an unramified (or trivial) K_v(√−g), so (u, −g)_v = 1; ∏_{v|2}(u, −1)_v = ∏_{v real}(u, −1)_v.
Consequence (a): U_𝔪 = ⟨−φ⟩ (σ₂(−φ) > 0) and the forced condition (−φ/𝔮) = −1 agrees with T1_TEMPLATE Thm 1.3 (χ = χ_{−φ}).
K(√−φ)/ℚ is not Galois (σ(−φ)/(−φ) = −φ^{−2} ∉ K^{*2}). The identity is correct; its *interpretation* is not — see M1.

### C10. Theorem 5.1 — SOUND
Re-derived. (1) If n mod ℓ ∈ S_ℓ then −n/4 ≡ φ^{2k+1} (mod 𝔮) for some k, so 𝔮 | a_k with (n/𝔮) = (n/ℓ) = −1 ⇒
orbit-solved (T1_TEMPLATE Thm 1.3(b)). (2) Good 𝔮: ℓ ≡ 1 (4), φ non-square ⇒ ord φ even and C = φ⟨φ²⟩ = non-squares in
⟨φ⟩, so (n/ℓ) = (−1/ℓ)((−n/4)/ℓ) = −1 automatically; ℓ ≡ 3 (4), φ square ⇒ C ⊂ squares and (−1/ℓ) = −1. |C| ≥ m/2.
(3) [K(i, √φ) : K] = 4 (K(√φ)/ℚ non-Galois, K(i)/ℚ abelian), so good 𝔮 have density ½ among primes of K and
rational primes with a good 𝔮 above them have lower density ≥ ¼. (4) ord_𝔮(φ) ≤ y ⇒ ℓ | N(φ^j − 1) for some j ≤ y;
Σ_{j≤y} log|N(φ^j − 1)| ≪ y², so ≪ y² such ℓ; with y = ℓ^{1/2}/log ℓ this is O(x/log²x) in [x/2, x]. (5) Montgomery's
arithmetic large sieve: |𝒩| ≤ (X + L²)/J, J ≥ Σ_{ℓ∈𝒫, ℓ≤L} ω(ℓ)/ℓ ≫ Σ_{dyadic x≤L} (x/log x)(x^{−1/2}/log x) ≍
L^{1/2}/log²L; L = X^{1/2} gives ≪ X^{3/4}log²X. Only the unconditional Chebotarev density theorem is used. ✓
*Check* (`review_uo_misc.py` (d)): for all split ℓ < 3000 and both 𝔮 | ℓ: |S_ℓ| = |C| ≥ ord/2 for every good 𝔮, and
"n ∈ S_ℓ ⟺ (∃k: 𝔮 | a_k) ∧ (n/ℓ) = −1" on all 574 004 pairs (𝔮, n).

### C11. Theorem 5.2 — SOUND (CONDITIONAL; m7)
Algebra re-derived as in R183 C7 with p → n: (t/𝔮) = (−1/ℓ)(n/ℓ)(φ/𝔮) = 1 for t = −n/(4φ), squares = ⟨φ²⟩. Lenstra
(1977) Cor. 4.8 with W = ⟨φ⟩, F = K(i, √n), C = {σ(i) = i, σ(√n) = −√n}: F/K is biquadratic because −1, n, −n ∉ K^{*2}
exactly when n ∉ T (−n < 0 at both real places); L₂ = K(√φ) ⊄ F (signature of φ is (+, −), of −1, ±n: (−,−), (±,±));
L_l non-abelian for odd l. So d(M) > 0 under GRH. The author's stated check "K(√n) ⊄ K(i, √φ)" is not Lenstra's
criterion (the relevant one is L_l ⊄ F) — the conclusion is right, the justification should be replaced (m7).
EVIDENCE (71 = |T ∩ [3, 10⁴)| non-solved odd n) not re-run by me; T1_TEMPLATE-level analogue was checked in R183.

### C12. Proposition 6.1 — SOUND
Re-derived: v_q(z) = 2s − 2c ≥ 0 ⟺ s ≥ c when s < 2c; v_q(z) ≥ 0 when s ≥ 2c; 2-adically 4 | g + 1. Hence z ∈ ℤ ⟺
Q | g + 1 ⟺ 4Q | g + 1. *Check* (`review_uo_misc.py` (b)): 51 558 shots, z ∈ ℤ in 3 100, criterion agrees in all —
identical totals to the author's.

### C13. Theorem 6.2 — SOUND (as scoped)
(i) Over ℤ the only positive unit is 1 ✓; the Assessment "Σ_{Q∈⟨S⟩} τ(n + 4Q²)/φ(4Q) converges" is correct as a
heuristic (Σ_{Q∈⟨S⟩} Q^{ε−1} = ∏_{q∈S}(1 − q^{ε−1})^{−1} < ∞). (ii) example verified. (iii) ✓. The equality "ES-solutions
= ES^{(S)}-solutions + g ≡ −1 (4Q)" is correctly restricted to the orbit family; the ES solution
4/169 = 1/52 + 1/234 + 1/6084 checks.
