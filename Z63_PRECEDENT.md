# Z63_PRECEDENT — is there ANY theorem proving pointwise existence at polylog expected count without an identity? (wave z63, lane PRECEDENT)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results are internally reviewed only. Brief: `z52bbriefs/z63_lanes.md` §PRECEDENT.
Source excerpts (verbatim, URL, access date 2026-11-07, theorem numbers): `data/z63/precedent/sources/*.txt`.
Script: `scripts/z63_precedent_qnr_zeros.py` → `data/z63/precedent/qnr_zeros.txt`.

**Verdict: narrowed (literature: answer (b) in the sense that matters, with an exact list of the literal precedents and
why each fails to transfer). No HOT LEAD.**

## 0. Bottom line

1. *Literal precedents exist, in exactly four mechanism classes.* (Assessment, resting on the verified rows of §2.) Read
   literally, the brief's criteria are (P1) pointwise, (P2) polylog or bounded expected count, (P3) no identity, and
   (P4) unconditional. These four classes pass them:
   * **(S) size/valuation squeeze.** AKS Lemma 4.3 (V); least prime non-divisor (V); Sylvester–Schur.
   * **(M2-W) RH-strength character sums at a fixed modulus, made unconditional by Weil in 𝔽_q[t].** Bhowmick–Lê
     Thms 3, 5, 6 (V) and Shoup/Shparlinski: primitive elements of 𝔽_{qⁿ} among the monic polynomials of degree
     ≍ log_q n. That is a candidate set of size polylog(qⁿ).
   * **(T) thick object + exact extraction.** Zagier's windmill, Thue/Minkowski.
   * **(R) rigidity.** Zsigmondy/BHV; r₂(p) = 8.
   (T) and (R) are what the brief calls "algebraic". Over ℤ, (M2) is available only under GRH: Lamzouri–Li–Soundararajan
   (LLS) Cor 1.1 and Thms 1.2 and 1.4 (V).
2. *None of the four transfers to B2, and each fails at a named screen.* (§3, §4.) Each line is labelled separately.
   * **(S): no input-blind squeeze exists.** Lemma 1 (PROVED; a short consequence of T1). Every known squeeze is
     input-blind: it works for all n ≥ 1. A squeeze for B2 would instead need a step "p prime ⟹ divisibility", and no
     such step is known that is not an identity.
   * **(M2): it reaches only the non-residue layer.** EVIDENCE (CERTIFIED computation): every one of the 14 (★)-zero
     primes p ≤ 10¹⁰ has a prime non-residue ≤ 23 (F4, §4). So no argument whose only arithmetic input about p is a
     small non-residue can produce a (★) witness at these p.
   * **Function-field check on (M2-W).** In 𝔽_q[t], RH and polylog-window M2 theorems are unconditional, yet the
     T1-compatible ES analogue MS_q is *false* at a positive proportion of irreducibles of each fixed even degree once q
     is large (PROVED relative to Chebotarev, `Z58_FFIELD.md` Cor 3.2), and open at fixed q.
   * **(T) and (R):** screened earlier (z52 §2.1, B4, PRIMITIVE_INTERSECTION).
3. *No precedent of the needed kind.* (Assessment.) I found no unconditional theorem over ℤ that lower-bounds a sparse
   count at a prescribed input. Nor did I find, even under GRH, a theorem proving a pointwise **hit** event at polylog
   expected count when the target density per trial is not ≥ 1/polylog. The cleanest calibration is the least prime
   ≡ a (mod q):
   * Heath-Brown's conjectured P(a, q) ≪ q(log q)² is open.
   * GRH gives only (φ(q) log q)² (LLS Cor 1.2, V).
   * A 2026 pair-correlation paper says outright that its method "does not bring us closer" (Kandhil–Languasco–Moree
     arXiv:2607.14515v1, Remark 2, V).
   * Explicit additive bases with r(n) ≤ polylog are open. The best explicit result is n^{c/log log n} (Jain–Pham–
     Sawhney–Zakharov (JPSZ) arXiv:2405.08650 Thm 1.1, V). The random construction of Erdős 1956 does reach r ≍ log n,
     but only for a *chosen* set.
4. *The gap, stated precisely* (§3.5). The first theorem of its kind would assert, for every large prime p:
   * existence of a divisor of a *specified* integer N(p, w) in a residue class whose modulus moves with w;
   * at expected total count (log p)^{O(1)};
   * with the statement false on an explicit infinite set (here the odd squares), so the proof must use a non-local
     property of p;
   * with the witness not produced by an identity, a thick extraction or a squeeze.
   Every known neighbour relaxes at least one of five features (§3.4 cell map): power count, fixed modulus, escape
   polarity, designed object, or algebraic event. B2 relaxes none of them.

## 1. Precise question, and why it is not already closed

**Definition (precedent).** A theorem T is a *precedent* if:
* (P1) for **every** sufficiently large input n in an infinite natural class 𝒩, it asserts a witness set W(n) ≠ ∅.
  "Almost all n", averages over n, "infinitely many n", and statements about a *chosen* (designed or random) object do
  not count.
