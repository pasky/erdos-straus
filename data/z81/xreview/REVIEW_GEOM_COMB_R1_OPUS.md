<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of lane z81-geom-comb (notes/z81/GEOM_COMB.md). The author is a GPT-6.2 Astra lane. Verify every theorem, geometry-of-numbers/Coppersmith/Davenport/sum-product/descent calculation, falsifier screen (F1–F4), and scope claim. Reject disguised B2 re-encoding or trivial volume counts. Cap any computational replay to ≤ 15 minutes.

Commit log:
commit 014fe3c23603c361749ca1ef245a62ae9adbaacc
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:07:57 2026 +0100

    Separate generated subgroups from simultaneous positive ES windows at prime inputs

 data/z81/geom_comb/screen.txt  |  56 ++++
 data/z81/geom_comb/smooth.json | 653 +++++++++++++++++++++++++++++++++++++++++
 data/z81/geom_comb/smooth.txt  |   4 +
 notes/z81/GEOM_COMB.md         |  80 +++++
 scripts/z81_gc_screen.py       | 139 +++++++++
 scripts/z81_gc_smooth.py       | 100 +++++++
 6 files changed, 1032 insertions(+)

Review:
**Verdict: accept with fixes, as BARRIER-SCOPED / METHOD-CX, with no STATUS delta.** I found no mathematical error in Theorem A, Proposition B, Lemma C, the D-envelope or the Coppersmith algebra. The results are honestly scoped and none is a claimed proof of ES. Their value is small, and two sections repeat material the repository already has.

## What I checked
- **Replay:** both scripts reproduce `screen.txt` and `smooth.txt` byte for byte, in about 2 s in total.
- **Primality certificates:** I audited `ec_check` and `check_lucas` and they are sound:
  - every inverse must exist mod n (Python's `pow(...,-1,n)` raises an error otherwise), so sP is a genuine affine point mod every prime ℓ dividing n;
  - qP=O together with the Hasse bound gives the required bound q>(n^{1/4}+1)², and the code rounds up safely;
  - the Lucas tail uses a complete factorisation of n−1, with each factor proved prime recursively.

  The 146- and 149-digit controls can therefore be relabelled **CERTIFIED** rather than "EVIDENCE pending replay".
- **Lemma C:** I re-derived the proof: the half-integer pairing gives RS ≥ ½, Poisson gives U=(1−V)/(1+V), and the fixed point is √2−1. A brute-force test on 300 random small cyclic groups found no violation; the largest RS was 0.64 of the stated constant.
- **Theorem A, step by step:**
  - **Field theory:** i ∉ K, the parity argument for [K:F], and Chebotarev on K(i) are all correct. A search with h=5 found r=128831 and others, each with −1 in class h, as claimed.
  - **Index set:** the induction giving (i−j) | j is correct.
  - **Admissibility:** 2Tⁱ≡1 (l) forces 2^d≡1 (l), hence T≡1 (l), a contradiction. The r-part is fine.
  - **Residues:** T^j≡1 mod k_d. q_j generates −1 mod k through an odd exponent (unique involution mod r^e, and −1 at the other prime powers). The Jacobi step and (q_j/p)=(q_j/k) are correct.
  - **Box failure:** the class of q_j^u p^v mod r in C_{2h} forces |u+v|≥h.
  - **Solubility:** the (★) identity holds: 4/p = 1/(3B′)+1/(3p)+1/(3B′p) with p=11B′−1.
  - **Maynard:** really needed, even at J=1, since q_j and p must both be prime. That correctly explains why the shifts cannot be prescribed.
- **Proposition B:** the discrete logs are right (11 is a primitive root mod 31, 2=11¹⁸, target 15). The residue sets have sizes 9, 21 and 13, and 3−18≡15 (mod 30).
- **Infinitude variant under Schinzel H:** the Eisenstein argument at 31, the admissibility (x↦x^e is a bijection on F_l^* for l≤e+1) and p≡1 (840) all check out.

## Substance: limits of the results
1. **Theorem A is modestly new.** The FRONTIER Anatomy entry (line 1135, from `ES_JUGULAR` §11) already records that the generated group can contain −1 while the exponent box misses. What A adds:
   - this happens unconditionally, at actual primes;
   - in J windows at once;
   - with an arbitrarily large exponent gap.

   Its limits:
   - the shifts k_d=T^d−1 are astronomically large;
   - the primes are deliberately soluble;
   - the obstruction is a single order-2h character mod r, which is just the small-S case of Lemma C. It fits z80 Theorem H's non-genus, index ≥3 case rather than escaping it.

   So the note's line "a plentiful subgroup… cannot explain these failures" is true only for index-2 (quadratic) subgroups. It should say so.
2. **Lemma C is not new.** It is Banaszczyk's transference adapted to an index-2 coset pair, so it must cite Banaszczyk (1993) and not imply novelty. As a sufficient criterion it needs S ≥ C(d), and C(d) grows linearly in d=ω(px). Nothing suggests this can be checked at actual primes more cheaply than searching the box itself.
3. **Proposition B and the smooth controls are trivial.** Primes ≡1 mod 31 are neutral, so the "ω ≥ D(G) forcing" hypothesis being refuted is a straw man. FRONTIER line 1628 already lists "Davenport forcing" as refuted, and z81 LIT's table marks Davenport as blind. The certificates are sound but far more machinery than needed: any prime of this shape works.
4. **The D-envelope is correct but trivial.** The qualifier "polylog-smooth" is superfluous, because the bound applies to every k.
5. **§5 Coppersmith repeats `Z53_LATTICE.md` §5** (uB<16C², "no existence content"). It should be a pointer, not a re-derivation. The greedy-rule kill is DATA.

## Form
- **The branch is behind main.** The note cites z81 LIT, Gao et al. and Jain, which exist only after main's merge `9313b724d`. Rebase before export. `git diff main..` shows spurious deletions of `z81/lit`; review with `main...HEAD`.
- **The prose is very dense and relies on undefined local jargon:** 11-shot, C-even, R₈, U₇, B2, (★), 𝔐, "Mordell primes". Garbled sentences include:
  - "Exact single-target transference is up to dimension factors";
  - "A's pricing is freedom to choose the offsets";
  - "Greedy positive remainder decreases its numerator after the first step only at k=3…";
  - "When k<p these denominators exceed x".
- **Minor proof wording:** the trivial intersection Q(ζ_h)∩M=Q should be argued by ramification, not by "exponent ≤2". The condition h≡1 mod 4 is unnecessary, though harmless.
- **The cited Jain theorem has no in-note reference.** It is identifiable from main's LIT note as arXiv 2611.21136.
- **There is no proposed one-line FRONTIER §6 entry.** Suggest merging into the line-1135 Anatomy entry: "(z81 `GEOM_COMB` A, PROVED rel. Maynard) realised unconditionally at J simultaneous unprescribed windows with exponent gap >B, on soluble primes."
- **Labels:** the controls should read CERTIFIED, and the Review line should point to this cross-review.

**Required before export:**
1. Rebase onto main.
2. Cite Banaszczyk and drop the implied novelty of Lemma C.
3. Replace §5 Coppersmith with a pointer to Z53 §5.
4. Scope the "cannot explain" sentence to quadratic (index-2) obstructions.
5. Upgrade the controls to CERTIFIED.
6. Rewrite the garbled sentences.
7. Add the FRONTIER merge line.
</code-review>