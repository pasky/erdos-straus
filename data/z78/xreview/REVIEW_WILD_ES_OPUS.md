<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Independent cross-lab Claude Opus hostile review of notes/z78/WILD_ES.md §§1–5, all commits main..HEAD. State actual model identity, provider/auth/quota errors explicitly. Attack every PROVED, CERTIFIED and data label: ratio step, M-th powers/line arrangement and transfer, Fermat cover units/Newton-rigidity and full Type II extension, H4 graded minorant/preload/Gallagher/endpoint sign/first height. Rerun key computations including replay under ulimit -v 1000000, timeout ≤400, UV offline and no pycache. Check for disguised B2 and novelty limits. Inspect last round hostile checks. Do not edit files (I will archive full output). Include your full critique, findings and verdict in final output.

Commit log:
commit 544c2b813164de37130a48fd9bfd056ac3d06b48
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:01:30 2026 +0100

    z78 wild: exact height panel at 192 deep primorial primes and hostile scope audit

 data/z78/wild_depth.csv         | 193 ++++++++++++++++++++++++++++++++++++++++
 data/z78/wild_depth_summary.txt |   6 ++
 notes/z78/WILD_ES.md            |  14 ++-
 scripts/z78_wild_depth.py       |  55 ++++++++++++
 4 files changed, 265 insertions(+), 3 deletions(-)

commit 95116e575654175d067617711c5f13ab18624e26
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 20:00:32 2026 +0100

    z78 wild: prescribe the exact first star modulus at a logarithmic-depth pseudosquare prime

 notes/z78/WILD_ES.md | 16 ++++++++++++++++
 1 file changed, 16 insertions(+)

commit 52344001ff6a04810347ece7513623c76bd397b3
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:56:41 2026 +0100

    z78 wild: forbid upward prime transport on the full Type II threefold

 notes/z78/WILD_ES.md | 6 ++++++
 1 file changed, 6 insertions(+)

commit ac05df0bfa0f044d451a9cb0a120bb810127810f
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:55:03 2026 +0100

    z78 wild: classify finite-etale input correspondences and forbid endpoint ascent to a prime

 notes/z78/WILD_ES.md | 19 +++++++++++++++++++
 1 file changed, 19 insertions(+)

commit de88dc0690aa85f195b306b48846acb1e8812004
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:52:06 2026 +0100

    z78 wild: bounded Brauer blindness for two pencils with a squareclass compatibility test

 notes/z78/WILD_ES.md | 17 +++++++++++++++++
 1 file changed, 17 insertions(+)

commit f118fcfcaa6c7a26505714e9038eebe7643f8f33
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:50:07 2026 +0100

    z78 wild: one non-coordinate unit rejects every old q-power patch

 notes/z78/WILD_ES.md | 6 ++++++
 1 file changed, 6 insertions(+)

commit 450d0e304f080ca21703baecb376b46c66e526a0
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:44:47 2026 +0100

    z78 wild: prove density one in every fixed exponent progression

 notes/z78/WILD_ES.md | 8 +++++---
 1 file changed, 5 insertions(+), 3 deletions(-)

commit 778c837a4b15ed6414464d232dc407f82260aa73
Author: Petr Baudis <pasky@ucw.cz>
Date:   Fri Nov 20 19:40:13 2026 +0100

    z78 wild: force the negative residue for infinitely many fixed-offset Proth cores

 notes/z78/WILD_ES.md | 26 ++++++++++++++++++++++++++
 1 file changed, 26 insertions(+)

Review:
# Hostile review of `notes/z78/WILD_ES.md` §§1–5 (commits `main..544c2b8`, 8 commits)

**Reviewer:** I'm Claude (Anthropic), running as a Claude Code subagent and dispatched as the Opus cross-lab reviewer. I can't see the exact model build string from inside the session. I hit no provider, auth or quota errors. I edited no files; my scratch scripts are in `/tmp/rev78/`.

**Verdict:** the mathematics holds. I found no fatal error and no disguised B2 claim. §1 is a correct thin-family theorem whose core overlaps z78 Lane 4. §§2–4 hold within their stated scopes, with several fixes to scope, form and triage listed below.

## Replays and independent checks
All ran under `ulimit -v 1000000`, `timeout ≤400`, `uv --offline --no-project` and `PYTHONDONTWRITEBYTECODE=1`, except one symbolic sympy check run at 2 GB. `git status` afterwards was clean apart from the existing untracked `.pi/`.

