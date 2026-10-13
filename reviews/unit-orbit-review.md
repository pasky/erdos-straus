# R186 — hostile review of O186 UNIT_ORBIT_ES.md (reviewer 1 of 2, full document)

**Repairs applied (R186, author O186 parked):** M1 and m1–m8 applied directly, each marked "(R186 repair …)":
UNIT_ORBIT_ES.md (§0 L1/L2, §1 shape definition, Thm 2.4 label + (b), new Cor 2.5, Remark (1), Prop 3.2, §4(a),
Assessment 4.2 + Galois paragraph (η_MP), §5 citation, Thm 5.2 proof), AGENT_REPORT_O186.md (SHARP 1, SHARP 3, SHARP 4
citation, Prop 3.2 line), BRAINSTORM/bsL_finite_mute.md (Cor 2.5), bsL_sieve_saturation.md (citation). Where a repair
annotates a diagnosis (M1), the author's original sentence is kept next to the annotation.

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

## Defects

### FATAL
None.

### MAJOR
**M1 (§0 (L2), §4 Prop 4.1 Consequence (a), Assessment 4.2 "Hypothesis responsible", AGENT_REPORT SHARP 3: the
Kummer condition is mis-identified as the barrier; for V_φ the barrier is the unit rank).**
(i) *V_φ.* For a split ℓ = 𝔮𝔮' ≡ 3 (mod 4): (−φ/𝔮') = (σ(−φ)/𝔮) = (φ^{−1}/𝔮) = (φ/𝔮), so
(−φ/𝔮)(−φ/𝔮') = (−φ²/𝔮) = (−1/ℓ) = −1: **exactly one prime above ℓ satisfies the forced Kummer condition**
(verified for all split ℓ ≡ 3 (4) below 3000, `review_uo_misc.py` (d)). Hence the forced condition only *selects* 𝔮,
and the full shot condition at ℓ ≡ 3 (mod 4) is a condition on ℓ alone: ℓ ≡ 3 (4), ℓ ≡ ±1 (5), (n/ℓ) = −1 (all
congruences) and ⟨−1, φ⟩ = F_ℓ^* (i.e. the root of t² − t − 1 that is a square mod ℓ has order exactly (ℓ−1)/2; the group
⟨−1, t⟩ = ⟨−1, −1/t⟩ does not depend on the root). This is a **rank-1 Artin problem with congruence conditions** — open unconditionally because
one generator is far below what Gupta–Murty (rank ≥ 4 at level ½) or Heath-Brown (3 independent generators, one of
which works) can handle — and no non-norm Chebotarev condition is involved. So the statement in §0 (L2) "Hypothesis of the
barrier that the variant satisfied: the orbit is a coset ηU² with η not a square (forced by a mute REAL place)", the
sentence "Hypothesis responsible: the mute place is REAL …" of 4.2, and SHARP 3 of the report misattribute the
obstruction for V_φ: what differs between V_φ and ES^{(S)} is the rank (1 vs |S| ≥ 4), not (only) the type of mute place.
(ii) *Assessment 4.2, first step.* "An Artin-type sieve for a number-field variant must count degree-1 primes of K with
a non-norm Frobenius condition; then E ⊇ K" is not justified: one may sieve the rational primes ℓ with the
condition "some 𝔮 | ℓ has the prescribed Frobenius", a union of classes in Gal(K̃(√U_𝔪)/ℚ), and apply Murty–Murty /
Murty–Petersen over the base ℚ; the level is then governed by abelian subgroups meeting *that* union, not by [K:ℚ].
(i) is the extreme case (the union contains a pure congruence condition). sources/uo/LITERATURE.md Q1 itself says only
that the Galois-closure route "does not help in general". The Galois paragraph (G-invariant central condition) is not
affected by this (there the condition is the same at every 𝔮 | ℓ).
*Repair.* (a) In §4(a) add: "for split ℓ ≡ 3 (mod 4) exactly one 𝔮 | ℓ has (−φ/𝔮) = −1, so the condition is free; the
unconditional V_φ problem is the rank-1 Artin problem ⟨−1, φ⟩ = F_ℓ^* for ℓ ≡ 3 (4), ±1 (5), (n/ℓ) = −1". (b) In
§0 (L2), 4.2 and SHARP 3 replace "the responsible hypothesis is the real mute place" by "the unit rank of the orbit (1
for V_φ) and, for higher-rank r₁ = 1 fields, Kummer conditions when MP is applied over the base K; whether the
Galois-closure/base-ℚ route avoids them is not checked". (c) Restate 4.2's conclusion as "with Murty–Petersen applied
over base K".

### MINOR
**m1 (Cor 1.2, §1).** "Type I/II" is never defined for ES^{(S)}. *Repair:* add after the Definition: "At ℓ | n
(ℓ ∉ S) write v_ℓ(z) = v_ℓ(Z); with v_ℓ(n) = 2s, Type I = one of x, y, z has v_ℓ ≥ 2s and two are ℓ-units, Type II =
one ℓ-unit and two with v_ℓ ≥ 2s (T1_TEMPLATE Thm 2.1(d))", and note that Thm 2.1(a)–(d) are used in their local
form (proofs need only v-integrality at the place in question).

