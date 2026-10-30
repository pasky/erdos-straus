# z52b lane `translate` — reformulations of ES translated into their native fields

**ES is OPEN.** Nothing here proves or disproves it. This is a breadth-first list of candidate connections, not a
graded slate: the only filter applied was "obviously false / meaningless / literal duplicate". Items are not checked
against the campaign barrier map (B1–B9) on purpose.

## Summary

* **{N} items**, each with a connection, why it is not nonsense, a cheap first step, refs, free-form tags, confidence
  and effort. {NSEEN} items carry an automatic `seen:` tag (a keyword occurs in an existing memo). The rest use
  keywords not found in the repo's `.md` files, e.g. pretzel/Seifert Euler number, Greene, Honda, FQH K-matrix,
  Temperley, Cuntz–Holm–Jørgensen, Chan–Kontorovich–Pak, Azarija–Škrekovski, Button, Hodges.
* Coverage by form (tags): HJ length 3 / ES₅ dominates, followed by Type II divisor forms, the original Egyptian
  equation, SL₂ words, the cubic surface U_n, friezes, I3/U, forest, quaternion, theta, Markoff, lattice L_ρ,
  pencil, V_n, function field and power ladder. The histogram is below.
* **Self-review.** A deep reviewer (gpt-6-astra) checked all items for false statements, misattributions and
  duplicates. About 40 corrections were applied. Examples:
  - The generalised slot lemma for L ≥ 4 is false as first phrased (counterexample [2,2,2,5]).
  - (tu − 1, p) is ramified along tu = 1 on the word surface.
  - The power-ladder rung uses a rational third term.
  - The forest's own critical group is trivial; that item was replaced.
  - The Chen, Ghosh–Sarnak, Heath-Brown/Siegel-zero, Li–Zhang and Hodges attributions were corrected.
  - Conditional claims were made conditional in their titles.
* **Cheap tests** (`scripts/z52b_translate_cheap.py`):
  - The integer-altitude triangle strengthening (an ES solution with all denominators > p/2) **fails for every
    prime p ≡ 1 (4)**. There is a short proof, and it was checked numerically below 1500; the first script had an
    ordering bug that the reviewer caught.
  - The quartic-symbol test is degenerate as first posed (QNR forces A^{(p−1)/4} = ±i); the item now asks for a
    canonical i.
  - The plain mean of HJ length is dominated by A near p, so the QR/QNR comparison needs a different statistic.
  - The U(n) sporadics were factored: all are ≡ 1 (mod 8), and two lie in square classes mod 840 (441 = 21², 625 = 25²).

### Ten items I find most exciting (by id)

1. **0286 — exact Seifert/pretzel form.** ES(n) ⇔ a Seifert space M(0; (x,1),(y,1),(z,1)) has Euler number −4/n,
   i.e. the double cover of the pretzel link P(x,y,z) with det = 4xyz/n. This is an exact new home for the original
   equation, with slice-pretzel (Greene–Jabuka) and Seifert machinery.
2. **0266 — lens-surgery obstruction.** For p ≡ 1 (4), QNR lens spaces are never integral surgeries on knots in S³
   (linking-form obstruction). So ES₅ lives in the homotopy class that Greene's changemaker-lattice classification
   never reaches.
3. **0001 / 0268 — sandpile form of ES₅, with a random-graph model.** ES₅ says some 4-vertex fan multigraph with p
   spanning trees has a non-square sandpile pairing. Wood's Cohen–Lenstra theorem for sandpile groups, extended to
   pairings by Hodges (arXiv:2311.07078), gives a theorem-level random model.
4. **0182 — slot lemma as van der Blij / Gauss–Milgram for odd lattices.** This is a candidate structural reason for
   the 4-divisibility rule. It is also the place to find the correct sign rule for λ ≤ L, L ≥ 4, since the naive
   extension is false.
5. **0181 — FQH hierarchy K-matrix.** The ES₅ sign is the class of the abelian anyon theory on ℤ/p of a 3-level
   hierarchy state.
6. **0045 — Harpaz's dP5 log K3 (the A₂ cluster variety).** It carries the ES₅ frieze-with-coefficient. Harpaz proved
   non-density of integral points there, and that BM is not the only obstruction.
7. **0164 — Borwein–Choi xy+yz+zx.** A sibling of I3/U with ≤ 19 exceptions via class groups (one excluded under
   GRH): the (R)-rigidity template for 'finite sporadic list'.