| Check | Result |
|---|---|
| `scripts/z78_wild_depth.py` replay (27 s) | Passed its CSV-equality assertion; stdout identical (`diff`) to `wild_depth_summary.txt` |
| Own Pocklington check on all 192 rows, with bases above B | All prime. Small bases cannot work, because every a ≤ B is a square mod p |
| Own Miller–Rabin compositeness witness for every skipped t | "First 32 primes above 10²⁰" confirmed |
| Own divisor-of-(g+1)/4 recomputation of the minimum modulus on all 192 rows | All match. The script only does this on 6 rows |
| −1 ∈ H by direct subgroup computation, h ≤ 25 | True at h = 5, 11, 13, 17, 19, 25. Also true at h = 7 and 23, where −1 ∉ ⟨2 mod h⟩. False at h = 9, 15, 21 (3 \| h) |
| Explicit Theorem A instances at h = 5 | 4/n identity checked in exact rationals; Jacobi((tu−1)/n) = −1; t, v ≡ 7 mod 8. Works at s = 17612, and also at **odd** s = 323323 and 911183 (odd r = 11, 31), confirming that Corollary A.1 does not need 4 \| s |
| 5^a examples | 2^{2·5^{a−1}} ≡ −1 mod 5^a holds for a = 1, 2, 3 |
| Sympy identities | Concurrent-line identity `u+n+bB = B(kCu−1+b)`, P lies on S, both ratios equal v², and C.1's `d′ = w²d/(np c′²)` |

## §1: Theorem A and Corollary A.1 (label PROVED). Accept.
- **Argument checked line by line:**
  - Every B_i is a unit.
  - B₃ = B₁² collapses the common coset; B₁/B₋₁ = 2.
  - The doubling product telescopes to −1/2.
  - Each ratio residue is B_{rj}/B_r, and these generate H.
  - Multiplicities up to N suffice.
  - Divisibility uses distinct cyclotomic factors of x^D+1, so no coprimality is needed.
  - The CRT congruence A ≡ 7u−1 mod 8u holds, as does v ≡ −1 mod 16.
  - The ES identity is self-contained and elementary.
  - The no-finite-cover argument (square unit at the odd part, 1 at the 2-part) is correct.
- **Challenge, scope:** the hypothesis −1 ∈ ⟨2 mod h⟩ is only sufficient. h = 7 and h = 23 also give −1 ∈ H. Lane 4 (`side-agent/z78-proth-allm`, `PROTH_ALLM.md` Theorem 1, and its Theorem 4, an exact criterion with no hypothesis on the doubling orbit) has the same core theorem and cross-cites this note. The only new content here is the density-one Corollary A.1. At export:
  - make it **one** §1C row;
  - give the core theorem joint credit;
  - credit the density refinement to this note;
  - use Lane 4's broader hypothesis.
- **Corollary A.1:** correct. Divergence of Σ1/ℓ in a progression is Dirichlet's theorem in analytic form, so the "Mertens" label is more than needed. "Density one" is over exponents s, so the n-values are still about log X many up to X. The scope says so.
- **Form:**
  - "(S)" and "interior" are never defined.
  - "Exceed 1,590,284,203,561" is an unexplained R₈-floor reference; cite it or drop it.
- **B2:** the divisor of n+u in the class −1 mod N is B2-shaped. It is solved only through the known cyclotomic factorisation of n+u, which is the standard thin-family bypass. The note claims nothing for primes. No disguised B2.

## §2: Lemma B0, Theorem B and the transfer. Accept, with a scope fix.
- **B0 checks out:**
  - z = kCu−1 equals q at P.
  - At the patched point u′ ≡ −n and z′ ≡ −n−1 is a unit mod q.
  - On the C-fibre, z·((q+1)B−1) = 1+(q+1)n, so the valuation drops by exactly one.
  - The quaternion (L, z) then has invariant difference 1/2 at q.
- **B0, form:** the sentence "Attempt to pin z instead of C … u not arbitrary" is a garbled leftover. Delete it.
- **Theorem B, gap (minor, fixable):** the proof says "the compositum with the cyclotomic k-field is Galois of 2-power degree". It also uses v₂(q−1) = 1. Both need 4 \| k and φ(k) a power of 2. That holds for k = 4 and k = 8, the cases used (including 131 and 241), but the theorem states no restriction on k. Either restrict k, or argue F ∩ K(ζ_k) = ℚ directly and handle the 2-part.
- **Completeness of the Brauer generators:** checked.
  - Residues lie in H¹ of a punctured line.
  - The geometric part fixed by Galois is ℤ/2 per puncture.
  - The splitting comes from a rational point.
  - Each puncture slot is realised by a pair symbol, and the M-torsion lifts behave correctly.
