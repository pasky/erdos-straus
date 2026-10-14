# s4_three_bits_meta — what "positivity-blind" means, made precise: one real component, three local bits, two relaxations (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md. Words w = (t, u, v) ∈ ℤ³ with t u v − u − v = n (X_n),
A = tu − 1, B = tv − 1, so AB = tn + 1 and A ≡ B ≡ −1 (mod t); χ(w) = (−A/n) (Jacobi); path form
Q_w = v x² + t y² + u z² − 2xy − 2yz (det n); "certificate" = 2-adic five-slice condition 4 | A, B, t, u or v.

## Idea
Goal (1) of O218: state exactly which arguments are "positivity-blind" and why each fails. The campaign has the
ingredients scattered ((J)13/(J)33 ε_∞ = −1, (J)42 §3 signed friezes, (J)45 Maslov/c_∞). Here they are put in one
frame with two small new lemmas (L1, L2) and a new negative observation (P3): **dropping positivity in the n-adic
form keeps T1 but does NOT make the problem easier — it is still a finite lottery of the same kind.** So positivity
is the T1 anchor, not the bottleneck.

## Statements
**L1 (PROVED, Sylvester).** For n > 0 and an integral point of X_n with t, u, v ≠ 0: Q_w is positive definite ⟺
t, u, v > 0; otherwise Q_w is indefinite (det n > 0 excludes negative definite).
*Proof.* Leading minors of [[v,−1,0],[−1,t,−1],[0,−1,u]] are v, tv − 1, tuv − u − v = n. If t, u, v ≥ 1 then tv > 1
unless t = v = 1, which gives n = −1. Conversely v > 0, tv > 1 force t > 0 and u(tv − 1) = n + v > 0. ∎
Hence, with β = [C₀(Q_w)] the CHI_FLIP Prop 1.6 Azumaya class: **inv_∞ β = ½ exactly on positive words, 0 on all
signed words** (C₀ of a ternary form is ramified at ∞ iff the form is definite).

**L2 (PROVED).** D := {(t,u,v) ∈ X_n(ℝ) : v > 0, tv > 1} is a connected component of X_n(ℝ) (n > 0), equal to the
positive orthant part and homeomorphic to ℝ²_{>0} via (u, v) ↦ t = (n + u + v)/(uv).
*Proof.* On X_n, tv = 1 forces n = −v < 0 when v > 0, and v → 0⁺ inside D forces t → ∞, so D is closed in X_n(ℝ);
it is open; on D, tv = 1 + (n + v)/u > 1 automatically, and u > 0 by L1's argument. ∎
So **ES-five(n) ⟺ X_n(ℤ) ∩ (D × Ω₂) ≠ ∅**, Ω₂ the 2-adic certificate region, and T1 at odd squares is a
Brauer–Manin obstruction whose real invariant is *non-constant on X_n(ℝ)*: ½ on the single component D, 0 elsewhere
(sharpening the wording of CHI_FLIP Prop 1.6, which says "positive integral points").

**Three bits.** For every w (signed or not) with gcd(A, n) = 1 the product formula reads ε_∞(w)·ε₂(w)·ε_n(w) = 1,
where ε_∞ = −1 ⟺ w positive (L1), ε₂ ↔ certificate, ε_n ↔ χ (TRANSPORT_LAW Thm 3.1 with r = 3; the ∞-factor is the
Maslov count). On D: certificate ⟺ χ = −1 (MODEL_SPECIFIC 3.1(a)). **For all words, signed included: certificate ⟺
χ·s_∞ = −1 with s_∞ = +1 iff w is positive** (CERTIFIED: every signed and positive word of every odd n ≤ 1001,
0 violations, `s4_signed_nadic.py`; it is the 2-adic cell law, which only sees w mod 8, plus L1).

**P3 (two relaxations; PROVED parts as marked).**
* (R₂) *signed, 2-adic form*: ∃ w ∈ X_n(ℤ), t u v ≠ 0, certificate. **No T1**: holds at every odd square (FRIEZE §3's
  explicit family; CERTIFIED here at all 15 odd squares ≤ 1001, script below). The bit that broke: ε_∞ = +1.