8. **0289 — Markov uniqueness at prime powers (Button).** A pointwise-at-primes rigidity theorem for a Markoff-type
   equation using a p-tied integer; S_{n,D} is Markoff-type. Paired with 0291: is S_{n,D} a twisted character variety,
   which would give the missing mapping-class-group action?
9. **0321 — the quaternion algebra (tu − 1, p) on the word surface tuv − u − v = p.** Its Hilbert symbol at p is the
   ES₅ sign. It is Azumaya only on the open set tu ≠ 1 (ramified along tu = 1), so the slot lemma would be a
   ramified/open-subset Brauer–Manin reciprocity. Finding an unramified replacement is part of the item.
10. **0243 — Maynard–Tao for many simultaneously prime 4Cp+1.** Open whether it applies with p prime. If it does, it
    is a provable quantitative B1: infinitely many primes fail at least m of the first K levels. Paired with 0293
    (small levels as norm-form conditions; Iwaniec, applicability to be checked).

Also notable: 0002/0269 (vertex-count and K₄ relaxation ladders), 0216 (Rav/Kneser divisor sumsets), 0215
(pseudosquares; 2521 = 2520 + 1 is the last I3_𝒞 zero), 0207/0208 (Zolotarev / 2-adic order form of the sign),
0267 (Honda tight-structure weights).

## What I did NOT get to

* Per-item nearest-theorem statements are from memory for non-arXiv classics. Many are flagged `(check)`, and none
  were re-read in full.
* No item was graded against the barrier map (by design). Several are marked `calibration` because they mostly
  explain a known barrier in another field's language.
* The cheap tests listed in `first_step` were mostly not run (only the ones above).
* Fields that were thin or skipped: harmonic analysis on adeles beyond local densities, PDE/analysis, tropical curve
  counting, motivic integration beyond Igusa, homotopy theory, higher category theory, and economics beyond fair
  division (judged mostly empty).
* `seen:` tags are keyword-based and may miss prior work phrased differently, or flag unrelated mentions.

## Method

1. Listed the repo's equivalent / sufficient / near-equivalent forms of ES and invented further translations. Sources:
   FRONTIER §§1–2, DEDEKIND_ES, FOREST_*, QUESTION_R, METAPLECTIC_ES, GEOMETRY_ES, FRIEZE_ES, WINDMILL, MARKOFF_ES,
   COMPOSITION_ES, LATTICE_MEETING, BALANCED_LATTICE, THREE_SQUARES, KUDLA_ES, QUATERNION_ES, LORENZINI_W,
   ZAREMBA_TRANSFER, POWER_LADDER_ES, the Z52 pencil and I3/U(n). New translations written down here include:
   - a 4-vertex fan multigraph with p spanning trees and a sandpile-pairing condition, and effective resistance A/p;
   - lens spaces, linear plumbings and 2-bridge links with their homotopy type;
   - Seifert spaces with Euler number −4/n and pretzel links;
   - tridiagonal ternary lattices with a non-square discriminant form;
   - triangle orbifolds of area 2π(1 − 4/n), and triangles with integer exradii and inradius n/4;
   - the Frobenius-class form uv | n + u + v (numerical semigroups, Popoviciu);
   - totally split cubics T²(T − s) + e(T − n/4);
   - frieze patterns with coefficients and the dP5 log K3 (Harpaz);
   - −Γ₁(c) matrices with fixed upper-right entry p;
   - TFNP search classes and Legendre-PRF-style heuristics.
2. For each form × field where it is native, recorded the nearest PROVED theorem (or the nearest known object), what
   the field's toolbox would try first, and the cheapest test.
3. `seen:<file>` tags were added automatically by a fixed-string `git grep -il` on 1–3 specific keywords per item
   (first hit, non-review files preferred). They mean "the keyword occurs there", not "this exact item was done there".
4. Literature: arXiv ids in `refs` were checked against the arXiv API (`scripts/z52b_translate_arxiv.py`). Non-arXiv
   classics are cited by author/title/year from memory, and are named as facts only where they are standard.
   Anything less certain is phrased as "check whether …".

Item count: {N}. Items carrying a `seen:` tag: {NSEEN}.
Data: `data/z52b/translate.jsonl`. Builder: `scripts/z52b_translate_build.py` (items are in `scripts/z52b_translate_items_*.py`).
