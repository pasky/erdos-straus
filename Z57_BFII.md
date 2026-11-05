# Z57_BFII — tryhard on the full Type II family: is f_II(p) ≥ 1 for every large prime p ≡ 1 (mod 4)?

Lane BFII (z57 BIG FISH). Problem: **prove f_II(p) ≥ 1 (a Type II solution exists) for every sufficiently large prime
p ≡ 1 (mod 4)**, using whatever the extra parameter c of Elsholtz–Tao Type II gives. Definitions only from
`sources/elsholtz-tao-1107.1010.pdf` §2 (ET), `SINGLE_P_COUNT.md` §1–2 and `LITERATURE_2026.md` §2.4. Labels: PROVED /
CONDITIONAL / CERTIFIED (exhaustive computation, validated code) / EVIDENCE (numerics) / Assessment.
Scripts `scripts/z57_bfii_*`, data `data/z57/bfii/`.

**Status: NOT PROVED. The Erdős–Straus conjecture remains open.** Nothing below proves f_II(p) ≥ 1 for all large p.

## 0. Summary

* **Exact forms (§1, PROVED).** Write N_II(n) := #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc} (ET (2.15)); for prime p,
  N_II(p) ≥ 1 ⟺ f_II(p) ≥ 1. Among the equivalent forms the useful new one is the **target-set form**: with
  m_f := (f + 1)/4 and T_f := {a·c⁻¹ mod f : a, c ≥ 1, ac | m_f} ⊂ (ℤ/f)^×,
    N_II(p) = Σ_{f ≡ 3 (4)} #{(a, c) : ac | m_f, a·c⁻¹ ≡ −p (mod f)},
  i.e. **a Type II solution exists iff −p mod f lies in T_f for some f ≡ 3 (mod 4)**. The (★) line is c = 1 (targets
  a | m_f only). Each two-parameter slice is a single-integer divisor problem: f | p + 4a²d (f ≡ −1 mod 4ad), f | cp + a
  (f ≡ −1 mod 4ac), f | 4c²dp + 1 (f ≡ −1 mod 4cd).
* **QNR-witness lemma (§2, PROVED).** Every t ∈ T_f has Jacobi symbol (t/f) = +1; hence every Type II solution at any
  odd n has (n/f) = −1 for both witness moduli f = 4acd − 1 and f′ = 4bcd − 1. Consequences: (i) **T1:** N_II(m²) = 0
  for every m (all four-parameter N-points, not only primitive ones); (ii) **witness barrier:** at a prime p ≡ 1 (4),
  min(4acd − 1, 4bcd − 1) ≥ n_p, the least quadratic non-residue mod p. So any argument that always produces a solution
  with witness modulus ≤ g(p) proves n_p ≤ g(p): g(p) = p^θ with θ < 1/(4√e) would beat Burgess, g(p) = (log p)^A
  would prove an open (GRH-strength) least-non-residue bound, and g(p) = C log p is impossible for infinitely many p.
* **Complete moduli (§3, PROVED + CERTIFIED).** −T_f is the full set of Jacobi-non-residue units mod f exactly for
  f ∈ {3, 7, 15} among f < 4000 (CERTIFIED), and for only finitely many f in total (PROVED). Hence (PROVED, Mordell-type)
  f_II(p) ≥ 1 whenever p is a non-residue mod 3, 5 or 7, with explicit solutions; for every other modulus the target set
  misses non-residue classes, so no finite covering exists beyond p ≡ □ (mod 105).
* **Computations (§4).** An exhaustive enumerator (validated against brute-force Erdős–Straus search and a second
  independent count) gives N_II(n) for every odd n ≤ 10⁷: **N_II = 0 exactly at the 1580 odd squares and at n = 4545**;
  every prime ≥ 3 has N_II ≥ 1 (CERTIFIED). The c ≥ 2 lines carry 86 % of all solutions at 10⁶–10⁷ and rescue every
  (★)-zero (R(p) = 0 at 14 primes p ≡ 1 (4) ≤ 10⁷, where N_II ≥ 76). Mean N_II(p) ≈ 0.076·log³p; minimum ≈ 0.012·log³p
  (EVIDENCE). A least-witness scan (CERTIFIED): every prime p ≡ 1 (4) below 10⁹ (25 423 491 primes) and in
  [10¹², 10¹² + 10⁸) has a witness f ≤ 3263; the largest least witness below 10⁹ is f = 3263 at p = 605 531 161.
* **Theorem G (§5.3 + Appendix A, PROVED; effective, Burgess + Pólya–Vinogradov only): a log p larger main term.** The
  genus main term of the Type II sub-family with witness f < p (f-coordinates, §4.3) satisfies
  G(p) ≥ 10⁻¹⁰ (log p)³ for every large prime p ≡ 1 (4), already on the box p^{0.004} < a ≤ p^{0.006},
  p^{0.080} < c ≤ p^{0.085}, p^{0.90} < f ≤ p^{0.99} — i.e. from the c-lines with c ≈ p^{0.08}; the c = 1 line has
  genus mass ≍ log²p. Identity behind it: the genus weight of target a·c⁻¹ equals that of the c = 1 target ac, so the
  Type II genus term is the τ(u)-weighted (★)-genus term in f-coordinates.
* **What c buys (§5; PROVED + EVIDENCE + Assessment).** (a) Not a free variable at fixed p: every slice is a single
  integer's divisor problem (Lemma 1.1(e)). (b) Larger target sets per modulus: the genus main term grows by a factor
  log p (Theorem G; per dyadic witness block ≍ log f, EVIDENCE); in a fixed block the relative order-≥3 remainder is ≈ 1.8× smaller for full
  Type II than for the c = 1 line (mean |A − G|/G = 0.20 vs 0.36 at p ≈ 10⁷), and the worst block ratio actual/genus is
  0.30 (vs 0 for c = 1). (c) None of this is pointwise: the order-≥3 remainder equals −(genus term) at every square, for
  every sub-family, and controlling it at one p needs character information of unbounded order at that p.
* **Verdict:** target not reached; the pointwise remainder problem is unchanged in kind by c (it gains a log p in the
  main term and a constant factor in relative fluctuation). New PROVED items: target-set form, QNR-witness lemma and
  barrier, complete-moduli classification. **ES is OPEN.**

## 1. Definitions and exact forms

Let n ≥ 1 be odd. ET Proposition 2.6/2.7: a Type II solution of 4/n = 1/x + 1/y + 1/z (n | y, n | z, gcd(n, x) = 1)
corresponds to (a, b, c, d) ∈ ℕ⁴ with

  (2.15)  4abcd = a + b + nc,   (x, y, z) = (abd, acdn, bcdn),

uniquely if gcd(a, b, c) = 1. Put N_II(n) := #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc} (no gcd condition) and
f_II(n) := #Type II solutions (ordered (x, y, z)).

