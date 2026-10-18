# B2_ACROSS_FIELDS — is B2 equivalent to a solved / deeply studied problem in another field? (task O261, wide net)

Status: checkpoint 1 (O261 deliverable complete; awaiting parent review). **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). External theorems are "Cited" only if their statement was read in the source
(abstract or excerpt in `sources/lit2026g/`); "(memory)" marks anything recalled but not re-read. Field memos:
`BRAINSTORM/z31_*.md`. Builds on (and does not repeat) LITERATURE_2026.md, LITERATURE_AUTOMORPHIC.md, PARITY_AUDIT.md ((J)87),
SYNTHESIS_SPARKS8.md ((J)89), BRAINSTORM/thin_group_orbits.md, farey_ford_cf.md, logic_divisibility_lgp.md,
gon_lll_relation_lattice.md, s6_divisor_pigeonhole.md, MARKOFF_ES.md.

## 0. Iteration log
* cp0: B2 forms checked against the source files (§1); feature list (§2); field plan.
* cp1: 5 research subagents (clusters A–E); 13 field memos; priority items read in the sources by me; table §3, deep items §4,
  synthesis §5, verification ledger §6.

## 1. B2 in its precise forms (checked against the files named)

Fix a prime p ≡ 1 (mod 4).
* **(E1) c = 1 line (★)** (PARITY_AUDIT §0, (J)6): ∃ C, u, B ≥ 1 with 4uBC − u − B = p; equivalently ∃ C: 4Cp + 1 has a
  divisor ≡ −1 (mod 4C). Heuristic count R(p) ≈ (log p)²/8 (EVIDENCE: 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰). Fails at exactly 14
  primes ≤ 10¹⁰ ((J)90).
* **(E2) b = 1 line** (SYNTHESIS_SPARKS8 Prop 1.3, B1_LINE.md; López 2404.01508 Thm 7 "Type A"): ∃ d ≥ 1: p + 4d has a divisor
  w ≡ −1 (mod 4d), w ≠ p + 4d. Fails at 193, 2521, 66529 and at no other prime ≤ 10¹¹ ((J)90).
