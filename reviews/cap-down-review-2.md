# Hostile review #2 of CAP_DOWN.md (O237) — R243, round 1

Reviewer: R243 (side-agent/review-cap-down-2). Round 1: no edits to the author's files. Reviewed: CAP_DOWN.md as merged
from side-agent/cap-down (iteration Z7-1/Z7-2 + self-review repairs), BRAINSTORM/z13_*.md. From-scratch scripts:
`scripts/review_r243_lemmas.py` (lemmas, exact Fractions), `scripts/review_r243_caps.py` (numerics). Pollack's paper
(author's PDF, pollack-math.net/generalsplit6.pdf) archived as `sources/r243/pollack-ijnt2014-generalsplit6.{pdf,txt}`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (general Type II window with cap) | SOUND |
| Thm 1.2 (even windows fire, (E)) incl. Def 1.1 compatibility of the 2^t in d | SOUND |
| Prop 1.3 (one-prime witness d = K·s^{o/2}, cap ≤ (q−3)/4) | SOUND |
| §1 "excluded case genuinely not forced / 2 unusable" (Assessment + verdict 1) | SOUND-AFTER-REPAIRS (false as worded: 2 IS usable when ord_q(2)/2 ≤ v₂(K), always at q = 3; D1) |
| Cor 2.1 (n₀^{1/4+ε} for n ≡ 1 (8), n₀^{1/2+ε} for n ≡ 5 (8); squares via d = n/p), rel. Pollack Thm 1.4 | SOUND |
| Lemma 3.1 (all ES^{(y,e)} solutions at fixed x) | SOUND |
| T1 for Lemma 1.1 (§3) | SOUND |
| Prop 4.1(a) (sharpness at a single window) | SOUND |
| Prop 4.1(b) (one-prime witness at composite windows) | SOUND-AFTER-REPAIRS (D3) |
| Prop 6.1 (order-3 necessary condition) | SOUND (Reading = Assessment, correctly labelled) |
| §5 numerics (39 175 primes cap 0 at m ≤ 63, record 87 481; 87 759 non-squares, only 3985 cap 1; squares) | SOUND, reproduced exactly; the 3985 explanation is wrong (D2) |
| §1 forced-window statistics (means, maxima, 9161) | SOUND, reproduced exactly; reading needs D1 |
| Novelty | No prior ES use of Pollack-type detector bounds found (quick search); related: Dahan 2026 Thm 4.6 |

No FATAL defects. No MAJOR defects. Four MINOR defects (D1–D4) plus remarks.

## Detailed checks

### Lemma 1.1 — SOUND
Re-derived. 4/n − 1/K = m/(nK); 1/(nA) + d/(nKA) = m/(nK) ✓. All primes of d divide K, none divides m (s | K, s | m ⇒ s | n,
excluded by (i)); so v_s(A) = v_s(K + d) and v_s(z) = b + v_s(A) − c equals b (c < b), ≥ b (c = b), 2b − c (c > b) ✓.
2-part of den z trivial by (ii), odd parts even by (iii), coprime to n by (i), s | A | y when c_s > 2b_s ≥ 2 ✓. No prime
outside K can occur in den z (den z | d up to cancellation) ✓.
*From scratch:* exhaustive over all odd n ≤ 600, windows m ≤ 60, every K-smooth d ≡ −K (mod m) with c_s ≤ 2b_s + 6
(51 725 triples): Lemma 1.1's predicted cap (None when (ii)/(iii) fail) equals the least e with the triple in
EXPONENT_CAP Def 1.1, computed directly from den z, y, n with exact Fractions — no mismatch. Note this also confirms the
converse direction (a triple violating (ii)/(iii) is in no ES^{(y,e)}), which Lemma 3.1 later uses.

### Thm 1.2 — SOUND
Re-derived line by line: gcd(K, qn) = 1 ✓; (K/q) = (n/q) = (q/n) = −1 (Legendre/Jacobi reciprocity with n ≡ 1 (4),
q prime) ✓; (K′/q) = (2/q)^t (K/q) = −1 under (E) (so K′ > 1 automatically) ✓; H contains a non-residue ⇒ |H| even ⇒
−1 ∈ H (cyclic F_q^*) ✓; −K′ a residue of odd order o, h = (−K′)^{(o+1)/2} ∈ H with h² = −K′ ✓; d = 2^t ∏ s^{2a_s} ≡ −K ✓;
e ≤ max(a_s − b_s) ≤ (q − 2) − 1 ✓ (q = 3: e = 0). Mod-8 case split ✓ (n ≡ 1: q ≡ 3 (8) ⇒ v₂(n+q) = 2, t = 0;
n ≡ 5, q ≡ 3 (8) ⇒ t = v₂(n+q) − 2 ≥ 1).
*Def 1.1 compatibility of 2^t (the point the brief flags):* Def 1.1 constrains only primes of **den z**, not of the
Type II divisor d. With c₂ = t = b₂, Lemma 1.1 gives v₂(z) = b₂ + v₂(A) − c₂ ≥ b₂ ≥ 0, so 2 ∤ den z; the 2^t factor
is admissible. (It would not be if c₂ > 2t, which is exactly why the excluded case cannot use the non-residue 2.) ✓
*From scratch:* every non-square n ≡ 1 (4), 5 ≤ n ≤ 3000 (all prime factors allowed, incl. ≡ 3 (4)), every prime
q ≡ 3 (4), q < 300, q ∤ n, (q/n) = −1: 9 605 (n, q) pairs satisfy (E); for each, ALL square roots h of −K′ in ⟨S⟩
(own BFS) give d with (x, y, z) passing Def 1.1 with e ≤ q − 3; (K′/q) = −1 asserted. The 2 041 pairs failing (E) are
all n ≡ 5, q ≡ 3 (8), v₂(n+q) odd ✓.
Minor remarks: see defects D1 (the "excluded ⟹ not forced" wording).

### Prop 1.3 — SOUND
Existence of s: (K′/q) = ∏(s/q)^{b_s} = −1 ⇒ some odd s with b_s odd, (s/q) = −1 ✓. Non-residue in cyclic group of
order 2u (u odd) has v₂(o) = 1, s^{o/2} = −1 ✓. c_s = b + o/2 even (both odd) ✓; c₂ = t, other c = b ✓; cap
max(0, (o/2 − b)/2) ≤ ((q−1)/2 − 1)/2 = (q − 3)/4 ✓.
*From scratch:* for all 9 605 pairs above and EVERY eligible s, the triple from d = K·s^{o/2} has Def 1.1 cap exactly
max(0, (o/2 − b)/2) and 4e ≤ q − 3 (exact). The "e.g. s ≡ −1 (mod q)" special case (o = 2) ✓.

### The excluded case of Thm 1.2 — wording false (D1)
Thm 1.2 itself only *excludes* (n ≡ 5, q ≡ 3 (8), t = v₂(K) odd) from its hypothesis; that is fine. But §1 ("using it costs
a 2-exponent that is uncontrolled"), §7 item 1 ("the forced non-residue is 2 itself, which is unusable") and
BRAINSTORM/z13_pollack_quarter ("Barrier") say more. In the excluded case 2 is a non-residue mod q, o₂ := ord_q(2) has
o₂/2 odd, and the Prop-1.3-type witness **d = K·2^{o₂/2}** has c₂ = t + o₂/2 and all odd c_s = b_s; by Lemma 1.1 it is
admissible (cap **0**) iff o₂/2 ≤ t. So the excluded window fires with an honest ES solution whenever
ord_q(2)/2 ≤ v₂(K). In particular **q = 3 always fires** (o₂/2 = 1 ≤ t; d = 2K, i.e. the classical n ≡ 2 (3) solution).
*From scratch* (`check_excluded_case`, n ≡ 5 (8) non-square ≤ 3000, q ≡ 3 (8) < 300): 2 041 excluded pairs; 98 fire at
cap 0 via d = K·2^{o₂/2} (all 85 q = 3 pairs among them); exhaustively, 1 825/2 041 have a Lemma-1.1 solution at some cap
≤ 40 and 216 have none (e.g. n = 5, q = 67, K = 18) — so "not forced" is right, "unusable" is wrong.
For the primes p ≡ 5 (8) ≤ 10⁶: of the 9 161 whose least q ≡ 3 (4) with (q/p) = −1 is excluded, **6 533 have that q = 3,
which is a cap-0 window** (`review_r243_caps.py … forced`). So the q_new statistics of §1 measure "least Thm-1.2
window", not "least firing window". No exponent in Cor 2.1 changes (the gain is confined to the finitely many q | 2^k + 1,
k odd ≤ t), so this is MINOR.

### Cor 2.1 — SOUND (relative to Pollack, ineffective)
*Source:* Pollack, "Prime splitting in abelian number fields and linear combinations of Dirichlet characters", author's
PDF (archived sources/r243/). Thm 1.4 verbatim: X finite group of (primitive) Dirichlet characters, conductor f, exponent
dividing n; ξ ∈ ℤ[X] with ξ(0) = a_1 = ±1; W := max{W_{ξ⁺}, W_{ξ⁻}}, W_η = ∏ f_χ^{a_χ} (Def 1.3), ξ⁻ = −(negative part);
L ≥ length; then the least prime q ∤ f with ξ(q) ≠ 0 is ≪ W^{1/4} f^ε, constant depending only on n, ε, L. Ineffectivity:
Prop 3.3 lower bound |L(1, χ)| ≫_ε f^{−ε} for real χ is Siegel (printed p. 10–11 of the preprint) ✓. The author's
transcription is accurate. I could NOT access the IJNT version; journal/pages (IJNT 10 (2014) 885–903) unverified (D4).
*Hypotheses:* (a) n₀ > 1 squarefree with all primes ≡ 1 (4) ⇒ n₀ ≡ 1 (4) a fundamental discriminant; X = {1, χ₋₄,
χ_{n₀}, χ_{−4n₀}} is closed under primitive multiplication, exponent 2, f = 4n₀ ✓. ξ = 1 − χ₋₄ − χ_{n₀} + χ_{−4n₀},
ξ(0) = 1, length 4; ξ⁺ = 1 + χ_{−4n₀} (W = 1·4n₀), ξ⁻ = χ₋₄ + χ_{n₀} (W = 4·n₀) ⇒ W = 4n₀ ✓. For q ∤ f, ξ(q) =
(1 − χ₋₄(q))(1 − χ_{n₀}(q)) (multiplicativity valid as q ∤ f) ∈ {0, 4}, ≠ 0 ⟺ q ≡ 3 (4), (n₀/q) = −1; (n₀/q) = (q/n₀)
(n₀ ≡ 1 (4)) = (q/n) (q ∤ m automatically, as q ≡ 3 (4)) ✓. Thm 1.2 needs n ≡ 1 (4), q ∤ n ✓, and for n ≡ 1 (8) no
exclusion ✓; n ≡ n₀ (mod 8) so the split is by n₀ ✓. e*(n) ≤ (q−3)/4 < q ≪_ε n₀^{1/4+ε}, constant depends on ε only
(Pollack's n = 2, L = 4 fixed), uniform in the square part m ✓. (b) recomputed: ξ⁺ = 1 + χ₈ + χ_{−4n₀} + χ_{−8n₀},
ξ⁻ = χ₋₄ + χ₋₈ + χ_{n₀} + χ_{8n₀}, both weights 8·4n₀·8n₀ = 4·8·n₀·8n₀ = 256n₀² ✓; detects q ≡ 7 (8), (q/n₀) = −1 ✓.
Remark (2) (O236 class has W = 256n₀² for n ≡ 1 (8) too) recomputed ✓.
*Remark (3) (divisor routes):* scaling 4/d = … by k = n/d: den(kz) = den z because every prime of k divides d and den z
is prime to d; rad den z | y | ky; coprime to n (same primes as d) ✓. (The stated reason "gcd(K_d, n/d) = 1" is true but
not what is needed.) Squares: d = a²/p has squarefree part p, d ≡ p (8) ✓. The n ≡ 5 (8) refinement (u ≡ 5 (8),
d = n/u ≡ 1 (8)) ✓.
*Ineffectivity* is labelled (Remark 1) ✓. Remark (4) "1/4 is Burgess's barrier" is an Assessment ✓.

### Lemma 3.1 — SOUND
Re-derived ((my − N)(mz − N) = N², D₁ = my − N; a den-z prime ℓ divides D₁ and y hence N; v_s(m) = 0 for s | 2nx since
gcd(m, nx) = 1 and m odd; local formula (c − 2b)⁺). *From scratch:* every odd n ≤ 61, every admissible x, every y with
D₁ ≤ min(N², 30 000): 845 011 (n, x, y) — Lemma 3.1's membership/cap prediction equals the direct Def 1.1 cap in all
(including "in no ES^{(y,e)}"). Example n = 5, x = 2, D₁ = 50 ✓.

### T1 for Lemma 1.1 — SOUND
Re-derived ((d/m) = −(K/m) = −(a²/m) = −1 vs (s/m) = 1 for every s | K: odd s via Jacobi reciprocity with
(m/s) = (−1/s), s ∤ a by gcd(K, n) = 1; s = 2 forces m ≡ 7 (8)). *From scratch:* odd a ≤ 59, windows m ≤ 200, caps ≤ 4:
0 hits; odd a ≤ 999, m ≤ 400, cap ≤ 3: 0 hits.

### Prop 4.1 — (a) SOUND; (b) SOUND-AFTER-REPAIRS (D3)
(a) Re-derived (c − 1 ≡ (q−1)/2 (mod q−1), c − 1 ∈ {−1, 0} impossible for q > 3, c = (q+1)/2 even). *From scratch:*
3 001 cases (q ∈ {7, 11, 19, …, 83}, K prime primitive mod q), exhaustive c < 3q: least cap = (q−3)/4 in all.
(b) The proof's "each component has 2-part ℤ/2" needs q_i ≡ 3 (4); true for CAP_POINTWISE Thm 1.1′ windows but not
stated in Prop 4.1(b) (D3). Negative j (|j| ≤ b) is covered by the max{0, ·}. The example n = 5, m = 567, K = 143:
ord_{81}(11) = 54, ord_7(11) = 3; ord_{81}(13) = 27, ord_7(13) = 2 — no prime with even order in both components ✓.

### Prop 6.1 — SOUND (necessary condition only)
Checked against SYNTHESIS_SPARKS2 Prop 3.1 (E = (n + 18D)/g, x = (ωn + E)/9, a = (g + ω²)/9). 9x ≡ ωn (mod r) ⇒
n ≡ 9ω²x; r | n + 18Q³ ⇒ Q³ ≡ −ω²x/2 ✓. Mute-set equivalence: for s | Q, s ∤ 3n (hence s ∤ r): s | a ⟺ g ≡ −ω² ⟺
n + ω²r ≡ 0 ⟺ s | ω²(ωn + r) = 9ω²x ✓. Units of ℤ[ω] are μ₆, x ∈ ⟨S⟩μ₆ when x is prime to 3 ✓. Residue-field spot
check (`check_prop61`, 20 000 random instances) ✓. The window is E = r, so g = (n + 18Q³)/r must still be ≡ g₀ (mod 18):
another constraint, only strengthening "necessary". The Reading (anchor constant, degree-2 accident) is Assessment ✓.
