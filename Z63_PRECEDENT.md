# Z63_PRECEDENT — is there ANY theorem proving pointwise existence at polylog expected count without an identity? (wave z63, lane PRECEDENT)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results are internally reviewed only. Brief: `z52bbriefs/z63_lanes.md` §PRECEDENT.
Notes and source excerpts: `data/z63/precedent/`.

*Status: CHECKPOINT 1 (skeleton). Sections marked TODO are filled in later.*

## 0. Precise question (Assessment-level meta-question; every row of §2 carries its own label)

Call a theorem **T a precedent** if all of the following hold.
* (P1) *Pointwise.* T asserts, for **every** sufficiently large input n in an infinite natural class 𝒩 (every n, every
  prime p, every prime in a residue class), that a witness set W(n) ≠ ∅. "Almost all n", averages over n, "infinitely
  many n", and statements about a *chosen* (designed or random) object are not pointwise for a prescribed input.
* (P2) *Thin.* The natural expected size of W(n) (heuristic, or proved on average over n) is (log n)^{O(1)}, or O(1).
  If W(n) lies in a window, the count *inside the window that T actually guarantees* is what matters, not the count in
  a smaller conjectural window.
* (P3) *No identity.* The proof does not produce the witness from an algebraic identity or parametrisation (a
  polynomial or digit formula w = F(n) on a finite partition of 𝒩).
* (P4) *Unconditional.* (Conditional theorems are listed for calibration, not as precedents.)

**Target event (B2).** At a prime p ≡ 1 (24): some C ≥ 1 and some divisor d | 4Cp + 1 with d ≡ −1 (mod 4C). The
expected number of such (C, d) is ≍ log²p (FRONTIER §2.2). Every witness d has a prime factor ℓ with (ℓ/p) = −1
(FRONTIER §3 B5). The full search box is O(p²) (B-fin).

Questions: (Q1) does a precedent exist? (Q2) For each candidate in the brief: expected count, pointwise or not,
mechanism, transfer to B2. (Q3) If a precedent exists: its mechanism, a transfer attempt, falsifier table. If none: a
precise statement of the gap — what the first theorem of its kind would have to assert.

## 1. Why this is not already closed (prior work, and what is new here)

This meta-question has been asked four times: `DETERMINISTIC_EXISTENCE.md` (O168), `B2_ACROSS_FIELDS.md` ((J)94: the
M1a/M1b/M2–M5 pattern, FRONTIER §3), `BRAINSTORM/s9_lower_tail_literature.md` ((J)103), `BRAINSTORM/z52_deep_thin_pointwise_opus.md`
(40-row catalogue, (T)/(R) taxonomy), plus `Z53_LIT.md` §6.4 (proposed (J)103 wording) and `Z58_LIT.md` §2.5. Their verdict
— "no every-n theorem for a natural problem with a polylog main term; thin-regime theorems are (T) thick object +
extraction, or (R) rigidity" — is an Assessment with several rows **NOT ACCESSED** in the primary source (z52 §4: Burgess
1957, Bach 1990, Heath-Brown 1986, Sylvester–Schur, Erdős–Selfridge, Dirichlet/Minkowski, …). This lane adds:
1. the brief's specific candidates, each verified at theorem-number level (many were never checked: Erdős 1956 /
   Erdős–Tetali / Wirsing / Choi–Erdős–Nathanson / Sidon bases, AKS's r-lemma, Alon–Füredi, entropy, o-minimality,
   divisors in (y, 2y], square-free values, Friedlander–Iwaniec, Duke);
2. a **literal-reading check**: the brief's (P1)–(P4) are *weaker* than (J)103's "natural problem" phrasing. Section 3
   tests whether any theorem passes them literally (the size/valuation squeeze class is the prime suspect), and if so,
   why its mechanism does or does not transfer;
3. a sharper gap statement, with calibration against the nearest *positive-polarity* problems (least prime ≡ 1 (mod q)
   in a window with polylog expected count — open even under GRH?), to be verified.

## 2. Ranked table (TODO — after source verification)

## 3. The literal precedents and their transfer (TODO)

**First falsifier (pre-registered, checkpoint 1).** Candidate literal precedent: *Chebyshev-type squeeze* — "every n ≥ 3
has a prime ℓ ≤ (1 + o(1)) log n with ℓ ∤ n" (expected number of such ℓ ≍ log n / log log n, unconditional, pointwise,
no identity). If (P1)–(P4) admit it, the answer to Q1 is literally (a). Kill test for its *transfer*: a size squeeze can
only certify a witness whose **failure** event is a divisibility event "w | F(n)" for an integer F(n) ≠ 0 of controlled
size. B2's failure event is a conjunction of *non*-divisibilities. So the transfer must route through a congruence
consequence of failure (R(p) = 0 ⟹ p lies in a sterile class modulo every small modulus); and since the profinite sterile
set contains the squares (B1/B5), the squeeze can reach at most the quadratic-character layer. Status: to be written as
a scoped statement in §3 with citations to B1/B5 and LOPEZT Prop 3.1.

## 4. Falsifier table (TODO)

## 5. Verdict, screens, proposed FRONTIER text, bottom line (TODO)

## 6. Review log (TODO)
