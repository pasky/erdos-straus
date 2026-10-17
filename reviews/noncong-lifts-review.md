# R267 — hostile review of O257 NONCONG_LIFTS.md (non-congruential lifts, numerator-model laboratory)

**Repairs applied** (author quiet): R267 repair notes in NONCONG_LIFTS.md (D-M1 at §1 after Thm 1.2, §2.4 ×4, §4.1, §5 Reading; D1, D2, D3, D4, D5, D6, D7) and AGENT_REPORT_O257.md (SHARP scope). Author text otherwise untouched.

Reviewer branch `side-agent/review-noncong-lifts`, merged `side-agent/noncong-lifts` at 3b74594d.
From-scratch code: `scripts/review_r267_*.{c,py}` (none of the author's scripts reused).
ES is OPEN; nothing reviewed proves ES or an infinite case of it.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Thm 2.6 (a), (b) (fixed-slice classes, all a, b, c; d irrelevant) | **SOUND** (re-derived; numerics to a ≤ b ≤ 1000) — D1–D3 minor |
| Thm 2.6 (c) "no level through ℓ ≡ ±3 (8) complete" | SOUND for the defined (slice) notion; ℓ ∤ k needed (D1) |
| Thm 2.6 *Reading* / report SHARP 1 ("4 vs every k ≥ 8 separation") | **GAP → SOUND-AFTER-REPAIRS** (D-M1: fails for ET's non-slice polynomial families: k = 8 covers x_{3,2}, x_{5,2}; k = 4 covers x_{11,2}) |
| Complete-level dictionary (k = 4 rule ≤ 6000, "if" PROVED; k = 8, 12 none ≤ 400k; deficits) | **SOUND** (reproduced exactly) — slice notion; k = 4 L = 12 is complete with families (D-M1) |
| Mordell-class primes are squares mod every 7-smooth level | SOUND (trivial) |
| Def 1.1 | SOUND-AFTER-REPAIRS (dichotomy not exhaustive, D-M1(5)) |
| Thm 1.2 (with gcd(p, M) = 1) | SOUND (classical in (ii)) |
| Prop 1.3 | SOUND (Schinzel; not re-read by me); D5 on the NEAR_SQUARE sentence |
| Prop 1.4 | SOUND |
| §2.1 exact E_k | SOUND — all k = 7…25 reproduced to 10⁷ with own solver |
| §2.3 margin | SOUND as EVIDENCE; quoted means ≈ 4 % high, unreproducible (D6) |
| Lemma 3.1 | SOUND |
| Computation 3.2 (fixtures; 0/1347 total; 30 % transport) | SOUND — all 16 fixture entries reproduced; aggregate reproduced to 3·10⁴ (D7) |
| §4.1 model screen | SOUND (entries reproduced) |
| §4.2 size information | SOUND as descriptive EVIDENCE; report overclaims (D8) |
| Resources | D9 (5-process burst) |

No FATAL. One MAJOR (D-M1, scope of the headline reading), nine MINOR.

## Claim-by-claim

### Thm 2.6 (§5) — x_{ℓ,2} lies in no witness class for 4 | k ≥ 8; k = 4 iff ℓ ∈ {3, 5}

**Re-derivation (independent, line by line).** Membership of the profinite point in the class of slice (θ, a, b, c)
depends only on the slice (d plays no role), and with m = v_ℓ(ab), H′ = kab/ℓ^m (ℓ ∤ k is needed here) it reads
II: e ≡ −1 (H′), e ≡ −2 (ℓ^m); I: e ≡ −1 (H′), 2e ≡ −1 (ℓ^m). So "no class" is genuinely over ALL slices
(unbounded a, b, c; d irrelevant). I re-derived every branch:
* Case 0: e ≥ kab − 1 > a + b ≥ e for k ≥ 4. ✓
* Case A, II: a + 2c = Lg, c(e+2) = L(g+b₀), Lh = e + 2 ≡ 1 (mod kab₀), Lh ≥ 3 ⇒ Lh ≥ kab₀ + 1; Lh = 2L(g+b₀)/(Lg−a).
  a ≤ Lg/2 ⇒ kb₀ + 1 ≤ 4 + 4b₀/g ⇒ b₀(k − 4/g) ≤ 3 (uses a ≥ 1); a > Lg/2 ⇒ (k/2)gb₀ < g + b₀, false for k ≥ 4. ✓
* Case A, I: 2a + c = Lg, 2e + 1 = Lh ≡ −1 (mod 2kab₀); 2a ≤ Lg/2 ⇒ 2kab₀ − 1 ≤ 2 + 4b₀ (false k ≥ 4);
  2a > Lg/2 ⇒ L(g+2b₀) > (k/2)Lgb₀ − 1, and since both sides are integers (k even!) g + 2b₀ ≥ (k/2)gb₀, false for
  k ≥ 8 (4gb₀ − g − 2b₀ ≥ 2b₀ − 1 > 0). ✓ (Note: the integrality step uses k even; see D3.)
* Case B: ℓ ∤ e forces ℓ^i | c; c₀e = a₀ + ℓ^n b₀; n = 0 is Case 0; n ≥ 1 is Case A for (a₀, b₀, ℓ^n, c₀) (all congruences
  used are implied), plus ℓ^{2i} | h from the full ℓ^{2i+n} congruence. ✓
* (b) k = 4: I re-ran every sub-branch (II: a = 1; g = 1 gives h(2c−1) ≤ 3 → (L,h,c) = (3,3,1), (5,1,2), h = 1 at c = 1
  gives b₀ = 0 (silently discarded in the text — fine); g ≥ 2 forces b₀ = 1, g(L−2) ≤ 3, L = 3, g = 3, fails mod 4.
  I: g = 1 ⇒ c = 1 ⇒ L + 1 = b₀(4Lt − 4t − 2L) ⇒ (L, b₀) ∈ {(3,2), (5,1)}; g = 2, b₀ = 1 impossible. Case B: h ∈ {3,1} (II),
  {5,3} (I), ℓ^{2i} ∤ h.) All ✓. The representative x = 17 checks.
* (c) x_{ℓ,2} mod L is a non-square unit class iff (2/ℓ) = −1 (other components are 1); a covering class of modulus
  H | L would contain the point. ✓ 4 | k is used only through the meaning of "complete"/T1, not in (a)/(b).

**From-scratch numerics** (`scripts/review_r267_x2.c`; two independent membership tests per slice — CRT-component
congruences and an explicit CRT representative x mod H with 128-bit products — 0 disagreements):
* a ≤ b ≤ 300, **every** k ∈ {4, 5, …, 32} (not only 4 | k), every odd prime ℓ < 60: for ℓ ∤ k the only hits are
  k = 4: (II/I, 1, 6, c = 1, e = 7) at ℓ = 3; (II, 1, 5, c = 2, e = 3), (I, 2, 5, c = 1, e = 7) at ℓ = 5 — exactly (b) —
  and k = 5: (II/I, 1, 3, c = 1, e = 4) at ℓ = 3. No hit at all for ℓ ∤ k, 6 ≤ k ≤ 32.
* ℓ | k (outside the theorem's hypotheses) there ARE hits: e.g. k = 12, ℓ = 3: (1, 6, e = 7), H = 72. So the hypothesis
  ℓ ∤ k is necessary, not cosmetic (see D1).
* a ≤ b ≤ 1000 for k = 4 and k = 8, ℓ < 60: see addendum below.

**Verdict: SOUND.** The proof is correct and complete; the mechanism is indeed the size inequality (Case A,
a ≤ Lg/2 branch for II; Case A, 2a > Lg/2 for I — the latter needs k ≥ 8 *and* k even, not b₀(k − 4/g) ≤ 3).

### Complete-level dictionary (§2.4) and "every Mordell-class prime is a square mod every 7-smooth level"

**Definition used (made precise).** k | L; L is *complete* iff every unit class r mod L that is not a square mod L
lies in some witness class with H = kab | L, i.e. r ≡ −e (mod H) (II) or re ≡ −1 (mod H) (I), e = (a + b)/c, c | a + b.
(d is irrelevant: every prime in such a class gives d = N/H ≥ 1.) This is what the text says; fine.

**From-scratch recomputation** (`scripts/review_r267_complete.py`, own covering enumeration over all (a, b, c) with
kab | L, own square test, numpy masks; T1 asserted: 0 covered square unit classes at every level):
* k = 4, all L = 4m ≤ 1600: 59 complete levels, **all 7-smooth** ✓.
* k = 4, all 7-smooth L ≤ 6000: complete ⟺ (3 | L ⟹ 8 | L) ∧ (7 | L ⟹ 24 | L), **0 rule violations** ✓
  (840 complete — Mordell).
* k = 8 (L ≤ 3200) and k = 12 (L ≤ 4800): **no complete level** ✓.
* Deficits at L = 105k / 210k: k = 8: 96/52; 12: 178/213; 16: 276/322; 20: 346/460; 24: 464/699 — **identical** to the text.

**"If" direction (PROVED claim).** Re-derived: for a rule-satisfying 7-smooth L put L₀ = 2^{min(v₂L,3)}·rad_odd(L); if
v₂(L) = 2 the rule forces 3, 7 ∤ L, so L₀ ∈ {4, 20} with v₂(L₀) = v₂(L); otherwise 8 | L₀. In both cases a unit is a
square mod L iff it is a square mod L₀ (odd ℓ: square mod ℓ^v ⟺ mod ℓ; 2: mod 4 when v₂ = 2 on both sides, ≡ 1 (8)
when v ≥ 3), and covering classes mod H | L₀ pull back. The base levels satisfying the rule are complete by
computation (my run includes all 16 levels 4s, 8s, s | 105). **SOUND.**

**Mordell-class squareness.** 𝓜 = {1, 121, 169, 289, 361, 529} mod 840 = squares of 1, 11, 13, 17, 19, 23; p ∈ 𝓜 ⟹
p ≡ 1 (8) and (p/3) = (p/5) = (p/7) = 1 ⟹ p is a square mod every 2^a3^b5^c7^d by Hensel. Trivially **SOUND**.

**Verdict: SOUND (CERTIFIED parts reproduced; "if" PROVED).** Defect D4 (logic of "k = 8 has none at all, because
already ℓ = 3, 5, 7 carry uncovered points").

### §1: Def 1.1, Thm 1.2, Prop 1.3, Prop 1.4

* **Def 1.1** — coherent; "with the same w′" makes the level a property of the pair (rule, w′). Fine.
* **Thm 1.2 (with gcd(p, M) = 1).** Re-derived. (i) The Dirichlet step is correct: progression p + M(t₀ + s·rad(kab)),
  first term coprime to the difference (primes of M: gcd(p, M) = 1; ℓ | kab, ℓ ∤ M: choice of t_ℓ). The parenthetical
  "ℓ = p does not divide kab by ET normalisation" is unnecessary (if p | kab the bad class for ℓ = p is t ≡ 0, which
  is excluded anyway) — harmless. Type I uses gcd(e, kab) = 1 from kabd = pe + 1 ✓. (ii) p ≡ s² (mod M), H | M, H even ⟹ s odd
  ⟹ the odd square s² lies in the witness class; the identity (abd, acdn, bcdn) / (abdn, acd, bcd) is valid for every n,
  so this is a parametric solution at n = s² — excluded by the local square-class obstruction. My
  `review_r267_complete.py` asserts exactly this local statement (no square unit class covered) at every level
  ≤ 6000 (k = 4), ≤ 3200 (k = 8), ≤ 4800 (k = 12): 0 violations. ET Prop 1.6 checked in the PDF ("For any odd perfect
  square n, f_I(n) = f_II(n) = 0", proof via the point equations, i.e. slice-local) ✓. **SOUND** (classical in
  substance, as the text now says).
* **Prop 1.3.** The k = 5 counterexample checks (1/(t+1) + 2/(2n(t+1)) = (n+1)/(n(t+1)) = 5/n for n = 5t + 4; 4 ≡ 2²
  mod 5). "Valid for infinitely many t ⟹ identity in ℚ(t)" ✓. Schinzel 2000 not accessible to me (no PDF in
  sources/); I rely on the O223 citation audit (DISCOVERIES (J)49 SHARP 2, (J)55). **SOUND (classical; Schinzel's).**
  The NEAR_SQUARE sentence after it is garbled — D5.
* **Prop 1.4.** All four coefficient comparisons re-derived (II←II λ = α, e = αe′ − β; II←I λ = α/e′, e = α/e′ − β;
  I←II e = 1, αe′ − β = 1; I←I e(α − βe′) = e′, λ = αe/e′). The α = 1 list is complete (I←I with δ ≠ 0 has no solution:
  δ > 0 makes 1 − δe′ ≤ 0, δ < 0 makes e < 1). Examples check: q = 37 (II, 1, 5, 2, d = 2, e′ = 3, N = 40) ↦ p = 13
  (I, same slice, e = 3, 13·3 + 1 = 40); q = 23 (II, 1, 6, 7, 1), p = 17, e = 7: (1, 6, 1) works, (1, 13, 2) needs 52 | 24.
  The "reselecting ⟺ (θ, e) ∈ Spec(p)" statement is a tautology once stated (fine, it is labelled algebra).
  **SOUND.**

### §2.1–2.3 laboratory (exact E_k, margin)

* **E_k (CERTIFIED claim).** Own solver `scripts/review_r267_ek.c` (divisor criterion on B², written from scratch,
  validated against a naive (x, y, z) search for every prime p ≤ 3000, k ∈ {4, 5, 8, 9, 12, 13}: 0 mismatches). Run for
  **every k = 7, …, 25 to 10⁷** and compared with `logs/z28_Ek_primes_1e8.txt` (after dropping 2 and p | k, cut at 10⁷)
  by `scripts/review_r267_ek_compare.py`: **all 19 lists identical**; last exceptions 241, 12241, 83449, 2763601, 620929
  (k = 8, 12, 16, 20, 24) and 19, 281, 2081, 14051, 62731 (k = 9, 13, 17, 21, 25) ✓. PW Table 1 (sources/pw.txt, k = 15
  row ends …, 12601, 16831, 20521) agrees. k = 4, 5: no exception ≤ 3000 (sanity). The 10⁷ → 10⁸ extension not rerun.
  **SOUND** (known data, correctly labelled as such).
* **§2.2 profile** — EVIDENCE, descriptive; not rechecked beyond the factorisation 2763601 − 1 = 2⁴·3·5²·7²·47 ✓.
* **§2.3 margin.** Own counter `scripts/review_r267_counts.c` (f_k(p) = #{x ≤ y ≤ z}), primes in [16000, 48000):
  mean f/log³p = 0.1535, 0.0692, 0.0412, 0.0288, 0.0243, 0.0181 (k = 4, …, 24); min f = 23, 4, 1, 0, 0, 0; Mordell
  primes (88): mean 0.0529 (k = 4, ratio 2.9), 0.0190 (k = 8, ratio 3.6), min 23 and 4. Minima and ratios ✓; the
  quoted means (0.159, 0.072, 0.043, 0.030, 0.025, 0.019) are uniformly ≈ 4 % higher than mine — and also higher
  than the author's own `z28_lab cnts 4 16000 48000` output, which gives 0.1535 under the obvious estimator (D6).
  Qualitatively **SOUND (EVIDENCE)**; the numbers need provenance.

### §3: Lemma 3.1 and Computation 3.2

* **Lemma 3.1.** Re-derived. One unstated point checked: q ∤ H′ for a witness at a prime q ∤ k (Type I: qe + 1 = kabd;
  Type II: q | a ⟹ q | e ⟹ q | b ⟹ q + e = kabd ≥ kq(a+b)/2 > q + e, contradiction), so "non-square mod ℓ^v" is a
  statement about a unit and the Legendre/mod-8 transfer is legitimate. **SOUND.**
* **Computation 3.2.** Own enumerator `scripts/review_r267_matched.py` (complete solution lists via the B²-divisor
  criterion, ET representation recovered from each solution, own general squareness test, det ⟹ visible asserted).
  My raw counts are exactly twice the author's because I count (a, b) and (b, a) separately; halved, **all 16 fixture
  entries agree exactly** (97: 5/6/7, 16/20/21, 13/17/22, 9/14/18; 193: 10/18/22, 12/18/20, 8/13/18; 313: 6/6/7,
  3/6/8, 7/16/22, 8/15/18; 3361: 3/22/29, 9/25/30, 6/19/30; 5209: 0/20/33, 4/19/30). The convention "(a, b) unordered"
  should be stated (D7).
  Aggregate: 273 Mordell primes ≤ 10⁵ and 1347 matched sources (W = 1000) ✓. Witness-level aggregate recomputed for the
  83 Mordell primes ≤ 3·10⁴ (413 sources, 21550 witnesses): visible 65.2 %, transporting/visible 29.6 %, **0 total
  sources, 0 sources with visibility sufficient** — same rates as the author's 10⁵ aggregate (64.6 %, 29.6 %, 0, 0).
  Not rerun to 10⁵ (Python cost). **SOUND (CERTIFIED for the fixtures; aggregate consistent).**
* The *Reading* "exactly as §2.4 predicts" overstates: §2.4 predicts that visibility is not sufficient, not the 30 %
  rate. Cosmetic.

### Scope test: what Thm 2.6 / "complete" do NOT cover — non-slice polynomial families (leads to D-M1)

NONCONG's "witness class" is the **fixed-slice** class (θ, a, b, c fixed, d free), modulus H = kab. The classical
notion behind "Mordell's theorem", Salez's S_ℓ and ET Prop 1.9 ("solvable by polynomials") also contains the
one-parameter families with (a, c, d) or (a, d, e) fixed (Type II) and (a, d, e), (a, c, f), (c, d, f) fixed (Type I).
Re-derived for numerator k from n = kabd − e / ne + 1 = kabd, ce = a + b:
II-2 n ≡ −ka²d (mod kacd − 1); II-3 n ≡ −ka²d − e (mod kade), gcd(kad, e) = 1; I-1 n ≡ −(ka²d+1)/e (mod kad);
I-2 n ≡ −f (mod kac), n ≡ −c/a (mod f); I-3 n ≡ −f (mod kcd), n² ≡ −kc²d (mod f). Their moduli need not be multiples of k
(II-2: f = kacd − 1 is coprime to k). `scripts/review_r267_families.py` tests the point x_{ℓ,r} against them and
**verifies each hit on an actual prime by building the solution and checking k/n exactly**:
* k = 4, x_{11,2}: II-2 (a, c, d) = (4, 9, 1): every n ≡ 79 (mod 143) has 4/n = 1/(4b) + 1/(36n) + 1/(9bn)
  (b = 9e − 4, e = (n + 64)/143); 79 ≡ 2 (11), ≡ 1 (13) so x_{11,2} lies in this class. Check n = 79:
  79 + 1 = 4·4·5·1 ✓.
* k = 4, x_{13,5}: II-2 (1, 5, 2): n ≡ 31 (mod 39) (n = 31: 4/31 = 1/8 + 1/310 + 1/1240 ✓). This is why Salez's
  S₁₃ = {5, 6, 8, 11} ≠ the slice-covered set {6, 11} that NONCONG's scan finds (it reports {2, 5, 7, 8} uncovered at 13);
  the agreement at ℓ = 11 ({7, 8, 10}) quoted in §2.4 is a coincidence of two different notions.
* **k = 8, x_{3,2}: II-3 (a, d, e) = (3, 3, 7): every n ≡ 281 (mod 504) is solvable** (c = (n + 223)/504, b = 7c − 3;
  n = 281: 8/281 = 1/36 + 1/(9·281) + 1/(12·281) ✓); 281 ≡ 1 (8), 2 (9), 1 (7).
* **k = 8, x_{5,2}: II-2 (1, 2, 1): every n ≡ 7 (mod 15) is solvable** (n = 7 ✓, 97 ✓).
* k = 8, x_{13,2}: II-2 (9, 2, 1), n ≡ 67 (mod 143) ✓.
* No family hit (parameters ≤ 40): k = 4 at x_{19,2}, x_{29,2}; k = 8 at x_{11,2}, x_{7,3}; k = 16 at x_{3,2}, x_{5,2};
  k = 12 at x_{5,2}.
Level deficits with all families allowed (`scripts/review_r267_famcomplete.py`; T1 still holds: 0 square classes
covered): k = 4: L = 12 becomes complete (slice-only deficit 1 → 0; the classical n ≡ 2 (3) family), L = 3432 = 24·143:
40 → 12; k = 8: L = 120: 18 → 5, 840: 96 → 15, 5040: 136 → 26 (still incomplete).

**Consequence.** Thm 2.6 is a correct theorem about fixed-slice classes, and "complete" (H = kab | L) is a correct
definition for O253's *determined* lifts (which choose a fixed target slice). But the headline readings — "a proved
point-classification separating 4 from every 4 | k ≥ 8", "for every 4 | k ≥ 8 no prime ℓ ≡ ±3 (8) is complete-capable",
"(c) no level through ℓ is complete", "Mordell completeness is the only 4-specific resource and is exhausted on 𝓜" —
do not survive passing to polynomial-family lifts, which the document's own Prop 1.3 treats as an equally legitimate
"visible-only" lift class of level M₀: for k = 8 the points x_{3,2}, x_{5,2} *are* covered, for k = 4 x_{11,2} is, and
the k = 4 dictionary changes (12 complete). See D-M1.

### §4: model screen and size information

* **§4.1 (CERTIFIED claim).** Reproduced from scratch (`review_r267_matched.py` with k as parameter): 8/131 sources
  59 (3/3 visible), 251 (10/10), 419 (7/7); 8/241: 409 (6/7), 601 (6/6), 769 (6/7); 12/12241: 11689 (13/19), 12409 (8/10),
  12841 (7/15); 16/3361: 3049 (1/2), 3529 (5/6), 3889 (0/1); 16/33601: all seven sources identical to the log. p has no
  witness in each case ✓. The logic is trivial once stated (any law whose antecedent holds at a model exception is
  refuted there) and the scope caveat (R-O257 M5) is present. **SOUND.** Note 16/3361 ← 3889 is "vis-sufficient"
  only vacuously (0 visible witnesses) — the log's `vis-sufficient=1` should say so.
* **§4.2 (EVIDENCE).** The document's own wording is honest ("descriptive, not a statistical test; independence is not
  established"). The hit rate of "some X of p divisible by D" is dominated by the distribution of D (small D hit almost
  surely), so matched/unmatched/shuffled differences mainly measure D-size differences (the author notes this for a′b′d′
  only). The report's "size-information permutation test: source sizes carry no signal" overstates (D8).
  **SOUND as EVIDENCE (descriptive).**

### Novelty, labels, resources

* Thm 1.2(ii), Prop 1.3: classical (Mordell–Schinzel, ET Prop 1.6, Schinzel 2000), correctly attributed after R266.
  Prop 1.4: elementary algebra; new packaging. Thm 2.6: I know no prior statement in this form; the relevant literature
  is ET Prop 1.9 (classification of polynomial-solvable classes) and Salez's filters — against which Thm 2.6 is a
  statement about the *slice* sub-family only (D-M1). Relative to (J)41: Thm 2.6 is indeed a non-numerator-blind
  statement, but only for fixed-slice classes; with all ET families the k = 8 points x_{3,2}, x_{5,2} are covered, so the
  "4 vs 8 separation at ℓ = 3, 5" is not a separation of polynomial solvability.
* Labels: PROVED / CERTIFIED / EVIDENCE are used correctly for the mathematics; the overclaims are in the Readings and
  in the report's SHARP 1/2 (D-M1).
* Resources: the self-reported 5-process burst (≈ 1 min) violated the ≤ 2-core rule (D9). My runs: ≤ 1 core, all under
  `ulimit -v 8000000` and `timeout`.

## Defects

**D-M1 (MAJOR) — fixed-slice scope of Thm 2.6 / §2.4 / §4.1 readings and of the Def 1.1 dichotomy.**
Location: §2.4 (definition of complete; "Completeness of L is exactly 'visibility at level L is sufficient for a
determined lift'" is right, but the Reading and the adelic-points bullet equate slice coverage with Salez's S_ℓ and
Mordell coverage), §5 Thm 2.6 (c) and *Reading* ("a proved point-classification separating 4 from every 4 | k ≥ 8",
"for every 4 | k ≥ 8 no prime ℓ ≡ ±3 (8) ever is [complete-capable]"), §4.1 last sentence, report SHARP 1–2,
memo z28_complete_levels. Problem: ET's non-slice polynomial families (II-2, II-3, I-1..I-3; moduli such as kacd − 1
coprime to k) cover x_{3,2} and x_{5,2} for k = 8 (n ≡ 281 (504), n ≡ 7 (15)), x_{11,2} for k = 4 (n ≡ 79 (143)), make
L = 12 complete for k = 4, and explain why the §2.4 scan disagrees with Salez at ℓ = 13. These are exactly Prop 1.3's
"polynomial lifts" — visible-only lifts of fixed level M₀ whose target slice varies with p — so they belong to the
lift picture the document analyses; Def 1.1's dichotomy (congruence-mediated with a fixed output vs witness-level) is
not exhaustive (such lifts are neither). Repair: (1) rename "complete" → "slice-complete" (complete for determined
lifts = fixed target slice, O253 Thm 3.1), and say so in Thm 2.6(c); (2) add a remark with the family examples above
and state that Thm 2.6's 4-vs-8 separation is a statement about fixed-slice classes only — for polynomial-family
coverage it fails at ℓ = 3, 5 for k = 8 and at ℓ = 11 for k = 4; (3) delete "= Salez's S₁₁" (coincidence) and
note S₁₃ ≠ slice set; (4) in the §2.4/§4.1 Assessments replace "the only 4-specific resource … is exhausted on 𝓜" by
"the only 4-specific resource *for determined (fixed-slice) lifts* …", and note that for polynomial-family lifts
levels through 11·13 are not useless for 𝓜 (e.g. Mordell primes ≡ 79 (143) are all solved by one family);
(5) add to Def 1.1 a third class ("fixed level, slice varying polynomially with p" = Prop 1.3), so the dichotomy is
explicitly "fixed slice / polynomial family / witness-level".

**D1 (MINOR)** §5 (c) and Reading: "for every 4 | k ≥ 8 (including ℓ = 3, 5)" holds only for ℓ ∤ k (k = 12 excludes
ℓ = 3; there x_{3,2} IS in the slice class (1, 6, e = 7), H = 72; k = 20 excludes 5). Repair: write "(ℓ = 3, 5 whenever
ℓ ∤ k)".
**D2 (MINOR)** §5 mechanism: "b₀(k − 4/g) ≤ 3" is only the Type II branch; the Type I branch that needs k ≥ 8 is
g + 2b₀ ≥ (k/2)gb₀ and uses k even (integrality). 4 | k is not used in (a)/(b) (only even k ≥ 8 resp. k = 4);
numerically (a) holds for every k ∈ [6, 32] with ℓ ∤ k (my scan). Repair: state the hypotheses actually used.
**D3 (MINOR)** §5 (b), Type II g = 1, c = 1: h = 1 (b₀ = 0) is dropped silently. Add "h = 1 gives b₀ = 0".
**D4 (MINOR)** §2.4 single-prime bullet: "k = 8 has none at all, because already ℓ = 3, 5, 7 carry uncovered points" is
a non sequitur (levels supported on 2 and on primes ≡ ±1 (8) are untouched; Thm 2.6(c) itself says so). Repair:
"k = 8 has no complete level divisible by 3, 5 or 7 (EVIDENCE for 7; PROVED for 3, 5 by Thm 2.6) and none ≤ 3200 at all".
**D5 (MINOR)** §1 after Prop 1.3: "p = m² ± j: Thm 2.2 (j > 0) and Thm 3.4 (j < 0; ℚ(√j))" mismatches NEAR_SQUARE's
convention (p = m² + k: Thm 2.2 for k > 0 with sterile set {m : m² + k ∈ (Ẑ^odd)²}, nonempty iff k ≡ 0, 1, 5 (8);
Thm 3.4 for k = −j < 0, j non-square, K = ℚ(√j), sterile set Z_K⁺). Repair: restate accordingly; only the j < 0 case
lives in ℚ(√j).
**D6 (MINOR)** §2.3 means not reproducible: no log/script; my counts (and the author's own `z28_lab cnts` output) give
0.1535 for k = 4 (text 0.159), uniformly ≈ 4 % lower for all k. Repair: state estimator and range, add a log; update
numbers (ratios and minima unchanged).
**D7 (MINOR)** Computation 3.2: counts treat (a, b) as unordered; say so.
**D8 (MINOR)** Report: "size-information permutation test: source sizes carry no signal" → "descriptive hit rates; no
visible difference; D-size confounded".
**D9 (MINOR, process)** 5-process burst over the 2-core limit (self-reported).

### Addendum: Thm 2.6 numerics extended
`review_r267_x2.c` with a ≤ b ≤ 1000, k = 4 and k = 8, all odd ℓ < 60: k = 4 hits exactly the four Mordell classes;
k = 8: no hit; 0 disagreements between the two membership tests.