* (P2) the natural expected size of W(n) is (log n)^{O(1)} or O(1). If T confines W(n) to a window, the expected count
  that matters is the one **inside the window T actually guarantees**.
* (P3) the proof does not produce the witness from an algebraic identity or parametrisation.
* (P4) T is unconditional.

**Target (B2).** At a prime p ≡ 1 (24):
* we need some C ≥ 1 and a divisor d | 4Cp + 1 with d ≡ −1 (mod 4C);
* the expected number of such (C, d) is ≍ log²p (FRONTIER §2.2);
* every witness d has a prime factor ℓ with (ℓ/p) = −1 (FRONTIER §3 B5, Lemma CT);
* the search box is O(p²) (B-fin).

Equivalent "d-form" (`Z58_WITNESS.md` §1): some d ≡ 3 (4) has (−p mod d) | (d + 1)/4. In words, p mod d hits a target
set S_d of size τ((d + 1)/4), a per-trial density that decays like a power of d.

**Prior work** (do not redo):
* `DETERMINISTIC_EXISTENCE.md` (O168).
* `B2_ACROSS_FIELDS.md` ((J)94, the M1a/M1b/M2–M5 table in FRONTIER §3).
* `BRAINSTORM/s9_lower_tail_literature.md` ((J)103).
* `BRAINSTORM/z52_deep_thin_pointwise_opus.md`: 40-row catalogue, (T)/(R) taxonomy, generator matrix, and
  count-congruence / zero-sum / discharging / interlacing screens.
* `Z53_LIT.md` §6.4 (proposed (J)103 wording) and `Z58_LIT.md` §2.5 (no pointwise lower bound for divisors in a class).

The verdicts there are Assessments, and several rows were **NOT ACCESSED** in the primary source (z52 §4): Burgess,
Bach, Sylvester–Schur, the GRH coset result, and the whole thin-basis literature. **New here:**
* the brief's candidate list, verified at theorem-number level (§2);
* the **(M2-W)** finite-field row: an unconditional literal precedent, never screened in the repo;
* the **squeeze** class isolated as a literal precedent over ℤ, with a proved obstruction to transferring it (Lemma 1);
* the **target-density calibration** of GRH-M2 (LLS Thm 1.4): polylog windows are reached only when the target has
  density ≥ 1/polylog;
* the explicit-basis calibration (JPSZ);
* an F4 falsifier for the M2 transfer (§4);
* a cell map and gap statement (§3.4–3.5).

## 2. Ranked table

Verification: **V** = statement read in the source (by me or by a subagent with a saved excerpt; the decisive rows,
marked ✔, I re-read myself from the PDF). **V2** = read in a later paper that restates it (named). **R** = verified
earlier in the repo (file named). **NA** = not accessed.

"Count" is the expected witness count in the window the theorem guarantees, at one input. "P1–P4" is ✓ when the row
passes all four criteria of §1; otherwise the first failing criterion is named.

Ranking is by closeness to a usable precedent for B2. Literal passes come first; within a tier, structural similarity to
B2 (hit polarity, moving modulus, divisors of a specified integer) breaks ties.

### Tier A — literal precedents (pass P1–P4)

