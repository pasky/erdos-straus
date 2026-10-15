# AGENT_REPORT_O235 — exponential near-squares: label points, ℓ-lines, k = 105

Branch side-agent/exp-near-square (merged side-agent/sign-fields, then main). Main file EXP_NEAR_SQUARE.md; memos
BRAINSTORM/z11_*.md (3); scripts scripts/z11_* (tree.c, pool, tree2, cantor, cantor_dfs, cantor_tree, fiber, line,
check_cantor); data/z11/ (one check log). **ES is not solved; no new infinite ES family is certified here.**

## SHARP
1. **Mixed points = label points, and why they evade (PROVED, Lemma 1.2).** A label point puts an integer square point of
   4^x + k in every ℓ-adic component of the exponent. At σ-pure primes ν ≡ s_x², so any modulus made of pure primes sees a
   *unit square* (CRT of squares) and no ET class can contain it; the D_q of the square points depend only on ℓ | ord_q(4)
   and are switched off by a different label there. Binary core Π_ℓ{4, −2} of 4^s + 105: **covered by 10 classes**
   (CERTIFIED, independent replay `z11_check_cantor.py`, support {2,3,5,11,17,19,29,47}). Quaternary core {4,−2,2,3}: open.
2. **ℓ-lines through square points, exponential analogue of (J)26's r-generic lines (diagnosis + EVIDENCE, §2).** The
   per-branch Ẑ tree (C) drives uncovered measure to 3·10⁻¹¹ for k = 105, 2·10⁻¹¹ for k = 297, but stuck nodes multiply
   ×10–100 per level (supercritical branching). k = 297 has ONE square point (no mixed points) and diverges equally: stuck
   nodes lie near X_{3,3} = {μ_ℓ′ = 3 ∀ℓ′ ≠ 3}, square at every q with 3 ∤ ord_q(4). The line itself is fully covered
   (z11_line: classes with v₃(L_M) ≤ 2), but only by classes with large new ℓ′ in their period — the tree must split on ℓ′,
   the on-line child is pure and survives. Sharp question: is there a measure argument on ℓ-lines like (J)26's? Heuristic
   says no (Σ τ²/q over q with ℓ | ord diverges) ⇒ coverings exist but are huge.
3. **Lemma 3.1 (PROVED, elementary): c₀·4^s + k has a unit-square point iff c₀ + k = 4^j**; non-trivial cases (3, 1) and
   c₀ ≡ 7 (mod 8), k = 4^j − c₀ (7·4^s + 9, 15·4^s + 1, 23·4^s + 41, …) have **no finite ET/divisor covering**.

## Goals
* (1) k = 105: **NOT decided.** Neither a certificate nor a sterile point. Progress: binary core certified; O232's period
  explosion replaced by a tree whose measure decays fast but whose stuck count grows; the bottleneck identified (label set
  + ℓ-lines; class supply per fibre). No sterile point found anywhere (μ*, σ₀ = (B on {3,13,17}) neighbourhoods all hit
  by classes with larger ℓ in their period).
* (2) k = 33, 273, 297: same picture (tree tables in §2; 273 also has 4⁴ + 273 = 23², missed by O232; 297 has one point).
* (3) c₀ ∈ {2, 3, 5} surveyed (EVIDENCE, not replayed; probably many Mordell-immediate — R236 D1 caveat applies);
  Lemma 3.1. 4^a·9^b + k NOT done.
* (4) CONJECTURE E (weak): coverable iff c₀ + k ≠ 4^j; B1 over Ẑ-parameter spaces becomes quantitative (branching).

## Caveats for the reviewer
* z11_tree.c / z11_tree2.py emit stream certificates but no run terminated, so there is NO z11_check stream checker
  (nothing to check). The "uncovered measure" numbers are from the C tree (double precision, depth-capped).
* z11_cantor*.py, z11_line.py, z11_fiber.py trust mordell_lib.residue_table (no replay except Result 1.1).
* Line result for k = 297 is a coverage computation without witness replay.
* Survey (c₀ = 2, 3, 5) used the O232 search (no ec_cert run).
* Large pools were built in /tmp (500 MB), not committed.

## Sparks (not pursued)
* S1. Label tree in C with a much larger supply (q ≤ 10⁸ prime moduli: II2 + D tests are O(τ((q+1)/4)) per value) —
  decide the quaternary core of 105.
* S2. Hybrid certificate: tree on small primes + per-node *line certificates* (classes with frozen components) — a
  certificate format where a node is closed by a covering of its ℓ-line plus a separately covered off-line complement.
* S3. A (J)26-style measure bound on ℓ-lines restricted to classes of modulus ≤ X: quantify the minimal covering size
  (lower bound on certificate size for 105 — would turn "huge" into a theorem).
* S4. 4^a·9^b + k (Ẑ² exponents): enumerate unit-square points via k = (y − w)(y + w), then run the tree in 2D.
* S5. m-polynomial families with m = 2^s (period ord_q(2), sees the sign of 2^s mod q) as extra supply.
