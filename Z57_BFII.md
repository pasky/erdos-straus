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
* **What c buys (§5; EVIDENCE + Assessment).** (a) Not a free variable at fixed p: every slice is a single integer's
  divisor problem (Lemma 1.1(e)). (b) Larger target sets per modulus: the genus main term per dyadic witness block grows
  like log f, total ≍ log³p (EVIDENCE); in a fixed block the relative order-≥3 remainder is ≈ 1.8× smaller for full
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

**5.3 A log p larger main term.** EVIDENCE (§4.3): the genus main term per dyadic witness block is ≍ log F, total
≍ log³p, versus ≍ log²p for (★). Assessment: a rigorous unconditional lower bound M_gen^{II}(p) ≫ log³p should follow by
running the slice machinery of `Z56_FAMDESIGN` §3 (Lemma 3.3 / Props 3.4, 3.6) on each line c ≤ p^ε with c odd and
coprime to a: fix a, sum over b ≡ −a (mod c) in a Burgess-long window (characters ψ mod c twist η; ηψχ_D stays
non-principal because p | cond χ_D, D = disc ℚ(√(−pac))), then average 𝓛(χ_{D_{ac}}) over a. Each line contributes
≍ φ(c)⁻¹ log²p, and Σ_{c ≤ p^ε} gives ≍ ε log³p. **Not written out or checked here; label: Assessment.** It would not
change the verdict: the remainder X also scales up (it equals −M_gen at squares), so the needed inequality
X(p) ≥ −(1 − ε)M_gen(p) keeps its form.

**5.4 Short-interval / sieve route.** Using only small e (form (a) with x = (p + e)/4 running over the consecutive
integers in (p/4, p/4 + H]): failure at all e ≤ 4H means each x has its divisor set mod 4x − p avoiding −1 in the
"a/b" sense — a simultaneous condition on H shifted integers. Sieves bound the number of n ≤ N with that property from
above (a positive density decaying in H), never to zero for one given p; squares satisfy it for every H.

**5.5 What would suffice (CONDITIONAL statement, for the record).** Hypothesis SB(θ): for every large prime
p ≡ 1 (4) there is F ∈ [p^θ, p^{1/2}] such that Σ_{F<f≤2F, f≡3(4)} #{(a, c) : ac | m_f, a c⁻¹ ≡ −p (f)} ≥ ½ G_F(p),
G_F(p) := Σ_{F<f≤2F} G_f(p). Then f_II(p) ≥ 1 for large p *provided* G_F(p) > 0, which is a genus (real-character)
statement of Theorem V type (Assessment: G_F(p) ≫ log²F should follow by the §5.3 route for F in the Burgess range).
SB(θ) is consistent with T1 — at n = m² both sides vanish, since −m²·c·a⁻¹ is never a square unit mod f
((−ac/f) = −1 by Lemma 2.1) — so all the non-squareness enters through G_F(p) > 0 and the ½. It is not a standard
conjecture and (Assessment) not implied by GRH, which controls χ(p) on average over characters, not the order-≥3 Fourier
mass at one p. §4.4: its block version with ½ replaced by 0.30 held for all 3087 tested primes at 10⁷ (EVIDENCE only).

## 6. Bottom line

* PROVED: the target-set form (Lemma 1.1(d)) and slice forms; Lemma 2.1, the QNR-witness Proposition 2.2 with T1
  (Cor. 2.3) and the witness barrier (Cor. 2.4); the complete-modulus classification (Prop. 3.1).
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