**Lemma 1.0 (PROVED).** For a prime p: N_II(p) ≥ 1 ⟺ f_II(p) ≥ 1. *Proof.* Any (a, b, c, d) gives
1/(abd) + 1/(acdp) + 1/(bcdp) = (cp + b + a)/(abcdp) = 4/p. If p | x = abd then p divides x, y, z and 4 = 1/x′ + 1/y′ + 1/z′
with x′, y′, z′ ∈ ℕ, impossible since the right side is ≤ 3; so the solution is of Type II. Dividing (a, b, c) by
g = gcd(a, b, c) and multiplying d by g² keeps (2.15) and (x, y, z) (ET's dilation symmetry), so a primitive
quadruple exists; the converse is ET Prop. 2.6. ∎

**Lemma 1.1 (exact forms; PROVED).** For odd n ≥ 1, N_II(n) equals each of:
(a) #{(a, b, d, e) : e | a + b, 4abd = n + e}  [c = (a + b)/e];
(b) #{(a, c, d, e) : ce > a, n = e(4acd − 1) − 4a²d}  [b = ce − a];
(c) #{(a, c, d) : f := 4acd − 1 divides cn + a}  [b = (cn + a)/f];
(d) **(target-set form)** Σ_{f ≡ 3 (mod 4)} #{(a, c) ∈ ℕ² : ac | m_f, a·c⁻¹ ≡ −n (mod f)}, m_f := (f + 1)/4;
(e) **(slices)** for fixed (a, d): #{f | n + 4a²d : f ≡ −1 (mod 4ad)}; for fixed (a, c): #{f | cn + a : f ≡ −1 (mod 4ac)};
    for fixed (c, d): #{f | 4c²dn + 1 : f ≡ −1 (mod 4cd)}; summing any one of these over its two outer parameters gives N_II(n).
(f) the c-line decomposition N_II(n) = Σ_{c≥1} R_c(n), R_c(n) := #{(u, B, C) : 4uBC − u − B = cn, c | C}; R_1 = R is the
    (★) count of `SINGLE_P_COUNT` §1.
*Proof.* (a) Given (2.15), c | a + b (as 4abcd − nc ≡ 0 mod c); with e := (a + b)/c, dividing (2.15) by c gives
4abd = n + e. Conversely c := (a + b)/e restores (2.15). (b) Substitute b = ce − a into 4abd − e = n:
4ad(ce − a) − e = e(4acd − 1) − 4a²d. (c) (2.15) ⟺ b(4acd − 1) = a + cn. (d) f ≡ −1 (mod c), so c is a unit mod f,
as is a; f | cn + a ⟺ a·c⁻¹ ≡ −n (mod f). The map (a, c, d) ↦ (f, a, c) is a bijection onto {(f, a, c) : f ≡ 3 (4),
ac | m_f} (d = m_f/(ac)). (e) Since gcd(4ad, f) = 1 and 4ad(cn + a) = n(f + 1) + 4a²d ≡ n + 4a²d (mod f),
f | cn + a ⟺ f | n + 4a²d; similarly 4cd(cn + a) = 4c²dn + (f + 1) ≡ 4c²dn + 1. Conversely, a divisor f ≡ −1 of the
stated modulus determines the third parameter ((f + 1)/(4ad) = c, etc.). (f) (2.15) with (u, B, C) = (a, b, cd) reads
4uBC − u − B = cn with c | C; the map is injective (c is recorded). ∎

Validation: `z57_bfii_brute.py` (all odd n ≤ 400: (a) against direct quadruple loops; for primes, primitive count against a
brute-force Erdős–Straus Type II search: 0 mismatches); `z57_bfii_fform.py` ((d) restricted to a ≤ b, f < 4p, against
direct (a ≤ b) counts at 10 values of n up to 10⁵: all agree) — `data/z57/bfii/brute_check.txt`, `fform_check.txt`.

*Remark (what c changes).* In form (a) the c = 1 line forces e = a + b; c ≥ 2 lets e be a proper divisor of a + b. In (d)
the c = 1 targets are the τ(m_f) integers a | m_f, the full targets are the ≤ τ₃(m_f) fractions a/c. Example: f = 3
(a = c = d = 1) solves every p ≡ 2 (mod 3) via (x, y, z) = ((p + 1)/3, p, p(p + 1)/3); here c = 1 already suffices
(T_3 = {1}). The first difference is f = 7: c = 1 gives the targets {1, 2}, all c give {1, 2, 4} (complete, §3). In the
data the least c = 1 witness exceeds 4·10⁵ for 18 primes < 10⁹, while the least Type II witness never exceeds 3263 (§4.2).

## 2. The QNR-witness lemma, T1, and the witness barrier

**Lemma 2.1 (PROVED).** Let k ≥ 1 and f odd positive with f ≡ −1 (mod 4k). Then the Jacobi symbol (k/f) = 1.
*Proof.* Write k = 2^s k′, k′ odd. If s ≥ 1 then 8 | 4k, f ≡ −1 (mod 8) and (2/f) = 1. For k′ > 1, Jacobi reciprocity
gives (k′/f) = (f/k′)·(−1)^{((k′−1)/2)((f−1)/2)}; (f/k′) = (−1/k′) = (−1)^{(k′−1)/2} because f ≡ −1 (mod k′), and
(f − 1)/2 is odd. So (k′/f) = 1. ∎

**Proposition 2.2 (QNR witness; PROVED).** Let n be odd and (a, b, c, d) a solution of (2.15). Then for both
f = 4acd − 1 and f′ = 4bcd − 1: gcd(n, f) = 1 and (n/f) = −1 (Jacobi). Every t ∈ T_f has (t/f) = +1.
*Proof.* By Lemma 1.1(c), −n ≡ a·c⁻¹ (mod f), a unit (f ≡ −1 mod a and mod c), so gcd(n, f) = 1. Since
(c⁻¹/f) = (c/f), (a·c⁻¹/f) = (ac/f) = 1 by Lemma 2.1 (f ≡ −1 mod 4ac). Thus (−n/f) = 1 and (n/f) = (−1/f) = −1
(f ≡ 3 mod 4). For f′ use the symmetry a ↔ b of (2.15): f′ | cn + b. The same computation shows (t/f) = 1 on T_f. ∎

**Corollary 2.3 (T1; PROVED).** N_II(m²) = 0 for every odd m: (m²/f) = 1 ≠ −1. (CERTIFIED check: all 1580 odd squares
9 ≤ m² ≤ 10⁷ have N_II = 0.) This is where any proof must use non-squareness; a correct argument for N_II(p) ≥ 1 must
fail at n = m², i.e. must use some f with (p/f) = −1 — Proposition 2.2 says that *every* solution is such a certificate.

**Corollary 2.4 (witness barrier; PROVED).** Let p ≡ 1 (mod 4) be prime and n_p the least quadratic non-residue mod p
(a prime). Every solution has 4acd − 1 ≥ n_p and 4bcd − 1 ≥ n_p.
*Proof.* (p/f) = −1 forces a prime ℓ | f with (p/ℓ) = −1; by reciprocity (ℓ/p) = (p/ℓ) = −1 (p ≡ 1 mod 4), so
n_p ≤ ℓ ≤ f. ∎
*Consequence (Assessment, rigorous as stated).* An argument that, for every large p, exhibits a solution with
4acd − 1 ≤ g(p) proves n_p ≤ g(p). The best unconditional bound is n_p ≪ p^{1/(4√e)+ε} (Burgess); n_p ≤ 2 log²p is
known only under GRH (Ankeny/Bach); and n_p ≫ log p·log log log p for infinitely many p (Graham–Ringrose 1990;
≫ log p·log log p under GRH, Montgomery) — these two lower bounds are quoted from memory, and whether the exceptional
primes can be taken ≡ 1 (mod 4) was not re-checked (Assessment; the usual constructions take p ≡ 1 mod 8). So a proof
confined to f ≤ p^θ, θ < 1/(4√e) ≈ 0.152, would improve Burgess, and one confined to f ≤ (log p)^A would prove a
GRH-strength least-non-residue bound unconditionally. (It does not constrain e or d: e = 3 works for half of all primes.) CERTIFIED check: in the scans of §4
the least witness f is ≥ n_p for all 25 423 491 primes p ≡ 1 (4) below 10⁹ (0 violations).

## 3. Complete moduli: what finite covering gives

Call f ≡ 3 (mod 4) **complete** if −T_f = {u ∈ (ℤ/f)^× : (u/f) = −1}. Since f is not a square, (·/f) is a non-principal
character mod f and the right side has φ(f)/2 elements.

**Proposition 3.1 (PROVED; list CERTIFIED below 4000).**
(a) f = 3, 7, 15 are complete: T_3 = {1}, T_7 = {1, 2, 4}, T_15 = {1, 2, 4, 8}, and −T_3 = {2}, −T_7 = {3, 5, 6},
    −T_15 = {7, 11, 13, 14} are exactly the Jacobi-non-residue units.
(b) Only finitely many f are complete: |T_f| ≤ τ₃(m_f) = f^{o(1)} < φ(f)/2 for f large. No other f < 4000 is complete
    (`z57_bfii_cover.py` → `cover.txt`; the next best coverage ratios are 9/11 at f = 23, 3/4 at f = 39, 3/5 at f = 11).
(c) Hence f_II(p) ≥ 1 whenever (p/3) = −1, (p/7) = −1 or (p/15) = −1, i.e. whenever p is a non-residue modulo 3, 5 or 7.
    Explicit witnesses (a, c, d): f = 3: (1, 1, 1); f = 7: (1, 1, 2), (2, 1, 1), (1, 2, 1) for p ≡ 6, 5, 3 (mod 7);
    f = 15: (1, 1, 4), (2, 1, 2), (4, 1, 1), (1, 2, 2), (1, 4, 1), (2, 2, 1) ; then b = (cp + a)/f and
    (x, y, z) = (abd, acdp, bcdp).
*Proof.* (a) is a finite check (by hand: the pairs (a, c) with ac | m_f are listed in (c); also `cover.txt`). (b) τ₃(m) ≪_ε m^ε and
φ(f) ≫_ε f^{1−ε}. (c) If (p/f) = −1 for a complete f then p mod f ∈ −T_f, i.e. −p mod f ∈ T_f, and Lemma 1.1(d) gives a
solution. (p/15) = −1 with (p/3) = 1 means (p/5) = −1; conversely if (p/3) = (p/7) = 1 and (p/5) = 1 none of the three
applies. ∎

*Assessment.* This is the Type II part of Mordell's classical covering (the residual classes are p ≡ □ mod 105; the
mod-8 condition never enters Type II since every witness f is odd). Part (b) is the precise reason no finite set of
witness moduli can work: beyond {3, 7, 15}, each T_f covers a vanishing fraction of the classes that Proposition 2.2
allows, so finite coverings leave positive-density sets of non-square classes; an infinite family of moduli is needed,
and at that point the question is the distribution of the single residue sequence (p mod f)_f.

