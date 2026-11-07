# Z63_PRECEDENT — is there ANY theorem proving pointwise existence at polylog expected count without an identity? (wave z63, lane PRECEDENT)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results are internally reviewed only. Brief: `z52bbriefs/z63_lanes.md` §PRECEDENT.
Source excerpts (verbatim where quoted, URL, theorem numbers; access dates as recorded in each file, mostly 2026-11-07):
`data/z63/precedent/sources/*.txt`. Script: `scripts/z63_precedent_qnr_zeros.py` → `data/z63/precedent/qnr_zeros.txt`.

**Verdict: narrowed** — literature lane; no HOT LEAD. Literal precedents exist (answer (a) in the literal reading), in
five mechanism classes found by this survey; none transfers to B2, each failing at a named screen. No example of the
shape B2 needs was found (answer (b) in the sense that matters), stated as a gap in §3.5.

## 0. Bottom line

1. **Literal precedents exist** (Assessment, on the verified rows of §2, Tier A). Read literally, the brief's criteria
   are (P1) pointwise, (P2) polylog or bounded expected count, (P3) no identity, (P4) unconditional. Among the results
   reviewed, the rows that pass them use these mechanisms:
   * **(Sv) sieve lower bound for an escape event.** Iwaniec's Jacobsthal bound j(m) ≪ (ω(m) log ω(m))² (1978, V2 via
     Costello–Watts arXiv:1306.1064). Every prescribed interval of that length contains an integer coprime to a
     prescribed m. This was raised by the hostile reviewer, not found by my own search.
   * **(S) size/valuation squeeze.** AKS Lemma 4.3 (V); the least prime not dividing n (V).
   * **(M2-W) RH-strength character sums at one fixed modulus, made unconditional by Weil in 𝔽_q[t].** Shoup (1992) and
     Shparlinski (1990) give poly(n)-size sets containing a primitive element of 𝔽_{qⁿ} for small q. Bhowmick–Lê
     (arXiv:1412.7373, V) show that the monic polynomials of degree ∼ C log_q n contain one.

   Structural comparators — (T) Zagier's windmill and Thue/Minkowski; (R) Zsigmondy and r₂(p) = 8 — are what the brief
   calls "algebraic" and are not counted as passes. Over ℤ, (M2) at polylog windows is available only under GRH.
2. **None of these transfers to B2.** Each fails at a named screen (§3, §4).
   * **(Sv) Jacobsthal-type sieve.** The sifting classes are fixed per prime ℓ | m. B2's good events have moduli tied
     to the candidate (FRONTIER B2). A sieve driven by local densities is also T1-blind: at a square in the same
     residue classes the local data agree and R = 0. That is the closed "low-conductor universality" item (z53 brief).
   * **(S) squeezes.** No input-blind squeeze can work, because odd squares fail in every window (Lemma 1, PROVED, a
     direct consequence of T1).
   * **(M2) under GRH.** It supplies a small non-residue. Under GRH, "small non-residue ⟹ witness for large p" is
     equivalent to ES (z52 row 11), so the M2 step adds no forcing. Finite check (CERTIFIED): all 14 (★)-zero primes
     ≤ 10¹⁰ have n_p ≤ 23. That refutes only the threshold-free implication, not an eventual one.
   * **(M2-W) Weil in 𝔽_q[t].** RH is a theorem there, yet the T1-compatible analogue MS_q has no positivity argument
     with a q-independent degree threshold. A positive proportion of irreducibles of each fixed even degree fail for
     large q (`Z58_FFIELD.md` Cor 3.2, PROVED relative to Chebotarev). At fixed q it is open.
3. **No example of B2's shape was found** (Assessment; a statement about the results reviewed, not a theorem). No
   result reviewed, unconditional or under GRH, proves a pointwise **hit** of a target whose per-trial density decays
   like a power, with a modulus that moves with the trial, at polylog expected count. Calibrations in that
   neighbourhood are open:
   * Least prime ≡ a (mod q) ≤ q(log q)^A. Heath-Brown's conjecture is open; GRH gives (φ(q) log q)² (LLS Cor 1.2, V);
     Kandhil–Languasco–Moree (KLM) arXiv:2607.14515 Remark 2 says their GRH + pair-correlation method "does not bring
     us closer" (V).
   * An explicit additive basis with r(n) ≤ polylog is open. The best explicit result is n^{c/log log n} (Jain–Pham–
     Sawhney–Zakharov (JPSZ) arXiv:2405.08650 Thm 1.1, V). Erdős's random set does reach r ≍ log n, but only for a
     *chosen* set.
4. **The gap** (§3.5). A theorem of B2's shape would assert, for every large prime p, a divisor of a specified integer
   N(p, w) in a residue class whose modulus moves with w, at polylog expected count, false on an explicit infinite set
   (the odd squares). Every result reviewed relaxes at least one of these features: power count, fixed modulus, escape
   polarity, designed object, or exact algebraic structure.

## 1. Precise question, and why it is not already closed

**Definition (literal precedent).** A theorem T passes (P1)–(P4) if:
* (P1) for **every** sufficiently large input n in an infinite natural class 𝒩, it asserts W(n) ≠ ∅. "Almost all n",
  averages, "infinitely many n", and statements about a *chosen* object do not count.
* (P2) the natural expected size of W(n) is (log n)^{O(1)} or O(1), where n is the size of the input (for 𝔽_{qⁿ}, the
  field size N = qⁿ; for Jacobsthal, m). If T confines W(n) to a window, the expected count is taken inside the window
  T actually guarantees.
