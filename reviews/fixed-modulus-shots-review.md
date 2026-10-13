# R191 — hostile review of FIXED_MODULUS_SHOTS.md (O191)

Reviewer: R191 side agent. Documents: FIXED_MODULUS_SHOTS.md, BRAINSTORM/bsN_divisor_box.md, reviews/agent-reports/AGENT_REPORT_O191.md
(as merged from side-agent/fixed-modulus-shots). All checks below use from-scratch code `scripts/review_fms_*.py`; the
author's `scripts/fms_*` were not used.

## Summary verdicts

(filled in progressively; see §§ below)

## A. Lemma 1.1 (Type II certificate cube) — SOUND

Re-derivation. 4cdj ≡ 1 (mod h) makes 4cd, 4dj units; 4cd(pj + c) ≡ p + 4c²d and 4dj(pj + c) ≡ 4dj²p + 1, so the three
divisibilities are equivalent. e·h = p + 4c²d with h ≡ −1 (mod 4cd) gives p + e ≡ 0 (mod 4cd); x + c²d = cdj·e from
4(x + c²d) = e(h + 1); then 1/y + 1/z = (x + c²d)/(p·cdj·x) = e/(px) = 4/p − 1/x. The bound: h ≤ pj + c gives
4cd ≤ p + (c + 1)/j ≤ p + c + 1, hence 3cd ≤ p + 1; so p ∤ c, d, p ∤ e, p ∤ x. Converse as written is correct (I
re-did it with D = ey′ − x, DD′ = x²). The map cube → solutions is **not injective** (points (bs, D/(b²s²), as) for every
s with s² | D/b² give the same solution); the text's "from at least one cube point" is accurate.

From-scratch check (`scripts/review_fms_cube.py 3000 1500`, 5 s): independent divisor-method Type II solver (ordered
(y, z)), itself validated against a fully naive triple loop for p ≤ 70. For **all 428 primes 5 ≤ p ≤ 3000** the set of
cube solutions equals the brute-force Type II set exactly; at every cube point the three divisibilities hold, p ∤ x,
3cd ≤ p + 1, and the triple is an exact solution. For p ≤ 300 a **wide** scan (all cd ≤ 2p, ignoring the 3cd ≤ p + 1
cut) finds no further cube point.

## B. Lemma 4.1 (Type I cube) — SOUND-AFTER-REPAIRS (minor)

Algebra re-derived: 1/y + 1/z = 4/p − 1/x ⟺ u(4vwf − p) = pv + f. Converse correct. Brute force (independent solver
enumerating the smaller of y, z in (p/4, 2p/3]) vs cube along (w, f), wf ≤ 2p/3: **identical ordered Type I sets for
all 237 primes 5 ≤ p ≤ 1500**; at every enumerated point with gcd(g, p) = 1 the divisibilities g | pv + f and
g | 4v²w + 1 agree. Non-Type-I cube points (p | uvwf) give genuine (Type II) solutions, as claimed.
Defect m1 below (hidden hypothesis in the three-way equivalence).

## C. Prop 6.1 (finiteness, O(p²)) — SOUND

Type II: x ≤ p/2 (else 1/y′ + 1/z′ > 2 — the text's route via y′ = 1 is also fine). The text's "both y′, z′ ≤
x(x + D)/(eD)" is not literally true for the chosen order (if D > x then y′ = (x + D)/e > x(x + D)/(eD)); the correct
statement is max(y′, z′) = x(x + D_min)/(e·D_min) with D_min = min(D, D′) ≤ x (DD′ = x²), ≤ x(x + 1)/e — same bound
(defect m2). f(e) = (p + e)(p + e + 4)/(4e) is convex on (0, p], f(1) = (p+1)(p+5)/4 > f(p) = p + 2, so
h ≤ (p+1)(p+5)/4 − 1. Type I: wf ≤ 2p/3, g ≤ p² + 4wf² ≤ 25p²/9 < 3p². Numerics: max h/((p+1)(p+5)/4) → 1, the
bound (p+1)(p+5)/4 − 1 is **attained** at 217 of 428 primes ≤ 3000 (all p ≡ 3 mod 4: e = 1, D = 1); max g/p² = 1.33
(p = 7), so the Type I constant 3 is loose but correct.