## 4. Computations

**4.1 Exhaustive counts (CERTIFIED).** `z57_bfii_enum.c` loops over (a, b, d) with 4abd − (a + b) ≤ X and e | a + b
(precomputed divisor lists), recording for every n ≤ X = 10⁷: N_II(n), the c = 1 count R(n), the primitive count
(= f_II(n) for primes), the largest c and the least e. Runtime 8 min. Results (`stats_1e7.txt`):
* odd 1 < n ≤ 10⁷ with N_II(n) = 0: the 1580 odd squares 3², …, 3161² and **n = 4545 = 3²·5·101** (ES holds there through the factor 5);
* every prime p ≤ 10⁷ has N_II(p) ≥ 1; minimum of f_II(p) over p ≡ 1 (4) is 2 (p = 5, 13);
* R(p) = 0 for 14 primes p ≡ 1 (4) ≤ 10⁷ (last 8 813 281) and 10 primes p ≡ 3 (4); there N_II(p) ∈ [76, 184].

| p ≡ 1 (4) in | #p | mean N_II/L³ | mean f_II/L³ | mean R/L² | min N_II/L³ | var/mean (N_II) | share of c ≥ 2 |
|---|---|---|---|---|---|---|---|
| [10³, 10⁴) | 529 | 0.0813 | 0.0660 | 0.180 | 0.0075 | 7.7 | 0.74 |
| [10⁴, 10⁵) | 4174 | 0.0783 | 0.0609 | 0.173 | 0.0127 | 14.9 | 0.80 |
| [10⁵, 10⁶) | 34392 | 0.0765 | 0.0578 | 0.169 | 0.0160 | 24.6 | 0.83 |
| [10⁶, 10⁷) | 293005 | 0.0756 | 0.0557 | 0.166 | 0.0131 | 39.0 | 0.86 |

(L = log p; EVIDENCE for the trend.) The minimiser of N_II/L³ above 10⁶ is p = 2 031 121 (N_II = 40).

**4.2 Least witness (CERTIFIED).** `z57_bfii_witness.c`: for each prime p ≡ 1 (4), the least f ≡ 3 (4) with
−p mod f ∈ T_f (and the least with c = 1 only, searched to f ≤ 4·10⁵). `witness_1e9.txt`, `witness_1e12win.txt`:

| range | #p | max least f (Type II) | at p | c = 1 line: no witness ≤ 4·10⁵ | max least c = 1 witness found |
|---|---|---|---|---|---|
| [5, 10⁹) | 25 423 491 | 3263 | 605 531 161 | 18 primes | 314 543 |
| [10¹², 10¹² + 10⁸) | 1 809 206 | 1079 | 1 000 077 030 541 | 0 | 230 583 |

Distribution of the least f below 10⁷: f = 3 for 50.0 %, ≤ 7 for 75.0 %, ≤ 15 for 91.3 %, ≤ 47 for 98.5 %, ≤ 307 for
99.98 % (Type II), against 50.0 / 66.7 / 80.0 / 92.1 / 98.5 % for the c = 1 line.