* (P3) the proof does not produce the witness from an algebraic identity or parametrisation.
* (P4) T is unconditional.

**Target (B2).** At a prime p ≡ 1 (24): some C ≥ 1 and some d | 4Cp + 1 with d ≡ −1 (mod 4C).
* Expected count ≍ log²p (FRONTIER §2.2).
* Every witness d has a prime factor ℓ with (ℓ/p) = −1 (FRONTIER §3 B5, Lemma CT).
* The search box is O(p²) (B-fin).
* d-form (`Z58_WITNESS.md` §1): some d ≡ 3 (4) has (−p mod d) | (d + 1)/4. So p mod d hits a target S_d of size
  τ((d + 1)/4). The per-trial target density τ((d + 1)/4)/d decays like a power, and the modulus d is the trial.

**Prior work** (not redone):
* `DETERMINISTIC_EXISTENCE.md` (O168).
* `B2_ACROSS_FIELDS.md` ((J)94, the M1a/M1b/M2–M5 table in FRONTIER §3).
* `BRAINSTORM/s9_lower_tail_literature.md` ((J)103).
* `BRAINSTORM/z52_deep_thin_pointwise_opus.md` (40-row catalogue, (T)/(R) taxonomy).
* `Z53_LIT.md` §6.4 and `Z58_LIT.md` §2.5.
* The z52b brainstorms that name the Jacobsthal analogy as an untested idea: `BRAINSTORM/z52b_free_fable.md` item 139
  and `z52b_free_opus.md` item 263.

Those verdicts are Assessments, and several rows were **NOT ACCESSED** (z52 §4: Burgess, Bach, Sylvester–Schur, the
thin-basis literature). **New here:**
* the brief's candidate list, verified at theorem-number level (§2);
* the (Sv) and (M2-W) rows, which are literal precedents, with the transfer screens of §3–§4;
* Lemma 1 (T1 bars input-blind squeezes);
* a reading of LLS Thm 1.4 as a target-density calibration;
* the explicit-basis calibration (JPSZ);
* a cell map and gap statement.

## 2. Ranked table

**Verification key.**
* **V**: statement read in the source, by me or by a research subagent with a saved excerpt. Rows marked ✔ I re-read
  myself from the PDF; LLS Thm 1.4 was checked visually.
* **V2**: read in a later paper that restates it (named).
* **R**: verified earlier in the repository (file named).
* **NA**: not accessed.
* "Count" is the expected witness count, at one input, inside the window the theorem guarantees. Inferred counts are
  marked "(inferred)".

Ranking runs from literal passes (Tier A) to structural comparators, conditional results, designed objects,
power-count, non-pointwise, tools, failures and open problems. Within a tier, structural similarity to B2 breaks ties:
hit polarity, moving modulus, divisors of a specified integer.

### Tier A — literal passes of (P1)–(P4)

| # | statement (source, theorem no.) | ver. | count | mechanism | transfer to B2 |
|---|---|---|---|---|---|
| A1 | **Jacobsthal (Iwaniec 1978).** g(n) ≤ X(k log k)², k = ω(n), where g(n) is "the smallest number Q such that every sequence of Q consecutive integers contains an integer coprime to n". Source: Costello–Watts arXiv:1306.1064 Intro, citing Iwaniec, Demonstratio Math. 11 (1978) 225–231 | ✔V2 | L·φ(m)/m with L ≍ (ω log ω)², i.e. ≍ ω² log ω: polylog in m (inferred) | **Sv**: lower-bound sieve; escape event (avoid 0 mod ℓ, ℓ \| m); fixed sifting classes; prescribed interval | **Fails** at the tied modulus and at T1 (§3.4 b): B2's good set in the candidate variable is not the complement of fixed classes, and sieve main terms are local, hence equal at squares |
| A2 | **AKS Lemma 4.3.** "There exist an r ≤ max{3, ⌈log⁵ n⌉} such that o_r(n) > log² n." Proof: the least r not dividing n^{⌊log B⌋}·∏_{i ≤ log²n}(nⁱ − 1), via lcm(1..m) ≥ 2^m (Lemma 3.1). Agrawal–Kayal–Saxena, Annals 160 (2004); author PDF v6 | ✔V | existence only; candidates r ≤ log⁵ n, so the window is polylog | **S** (input-blind squeeze) | **Fails**: Lemma 1 |
| A3 | Least prime not dividing n: a(n) < (1 + ε) log n for n > N(ε) (OEIS A053669 %F; primorial size) | V | ≍ log n/log log n | **S** (input-blind) | as A2 |
| A4 | **𝔽_q[t], (M2-W).** Shoup, Math. Comp. 58 (1992): a poly-time deterministic subset of GF(pⁿ) containing a primitive root for p = n^{O(1)}, no hypothesis (abstract, via `hunt_primitive_root.txt`). Bhowmick–Lê arXiv:1412.7373: "we show that the simple set of all monic polynomials of degree d ∼ C log_q n is guaranteed to contain a primitive element. This statement as it is, is not new because of the above result of Shoup." Their character-sum Thm 3 ("Our result is unconditional") rests on Thm 8 (Hsu Thm 2.1; Effinger–Hayes), i.e. Weil. Their density Thms 5–6 carry explicit parameter conditions (Thm 6 needs ε_{q,d,r,n} below c/(ω(N−1)²(log ω(N−1) + 1)²)) that are not reproduced here | ✔V (Bhowmick–Lê); V (Shoup abstract) | q^d = poly(n) candidates, polylog in N = qⁿ | **M2-W**: fixed modulus, RH-strength sums (Weil); escape (primitive = in no maximal subgroup) | **Fails** as a q-independent-threshold mechanism (`Z58_FFIELD.md` Cor 3.2); open at fixed q (§3.3) |

