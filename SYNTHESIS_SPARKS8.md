# SYNTHESIS_SPARKS8 — cross-combinations of wave AA ((J)84–(J)87, relays O256/O257) (task O258, synthesis VIII)

Status: O258 checkpoint 1 (unreviewed). **ES is not solved here, and no infinite case of ES for primes is claimed.** Labels as
in DISCOVERIES.md. Memos `BRAINSTORM/s8_*.md`; scripts `scripts/s8_*` (`s8_lines.c` = census engine, `s8_check_b1.py` =
independent brute-force checker); logs `logs/s8_*` (tiny).

Notation. Type II (ET): c n + a + b = 4abcd, (x, y, z) = (abd, acdn, bcdn). Window m := 4abd − n = (a + b)/c, K_m := (n + m)/4.
Lines (one-parameter sub-families of Type II): **b = 1 line** (cn + a + 1 = 4acd), **c = 1 line** (n + a + b = 4abd; this is
PARITY_AUDIT's (★)), **d = 1 line** (LATTICE_MEETING's meeting locus).

## 0. Iteration log
(I1) Mandatory (i), least residue × height-dependent target. Wrote the single-p event in four equivalent coordinates (window,
twisted modular hyperbola, Kloosterman fraction, mutual shift pairs; §1). Construction attempts: (1) Minkowski/Thue on the
hyperbola — Thue produces points of the twisted hyperbola Xε ≡ u (p) of uncontrolled height; ES needs a height-dependent
class (barrier hypothesis it meets: "target fixed in advance"). (2) DFI 1997 — its bilinear Kloosterman-fraction bounds ARE
uniform in the numerator a = p (so "fixed p" is not the obstruction); what fails is volume: the ES indicator has expected
count O(1) per dyadic box, so any equidistribution statement must save the full box volume (Lemma 1.5). (3) Piecewise
linearity of y ↦ (−p mod y) (continued-fraction structure) linearises the least residue on each interval (p/(k+1), p/k] and
returns exactly ET's window form (Prop 1.4). All three return to B2; recorded as a precise "what fails" (§1.6).
(I2) Mandatory (ii), support-1 lottery. Checked the brief's form: s | jp + 1, s ≡ 3j − 1 (4j) is the b = 1 line with a = s prime
(and forces j even unless s = 2). Found the **b = 1 duality** (Prop 1.3): b = 1 ⟺ some mutual shift pair (g, D) of p has
4 | D. Census (§2): **the b = 1 line fails at exactly three primes p ≡ 1 (4) ≤ 10⁸ — 193, 2521, 66529 —** and the c = 1 line at
14 primes ≤ 10⁷ and none in (10⁷, 10⁸]; the two lines never fail together ≤ 10⁸ (EVIDENCE). Per-j events are pairwise
independent to within 0.4 % on average (max ratio 1.27); joint all-j failure is 1.5 × the independence prediction. A
deterministic forcing of one j would have to be 4-specific: the k = 8 analogue of the two-line union fails at 34 primes < 8000,
including 131 and 241.
(I3) Mandatory (iii), forced windows × T1 adversary: §3.
(I4) Mandatory (iv), positivity × signed slices: §4.
(I5) Own: profinite proximity to the T1 point 1 (smooth p − 1) as a hardness coordinate (s8_profinite_proximity).

## 1. Deep item 1: one event, four coordinates (mandatory (i))

**Definition 1.1.** For n ≥ 1, the set of *mutual shift pairs* is MP(n) := {(x, y) ∈ ℤ²_{≥1} : x | n + y, y | n + x, xy | n + x + y};
N(x, y) := (n + x + y)/(xy). (If gcd(x, y) = 1 the last condition follows from the first two.)