* (R_n) *signed, n-adic form*: ∃ w ∈ X_n(ℤ), t u v ≠ 0, χ(w) = −1. **Keeps T1 automatically** (Jacobi symbols mod an
  odd square are +1; PROVED). But:
  (a) it is a **finite search**: A ≡ B ≡ −1 (mod t), A, B ≠ −1 give |A|, |B| ≥ |t| − 1, so (|t| − 1)² ≤ |t|n + 1 and
      |t| ≤ n + 3 (PROVED);
  (b) **no forcing**: for every t, χ(A)χ(B) = (AB/n) = (tn + 1 / n) = 1, so the Jacobi symbol of the whole
      factorisation is always +1 and the sign must come from choosing a sub-product (B2/B4 shape) (PROVED; at the
      level of single primes q | tn + 1 one has χ(±q) = (−t/q) for n ≡ 1 (4) — a genus character of q whose product
      over the factorisation is trivial);
  (c) EVIDENCE: **(R_n) holds at every odd non-square n ≤ 10⁷, including n = 105, where ES-five fails**
      (`scripts/s4_sqpm.c`), always with |t| ≤ 18 (record at n = 4 884 441); the positive version (ES-five) needs
      t up to 231 already below 2·10⁶ (record n = 702 585) and fails at 105. At primes ≤ 1001: ≈ 75.5 signed
      χ = −1 words on average versus ≈ 33.7 positive ones.
  (d) no finite t-set suffices (CONDITIONAL on Schinzel's H): for t = ±1, ±2 the only words with tn + 1 = ±prime·(unit)
      are the trivial ones, χ = (−1/n) = +1 for n ≡ 1 (4); for |t| ≥ 3 a prime |tn + 1| (resp. 2·prime) has no
      factorisation with A, B ≢ … ≠ −1 except A or B = ±1, excluded or of the wrong class. So H gives infinitely many
      n ≡ 1 (8) where every |t| ≤ T fails (sketch; admissibility of the prime tuple to be checked per T).
  Mechanism of the quantitative gain: with A, B < 0 the factors a = |A|, b = |B| satisfy a ≡ b ≡ +1 (mod t) (the
  *wide/trivial* class), and for prime t ≡ 1 (4), n ≡ 1 (4), χ = (−t/a) = (−1/a): the c_∞-condition moves from
  "≡ −1 mod t" to "≡ −1 mod 4" — a fixed modulus. So positivity is what makes the c_∞ modulus grow with t.

## Literature
CHI_FLIP Thm 1.1 / Prop 1.6 ((J)33), TRANSPORT_LAW Thm 3.1 ((J)45), FRIEZE_ES §3 ((J)42), MODEL_SPECIFIC Thm 3.1
((J)32). Sylvester's criterion; C₀ of ternary forms (e.g. Voight, *Quaternion Algebras*, Ch. 22). The BM-with-real-
components phenomenon is standard (Skorobogatov, *Torsors and rational points*, §5.2).

## Barrier screen
* B5/T1: the meta-statement *is* the T1 analysis. Any argument whose output lands in a region R × U with R meeting a
  component other than D proves a statement true at odd squares when U ⊆ Ω₂ (R₂) — a positivity-blind argument.
  Concretely blind: centrally symmetric geometry of numbers (Minkowski, Siegel's lemma, Thue), pigeonhole differences
  (LONGSHOT_PIGEONHOLE), wide ray classes / even characters (y5_narrow_wide), strong approximation and real density
  arguments on X_n(ℝ) as a whole, finite-ring frieze theory (FRIEZE §3).
* B2: (R_n) shows the moving-modulus lottery is *independent of positivity*: it survives verbatim in the signed
  n-adic form, which is T1-bearing and finite (P3(a,b)).
* Harness: (R_n) for 8/n (eight-slices with χ) is not needed — P3 is about where the sign enters, not numerator data.

## Cheap numerics
`scripts/s4_signed_nadic.py N` (N = 2501: 15 s). Output N = 2501: primes 366/366 POS, CERT2, SGN_n; odd squares 24:
POS 0, CERT2 24, SGN_n 0; other 860: POS 859 (105 fails), SGN_n 860; positivity ≠ definiteness: 0; definite words
violating "certificate ⟺ (χ = −1 xor signed)": 0 (N = 1001 run).

## Assessment
The precise meta-statement: **positivity enters ES exactly as the single bit ε_∞ = −1 on the single real component D;
it converts the 2-adic certificate condition into the n-adic condition χ = −1, and nothing else.** Dropping it in the
2-adic form trivialises ES and loses T1; dropping it in the n-adic form keeps T1 and stays qualitatively the same
(finite, no forcing, a sub-product lottery, no finite t-set under H) but becomes quantitatively far easier (|t| ≤ 18
to 10⁷ versus 231 by 2·10⁶), because the c_∞-requirement then lives at the fixed modulus 4 instead of the moving
modulus t. **New CONJECTURE SQ_± (EVIDENCE to 10⁷): for odd n, χ is non-constant on the signed points of X_n iff n is
not a square** — the exception 105 of SQ₅ disappears. So "ES must use positivity archimedeanly" is true for T1, but a
positivity-respecting tool is not thereby a lottery-breaker: the lottery is n-adic. Label: L1, L2, P3(a,b) PROVED
(elementary); P3(c) EVIDENCE; the reading is an Assessment.
