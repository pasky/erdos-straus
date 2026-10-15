# s6_unique_forced_cap0 — forced cap 0 at a window happens only at m = 3 (O238; mandatory (i) × (J)57)

## Idea
(J)57: "4 costs zero bits" (Fano pigeonhole). Window analogue: when does the forced bit (K a non-residue mod every prime of
m) force cap 0 for EVERY K? **Prop (PROVED).** Let m ≡ 3 (mod 4) be a forced window (CAP_POINTWISE Thm 1.1′; R246 repair: more generally any admissible
m of Thm 1.1′, i.e. m ≡ 4 − n (8) with all prime factors ≡ 3 (4) — then (ℤ/m)^* = E × U with E ≅ (ℤ/2)^r, so U = 1 ⟺ m = 3
⟹ (ℤ/m)^* = {±1}; brute force over all admissible m ≤ 300: only m = 3, `scripts/review_r246_pigeon.py`). Cap 0 is
forced for all admissible K iff the odd part U of (ℤ/m)^* is trivial, iff λ(m) | 2 with m ≡ 3 (4), iff m = 3.
*Proof.* If U = 1, (ℤ/m)^* = {±1}, every QNR prime of K is ≡ −1 and has exponent ≥ 1: −1 ∈ Σ_m(K). If U ≠ 1, take K = s
a prime with s ≡ −u₀ (mod m), u₀ ∈ U \ {1} (Dirichlet; R245 repair: this makes s a non-residue modulo every prime of m; the statement concerns the δ_n = 0 slice of CAP_DOWN Lemma 3.1): Σ_m(s) = {1, s, s⁻¹} ∌ −1 (s has order 2o > 2, so
s ≢ −1); such s is a forced K (a non-residue in every component) for n := 4s − m, s large in its class. λ(m) | 2 and m ≡ 3 (4) leave m = 3 only (m | 24). ∎
With the 2-adic addendum (CAP_DOWN Thm 1.2 Addendum: q = 3 always fires, even in the excluded case), the window m = 3 is
exactly the classical identity for n ≡ 2 (mod 3). So the "degree-2 accident" ((J)19, CAP_DOWN Prop 6.1) has a sharp
form: the forced level equals cap 0 only where the unit group is 2-elementary, i.e. at Mordell's first congruence.
(Assessment, R246 repair: not proved) For numerator ν the same statement: windows m ≡ −n (mod ν) with 2-elementary unit group, m | 24 — the classical
small-modulus identities. Fano's "4 costs zero" ((J)57) is the 2-adic analogue of U = 1.

## Literature
Mordell, *Diophantine Equations* (1969) §30 (the classical congruence identities); CAP_DOWN.

## Barrier screen
This IS a barrier statement: B1 (the forced cap-0 windows are a finite menu of congruences). T1 respected (no forced window
at squares for ν = 4).

## Cheap numerics
Trivial (the proof is constructive). s6_witness_caps.py confirms: every p ≡ 1 (4) with (3/p) = −1 has cap 0 at m = 3.

## Assessment
PROVED, small. Negative: the forced mechanism yields cap 0 for all K only at m = 3.
