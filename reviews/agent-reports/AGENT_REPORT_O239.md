# AGENT_REPORT_O239 — exponential window classes: ES for all 7·4^s + 9 and 3·2^m + 1; Jacobi sterility at unit-square points

Branch side-agent/exp-105 (merged side-agent/exp-near-square and main incl. O238). Main file EXP_105.md (§1 tree, §2
windows); scripts `scripts/z14_*`; certificates `data/z14/cert_c{3_k1,6_k1,7_k9}.txt`. Self-review (deep reviewer,
4 MAJOR, all repaired — see "Repairs"). **ES is not solved. Two infinite families are PROVED (computer-assisted).**

## SHARP
1. **ES holds for every n = 7·4^s + 9 (Thm 2.6, PROVED computer-assisted).** A c₀ ≡ 7 (mod 8) Lemma-3.1 family (7 + 9 = 16:
   profinite unit-square point, hence *no* ET/divisor covering by (J)22 Thm 1.4); every even s ≥ 2 is Mordell-hard
   (n ≡ 121 mod 840). Certificate: 59-leaf tree, 40 window leaves (m = 19 Sophie-Germain at μ = 0; m = 103, 663),
   found with a forced prefix μ mod 36. (O240's orchestrator note says their 7·4^s + 9 attempt had stuck nodes — this one
   closes.) Replay: `PYTHONPATH=scripts uv run python scripts/z14_check.py 7,9 data/z14/cert_c7_k9.txt --explicit 1000` → OK.
2. **ES for every 3·2^m + 1 (Thm 2.2/2.3)** — the (J)22 Cor 1.5 family. *Independently* obtained by O240 (MENU_STERILITY,
   one SG window m = 11 + 6 ET classes); mine is a 9-leaf tree (3 windows, m = 11) + the trivial odd half; closed form of
   the window in EXP_105 §2. Two independent certificates now exist.
3. **Exact Jacobi sterility of unit-square points for windows (Prop 2.4, Cor 2.5, Prop 2.7, Cor 2.8; PROVED).** For
   c₀ + k = 4^J, k ≡ 1 (8), J ≥ 2: a window piece is "visible" at μ = 0 only through an odd 2-adic valuation of its S-integer
   limit; all h = 1, cyclotomic, 'sg', and 'sg1' (j ≥ 3 or w even) windows are blind there; the single surviving shape
   (sg1, j = 1, w odd, m = 4c₀w⁴ − k) is a finite check. Result: **15·4^s + 1, 31·4^s + 33, 7·4^s + 57, 63·4^s + 1,
   47·4^s + 17, 55·4^s + 9 have NO finite covering by ET + divisor + z14 window classes** (μ = 0 sterile for this menu);
   (3,1), (7,9), (23,41), (39,25) have a window at μ = 0. This is the window analogue of CAP_DOWN's T1: T1 bites a window
   at a unit-square point iff all its pieces are square-like there; the escape is a Sophie-Germain piece with 2-adic
   denominator (2/m) = −1. (Correction after review: the n-piece is NOT what escapes; c₀ + A₊ = m/2 already works.)

## Goals status
* k = 105: closed by O238 (pivot); stopped.
* k = 297, 33, 273 and c₀ ∈ {2, 3, 5} open list (17, 161, 233, 257, 281; 73; 41, 89, 209): **NOT decided.** Trees with
  ET (on-the-fly II2/I3 with unbounded composite f from 100-smooth-order primes ≤ 10⁸) + windows stay supercritical
  (e.g. 297: depth 12, uncovered 9.8·10⁻⁸, 5218 stuck; 5·4^s + 41: depth 13, 9.1·10⁻⁸). Stuck nodes sit on ℓ-lines through
  integer square points; on the exact 3-line of 297 **no window fires** (764 windows, μ₃ ∈ {0, 3, 6} mod 9) — at a
  non-unit square point the pieces are integers and the T1 Jacobi argument applies (Assessment; windows with r < 0
  could escape but none found).
* (23, 41): μ = 0 covered, but the 2-line through μ = 0 is not covered at the tested supply (384/1024 residues mod 2¹⁰).
* General criterion (spark 2), Assessment: compactness (Thm 1.4) applies to any clopen menu; for windows the sterility
  of a unit-square point is decided by Jacobi symbols of S-integer piece limits (Prop 2.4–2.8). Conjecture-level: a
  family c₀4^s + k is coverable by ET + windows iff its unit-square point (if any) has a window with an SG piece of
  Jacobi −1 *and* the lines through it are covered — not proved.

## Repairs after self-review (R-O239, reviewer subagent)
* MAJOR 1/2: Prop 2.7 rewritten (cyclotomic windows need h | j at μ = 0, so the "open case" was impossible; hypothesis
  k ≡ 1 mod 8 added — counterexample (1, 15) for c₀ ≡ 1 mod 8 without it). Cor 2.8 finite check added.
* MAJOR 3: checker window cache keyed without j (an altered leaf was accepted) — fixed; parameters validated per leaf;
  mutation now rejected; split primes and a, d ≥ 1 validated; explicit-mode fallback made strict.
* MAJOR 4: u64 overflow in the C Sophie-Germain residues — fixed (search code only; certificates were checked in Python).
* MINOR: m = 663 window listed; ν(0) wording; `or True` assertion removed; z14_line/probe scope caveats in the text.
All three certificates re-pass `--explicit 1000` after the repairs.

## Caveats
* Checker trusts sympy (isprime, n_order, cyclotomic_poly, lambdify on integer inputs). Search code is heuristic.
* "No covering" statements in SHARP 3 are relative to the z14 window menu (unsplit SG numerators in the finite check).
  (R254 repair: the menu is now defined explicitly in EXP_105 §2 "The z14 window menu"; richer menus — split Y-pieces, O245 — are not covered.)
* Novelty (R254 repair): no prior proof of ES for all 3·2^m + 1 or all 7·4^s + 9 was found (brief web search; see
  EXPONENT_COVERING §5.4, non-exhaustive).
* Independent reviews: R253 (reviews/exp-105-review.md) and R254 (reviews/exp-105-review-2.md) — headline SOUND, only MINOR
  wording repairs (applied, marked R253/R254).
* Scratch in /tmp/z14 (prime list 4 MB, tree outputs) kept for possible repair rounds; delete when the branch is closed.

## Sparks
* S1. (23, 41): cover the 2-line X_{0,2} through the unit-square point (needs primes with even ord_q(4) or a window
  with a 2-adic-sensitive SG piece) — then the tree likely closes as for (7, 9).
* S2. Non-unit square points (297's 3-line): windows with j > s₀ evaluate to S-integers on the line; a Jacobi
  classification like Prop 2.7 there would say whether windows can ever help 297/33/273 — or prove they can't.
* S3. Splitting SG numerators by fixed primes, and Type I/genus-≥1 polynomial-in-b identities (O245 menu ladder).
* S4. Tree heuristics: forced prefixes (period of the μ = 0 window first) were decisive for 7·4^s + 9; a best-first
  search ordered by node measure would be the next engineering step for the supercritical cases.
