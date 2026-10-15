# R249 — hostile review of O242 (SIBLING.md, BRAINSTORM/z17_*.md, AGENT_REPORT_O242.md)

Reviewer: R249 (side-agent/review-sibling). Author branch merged: side-agent/sibling-conj.
Status: round 1 complete (r = 19 depth-5 spot check still running). Repairs applied: none (author's branch is unchanged since the review started; parent to decide on forwarding vs. reviewer repairs).

## Summary verdicts
| claim | verdict |
|---|---|
| Lemma 1.1 (≤ 2 balls per key (m′, g′, s, a) in a parent; 3 deg Q > deg F) | **SOUND** (re-derived; 274 tuples s ≤ 15, max 1) |
| Lemma 1.2 (≤ 6 P-boxes per (c, d) per class, r ≤ 17) | **SOUND** (m1: "⌈√(r/2)⌉ + 1" should be ⌈√(r/2)⌉) |
| Prop 1.3 (Klein symmetry of Case B balls; parity law) | **SOUND** (re-derived; brute-force on own tuples s ≤ 17: 178 balls, as author; O241 ball list) |
| Prop 3.1 (route-type counts do not localise; window (n, 5n]) | **GAP** (D1 MAJOR: central inequality false for the natural localised route R2L; proof sentence wrong; PROVED only for an explicit list; D2 citation label) |
| Cor 4.1 (pair-count forms) | (i), (iii) **SOUND**; (ii) **SOUND-AFTER-REPAIRS** (D3: needs an alive depth-N₀ cylinder) |
| Conjecture 4.2 + "PROVED consequence" + "sharp threshold at 17" | data **REPRODUCED** (r ≤ 31 to depth 4, r ≤ 61 to depth 3, all r ≤ 13 at level 1); label CONJECTURE correct; consequence **GAP** (D5 MAJOR: needs level-1 survival, certified only for r < 2·10⁴) ; D6 heuristic |
| §2.1/§2.3 Poisson calibration (EVIDENCE) | numbers **wrong** (D4: with-replacement model; exact 0.062 not 0.145, pairs ×1.5 too high, "0.40" → 0.105); conclusions survive (data even weaker); "no attraction" → mild excess of pairs |
| §2.2 (siblings never share a key) | confirmed for the 12 Case-B–Case-B pairs at depth ≤ 8 (own code); the 2 others involve Case A |
| §5 digit uniformity | counts 61/60/51 confirmed |
| Labels overall | Prop 3.1 and the Conj 4.2 consequence over-labelled (D1, D5); everything else correctly labelled |

No FATAL defect. Two MAJOR (D1, D5), both repairable by rescoping/adding a hypothesis.

## Claim-by-claim

### Lemma 1.1 (≤ 2 balls per key (m', g', s, a) in a parent) — SOUND
Re-derived: EE' = T²L'²w₁C₁ − TL'(w₁ + C₁) + 1 = T^sL'g' + T²L'g'v₁ − T²L'g'v₁ + 1 = 1 + T^s m'g'² (using L'²/m' = L'g').
E + 1 = T m'g'w₁ ⟹ E ≡ −1 (mod m'g'); B_τ ⊂ V fixes E mod T^N (N = N(s)), gcd(T, m'g') = 1, so E lies in one unit class mod
Q = T^N m'g' (unit: E(0) = −1, E ≡ −1 mod m'g'). ρ = N + z + y, n = deg F = s + z + 2y, 3ρ − n = 3N − s + 2z + y ≥ s/2 > 0;
deg E = a + y + z fixed by the key. SP Lemma 1.4 (checked: hypotheses "F ≠ 0, ρ ≥ 1, σ unit, 3ρ > n", conclusion ≤ 2 divisors of
degree d in the class, monic or not) applies verbatim. No hidden hypothesis; the key must include a (it does) and s (it does).
From-scratch check (`scripts/review_r249_caseb.py`: own Case B enumerator, route E·C₁ = g'T^{s−1} + w₁ with a ≤ b plus the
w₁ ↔ C₁ swap, validated against an unpruned brute force over (m', w₁, C₁) for s ≤ 9 — identical tuple sets; dump
`scripts/review_r249_dump.py`, check `scripts/review_r249_check11.py`): q = 3, all 274 Case B tuples with s ≤ 15 — the maximum
number of distinct E per (key, parent) is **1** (the bound 2 is never attained in this range).
Remark (not a defect): the lemma is correct but, as the author says, bounds a quantity that the data show to be irrelevant
(siblings never share a key).

### Prop 1.3 (Klein symmetry of Case B balls) — SOUND
Re-derived the sign bookkeeping: (B₁) sign (−1)^{z+a+b−2} = (−1)^s; (B₂) needs a ≡ b (from a + b + z = s and z ≡ s) and
a + y + s ≡ 0 (from y + t = max(a, b), t ≡ s); E^σ sign y + z + a ≡ 0. All three use OA Cor 1.7 (z ≡ t ≡ s mod 2), which I
checked is stated for all odd q and k ≥ 2 (FF_ODD_ABSENCE.md l.110). The swap is an obvious symmetry of (B) and
(−E)(−E') = EE' ≡ 1 (mod T^s), s ≥ N + 1, so the inverse ball is the E'-ball of the same level. The maps are isometries of
T-adic cylinders, so "ball set invariant" is meaningful level by level.
From-scratch check (same 274 tuples, s ≤ 15, `scripts/review_r249_check11.py`): parity law holds on every tuple; y + t =
max(a, b) on every tuple; τ^σ is a valid Case B tuple and E^σ = E(−T) for every tuple (asserted); the 128 Case B balls of depth
≤ 9 (depths 3..8 complete; 9 partial until s = 16 is added) are invariant under u ↦ u(−T), u ↦ 1/u and ι; 32 are ι-fixed.
**Addendum (s ≤ 17, 348 tuples):** parity law, y + t = max(a, b), validity of τ^σ and E^σ = E(−T) hold on all; the Case B ball set
has **178 balls of depth ≤ 10 — exactly the author's census count** — and is invariant under all three maps (38 ι-fixed);
Lemma 1.1 maximum still 1 per (key, parent).
"Reading" (an involution fixing V fixes a child, so symmetry never forbids a triple): correct and trivially so.

### Lemma 1.2 (≤ 6 P-boxes per key (c, d) in a class mod r^{L−1}) — SOUND (one MINOR wording defect, m1)
Re-derived: Σ^II gives 4abd = N + e, e = (a + b)/c ≤ a + b ≤ 2b ≤ 2abd, so abd ≤ N/2 and a² ≤ N/2 for a ≤ b, i.e.
a ≤ √(r/2)·r^{L−1} (2.915·r^{L−1} at r = 17). −(4acd − 1) ≡ x (mod r^{L−1}) puts a in one class mod r^{L−1} (r ∤ 4cd), and
b(4acd − 1) = a + Nc fixes b. (4acd − 1)(4bcd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dN + 1 ≡ 1 (mod r^L) (2L − 1 ≥ L), so the
second box lies in x iff the first lies in x^{−1}. Number of a ∈ [1, X] in one class mod M is ≤ ⌈X/M⌉ = ⌈√(r/2)⌉: 3 for
r ∈ {11, 13, 17}, 2 for r ∈ {5, 7}, 4 for r ∈ {19, 23}. Bound 2⌈√(r/2)⌉ per key; "six" is right for r ≤ 17.
Level-L boxes come only from K = 2L − 1 (K = 2L is empty by the r-free reciprocity of M17 Lemma 1.3), so restricting to
"P-data of level L" loses nothing for the per-level statement.
From-scratch P-enumerator (`scripts/review_r249_rbox.c`, naive (a, b) scan; reproduces D_P(K) = 2, 32, 121, 258 at r = 17,
K = 1..7, and D_Q = 2, 73 (k = 1, 3, a ≤ b) of M17) — not separately tested for the per-key bound (it is a two-line argument).

### Prop 3.1 (window (n, 5n]: "every route-type bound inside a depth-n cylinder is ≥ 3^{2s/5}") — GAP (D1, D2)
What is right: at p* = (s; s/5, s/5, s/5, 2s/5) (b = 3s/5) the *fixed-data* counts of the listed routes R1 (3^{t−2}), R2
(3^{z+y}), R3 (3^{a−1+y}), R4 (3^{z+a−1}), R4L (3^{a+z−1+max(0, y−n+1)}) are all 3^{2s/5 − O(1)}, and so are those of every
other route of SP Lemma 1.6 that the text does not mention (I checked T0 3^{3s/5}, R4′/X1/X2 3^{4s/5}, R5a 3^{3s/5},
R6a ≥ 3^{2s/5}, R8a 3^{3s/5}, R9a/R10a ≥ 3^{3s/5}, R10b ≥ 3^{2s/5}). The arithmetic 2s/5 ≤ s/2 − n ⟺ s ≥ 10n ⟺ N ≥ 5n is
right, and so is "the global bound already reaches this threshold". The exponent-level conclusion for the listed routes holds.
Caveat on the citation: SS Cor 4.2 labels "the unique maximiser (1/5,1/5,1/5,2/5), value 2/5" as **EVIDENCE (grid)**; only the
bound q^{2s/5+o(s)} is PROVED there. Prop 3.1 does not actually need the maximiser property (it only evaluates routes at p*),
so this is a citation-label slip (m2), not a gap.
What is wrong: the proof's key sentence "their localised forms only change the multiplicity factor" is false in general —
R4L itself changes the fixed data, and so does the equally natural route **R2L**: fix m′ (3^z), then P := g′w₁ satisfies
m′P ≡ (e₀ + 1)/T (mod T^{n−1}) (E + 1 = T m′g′w₁, E ≡ e₀ mod T^n), so P (monic, degree y + a − 1) has ≤ 3^{max(0, y+a−n)}
choices; (m′, P) fixes E, and g′ | P is a divisor choice, q^{o(s)} by SS Lemma 4.1. Hence
  N_V(p*) ≤ 3^{s/5 + max(0, 2s/5 − n) + o(s)},
which is **< 3^{2s/5 − O(1)} as soon as n > 2s/5 + o(s)** (i.e. in the sibling regime n ≈ N(s) − 1 ≈ s/2). So the displayed
claim "every route-type bound for N_V(p*), localised or not, is ≥ 3^{2s/5 − O(1)}" is false for a natural localised route.
The *mass* conclusion survives for R2L: its relative-mass exponent is z + max(0, y + a − n) + n − s/2 ≥ s/10 > 0 for every n
(it is effectively a count of E in V), and the same holds for the analogous "fix one of (m′, g′, w₁), the product of the other
two in its class" routes and for counting E directly (3^{deg E − n}). So the window statement is plausibly true for a much wider
class, but the proposition as written proves it only for an explicit finite list, and its central inequality is false beyond it.
Severity MAJOR (the report's SHARP 2 headline "counts do not localise … every route-type bound" and the PROVED label in §6).
Repair (D1): restate Prop 3.1 as: "For each route of SP Lemma 1.6 (all rows), its modulus-localisations, R4L and R2L
(and the variants obtained by fixing one or two of m′, g′, w₁ and constraining the rest mod T^{n−1}), the bound on the relative
mass N_V(p*)·3^{n−N(s)} at p* is ≥ 3^{min(n − s/10, s/10) − o(s)}; hence < 1 only if s > (10 + o(1))n." Label PROVED for that
explicit list; "every route-type count / counts do not localise / Lemma 3.1 must be fed by positional information" → Assessment.
Replace "localised forms only change the multiplicity factor" by the R2L/R4L case analysis. (D2, MINOR) Cite SS Cor 4.2 only for
the PROVED upper bound; drop "unique maximiser" or label it EVIDENCE.
*Explicit form (Assessment).* Per-level terms of SS §5.3 confirmed (26.3, 9.15, 2.43, 0.60, 0.15, 0.039 at s = 40..90); they are
union-bound terms over both slices without the parity filter, so using them for one cylinder is conservative. Decay 3^{−0.127 s}
per level ⇒ tail ≈ 7.7·term(s₁); tail < 3^{2−n} gives s₁ ≈ 65 + 8n, not 80 + 9n (depth ≈ 33 + 4n rather than 40 + 4.5n; with
OA's parity factor ≈ 4 another ≈ 10 levels lower). Order of magnitude unaffected (m3).

### Cor 4.1 (pair-count forms) — (i), (iii) SOUND; (ii) GAP (missing hypothesis, D3)
(i): a full alive parent of depth N gives C(3, 2) = 3 pairs, so Π_N ≤ 2 ∀N ≥ 9 is (W) with m = 1, K = 1 at every alive depth
N ≥ 9; an alive depth-9 cylinder exists (SD §3 tree, complete for ball depth ≤ 9 — needs s ≤ 16 plus Case A α ≤ 7, both inside the
census s ≤ 17), so SD Lemma 3.1 with n₀ = 9 applies. ("no full alive parent before" is not used.) SOUND.
(ii) as stated ("Π_N(c) = 0 ∀N ≥ N₀ ≥ 9 ⟹ dim_H U_c ≥ log 2/log 3") needs an alive cylinder of depth N₀; for N₀ > 9 nothing
in the hypothesis or the data supplies one (if every depth-N₀ cylinder were dead the hypothesis holds vacuously-strongly and
U_c = ∅). Repair (D3, MINOR): add "and Π_N(c) ≤ 2 for 9 ≤ N < N₀" (then (i)'s argument keeps an alive depth-N₀ cylinder) or
"and some depth-N₀ cylinder of X_c is alive". (iii): starts from an alive class of depth 7 in C₅ (r = 17 tree complete to depth 7,
O241) — SOUND; K = 1 resp. 14, m = 1, transplanted Lemma 3.1 is formally identical in ℤ_17.

### §2.1 / §2.3 pair statistics and Poisson calibration (EVIDENCE / Assessment) — numbers wrong, conclusions survive (D4)
From-scratch recomputation `scripts/review_r249_poisson.py` (log below) with the *exact* uniform model: the b_d balls of depth d
are b_d **distinct** cylinders among M = 3^{d−2}; a given parent has all three children with probability
b(b−1)(b−2)/(M(M−1)(M−2)), two given balls are siblings with probability 2/(M − 1).
* §2.3 "expected number of alive full parents over depths 3–9 = 0.145, P(none) ≈ 0.86": the author's `A·p³` (independent
  children, p = b/M) counts impossible configurations (0.037 at d = 3 with b = 1 ball, 0.022 at d = 4 with b = 2). Exact:
  **0.062, P(none) ≈ 0.94**; E[alive parents with ≥ 2 ball children] = **2.39** (author 2.90; observed 2).
* §2.1 "expected pairs b(b−1)/2/#parents": exact is C(b, 2)·2/(M − 1) = b(b−1)/(3·#parents − 1), i.e. the author's
  expectations are ≈ 1.5× too large at q = 3: exact 0.25, 0.46, 1.65, 0.64, 1.04, 0.30 (d = 4..9; total 4.34) against observed
  1, 0, 4, 1, 1, 0 (total 7, author's expectation total 6.4). So the q = 3 data show **mild attraction** (7 vs 4.3; Poisson tail
  P(X ≥ 7 | 4.34) ≈ 0.15, driven by d = 6, where §2.2 reports Case A + Case B pairs), not "neither repulsion nor
  attraction". (At r = 17 the factor is (r−1)/r·r/(r−1) ≈ 1, so the r = 17 row is essentially right.)
* "No triple among all q = 3 parents (expected 0.40 over depths 5–9)": the script's C(b,3)/npar² omits the factor 2/9
  ("three distinct children of one parent"), and 0.40 is the d = 6–9 sum. Exact (depths 5–9, all parents): **0.105**.
Effect: every correction makes the depth ≤ 9 data *weaker* evidence for the sibling conjecture, which is the author's own
conclusion; the "Poisson-like" description should become "consistent with uniform placement, mild excess of pairs at d = 6".
Repair (D4, MINOR): replace the numbers as above (or label the model as the with-replacement approximation and drop d = 3, 4).
    3 alive: E3 0.0000 E>=2 0.000 | all parents: E3 0.0000, E[sibling pairs] exact 0.000 (author C(b,2)/npar = 0.000)
    4 alive: E3 0.0000 E>=2 0.167 | all parents: E3 0.0000, E[sibling pairs] exact 0.250 (author C(b,2)/npar = 0.333)
    5 alive: E3 0.0082 E>=2 0.291 | all parents: E3 0.0123, E[sibling pairs] exact 0.462 (author C(b,2)/npar = 0.667)
    6 alive: E3 0.0413 E>=2 0.895 | all parents: E3 0.0696, E[sibling pairs] exact 1.650 (author C(b,2)/npar = 2.444)
    7 alive: E3 0.0053 E>=2 0.340 | all parents: E3 0.0098, E[sibling pairs] exact 0.645 (author C(b,2)/npar = 0.963)
    8 alive: E3 0.0066 E>=2 0.542 | all parents: E3 0.0124, E[sibling pairs] exact 1.038 (author C(b,2)/npar = 1.556)
    9 alive: E3 0.0006 E>=2 0.154 | all parents: E3 0.0011, E[sibling pairs] exact 0.297 (author C(b,2)/npar = 0.446)
    depths 3-9 alive parents: E[triples] exact 0.0620 (binomial p^3 model: 0.1453), P(none)~0.940; E[>=2] 2.389
    all parents, depths 5-9: E[triples] exact 0.1052

### §2.4 r-landscape and Conjecture 4.2 (uniform multiplicity ≤ 3 from depth 4) — data REPRODUCED; label CONJECTURE correct;
### the "PROVED consequence" has a hidden hypothesis (D5); the "out of reach" heuristic is internally inconsistent (D6)
From-scratch engine: `scripts/review_r249_rbox.c` (P: naive scan of all a ≤ b, ab ≤ N/2, e = (−N mod 4ab), both orientations,
r ∤ cd; Q: Σ^I_F via e | 4a²d + 1 with e ≡ −F^{−1} (mod 4ad), ad ≤ F/2 + 1/4 (re-derived from e ≤ a + b ≤ 2b), boxes −4a²d and
−4b²d, r ∤ e; every datum verified against its defining equation) + `scripts/review_r249_rtree.py` (alive tree in the
non-residue cells; boxed children counted only below alive parents). Box types P, Q (Q⁻¹ = Q, √Q = ∅, U ⊂ P) are taken from
M17/M17B Lemma 1.1 and M17 Lemmas 1.3, 5.1, 5.2, whose proofs I re-read and found r-free (Jacobi reciprocity with
f ≡ −1 mod 4d; nothing uses 17 beyond being an odd prime) — so the reduction itself is shared with the author, the
enumeration is independent (different algorithm: the author uses the ET four-regime factoring enumerator).
Results (all agree exactly with `data/z17/landscape_d4.txt`, `rtree19_d6.txt`, `rtree23_d6.txt` where they overlap):
* r ∈ {5, 7, 11, 13}: every non-residue cell is a level-1 box. ✓
* surviving cells: 17: {5, 7}; 19: {2, 3, 10, 13}; 23: {5, 14}; 29: 6/14; 31: {3, 6, 21, 26}; 37: 6; 41: 14; 43: 10; 47: 6;
  53: 8; 59: 10; 61: 14 ✓ (all twelve).
* max boxed children of an alive parent, d2/d3/d4: 17: 4/4/2; 19: 7/5/2; 23: 8/5/3; 29: 5/4/2; 31: 10/2/2 ✓, min alive fraction at
  d4 0.6782, 0.5698, 0.5800, 0.8002, 0.6621 ✓; d2/d3 for 37..61: 5/4, 3/3, 7/3, 14/3, 4/3, 8/3, 6/4 ✓. Histograms at r = 19, 23
  (d ≤ 4) identical to the author's. (Depth 4 for r ≥ 37 and depths 5–6 at r = 19, 23 not reproduced: the naive scan costs
  ≈ N log N, N = r^{2L−1}.) **Addendum:** r = 17 to depth 5 reproduced (D_P(9) = 604 as in M17; d5 max 2, hist {1: 81, 2: 1},
alive fraction 0.6772 = M17's 56561/83521); r = 19 depth 5 running (≈ 2 h) — result appended if it finishes.
* Note: the bound 3 is **attained** (r = 23, d = 4, one parent with 3 boxed children): Conjecture 4.2 is fitted to the data
  maximum with zero slack; "≤ 5 at depth 3" is likewise attained (r = 19, 23).
(D5, MAJOR — hidden hypothesis in a PROVED implication and in the headline "sharp threshold".) "Conjecture 4.2 for a prime r
implies that the r-generic line contains sterile points" needs **a non-residue cell surviving level 1** at that r (Conj 4.2
quantifies over surviving cells and is vacuous if there are none). Survival is CERTIFIED only for 17 ≤ r < 20000 (STERILE_LOWER
Comp. 4.1); for 2·10⁴ ≤ r < 2^{21.44} ≈ 2.84·10⁶ it is not established anywhere I could find (STERILE_LOWER Thm 6.3 covers
r ≥ 2^{21.44} only). So "Conjecture 4.2 on 17 ≤ r < 2^{21.44} would give sterile r-generic points for every prime r ≥ 17" is
CONDITIONAL also on level-1 survival in [2·10⁴, 2^{21.44}). Repair: add the hypothesis (or fold "some non-residue cell survives
level 1" into Conj 4.2 for r ≥ 2·10⁴), in §4, §6, the memo z17_uniform and SHARP 1 of the report. (Very likely true and cheap
to certify: level-1 boxes come from ES solutions of 4/r, a handful against (r − 1)/2 cells; a level-1 sweep to 2.84·10⁶ with a
√r-type enumerator would close it.)
(D6, MINOR — Assessment.) "≈ N^{2/5}/r^{L−1} = r^{0.6−0.2L} points per class on average (ET exponent), so true for L ≥ 4 on
average": the ET exponent is an *upper bound*; if it were the true average, a Poisson count over the ≈ r^{L−2} classes of a cell
would give ≈ r^{L−2}·λ⁴/24 = r^{0.2L+0.4}/24 classes with ≥ 4 boxes — growing in L, i.e. Conjecture 4.2 would be heuristically
*false* at large depth. The heuristic supporting 4.2 is the true growth of D_P, which at r = 17 is ≈ ×1.8 ≈ 17^{0.2} per level
(D_P(7..13) = 258, 604, 836, 1463), far below 17^{0.8}. Repair: replace the sentence by the observed growth, and say that with
the ET exponent as the true rate the conjecture would fail.

### Prop 1.3 check / spark S3′ (note for O244, not main scope)
`scripts/review_r249_inv.py` on O241's `data/z16/balls_d9.txt` (172 balls, depth ≤ 9, both slices) + my own Case B tuples
(s ≤ 16): my Case B enumeration reproduces **exactly** the 148 Case B balls of depth ≤ 9 in that list (none missing, none extra);
the other 24 are Case A, and these are precisely the 24 balls without an inverse ball (author's count confirmed). **But every one
of the 24 inverse cylinders already lies inside a ball of smaller depth** (depths 3–7). So through depth 9 the *covered set*
⋃𝔅 is invariant under u ↦ 1/u; the asymmetry is in the list of balls, not in coverage. For S3′ ("if a Case A⁻¹ type is missing,
coverage at q = 3 is underestimated"): the depth ≤ 9 data show **no** coverage underestimate from a hypothetical inverse family —
any such family would have produced only redundant balls so far. Many of the orphan Case A balls are themselves redundant
(e.g. 11200 ⊂ ball 112). The author's sentence "Case A data break the inversion symmetry" is correct for ball lists and should
add "(the covered set through depth 9 is nevertheless inversion-invariant: all 24 inverse cylinders are already covered)".
Suggested m4.

*Cross-reference (orchestrator FYI, O244 / FF_INVERSION_CHECK.md, under review R250 — not checked by me):* O244 explains the
asymmetry as the FF model omitting ET types I4 ("Case A⁻¹") and II2, both dominated on the sterility slices by Case B (a Case A
ball lies inside a same-E Case B ball when α + v ≥ k), with 0 unmirrored balls for A + B + I4 at depth 9 and unchanged survivors.
My independent finding above (all 24 inverse cylinders already covered at lower depth, covered set inversion-invariant through
depth 9) is consistent with that and gives a check of "survivors unchanged" through depth 9 that does not use O244's code. So the
author's S3′ worry ("coverage at q = 3 is underestimated") is answered negatively there; SIBLING should cite O244 and change
"Case A data break the inversion symmetry" to "the FF model omits I4/II2; the omitted balls are redundant (O244)".

## Numbered defects (consolidated)
* **D1 (MAJOR)** SIBLING §3 Prop 3.1 (statement "every route-type bound for N_V(p*), localised or not, is ≥ 3^{2s/5−O(1)}", proof
  sentence "their localised forms only change the multiplicity factor"), §6 PROVED list, report SHARP 2, memo z17_window:
  false for the localised route R2L (fix m′, then g′w₁ in its class mod T^{n−1}): ≤ 3^{s/5 + max(0, 2s/5 − n) + o(s)}. Repair:
  state the result for relative mass, exponent ≥ min(n − s/10, s/10) − o(s), for an explicit list (all SP Lemma 1.6 rows,
  modulus-localisations, R4L, R2L and the one/two-factor variants); downgrade "every route-type count / counts do not localise /
  must be fed by positional information" to Assessment.
* **D2 (MINOR)** §3: SS Cor 4.2's "unique maximiser (1/5,1/5,1/5,2/5)" is EVIDENCE (grid) there, cited as fact. Not needed; drop or
  label.
* **D3 (MINOR)** Cor 4.1(ii): add "and some depth-N₀ cylinder is alive" (or Π_N ≤ 2 for 9 ≤ N < N₀).
* **D4 (MINOR)** §2.1, §2.3, memo z17_poisson, report SHARP 3: replace with exact uniform-placement numbers (0.062 / P(none) 0.94 /
  E[≥2] 2.39; pair expectations C(b,2)·2/(M−1): 0.25, 0.46, 1.65, 0.64, 1.04, 0.30; all-parent triples 0.105 over d = 5–9);
  "neither repulsion nor attraction" → "no repulsion; mild excess of pairs (7 vs 4.3), concentrated at d = 6".
* **D5 (MAJOR)** §4 "Consequence (PROVED)", §6, memo z17_uniform, report SHARP 1: the implication needs a non-residue cell surviving
  level 1, certified only for r < 2·10⁴; add the hypothesis (or certify level 1 up to 2^{21.44}).
* **D6 (MINOR)** §4 "Why it is out of reach": the ET-exponent average r^{0.6−0.2L} would, if true, make Conj 4.2 heuristically false at
  large depth (≈ r^{0.2L+0.4}/24 classes with ≥ 4 boxes); the supporting heuristic is the true slow growth of D_P (≈ 17^{0.2} per level).
* **m1** Lemma 1.2 proof: "at most ⌈√(r/2)⌉ + 1 values (3 for r ≤ 17)" — the formula gives 4 at r = 17; correct count ⌈√(r/2)⌉.
  Header "PROVED, any prime r ≥ 5" vs "six" (r ≤ 17): state the general bound 2⌈√(r/2)⌉.
* **m3** §3 explicit form: with the quoted decay the tail condition gives s₁ ≈ 65 + 8n (depth ≈ 33 + 4n), not 80 + 9n; ±10 more with
  the parity filter. Assessment only.
* **m4** §1 check of Prop 1.3: add that the 24 orphan Case A balls have inverse cylinders already covered at lower depth, so the
  covered set through depth 9 is inversion-invariant (relevant to S3′ / O244).
* **m5** §2.4: "5 → 1 in C₃, C₁₃" (r = 19) skips the depth-4 value 2 (data file: 5, 2, 1, 1 at d = 3..6); say "5, 2, 1, 1".
* **m6** §2.4/Conj 4.2: say explicitly that the bound 3 (and 5 at depth 3) is attained (r = 23, d = 4), i.e. no slack in the data.
