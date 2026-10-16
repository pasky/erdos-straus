# AGENT REPORT O249 — Astra bridge: square removal ↔ exponent cap (checkpoint 1)

Branch side-agent/astra-bridge. Main file ASTRA_BRIDGE.md; memos BRAINSTORM/z21_*.md (3); scripts scripts/z21_*.py (5);
data data/z21_*.txt (tiny). Astra (../erdos-straus-astra at d7300f8) was only read; no file there was written and no
Astra script was run. Internal hostile review (reviewer subagent, committed by it as reviews/astra-bridge-9bcb149a-hostile.md):
no FATAL, five MAJOR (M1–M5), all repaired in the main file and marked R-O249. **ES is not solved; no infinite case claimed.**

## SHARP:
* **Lattice meeting point (Thm 3.4, PROVED, 168 858 shots checked exactly).** For a slice g ≡ 3 (4) (prime or composite,
  gcd(g, p) = 1), h = (g+1)/4, root ρ² ≡ −p, lattice L_ρ(g) = {Y ≡ ρM (mod g)}: Astra sources = the points (m, 1)
  (horizontal line Y = 1); Claude shots with odd overflow = the points (2k, Y) with **k | h** (vertical lines), with
  den z = Y² exactly (overflow = Y; self-mute ⟺ rad Y | h); ES shots = the intersection (2k, 1), k | h. Astra's q is
  Claude's *slice* g (not the window, as the orchestrator guessed), Astra's s is EXPONENT_CAP Prop 1.3's D, Astra's
  twist m is Prop 1.3's 2k.
* **Genuineness excludes exactly the classical line (Thm 3.1(c),(d), PROVED; 9415/9415 checked).** For even m:
  s ≡ −1 (mod 2m) ⟺ m | (q+1)/2, and then the source gives an honest ES solution sharing y = ph (the classical
  "4k²p + 1 has a divisor ≡ −1 (mod 4k)"). Astra's genuineness gcd(m, h) = 1 rules this out except m = 2.
* **Same prime, opposite parity (Prop 5.1).** An admissible q (q ≡ 3 (4), (q/p) = −1) is *forced* as a Claude window
  ((K/q) = −1) and *unforced* as Astra's slice ((h/q) = +1).

## What was done (labels)
1. Slot dictionary (§1, PROVED, scope repaired): both programmes are rational points of 4/p with square denominators;
   Astra sources twist the p-free coordinate, Claude window shots a p-divisible one with self-muteness. Not disjoint:
   Astra's 193 twist-5 certified state is a Claude ES^{(y,1)} point. Genuine sources can never be scalar-reduced (m = 1 forced).
2. Thm 2.1 (PROVED): Astra certified states (e, H, r) at twist n ⟷ twisted Type I points (U/n², v, pH), r | H²,
   e | n² + 4r; ES = class −4⁻¹. Cor 2.2 (PROVED, 62 179 pairs checked): a prime level carries an Astra state iff
   H = (pe+1)/4 has a p-non-residue prime factor (Kronecker at 2). Claude-alive ⊊ Astra-alive (reviewer's p = 5, e = 7).
3. Prop 3.3 (PROVED): T1 — Astra sources and certified Type I states are empty at odd squares.
4. Fixtures (§4, exact): 51 distinct Astra triples re-verified; every exit is a classical small-modulus certificate
   (25 Type I at levels ≤ 143, 5 Type II at windows ≤ 39). The 15241 fold = Claude window shot R = 11, Q = 2.
5. Transfers (§5): phase diagram (Prop 5.2, PROVED) — without self-muteness, prime twists and twists < q₀/2 are free;
   macro table (Assessment) — Astra's fixed-level moves act on one divisor r; no forced cap descent found; heights
   (§5.4) — Claude's results live at small twists, Astra's compression problem at r → ∞; no transfer.
6. The bet (§6): **no bounded-cap proof obtained (Assessment).** PROVED pieces: saturation (whole-subgroup covering) fires
   only at levels e ≤ p^{O(1/log log p)} (Prop 6.1); Type I aliveness and −4⁻¹ ∈ ⟨primes of H⟩ can be forced by CRT (Prop 6.2).
   Gate-by-gate B2 table 6.1. Nothing here excludes a single target in a small box.

## Numerics (all exact rationals; ≤ 11 s each)
z21_dict (p ≤ 10⁵, q ≤ 100, m ≤ 600: 2.35M sources), z21_typeI (p ≤ 10⁵, prime levels ≤ 100; odd squares ≤ 10⁶),
z21_lattice (p ≤ 3000, g ≤ 400), z21_phase (p ≤ 10⁵), z21_fixtures (all Astra fixtures). Reviewer replays passed.
Not done: primes to 10⁶ for the dictionary checks (the claims are proved; the runs are code checks).

## Sparks (not pursued)
* Moving the slice: does ideal composition in Cl(−4p) (g → g·ℓ) carry Claude points (2k, Y) to smaller |Y| while
  keeping k′ | h′? (BRAINSTORM/z21_lattice_meeting_point.md)
* A Type II ES point has one window and two slices; classify the forced/unforced parity of all slots; look for a point
  with two forced slots (z21_window_vs_slice.md).
* Genealogy-forced small orders: can Astra's composite-q genealogies make an inherited prime ℓ have ord_e(ℓ) ≤ v_ℓ(H)
  at the next level (would remove the §6.2 difficulty)? (z21_gates_are_B2.md)
* Windows of the twisted input pm²: K = (pm² + q)/4 is shaped by m, but x = K is prime to m, so nothing descends;
  a window-type construction with x ≡ 0 (mod m²) would be new.
