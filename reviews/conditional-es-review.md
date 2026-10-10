# R127 — hostile review of O127 (`CONDITIONAL_ES.md` §§1–9, reports O127/O127b, `scripts/cond_*`)

Reviewer: R127 side agent (branch `side-agent/review-conditional`). Author files merged from
`side-agent/conditional-es`. All numerics below are from FROM-SCRATCH code
(`scripts/review_r127_*`), not from the author's scripts. Sources checked: ET
(`sources/elsholtz-tao-1107.1010.pdf`, text-extracted), BL (`sources/bright-loughran-1908.02526.pdf`).

## Summary verdicts (per claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (slice, lift to ES solution) | SOUND |
| Dual form (§6) and remainder form (§7.5) | SOUND-AFTER-REPAIRS (minor: coprimality in the "iff") |
| Prop 2.3 / Lemma 2.1 (scale constraint) | (see §2 below) |
| Cor 4.1 / Remark 4.2 | (see §4 below) |
| Thm 6.1 | (see §6 below) |
| Prop 7.1 | (see §7 below) |
| Prop 7.2 | (see §7 below) |
| Prop 7.3 | (see §7 below) |
| Prop 9.1 + §9 Assessment | (see §9 below) |
| §8 EVIDENCE S(5101441) = 1 | (see §8 below) |

## 1. Lemma 1.1 — SOUND

Re-derived by hand:
* (1)⇒(2): with `f=(m+1)/t`, `c=(m''+1)/t`: `(tf−1)(tc−1) = tn+1` ⇔ `tcf − c − f = n`; `4 | m = tf−1`
  ⇔ `tf ≡ 1 (4)`. (2)⇒(1) by the identity `(gc−1)(gf−1) = g(gcf−c−f)+1`. Cofactor ≡ −1 automatic. ✓
* Lift: `d=(fg−1)/4 ≥ 1` (fg = 1 forces n = −1); `n+c = f(cg−1)`; `4bd = (cg−1)(fg−1) = gn+1`;
  `c + n(b+1) = c(1+ng)`; so the sum is `4/n`. ✓ `t ≤ n+2` from `(t−1)² ≤ tn+1`. ✓
* Dictionary to ET Type I at a = 1 (`b = m''`, `4d = m`, `ct = 1+b`). ✓

