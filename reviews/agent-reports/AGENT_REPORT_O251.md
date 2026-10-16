# AGENT REPORT O251 — lattice meeting point / class-group slice moves (checkpoint 1)

Branch side-agent/lattice-meeting (merged side-agent/astra-bridge first, as instructed). Deep file LATTICE_MEETING.md;
memos BRAINSTORM/z23_*.md (7, indexed in BRAINSTORM/README.md); scripts scripts/z23_*.py (7); no data files.
**ES is not solved; no infinite case claimed.**

## SHARP:
* **The meeting point (2k, 1) is a finite set, empty for 99 primes ≤ 10⁶ (Prop 1.1, PROVED + CERTIFIED).**
  ASTRA_BRIDGE Thm 3.4(c)'s ES points = {(a, b, k) : a + b = k(4ab − p)} ⟷ {(a, g) : g | p + 4a², g ≡ −1 (4a)}, ES point
  4/p = 1/(ab) + 1/(pka) + 1/(pkb); finite since (4a−1)(4b−1) ≤ 4p+1. Empty for exactly 99 of 39 175 primes p ≡ 1 (4)
  ≤ 10⁶: 13, 37, 97, 181, 193, 541, 673, … (all ≡ 1 mod 12; two independent scans agree to 2·10⁴). So no descent of any
  kind in the slice lattices can end at height 1 for those p.
* **The correct meeting set is a square-class meeting (Thm 1.4, PROVED; 89 117 slices checked set-by-set).** At a slice
  g (h = (g+1)/4) the Type II solutions with y = ph are in bijection with the k | h such that
  d_k := (−4k²p mod g) = Y_k² mod g divides k (Y_k = the height class of the vertical line M = 2k): formally the lattice
  point (2k, √d), ET's parameter d. The 99 primes are rescued at d = 2 (96), 3 (1), 5 (2) on slices of the same ℤ[√−p].
* **Class-blindness (Cor 1.5, PROVED).** d_k is root-free, so the ES predicate on ideals 𝔤 depends only on N𝔤
  (∃ k | (g+1)/4, d | k with g | 4k²p + d). Stronger than WINDMILL Prop 10.3 in these coordinates: a class-group walk
  is, for ES, the integer walk g → gℓ.

## What was done (labels)
1. Prop 1.1 / Cor 1.2 (PROVED): explicit finite meeting locus; T1 empty; p ≡ 2 (3) always hits (a, g) = (1, 3).
   Certified emptiness list (§1). Rescue fields (§1.4, CERTIFIED).
2. Thm 1.4 / Cor 1.5 (PROVED, repackaging of ET Prop 1.3 = EXP_OPEN row II-ad): slice criterion and norm-only dependence.
3. §2 moves (PROVED): composition coordinates (M, Y) ↦ (uM + vY, uY − pvM); controlled lifts u ≡ 1 (mod 4h) keep h | h′ but
   ES propagates only *down* (tower = divisor lattice of 4k²p + d); fixed-line Vieta/Gauss reduction on forms
   [g, 2Y, D] of disc −16k²p — admissibility is a genus condition iff k | 6 (B1), else the ray-class mod 4k B2 datum.
4. §3 Prop 3.1 (PROVED): slices and Type I levels are unforced at every prime (4h ≡ 1); a Type II point has ≤ 1 forced
   slot (the window). Goal (3)'s "two forced slots" point does not exist.
5. §4 (EVIDENCE + JMV 2009 under GRH): worst-start Cayley distance to an ES class ≤ 4–8 steps whenever one exists
   (p ≤ 3000, k ∈ {1,2,3,5}); lines without ES classes 26–73 %. The Gauss-reduction descent from the least-root window
   shot is the identity (all 1565 starting forms already reduced). Walks add reachability, never existence.
6. Verdict (§5, Assessment): the class-group walk route is closed in the precise sense of Cor 1.5 + §2–§4; what would
   reopen it is a joint-factorisation identity forcing h′'s divisors and p mod g′ simultaneously (H-A), not class data.

## Numerics (all exact; each ≤ 25 s; ulimit -v 8 GB, ≤ 2 cores)
z23_meet (p ≤ 10⁶ exhaustive by Prop 1.1 bound; odd squares ≤ 10⁶ empty), z23_shape (k-scan cross-check, p ≤ 2·10⁴),
z23_alld (p ≤ 6000, g ≤ 3000: criterion = brute force), z23_rescue (99 primes), z23_cayley (p ≤ 3000; T1 odd squares no
ES class), z23_descent (p ≤ 2·10⁴).
Known limitation: z23_cayley's composition skips a step when both outer coefficients share ℓ (5 lines with an
unreached remainder, flagged in §4; does not affect the distances reported for reached classes).

## Sparks (not pursued)
* Reciprocity across d: in ℚ(√−p, √d) relate solvability at d and d′ (z23_biquadratic_height). Expect B2/B5 to block forcing.
* Is the d = 1 locus empty for infinitely many p? Heuristically |𝓜(p)| grows (mean 13.4 at p ≤ 10⁵) and emptiness
  thins (22 / 23 / 54 per decade-block); a proof of infinitude would be a B1-type statement (Landau-type sieve on
  p + 4a², a ≤ √p/2 simultaneously) — plausible via a Selberg sieve upper bound? Not attempted.
* Upward controlled lifts: choose u | (4k²p + d)/g with u ≡ 1 (mod 4h) — a divisor-of-a-given-integer event; maybe
  combine with Astra's forced factors (CRT-prescribed ℓ | h) to make one lift forced.