* **(E3) window form** (CAP_POINTWISE §1, FORCED_WINDOW Prop 2.1, PARITY_AUDIT event (b)): for a prime q ≡ 3 (4), q ≡ 4 − p (8),
  (q/p) = −1, K := (p + q)/4: ES holds at window q (cap 0) iff Rat_q(K) ∩ {−1, −p} ≠ ∅, where Rat_q(K) = {u/v mod q : uv | K,
  gcd(u, v) = 1} (the brief's "Σ_q(K)"). Least-residue form (FORCED_WINDOW Prop 2.1): ES-Type-II(p) ⟺ ∃ coprime (u, v) with
  (−p mod 4uv) | u + v (prime to p).
* **(E4) lattice form** (ASTRA_BRIDGE Thm 3.4(c), (J)81): for g ≡ 3 (4), gcd(g, p) = 1, h = (g + 1)/4, ρ² ≡ −p (mod g),
  L_ρ(g) = {(M, Y) : Y ≡ ρM (mod g)}; ES shots with modulus g ⟷ points (2k, 1) ∈ L_ρ(g) with k | h, i.e. g | 4k²p + 1 with
  4k | g + 1.
* **(E5) twisted hyperbola** (SYNTHESIS_SPARKS8 Prop 1.5): ES-Type-II(p) ⟺ ∃ u ≥ 1 and (X, ε) with Xε ≡ u (mod p), height
  c = (Xε − u)/p ≥ 1, X ≡ −1 (mod 4cu). Kloosterman-fraction form: X̄/(4p) within ≍ 1/(uX) of 1/(4u) (§1.7 there).
* **(E6) integral points** on the affine cubic surface U_n : 4xyz = n(xy + yz + zx) in the positive octant (Bright–Loughran,
  arXiv:1908.02526, `sources/bright-loughran-1908.02526.pdf`); Br U_n/Br ℚ ≅ ℤ/2 (BL Thm 1.6), no BM obstruction to existence
  of positive points (BL Thm 1.8), BM does not control strong approximation (BL Thm 1.9).

## 2. Structural features a counterpart must match (the "fingerprint")
F1 single fixed integer p (pointwise, not almost-all);
F2 polylogarithmic expected count ≍ (log p)²–(log p)³ (no power-size main term);
F3 tied modulus: the residue-class modulus is part of the solution (height-dependent target);
F4 no local obstruction at primes (T1: odd squares kill only the Type I/II *shapes*);
F5 4-specific: the numerator-8 analogue of the event fails (131, 241);
F6 class-group / genus data see only the quadratic-character shadow (WINDMILL_REDUCTION Prop 10.3).

## 3. Field-by-field verdicts (13 memos, `BRAINSTORM/z31_*.md`)

Verdict scale: EQUIVALENT (same statement up to a dictionary) / INSTANCE (B2 is a special case of the counterpart problem
class) / ANALOGUE (shared shape, different statement) / UNRELATED. "Transfer" = could the counterpart's pointwise mechanism
plausibly prove B2. No row is SHARP for ES.

| # | field | counterpart (exact source) | pointwise proved? mechanism | first blocking feature | verdict | memo |
|---|---|---|---|---|---|---|
| 1 | thin orbits / CF | Zaremba: ∀q ∃a, digits of a/q ≤ M. BK Ann. Math. 2014 Thm 1.8 (a.a., mult. ≫ N^{2δ−1001/1000}); **Shkredov arXiv:2603.14116 Cor 1 (every prime/squarefree q), X. Zhang arXiv:2605.02518 Thm 1.2 (all q) — 2026 preprints** | YES (claimed, 2026): growth in SL₂(ℤ/qℤ) on two Cantor half-sets of size q^{w_M}, count q^{2w_M−1} | F2: ES-five = HJ-length-3 digit set (DEDEKIND_ES Cor 4.6), dimension 0, critical 2δ = 1; no alphabet knob | ANALOGUE | zaremba_thin_orbits |
| 2 | Markoff / strong approx. | Γ transitive on X*(p): BGS (Chen Thm 1.2.3), **Chen Thm 1.2.5 (orbit sizes ≡ 0 mod p), Thm 1.2.6** | YES (all but finitely many p): degree congruence on Hurwitz spaces + giant component | wrong axis (connectivity mod p of one surface vs existence on a family); on the family axis (x²+y²+z²−xyz = k) pointwise is FALSE (Ghosh–Sarnak); no Vieta group on U_n | ANALOGUE | markoff_chen |
| 3 | quadratic forms | (i) binary forms by I₃ (one-class genus); (ii) xy+yz+zx = n (Borwein–Choi); (iii) ternary (Duke–Schulze-Pillot), 290 | (i) local; (ii) class numbers + GRH; (iii) Eisenstein main term ≍ n^{1/2} | (i) solves only the sign layer ((J)48); (ii)/(iii) F2, F6 | (i) INSTANCE (sign layer); (ii),(iii) ANALOGUE | quadratic_forms |
| 4 | equidistribution | Duke 1988 Thm 1 (Heegner points, error \|d\|^{−δ}) | YES, power-size point sets, region targets | F3: **Lemma 4.1 (PROVED): ES shot ⟺ ideal divisor of (1 + 2k√−p) of norm ≡ −1 (mod 4k)** — a divisor condition on a representative, not a region; then F2 | ANALOGUE | duke_equidistribution |
| 5 | unit fractions | Bloom Thm 2; Liu–Sawhney Thm 1.1; Croot 2003; Graham 1963 (n > 77) | Bloom/Croot: density/colouring, target fixed, set varies; Graham: pointwise by additive recursion n ↦ 2n+2, 2n+9 | F1 (Bloom), multiplicativity (Graham: ES(n) ⟹ ES(mn) never reaches primes; B1) | ANALOGUE | unit_fractions |
| 6 | arithmetic geometry | integral HP on log K3 surfaces (BL: U_n is log K3); x³+y³+z³ = k (CTW: no BM obstruction; Heath-Brown: ~ρ log B solutions) | NO for any non-homogeneous family; YES for homogeneous spaces (strong approximation) | not homogeneous; Harpaz/GTZ blocked by F1/F3 | **INSTANCE** (B2 ⊂ bounded-height integral HP on a log K3 family); three cubes = closest sister ANALOGUE | integral_points_cubics |
| 7 | logic | Lipshitz LGP for increasing-form divisibility systems (via DHMP arXiv:2308.13609 p. 3) | YES for acyclic systems | F3 = a cycle d → w → d: **Lemma 7.1 (PROVED): E2 is non-increasing and its LGP fails at 193, 2521, 66529** | EQUIVALENT reformulation; mechanism ANALOGUE | logic_divisibility |
| 8 | complexity | Lenstra 1984 / CHN 2008 divisors in residue classes (s > n^{1/4+ε}) | YES, upper bound + algorithm | regime (ES slices have s ≪ n^{1/4}); no existence content | per-slice EQUIVALENT, NOT SHARP; hardness: constructive polylog B2 ⟹ deterministic QNR ((J)35) | complexity |
| 9 | additive combinatorics | ±-Davenport, Kneser, Olson/Szemerédi–Vu, Erdős–Rényi, AGP | YES given length ≳ log q (random) / √q (spread) / q (worst) | F2 (Ω(K) ≈ log log p), F1 (K forced, unlike AGP), F6 (+1 vs −1) | EQUIVALENT at a window (target −1 in a box product set); NOT SHARP | zero_sum |
| 10 | analytic NT, small counts | least QNR / primitive root / Linnik; 2^k + p (Erdős covering); Heath-Brown–Puchta (2 primes + 13 powers of 2) | polylog only under GRH and only for fixed-modulus character events; HBP via power main term | F3 (not a character event); F2 (HBP) | ANALOGUE | small_count_pointwise |
| 11 | graphs / probability | Poisson/Janson model of the shot graph; LLL; deterministic percolation (Gaussian moats) | random models only; LLL points the wrong way; deterministic versions open | F1 | ANALOGUE | graphs_probabilistic |
| 12 | geometry of numbers / topology | Minkowski, covering radius, degree/parity (Zagier) | YES (volume / parity) | F3 (exact height), sub-power windows ((J)85), T1 parity | ANALOGUE | geometry_topology |
| 13 | dynamics / ergodic | Furstenberg; Hecke orbits; Rényi/Euclid transfer operators | averages; power orbits; main terms only | F1, F2 (critical exponent: indifferent fixed point) | ANALOGUE | dynamics_ergodic |

Hilbert's 10th / o-minimality: UNRELATED for B2 (single p is a finite search; Pila–Wilkie gives upper bounds) — memo 7.

## 4. Deep items (the brief's priority list)

**4.1 Zaremba (BK → Huang → Shkredov 2026 → X. Zhang 2026).** Read by me: BK Thm 1.8 and p. 8 ("if we could prove that the
errors are individually bounded, |E_N(d)| ≪ N^{2δ−1−ε}, say, then we would conclude the full Conjecture 1.7. We are not able
to establish control of this quality individually, but do succeed on average"); Shkredov arXiv:2603.14116v2 Cor 1, Thm 8,
Lemma 13; Zhang arXiv:2605.02518v2 Thm 1.2, Remark 1.4. **New to the campaign: Zaremba is claimed proved pointwise (every
prime/squarefree q: Shkredov; every q: Zhang), by growth in SL₂(ℤ/qℤ), i.e. by a non-averaged mechanism.** Both are 2026
preprints; I did not check proofs. What the mechanism uses (memo 1 §(c)): a fixed modulus q (the denominator), two
Cantor-type half-sets of size q^{w_M}, w_M = 1 − O(1/M), glued by a congruence mod q whose expected count is
q^{2w_M−1} — a power, bought by taking M large. In CF coordinates ES-five(p) is also a fixed-modulus statement ("some QNR A mod p
with HJ-length(p/A) ≤ 3", DEDEKIND_ES Cor 4.6), so F3 is *not* the obstruction there; the obstruction is F2 in its rigid form:
the ES digit set is a finite-length word set (dimension 0, critical exponent 2δ = 1, ≍ log² p numerators), with no alphabet
knob, and growth theorems need sets of size ≥ q^ε. Verdict ANALOGUE, transfer NOT SHARP. **Erratum-type flag for the parent:**
BRAINSTORM/thin_group_orbits.md §4 ("Every thin-orbit local-global theorem known is density one") and farey_ford_cf.md
("BK and Huang are 'almost all q' statements") are outdated if the 2026 preprints stand; the barrier statement survives in the
form "every known pointwise thin-orbit theorem has a power-size representation count".

**4.2 Markoff / Chen.** Read by me: Chen Thms 1.2.3 (BGS), 1.2.5, 1.2.6. Chen's is a genuinely non-counting pointwise argument
(orbit sizes divisible by p via a degree congruence on Hurwitz spaces + a giant component), but it proves *uniqueness of an
orbit* on a power-size set with trivially non-empty fibres; the ES-shaped question is the family axis k ↦ X_k, where the
pointwise integral Hasse principle is false (Ghosh–Sarnak). No group acts on U_n(ℤ). Verdict ANALOGUE, NOT SHARP.

**4.3 Duke.** Duke 1988 Thm 1 (verbatim via agent). New elementary dictionary (memo 4, Lemma 4.1, PROVED, numerically
checked): an ES shot is an ideal divisor 𝔞 | (1 + 2k√−p) in ℤ[√−p] with N𝔞 ≡ −1 (mod 4k). Duke-type theorems see classes and
regions; the ES condition is on a representative dividing a prescribed element (F3), with polylog expected count among ≍ √p
points (F2). Verdict ANALOGUE, NOT SHARP.

**4.4 Bloom.** Bloom Thm 2 (abstract re-read by me): positive upper density ⇒ some finite S with Σ 1/n = 1. The quantifiers are
reversed relative to B2 (target fixed at 1, the denominator set is the free object, exponentially many subsets); 3-term sums
have no central-limit behaviour for Bloom's Fourier step to exploit. Verdict ANALOGUE, NOT SHARP.

## 5. Synthesis and verdict (Assessment)

**Answer to O261.** B2 is **not** equivalent to, nor an instance of, any *solved* problem found in 13 fields. It is
* an **INSTANCE** of the bounded-height integral Hasse principle on a family of log K3 surfaces (BL's framing; memo 6), a class
  in which no pointwise existence mechanism is known for any non-homogeneous family; its closest open sister is
  x³ + y³ + z³ = k (one parameter, ~ρ log B expected solutions, no BM obstruction (CTW), open for every individual k);
* **EQUIVALENT (exact reformulations, PROVED dictionaries)** to: a cyclic (non-increasing) linear divisibility system
  (memo 7, Lemma 7.1); a target-(−1) problem for a box product set in (ℤ/q)^* (memo 9); a divisors-in-a-residue-class decision
  problem per slice (memo 8); an ideal-divisor-in-a-ray-class condition on (1 + 2k√−p) (memo 4, Lemma 4.1) — none of which
  lands in a solved regime of its field.

**The pattern (Assessment).** Every pointwise existence theorem surveyed uses at least one of four inputs, and B2 offers none:
| input | used by | B2 lacks it because |
|---|---|---|
| M1 power-size main term | Duke, ternary forms, 290, Borwein–Choi, BGS, Shkredov/Zhang Zaremba, HBP, Graham | F2: ≍ (log p)²–(log p)³ |
| M2 fixed-modulus character/group event | least QNR / primitive root under GRH, Lipshitz LGP (acyclic), Shkredov/Zhang (mod q) | F3 (in CF coordinates the modulus is fixed but then M1 fails — the trade of SYNTHESIS_SPARKS8 Prop 1.4) |
| M3 homogeneity / group action on solutions | strong approximation for groups, Chen/BGS, Zagier windmill | U_n not homogeneous; finite automorphism group; T1 parity |
| M4 freedom to choose the objects | AGP Carmichael, Bloom/Croot, Graham's recursion, fibration methods | F1: p and K = (p+q)/4 are forced |
The 2026 Zaremba theorems are the sharpest test of this pattern: a pointwise theorem in a CF/thin-orbit problem by growth
(M1 + M2), whose ES-five analogue keeps M2 but has no M1 (in that coordinate the ES-five certificate set is exactly the
set of HJ-length ≤ 3 numerators, DEDEKIND_ES Cor 4.6, of size ≍ log² p). This is a sharpened restatement of the campaign's B3 (scale) and B2 (tied modulus) barriers, not a new
obstruction theorem.

**No field offered a SHARP transfer.** One spark for the parent (not pursued): if Shkredov–Zhang hold, is there any ES
*relaxation* whose certificate set at p, in CF coordinates, has dimension > 1/2 (a "Zaremba-sized menu")? Such a relaxation
would become a pointwise theorem by their method; the campaign's provable relaxations (ES^{(S)}, capped ES) are already
theorems by other means, so the value would be methodological only.

## 6. Verification ledger (research-agent claims graded by me)
* **Verified by me in the source:** BK Thm 1.8, Conj 1.3/1.7, (1.37) discussion (arXiv PDF); Shkredov 2026 Cor 1, Thms 8, 12,
  Lemma 13 (arXiv PDF); Zhang 2026 Thm 1.2, Rem 1.3–1.4 (arXiv PDF); Moshchevitin–Shkredov abstract (q = O(p³⁰), p | q);
  Chen Thms 1.2.3, 1.2.5, 1.2.6 (arXiv PDF); CTW abstract; Heath-Brown's conjecture (Booker–Sutherland p. 5); Lipshitz LGP via
  DHMP pp. 2–3; Bloom abstract; BL Thms 1.8, 1.9 and "log K3" (local PDF).
* **Verbatim per research agent, not re-read by me:** Duke 1988 Thm 1; Huang Thm 1.1; Liu–Sawhney Thm 1.1; Croot abstract;
  Graham 1963 statement; Borwein–Choi abstract; HBP Thm 1; Lenstra 1984; CHN 2008 abstract; LOW 2015 abstract; Jeřábek
  abstract; Ghosh–Sarnak abstract; Harpaz Thm 1.0.1; BGS 1607.01530 Thms 1–2.
* **NOT verified (memory or secondary; flagged):** Duke–Schulze-Pillot statement; Ono–Soundararajan statement; Bhargava–Hanke
  exact wording; Humphries–Radziwiłł exponents; ELMV theorem number; Frolenkov–Kan/Kan theorem numbers; Magee–Oh–Winter
  role; Niederreiter special families; Eddy et al. numerical threshold; Brown's computations; Colliot-Thélène–Wei–Xu and
  Loughran–Mitankin theorem numbers; Colliot-Thélène–Xu theorem; Vaughan 1970 (secondary); Erdős 1950 (secondary);
  Pintz–Ruzsa K = 8; least-witness bounds (Burgess, Ankeny, Bach, Shoup, Xylouris); ACFKP D_± value; Erdős–Rényi threshold;
  AGP lemma; Olson / Szemerédi–Vu; Graham's recursion details (2n + 2, 2n + 9); Booker 33 / Booker–Sutherland 42.
* **Brief item not identified:** "Conway–Guy" (no relevant theorem found by agent D or me; no claim made).