### Tier A′ — structural comparators (the brief's "algebraic" class; not counted as passes)

| # | statement | ver. | count | mechanism | transfer |
|---|---|---|---|---|---|
| A5 | Zagier, AMM 97 (1990) 144: an involution on S = {(x, y, z) ∈ ℕ³ : x² + 4yz = p} has exactly one fixed point | R (z52 row 1) | r₂(p) = 8 | **T** + count congruence on a thick set | screened: every (★) level count is even, and R(p)/2 behaves like a fair coin on samples (z52 §2.1, EVIDENCE); finite affine windmill menus are barred (INVOLUTION_ES2 Thm 5.1) |
| A6 | Thue/Brillhart, Minkowski: p = x² + y² | NA (z52 row 2) | O(1) | **T** (collision, symmetric target) | B4: signed solutions; ES's target −1 is not the identity |
| A7 | Bang–Zsigmondy; Bilu–Hanrot–Voutier | R (z45_recent_pointwise_tools) | ≥ 1 (no count model) | **R** (cyclotomic) | prime-divisor (★) subfamily fails at 94 primes < 10⁶ (PRIMITIVE_INTERSECTION, CERTIFIED there) |
| A8 | r₂(p) = 8; one class per genus | R (z52 β′) | O(1) | **R** (exact multiplicative count) | R(p) is not multiplicative; fixed-level identities fail T1 ((J)7) |
| A9 | Sylvester–Schur: for n > k, one of n, …, n + k − 1 has a prime factor > k (Erdős 1934; the stronger Erdős 1955 Thm 1 bounds the number of consecutive integers needed) | V (subagent excerpt) | not sparse | **S** (valuation count) | as A2 |

### Tier B — conditional M2 over ℤ (fail P4)

| # | statement | ver. | count | mechanism | transfer |
|---|---|---|---|---|---|
| B1 | **LLS arXiv:1309.3595.** Cor 1.1 (GRH): for prime q ≥ 5, the least QNR is < (log q)². Thm 1.2 (GRH): the least prime not in H, index h > 1, is < (α(h) + o(1))(log q)², α(2) = 0.8. Bach, Math. Comp. 55 (1990), abstract: under ERH a compositeness witness ≤ 2 log²m (internal theorem number NA) | ✔V (LLS); V (Bach abstract) | polylog | M2, escape | only the non-residue layer (§3.2, §4) |
| B2 | **LLS Thm 1.4** (GRH, q ≥ 20000, h > 1): the least prime p in a coset aH satisfies p ≤ 10⁹ or p ≤ ((h − 1) log q + 3(h + 1) + (5/2)(log log q)²)². With H = {1}: P(a, q) ≤ (φ(q) log q)² (Cor 1.2); Bach–Sorenson (1.1)–(1.2) | ✔V (Thm 1.4 visually) | ≍ h(log q)²/log(h log q) in that window: polylog when h ≤ polylog | M2, hit | §3.2: no guarantee from this bound at power-density targets; B2's moduli also move |
| B3 | Shoup (GRH): least primitive root g(p) ≪ ω(p−1)⁴(log ω(p−1) + 1)⁴ log²p (via Moree, arXiv:math/0412262v2 §27, z52 row 14) | V2 | polylog | M2 | as B1 |

### Tier C — designed or random objects (fail P1: the object is chosen, not prescribed)

