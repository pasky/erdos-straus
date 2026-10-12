# BRAINSTORM / ident_form_families — ES identities on primes p = P(t), P quadratic (O145 (b))

Labels as in DISCOVERIES.md. ES is not solved; nothing here proves any infinite case of it
(the families below cover sets of primes that are not known to be infinite, and are density 0).

## 1. Idea

Theorem C (POINTWISE_SIZE §2) excludes bounded procedures in a *linear* parameter (`p = uq+v`). Its
Remark 2: "Linearity of P is used only in computing (r_h/p). For deg P ≥ 2 ... a FAIL output must be
certified another way." So families for primes of the form `p = P(t)` with P quadratic (equivalently,
primes represented by a binary form on a line), with x, y, z polynomial in t but *not* in p, are not
covered by Thm C. Such a family is a non-congruence family in p (the set {P(t)} is not a union of
classes). Questions: (i) does the character trap still bite? (ii) do genuinely t-dependent families
exist? (iii) do they reach Mordell-hard primes? (iv) can they be made 2-dimensional (positive density)?

## 2. Literature anchor

Schinzel (Funct. Approx. 28 (2000)) and Mordell treat polynomial identities in a linear parameter
only (statement via Schuh, arXiv:2404.01307 p. 2, which also says Schinzel's theorem is specific to
4 | m). No ES identities for quadratic-polynomial values were found in the campaign's literature
files; not searched exhaustively (Assessment: unverified novelty, probably folklore-level).

## 3. Results

**Lemma 3.1 (the character step for quadratic P).** Let `p = P(t)` be prime, `P = N_{K/Q}(t − θ)`
with `K = Q(θ)` imaginary quadratic, and `𝔭 = (t − θ, p)`, a degree-1 prime of K. For h ∈ Z[t],
`h(t) ≡ h(θ) (mod 𝔭)`, so `(h(t)/p) = (h(θ)/𝔭)_K` — a quadratic residue symbol of a *fixed* element
γ = h(θ) of K at a *varying* prime (PROVED, trivial). Unlike the linear case (`h(q) ≡` a rational
constant mod p), this is not a Legendre symbol of fixed rational primes; it is the Artin symbol of 𝔭
in `K(√γ)/K`, i.e. ray-class data of 𝔭 mod 4γ.
(a) **k = 1: the Gaussian class of one is a universal trap (PROVED).** For `P = t² + 1`, θ = i,
`t − i = −i(1 + it)`. If `4N(γ) | t` then `1 + it ≡ 1 (mod 4γ)`, so 𝔭 is in the trivial ray class mod 4γ
(K has no real place) and splits in `K(√γ)`: `(h(t)/p) = +1`. Also `(ℓ/p) = +1` for every fixed prime ℓ | t.
Hence at the profinite point `t* = 0` every polynomial value met by a formal run is a residue mod p, and
the proof of Thm C goes through verbatim in the parameter t: **every correct bounded procedure in t
fails for infinitely many primes `p = t² + 1` (CONDITIONAL on Hypothesis H for the finite family met,
now including P = t²+1 itself).** EVIDENCE: at `t ≡ 0 (mod 64·47#)`, 0 of the values `t + a` (|a| ≤ 7) and
`t² + bt + c` (|b|,|c| ≤ 3) are non-residues mod p (6 primes p ≈ 10⁴⁰); shifts with |a| ≤ 60, whose
`a² + 1` has primes > 47, give ≈ 1/3 non-residues, as the lemma predicts.
(b) For general k there is no such point in general: `t − √−k` is never ≡ a unit mod N, and the
families of Prop 3.4 below (k = 21, 37) show that the trap can indeed fail at Mordell-hard primes.

**Prop 3.2 (Type II families are old; PROVED).** Let P ∈ Q[t] be quadratic with `P(t) > 0` for all
real t. Use the Type II coordinates `p = 4dgg' − h`, `g+g' = ch` (equivalent to `ff' − 4c²dp = 1`,
`f = 4cdg − 1`, `f' = 4cdg' − 1`). If c, d, g, g', h are polynomials in t, eventually positive, with
`P = 4dgg' − h` and `g + g' = ch` identically, then all five lie in Q[P].
*Proof.* Leading coefficients are positive, so there is no cancellation; let `m = deg h`, `G = max(deg g,
deg g')`; `deg c = G − m ≥ 0` and `deg d + deg g + deg g' = max(2, m)`.
(a) `m ≥ 2`: then G = m, the other two factors and c are constant, and `h(4dg'c − 1) = P + 4dg'²`, so
h, g ∈ Q[P]. (b) `m ≤ 1`, degrees (2,0,0) or (0,2,0) with m = 0: everything is in Q[P].
(0,2,0) with m = 1: `h | P + 4dg'²`, impossible at the real root of h since `P + 4dg'² > 0`.
(1,1,0): at the root t₁ of g, `P(t₁) = −h(t₁)`, and `h(t₁) = g'/c > 0` (m=1) or `= h > 0` (m=0): contradiction.
(0,1,1): m = 0 gives `P(t₁) = −h < 0`; for m = 1, c is constant and `P(t₁) = −g'(t₁)/c`, `P(t₂) = −g(t₂)/c`
at the roots t₁, t₂ of g, g'; positivity forces t₁ < t₂ and t₂ < t₁. ∎
(Divisibility of values at infinitely many t implies divisibility in Q[t], so integer-valued families
on a residue class of t are covered.) Hence Type II t-families reduce to Mordell-type families in p.