- **Test bed:** a = (n+v²)/(1−v²) and b = (n+1)/(1−v²) both give ratio v², and the π₁-surjectivity argument is fine.
- **Not re-verified:** the transfer to U° and X° rests on the z75 morphism.
- **Triage:** this is BARRIER-SCOPED (a blindness result). Do not promote it to STATUS.

## §3: Theorem C and Corollary C.1. The mathematics is correct; the triage is too strong.
- **Checked:**
  - π₁ = ℤ³, so the Fermat covers are cofinal.
  - Units on the Fermat open are monomials: their divisor is supported on hyperplane sections, and H² = m ≠ 0.
  - P divides Q, and Newt(Q) is the Minkowski sum.
  - Four vertices with a refined normal fan force a homothetic simplex.
  - The axis points give m \| l, and the line Z = 0 gives l = m.
  - In the Q ≡ 0 case, degenerate subsums are excluded by positivity.
  - In C.1, the torus factor forces a constant t-exponent.
  - The integrality bounds a, b, c ≤ n and d < n hold.
- **Challenge:**
  - **Weak arithmetic content:** since W_n ≅ W_{n′} ≅ W, the theorem amounts to "maps from finite étale covers of P² minus four lines to itself are the S₄ symmetries". Natural descent moves (Vieta-type, divisor swaps) are birational or ramified on the open. So the "surviving possibility" the note concedes is essentially the whole space of moves anyone would use.
  - **Novelty:** the result has the flavour of classical function-field unit equations, and priority is unverified.
  - **Triage:** the "BARRIER-BROAD candidate (§3)" label should become BARRIER-SCOPED, one FRONTIER §6 line.

## §4: Theorem D (PROVED rel. (G) plus the internal, unrefereed energy lemma). Accept.
- **Checked against `H4_NOT_POLYLOG.md`:**
  - Shadow-only events satisfy (4), giving S♯ ≪ L³ log L.
  - The preload is legitimate: H4 §6 already uses an lcm(840, L_Y) start, and the "uniform on any 1-fibre" bound (2) covers it.
  - log Q ≪ B + L⁵ log L.
  - Appending f with residue −1: the exceptional coefficient becomes ±μ, and −μ only helps. f is coprime to every event and cell modulus. Every prime in the fibre exceeds f.
  - The minimum equals f: A = 3 is killed by p ≡ 1 mod 3, and d = (f+1)/4.
  - QR depth up to B, with B ≫ log p.
- **Understated:** the proof gives a least (★) modulus above exp((log p/log log p)^{1/5}). That is a 1/5 exponent, against STATUS's 1/6 for the joint forest/covering quantity, though for a different quantity. Either state it, or say explicitly that it is not claimed.
- **Novelty:** modest, a corollary of H4's machinery.
- **Computation:** the CERTIFIED label is confirmed. The narrative needs correcting:
  - At the panel's B values the theorem's f would be about e^{B^{1/5}}, which is below B, so the theorem is vacuous there. "Despite the opposite extremal theorem" implies a tension that does not exist.
  - f > B is forced trivially, which is why the minimum f sits just above B.
  - The panel neither supports nor strains Theorem D.

## §5 and the last-round hostile checks
- The next-round question (Br[2] orthogonality at 8/131 on the u+n-deleted open) is not B2. At best it explains a known failure; it cannot yield ES.
- The "Internal hostile checks" paragraph and commit `544c2b8`'s "hostile scope audit" are self-audits by the authoring lane, not independent reviews. They did catch the real 16 \| x versus 4 \| s subtlety.
- Form problems:
  - §0 says `Review: none` and should read "cross-review owed (this review)".
  - Section labels skip W3.
  - The labels for B–D appear only inline, not in §0.
  - The script does not regenerate the summary file. It matches stdout, but it is not machine-replayed.

## Recommended export
- **STATUS §1C:** one merged row with Lane 4: infinitely many Mersenne multipliers 4^m−1 at offset +1 have ES on a density-one set of exponents, including square-unit progressions; not full families.
- **FRONTIER §6:** one line each for B0/B (blindness) and C/C.1 (étale-correspondence rigidity).
- **Theorem D:** WAVES line only, unless the 1/5 exponent is made explicit and cross-reviewed.
</code-review>