| # | statement | ver. | count | mechanism | transfer / calibration |
|---|---|---|---|---|---|
| C1 | Alon–Spencer, *The Probabilistic Method* 2nd ed. §8.6: "Theorem 8.6.2 [Erdős (1956)] There is a set S … c₁ ln n ≤ f(n) ≤ c₂ ln n." Proof: Pr[x ∈ S] = min(10√(ln x/x), 1), Chernoff, Pr[A_n] < n^{−1.1}, Borel–Cantelli. Erdős 1954 (Acta Szeged 15): 0 < f(n) < c₁ log n, "We will not be able to construct our sequences explicitely" | V2 / V | ≍ log n | M4: random + concentration + BC | p is forced; there is no randomness to choose (prob_lll_fixed_p) |
| C2 | Erdős–Tetali (RSA 1 (1990)) via Alon–Spencer Thm 8.6.3; Vu (Duke 105 (2000)) via Vu RSA 21 (2002) Thm 7.4: thin Waring bases with R = Θ(log n) | V2 | ≍ log n | M4 + Janson / Kim–Vu | as C1 |
| C3 | Kolountzakis (Discrete Math. 145 (1995)): deterministic poly-time enumeration of an Erdős basis "by derandomizing a probabilistic proof" | V2 | ≍ log n | M4, derandomised | needs freedom to choose: at fixed p the conditional expectation ≥ 1 is R(p) ≥ 1 (z52 λ) |
| C4 | **JPSZ arXiv:2405.08650v1 Thm 1.1:** "There is an explicit set A ⊂ ℕ … for every n ∈ ℕ, we have 1 ≤ σ_A(n) ≤ Cn^{c/log log n}." "Explicit" means membership testable in (log n)^{O(1)} time (so C3 is not explicit in their sense). Also: "We believe obtaining an explicit construction achieving σ_A(N) ≤ exp((log N)^ε) or better would be interesting." Under "strong number theoretic conjectures", numbers within O((log n)^{O(1)}) of a square work | ✔V | upper bound n^{c/log log n}; a polylog explicit construction is not known | **I** (generalised-base digits; Ruzsa's A_p + A_p = ℤ/p²; every n covered by construction) | calibration: pointwise existence for an explicit set comes from an exact covering, and the proved upper bound is super-polylog |
| C5 | Thin square bases. Erdős–Nathanson (1981): random squares, B(x) ∼ c x^{1/3+ε}, basis of order 4. Wirsing (Analysis 6 (1986)): for h ≥ 4 a squares basis of order h with B(x) < c(x log x)^{1/h} (probabilistic). Spencer (1996): short proof for h = 4. Choi–Erdős–Nathanson (PAMS 79 (1980)): explicit, finite range, \|A\| < c n^{1/3} log n | V2 (Nathanson 1986/1987; Vu 2002 §7.2) | not quoted (a random-model count for Wirsing would be ≍ log n; not a quoted theorem) | M4 | as C1 |
| C6 | Pilatte arXiv:2303.09659v3 Thm 5.4: a Sidon asymptotic basis of order 3 exists a.s., via Lemma 5.3, P(m ∉ 3S) ≤ exp(−m^{3c−1−o(1)}) with c = 0.35 | ✔V | the proof's restricted expected representation count is m^{3c−1+o(1)} = m^{0.05+o(1)} (eq. (9) and the trial probabilities), a power (inferred) | M4 + Sawin's 𝔽_q[t] bound | calibration |

### Tier D — pointwise and unconditional, power count in the guaranteed window (fail P2)

| # | statement | ver. | count | mechanism |
|---|---|---|---|---|
| D1 | Burgess, Mathematika 4 (1957), Thm 2: least QNR = O(p^a) for any fixed a > 1/(4√e) | V | power | character-sum amplification |
| D2 | Linnik P(a, q) ≪ q^L (L = 5.2 per LLS; ≤ 5 per KLM; sources disagree on attribution); Chang (2014) Cor 11: P < q^{12/5+o(1)} for smooth q | V2 | power | zero-density / log-free |
| D3 | Burthe, Acta Arith. 80 (1997): w(n) = O_ε(n^{1/(6√e)+ε}) for odd composite n (p. 313; Cor 4.3, Thms 4.6–4.7) | V | power | Burgess-type |
| D4 | Filaseta–Trifonov, JLMS 45 (1992): (x, x + c x^{1/5} log x] contains a squarefree integer | V2 (arXiv:2211.09975) | power | lattice points near curves |
| D5 | Duke, Invent. 92 (1988), Thm 1 (squarefree n in admissible classes; ineffective); Duke–Schulze-Pillot, Invent. 99 (1990) | V / V2 | n^{1/2±ε} | half-integral weight + Siegel |
| D6 | Linnik (dispersion): every large n = p + x² + y² (Assing–Blomer–Li arXiv:2005.13915 Thm 1.2, count ≍ n/log n); Helfgott ternary Goldbach | V2 / V | power | dispersion / circle method |
| D7 | Borwein–Choi, Exp. Math. 9 (2000): xy + yz + zx represents all n except a finite list and at most one more (none more under GRH) | V2 (OEIS A025052) | power (class-number size; inferred) | class groups, ineffective |
| D8 | Zaremba claims (Shkredov arXiv:2603.14116, Zhang arXiv:2605.02518, unrefereed); MMS arXiv:2212.14646; Niederreiter for q = 2^α, 3^α, 5^α | R (Z53_LIT §5(g)) / V2 | power | expansion / explicit |
| D9 | Ramaré–Walker Thm 1.1; Heath-Brown–Puchta (2 primes + 13 powers of 2); Zaharescu ‖n²α‖ ≪ N^{−4/7+ε} | R (z52) / V2 | power | dense generating set; circle method |

Transfer of every Tier D row: B3/B-fin. ES's whole O(p²) box has expected count ≍ log²p, so there is no box to
enlarge.

### Tier E — not pointwise for a prescribed input (fail P1)

| # | statement | ver. | why not |
|---|---|---|---|
| E1 | Ford, Annals 168 (2008), Thm 1(v): H(x, y, 2y) ≍ x/((log y)^δ(log log y)^{3/2}) (in its stated range of y) | V | density; false at primes |
| E2 | Friedlander–Iwaniec, Annals 148 (1998), Thm 1; Heath-Brown, Acta 186 (2001) | V | asymptotics |
| E3 | Heath-Brown, Acta Arith. 155 (2012): n² + 1 squarefree, N(x) = c₀x + O(x^{7/12+ε}) | V | density |
| E4 | Heath-Brown 1986 (Artin): at most two exceptional primes q | R (z52 row 15) | infinitely many p |
| E5 | Hough, Annals 181 (2015), Thm 1; BBMST arXiv:1811.03547 Thm 1.1 (uncovered density ≥ e^{−4C}/2) | V | they show some integer is uncovered; dually, sterile sets are non-empty (the B1 direction) |
| E6 | Tao, Discrete Analysis 2016:1, Thm 1.1 (EDP) | V | unquantified; witnesses not thin |

### Tier F — existence tools (guarantee ≥ 1 given structure)

| # | statement | ver. | relevance |
|---|---|---|---|
| F1 | Combinatorial Nullstellensatz (Alon, CPC 8 (1999), Thm 1.2) | V | needs a nonzero top coefficient |
| F2 | Chevalley–Warning, Warning II, Ax–Katz, restricted variables (arXiv:1404.7793 Thms 1.1, 1.2) | V2 | z52 §2.1 Lemma 2.1(c): the cubic (★) encoding has #vars = degree |
| F3 | Alon–Füredi (Clark–Forrow–Schmitt Thm 2.3, citing [AF93, Thm 5]); Schanuel / Brink (congruences mod p^v) | V2 | a lower bound once one non-zero exists, or congruences only |
| F4 | LLL (Erdős–Lovász 1975); Moser–Tardos, JACM 57 (2010), Thms 1.1–1.2 | V | needs a free random object |
| F5 | Szemerédi–Trotter, Beck | V2 | upper bounds / linear counts |
| F6 | Pila–Wilkie (Duke 133 (2006), theorem number unverified); Pila–Shankar–Tsimerman arXiv:2109.08788 Thm 1.1 | V2 / V | upper bounds; existence by power-vs-T^ε contradiction (finiteness) |
| F7 | Entropy decrement (Tao arXiv:1509.05422 §§1, 3) | V | pigeonholes a scale; averaged statements |

### Tier G — failure-side calibrations (repo: s9, z52 rows 34–38)

* Crocker, PJM 36 (1971): infinitely many odd n ≠ p + 2^a + 2^b.
* Pan: ≫ x^{1−ε} exceptions.
* Ghosh–Sarnak, Markoff: (log k)² average, power-many failures.
* Goldbach's other conjecture: 5777, 5993.

### Tier H — open problems near B2's cell

| # | problem | status |
|---|---|---|
| H1 | least prime ≡ a (mod q) ≤ q(log q)^A (a hit, fixed modulus, polylog count) | open under GRH as far as found. LLS Cor 1.2 gives (φ(q) log q)². KLM arXiv:2607.14515v1 Thm 5 (GRH + pair correlation) gives φ(q) exp(B(log q)^A), and Remark 2 says it "does not bring us closer to establishing Heath-Brown's conjectural estimate p(k) ≪ k(log k)²" (✔V) |
| H2 | explicit basis of order 2 with σ_A ≤ polylog | open; best is n^{c/log log n} (JPSZ ✔V) |
| H3 | squarefree integer in every (x, x + (log x)^A] | open; Filaseta–Trifonov give x^{1/5} log x |
| H4 | pointwise lower bound ≥ 1 for #{d \| N : d ≡ a (mod q)}, q ≥ N^ε | none found; Lenstra 1984 and CHN give upper bounds (Z58_LIT §2.5). Absence of a find, not a proof of absence |
| H5 | unconditional polylog QNR / primitive root | open; Graham–Ringrose: n_p ≫ log p log log log p infinitely often (V2) |

## 3. Analysis

### 3.1 How the literal passes get existence (Assessment)

Each Tier A row is of one of three kinds:
* **A sieve or squeeze for an escape event.** The bad events are congruence conditions with moduli fixed by the input
  (primes dividing m; r | n^i − 1). Survival is certified by a lower-bound sieve (A1) or by size (A2–A3).
* **An RH-strength explicit formula for one fixed modulus (A4).** Unconditional only in 𝔽_q[t].
* **Not** a lower bound for a sparse **hit** count with moving moduli at a prescribed input, which is what B2 needs.

The earlier (T)/(R) taxonomy (z52) is incomplete as a classification of literal passes: it lacks (Sv), and does not
list (M2-W) as unconditional. "Classes represented in this survey" is the honest scope. I make no exhaustiveness claim.

### 3.2 Hit polarity under GRH: what LLS Thm 1.4 does and does not give (Assessment)

LLS Thm 1.4 bounds the least prime in a coset of index h by X_h := ((h − 1) log q + 3(h + 1) + (5/2)(log log q)²)²
(GRH, q ≥ 20000, unless p ≤ 10⁹). The heuristic number of primes in the coset up to X_h is
Li(X_h)/h ≍ h(log q)²/log(h log q). This **particular guaranteed window** therefore has polylog expected count when h
is polylog, and gives no polylog-count guarantee otherwise.

For H = {1} (h = φ(q)) the best GRH guarantee found is P(a, q) ≤ (φ(q) log q)² (LLS Cor 1.2), a power window. This is
a weakness of the known bounds, not a proven limitation of GRH methods; KLM Remark 2 says the same of their stronger
hypotheses.

B2's per-trial target densities decay like a power: τ((d + 1)/4)/d in the d-form. In the C-form, the heuristic
chance that 4Cp + 1 has a divisor ≡ −1 (mod 4C) is roughly τ(4Cp + 1)/φ(4C). The moduli move with the trial, and no
single character mod a fixed q encodes the event (FRONTIER B2, tied modulus).

### 3.3 Function-field check for (M2-W) (Assessment, on `Z58_FFIELD.md` Cor 3.2 and §5)

In 𝔽_q[t], RH-type input is a theorem (Bhowmick–Lê Thm 8 = Hsu Thm 2.1), and A4 holds for small q and growing degree.
For the T1-compatible analogue MS_q, `Z58_FFIELD.md` proves (relative to Chebotarev) that at each fixed even degree a
positive proportion of irreducibles fail once q is large. So **no positivity argument with a degree threshold
independent of q exists** (Cor 3.2). The source expressly does not exclude fixed-q arguments, or thresholds N₀(q) that
grow with q.

The regime of A4 (fixed q, degree → ∞) is exactly where MS_q is open: "RH supplies equidistribution only in a range
where avoiders still provably exist" (Z58_FFIELD §5(d)). The honest reading: having RH as a theorem has not, so far,
produced a single (★)-type event at one P in 𝔽_q[t]. That is a statement about current knowledge, not a barrier
theorem.

### 3.4 Transfer screens

**(a) Squeezes: Lemma 1 (PROVED, elementary; a direct consequence of T1).** Let 𝒲(n) be the set of (★) witnesses
(u, B, C) at n. Let κ be any size function on witnesses, e.g. d = 4uC − 1, C, u, min(u, B, C) or max(u, B, C). Put
𝒲_X(n) = {w ∈ 𝒲(n) : κ(w) ≤ X}.
* (i) For every odd m and every X ≥ 1, 𝒲_X(m²) = ∅.
* (ii) Let 𝒩 ⊆ {n ≡ 1 (mod 24)} contain infinitely many odd squares, let X: 𝒩 → [1, ∞), and let G be a fixed
  constant. The implication "𝒲_{X(n)}(n) = ∅ ⟹ n ≤ G" cannot hold on all of 𝒩. It fails at every odd square
  m² ∈ 𝒩 with m² > G.

*Proof.* (i) T1 (FRONTIER §3 B5: for n = m² and every u ≥ 1, n + u has no divisor ≡ −1 (mod 4u)) gives R(m²) = 0, so
𝒲(m²) = ∅. (ii) By (i) the premise holds at each m² ∈ 𝒩, and the conclusion fails once m² > G. If 3 ∤ m and m is
odd, then m² ≡ 1 (mod 24), so 𝒩 = {n ≡ 1 (24)} qualifies. ∎

*Consequence (logical).* An eventual squeeze for (★) cannot have all its premises valid at arbitrarily large odd
squares. Some premise must use a property of n that fails at all but finitely many squares of 𝒩, such as primality,
non-squareness, or a quadratic-character condition.

*Reading (Assessment).* The known squeezes A2, A3, A9 are input-blind: their premises hold at every n ≥ 1 or 2. Their
failure event is a conjunction of divisibilities of an integer the theorem already holds. B2's failure event is a
conjunction of non-divisibilities and holds at all odd squares. The primality-sensitive divisibility statements I know
of are identities (Fermat, Wilson) or finite identity menus (Mordell), and the latter are barred by B1. B1's
quantitative form (`POINTWISE_OMEGA13.md` Thm 5.1, PROVED modulo its stated inputs) gives Type II witness moduli
> exp(c(log p)^{1/4}(log log p)^{−1/4}) for infinitely many Mordell-hard primes. So no polylog-window certificate of the
multiplier type exists. In finite range, the d_min record is 2 953 943 at p = 85 664 329 (`Z58_WITNESS.md` §2).

**(b) Sieve (Jacobsthal type) (Assessment).** In A1 the candidate variable k runs over an interval, and the bad events
"ℓ | n + k" are one fixed class per prime ℓ | m. In B2, take the trial variable u (or C). Then "u good" means p + u has
a divisor f ≡ −1 (mod 4u). For a fixed f this picks out the finite set {u ≡ −p (mod f), u | (f + 1)/4}, not a residue
class: the modulus is tied to the candidate. This is the obstruction already noted in z52b_free_opus item 263.

Moreover, a lower-bound sieve's main term is built from local densities of the good set in progressions. At an odd
square m² lying in the same residue classes as p modulo every modulus used, those local data coincide, yet R(m²) = 0.
So the remainder terms must carry a square-sensitive input. Remainders uniform over rough n cannot do this: that is the
closed "low-conductor universality" item (z53 brief). B2 is also a **hit** of a sparse good set: its density among
u ≤ X is ≈ (log p)(log X)/X (heuristic). Jacobsthal certifies **escape** into a set of density φ(m)/m ≫ 1/log ω(m).

**(c) M2 under GRH.** Under GRH every large p has a non-residue ≤ (log p)². "Small non-residue ⟹ (★) witness for all
large p" is then equivalent to (★)-ES for large p (z52 row 11). The M2 step contributes no forcing; all the content is
in the implication. The F4 data (§4) refute only the threshold-free version.

## 3.5 Cell map and the gap (Assessment; describes the results reviewed)

Features of an existence statement at a prescribed input:
* **count**: power vs polylog;
* **modulus**: fixed per input vs moving with the trial;
* **polarity**: escape (avoid fixed classes / non-divisibility) vs hit (land in a sparse target);
* **object**: prescribed vs designed;
* **mechanism**: exact structure vs analytic.

| count | modulus | polarity | object | examples among the rows of §2 |
|---|---|---|---|---|
| power | any | any | prescribed | Tier D |
| polylog | fixed | escape | prescribed | A1 Jacobsthal (sieve), A2–A3 (squeeze), A4 (Weil, 𝔽_q[t]); B1, B3 (GRH) |
| polylog | fixed | hit, target density ≥ 1/polylog | prescribed | B2 / LLS Thm 1.4 (GRH) |
| polylog | fixed | hit, power-density target | prescribed | none found (H1 open, including under GRH as far as found) |
| O(1) / polylog | — | hit | prescribed, exact structure | A5–A8 |
| polylog | — | hit | designed | C1–C3; explicit only at n^{c/log log n} (C4) |
| **polylog** | **moving** | **hit, power density** | **prescribed, analytic** | **none found: this is B2's cell** |

**Gap statement.** A theorem of B2's shape would read: *for every sufficiently large prime p (in a class), there exist
w ∈ 𝒫(p) and d | N(p, w) with d ≡ a(w) (mod q(w)), where q(w) → ∞ with w; the expected number of (w, d) is
(log p)^{O(1)}; the statement is false on an explicit infinite set (here the odd squares, so the proof must use a
property of p that distinguishes it from squares); and the witness is not produced by an identity or a thick
extraction.*

No row of §2 has this shape. The fixed-modulus relaxation with a power-density target (H1) is unresolved even under
GRH in the sources found. The designed-object relaxation is unresolved once the object must be explicit with polylog
counts (H2).

This does **not** say an ES proof must establish this shape. ES need not go through (★), and a proof could come from
exact structure. It says that if it does go through B2 analytically, no result reviewed here is a template.

## 4. Falsifier table (mandatory; one row per transfer attempt)

| transfer attempt | F1 odd squares | F2 C-even / numerator 8 | F3 composites | F4 known zeros | outcome |
|---|---|---|---|---|---|
| (S) input-blind squeeze (AKS / Chebyshev type) | **bars it**: squares fail in every window (Lemma 1) | n/a | n/a | n/a | the input-blind class is excluded (PROVED). Primality-sensitive squeezes are not excluded, but none is known apart from identities |
| (Sv) Jacobsthal sieve on the trial variable u or C | local main terms agree at squares in the same classes; remainders must be square-sensitive (low-conductor universality, closed) | — | — | — | blocked at T1 and at the tied modulus (§3.4 b; Assessment) |
| (M2) GRH: small non-residue ⟹ witness | passes (squares have no non-residue) | numerator-blind: 131 has the non-residue 2 ((2/131) = −1, 131 ≡ 3 mod 8), yet 8/131 has no unit-fraction solution (FRONTIER §1) | the layer holds at non-square composite zeros: 4545 ≡ 2 (mod 11), so (4545/11) = −1, yet N_II(4545) = 0 (`Z58_WILDCARD.md`) | all 14 (★)-zero primes ≤ 10¹⁰ have n_p ≤ 23: 7, 5, 13, 13, 7, 13, 23, 5, 23, 7, 13, 19, 11, 17. R(p) = 0 is recomputed here for p ≤ 10⁴; larger zeros are the inherited certificate (FRONTIER §2.1). `qnr_zeros.txt` | refutes the threshold-free implication. The eventual implication is ES-strength (§3.4 c), so the M2 step adds no forcing |
| (M2) GRH coset hit (LLS Thm 1.4) | — | — | — | — | the known bound gives no polylog guarantee at power-density targets, and the modulus moves (§3.2) |
| (M2-W) Weil in 𝔽_q[t] | MS_q has T1 (Z58_FFIELD Lemma 1.2) | proxies only | composite zeros persist | positive-proportion irreducible zeros at fixed even degree for large q (Cor 3.2) | no q-independent-threshold mechanism; fixed q open (§3.3) |
| (T) Zagier count congruence | an affine windmill would have to fail at squares | — | — | R(p)/2 parity behaves like a coin (z52 §2.1, EVIDENCE) | screened; non-affine thick windmills open (z52 ζ) |
| (T) Thue/Minkowski collision | — | — | — | — | B4: signed solutions |
| (R) Zsigmondy primitive divisor | — | — | — | the prime-divisor subfamily fails at 94 primes < 10⁶ | dead for that family |
| (M4) random / derandomised | — | — | — | — | inapplicable: p is prescribed |
| (I) explicit covering (JPSZ-type digits) | B1 Thm M: finite identity menus fail at square-mimicking points | — | — | — | B1. Unbounded digit loops form the E2 hatch (z52 α); no construction known |

## 5. Verdict, screens, proposed FRONTIER text

**Verdict: narrowed. No HOT LEAD.**
* *Literal precedents found:* (Sv), (S), (M2-W). (Sv) came from the reviewer; (M2-W) is new to the repository's
  catalogue.
* *Transfer:* each is shown not to transfer in its natural form — Lemma 1 (PROVED), the sieve and M2 screens
  (Assessment), the 𝔽_q[t] check (relative to Z58_FFIELD Cor 3.2).
* *B2's shape:* no example found among the results reviewed, including under GRH. The nearest open relatives (H1, H2)
  are unresolved even with GRH or with full design freedom (H2 when explicit).

**FRONTIER §4 hard screens for the best transfer candidates.**
* T1: fails for input-blind squeezes (Lemma 1) and for local-density sieves; M2 passes.
* 8/131: M2 and sieves are numerator-blind, so they fail.
* Tied modulus: Jacobsthal and M2 need fixed moduli, so they fail.
* Fixed p: all three are pointwise, so they pass.

**Proposed FRONTIER text** (§3, after the (J)94 table; not applied here):
> *(z63, `Z63_PRECEDENT.md`; Assessment, rows source-verified.)* Unconditional pointwise existence at polylog expected
> count without an identity does occur, in the results reviewed, through:
> * (Sv) lower-bound sieves for escape events: Iwaniec's Jacobsthal bound j(m) ≪ (ω log ω)²;
> * (S) input-blind squeezes: AKS Lemma 4.3, least prime non-divisor;
> * (M2-W) RH-strength fixed-modulus sums, unconditional only in 𝔽_q[t]: Shoup; Bhowmick–Lê.
>
> None transfers:
> * T1 bars input-blind squeezes (Lemma 1, PROVED).
> * Jacobsthal needs fixed sifting classes, and its local main terms coincide at squares.
> * GRH-M2 yields only a small non-residue, and "non-residue ⟹ witness" is ES-strength (all 14 (★)-zero primes have
>   n_p ≤ 23).
> * In 𝔽_q[t] no q-independent-threshold positivity exists (Z58_FFIELD Cor 3.2).
>
> No result reviewed proves a pointwise hit of a power-density, moving-modulus target at polylog count, even under
> GRH. The least prime ≡ a (mod q) within q(log q)^A is unresolved on GRH (LLS Cor 1.2; KLM 2607.14515 Remark 2), and
> explicit polylog additive bases are open (JPSZ 2405.08650).

**Bottom line.** Literally, yes: pointwise existence at polylog expected count without an identity is proved, by a
sieve (Jacobsthal), by input-blind squeezes (AKS, Chebyshev), and in 𝔽_q[t] by Weil-strength character sums. All of
these certify **escape** events against **fixed** moduli. B2 needs a **hit** of a power-density target with a
**moving** modulus.
* T1 rules out input-blind squeezes outright (Lemma 1).
* Sieves and GRH character information stop at the local / non-residue layer. Every known (★)-zero prime has a
  non-residue ≤ 23, and in 𝔽_q[t] RH is a theorem without having produced MS_q.

Among the many results reviewed, no theorem of B2's shape was found, even conditionally. Its fixed-modulus relative
(least prime in an AP within q·polylog) is unresolved on GRH. *Assessment:* an analytic proof of B2 would have no
template in this literature. This is not a statement about all possible ES proofs. It supports the spending rule
(fund only genuinely new mechanisms).

## 6. Review log

**Internal hostile review** (reviewer subagent, openai-codex/gpt-6-astra, deep mode, on commit 4f3359400).
* Re-fetched all six ✔ PDFs, read all saved excerpts, and reran the F4 script: output identical.
* Confirmed: JPSZ Thm 1.1 and quotes; Pilatte Thm 5.4 / Lemma 5.3; KLM Thm 5 / Remark 2; AKS Lemma 4.3; LLS
  Cor 1.1/1.2 and Thm 1.2; PRIMITIVE_INTERSECTION's 94 primes; the z52 parity attributions; POINTWISE_OMEGA13 Thm 5.1
  exponent.

Findings and fixes:
1. *FATAL to the "exactly four classes" taxonomy:* the Iwaniec Jacobsthal bound, an unconditional pointwise
   polylog-count sieve result over ℤ, was omitted. **Fixed:** added as A1, a new class (Sv) with a transfer screen
   (§3.4 b); "exactly" removed throughout. Re-verified from Costello–Watts arXiv:1306.1064.
2. LLS Thm 1.4 formula misquoted (the 5/2 belongs to (log log q)²). **Fixed** after a visual check of the PDF;
   hypotheses added.
3. "Target-density threshold / converse" overclaimed. **Fixed:** §3.2 now describes what the displayed bound gives,
   and says the H = {1} case shows a weakness of known bounds, not a limitation of GRH.
4. Bhowmick–Lê formula and Thm 6 condition misrepresented. **Fixed:** A4 now quotes the authors' summary sentence and
   Shoup's abstract, and flags the Thm 5–6 parameter conditions.
5. Finite F4 data cannot refute an eventual implication. **Fixed:** stated as refuting only the threshold-free
   version, with the eventual version identified as ES-strength.
6. The function-field screen mixed regimes. **Fixed:** the source's quantifiers are preserved ("no q-independent
   degree threshold"); fixed q is open.
7. Universal novelty claims ("none exists, in any field, even conditionally"; "an ES proof would be the first").
   **Fixed:** restricted to the results reviewed; no claim about every ES proof.
8. Tier A mixed literal passes with comparators (Sylvester–Schur not sparse; Zsigmondy no count model; r₂ an
   identity). **Fixed:** split into Tier A and Tier A′.
9. GRH primitive-root bound O(log²p) was taken from an intro sentence. **Fixed:** replaced by Shoup's verified bound
   via Moree.
10. Thin-square-basis densities misattributed. **Fixed** (Erdős–Nathanson x^{1/3+ε}; Wirsing is an upper bound; the
    count is not quoted).
11. The 131 Legendre-symbol inference was reversed. **Fixed** (uses (2/131) = −1).
12. Lemma 1's conclusion was stronger than its proof. **Fixed:** the consequence is now stated as "some premise must
    fail at all but finitely many squares"; G is a constant.
13. Minor precision fixes:
    * AKS: "most r qualify" removed.
    * Erdős 1955 Thm 1 role corrected.
    * JPSZ's definition of "explicit" added.
    * Pilatte count now cites eq. (9), labelled as an inference.
    * Burgess exponent written exactly.
    * Linnik count corrected.
14. Script docstring vs actual controls/range. **Fixed** in the script.