**4.3 Dyadic witness profile (EVIDENCE).** `z57_bfii_profile.py` → `profile.txt`: for f ≤ 2¹⁷, actual counts per dyadic
f-block vs the genus expectation G_f = (2^{ω(f)}/φ(f))·#{(a, c) : −p·c·a⁻¹ is a square unit mod f} and the naive
Σ τ₃(m_f)/φ(f). The naive and genus block totals grow linearly in log f (≈ 0.9 per unit of log₂ f at these sizes), i.e.
≍ log²F per dyadic block and ≍ log³p in total. The two hardest primes (2 031 121, 605 531 161) and the slowest prime of the
10¹² window have *both* deficits: genus below naive at f ≤ 2¹² (they are residues mod many small primes), and actual
counts at 25–45 % of genus at f ≤ 2¹⁴ (order-≥3 deficit). Random comparison primes track the genus term.

**4.4 Does c average out the remainder? (EVIDENCE).** `z57_bfii_block.c`: for the 3087 primes p ≡ 1 (4) in
[10⁷, 10⁷ + 10⁵) and the block f ∈ [2¹⁰, 2¹⁴), actual A vs genus G (`blockstats_1e7.txt`):

| family | mean A | mean G | var(A − G)/mean G | mean |A − G|/G | 99 % |A − G|/G | min A/G | #A = 0 |
|---|---|---|---|---|---|---|---|
| Type II (all c) | 31.5 | 31.5 | 2.02 | 0.20 | 0.66 | 0.30 | 0 |
| c = 1 line | 6.96 | 6.95 | 1.45 | 0.36 | 1.25 | 0 | 9 |

So the c-lines are positively correlated (overdispersion 2.0 vs 1.45: they share moduli f and their targets a/c share
numerators), but the 4.5× larger mean still shrinks the relative remainder by ≈ 1.8×. The genus term is an unbiased
predictor (mean ratio 1.002) in both.

## 5. The attack lines and where each stops

The target is pointwise in p. Each line below was pushed until it reduced to a statement about the single residue
sequence (p mod f)_f at characters of order ≥ 3, which is where all of them stop.

**5.1 c as an independent variable.** By Lemma 1.1(e) every pair of the three "outer" parameters (a, c, d) fixes a single
integer (p + 4a²d, cp + a or 4c²dp + 1) and a modulus tied to the pair, and the third parameter only indexes divisors of
that integer. No slice has an averaging variable independent of p; e.g. the a = 1 slice is exactly the HC problem
"p + x has a divisor ≡ −1 (mod x)" at x = 4d. Summing over c inside a slice changes the integer (cp + a), not the
modulus class of a fixed integer. (In the language of the brief: c *is* attached to p — it multiplies p in (2.15).)

**5.2 c as a target enlargement.** Fourier-expanding form (a) per pair (a, b) (moduli q = 4ab, targets −e, e | a + b):
  N_II(p) = Σ_{a,b: 4ab ≤ p+a+b} φ(q)⁻¹ Σ_{χ mod q} χ(−p)·σ_χ̄(a + b),  σ_ψ(m) := Σ_{e | m} ψ(e)
(p ≡ −e (mod q) with p + e > 0 makes d = (p + e)/q a positive integer automatically; it is impossible when
q > p + a + b and when gcd(e, q) > 1, matching χ(e) = 0). Compared with the c = 1 line (σ replaced by
χ̄(a + b)), each modulus carries the multiplicatively smoothed weight σ_χ̄(a + b), whose size is τ(a + b) for χ trivial on
the primes of a + b and typically ~τ(a + b)^{1/2}: this is the 1.8× relative gain of §4.4. Splitting real χ (genus
part M_gen) from order ≥ 3 (X), Corollary 2.3 gives X(m²) = −M_gen(m²) for every sub-family (both are 0 there), and at
p the factor χ(−p) is uncontrolled: bounding |X(p)| < M_gen(p) requires knowing p's residues mod 4ab up to characters
of unbounded order, the same single-p problem as for (★) (`SINGLE_P_COUNT` §4). No averaging over c touches χ(−p).

**5.3 A log p larger main term (Theorem G, PROVED).** In f-coordinates the genus weight of a triple (a, c, d),
f = 4acd − 1 < p, is
  γ(a, c, d) := (2^{ω(f)}/φ(f))·1[−p·c·a⁻¹ is a square unit mod f] = φ(f)⁻¹ ∏_{ℓ | f}(1 + χ_u(ℓ)),
  u := ac,  χ_u(n) := (−pu/n) (Jacobi, n odd)
(Hensel: square units mod odd f are the units that are residues mod every ℓ | f; (c·a⁻¹/ℓ) = (ac/ℓ)). It depends on
(a, c) only through u = ac, so **G(p) := Σ_{4acd−1<p} γ(a, c, d) = Σ_{u, d} τ(u)·w(u, d)**, where Σ_{u,d} w(u, d) is the
c = 1 ((★)) genus term in the same coordinates (PROVED, immediate). EVIDENCE (§4.3): G per dyadic f-block ≈ 0.9·log₂ f.

**Theorem G (PROVED; Appendix A).** For every sufficiently large prime p ≡ 1 (mod 4) (effective p₀, not computed),
G(p) ≥ 10⁻¹⁰ (log p)³. The bound already holds for the sub-sum over odd squarefree coprime a, c with
p^{0.004} < a ≤ p^{0.006}, p^{0.080} < c ≤ p^{0.085} and p^{0.90} < f ≤ p^{0.99}.

*Proof outline (full proof in Appendix A).* For fixed u = ac the f run over the progression f ≡ −1 (mod 4u); expanding
by characters ψ mod 4u, the weight factors as ψ·(1 ∗ χ_u ∗ h) with h small, and the twisted character ψ*χ_u is never
principal because **p divides its conductor**; Burgess (r = 2) and Pólya–Vinogradov in a two-character hyperbola give
the slice asymptotic (1 − 1/p)B_u L(1, χ_u) log(X/Y)/(4u) + O(p^{−0.14}) (numerically checked to within 1.2 % at
p ≈ 10⁶–10⁷, `thmG_check.txt`). Averaging L(1, χ_{ac})/(ac) over the box with Burgess (r = 20) in the c-variable kills
the non-square terms of the truncated L-series; the n = 1 term leaves the harmonic mass Σ 1/(ac) ≫ (log p)² (squarefree
coprime pairs, elementary). T1: at n = m² the twisted character ψ*χ_u becomes principal for ψ induced by χ_{−u}, a
second pole appears with coefficient −1 and cancels the main term exactly, matching γ ≡ 0 there (Cor. 2.3).

*Remarks.* (i) The constant 10⁻¹⁰ reflects the thin box only; no attempt was made to optimise (the natural constant is
of the order of the 0.9·log₂ f-per-block slope). (ii) Theorem G is about the genus (real-character) part only; it
says nothing about the actual count N_II(p). It does not change the verdict: the order-≥3 remainder also scales up (it
equals −G at squares), so the needed inequality X(p) ≥ −(1 − ε)G(p) keeps its form. (iii) The proof (Appendix A) was
written by a deep-mode subagent and checked by me line by line (hyperbola error bookkeeping, conductor claims, the
exponents −0.1485, −0.000180, −0.000193, the local factor H/φ(4u) = (1 − 1/p)B_u/(4u)); it is also included in the
hostile review of this memo.