**From-scratch brute force** (`scripts/review_r127_lemma11.py 200`): for every 1 ≤ n < 200 the three
forms (1), (2), (3) give *identical* solution sets (as (c,f,g) triples; form (1) enumerated
independently over all (t, m)), all 600 solutions rebuilt and `4/n` checked in exact rationals,
0 failures; the "cofactor automatic" assertion never fired. The dual form of §6 ("least positive
residue g of −n⁻¹ mod m divides m+1", m ≡ 0 (4), gcd(m,n)=1) and the first remainder form of §7.5
(`(cm−n) | (m+1)`) agree with solvability for every odd 1 < n < 200. (Note: in the dual form the
witness g of Lemma 1.1 need not be the least residue — g = m+1 is possible — but then t = 1 also
works, so the equivalence holds; checked numerically.)

Side fact: no slice solution with `n | c` exists for any 3 < n < 200; for primes p > 3 it is
impossible (p | c forces p | f and then `pl(pg−1)… = 2`-type contradiction), so `S'(p) = S(p)`
exactly, not "up to O(1)" (§7.4) — MINOR, harmless.

## 8. §8 EVIDENCE and the full Type I / II counts — SOUND (EVIDENCE confirmed); new data

From-scratch tool `scripts/review_r127_counts.c` (gcc -O2): (a) `S(p)` by *direct* enumeration of
all pairs (c, f) with `(c−1)(f−1) ≤ p+1` (a different algorithm from the author's dual-form scan);
(b) the FULL ordered solution count `f(n)` of `4/n = 1/x+1/y+1/z` by enumerating `x ≤ y ≤ z`,
`x ∈ (n/4, 3n/4]`, and all divisors u ≤ B' of `B'²` (`1/y+1/z = A'/B'`, `(A'y−B')(A'z−B') = B'²`),
each sorted triple weighted by its number of permutations and classified by how many coordinates
n divides; `f_I = #(exactly one)/3`, `f_II = #(exactly two)/3` (ET (1.4)). Validation: the tool
reproduces ET's list `f(2..8) = 3, 12, 10, 12, 39, 36, 46` exactly, and `S` matches the Python
brute force of §1 at 13, 29, 193. Output: `data/review_r127/counts.txt` (2.3 s total).

| p | S(p) (slice) | the slice solution (c, f, g) | f(p) | f_I(p) | f_II(p) |
|---|---|---|---|---|---|
| 2521 | 1 | (2, 87, 15) | 54 | 12 | 6 |
| 5569 | 1 | (17, 7, 47) | 162 | 34 | 20 |
| 21169 | 1 | (4, 31, 171) | 222 | 38 | 36 |
| 43969 | 1 | (20, 31, 71) | 300 | 60 | 40 |
| 5101441 | **1** | (890, 39, 147): `147p+1 = 5732·130829` ✓ | 798 | **188** | **78** |

* **S(5101441) = 1 is CONFIRMED independently** (EVIDENCE), with exactly the author's witness
  (g = 147, m = 5732, m'' = 130829).
* Also confirmed: S = 3 at 943009 and 830041 (least g = 367 at 830041 ✓), S = 2 at all 11
  primes listed in §8 (1201, …, 2922529); the slice (I1) solves every prime 3 ≤ p < 3000 (429
  primes); the Type II a = 1 slice fails exactly at p ∈ {193, 2521} below 3000 ✓.
* Not re-checked: the full 20513-prime scan below 10⁷ (the table's means/minima) — too costly with
  the independent O(p log p) algorithm; spot checks above all agree.
* **New EVIDENCE (answers the author's "suggested next step").** At the slice-singleton primes the
  full counts are *not* O(1): `f_I(5101441) = 188` (`≈ 0.79 log²p`), `f_II = 78`; at the four
  smaller singletons `f_I ∈ [12, 60]`, `f_II ∈ [6, 40]`. So the a = 1 slice is a thin (≈ 1/188 at
  p = 5101441) and fragile part of a Type I family of normal polylog size. The report O127b's
  conditional "if those are also O(1) … ES at hard primes is decided at Planck scale with no
  margin" does **not** occur at these primes. This supports §8's own recommendation (state any
  conjecture for full Type I ∪ II) and weakens nothing else. (R127 repair: a sentence recording
  this has been added below §8's "Reading" — see repairs list.)

## 2. Lemma 2.1 / Prop 2.3 (scale constraint) — SOUND-AFTER-REPAIRS (minor)

* ET Thm 1.1 checked in the source: `Σ_{p≤N} f_I(p) ≪ N log²N log log N`, `Σ_{p≤N} f_II(p) ≪ N log²N`;
  with ET (1.4) `f(p) = 3f_I(p)+3f_II(p)` this gives Lemma 2.1's bound for ordered solutions. ✓
* Prop 2.3 proof `M/2 ≤ #𝔗_p ≤ μ f(p)` is correct and holds for *every* large p. ✓
* **D1 (MINOR, dyadic).** Lemma 2.1 gives `f(p) ≤ N^δ` off an exceptional set; Prop 2.3 states
  `M(p) ≤ 2μ p^δ`, i.e. the threshold `p^δ`, not `N^δ`. Repair: apply Markov on each dyadic block
  `(N/2^{k+1}, N/2^k]` with λ = `(N/2^{k+1})^δ` and sum: `Σ_k (N/2^k)^{1−δ}log³N ≪_δ N^{1−δ}log³N`. The
  implied constant depends on δ (fine for fixed δ < 1).
* **D2 (MINOR, quantifier).** "μ ≤ p^{o(1)} ⇒ M(p) ≤ p^{o(1)} for almost all p" needs a diagonal
  step: the exceptional set depends on δ. Correct statement: there is a function δ(p) → 0 with
  `M(p) ≤ 2μ(p)p^{δ(p)}` outside a set of density 0 (choose N_k with exceptional count for δ = 1/k
  below N/k for N ≥ N_k). Also "μ(p) ≤ p^{o(1)}" must be uniform in p (a single o(1) function).
  The *consequence* actually used ("a main term `M(p) ≥ p^η` for all large p is excluded") is
  unaffected, since it needs only one δ < η.
* Note (not a defect): pointwise, only `f(p) ≪ p^{3/5+o(1)}` is known (ET Prop 1.7), so the
  "almost all" is genuinely needed; a driver with power main term on a sparse set of p is not
  excluded — the text says "almost all", correctly.
* "PROVED relative to ET Thm 1.1" — label honest; the result is elementary (Markov).

## 4. Cor 4.1 / Remark 4.2 — SOUND-AFTER-REPAIRS (minor citation precision)

HR arXiv:1910.01360v2 **fetched and read** (`/tmp/hr.pdf`, not committed).
* HR Thm 1.12(1): `|D|^{−1/12+δ} ≪ r < R ≪ 1`, `|D|^{−1/2+δ} ≪ μ(A_{r,R}) ≪ 1`, D → −∞ through
  squarefree fundamental discriminants, conclusion for all w outside a set of measure o_δ(1).
  **Quoted correctly.** Expected count `μ(A)h(D) ≥ |D|^{δ−o(1)}` (the text says `≥ |D|^δ`; drop
  of o(1), harmless).
* HR Thm 1.6 (sphere, squarefree n ≡ 3 (8)): asymptotic for `n^{−δ} ≪ σ(B_R) ≪ 1`, **δ < 1/12
  unconditionally, δ < 1/4 under GLH**. Quoted correctly for GLH. **D3 (MINOR).** HR Thm 1.6
  is stated for a **fixed** centre w ("Fix w ∈ S²", n → ∞), not uniformly in w; the text's
  bullet heading "All centres" overstates it (a uniform-in-w version is what one would need for a
  p-dependent centre). Repair: "Fixed centre (HR Thm 1.6 is stated for fixed w; uniformity in w is
  not asserted there)". Also mention the unconditional range δ < 1/12 (expected count
  `≥ n^{5/12−o(1)}`). This only weakens the positive tool further, so Cor 4.1 is unaffected.
* Young [You17 Thm 2.1] / Humphries [Hum18 Thm 1.24]: HR cite them as the Heegner-point
  analogues of Thm 1.6 ✓; exponents not checked by me either (sources not accessed).
* "HR §1 (end) … balls at radius `|D|^{−1/4+δ}` beyond their method": the passage is the
  **closing paragraph of HR §6** (before the Acknowledgements), not §1; content ✓ (needs a
  sub-Weyl subconvex bound). MINOR location fix.
* Cor 4.1 logic re-derived: an asymptotic with expected count `M ≥ |D|^η ≥ p^{κη}` gives
  `#𝔗_p ≥ M/2` for large p, then Prop 2.3 gives `p^{κη} ≤ 2μ f(p) ≤ p^{o(1)}` off a sparse set —
  contradiction. Hence, unconditionally, for almost all p an ES target with such an encoding is
  *not* an admissible region of the theorem. ✓ No upper bound on |D| is needed. ✓
* Remark 4.2 "(PROVED implication)": ✓ as an implication. **D4 (MINOR).** "the (believed …)
  asymptotic for balls at that scale" should be restricted to the families where it is
  believed (S², Heegner points): on S³ the all-centre asymptotic already **fails** at expected
  count `(#pts)^{1/4−o(1)}` (big holes, the author's own §7.1). Repair: add "(for S² / Heegner
  families; on S³ it is false, §7.1)".

## 6. Theorem 6.1 — SOUND (trivial, as the author says)

X_slice(p) is Lemma 1.1(3) at n = p; the solution `(bdp, cd, bcd)` is positive (§1). The dual
form is equivalent (checked by hand and numerically, §1 above). **D5 (MINOR, §6 random-model
Assessment).** "`P(S(p)=0) ≈ exp(−c log²p)`, summable": at Mordell-hard primes near 5·10⁶ the
Poisson model with mean `0.1·log²p ≈ 24` predicts `P(S ≤ 1) ≈ 24e^{−24} ≈ 10⁻⁹`, yet five
singletons occur among ≈ 2·10⁴ hard primes (§8, confirmed above). The model is *refuted* on
the hard classes; the existing caveat ("only indicative") is too weak. Repair: add "(and it is
contradicted at Mordell-hard primes by §8)".

## 7. Propositions 7.1–7.3

### Prop 7.1 — SOUND (with D1/D2 of §2 inherited)
`#𝔗_p ≤ μ f(p) ≤ p^{ε/2+o(1)}` off the Lemma 2.1 exceptional set (δ = ε/2). Correct and trivial.
The labels are honest: "natural ⇒ not power-deficient" and "artificial multiplicity reduces to
the quotient" are marked Assessment.

### Prop 7.2 — SOUND-AFTER-REPAIRS; statement fair as stated, but over-advertised in §0
* Construction re-derived and **simulated from scratch** (`scripts/review_r127_diag.py`):
  `M_j = 3, 6, 7, 12, 13, 18, 19`, Dirichlet primes `p_j = 59, 419, 55439, 1081079, 24504479`
  (≡ −1 mod lcm(m ≤ M_j)), classes chosen greedily; **none of the p_j lies in any class with
  m ≤ 20000** ✓. Edge case checked: if `m | p_i` the residue `p_i mod m` is a non-unit and costs
  nothing; m = 3 has the single admissible class 1. ✓
* **D6 (MINOR, wrong probability).** "hits with probability exactly `1/φ(m)`": under Haar measure
  on Ẑ, `P(n ≡ r_m mod m | n ≡ b mod Q) = 1/m` for (m, Q) = 1, not `1/φ(m)` (that would be the
  probability for a random *unit*, i.e. a prime-like model). The conclusion survives because
  `Σ_{(m,Q)=1} 1/m = ∞`. Repair: replace `1/φ(m)` by `1/m` (or say "Haar-random unit").
* **Fairness.** The refuted statement quantifies over *all* unit-class systems, including
  adversarially chosen ones; nobody conjectures that, so Prop 7.2 refutes a deliberately general
  statement, not a conjecture from the literature. The text draws the honest conclusion ("must
  restrict the class of systems"), so §7.3 is fair. But **D7 (MINOR, overclaim in §0 and §7.5)**:
  "every general Cramér-scale covering statement is false" reads as if natural Cramér-scale
  conjectures were refuted. Repair: "every covering statement quantified over arbitrary
  unit-class systems is false (diagonal); definable classes are tested only numerically". Note
  also the system has expected count `Σ_{m≤X} 1/m ≈ log X` up to modulus X, i.e. it *is* at
  Cramér scale with C = 1; with K classes per modulus (`φ(m) > j + K`) the diagonal gives any C, so
  the result is robust in C ✓.

### Prop 7.3 — SOUND as stated; GAP in its use (§7.3 consequence and §9)
* R125 Lemma 5.1 re-checked against ET: ET line "a Type I solution if n divides x but is coprime
  to y and z" and ET Prop 1.6 "for any odd perfect square n, f_I(n) = f_II(n) = 0" ✓; `4bd = gn+1`
  gives `gcd(n, bd) = 1`, so `gcd(n,c) = 1` makes `(bdn, cd, bcd)` Type I ✓. Numerically (own C):
  `S(m²) = 0` for all odd 3 ≤ m ≤ 61 (complete) ✓.
* Proof: m odd, `m ≡ m₀ (mod 2Q)` (m₀ odd by CRT; automatic if Q even), count in
  `(√X, √(2X)]` is `≈ 0.21 X^{1/2}/Q ≥ 0.2X^ε ≥ 1` for X ≥ X₀(ε) ✓. p prime > Q so the class is a
  unit class ✓.
* **D8 (MAJOR, §9 third bullet and the §9 closing paragraph; also report O127b (3)).** The text
  says arguments using p "only through `(p mod q)_{q ≤ p^{1/2−ε}}` and size" give the same
  output at an odd square, and that this "is PROVED … it is Prop 7.3 with H the argument's
  hypothesis". **False.** Prop 7.3 is about a *single* modulus Q ≤ X^{1/2−ε}. The joint data
  `(p mod q)_{q ≤ Q₀}` is `p mod lcm(1..Q₀)`, and `lcm(1..Q₀) = e^{(1+o(1))Q₀} ≫ X` for
  `Q₀ = X^{1/2−ε}`; by CRT the only n ∈ (X, 2X] with these residues is p itself, which is not a
  square. So there is **no** odd square sharing that data, and the argument fails. The same
  applies to "L-function hypotheses about characters of moduli ≤ p see p only through p mod q":
  characters of all moduli ≤ p jointly determine p. Correct scope: arguments that use p only
  through `p mod Q` for a single Q (equivalently, a family of moduli with **lcm** ≤ `X^{1/2−ε}`)
  and the dyadic size. Repair applied (R127 repair) in §9 and noted in §7.4.
* **D9 (MINOR, §7.4 consequence).** "A true conjecture implying X_slice (or ES at square-mimicking
  primes) must …": odd squares *do* satisfy ES (`ES(m) ⇒ ES(m²)` by scaling), so Prop 7.3 says
  nothing against a hypothesis H(n) ⇒ ES(n). It refutes H(n) ⇒ S'(n) ≥ 1 and, by ET Prop 1.6,
  H(n) ⇒ f_I(n)+f_II(n) ≥ 1. Repair: replace "(or ES at square-mimicking primes)" by "(or
  `f_I + f_II ≥ 1`, which is ES at primes)". Also "use moduli `Q > n^{1/2}`" should read "use
  local data whose total modulus (lcm) exceeds `n^{1/2−ε}`".

