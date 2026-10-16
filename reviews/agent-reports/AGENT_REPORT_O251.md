# AGENT REPORT O251 — lattice meeting point / class-group slice moves (checkpoint 1)

Branch side-agent/lattice-meeting (merged side-agent/astra-bridge first, as instructed). Deep file LATTICE_MEETING.md;
memos BRAINSTORM/z23_*.md (7, indexed in BRAINSTORM/README.md); scripts scripts/z23_*.py (8); no data files.
**ES is not solved; no infinite case claimed.**

## SHARP:
* **p = 3361: no Type II solution lies on any slice lattice of ℤ[√−p] (CERTIFIED, two independent exhaustive methods).**
  Its only Type II solutions are 4/3361 = 1/850 + 1/(3361·25) + 1/(3361·170) and 1/841 + 1/(3361·290) + 1/(3361·8410);
  all four slices 99, 679, 1159, 33639 have −3361 a non-square. So the ASTRA_BRIDGE Thm 3.4 lattice framework
  (Cl(−4p), Astra line Y = 1, Claude lines k | h) cannot see Type II at 3361 at all. Reason (PROVED): a Type II
  slice g | p + 4a²d is split iff the ET parameter d is a square mod g. 3361 is the only such prime ≤ 10⁷ (only the 160 primes
  ≤ 10⁷ with empty d = 1 locus can be candidates; 159 of them have a split-slice solution).
* **The meeting point (2k, 1) is a finite set, empty for 99 primes ≤ 10⁶ (Prop 1.1, PROVED + CERTIFIED).**
  Thm 3.4(c)'s ES points = {(a, b, k) : a + b = k(4ab − p)} ⟷ {(a, g) : g | p + 4a², g ≡ −1 (4a)}, ES point
  4/p = 1/(ab) + 1/(pka) + 1/(pkb); finite since (4a−1)(4b−1) ≤ 4p+1. Empty for exactly 99 of 39 175 primes p ≡ 1 (4)
  ≤ 10⁶: 13, 37, 97, 181, 193, 541, 673, … (all ≡ 1 mod 12; two independent scans agree to 2·10⁴).
* **Slice criterion (Thm 1.4, PROVED; repackaging of ET Prop 2.6).** Type II with y = ph ⟺ ∃ k | h with
  (−4k²p mod g) | k (a surjection k ↦ solution); at split slices this is the square-class meeting Y_k² ≡ d (mod g), d | k
  ("height √d"). Consequently the ES predicate on slice ideals depends only on the norm (Cor 1.5; its "class methods
  can act only through norms" reading is Assessment).

## What was done (labels)
1. Prop 1.1 / Cor 1.2 (PROVED): explicit finite meeting locus; T1 empty; p ≡ 2 (3) always hits (a, g) = (1, 3).
   Certified emptiness list (§1). Rescue fields (§1.4, CERTIFIED).
2. Thm 1.4 / Cor 1.5 (PROVED, repackaging of ET Prop 2.6 = EXP_OPEN row II-ad): slice criterion (surjection) and norm-only
   dependence; lattice visibility needs d square mod g (§1.3–1.4; 98/99 empties visible, 3361 not).
3. §2 moves (PROVED): composition coordinates (M, Y) ↦ (uM + vY, uY − pvM); controlled lifts u ≡ 1 (mod 4h) keep h | h′ but
   ES propagates only *down* (congruence-filtered divisors of 4k²p + d); fixed-line Vieta/Gauss reduction on forms
   [g, 2Y, D] of disc −16k²p — for coprime first coefficients admissibility is a genus property iff k | 6 (B1), not
   preserved by all reduction moves; else the ray-class mod 4k B2 datum.
4. §3 Prop 3.1 (PROVED): slices and Type I levels are unforced at every prime (4h ≡ 1); a Type II point has ≤ 1 forced
   slot (the window). Goal (3)'s "two forced slots" point does not exist.
5. §4 (EVIDENCE + JMV 2009 under GRH): worst-start Cayley distance to an ES class ≤ 4–8 steps whenever one exists
   (p ≤ 3000, k ∈ {1,2,3,5}; 5 lines uncertified); lines without ES classes 26–73 %. ES class = sub-event of the
   divisor event (needs d square mod g). The Gauss-reduction descent from the least-root window
   shot is the identity (all 1565 starting forms already reduced). Walks add reachability, never existence.
6. Verdict (§5, Assessment): the class-group walk route, as posed, yields no existence mechanism (Cor 1.5 + §2–§4, 3361); what would
   reopen it is a joint-factorisation identity forcing h′'s divisors and p mod g′ simultaneously (H-A), not class data.

## Review
Internal hostile reviewer pass (on 074c1b47): 1 FATAL (claimed all 99 rescues lie on ℤ[√−p] slice lattices — false,
9 at least-d, and 3361 at every d), 5 MAJOR (Thm 1.4 not a bijection; §2.3 k | 6 invariance false as written; Cor 1.5
reading a non sequitur; §4 target sets conflated; mean |𝓜| miscounted 13.4 vs 24.4 ordered), minors (wording, ET
citation = Prop 2.6, Landau as heuristic, BFS caveat, memo contradiction). All repaired, marked R-O251. The 99-prime
list, the 96/1/2 histogram and all tables were independently reproduced by the reviewer.

## Numerics (all exact; each ≤ 25 s; ulimit -v 8 GB, ≤ 2 cores)
z23_meet (p ≤ 10⁶ exhaustive by Prop 1.1 bound; odd squares ≤ 10⁶ empty), z23_shape (k-scan cross-check, p ≤ 2·10⁴),
z23_alld (p ≤ 6000, g ≤ 3000: criterion = brute force), z23_rescue (99 primes), z23_cayley (p ≤ 3000; T1 odd squares no
ES class), z23_descent (p ≤ 2·10⁴), z23_split (99 empties; brute-force all Type II solutions of 3361).
Known limitation: z23_cayley's composition skips a step when both outer coefficients share ℓ (5 lines with an
unreached remainder, flagged in §4; does not affect the distances reported for reached classes).

## Sparks (not pursued)
* Reciprocity across d: in ℚ(√−p, √d) relate solvability at d and d′ (z23_biquadratic_height). Expect B2/B5 to block forcing.
* Is the d = 1 locus empty for infinitely many p? Heuristically |𝓜(p)| grows (mean 13.4 at p ≤ 10⁵) and emptiness
  thins (22 / 23 / 54 per decade-block); a proof of infinitude would be a B1-type statement (Landau-type sieve on
  p + 4a², a ≤ √p/2 simultaneously) — plausible via a Selberg sieve upper bound? Not attempted.
* Upward controlled lifts: choose u | (4k²p + d)/g with u ≡ 1 (mod 4h) — a divisor-of-a-given-integer event; maybe
  combine with Astra's forced factors (CRT-prescribed ℓ | h) to make one lift forced.