**Lemma 3.3 (Type I: e has no real root; PROVED).** In ET's Type I coordinates (`pe + 1 = 4abd`,
`a + b = ce`), a polynomial family for positive-definite P has e(t) > 0 on ℝ. *Proof.* At the largest
real root s of e: `4abd(s) = 1` and `a(s) = −b(s)`, so `d(s) < 0`; d is eventually positive, so it has a
root `t_d > s`, where `P(t_d)e(t_d) = −1`, i.e. `e(t_d) < 0` — impossible beyond the last root of e. ∎

**Prop 3.4 (constant-level Type I families; PROVED).** For `P = t² + k` (k ≥ 1) and constant c, d, the
quartic `P² + 4c²d` splits over Q iff `4c²d = 4m²(m²+k)` for an integer m ≥ 1, with
`P² + 4m²(m²+k) = (t² − 2mt + 2m² + k)(t² + 2mt + 2m² + k)` (coefficient comparison: the
`(t²+ν)(t²+ν')` shape needs a negative discriminant `−16c²d·…`, so the factors are `t² ± μt + ν`,
`ν² = k² + 4c²d`, `2ν − μ² = 2k`, and integrality of f forces μ = 2m). The family is Type I at level
(c, d) with `c² d = m²(m²+k)`, `f = (t∓m)² + m² + k`, valid on the t-classes
`2cd | t² ∓ mt + m² + k`. For **k = 1 no member reaches p ≡ 1 (mod 8)** (needs t ≡ 0 (4); then
`t² ∓ mt + m² + 1 ≡ m² + 1 (mod 4)` is odd (m even) or ≡ 2 (4) with cd even (m odd) — contradiction).

## 4. Experiments

* `scripts/bs_ident_tfamily.py 12 4000` (k = 1): 18 families, 0 identity failures on every t ≤ 4000
  with `gcd(p, 4cd) = 1`; only `t ≡ 2, 6 (mod 8)` occur (Prop 3.4) → `data/bs_ident/tfamily_M12_T4000.txt`.
* `scripts/bs_ident_tfamily_k.py 40 6` (k ≤ 40, m ≤ 6, all admissible c, both signs; 1526 families):
  exactly **k = 21 and k = 37 (m = 1, c = 1, d = k+1)** reach Mordell-hard primes (24 t-classes mod
  9240, resp. 12 mod 15960); each reported example is verified as an actual solution of 4/p, e.g.
  `p = 27830² + 21 = 774508921` (hard), solved by the (c,d) = (1,22) Type I slice with
  `f = t² − 2t + 23 ≍ p` (`data/bs_ident/tfamily_k40_m6.txt`).
  So: **there are polynomial identities in t that solve every prime `p = t² + 21` with t in 24 classes
  mod 9240, all Mordell-hard** (PROVED by the algebra of Prop 3.4 plus the class check; EVIDENCE that
  the classes contain primes). This set of primes is not a union of residue classes of p.

## 5. Barrier screen

* **B1/B5.** For k = 1 Thm C extends (Lemma 3.1(a), CONDITIONAL on H), matching Prop 3.4's 2-adic
  miss. For other k Thm C does not apply as proved, and Prop 3.4 families do reach square classes
  mod 840 (k = 21). B5 test: `p = t² + 21` is never an odd square for t > 10 — the step "P² + 4c²d
  factors polynomially" is what is false at generic n; the families are thin rather than obstructed.
* **Coverage / B3 (decisive).** One-variable families cover ≪ x^{1/2} primes up to x. Homogenising to
  `p = u² + kv²` (positive density) gives `c = mv²` (or `c = m`, `d = (m²+k)v⁴`) and the condition forces
  `v² | u²`, i.e. v = 1 for primitive (u,v): **no 2-variable extension of these families** (PROVED for
  the constant-level shape). Covering all p would need k ≈ p − ⌊√p⌋² ≍ √p unbounded, i.e. E1, and the
  condition `4cd | 2(t² − mt + m² + k)` becomes a divisor-in-class event in k: B2 lottery again.
* **B2.** Every family is a single fixed slice (c, d); Thm 2.2(iii) of redteam-2 (CONDITIONAL on H)
  says finitely many slices fail i.o. among p ≡ 1 (24). What the form `t² + k` buys is a *deterministic*
  large divisor `f ≍ p` of `p² + 4c²d` — the Planck-scale event made algebraic on a thin set.
* **B6:** not an averaging argument; no leak.

## 6. Viability Assessment

**PARTIAL.** New small theorems, no route to ES: (i) Lemma 3.1 — for quadratic parameters the
character step of Thm C becomes ray-class data in Q(√−k); for k = 1 the Gaussian class of one is a
universal trap, so Thm C extends to `p = t² + 1` (CONDITIONAL on H), closing Remark 2 there; (ii) Prop 3.2 — Type II
identities on positive-definite quadratic values are all old (PROVED); (iii) Lemma 3.3 + Prop 3.4 —
constant-level Type I identities on `t² + k` are classified; for k = 1 they miss p ≡ 1 (8), for k = 21, 37
they solve explicit non-congruence sets of Mordell-hard primes (PROVED algebra; EVIDENCE for
primes in them). **COLLAPSES** as an ES strategy at the coverage step (density 0; no 2-variable
extension; growing k is the B2 lottery). Open (UNCLEAR, cheap next step): Type I families with
non-constant level `c(t), d(t)` for `t² + k` (Lemma 3.3 constrains e) and quadratic P with t-dependent
leading coefficient; and whether *some* 2-variable identity on a binary form exists — Prop 3.2 rules
out Type II on every line through such a form, so it would have to be Type I.
