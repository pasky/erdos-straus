# z52b lane `translate` — reformulations of ES translated into their native fields

**ES is OPEN.** Nothing here proves or disproves it. This is a breadth-first list of candidate connections, not a
graded slate: the only filter applied was "obviously false / meaningless / literal duplicate". Items are not checked
against the campaign barrier map (B1–B9) on purpose.

## Summary

* **{N} items**, each with a connection, why it is not nonsense, a cheap first step, refs, free-form tags, confidence
  and effort. {NSEEN} items carry an automatic `seen:` tag (a keyword occurs in an existing memo). The rest use
  keywords not found in the repo's `.md` files, e.g. pretzel/Seifert Euler number, Greene, Honda, FQH K-matrix,
  Temperley, Cuntz–Holm–Jørgensen, Chan–Kontorovich–Pak, Azarija–Škrekovski, Button.
* Coverage by form (tags): HJ length 3 / ES₅ dominates, followed by Type II divisor forms, the original Egyptian
  equation, SL₂ words, the cubic surface U_n, friezes, I3/U, forest, quaternion, theta, Markoff, lattice L_ρ,
  pencil, V_n, function field and power ladder. The histogram is below.
* Three cheap tests were run (`scripts/z52b_translate_cheap.py`):
  - The 'integer-altitude triangle' strengthening (ES solution with p/2 < x ≤ 3p/4) **fails** for 127 primes
    p ≡ 1 (4) below 3·10⁴, so it is false as a universal statement.
  - The quartic-symbol test is degenerate as first posed (QNR forces A^{(p−1)/4} = ±i); the item now asks for a
    canonical i.
  - The plain mean of HJ length is dominated by A near p, so the QR/QNR comparison needs a different statistic.

  The U(n) sporadics were factored: all are ≡ 1 (mod 8), and two lie in square classes mod 840 (441 = 21², 625 = 25²).

### Ten items I find most exciting (by id)

1. **0286 — exact Seifert/pretzel form.** ES(n) ⇔ a Seifert space M(0; (x,1),(y,1),(z,1)) has Euler number −4/n,
   the double cover of the pretzel link P(x,y,z) with det = 4xyz/n. This is an exact new home for the original
   equation, with slice-pretzel (Greene–Jabuka) and Seifert machinery.
2. **0266 — lens-surgery obstruction.** For p ≡ 1 (4), QNR lens spaces are exactly those not obtainable by integral
   surgery on a knot (homotopy class), so ES₅ lives on the complement of Greene's changemaker-lattice classification.
3. **0001 / 0268 — sandpile form of ES₅, with a random-graph model.** ES₅ says some 4-vertex fan multigraph with p
   spanning trees has a non-square sandpile pairing. Wood's Cohen–Lenstra theorem for sandpile groups gives a
   theorem-level random model.
4. **0182 — slot lemma as van der Blij / Gauss–Milgram for odd lattices.** This is a structural reason for the
   4-divisibility rule and a route to the λ ≤ L ladder.
5. **0181 — FQH hierarchy K-matrix.** The ES₅ sign is the class of the abelian anyon theory on ℤ/p of a 3-level
   hierarchy state.
6. **0045 — Harpaz's dP5 log K3 (the A₂ cluster variety).** It carries the ES₅ frieze-with-coefficient. Proved
   non-density of integral points, and BM is not the only obstruction there.
7. **0164 — Borwein–Choi xy+yz+zx.** A sibling of I3/U with ≤ 19 exceptions via class groups (one excluded under
   GRH): the (R)-rigidity template for 'finite sporadic list'.
8. **0289 — Markov uniqueness at prime powers (Button).** A pointwise-at-primes rigidity theorem for a Markoff-type
   equation using a p-tied integer; S_{n,D} is Markoff-type. Paired with 0291 (is S_{n,D} a twisted character
   variety, which would give the missing mapping-class-group action?).
9. **0321 — Brauer class (tu − 1, p) on the word surface tuv − u − v = p.** Its evaluation at p is the ES₅ sign, so
   the slot lemma would be Brauer–Manin reciprocity, and ES₅ becomes 'an integral point with non-trivial evaluation'.
10. **0243 — Maynard–Tao forcing many simultaneously prime 4Cp+1.** If it applies with p prime, it is a provable
    quantitative B1: infinitely many primes fail any m chosen small levels. Paired with 0293 (small levels =
    norm-form conditions, Iwaniec).

Also notable: 0002/0269 (vertex-count and K₄ relaxation ladders), 0216 (Rav/Kneser divisor sumsets), 0215
(pseudosquares; 2521 = 2520 + 1 is the last I3_𝒞 zero), 0207/0208 (Zolotarev / 2-adic order form of the sign),
0267 (Honda tight-structure weights).

## What I did NOT get to

* Per-item nearest-theorem statements are from memory for non-arXiv classics. Many are flagged `(check)`, and none
  were re-read in full.
* No item was graded against the barrier map (by design). Several are marked `calibration` because they mostly
  explain a known barrier in another field's language.
* The cheap tests listed in `first_step` were mostly not run (only the three above).
* Fields that were thin or skipped: harmonic analysis on adeles beyond local densities, PDE/analysis, tropical
  curve counting, motivic integration beyond Igusa, homotopy theory, higher category theory, and economics beyond
  fair division (judged mostly empty).
* `seen:` tags are keyword-based and may miss prior work phrased differently, or flag unrelated mentions.

## Method

1. Listed the repo's equivalent / sufficient / near-equivalent forms of ES (FRONTIER §§1–2, DEDEKIND_ES, FOREST_*,
   QUESTION_R, METAPLECTIC_ES, GEOMETRY_ES, FRIEZE_ES, WINDMILL, MARKOFF_ES, COMPOSITION_ES, LATTICE_MEETING,
   BALANCED_LATTICE, THREE_SQUARES, KUDLA_ES, QUATERNION_ES, LORENZINI_W, ZAREMBA_TRANSFER, POWER_LADDER_ES, Z52 pencil,
   I3/U(n)) and invented further translations. New ones written down here include: a 4-vertex fan multigraph with p
   spanning trees and a sandpile-pairing condition; effective resistance A/p; lens spaces / linear plumbings / 2-bridge
   links and their homotopy type; tridiagonal ternary lattices with a non-square discriminant form; triangle orbifolds
   of area 2π(1 − 4/n); triangles with integer exradii and inradius n/4; the Frobenius-class form uv | n + u + v (numerical
   semigroups, Popoviciu); totally split cubics T²(T − s) + e(T − n/4); frieze patterns with coefficients; dP5 log K3
   (Harpaz); −Γ₁(c) matrices with fixed upper-right entry p; TFNP search classes; Legendre-PRF distinguishers.
2. For each form × field where it is native, recorded the nearest PROVED theorem (or the nearest known object), what the
   field's toolbox would try first, and the cheapest test.
3. `seen:<file>` tags were added automatically by a fixed-string `git grep -il` on 1–3 specific keywords per item
   (first hit, non-review files preferred). They mean "the keyword occurs there", not "this exact item was done there".
4. Literature: arXiv ids in `refs` were checked against the arXiv API (`scripts/z52b_translate_arxiv.py`). Non-arXiv
   classics are cited by author/title/year from memory, and are named as facts only where they are standard.
   Anything less certain is phrased in `first_step` as "check whether …".

Item count: {N}. Items carrying a `seen:` tag: {NSEEN}.
Data: `data/z52b/translate.jsonl`. Builder: `scripts/z52b_translate_build.py` (items are in `scripts/z52b_translate_items_*.py`).
