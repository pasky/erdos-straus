# AGENT REPORT O132 — red team 2 + synthesis (automorphic/geometric wave (I))

Deliverable: `reviews/redteam-automorphic-2.md`. Scripts: `scripts/rt2_slices.py`, `scripts/rt2_blocks.py`,
`scripts/rt2_pdivides_e.py`. Logs: `logs/rt2_slices_200.txt`, `logs/rt2_blocks.txt`.

Merged into this branch:
* `side-agent/redteam-automorphic` (red team 1 §7–§8 were not on main);
* `side-agent/quaternion-es`;
* `side-agent/review-quaternion` (R130 repairs).

`side-agent/review-geometry` (R126) was still in progress, so it was read but not merged.

## 1. T1–T8 on O123, O128, O131, O130 (§1)
All four negative conclusions **survive**. No FATAL or MAJOR defects. Findings:
* **O123 T3 (new):** §5's illustrative sufficient statement `Σ_{d≤L²} …` implies `n_p ≤ (log p)²` for
  `p ≡ 1 (4)`. The reason: Type I at level d needs `(d/p) = −1`. That bound is open even under GRH (Bach: `< 2log²p`).
  Same issue as SHT (red team 1 P7.2). Repair: anchor the levels at `n_p`.
* **O128 T2 (new small lemma, Dickson-conditional):** every single `(c,d)` shell is empty for infinitely many p.
  This is the twin of O123 P5.3.
* **O130:** Prop 1.3 silently used `p ∤ e`. One-line fix: `p | e` forces `(−d/p) = +1`. Found independently;
  R130 had found and repaired it too.
* **O131:** clean. Thm 5.2 is the model PROVED invisibility statement.
* **Headline audit (§1.6):**
  * "Barrier" and "no standard hypothesis suffices" are Assessments. The latter is meaningful only
    mechanism-scoped: if ES is true, every hypothesis implies it. The ledger phrasing is fine; keep "known" and
    "by these routes" everywhere.
  * "Planck scale" has a geometric sense (PROVED for the encodings) and an arithmetic one (a single integer's
    divisors), and the arithmetic one is more basic.
  * Untested, not dismissed: Brandt/weight 3/2, any rank > 2 object, and joint growing-family inputs.

## 2. Synthesis (§2) — PROVED, elementary
* **Lemma 2.1 (slice table).** Fix any two of ET's coordinates `(a,b,c,d,e)`, Type I or II. The fibre is then
  either a finite union of congruence classes of p, or the set of divisors of one integer `N_θ(p)` in a residue
  class mod `q_θ`. There are 14 rows with explicit N: `p²+4c²d`, `ap+c`, `(pe+1)/4a`, `(pe+1)/4d`, `4c²dp+1`,
  `cp+a`, `p+4a²d`, … The table was machine-verified for all primes `5 ≤ p < 200` against brute force.
* **Theorem 2.2.**
  * (i) The six encodings (SL₂/Heegner Type I, shells, GZ x = 2 collision, `(−d,−p)` factorisation, CM torus,
    `Q_d`) are slices.
  * (ii) Their representative-independent invariants are congruence or genus data. This collects O131 Thm 5.2,
    O130 P2.2, GEOMETRY P4.1 and O128 §8.
  * (iii) Any argument certifying ES(p) through a *fixed finite* set of slices fails for infinitely many
    `p ≡ 1 (24)` under H (POINTWISE_SIZE Thm C), **whatever auxiliary automorphic/spectral/geometric input it
    uses**, because its witness must lie in one of those fibres.
* The only remaining freedom is a growing parameter set (E1). By Lemma 2.1, that means the joint divisor events of
  a growing family of integers at one p.

## 3. Escape hatches (§3) — the forward-looking list
H-A to H-G, with citations verified by a research subagent (publisher/arXiv pages):
* **H-A:** joint factorisation over a growing family with a *moving* modulus. Open, no technology.
* **H-B:** parity-breaking (Friedlander–Iwaniec / Heath-Brown / Maynard-type) divisor-in-moving-class counts at
  fixed p. Open; the closest technology in spirit.
* **H-C:** E2 anchoring at `n_p`. A reparametrisation only.
* **H-D:** non-abelian / higher-rank data. No candidate object; the dihedral data have coefficient 0 by O131
  Thm 5.2.
* **H-E:** signed counting certificates. Termwise standard hypotheses lose `p^ε`; an exact positive identity is
  open (O131 negative within its dictionary).
* **H-F:** integral Hasse principle beyond BM. Cautionary: Markoff-type surfaces satisfy integral Hasse for almost
  all parameters, but it fails infinitely often (Ghosh–Sarnak).
* **H-G:** Type I ∪ II, and descent. Not an escape.

EVIDENCE (§3.1): Type II solutions of primes near 10⁶ and 4·10⁶ sit about one per dyadic `(a,c,d)` block, max 3. No
sub-family has a growing count, so any fixed-p route must aggregate ≍ 𝓛³ blocks of expected size O(1).

## Labels
* PROVED: Lemma 2.1; Thm 2.2(i),(ii) (relative to the cited PROVED statements); Thm 2.2(iii) relative to Thm C
  (CONDITIONAL on H).
* CONDITIONAL on Dickson: Lemma 1.2.1.
* EVIDENCE: §3.1, the slice checks.
* Assessment: every "barrier" and "no technology" verdict.

Nothing here proves or disproves ES.

## Suggested ledger entry
§4 item 1 of the deliverable.