| # | statement (source, theorem no.) | ver. | count | mechanism | transfer to B2 |
|---|---|---|---|---|---|
| A1 | 𝔽_q[t]: for Q of degree n and χ ≠ χ₀ mod Q, 2 log_q n ≤ r ≤ d ≤ n: Σ_{f∈A_d} χ(f) = Σ_{f∈P(d,r)} χ(f) + O(n q^{−r/2} q^d), "Our result is unconditional". With d = 2 log_q n + 2 log_q(1/ε)·(C log(1/ε)/log log(1/ε)), the density of primitive elements among the monic polynomials of degree d is within 2^{ω(N−1)} O_q(ε) of φ(N−1)/(N−1), where N = qⁿ. Input: Hsu Thm 2.1 / Effinger–Hayes, i.e. Weil (Bhowmick–Lê arXiv:1412.7373, Thm 3, Thm 5, Thm 6, Thm 8). Shoup (Math. Comp. 58 (1992)) and Shparlinski give poly(n)-size sets unconditionally for p = n^{O(1)} | ✔V | q^d = poly(n) = polylog(N) candidates, density ≫ 1/(log ω(N−1) + 1)² (Thm 6) | **M2-W**: fixed modulus Q, RH-strength sum (Weil), escape event (primitive = in no maximal subgroup) | **Fails.** MS_q is false at fixed even degree for large q (`Z58_FFIELD.md` Cor 3.2, a positive proportion of irreducibles). At fixed q it is open and "B2 reappears" (ibid. §5(d)) although RH is a theorem. §3.3 |
| A2 | "Lemma 4.3. There exist an r ≤ max{3, ⌈log⁵ n⌉} such that o_r(n) > log² n." Proof: the least r not dividing n^{⌊log B⌋}·∏_{i ≤ log²n}(nⁱ − 1), using lcm(1..m) ≥ 2^m (Lemma 3.1) (Agrawal–Kayal–Saxena, Annals 160 (2004); author PDF v6) | ✔V | most r ≤ log⁵ n qualify: polylog, dense | **S**: failure ⟹ every r ≤ B divides one integer of size < 2^B | Fails: Lemma 1 (no input-blind squeeze for B2) |
| A3 | Least prime not dividing n: a(n) < (1 + ε) log n for n > N(ε) (OEIS A053669 %F; primorial size) | V | ≍ log n/log log n | **S** (input-blind) | as A2 |
| A4 | Sylvester–Schur: for n > k, some element of n, …, n + k − 1 has a prime factor > k (Erdős 1934; Erdős 1955 Thm 1) | V (subagent excerpt) | not sparse | **S** (Legendre valuation count) | as A2 |
| A5 | Zagier's one-sentence proof: an involution on S = {(x, y, z) ∈ ℕ³ : x² + 4yz = p} has exactly one fixed point (Zagier, AMM 97 (1990) 144) | R (z52 row 1, `sources/z52/thin_pointwise/01-zagier.txt`) | r₂(p) = 8 | **T** + count congruence on a thick set | screened: every level count of (★) is even, R(p)/2 behaves like a fair coin (z52 §2.1); finite affine windmill menus are barred (INVOLUTION_ES2 Thm 5.1, closed list in z53 brief) |
| A6 | Thue/Brillhart, Minkowski: p = x² + y² via a lattice of index p | NA (z52 row 2) | O(1) | **T** (collision, symmetric target) | B4: collisions give signed solutions, and ES's target −1 is not the identity |
| A7 | Bang–Zsigmondy; Bilu–Hanrot–Voutier (primitive divisors) | R (z45_recent_pointwise_tools) | ≥ 1 | **R** (cyclotomic) | The integer and the class are wrong. The prime-divisor (★) subfamily fails at 94 primes < 10⁶ (PRIMITIVE_INTERSECTION) |
| A8 | r₂(p) = 8, one class per genus (idoneal) | R (z52 β′) | O(1) | **R** (multiplicative count) | R(p) = Σ_C D(4Cp + 1) is not multiplicative; fixed-level identities fail T1 ((J)7) |

### Tier B — conditional M2 over ℤ (fail P4)

