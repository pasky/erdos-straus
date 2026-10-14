# R206 — hostile review of TORSION_FIRING.md (O207)

Reviewer: R206 (side-agent/review-torsion-firing). Reviewed: TORSION_FIRING.md as merged from
side-agent/torsion-firing (commit at merge time), AGENT_REPORT_O207.md, data/tf/. From-scratch scripts:
scripts/review_tf_*.{py,c}. Status: IN PROGRESS.

## Summary verdicts

(filled in claim by claim below)

## Claim-by-claim

### §1 Lemma 1.1, Prop 1.2 — SOUND (minor wording defects D1, D2)

Re-derived. Lemma 1.1(a): f(−x) = −f(x) and (−1/h) = −1 give 2 points per pair {±x}, x ≠ 0, total h + 1;
Weil pairing m | h − 1 and m² | h + 1 give m | 2; full 2-torsion iff −D is a square iff (D/h) = −1. (b): cubing is
a bijection when 3 ∤ h − 1; exactly one 2-torsion point, so m is odd and m | 2 forces m = 1. Prop 1.2(b): at
x = 2cd, x³ + pd·x = 2cd²(p + 4c²d); conversely x_T² ≡ −pd with x_T = 2cd gives d(p + 4c²d) ≡ 0. The
hypothesis h ∤ 2c in the forward direction is automatic once 4cd | h + 1 (2c ≤ (h + 1)/2 < h).

From scratch (`scripts/review_tf_sec1.py 1000 400`, 1m49s):
* Lemma 1.1 by brute force (point list + exponent = lcm of all point orders), primes h < 1000, D ∈ {±1, ±2, ±3,
  5, 6, −7, 10, 11}, B ∈ {±1, 2, −3, 5, 7, 11}, h = 3 included where D ≢ 0: 1552 cases, 0 failures.
* Prop 1.2 END-TO-END against actual Type II solutions (not against the box): for every odd prime p ≤ 400, the set
  of PRIME h = 4y′ − 1 (both orderings) over all solutions 4/p = 1/x + 1/(py′) + 1/(pz′) found by brute force over
  (x, y′) equals the set of primes h ≡ 3 (4), h ≤ (p+1)(p+5)/4, for which some d with h ∤ d has a 2-torsion point
  (x_T, 0) ≠ (0, 0) of y² = x³ + pd·x with x_T ∈ [1, h), 2d | x_T, 2x_T | h + 1 (x_T scanned over ALL multiples
  of 2d, not via divisors), and equals the (a)-form set {h : ∃ cd | (h+1)/4, h | p + 4c²d}: 0 mismatches.
* Prop 5.1 / T1: odd squares 9 ≤ m² ≤ 625, all h ≤ (n+1)(n+5)/4: 0 firing pairs.

### §2 Prop 2.1, Cor 2.2, Prop 2.3 — SOUND (D4: Prop 2.3 is a triviality; edge cases fine)