**Proposition 1.2 (Type II = mutual shift pairs with a 2-adic quotient condition; PROVED, ET reparametrised).** For odd n,
Type II solutions (a, b, c, d) of 4/n correspond bijectively to triples (c, (x, y)) with (x, y) ∈ MP(cn) and 4c | N(x, y), via
(x, y) = (a, b), d = N/(4c). In particular
* the c = 1 line ⟺ ∃ (x, y) ∈ MP(n) with 4 | N(x, y);
* the d = 1 line ⟺ ∃ c, (x, y) ∈ MP(cn) with N = 4c;
* the b = 1 line ⟺ ∃ c: cn + 1 has a divisor w ≡ −1 (mod 4c) with w ≤ (cn + 1)/2 (x = (cn + 1)/w, y = 1).
*Proof.* cn + a + b = 4abcd says exactly ab·4cd = cn + a + b; this gives a | cn + b, b | cn + a and N = 4cd. Conversely N = 4cd with
d ≥ 1 integral reverses it. For b = 1: a(4cd − 1) = cn + 1. ∎

**Proposition 1.3 (b = 1 duality; PROVED).** For n ≡ 1 (mod 4): the b = 1 line holds ⟺ ∃ (g, D) ∈ MP(n) with 4 | D. Explicitly
(a, 1, c, d) ↦ (g, D) = ((n + 4d)/(4cd − 1), 4d), with N(g, D) = c; inverse (g, D = 4d) ↦ c := N(g, D), a := (cn + 1)/(4cd − 1).
Equivalently: **b = 1 ⟺ ∃ d ≥ 1: n + 4d has a divisor ≡ −1 (mod 4d)** (other than n + 4d itself).
*Proof.* w := 4cd − 1 divides cn + 1, hence divides 4d(cn + 1) − n·w = n + 4d; put g := (n + 4d)/w. Then g(4cd − 1) = n + 4d, i.e.
4cdg = n + g + 4d: so g | n + 4d, 4d | n + g, and N(g, 4d) = c. Conversely, from 4dgN = n + g + 4d put c := N, w := (n + 4d)/g =
4cd − 1; since 4cd ≡ 1 (mod w), c(n + 4d) ≡ cn + 1 (mod w), so a := (cn + 1)/w ∈ ℤ_{≥1}. The divisor form: w | n + 4d with
w ≡ −1 (4d) is the pair (g, 4d); w ≠ n + 4d as n + 4d ≡ n ≢ −1 (mod 4). ∎
(Checked: `s8_lines census` decides both forms completely for all p ≡ 1 (4) ≤ 10⁶: 0 mismatches.)
*Reading.* The two lines b = 1 and c = 1 are the two 2-adic faces of the one set MP(p): **b = 1 ⟺ some pair has a coordinate
≡ 0 (4); c = 1 ⟺ some pair has quotient ≡ 0 (4).** For p odd and (x, y) ∈ MP(p) coprime, at most one coordinate is even and if both
are odd then N is odd (xyN = p + x + y). So b = 1 ∪ c = 1 fails ⟺ every pair of MP(p) with an even coordinate x has v₂(x) = 1
and v₂(N) ≤ 1. T1 (PROVED, by ET Prop 1.6): for n = m² every pair of MP(m²) has this shape.

**Proposition 1.4 (piecewise-linear least residue returns the window form; PROVED).** For y ∈ I_k := (n/(k+1), n/k], (−n mod y) =
(k + 1)y − n. Hence the pairs (x, y) ∈ MP(n) with x < y and y ∈ I_k are exactly x = (k + 1)y − n with x | k + 2 (if n is
prime and x < n); writing s := k + 1: **MP(p) ∩ {x < y} ↔ {(x, s) : x | s + 1, s | p + x}**, y = (p + x)/s, N = (s + 1)/x.
*Proof.* On I_k, 0 ≤ (k+1)y − n < y. If x = (k+1)y − n divides n + y then x | (k+1)(n + y) − x = (k + 2)n; as x < y ≤ n and n = p
prime, x | k + 2. Conversely x | k + 2 gives gcd(x, k + 1) = 1 and x | (k + 2)n − ... i.e. x | (k+1)(n + y), hence x | n + y; and
y | n + x as n + x = (k + 1)y. N = (n + x + y)/(xy) = (s + 1)y/(xy). ∎
*Reading.* The continued-fraction (Farey) structure of y ↦ −p mod y is exactly piecewise linear, and linearising returns ET's
window form "s | p + x, x | s + 1" — the divisor-in-a-moving-class event (B2). No information is gained or lost.
