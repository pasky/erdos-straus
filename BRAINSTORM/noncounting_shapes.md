# BRAINSTORM O153 / W3 — non-counting argument shapes: compactness, overspill, minimal counterexample, descent

**Verdict: COLLAPSES** (each shape, at a named step). Compactness, overspill and ultraproducts see p only as a
point of Ẑ, and K ∩ Ẑ^× ⊇ (Ẑ^×)² is a nonempty set at which primes accumulate (B1/B5). Minimal counterexample is
idle (H-G). Fermat/Lagrange descent dies at the "shape" constraint (B2). By-product: an exact profinite
dictionary (Props 1–3). No case of ES is claimed.

## 1. Idea

The brief asks for argument shapes that do not count solutions: a "sterile prime must have property X" chain,
compactness, or algebraic forcing (W1 covers forcing). This memo puts every such shape into one exact frame: the
**profinite sterile set** K ⊂ Ẑ. It then names, for each shape, the step at which it needs information about p
that the shape cannot supply.

## 2. The profinite frame (PROVED, elementary)

For integers a, b, e ≥ 1 with e | a+b, put
* `C_II(a,b,e) = {x ∈ Ẑ : x ≡ −e (mod 4ab)}`,
* `C_I(a,b,e) = {x ∈ Ẑ : xe ≡ −1 (mod 4ab)}` (empty unless gcd(e, 4ab) = 1).

Let 𝒞 be the set of all these classes (compact-open in Ẑ), and `K := Ẑ \ ⋃𝒞` (closed).

**Prop 1 (exact dictionary).** For a prime p ≥ 5: ES(p) ⟺ p ∉ K.
*Proof.* (⇐) If `p ∈ C_II(a,b,e)`, put `d = (p+e)/(4ab) ∈ ℤ_{≥1}` and `c = (a+b)/e`. Then `4abcd = c(p+e) =
cp + a + b`, which is ET's Type II equation. All parameters are positive, and ET's formulas give a positive
solution. If `p ∈ C_I(a,b,e)`, put `d = (pe+1)/(4ab)` and `c = (a+b)/e`: this is ET's Type I datum (the e-slice
form, LONGSHOT_PIGEONHOLE Lemma 1.1(ii)). The positivity threshold is automatic: membership already forces
`d ≥ 1`. (⇒) For a prime p every solution is Type I or II (ET), and every Type I/II solution has e-slice
coordinates (a, b, e) as above (Lemma 1.1(ii)); for Type II, e ≤ (p+4)/3 < p, so p ∤ e there. ∎
*Remark.* There is no archimedean threshold to track: an integer p lies in a class `C(a,b,e)` only when that class
already yields a positive solution. So "p ∉ K" is a purely profinite statement about the integer p.

**Prop 2 (squares).** `(Ẑ^×)² ⊆ K`. In particular 1 ∈ K and every odd square lies in K.
*Proof.* By ET Prop 1.6 (Type I/II are empty at odd squares, proved by a Jacobi-symbol argument on the same
parameters), no odd square lies in any C ∈ 𝒞. EVIDENCE for the class-level form, with no gcd conventions imposed:
`scripts/bs_wild_squares.py 151 2000` (`logs/bs_wild_squares.txt`): no hit for odd m ≤ 151 (Type II exhaustive,
Type I for e ≤ 2000).
Now let `y ∈ Ẑ^×` with y² ∈ C, where C has modulus Q. Pick an integer m ≡ y (mod Q). It is odd, since y is a
unit at 2. Then m² ∈ C, a contradiction. ∎

**Prop 3 (overspill / limit points).** If ES fails for infinitely many primes, then the failing primes accumulate in
Ẑ, and every accumulation point lies in `K ∩ Ẑ^×`.
*Proof.* Ẑ is compact and K is closed, so every accumulation point lies in K. For each ℓ, only one prime is
≡ 0 (mod ℓ), so every accumulation point is a unit at ℓ. ∎
The same statement covers ultraproducts: a nonstandard sterile prime p* has standard part st(p*) ∈ K ∩ Ẑ^×.

## 3. Screening the shapes

**(a) Compactness / Ramsey / ultraproducts / overspill.** These shapes use only the position of p in Ẑ (plus
first-order transfer). Compactness gives: a compact-open U is covered by finitely many classes iff U ∩ K = ∅. By
Dirichlet, every point of Ẑ^× is an accumulation point of primes, including the points of (Ẑ^×)² ⊆ K (Prop 2).
**So no property of the profinite position of primes can exclude them from K.** The step that fails is
"p ∈ K ⇒ contradiction". To make it work one must know whether a *specific* integer lies in a closed null set.
By Prop 1's proof, membership is decided by classes of modulus 4ab ≤ p + e (Type II) or ≤ pe + 1 (Type I), i.e.
at the profinite "Planck scale" Q ≍ p. That is B3, and B1 for any finite-level truncation (Thm M, Thm C: some
primes need moduli `> exp(c(log p)^{1/4})`). The x** programme (MORDELL13–13E) asks whether K contains non-square
points. Even a complete description of K would not decide whether primes lie in it.
*T1:* the shape cannot even separate p from odd squares. They are in K by Prop 2, and primes accumulate there.