**m2 (Thm 2.4(b)).** "ES^{(S)}(n) has no solution of Type I/II shape at all" is literally false when m has two or more
primes. Counterexample (`review_uo_twoprime.py`): n = (13·19)² = 61009, S = {3, 5, 7, 11}, partial box
(n/4 < x < n/4 + 1500, x ≤ y ≤ 4n): 393 ES^{(S)} solutions, of which 105 are Type I at 19 (other at 13), 34 Type II at 19,
83 Type I at 13, 22 Type II at 13; none Type I/II at both. *Repair:* "… no solution has Type I/II shape at every prime of
n (Cor 1.2)".

**m3 (Thm 2.4, Remark (2), report "Effective version").** The proof is ineffective (BV ⇒ Siegel–Walfisz): it gives
no bound for the least Q in terms of n. *Repair:* add "(ineffective: no bound on Q)" to the theorem's label.

**m4 (missed corollary; Remarks after Thm 2.4, AGENT_REPORT).** For |S| ≥ 4, **ES^{(S)}(n) holds for every n > 1
coprime to 2S, squares included**: if 4/d = 1/x + 1/y + Q²/Z with gcd(Z, Q) = 1 and k is coprime to S, then
4/(kd) = 1/(kx) + 1/(ky) + Q²/(kZ) with gcd(kZ, Q) = 1; write n = t^{2^j} with t > 1 a non-square and apply Thm 2.4(a)
to t. (Consistent with the T1: the inherited solutions are "other"-shaped at the primes of n, as C2's box data show.)
So ES^{(S)} is a *fully proved* variant for |S| ≥ 4, and the T1 is purely a statement about shapes. *Repair:* add
as Cor 2.5 and make Remark (1) say "the *mechanism* is exact-T1; the *variant* holds everywhere".

**m5 (Assessment 4.2).** The letter η denotes both an orbit element (§§2–5) and the Murty–Petersen level exponent.
*Repair:* rename the latter (e.g. η_MP).

**m6 (Prop 3.2, §0 (L1)).** The hypothesis n ≡ 1 (mod 8) is only a sufficient condition for n ∈ K_v^{*2}, v | 2. For
K = ℚ (ES^{(S)}) the identity holds for all n ≡ 1 (mod 4) (Jacobi reciprocity, a > 0), and for K = ℚ(√5) also for
n ≡ 5 (mod 8) (5 ∈ ℚ₄^{*2}); `review_uo_misc.py` (c) control: 7 000 / 7 000 shots with n ≡ 5 (8) over ℚ(√5) have total
symbol +1. *Repair:* state "n ∈ K_v^{*2} for all v | 2 (e.g. n ≡ 1 (8))" and note that for ES^{(S)} and V_φ the no-reciprocity
statement covers all n ≡ 1 (mod 4).

**m7 (Thm 5.2 proof).** "Lenstra's theorem applies because K(√n) ≠ K and K(√n) ⊄ K(i, √φ)" is not Lenstra's
criterion. *Repair:* cite Lenstra (1977) Cor. 4.8 as in R183 C7/m8: W = ⟨φ⟩, F = K(i, √n), L₂ = K(√φ) ⊄ F,
L_l (l odd) non-abelian; and state GRH as GRH for ζ_{K(ζ_m, φ^{1/m})}, m squarefree.

**m8 (§5 "Contrast with ES", bsL_sieve_saturation).** "DISCOVERIES (A)19–20" should be **(D)19** (large sieve cap; also
(D)22 for prime-only majorants), and that cap is "PROVED, conditional on KARY2 Thm 5.1", not unconditionally "proved".
*Repair:* fix the reference and the qualifier.

## Labels
PROVED labels on Lemma 1.1, Cor 1.2, Prop 2.1, Lemma 2.3, Props 3.1, 3.2, 4.1, 6.1 are justified; "PROVED relative to
standard sieve theorems" for Lemma 2.2 / Thm 2.4 and "relative to the large sieve and Chebotarev" for Thm 5.1 are
justified (both use only BV / Montgomery / unconditional Chebotarev density); Thm 5.2 CONDITIONAL (GRH) is right.
Assessments 4.2, Galois paragraph, Remark (4), the Thm 6.2 lottery are correctly labelled, but 4.2's diagnosis needs M1.
"ES is not solved, nor any infinite case of ES" — correct; nothing here bears on ES itself (Prop 6.1 / Thm 6.2 say so).

## Process note
Round 1 left repairs to the parent; the orchestrator then reported the author parked, so all repairs were applied by R186 (see top). At the time of round 1 (12:20) the author's worktree (side-agent/unit-orbit-es, last commit
2f229f86 at 12:04, clean tree) was idle but present.
Reproduce: `cd scripts; PYTHONPATH=. uv run --with sympy --with numpy python review_uo_evidence.py 200000 30000`
(4 s), `… review_uo_squares.py 3 300 169 289 361` (+ `--noparity`, ~30 s each), `… review_uo_twoprime.py` (6 s),
`… review_uo_misc.py` (~4 min).