Prop 2.1 re-derived: at good supersingular h ≥ 5, Hasse + h | a_h give a_h = 0; char. poly x² + h has
discriminant −4h ∈ ℤ_ℓ^* for odd ℓ ≠ h, so F mod ℓ is non-scalar, has a cyclic vector v, and in the basis (v, Fv)
(Cayley–Hamilton F² = −h) F is [[0, −h], [1, 0]]. Edge cases: h = 2, 3 are excluded by hypothesis (there a
supersingular curve can have a_h = ±h, ±√(2h)…; the same argument would give the companion matrix of x² − a_h x + h,
so nothing breaks, it just isn't x² + h). j = 0, 1728 play no role (the proof never uses End(E)). ℓ = 2 correctly
excluded (F ≡ I mod 2 iff E[2] ⊂ E(F_h)). Consistency check: F² = −h·I, so E(F_{h²}) ≅ (ℤ/(h + 1))² for every
supersingular E with a_h = 0, at all ℓ including 2 — matches Lemma 1.1 data. Cor 2.2 is correct after the R-O207
repair (h-part zero, 2-adic part separate).

Prop 2.3: correct, but its content is that det ρ_{E,h}(Frob_p) = p, which holds for EVERY E/ℚ with good reduction
at p (Weil pairing / cyclotomic determinant), CM or not, p ≡ 1 (4) or not; and "firing depends only on p mod h" is
the definition of Fire_II (FMS Thm 3.1). The CM/Deuring input (Frob_p = uπ_p on ℤ[i]/h) is only used to name the
"torus part" π_p/π̄_p, which is then shown to be irrelevant. See D4.

### Thm 3.1 / Cor 3.2 — Thm 3.1 SOUND; Cor 3.2 SOUND as stated; its use in §3 Assessment / §6.3 OVERCLAIMS (D3, MAJOR)

Exponent arithmetic re-derived: g = gcd(h^s + 1, h^t − 1); ord_g(h) divides t and 2s, hence gcd(t, 2s) = gcd(t, s)
(t odd), hence s, so h^s ≡ ±1 both, g | 2 (and g = 2 for h odd). Image of a hom from an exponent-(h^s+1) group to
the cyclic group F_{h^t}^* has order | g. The examples are right: for a_h = 0, a_{h^s} = (i√h)^s + (−i√h)^s = 0
for odd s, so #E(F_{h^s}) = h^s + 1. From scratch (`scripts/review_tf_thm31.py`): gcd = 2 for all odd h < 400,
s ≤ 8, odd t ≤ 9 (0 exceptions; t even fails, e.g. h = 7, t = 2: gcd 8, so "t odd" is necessary). Also checked
directly in F_{h²} (h ≡ 3 mod 4, h < 200): μ_{h+1} ∩ F_h^* = {±1} and every coset σ·μ_{h+1}, σ ∈ F_{h²}^*, meets
F_h^* in 0 or 2 points — so the factor-2 bound per seed element survives even for seeds outside F_h^*
(a point the document does not state but that closes the obvious escape via t = 2).

Precise scope of "amplifies by ≤ 2": Cor 3.2 proves |{x ∈ F_h^* : x ∈ ψ(Γ_h)·S}| ≤ 2|S| for any HOMOMORPHISM ψ
from a group of exponent dividing h^s + 1. It says nothing about (i) non-homomorphic transport (coordinates — the
document admits this), and (ii) groups of points at ORDINARY reduction, where #E(F_h) = h + 1 − a_h and
gcd(#E(F_h), h − 1) can be large (from scratch: y² = x³ + x + 1 at h = 127 has #E = 126 = h − 1; at h = 163,
gcd = 27). The §3 Assessment ("The only bridges … are therefore non-homomorphic") and §6.3 ("points live in the
(f + 1)-world"; "the precise reason the task's 'finitely generated group of points reduced mod f' cannot play the
role of ⟨s⟩") drop the supersingular hypothesis. See D3.

## Defects

D1 (MINOR, §1 Lemma 1.1 vs Prop 1.2). Lemma 1.1 is stated for h ≥ 5, but Prop 1.2 (and Prop 5.1) quantify over
all primes h ≡ 3 (mod 4), including h = 3 (k = 1, c = d = 1: h | p + 4). The statements are true at h = 3 (checked:
y² = x³ + x over F_3 is ℤ/4, y² = x³ − x is (ℤ/2)²; the proof of (a) works verbatim for h = 3). Repair: state
Lemma 1.1(a) for h ≥ 3 (keep h ≥ 5 only for (b), where h ∤ 6B excludes 2, 3 anyway).

D2 (MINOR, §1 "Reading"). "the firing datum c is the (reduced) x-coordinate of a 2-torsion point" — the
x-coordinate is x_T = 2cd, not c (c = x_T/(2d)). Repair: "c = x_T/(2d), where x_T is …". Also worth saying
explicitly that Prop 1.2(b) is a tautological reformulation (the non-zero 2-torsion x-coordinates of
y² = x³ + pd·x are just the square roots of −pd, and x_T = 2cd, x_T² ≡ −pd IS h | p + 4c²d); the curve adds no
structure beyond the quadratic-character sign (pd/h) = −1 (which is what Prop 5.1 then uses). The Reading half-says
this ("This is the box again"); the verdict §6.1 lists it as an "exact dictionary" without that caveat.


D3 (MAJOR, §3 "Where the hypothesis bites" + §6.3 + AGENT_REPORT SHARP 1). Two overclaims about Thm 3.1/Cor 3.2.
(a) Dropped hypothesis. Thm 3.1 needs exponent | h^s + 1, i.e. SUPERSINGULAR (a_{h^s} = 0) reduction or the
non-split torus. A finitely generated group of points of a curve that is ORDINARY at h lands in E(F_h) of order
h + 1 − a_h, and Hom(E(F_h), F_h^*) can be large (y² = x³ + x + 1: #E(F_127) = 126 = h − 1; gcd(#E(F_163), 162) = 27;
`scripts/review_tf_thm31.py`). For a Type II modulus h ≡ 3 (mod 4) the curve E_0 (CM by ℤ[i]) is supersingular, but
nothing in "replace ⟨s⟩ by a group of points" forces the curve to be E_0 or supersingular at h. "points live in the
(f + 1)-world" and "the only bridges … are non-homomorphic" are true only for supersingular-at-h data.
(b) Wrong attribution of the bound. The last sentence of Cor 3.2 ("a sufficient rule … has ≤ |Box(k)| ≤ τ₃(k)
elements") does not use Thm 3.1 at all: for ES over ℚ at a fixed h, ANY sufficient rule (homomorphic or not,
supersingular or ordinary) fires on a subset of −Box(k), by FMS Thm 3.1. What Thm 3.1 adds is only that the
homomorphic image ψ(Γ_h) is ⊆ {±1}; for ordinary data ψ(Γ_h) can be large but then ψ(Γ_h)·S ⊆ Box(k) is simply
violated, with the same conclusion. So "the precise reason Γ cannot play the role of ⟨s⟩" is not orthogonality; it
is that ES over ℚ has no mute place (FF_MUTE amplifies by CHANGING the equation — S-unit denominators s^j — so that
the firing set at f becomes the coset −A⟨s²⟩, which is not a subset of a box). Thm 3.1 is a correct and clean
statement about which group the supersingular data can reach, but not a no-go for the GL₂ mute analogue unless that
analogue is first defined (what modified equation would ψ(Γ) enter?).
Repair: in Cor 3.2 and §6.3 add "for Γ_h inside a group of exponent dividing h^s + 1 (supersingular reduction at h,
or the non-split torus)"; replace "This is the precise reason …" by "For supersingular-at-h data this is why …; for
ES over ℚ itself, any sufficient rule at h is ⊆ −Box(k) regardless (FMS Thm 3.1), and a genuine GL₂ mute analogue
would first need a modified equation, not formulated here". Downgrade SHARP 1 in the agent report accordingly.

D4 (MINOR, §2 Prop 2.3 and §6.1). "per-modulus, firing reads only det = N(π_p) of the CM Frobenius of p on E_0[h]"
is listed among the PROVED dictionaries, but det ρ_{E,h}(Frob_p) = p for every E/ℚ (Weil pairing), and firing at h is
by definition a function of p mod h. The CM structure (π_p, the torus part) adds nothing. Repair: label Prop 2.3 as a
remark/restatement ("firing is a function of det = p; the CM torus part π_p/π̄_p is invisible") and drop it from the
§6.1 list of dictionaries, or state that it holds for every E.