**(b) Minimal counterexample.** Let p be the least prime with ES(p) false. The extra hypothesis is ES(n) for all
n < p. Known to 10¹⁷ anyway, it says nothing about the factorisation of N_θ(p), even though N_e = (p+e)/4 < p:
what matters is the divisor structure of N_e in classes mod e, not whether 4/N_e is solvable.
Transfers ES(n) ⇒ ES(p) exist only for n | p (scaling); H-G and notes §77.6 record that the natural forms are
closed. **Idle.** Also, ES(3p) holds for every p via 4/(3p) = 1/p + 1/(4p) + 1/(12p). So solvability of
composite relaxations n = mp carries no information about p.

**(c) Fermat/Euclid/Lagrange descent.** Fermat's descent for p = x² + y² composes relaxed solutions
`mp = x² + y²` through the norm form of ℤ[i] and lowers m. An ES analogue needs a relaxed family with a
composition law.
* *Denominator relaxation* (ES at mp): useless, by the 3p example in (b).
* *Quaternion norms* ((I)6, QUATERNION_ES Lemma 3.1): Type II ⟺ `(2ai + j)(2bi − j) = −e(1 + 2ck)` in (−d, −p).
  Taking norms, `(4a²d + p)(4b²d + p) = e²(1 + 4c²dp)`. Norm-form descent controls norms only. The ES condition
  is a **shape** condition: zero real part and j-coefficient exactly ±1. Restricted to that shape, the norm form
  is the binary family `4da² + p`, and the existence question is the slice "`p + 4a²d` has a suitable divisor".
  Collapses to B2 there. Also, norm-Euclidean definite quaternion orders are finitely many (classification
  from memory, unverified), while the algebra varies with p.
* *Toric composition.* The only group structure on the ES variety is the split torus of the toric model
  (GEOMETRY_ES, (I)7). Integral points of a split torus over ℤ are units, so composition has no descent content
  (Assessment, consistent with GEOMETRY_ES Thm 3.1).

**(d) "A sterile prime has property X" chains.** Every property derivable so far is profinite: p ∈ K, so p avoids
all classes; through Mordell/Yamamoto/MORDELL13 Thm 3.1 that forces square classes mod 840, near-squares mod
11 and 13, etc. Such chains end in "p is square-mimicking up to level Q". That is consistent with p being prime for
Q up to `≍ log p log log p` (Graham–Ringrose type) and is no contradiction (POINTWISE_SIZE Thm C). Least
non-residue bounds (Burgess; Bach under GRH) cap Q only at `≪ p^{1/(4√e)+ε}`, resp. `2 log²p`. To turn
"QR modulo all q ≤ Q" into a contradiction one would need, *for every prime q*, a finite cover of the non-residue
classes mod q (call it NR_q). By compactness, NR_q ⟺ K contains no point that is a non-residue mod q. The
campaign's x** = x(2,15) is a non-residue mod 11 and mod 13 and survives through ES level 2.59·10¹⁰
(MORDELL13E, CERTIFIED); its sterility is a CONJECTURE. If it is sterile, NR_11 and NR_13 fail and the chain is
dead. Even if not, the chain needs NR_q for all q with explicit moduli, which is again a congruence-covering
statement (B1).

## 4. Barrier screen (summary)

* B1: (a) and (d) are congruence/profinite arguments by construction.
* B2: (c) ends in the slice.
* B3: (a) needs moduli ≍ p.
* B4: not applicable.
* B5: (a) cannot separate primes from (Ẑ^×)² (Prop 2); (b)'s composite relaxations are solvable at squares too
  (`4/(3m²)`).
* B6: none of these shapes averages, which is their appeal. They fail before any estimate is used.

## 5. Viability Assessment

**COLLAPSES**:
* (a) at "p ∈ K ⇒ contradiction" (B1/B3/B5, via Props 2–3 and Dirichlet);
* (b) idle (H-G);
* (c) at the shape constraint (B2);
* (d) at NR_q (B1; CONJECTURALLY false at q = 11, 13 via x**).

By-products (PROVED, elementary; modest novelty):
* the exact dictionary ES(p) ⟺ p ∉ K (Prop 1), where the class membership needs no positivity threshold;
* (Ẑ^×)² ⊆ K (Prop 2);
* limit points of failures lie in K ∩ Ẑ^× (Prop 3).

**Take-away for the parent.** Any argument shape whose only access to p is first-order or profinite (compactness,
ultraproducts, Ramsey, overspill, minimal counterexample) is provably blind to ES, because primes accumulate on
(Ẑ^×)² ⊆ K. A non-counting route must use the archimedean size of p against moduli ≍ p, and that is the regime of
B2/B3.
