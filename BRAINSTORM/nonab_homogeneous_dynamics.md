# Brainstorm O147(b): homogeneous dynamics (Oppenheim/Margulis, EMM, Ratner, Hecke orbits, Duke)

ES is not solved; nothing here proves any case of it. This angle overlaps LONGSHOT_FIBRED (O136) Thm 3.1 and
CONDITIONAL_ES Prop 2.3. Only what is new or sharper is recorded here.

## 1. Idea

Find a homogeneous space Γ\G (G = SO(2,1) ≅ PGL₂, or SL₂ⁿ) and a family of points or orbits there that
encodes *all* ES solutions across n. Each fibre over a prime p should then be the intersection of an orbit
(or an orbit family) with a target set T_p. An equidistribution or counting theorem (Ratner/Margulis–
Mozes–Shah for unipotent and expanding orbits, Eskin–Margulis–Mozes quantitative Oppenheim,
Duke–Rudnick–Sarnak / Eskin–McMullen lattice-point counting on quadrics, Clozel–Oh–Ullmo Hecke orbits,
Duke's theorem on CM points) would then show #(orbit ∩ T_p) > 0 for each large p.

The candidate spaces, all already present in the campaign:
* (H1) X_d: ef − 4da² = 1, a one-sheeted hyperboloid with Γ_d = SO(Q_d)(ℤ) acting with finitely many
  orbits. ES Type II(p) through a point (a, e, f) ⟺ the congruence 4da | f + p (GEOMETRY_ES Prop 4.1,
  POINTWISE_TERNARY §5; (I)1, (I)7).
* (H2) Heegner points of discriminant −4dp on SL₂(ℤ)\ℍ, which Duke shows equidistribute as dp → ∞.
  Type II ⟺ a point on the shell ⟨u, v⟩ = −1, i.e. a tube of hyperbolic width ≍ (dp)^{−1/2} ((I)4).
  Type I ⟺ points in tubes of width ≍ 1/p ((I)3).
* (H3) Real Oppenheim form: ES(n) ⟺ the cubic 1/x + 1/y + 1/z takes the value 4/n exactly at a positive
  integer point.
* (H4, new framing) the profinite "space of all primes": each Type II witness w = (a, c, d), with
  f = 4acd − 1, covers the open set A(w) = {x ∈ ℤ̂ : x ≡ −4a²d (mod f)} (POINTWISE_TERNARY §8). Let
  U = ⋃_w A(w) and K = ℤ̂ ∖ U (closed). Then ES-Type-II(p) ⟺ p ∉ K. The affine/multiplicative actions of
  ℤ on ℤ̂ give a topological-dynamics frame.

## 2. Literature anchor (from memory, unverified unless stated in the campaign files)

Margulis 1987 (Oppenheim conjecture); Eskin–Margulis–Mozes, Ann. Math. 147 (1998) (quantitative Oppenheim,
≥ 4 variables, and signature (2,1)/(2,2) exceptions); Duke–Rudnick–Sarnak, Duke Math. J. 71 (1993); Eskin–McMullen,
Duke Math. J. 71 (1993); Duke, Invent. Math. 92 (1988); Clozel–Oh–Ullmo, Invent. Math. 144 (2001);
Benoist–Oh (effective equidistribution of S-integral points; counting with congruence conditions,
uniform spectral gap via Bourgain–Gamburd–Sarnak for thin groups). The campaign's checked versions are in
LONGSHOT_FIBRED §3 (EM/EMS/BR/CTX), with the caveat recorded in (I)10.

## 3. The common collapse: the target scale (PROVED relative to the cited counting theorems in the stated form)

**Lemma B (effective equidistribution cannot see a polylog fibre).** Suppose an equidistribution theorem
counts orbit points in a target T of normalised measure μ, among N points tested, with error
`O(N^{1−δ}·Comp(T)^A)`. Here Comp(T) ≥ 1 is a complexity: Sobolev norm, level of the congruence, or
inverse width. A positive count follows only if μN ≫ N^{1−δ} Comp(T)^A.

In every encoding (H1)–(H3), the fixed-p fibre has expected size μN ≍ polylog(p). This is ET's mass:
Σ f_II ≍ N log³N, (I)3/(I)4. The complexity is a power of p:
* (H1): the congruence 4da | f + p has modulus as large as the coordinate a itself. The number of points
  of X_d of height ≤ H with a fixed congruence modulo q is asymptotic only for q ≤ H^{η}, with η depending
  on the spectral gap. Here q ≍ a ≍ H^{1/2} for the relevant points, and summing over q destroys the
  fixed residue −p (Lemma 2.1 of redteam-2: the fibre is "divisors of N_θ(p) in a class mod q_θ").
* (H2): the width is (dp)^{−1/2}, so Comp ≍ p^{1/2}. The best known reach is D^{−1/18} unconditionally
  (Young) and D^{−1/6} under Lindelöf ((I)4).
* (H3): to detect the equality you need ε < 1/(nxyz). EMM's count c·ε·T^{k−2} (k = number of variables)
  then has main term < 1. The cubic is not quadratic anyway.

So μN ≍ (log p)^3 forces N^{1−δ}Comp^A ≤ (log p)^3. That is impossible once Comp ≥ p^{c}. This is exactly
Prop 2.3 (scale constraint, B3): main term ≤ p^{o(1)} is required, while the error terms are powers of p.

**T7 / B6.** Duke, COU and Hecke-orbit theorems vary the discriminant or the Hecke operator, i.e. p
itself, or average over the full class group (size ≍ √p) to reach a set whose ES-relevant part has
polylog size. EMM/DRS count over growing regions in *all* n at once, which is interval averaging by
Prop 5.4 of (I)3. Neither gives anything at a single p.

## 4. The profinite frame (H4): a sharp reformulation and why it fails

**Prop P (PROVED, elementary).** Let Sq̄ ⊂ ℤ̂ be the closure of the squares (x is a square mod every M).
No prime lies in Sq̄: by quadratic reciprocity every prime p > 2 is a non-square modulo some prime q.
Hence *if K ⊆ Sq̄ then ES holds for every prime p > 2*. Here U is enlarged to the union of all Type I and
Type II witness classes (each is a finite union of classes mod 4cd·f, hence open), and K = ℤ̂ ∖ U. Do not
add "∪ non-units": every prime is a non-unit of ℤ̂. The statement "K ⊆ Sq̄" is pure congruence
data. Theorems M/C do not refute it, because U is an infinite union, and a non-compact open cover has no
finite subcover. So C/M only say that no finite sub-union suffices, which is consistent.

**Collapse.**
* The campaign's candidate sterile point x** = x(2, 15) has 11-adic digit 2, a non-residue mod 11. So
  x** ∉ Sq̄, and x** lies in no ES class through level 2.59·10¹⁰ (MORDELL13E, CERTIFIED).
* If x** is sterile (CONJECTURE in the campaign), then K ⊄ Sq̄ and the sufficient condition of Prop P is
  false.
* Even then, ES only needs the primes to avoid K, not K to be small. Primes are dense in ℤ̂^×, so a prime
  p close to x** (p ≡ x** mod a large M) must be covered by a witness of modulus > M. This is B1:
  Type II moduli exceed exp(c(log p)^{1/4}) infinitely often.
* The question "does the closed set K contain a prime?" therefore carries all the quantitative content of
  ES. Topology/dynamics on ℤ̂ is qualitative, and every fixed-modulus action (x ↦ ax + b) preserves the
  congruence σ-algebra, so the B1 theorems apply verbatim.

Assessment: (H4) is a clean restatement ("ES ⟺ primes ∩ K = ∅"), not a mechanism. EVIDENCE: deciding
whether x** ∈ K is itself the open MORDELL13E question.

## 5. Barrier screen

* **B1**: applies to (H4) (§4).
* **B2**: (H1)/(H2) are slices of Thm 2.2(i) (Q_d, Heegner/shell).
* **B3**: decisive (Lemma B).
* **B4**: orbit/fibred encodings with bounded covolume ratio collapse by LONGSHOT_FIBRED Thm 3.1.
  Unbounded-covolume families (thin groups, Bourgain–Gamburd–Sarnak expansion) still give
  N^{1−δ}-type errors, so Lemma B still applies.
* **B5/T1**: local, genus and spinor data hold at odd squares ((I)4 Prop 8.3). Any dynamical main term
  built from local densities (a Siegel mass) is positive at m², while the true count is 0. The false step
  is "main term dominates error", which fails at Planck scale; it is the same step as at primes.
* **B6/T7**: §3.

## 6. Viability Assessment

**COLLAPSES to B3 at the step "error ≤ main term" (Lemma B).** The ES fibre at p has polylog mass, while every
homogeneous-dynamics error term is a power of the target's complexity, and the complexity is ≥ p^c.
The profinite reformulation (H4)/Prop P is a sharp but non-mechanistic restatement. Its sufficient
condition K ⊆ Sq̄ is falsified if x** is sterile (CONJECTURE), and otherwise it is B1.

By-product: Prop P (PROVED, elementary; novelty low).