**5.4 Short-interval / sieve route.** Using only small e (form (a) with x = (p + e)/4 running over the consecutive
integers in (p/4, p/4 + H]): failure at all e ≤ 4H means each x has its divisor set mod 4x − p avoiding −1 in the
"a/b" sense — a simultaneous condition on H shifted integers. Sieves bound the number of n ≤ N with that property from
above (a positive density decaying in H), never to zero for one given p; squares satisfy it for every H.

**5.5 What would suffice (CONDITIONAL; the implication is PROVED).** For a dyadic block put
A_F(p) := Σ_{F<f≤2F, f≡3(4)} #{(a, c) : ac | m_f, a·c⁻¹ ≡ −p (mod f)} (actual solutions with witness in the block) and
G_F(p) := Σ_{F<f≤2F, f≡3(4)} G_f(p) (its genus expectation, §4.3). **Hypothesis SB:** for every large prime p ≡ 1 (4)
there is F ∈ [p^{0.9}, ½p^{0.99}] with A_F(p) ≥ ½·G_F(p).
*Claim (PROVED): SB ⟹ f_II(p) ≥ 1 for all large p.* Appendix A Lemma 3 holds verbatim for the window (Y, X) = (F, 2F)
(its error O(p^{−0.14}) is uniform in Y ≥ p^{0.9}, X ≤ p^{0.99}), so with Lemma 5 the box part of G_F(p) is
≥ (log 2)·(10⁻⁵/512)(log p)² − O(p^{−0.049}) > 0, and G_F(p) is at least its box part (all weights ≥ 0). Hence
A_F(p) > 0, and Lemma 1.1(d) gives a solution.
SB is consistent with T1 — at n = m² both sides vanish, since −m²·c·a⁻¹ is never a square unit mod f ((−ac/f) = −1 by
Lemma 2.1) — so all the non-squareness enters through G_F(p) > 0 (Theorem G's mechanism) and the ½. SB is not a
standard conjecture and (Assessment) not implied by GRH, which controls χ(p) on average over characters, not the
order-≥3 Fourier mass at one p. It is a single-prime equidistribution statement for the residues of p modulo the
witnesses in one dyadic block, at characters of all orders. §4.4 tested the analogous block statement at much smaller
scale (f ∈ [2¹⁰, 2¹⁴), p ≈ 10⁷): there the ratio A/G was ≥ 0.30 for all 3087 primes (EVIDENCE only, and not in SB's
range f ≥ p^{0.9}).

## 6. Bottom line

* PROVED: the target-set form (Lemma 1.1(d)) and slice forms; Lemma 2.1, the QNR-witness Proposition 2.2 with T1
  (Cor. 2.3) and the witness barrier (Cor. 2.4); the complete-modulus classification (Prop. 3.1); Theorem G (genus
  main term of Type II ≥ 10⁻¹⁰ log³p, effective).
* CERTIFIED: N_II(n) for all odd n ≤ 10⁷ (zeros exactly at odd squares and 4545); least witnesses for all p ≡ 1 (4)
  below 10⁹ and in [10¹², 10¹² + 10⁸) (max 3263).
* EVIDENCE: mean N_II ≈ 0.076 log³p, min ≈ 0.012 log³p; c ≥ 2 carries 86 % of solutions; relative block remainder 1.8×
  smaller than for c = 1.
* NOT PROVED: f_II(p) ≥ 1 for all large p. What the c-parameter gives is a log p in the main term and a constant
  factor in relative fluctuation. It gives no variable independent of p, and every solution has to contain a quadratic
  non-residue certificate f ≥ n_p (Cor. 2.4).

## 7. Reproduction

```
gcc -O2 -o /tmp/z57enum scripts/z57_bfii_enum.c && /tmp/z57enum 10000000 /tmp/e1e7.bin       # 8 min
uv run --with numpy python scripts/z57_bfii_stats.py /tmp/e1e7.bin                            # stats_1e7.txt
/tmp/z57enum 100000 /tmp/e1e5.bin; uv run --with numpy python scripts/z57_bfii_brute.py /tmp/e1e5.bin 400
uv run --with numpy python scripts/z57_bfii_fform.py /tmp/e1e5.bin 5 13 17 97 3361 9973 4545 2521 10009 99991
gcc -O2 -o /tmp/z57wit scripts/z57_bfii_witness.c -lm && /tmp/z57wit 5 1000000000 400000      # 1.5 min
/tmp/z57wit 1000000000000 1000100000000 400000
python3 scripts/z57_bfii_cover.py; python3 scripts/z57_bfii_profile.py 131072 2031121 2031137 605531161 605531237 1000077030541 1000000000061
gcc -O2 -o /tmp/z57blk scripts/z57_bfii_block.c -lm && /tmp/z57blk 10000000 10100000 1024 16384 > data/z57/bfii/block_1e7_f1024_16384.txt
uv run --with numpy python scripts/z57_bfii_blockstats.py data/z57/bfii/block_1e7_f1024_16384.txt
```
(All runs under `ulimit -v 6000000` and `timeout`.)

## Appendix A. Proof of Theorem G (PROVED)

Notation as in §5.3: γ(a, c, d) is the genus weight of the triple, f = 4acd − 1, u = ac, χ_u(n) = (−pu/n) on odd n,
G(p) = Σ_{4acd−1<p} γ(a, c, d). (Draft source: `data/z57/bfii/thmG_draft.md`; numerical check
`scripts/z57_bfii_thmG_check.py` → `data/z57/bfii/thmG_check.txt`.)

### A.1. Statement

For every sufficiently large prime p ≡ 1 (mod 4),

**G(p) ≥ 10⁻¹⁰ (log p)³.**

The threshold p₀ is absolute and effective. No numerical value for p₀ is asserted. In fact this bound holds using only the ordered pairs (a,c) and moduli f in the following region:

- p^{0.004} < a ≤ p^{0.006}, p^{0.080} < c ≤ p^{0.085};
- a and c odd and squarefree, gcd(a,c) = 1;
- p^{0.90} < f = 4acd − 1 ≤ p^{0.99}.

Here d is a positive integer, and each summand is the original genus weight, with its original factor 1/φ(f). Put α := 0.091, so u := ac ≤ p^α. All logarithms are natural. The rather asymmetric a,c ranges are intentional: cancellation in the L-value average is required only in c. This permits enough saving in the progression calculation to sum its absolute errors over every pair (a,c).

### A.2. Inputs and conventions

**Burgess.** For a primitive nonprincipal character ξ of cube-free conductor Q, integer r ≥ 2, and ε > 0,

|Σ_{M<n≤M+T} ξ(n)| ≤ C(r,ε) T^{1−1/r} Q^{(r+1)/(4r²)+ε},  T ≥ 1,

with an effective constant, uniformly in real M ≥ 0. Reference: Burgess, *On character sums and L-series II*, Proc. LMS (3) 13 (1963), 524–536; Iwaniec–Kowalski, *Analytic Number Theory*, Theorem 12.6 (cube-free-conductor form). Complex characters are allowed. We use ε = 10⁻⁶, r = 2 for progression slices, and r = 20 for the outer average.

**Pólya–Vinogradov.** A primitive nonprincipal character of conductor Q has every interval sum bounded by C√Q log(2Q), with an absolute effective C. This standard effective version, not an optimal constant, suffices.

We use `Z53_GENUSLVAL.md`, Lemma 2.1, for Burgess tails and Lemma 2.2(b), with r = 2, for the principal-character hyperbola calculation. Their proofs use only the character-sum bounds and absolute values, so apply to complex characters too. We explicitly prove the mixed Pólya–Vinogradov/Burgess variant needed for other characters. The local convolution is the one in `Z56_FAMDESIGN.md`, Proposition 3.4; it is recomputed below. Neither memo's window proposition is quoted for our progression: its hypotheses concern a different projector. Neither memo's outer-average proposition is quoted for our two-variable squarefree restriction: that average is proved below. No large sieve, zero-free region, Siegel theorem, or nonvanishing theorem is used.

The supplied elementary reciprocity lemma, (u/f) = 1 for f ≡ −1 (mod 4u), is used in the T1 audit.

Notation p^{o(1)} always means a positive quantity bounded, for each fixed η > 0, by C_η p^η with an effective constant. Only logarithms, divisor functions of integers ≤ p², and explicitly bounded convergent Euler products are absorbed this way. The elementary effective estimate τ(n) ≪_η n^η follows by separating the finitely many primes ℓ ≤ 2^{2/η} and using e+1 ≤ ℓ^{η e/2} at the others. It also bounds any fixed power of τ(n), by decreasing η. All implied constants below are effective.

### A.3. Lemmas with proofs

#### Lemma 1. The character and its local factorization

Let u be odd squarefree, u ≤ p^α. Define χ(n) = χ_u(n) to be zero on even n and to be the Jacobi symbol (−pu/n) on odd n. It is a real Dirichlet character, zero exactly at integers not coprime to 2up. Its primitive conductor divides 4up, is cube-free, and is divisible by p. More precisely the primitive discriminant is −4up if u ≡ 1 (4), and −up if u ≡ 3 (4); in the second case the Euler factor at 2 is removed.

Set

 g(n) := 1[(n,2up)=1] · (n/φ(n)) ∏_{ℓ|n}(1+χ(ℓ)).

Then g = 1 ∗ χ ∗ h, where h is multiplicative and its prime-power coefficients are:

- ℓ | 2up: h(ℓ)=−1 and h(ℓʲ)=0 for j≥2;
- ℓ ∤ 2up: h(ℓ)=(1+χ(ℓ))/(ℓ−1), h(ℓ²)=χ(ℓ)[1−(1+χ(ℓ))ℓ/(ℓ−1)], and h(ℓʲ)=0 for j≥3.

For t = 1/3,

 Σ_n |h(n)| n^{t−1}(1+log n)² = p^{o(1)}.                       (3.1)

Moreover, writing H := Σ h(n)/n and B_u := ∏_{ℓ∤2up}(1+χ(ℓ)/ℓ²),

 H = [∏_{ℓ|2up}(1−1/ℓ)] B_u,
 H/φ(4u) = (1−1/p)B_u/(4u),                                   (3.2)
 B_u ≥ 1/2,   L(1,χ) ≥ 0.                                     (3.3)

*Proof.* The discriminants follow from the elementary classification of quadratic characters, or directly from quadratic reciprocity. At a good prime the local series of g is

 1 + [(1+χ(ℓ))ℓ/(ℓ−1)] Z/(1−Z).

Multiplication by (1−Z)(1−χ(ℓ)Z) gives the displayed coefficients. At a bad prime χ(ℓ)=0 and the local series of g is 1, giving 1−Z. At good odd primes, |h(ℓ)|≤2/(ℓ−1), |h(ℓ²)|≤2. Thus the good-prime absolute product in (3.1), without its logarithm, is bounded by

 ∏_{ℓ≥3}(1+2ℓ^{−2/3}/(ℓ−1)+2ℓ^{−4/3}) < ∞.

Bad primes contribute at most 2^{ω(2up)}. The logarithmic factor follows by the same argument with t increased slightly, say to 3/8, since (1+log n)² ≪ n^{1/24}. Evaluation at Z=1/ℓ gives 1+χ(ℓ)/ℓ² at good primes. Since φ(4u)=2φ(u), (3.2) follows. Finally

 B_u ≥ ∏_{ℓ odd}(1−ℓ⁻²) ≥ 1−Σ_{j≥3, j odd}j⁻² > 3/4 > 1/2.

Here Σ_{j≥3, j odd}j⁻²=π²/8−1<1/4; finite product inequalities followed by limits justify the middle inequality. For real s>1 the Euler product gives L(s,χ)>0. Burgess tails give convergence and continuity at s=1, hence L(1,χ)≥0. Strict positivity is unnecessary. ∎

#### Lemma 2. A mixed hyperbola estimate

Suppose F is primitive nonprincipal of conductor ≤4u, and G is a nonprincipal character whose primitive conductor is cube-free and ≤4up, with any removed primes dividing 2u. Put

 K_F := max(1, C₁√(4u)log(8u)),
 K_G := max(1, C₂τ(rad(2u))(4up)^{3/16+10⁻⁶}),

where C₁,C₂ are sufficiently large absolute effective constants. For 0<y≤p let

 Φ(y) := Σ_{ab≤y} F(a)G(b)/(ab),
 E(y) := (K_F K_G²/y)^{1/3}.

Then

 Φ(y) = L(1,F)L(1,G)
        + O(E(y)(1+log p+|log y|)²).                           (3.4)

For F≡1 and the same G, put E₀(y):=(K_G²/y)^{1/3}. Then

 Φ(y) = L(1,G)(log y+γ_E)+L′(1,G)
        + O(E₀(y)(1+log p+|log y|)²).                          (3.5)

*Proof.* Pólya–Vinogradov and Abel summation give

 |Σ_{n>t}F(n)/n| ≤ K_F/t.

Burgess with r=2, inclusion–exclusion over removed primes, and `Z53` Lemma 2.1 give

 |Σ_{n>t}G(n)/n| ≤ K_G t^{−1/2},  t≥1.

If E(y)≤1, take z=(K_F²y/K_G²)^{1/3}. Then z=K_F/E≥1 and y/z=(K_G/E)²≥1. In the exact weighted hyperbola identity, replace both partial harmonic character sums by their full L-values minus their tails. The error is at most

 K_G y^{−1/2}Σ_{a≤z}a^{−1/2}
 + (K_F/y)Σ_{b≤y/z}1
 + K_F K_G/(√y√z)
 ≤ 2K_G√(z/y)+K_F/z+K_F K_G/(√y√z)
 = 3E+E² ≤ 4E.

This proves (3.4) in that case. For (3.5), if E₀≤1 take z=(y/K_G²)^{1/3}=1/E₀ in `Z53` Lemma 2.2(b), r=2. Its bound is at most 20K_G√(z/y)(1+log y)+2/z, hence O(E₀(1+log y)).

For E>1 or E₀>1 use |Φ(y)|≤(1+log y)² when y≥1, and Φ(y)=0 for y<1. All L-values here are O(log p), and their derivatives at 1 are O((log p)²). To check these last bounds, their character moduli are at most 4up: split the series at that modulus, bound the head absolutely, and bound the tail and logarithmic tail by periodicity and Abel summation. Each nonprincipal character has period with sum zero, so its partial sums are bounded by its modulus. The asserted error then bounds the main terms too, including L(1,G)log y for y<1. ∎

#### Lemma 3. The full progression slice, including its local factors

Uniformly for odd squarefree u≤p^α, define

 S_u(Y,X) := Σ_{Y<f≤X, f≡−1 (mod 4u)} g(f)/f,
 Y=p^{0.90}, X=p^{0.99}.

Then

 S_u(Y,X) = [(1−1/p)/(4u)] B_u L(1,χ_u) log(X/Y)
             + O(p^{−0.14}).                                 (3.6)

The error is effective and absolute.

*Proof.* Put q=4u. Every character ψ modulo q is induced by a unique primitive character ψ*. Since g is supported on integers coprime to q, ψ(n)g(n)=ψ*(n)g(n). Complete multiplicativity and Lemma 1 give

 ψ*(n)g(n) = (ψ* ∗ (ψ*χ_u) ∗ (ψ*h))(n),

where ψ*h in the third factor denotes pointwise multiplication, not convolution. For every ψ, the primitive conductor of G=ψ*χ_u divides 4up and is divisible by p: ψ* has conductor dividing 4u, while χ_u has a nontrivial quadratic component at p. At each odd prime dividing u the conductor exponent is at most one, and at 2 it is at most two. Thus this conductor is cube-free. Additional removed primes divide 2u. **In particular G is never principal.** These statements also hold for non-real ψ.

For ψ≠ψ₀ apply (3.4) to the first two convolution factors; ψ* is nonprincipal. Summing over the third factor and using (3.1) gives, for T∈{Y,X},

 Σ_{n≤T}ψ(n)g(n)/n
 = L(1,ψ*)L(1,ψ*χ_u) Σ_{k≥1}ψ*(k)h(k)/k
   + O(p^{o(1)}(K_F K_G²/T)^{1/3}).                           (3.7)

Here the formula is applied with y=T/k, including k>T, where Φ(y)=0; the extension is justified by (3.1), since the error has the factor k^{1/3} and at most squared logarithms. The constant term is absolutely convergent in k. Subtracting T=Y from T=X kills it.

For ψ=ψ₀, ψ*≡1. Equation (3.5), with the identical summation argument, gives

 Σ_{n≤T}g(n)/n = H L(1,χ_u)log T + C_u
                  + O(p^{o(1)}(K_G²/T)^{1/3}),

where C_u=H[γ_E L(1,χ_u)+L′(1,χ_u)]−L(1,χ_u)Σ_k h(k)log k/k is independent of T. Its series converges absolutely. Again the constant cancels in the window.

For T≥Y and u≤p^α the exponent in the nonprincipal error is at most

 [α/2 + 2(3/16+10⁻⁶)(1+α) − 0.90]/3
 = −0.148457606… < −0.14.

The principal error is smaller, with the α/2 term absent. The effective p^{o(1)} factors can therefore be absorbed into p^{0.008}, for all sufficiently large p. Orthogonality gives

 S_u(Y,X) = (1/φ(q)) Σ_{ψ mod q} overline{ψ(−1)}
                         Σ_{Y<n≤X}ψ(n)g(n)/n.

There are exactly φ(q) characters, all coefficients have absolute value 1, and the factor 1/φ(q) is retained. Consequently the error remains O(p^{−0.14}), not φ(q) times this error. The principal main term is H L(1,χ_u)log(X/Y)/φ(q); now use (3.2). ∎

#### Lemma 4. There is enough squarefree coprime harmonic mass

Put A₀=p^{0.004}, A₁=p^{0.006}, C₀=p^{0.080}, C₁=p^{0.085}, and let ℬ be the set of ordered pairs in these intervals with a,c odd squarefree and gcd(a,c)=1. For sufficiently large effective p,

 M := Σ_{(a,c)∈ℬ}1/(ac) ≥ (10⁻⁵/16)(log p)².                (3.8)

*Proof.* Write L_A=log(A₁/A₀)=0.002 log p and L_C=0.005 log p. For odd t≤W and V≥1,

 Σ_{V<n≤W, n odd, t|n}1/n = log(W/V)/(2t)+O(1/V).            (3.9)

This follows by substituting n=tk and the elementary odd harmonic-sum estimate; the estimate is uniform also when V/t<1, where its error O(t/V) before division by t is sufficient.

The unrestricted odd-pair mass is L_A L_C/4+o(1). Exclude pairs for which some odd prime ℓ has ℓ²|a, ℓ²|c, or ℓ|gcd(a,c), using a union bound. Put S=Σ_{j≥3, j odd}j⁻²=π²/8−1<1/4. By (3.9), the first exclusion costs at most

 (L_A L_C/4)S + O(L_C√A₁/A₀ + L_A/C₀ + 1/A₀),

with harmless smaller terms absorbed; the second has the analogous bound with A,C interchanged. Both error bounds tend to zero because 0.006/2<0.004 and 0.085/2<0.080. For the common-prime exclusion, ℓ≤A₁, and multiplication of the two instances of (3.9) gives cost at most

 (L_A L_C/4)S
 + O((L_A/C₀+L_C/A₀)(1+log A₁)+A₁/(A₀C₀)).

This error also tends to zero. Thus M≥(1−3S)L_A L_C/4−o(1). Since 1−3S>1/4, for sufficiently large effective p this is at least L_A L_C/16, which is (3.8). ∎

#### Lemma 5. An effective two-variable L-value lower bound

For the same set ℬ,

 Σ_{(a,c)∈ℬ} L(1,χ_{ac})/(ac)
 ≥ (10⁻⁵/32)(log p)²                                       (3.10)

for sufficiently large effective p.

*Proof.* Here use r=20, κ=1/20, θ=21/1600+10⁻⁶=0.013126 and N=p^{0.29}. For every (a,c)∈ℬ, the character in Lemma 1 has primitive conductor ≤4p^{1+α} and at most the prime 2 removed. `Z53` Lemma 2.1 gives

 L(1,χ_{ac}) = Σ_{n≤N, n odd}(−p/n)(a/n)(c/n)/n
                + O(p^{θ(1+α)−0.29κ+o(1)}).

The exponent is

 θ(1.091)−0.29/20 = −0.000179534 < 0.                      (3.11)

Since Σ_{a,c}1/(ac) ≪ (log p)², the total weighted tail is o(1), effectively.

For odd nonsquare n write n=n₁s², with n₁>1 odd squarefree. For a fixed admissible a, set

 V_a(n) := Σ_{C₀<c≤C₁, c odd, μ²(c)=1, (c,a)=1}(c/n)/c.

We claim

 |V_a(n)| ≪ τ(rad(2as)) n^θ C₀^{−κ}.                       (3.12)

Indeed (c/n)1[(c,2a)=1] equals the primitive character (c/n₁) multiplied by 1[(c,2as)=1]. The character (·/n₁) has conductor n₁, which is cube-free and >1. Expand μ²(c)=Σ_{e²|c}μ(e). Terms with e not coprime to 2asn₁ vanish. In the remaining terms put c=e²v and remove the condition (v,2as)=1 by inclusion–exclusion over t|rad(2as). Burgess bounds the unweighted sum up to T by

 C τ(rad(2as)) n₁^θ T^{1−κ} Σ_{e≥1}e^{−2+2κ}
 ≤ C ζ(2−2κ) τ(rad(2as)) n^θ T^{1−κ}.

The factors t^{−1+κ} are ≤1; terms with T/(e²t)<1 are empty. Partial summation on (C₀,C₁] bounds the weighted sum by at most (2+1/κ) times this constant times C₀^{−κ}, proving (3.12).

Interchange the finite a,c,n sums. The absolute contribution from all nonsquare n is, using |(−p/n)(a/n)|≤1,

 ≪ p^{o(1)} C₀^{−κ} Σ_{n≤N}n^{θ−1}
 ≪ p^{0.29θ−0.080κ+o(1)} = p^{−0.00019346+o(1)} = o(1).     (3.13)

The sum over a with weight 1/a, its divisor factors, and τ(s) are absorbed by the stated effective divisor bounds. The elementary inequality Σ_{n≤N}n^{θ−1}≤1+N^θ/θ is sufficient.

For n=m² every term is nonnegative: the Jacobi symbols are products of coprimality indicators, and (−p/m²) is 0 or 1. Retain only n=1; its contribution is exactly M. Therefore the left side of (3.10) is at least M−o(1). Apply (3.8), and weaken its constant by a factor two to obtain (3.10). All limits and thresholds are effective by (3.11)–(3.13). ∎

### A.4. Proof of Theorem G

For each (a,c)∈ℬ, u=ac is odd squarefree and ≤p^{0.091}. Every integer f≡−1 (mod 4u) in (p^{0.90},p^{0.99}] has the unique positive integer d=(f+1)/(4u). Also f<p and gcd(f,2up)=1: coprimality with 2u follows from the progression, and with p from 0<f<p. The stipulated genus-weight identity gives

 γ(a,c,d) = g(f)/f.

Different ordered triples remain different summands, even if they have the same u or f. Nonnegativity permits restriction to this region, and Lemma 3 gives

 G(p) ≥ 0.09 log p · Σ_{(a,c)∈ℬ}
             [(1−1/p)B_{ac}/(4ac)] L(1,χ_{ac})
          − O(p^{0.091−0.14}).                               (4.1)

The number of ordered pairs is at most A₁C₁=p^{0.091}, which justifies the absolute total-error estimate; no cancellation over pairs is assumed. For p≥2, Lemma 1 and nonnegativity of L give

 [(1−1/p)B_{ac}/(4ac)] L(1,χ_{ac})
 ≥ L(1,χ_{ac})/(16ac).

By Lemma 5, (4.1) is at least

 [0.09·10⁻⁵/(16·32)](log p)³ − O(p^{−0.049})
 = 1.7578125·10⁻⁹ (log p)³ − O(p^{−0.049}).

Increase the absolute effective threshold so that this is ≥10⁻¹⁰(log p)³. This proves the asserted theorem and region. ∎

### A.5. T1 audit: why odd squares give zero instead

Replace p by an odd square m². If gcd(f,m)>1, the square-unit test has weight zero. Otherwise, for f≡−1 (mod 4u), the supplied reciprocity lemma gives (u/f)=1 and (−1/f)=−1, so (−m²u/f)=−1. If all the local square tests passed, their Jacobi product would be +1, a contradiction. Thus every genus weight vanishes.

The exact failing step of the proof is the bold assertion in Lemma 3 that **ψ*χ_u is never principal, because its conductor contains p**. At m², the character on units is instead χ_{−u}, induced from a character η modulo 4u, with additional zeros at primes dividing m. Take that nonprincipal character η modulo 4u as ψ. Then ψ*χ_u is principal on its support; it has no Burgess cancellation. Thus Lemma 2 and (3.7) cannot be applied to this ψ. This is a second pole, not a negligible window error. Indeed χ_{−u}(−1)=−1 and η(n)=1 on the support of g, since every prime dividing such n is split. Consequently its twisted window equals the principal twisted window exactly, while its progression coefficient is −1. The two terms cancel. If m shares primes with u, the same argument holds on units with the relevant extra zeros; no nontrivial prime-conductor component remains. The failure is therefore precisely at the conductor/nonprincipality step, not at an unmentioned positivity assumption.

### A.6. Numerical check summary

The script `scripts/z57_bfii_thmG_check.py` checks exact weights in the f-window (⌊p/20⌋,⌊9p/10⌋], for (a,c)=(1,1),(1,5),(3,5). These are checks of the slice residue and all its local factors, not a claim that the theorem's very narrow exponent box is populated at these sizes. The predicted quantity is exactly

 (1−1/p)L(1,χ_u)B_u log(X/Y)/(4u).

L-values are computed with the exact half-period formula for an odd primitive quadratic character ξ of conductor Q:

 L(1,ξ)=π Σ_{1≤n≤Q/2}ξ(n)/[(2−ξ(2))√Q],

followed by removal of the Euler factor at 2 when required. This numerical identity follows from the standard finite Fourier expansion of a primitive quadratic character and the Fourier series of the sawtooth function; it is used only for the check, not as an input to the proof. Character values and the finite character sum are computed as integers. The B-product is truncated at X; its omitted logarithmic tail has absolute value at most 2/X. The exact genus sum uses a smallest-prime-factor sieve, not an Euler-product approximation.

| p | u=1 ratio | u=5 ratio | u=15 ratio | pooled ratio |
|---:|---:|---:|---:|---:|
| 1000033 | 1.004098 | 1.001113 | 0.988935 | 1.001326 |
| 5212561 | 1.000363 | 0.998776 | 0.995762 | 0.999717 |
| 8813281 | 0.999571 | 1.000957 | 0.990541 | 0.999652 |

“Ratio” means exact/predicted. Pooling the three slices is also a check of an averaged quantity. All slice ratios are within 1.2% of 1; there is no factor-two discrepancy. Full output: `data/z57/bfii/thmG_check.txt`. Arrays use less than 200 MB, character sums are streamed in chunks of 250000, and the run uses a 6 GB process virtual-memory limit. The script needs only NumPy and SymPy and can be run with `uv run --with numpy --with sympy`.

### A.7. List of gaps

**None identified in the proof above.** The threshold is effective but uncomputed, and the finite-size checks are evidence for local-factor bookkeeping, not substitutes for the analytic estimates. No asymptotic for the whole G(p), no upper bound for G(p), and no statement about actual Erdos–Straus solution counts is claimed.