| # | statement | ver. | count | mechanism | transfer |
|---|---|---|---|---|---|
| B1 | GRH: least QNR mod a prime q ≥ 5 is < (log q)² (LLS arXiv:1309.3595, Cor 1.1). Least prime outside a subgroup H of index h is < (α(h) + o(1))(log q)², α(2) = 0.8 (Thm 1.2). Bach (Math. Comp. 55 (1990)): least compositeness witness ≤ 2 log² m under ERH (abstract; internal theorem number NA) | ✔V (LLS), V (Bach abstract) | ≍ log²q/log log q: polylog | M2, escape | Gives only the non-residue layer. Under GRH, "(q/p) = −1 for some prime q ≤ 2 log²p ⇒ ES(p)" is *equivalent* to ES for large p (z52 row 11). F4 falsifier (§4): every (★)-zero prime has a non-residue ≤ 23 |
| B2 | GRH, **hit** form: the least prime p in a given coset aH of index h satisfies p ≤ 10⁹ or p ≤ ((5/2)(h − 1) log q + 3(h + 1) + (log log q)²)² (LLS Thm 1.4). With H = {1}: P(a, q) ≤ (φ(q) log q)² (LLS Cor 1.2); Bach–Sorenson (1.1)–(1.2) | ✔V | ≍ h(log q)²/log(h log q): polylog **iff h ≤ polylog** | M2, hit | §3.2: hit events reach polylog windows only when the target density is ≥ 1/polylog. B2's per-trial density decays like a power, and its moduli move |
| B3 | Least primitive root g(p) = O(log²p) under GRH (as quoted in arXiv:1703.06673; Shoup's GRH bound via Moree, z52 row 14) | V2 | polylog | M2 | as B1 |

### Tier C — designed or random objects (fail P1: the object is chosen, not prescribed)

| # | statement | ver. | count | mechanism | transfer |
|---|---|---|---|---|---|
| C1 | "Theorem 8.6.2 [Erdős (1956)] There is a set S … c₁ ln n ≤ f(n) ≤ c₂ ln n." Proof: Pr[x ∈ S] = min(10√(ln x/x), 1), Chernoff, Pr[A_n] < n^{−1.1}, Borel–Cantelli (Alon–Spencer, 2nd ed., §8.6). Erdős 1954 (Acta Szeged 15): 0 < f(n) < c₁ log n, "We will not be able to construct our sequences explicitely" | V2 / V | ≍ log n | M4: random set, concentration + BC | p is forced, so the random choice is unavailable (prob_lll_fixed_p). A random model of (★) predicts failure probability exp(−c log²p), but nothing transfers that bound to a prescribed p |
| C2 | Erdős–Tetali (RSA 1 (1990)): k-term bases with r ≍ log n (Alon–Spencer Thm 8.6.3); Vu (Duke 105 (2000)): thin Waring bases with R = Θ(log n) (as Vu, RSA 21 (2002) Thm 7.4) | V2 | ≍ log n | M4 + Janson / Kim–Vu concentration | as C1 |
| C3 | Kolountzakis (Discrete Math. 145 (1995)): deterministic poly-time enumeration of an Erdős basis, "by derandomizing a probabilistic proof" | V2 (O'Bryant survey, JPSZ) | ≍ log n | M4, derandomised (conditional expectations) | Derandomisation needs freedom to choose; at fixed p the conditional expectation ≥ 1 *is* R(p) ≥ 1 (z52 λ row) |
| C4 | **JPSZ (arXiv:2405.08650v1) Thm 1.1**: "There is an explicit set A ⊂ ℕ … for every n ∈ ℕ, we have 1 ≤ σ_A(n) ≤ Cn^{c/log log n}". Also: "We believe obtaining an explicit construction achieving σ_A(N) ≤ exp((log N)^ε) or better would be interesting"; and under "strong number theoretic conjectures" one can take numbers within O((log n)^{O(1)}) of a square | ✔V | n^{c/log log n}: **not** polylog | **I** (generalised-base digits, Ruzsa's A_p + A_p = ℤ/p²; every n is covered by construction) | Calibration: even a designed *explicit* set gets pointwise existence only from an exact covering identity, at a super-polylog count. Explicit polylog is open |
| C5 | Erdős–Nathanson (1981), Wirsing (Analysis 6 (1986)), Spencer (1996): thin random subsets of squares that are bases of order 4, with B(x) ≍ (x log x)^{1/4}. Choi–Erdős–Nathanson (PAMS 79 (1980)): explicit, finite range, \|A\| < c n^{1/3} log n | V2 (Nathanson 1987; Vu 2002 §7.2) | Wirsing: ≍ log n (inferred from the density, not quoted) | M4 | as C1 |
| C6 | Pilatte (arXiv:2303.09659v3) Thm 5.4: a Sidon asymptotic basis of order 3 exists a.s., via Lemma 5.3, P(m ∉ 3S) ≤ exp(−m^{3c−1−o(1)}) with c = 0.35 | ✔V | the exponent shows the count is ≈ m^{0.05}, a **power** | M4 + function-field (Sawin) input | Calibration: even the designed Sidon basis runs at a power count |

### Tier D — pointwise and unconditional, but the guaranteed window has a power count (fail P2)

| # | statement | ver. | count | mechanism |
|---|---|---|---|---|
| D1 | Burgess, Mathematika 4 (1957), Thm 2: least QNR d = O(p^a) for every a > 1/(4√e) | V | p^{0.15}-window, power | character-sum amplification |
| D2 | Linnik P(a, q) ≪ q^L (L = 5.2 per LLS; ≤ 5 per Xylouris/KLM — sources disagree); Chang (2014) Cor 11: P < q^{12/5+o(1)} for smooth q | V2 | power | zero-density / log-free |
| D3 | Burthe, Acta Arith. 80 (1997): w(n) = O_ε(n^{1/(6√e)+ε}) for odd composite n (p. 313; Cor 4.3, Thms 4.6–4.7) | V | power | Burgess-type |
| D4 | Filaseta–Trifonov (JLMS 45 (1992)): (x, x + c x^{1/5} log x] contains a squarefree integer | V2 (arXiv:2211.09975) | power | lattice points near curves |
| D5 | Duke, Invent. 92 (1988), Thm 1 (equidistribution of Heegner points / geodesics; r₃(n) ≫ n^{1/2−ε}); Duke–Schulze-Pillot, Invent. 99 (1990) | V / V2 | n^{1/2±ε} | half-integral weight + Siegel |
| D6 | Linnik (dispersion): every large n = p + x² + y² (Assing–Blomer–Li arXiv:2005.13915 Thm 1.2); Helfgott, ternary Goldbach | V2 / V | ≍ n, ≍ n²/log³n | dispersion / circle method |
| D7 | Borwein–Choi, Exp. Math. 9 (2000): every n except 18 listed values and at most one more is xy + yz + zx (none more under GRH) | V2 (OEIS A025052) | class-number size, power | class groups, ineffective |
| D8 | Zaremba claims (Shkredov arXiv:2603.14116, Zhang arXiv:2605.02518); MMS arXiv:2212.14646; Niederreiter q = 2^α, 3^α, 5^α | R (Z53_LIT §5(g)) / V2 | q^{2w_M − 1}, power | expansion / explicit (I) |
| D9 | Ramaré–Walker Thm 1.1 (products of 3 primes in every class); Heath-Brown–Puchta (p₁ + p₂ + 13 powers of 2); Zaharescu ‖n²α‖ ≪ N^{−4/7+ε} | R (z52) / V2 | power | dense generating set; circle method |

Transfer of all Tier D rows: B3/B-fin. The count in ES's *whole* O(p²) box is ≍ log²p, so there is no box to enlarge.

### Tier E — not pointwise for a prescribed input (fail P1)

| # | statement | ver. | why not pointwise |
|---|---|---|---|
| E1 | Ford, Annals 168 (2008), Thm 1(v): H(x, y, 2y) ≍ x/((log y)^δ(log log y)^{3/2}) | V | a density; false at primes |
| E2 | Friedlander–Iwaniec, Annals 148 (1998), Thm 1 (X² + Y⁴); Heath-Brown, Acta 186 (2001) (x³ + 2y³) | V | asymptotic counts in x |
| E3 | Heath-Brown, Acta Arith. 155 (2012): #{n ≤ x : n² + 1 squarefree} = c₀x + O(x^{7/12+ε}) | V | density |
| E4 | Heath-Brown 1986 (Artin): at most two exceptional primes q | R (z52 row 15) | infinitely many p |
| E5 | Coverings: Hough, Annals 181 (2015), Thm 1 (least modulus ≤ 10¹⁶); Balister–Bollobás–Morris–Sahasrabudhe–Tiba (BBMST) arXiv:1811.03547 Thm 1.1 (uncovered density ≥ e^{−4C}/2) | V | a statement about *some* uncovered integer. Dually it shows that sterile sets are non-empty, which is the B1 direction (it works *against* pointwise ES) |
| E6 | Tao, Discrete Analysis 2016:1, Thm 1.1 (EDP) | V | pointwise for every ±1 sequence but unquantified; witnesses are not thin |

### Tier F — existence tools whose guarantee is "≥ 1 given structure" (P2/P3 not applicable)

| # | statement | ver. | relevance |
|---|---|---|---|
| F1 | Combinatorial Nullstellensatz, Alon CPC 8 (1999) Thm 1.2 | V | needs a nonzero top coefficient (algebra) |
| F2 | Chevalley–Warning; Warning's second theorem; Ax–Katz; restricted-variable versions (Schauz, Brink) | V2 (arXiv:1404.7793 Thms 1.1, 1.2) | z52 §2.1 Lemma 2.1(c): the cubic (★) encoding has #vars = degree, so CW and its restricted form do not apply |
| F3 | Alon–Füredi: u_A = 0 or u_A ≥ m(a₁, …, a_n; Σa_i − deg P) (Clark–Forrow–Schmitt Thm 2.3, citing [AF93, Thm 5]); Schanuel 1974 / Brink: integer congruences mod p^v | V2 | gives a lower bound *once one non-zero exists*, or covers congruences only; no integer-equation analogue |
| F4 | LLL (Erdős–Lovász 1975), Moser–Tardos JACM 57 (2010) Thms 1.1–1.2 | V | needs a free random object; p is fixed (z52 λ) |
| F5 | Szemerédi–Trotter, Beck | V2 (Wikipedia) | upper bounds / linear counts |
| F6 | Pila–Wilkie (Duke 133 (2006); "Thm 1.8" not verified), Pila–Shankar–Tsimerman arXiv:2109.08788 Thm 1.1 | V2 / V | upper bounds; existence comes from a power-vs-T^ε contradiction (finiteness), not from lower bounds at one input |
| F7 | Entropy decrement (Tao arXiv:1509.05422 §1, §3) | V | pigeonholes a good *scale*; used for averaged statements |

### Tier G — failure-side calibrations (natural thin problems that FAIL pointwise)

Already in the repo (s9, z52 rows 34–38):
* Crocker, PJM 36 (1971): infinitely many odd n ≠ p + 2^a + 2^b, with expected count ≍ log n.
* Pan: ≫ x^{1−ε} exceptions.
* Ghosh–Sarnak, Markoff: (log k)² on average, power-many failures.
* Goldbach's other conjecture: 5777, 5993.

### Tier H — open problems in B2's own cell (calibrations)

| # | problem | status (source) |
|---|---|---|
| H1 | least prime ≡ a (mod q) ≤ q(log q)^A, i.e. a hit at polylog expected count with a fixed modulus | open **even under GRH**. LLS Cor 1.2 gives (φ(q) log q)². Kandhil–Languasco–Moree arXiv:2607.14515v1 Thm 5 (GRH + pair correlation) gives φ(q) exp(B(log q)^A), and its Remark 2 says it "does not bring us closer to establishing Heath-Brown's conjectural estimate p(k) ≪ k(log k)²" (✔V) |
| H2 | explicit basis of order 2 with σ_A ≤ polylog | open; best is n^{c/log log n} (JPSZ ✔V) |
| H3 | squarefree integer in every (x, x + (log x)^A] | open; FT give x^{1/5} log x |
| H4 | pointwise *lower* bound ≥ 1 for #{d \| N : d ≡ a (mod q)}, q ≥ N^ε | none known. Lenstra 1984 and Coppersmith–Howgrave-Graham–Nagaraj are upper bounds (Z58_LIT §2.5; the hunt subagent found nothing new — absence, not proof) |
| H5 | unconditional polylog QNR / primitive root | open. Graham–Ringrose (1990): n_p ≫ log p log log log p infinitely often (V2) |

## 3. Analysis

### 3.1 How literal precedents get existence (Assessment)

Every literal precedent in Tier A gets its witness from one of four sources:
1. **An exact structure.** An identity, a count congruence on a thick set, or a lattice collision (T, R). The witness
   count never enters the proof.
2. **A squeeze (S).** If no witness exists in the window, a single explicit integer is divisible by too much.
3. **A square-root-cancellation explicit formula for one fixed character modulus (M2).** This needs RH: Weil in
   𝔽_q[t], GRH over ℤ.
4. **Not an analytic lower bound for a sparse count at a prescribed input.** That is the B2 requirement, and no row
   does it.

The z52 (T)/(R) taxonomy missed (S) and (M2-W) as *literal* passes. Both were already present in its catalogue as
"(R)"-adjacent rows (μ squeeze; κ under GRH), but were not recognised as unconditional passes.

### 3.2 Hit polarity under GRH: the target-density threshold (Assessment from LLS Thm 1.4, ✔V)

Under GRH the least prime in a coset of index h is ≤ ((5/2)(h − 1) log q + O(h) + (log log q)²)². Up to that bound
the expected number of primes in the coset is ≍ h(log q)²/log(h log q). So M2 certifies a hit at polylog expected
count **exactly when the target density 1/h is ≥ 1/polylog**. The H = {1} case shows the converse. There h = φ(q)
and the guaranteed window is a power, P(a, q) ≤ (φ(q) log q)², even under GRH.

The polylog windows of M2 are therefore a feature of dense targets, not of hit polarity as such.

B2's per-trial target densities are not dense:
* In the d-form, |S_d|/d = τ((d + 1)/4)/d.
* In the C-form, the chance that 4Cp + 1 has a divisor ≡ −1 (mod 4C) is roughly τ(4Cp + 1)/φ(4C).
Both decay like a power of the trial parameter, and the moduli move with it. No single character mod a fixed q encodes
the event (FRONTIER B2, "tied modulus").

### 3.3 Function-field check for (M2-W) (Assessment, resting on `Z58_FFIELD.md` Cor 3.2 and §5)

In 𝔽_q[t] the RH-type input is a theorem (Weil; Bhowmick–Lê Thm 8 = Hsu Thm 2.1). Pointwise polylog-window M2
statements hold unconditionally: Thms 5–6 for primitive elements, and the same Corollary 4 gives small-degree
non-residues. Yet:
* (a) the T1-compatible ES analogue MS_q is **false** at a positive proportion of irreducibles of every fixed even
  degree once q is large (Cor 3.2, PROVED relative to Chebotarev);
* (b) at fixed q it is open, and "RH supplies equidistribution only in a range where avoiders still provably exist"
  (Z58_FFIELD §5).

Hence there is no route "RH-strength character information ⟹ (★)-type witness" that works uniformly in q. Any integer
argument whose arithmetic inputs are RH-strength statements about fixed characters attached to p would, if it had a
q-uniform function-field translation, prove a false statement.

This is a heuristic relativisation, not a theorem: an integer proof need not have a q-uniform translation. It is
consistent with ES not being known under GRH.

### 3.4 Squeezes: Lemma 1 (PROVED, elementary; a direct consequence of T1)

**Lemma 1.** Let 𝒲(n) be the set of (★) witnesses (u, B, C) at n. Let κ be any size function on witnesses, for
example d = 4uC − 1, C, u, min(u, B, C) or max(u, B, C). Put 𝒲_X(n) = {w ∈ 𝒲(n) : κ(w) ≤ X}. Then:
* (i) 𝒲_X(m²) = ∅ for every odd m and every X.
* (ii) Let 𝒩 be any set of n ≡ 1 (mod 24) that contains infinitely many odd squares, for example all n ≡ 1 (mod 24).
  Suppose that, for a function X(n) and an integer-valued G, the implication "𝒲_{X(n)}(n) = ∅ ⟹ n ≤ G" holds on all
  of 𝒩. Then this is impossible: it fails at every odd square m² ∈ 𝒩 with m² > G.

  So every squeeze certificate for (★) must use, in its "failure ⟹ divisibility" step, a property of n that fails at
  all but finitely many odd squares of 𝒩.

*Proof.* (i) By T1 (FRONTIER §3 B5: for n = m² and every u ≥ 1, n + u has no divisor ≡ −1 (mod 4u)), R(m²) = 0, so
𝒲(m²) = ∅. (ii) If m is odd and 3 ∤ m, then m² ≡ 1 (mod 24). So 𝒩 = {n ≡ 1 (24)} contains all such m², and by (i)
the hypothesis of the implication holds there for every window. The conclusion n ≤ G then fails for m² > G. ∎

*Reading (Assessment).* The known squeezes are input-blind:
* Chebyshev: if every prime ℓ ≤ X divides n ≥ 1, then n ≥ ∏_{ℓ≤X} ℓ.
* AKS Lemma 4.3: valid for every n ≥ 2.
* Sylvester–Schur.

Their failure event is a *conjunction of divisibilities* of an integer the theorem already holds (n, or ∏(nⁱ − 1)).
B2's failure event is a *conjunction of non-divisibilities*, and by Lemma 1 it is satisfied by an infinite natural set
of arbitrarily large inputs. A squeeze for B2 would need a step "p prime (or non-square) ⟹ an explicit integer is
divisible by many moduli".

The steps of that shape that I know are identities: Fermat (p | a^{p−1} − 1), Wilson, Mordell's identities. The
last are finite congruence menus, killed by B1. The only primality-sensitive input known to touch (★) is the quadratic
character (Lemma CT). Quantitatively, B1 (`POINTWISE_OMEGA13.md` Thm 5.1, PROVED modulo the stated inputs) already
bounds any multiplier-type certificate: the least Type II witness modulus exceeds exp(c(log p)^{1/4}(log log p)^{−1/4})
for infinitely many Mordell-hard primes. A Chebyshev-style polylog window for d is impossible for that reason too. In
finite range, the d_min record is 2 953 943 at p = 85 664 329 (`Z58_WITNESS.md` §2).

### 3.5 Cell map and the precise gap (Assessment)

Classify an existence statement at a prescribed input n by five features:
* **count**: power vs polylog;
* **modulus**: fixed per input (one character / one coset mod q(n)) vs moving with the witness;
* **polarity**: escape (avoid a sparse set of classes, or be non-divisible) vs hit (land in a sparse target);
* **object**: prescribed vs designed;
* **mechanism**: exact structure vs analytic.

| count | modulus | polarity | object | proved examples (verified rows) |
|---|---|---|---|---|
| power | any | any | prescribed | Tier D (Burgess, Linnik, Duke, Helfgott, Zaremba claims, Borwein–Choi) |
| polylog | fixed | escape | prescribed | squeezes A2–A4 (unconditional); M2 B1/B3 (GRH); M2-W A1 (unconditional in 𝔽_q[t]) |
| polylog | fixed | hit, target density ≥ 1/polylog | prescribed | M2 B2 under GRH (LLS Thm 1.4) |
| polylog | fixed | hit, target density = power | prescribed | **none**: least prime in AP at q(log q)^A is open even under GRH (H1) |
| polylog / O(1) | — | hit | prescribed, exact structure | Zagier, Thue, Fermat, Zsigmondy (A5–A8) |
| polylog | moving | hit | designed | Erdős 1956, Erdős–Tetali, Vu, Kolountzakis (C1–C3); explicit only at n^{c/log log n} (C4) |
| **polylog** | **moving** | **hit, power density** | **prescribed, analytic** | **none known. This is B2** |

**Gap statement (Assessment).** A first theorem of B2's kind would read: *for every sufficiently large prime p (in a
class), there exist w ∈ 𝒫(p) and d | N(p, w) with d ≡ a(w) (mod q(w)), where q(w) → ∞ with w; where the expected
number of (w, d) is (log p)^{O(1)}; where the statement is false on an explicit infinite set (the odd squares), so the
proof must use a non-local property of p; and where the witness is not produced by an identity, a thick extraction or
a squeeze.*

No theorem in any row of §2 has this shape, even conditionally. The fixed-modulus, power-density-target relaxation is
already open under GRH (H1), and the designed-object relaxation is open as soon as the object is required to be
explicit and polylog (H2). Of the four FRONTIER §4 hard screens, the gap statement contains T1 (via the explicit false
set) and the tied modulus (via q(w)). The other two are fixed p (pointwise) and 8/131 (the statement must be
numerator-4 specific).

## 4. Falsifier table (mandatory; one row per transfer attempt)

| transfer attempt | F1 odd squares | F2 C-even / numerator 8 | F3 composites | F4 known zeros | outcome |
|---|---|---|---|---|---|
| (S) squeeze, Chebyshev/AKS type | **kills** input-blind squeezes (Lemma 1: squares fail at every window) | n/a | n/a | n/a | dead as a class of input-blind arguments (PROVED); primality-sensitive squeezes are not excluded, but none is known except identities (B1) |
| (M2) GRH least non-residue ⟹ witness | passes (squares have no non-residue) | R₈ (numerator 8) zeros also have small non-residues; e.g. 131 is a non-residue mod 3 (131 ≡ 2 mod 3), yet 8/131 fails (FRONTIER §4 screen) | non-residue layer holds at composites with R = 0, e.g. 4545 = 3²·5·101 has (4545/7) = (2/7) = +1 but (4545/11) = (2/11) = −1 | **kills**: all 14 (★)-zero primes have n_p ≤ 23 (n_p = 7, 5, 13, 13, 7, 13, 23, 5, 23, 7, 13, 19, 11, 17), and R(p) = 0 is recomputed for p ≤ 10⁴ (`data/z63/precedent/qnr_zeros.txt`, CERTIFIED) | dead as a stand-alone mechanism. The layer is necessary (Lemma CT) but not sufficient |
| (M2) GRH coset hit (LLS Thm 1.4) | — | — | — | — | inapplicable: the target density is not ≥ 1/polylog and the modulus moves (§3.2) |
| (M2-W) Weil in 𝔽_q[t] | MS_q has T1 (Z58_FFIELD Lemma 1.2) | proxies only | composite zeros persist | **kills** the q-uniform version: positive-proportion irreducible zeros at fixed even degree (Cor 3.2) | dead as a q-uniform mechanism (Assessment §3.3) |
| (T) Zagier count congruence | an affine windmill on (★) sets would have to fail at squares | — | — | R(p)/2 parity is a fair coin (z52 §2.1, EVIDENCE) | screened earlier; non-affine thick windmills remain open (z52 ζ) |
| (T) Thue/Minkowski collision | — | — | — | — | B4: signed solutions only |
| (R) Zsigmondy primitive divisor | — | — | — | the prime-divisor subfamily fails at 94 primes < 10⁶ (PRIMITIVE_INTERSECTION) | dead for that family |
| (M4) random / derandomised | — | — | — | — | inapplicable: p is prescribed (C1, C3) |
| (I) explicit covering (JPSZ-type digits) | B1 Thm M: finite identity menus fail at square-mimicking points | — | — | — | B1. Unbounded digit loops form B1's E2 hatch (z52 α row); no construction is known |

The F2 row entry for 131: (131/3) = (2/3) = −1, so 3 is a non-residue. The claim that 8/131 has no Type I/II solution
with numerator 8 is the FRONTIER §4 screen, used as stated there and not recomputed here. The F3 entry for 4545 checks
only the Legendre symbols (4545 ≡ 2 mod 7 and mod 11). That 4545 is a zero of the Type II family is `Z58_WILDCARD.md`
(N_II(4545) = 0), as stated in the z58 brief.

## 5. Verdict, screens, proposed FRONTIER text

**Verdict: narrowed.** No HOT LEAD.
* *Found:* literal precedents in classes (S) and (M2-W). The second is new to the repository.
* *Shown:* neither transfers, by Lemma 1 (PROVED), the F4 computation (CERTIFIED) and the function-field check
  (Assessment relative to Z58_FFIELD Cor 3.2).
* *Not found:* no precedent of the needed kind (analytic, prescribed input, hit polarity, moving modulus, polylog
  count), even under GRH.
* *Calibrations:* the nearest open problems in the same cell (H1, H2) are open even with GRH or with full design
  freedom.

**FRONTIER §4 hard screens for the best "idea" (a squeeze or M2 transfer).**
* T1: fails for input-blind squeezes (Lemma 1); passes for M2.
* 8/131: M2 is numerator-blind, so fails.
* Tied modulus: M2 needs a fixed modulus, so fails.
* Fixed p: squeezes and M2 are pointwise, so pass.

**Proposed FRONTIER text** (§3, after the (J)94 table; do not apply here):
> *(z63, `Z63_PRECEDENT.md`.) Precedent hunt (Assessment; rows source-verified with theorem numbers).*
> * *Literal precedents.* Unconditional pointwise existence at polylog expected count without an identity occurs in
>   exactly two further classes, besides (T) and (R):
>   * (S) input-blind size squeezes: AKS Lemma 4.3, least prime non-divisor, Sylvester–Schur;
>   * (M2-W) RH-strength fixed-modulus character sums, unconditional only in 𝔽_q[t] (Bhowmick–Lê Thms 3, 5, 6 via
>     Weil).
> * *Why neither transfers.* (S) is barred for (★) by T1: no input-blind squeeze exists, since squares fail at every
>   window (Lemma 1, PROVED). (M2) yields only the non-residue layer: all 14 (★)-zero primes have n_p ≤ 23 (CERTIFIED).
>   In 𝔽_q[t], RH is a theorem and MS_q still fails at fixed degree for large q (Z58_FFIELD Cor 3.2).
> * *Target-density threshold.* Under GRH, hit events reach polylog windows only for target density ≥ 1/polylog (LLS
>   Thm 1.4). The least prime ≡ a (mod q) within q(log q)^A is open even on GRH (LLS Cor 1.2; KLM 2607.14515
>   Remark 2). Explicit additive bases with polylog r are open (JPSZ 2405.08650: n^{c/log log n}).
> * *Gap.* No theorem, even conditional, proves a pointwise hit of a power-density target with moving modulus at
>   polylog expected count for a prescribed input. B2 would be the first.

**Bottom line.** The brief asked whether any theorem proves pointwise existence at polylog expected count without an
identity.
* *Yes, literally, but only through:*
  * a size squeeze, whose failure event is a divisibility the theorem already holds;
  * an RH-strength sum for one fixed character, unconditional only over 𝔽_q[t];
  * or exact structure (windmill, lattice, cyclotomy).
* *None transfers to B2.* Squeezes are barred by T1 (Lemma 1). Character information stops at the non-residue layer:
  every known (★)-zero prime has a non-residue ≤ 23. The function-field model has RH and still fails.
* *No precedent of the needed kind exists, in any field, even conditionally.* That would be an analytic, pointwise
  lower bound for a hit of a power-density target with a moving modulus at polylog count. The closest fixed-modulus
  relative, the least prime ≡ a (mod q) within q(log q)^A, is open on GRH.
* *Implication* (Assessment). An ES proof would be the first theorem of its kind, or would have to come from exact
  structure. That is consistent with the campaign's spending rule, which funds only genuinely new mechanisms.

## 6. Review log

(pending: hostile reviewer subagent)
