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

### §3 Props 3.3–3.5 — 3.3 SOUND for D = 1, GAP in the D ≥ 2 application (D5); 3.4 SOUND; 3.5 SOUND (definitional)

Prop 3.3 (core). Re-derived: if Q is non-torsion, Cheon–Hahn give for every large n a good prime 𝔭 with
ord(Q mod 𝔭) = n exactly; n ≡ 1 (mod m) gives infinitely many 𝔭 with m ∤ ord — contradiction. Torsion Q has
ord(Q mod 𝔭) = ord(Q) for almost all 𝔭, so m | ord(Q). Citation CHECKED against the paper (downloaded:
sources/r206/cheon-hahn-aa8832.pdf, Acta Arith. 88 (1999) 219–222, Theorem on p. 219: "E/K number field, P ∈ E(K)
of infinite order. Then for every sufficiently large n there exists a prime ℘ of good reduction so that the order of
P … modulo ℘ is n"). The document's "citation from memory, not re-checked" can be upgraded. Mazur (orders 1–10, 12)
and Kamienny–Kenku–Momose (D = 2: 1–16, 18) are quoted correctly (from memory; standard). Multiples of 4 in
Mazur's list: {4, 8, 12} ✓.
Application, D = 1 (B = 𝔸¹_t, the case behind "4cd ∈ {4, 8, 12}"): for almost every prime h pick a prime
p ≡ t₀ = −4c²d (mod h) (Dirichlet); then h | p + 4c²d and R_p ≡ R_{t₀} (mod h) (granted good reduction and
integrality of the family at t₀ mod h for almost all h, and E_{t₀} non-singular — a hidden hypothesis: if t₀ is a
bad fibre the argument says nothing), so 4cd | ord(R_{t₀} mod h) for almost all h, and Prop 3.3 applies. SOUND.
Application, D ≥ 2: GAP (D5).
Prop 3.3 Scope (b): "[F : ℚ] ≫ φ(N)/log log N (Silverberg; Clark–Pollack)". The known CM bounds are stronger
(Silverberg / Prasad–Yogananda: φ(N) ≪ w(O)·[F : ℚ]; Clark–Pollack: max CM torsion over degree D is ≍ D log log D),
so the stated inequality is true but loose; not checked against sources (not in sources/). MINOR, no repair needed
beyond "from memory".

Prop 3.4. (a) Re-derived: int C is open and conjugation-stable; it contains gU and hence the whole preimage of the
class of gU in Gal(L_U/ℚ); L_U is unramified outside the finite set, so finite Chebotarev gives natural density
≥ 1/[L_U : ℚ] for primes with Frob in that class. C closed with empty interior means C = ∂C, so Jordan-measurable ⇒
μ(C) = 0. The R-O207 finite-ramification repair is necessary and sufficient for (a). (b) Re-derived: a conjugacy
class maps to a point of the infinite abelian quotient, so is Haar-null; G is second countable (L/ℚ countable), so
μ(K_i V) ↓ 0 along a countable neighbourhood basis; ∪ K_i V_i is open and conjugation-stable; C is its complement.
Note (b) does not need finite ramification. The measure-theoretic statement is correct as written. The
anticyclotomic claim (ii) is correct (a reflection in ℤ_ℓ ⋊ {±1} has order 2, so inert h has residue degree 2 in
K^{ac}/ℚ, i.e. splits completely in K^{ac}/K) and well known. SOUND.

Prop 3.5. With "forcing by an identity" DEFINED as U_N(α_{t₀}, β_{t₀}) = 0 and U_n ≠ 0 for n < N, the conclusion is
immediate: α_{t₀}/β_{t₀} (needs Q(t₀) ≠ 0 — implicit, MINOR) is a primitive N-th root of unity in a field of degree
≤ D, so φ(N) ≤ D; D = 2 gives N ∈ {1, 2, 3, 4, 6}, and 4 | N gives N = 4. SOUND, but the label PROVED covers only
this definitional statement; the claim that every deterministic coupling of primitive divisors to the shot is
either this or a lottery is (correctly) labelled Assessment.

### §4.1 (3361 unique without prime-modulus Type II certificate) — SOUND, independently REPRODUCED and EXTENDED to 10⁸

Definition used (checked against the text and FMS Lemma 1.1): a Type II solution 4/p = 1/x + 1/(py′) + 1/(pz′),
p ∤ x, is a certificate of modulus h = 4y′ − 1 for the ordering (y′, z′); "prime-modulus certificate" = some
solution and some ordering with 4y′ − 1 prime. Same definition in my code.
From scratch (`scripts/review_tf_primemod.c`; stage 1 = sieve on the (c, d)-form h | p + 4c²d, 4cd | h + 1 — not the
author's c/j-form; stage 2 = direct enumeration of ALL Type II solutions over x ∈ [⌈(p+1)/4⌉, (p−1)/2] (includes
x = (p+1)/4, the case the author's first version skipped) and y′ ∈ (x/e, 2x/e], deterministic 64-bit Miller–Rabin):
* validation `check 20000`: for all 2260 primes 5 ≤ p ≤ 2·10⁴, direct enumeration vs sieve with the FULL range
  H0 = (P+1)(P+5)/4: 0 mismatches; only 3361 lacks a prime-modulus certificate.
* `run 2·10⁶ 10⁵`, `run 10⁷ 10⁵`, `run 10⁸ 10⁵ 40`: after stage 1 with h ≤ 10⁵ the ONLY unmarked prime ≤ 10⁸ is 3361;
  stage 2 confirms it has none. Spot check: the 40 largest marked primes below 10⁸ re-enumerated directly: all have
  a prime-modulus certificate. So the claim holds to 10⁸ (author: 10⁷). Runtime: 18 s.
* `list 3361`: exactly 2 unordered solutions, (x, y′, z′) = (850, 25, 170) and (841, 290, 8410), moduli
  {99, 679} and {1159, 33639} — exactly the author's list. Factorisations 3²·11, 7·97, 19·61, 3·11213 confirmed.
* torsion-side bullet: with h ≤ 20000 only 3361 is unmarked among the 78 496 primes 5 ≤ p ≤ 10⁶ (matches); up to
  10⁸ eleven primes need h > 20000 (e.g. 89802703, 93896401), all but 3361 have one.

### Props 4.2 / 4.3 — mathematically SOUND; EVIDENCE REPRODUCED; significance OVERCLAIMED (D7, MAJOR)

Re-derived. 4.2(a): |a| = 4c²d − 1 ≤ 2√p, p ∤ a, so Deuring–Waterhouse gives E/F_p with #E(F_p) = p + 4c²d; any
finite abelian group has subgroups of every order dividing its order; Lemma 1.1 on the (c, d)-line accepts ANY
h ≡ −1 (mod 4cd) dividing p + 4c²d. (b): same with a = 1 − c, c = 1 the supersingular case (p ≥ 5). 4.3: the cofactor
of h in 4dp + 1 is ≡ −1 (mod 4d), the smaller one h₀ ≤ √(4dp+1), c = (h₀+1)/(4d) ≤ (√(4p+1)+1)/4 (much smaller
than the stated 2√p + 1 — the window is not tight, only sufficient); h₀ | 4dp + 1 ⟺ h₀ | p + c. Correct.
From scratch (`scripts/review_tf_hasse.c`, written as pure divisor tests, no curves):
* primes 5 ≤ p ≤ 10⁷ (664 577): (a) fails only at 193; (b) fails at exactly the 23 primes listed (7 … 8813281,
  identical list); never both. Odd squares ≤ 10⁷ (1580): neither (a) nor (b) ever holds. (author: to 10⁸; I stopped
  at 10⁷, 3.3 s, more than the requested 10⁶.)
* Prop 4.3: (iii) [d ≤ (p+1)/3, any size] vs (b) [window] agree on all 2260 primes 5 ≤ p ≤ 2·10⁴.
Answer to the brief's question: YES — Prop 4.2 is literally a restatement. (b) ⟺ "for some c ≤ 2√p + 1, p + c has
a divisor ≡ −1 (mod 4c)"; (a) ⟺ "for some 4c²d ≤ 2√p + 1, p + 4c²d has a divisor ≡ −1 (mod 4cd)". The elliptic
curve enters only through its order (Deuring–Waterhouse is used solely to have SOME group of order p + 1 − a, and
the cyclic group ℤ/(p + 1 − a) would do equally well); no group structure, Frobenius, endomorphism ring or isogeny
datum is used, and my check reproduces the EVIDENCE without any curve. See D7.

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

D5 (MAJOR → GAP, §3 Prop 3.3 "Application" for D ≥ 2). For a family over B with [ℚ(B) : ℚ(t)] = D ≥ 2, a fixed
b₀ over t₀ = −4c²d only inherits the hypothesis at those primes 𝔥 of ℚ(b₀) that are the reduction of SOME b over a
prime p (essentially: degree-1 primes of ℚ(b₀), via Hensel lifting of b₀ mod 𝔥 into the fibre over p), not at all but
finitely many 𝔥 ("for a suitable b₀" — b₀ depends on 𝔥). Prop 3.3's hypothesis "for all but finitely many 𝔥" is then
not met, and Cheon–Hahn primitive divisors are not known to be of degree 1. So "m ≤ B(D)" for D ≥ 2 (and the KKM
"m ≤ 18" line) is not proved by the argument given. Repair options: (i) restrict the proved application to D = 1
(which is all that the headline "4cd ∈ {4, 8, 12}" uses) and mark D ≥ 2 CONDITIONAL/Assessment; or (ii) strengthen
Prop 3.3 to "m | ord(Q mod 𝔥) for all degree-1 primes 𝔥 outside a finite set" — this needs a different argument
(e.g. an ℓ-adic Kummer/Chebotarev density argument for ℓ | m showing that the primes with v_ℓ(ord(Q mod 𝔥)) <
v_ℓ(m) have positive density among degree-1 primes when Q is non-torsion; true in many cases but not proved here).
Also state explicitly the hidden hypothesis that E_{b₀} is non-singular and R_{b₀} defined (t₀ not a bad fibre).

D6 (MINOR, §4.1 bullet 1). "679 and 1159 have a prime factor ≡ 1 (mod 4)" — so does 33639 = 3·11213
(11213 ≡ 1 mod 4); only 99 = 3²·11 is built from primes ≡ 3 (mod 4). Repair: "three of the four moduli (all but 99)
have a prime factor ≡ 1 (mod 4)".

D7 (MAJOR, overclaimed significance: §4 Prop 4.2 header "PROVED, Deuring–Waterhouse", the bold sentence "ES(p) is
witnessed by an elliptic curve over F_p itself", §6.1, §6.6, AGENT_REPORT SHARP 3 "Hasse-window dictionary at p
itself"). The dictionary is a relabelling of the integer statement "p + c (resp. p + 4c²d) has a divisor
≡ −1 (mod 4c) (resp. mod 4cd)" — the curve is used only as a container of order p + 1 − a, and "has a subgroup of order
h" is equivalent to h | p + 1 − a for ANY finite abelian group. Nothing about E (cyclicity, End(E), isogeny class,
Frobenius) is used, so "witnessed by an elliptic curve" carries no information beyond FMS Lemma 1.1 restricted to
the windows; the EVIDENCE (193; the 23 j = 1 failures) is a divisor statement (reproduced here with no curves). The
genuinely new mathematical content is Prop 4.3 (window costs nothing on the j = 1 face — divisor pairing) and the
numerical fact "(a) or (b) holds for every prime ≤ 10⁸" — both pure divisor statements. Repair: retitle Prop 4.2 as
"(restatement) ES tickets as point counts", say explicitly that only #E is used and ℤ/(p + 1 − a) would serve; move the
"natural home for the (J)35 isogeny-graph line" remark to Assessment/Spark (it is a spark, not a finding: making the
curve matter would need e.g. a statement about the E-structure (Lenstra's End-module) of the h-part, which the
document does not have); remove "Hasse-window dictionary" from SHARP in the agent report or relabel it
"EVIDENCE (divisor statement), curve language optional".