### §7.5 remainder form — SOUND-AFTER-REPAIRS
* `(cm−p) | (m+1) ⟹ (cm−p) | (p+c)` ✓ (from `c(m+1) − (cm−p) = c+p`). The converse needs
  `gcd(cm−p, c) = gcd(p, c) = 1`. **D10 (MINOR).** For composite n the second ("divisor of n+c")
  form is *not* equivalent: my brute force finds spurious hits at n = 9, 49, 81, 105, 121 (e.g.
  n = 9, c = f = 3), where the slice has no solution. For primes p > 3 it is fine: p | c with
  `f ≡ −p (mod 4c)` forces p | f, and then `f ≤ (p+f)/c + 1` fails. Repair: state "for a prime p"
  (or add `gcd(c, p) = 1`). The condition `(p+f)/c ≡ 0 (mod 4)` is implied by `f ≡ −p (mod 4c)`
  (redundant, harmless).

## 9. Prop 9.1 and the §9 Assessment — Prop 9.1 SOUND as bookkeeping; Assessment GAP (D8)

* Prop 9.1 re-derived: n = `(qjp+1)/4` with j in one class mod 4 is an AP of modulus qp inside
  `[1, X]`, `X ≍ p²`, of length ≍ p/q. Detecting it by the φ(qp) characters ψ and bounding each
  twisted sum by `O(X^{1/2+ε})` gives total error `X^{1/2+ε} = p^{1+o(1)}` (the factor `1/φ(qp)`
  cancels the number of ψ), against p/q terms. ✓ Since this is a statement about one route
  (triangle inequality over ψ, square-root error per ψ) the label "bookkeeping, mechanism scope"
  is honest. **D11 (MINOR wording).** The proof says "error ≥ X^{1/2} = p per ψ, after the
  `1/φ(qp)` normalisation"; it is ≈ `X^{1/2}/φ(qp)` per ψ and `X^{1/2}` in total. Repair: "in
  total over ψ".
* Assessment third bullet and closing paragraph: see **D8** (MAJOR) — the claimed rigorous
  support is not valid for joint data over many moduli. With the repair, the rigorous content is
  only: arguments that see p through a single modulus (lcm) ≤ `p^{1/2−ε}` plus size cannot prove
  `S'(p) ≥ 1`. GRH for all characters of modulus ≤ p is *not* such an argument; so the third
  fact supports the Assessment only heuristically. The Assessment label itself is honest.
