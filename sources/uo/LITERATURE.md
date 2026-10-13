# Literature check: BV with rational moduli over number fields; unit-group Artin; exponential congruences

Legend: **[READ]** = I read the statement myself in the PDF listed. **[SEC]** = taken from a secondary
source I read (named). **[RECALL]** = from memory, not checked. Local PDFs are in this directory.

---------------------------------------------------------------------------------------------------
## Q1. Bombieri–Vinogradov with RATIONAL moduli q for prime ideals of a number field

### Murty–Petersen, "A Bombieri–Vinogradov theorem for all number fields", Trans. AMS 365 (2013) 4987–5032
File: `murty-petersen-BV-all-number-fields-eprint.pdf` (FSU e-print, Jan 2012, 40 pp). **[READ]**
* **Theorem 0.2 (= Theorem 4.1).** K/M Galois extension of number fields, M arbitrary (need not be
  Galois over Q), G = Gal(K/M), C a conjugacy class. π(x,C,q,a) = #{prime ideals p of M, unramified in K,
  σ_p = C, Np ≤ x, Np ≡ a (mod q)}, N = N_{M/Q}. Let H be the largest abelian subgroup of G with
  H ∩ C ≠ ∅, E its fixed field, **η = max{[E:Q] − 2, 2}**, Q = x^{1/η − ε}. Then for every A,
  Σ'_{q≤Q} max_{(a,q)=1} max_{y≤x} |π(y,C,q,a) − d(C,q,a)π(y)| ≪ x/(log x)^A,
  where Σ' runs only over q with **K ∩ Q(ζ_q) = Q**; d(C,q,a) = |C|/(|G|φ(q)) for those q.
* Corollary 4.2: all prime ideals of a field K, condition Np ≡ a (mod q): η = max{[K:Q] − 2, 2}.
* Authors' own words: "a value of η = 2 would be ideal, but is not within the grasp of current methods …
  this seems to be far into the future." §4.1: d = n_E can be replaced by d* = min_H max_ω [G:H]ω(1)
  (H ∩ C ≠ ∅ and all L(s, ω⊗χ) entire); under Artin's holomorphy conjecture η = max{δ,2}, δ = max|χ(1) − 2|.
  (These refinements are written in Murty–Murty's M = Q language; for M ≠ Q I read them as degrees over
  Q, i.e. they don't beat the [M:Q] loss. My reading, not explicitly stated.)
* The level is limited by the large-Q range `(log x)^γ ≤ Q ≤ min{x^{1/2−ε}, x^{1/(d−2)−ε}}` (Prop. 3.1),
  d = n_E: the twisted L-functions have conductor ≍ q^{n_E}.

**Application to the question** (my deduction from Thm 0.2, which is stated in exactly this generality):
F any number field, f a modulus, L = ray class field mod f, C ∈ Cl_f(F). Take M = F, K = L. G = Gal(L/F)
is abelian ⇒ H = G, E = F. So, unconditionally,
  Σ'_{q ≤ x^{θ}} max_a |#{P: NP ≤ x, [P] = C, NP ≡ a (q)} − x/(h_f φ(q) log x)| ≪ x/log^A x
for **θ < 1/max{[F:Q] − 2, 2}**, Σ' over q with L ∩ Q(ζ_q) = Q (excludes q divisible by the conductor of
some nontrivial abelian-over-Q subfield of L). Degree ≥ 2 primes contribute ≪ x^{1/2} log x in total.
⇒ **Level 1/2 holds for [F:Q] ≤ 4 (Galois or not). For [F:Q] ≥ 5 level 1/2 is NOT known unconditionally**
(only 1/([F:Q]−2) from MP; see Jiang–Lü–Wang below). Using M = Q and the Galois closure instead does not
help in general: one needs an abelian subgroup of Gal(K̃/Q) of small index meeting the class.

### M. R. Murty & V. K. Murty, "A variant of the Bombieri–Vinogradov theorem", Number Theory (Montreal 1985), CMS Conf. Proc. 7 (1987) 243–272
Not available online; statements **[SEC]** from Harper–Murty CJM 2004 (Props 3, 4), Murty–Petersen 2009
(Prop 3.1) and Thorne (bounded gaps, Lemma 3.1/(3.4)):
* K/Q Galois, G, C. Basic theorem: level α with **α ≤ min(2/|G|, 1/2)** (HM Prop 3; MP2009 phrases it as
  η ≥ max(|G|/2, 2)), sum over q with K ∩ Q(ζ_q) = Q.
* Improvement "[MM, p. 269]" / "Section 7 (Thm 7.3, §7.4)": for any abelian A ≤ G with A ∩ C ≠ ∅,
  d = [G:A]: **η = d − 2 if d ≥ 4, η = 2 if d ≤ 4**; d may be replaced by d* as above; under Artin
  holomorphy d* = max_χ χ(1). Thorne: θ = 1/max(2, i − 2), i = index of largest abelian subgroup meeting C.

### Other BV-over-number-field results (none give rational-moduli level 1/2 for deg ≥ 5)
* Thorner, "A variant of the BV theorem in short intervals…", Math. Proc. Camb. Phil. Soc. (2016),
  arXiv 1405.5486 — `thorner-1405.5486.pdf` **[READ]**: restates MP as level 1/max{[E:Q]−2,2} (eq. 1.8);
  Thm 1.1 short-interval version with 0 ≤ θ < (1/3)(2/(5[E:Q]) − δ).
* Jiang–Lü–Wang, "A Bombieri–Vinogradov theorem for number fields", Mathematika 67 (2021) 678–713.
  Abstract **[READ via OpenAlex]**: "We refine the level of distribution in the previous work of
  Murty–Petersen" (+ short-interval version, numerical improvements for Euclidean S-integers).
  **Exact new level NOT verified** (paywalled, not on arXiv). Guess (unverified): the improved Type-I
  bound of Jiang–Lü–Thorner–Wang (η = max{n/2, 2}) suggests ≈ 1/max{n_E/2, 2}.
* Jiang–Lü–Thorner–Wang, "A BV theorem for higher rank groups", arXiv 2104.02711 (IMRN) **[READ]**:
  ideal moduli m of F weighted by h(m)/φ_F(m); Thm 1.1 level Q = x^{1/η}, η = max{2, n/2} (π self-dual cuspidal
  on GL_n/F, not a quadratic twist of itself; same η as Type-I Thm 1.3 — consistent with their n ≤ 4
  Titchmarsh application). Over F = Q with π on GL_n (n ≤ 4) this gives rational
  moduli at level 1/2 — relevant only if one can write the count as λ_π(p) of an automorphic π/Q.
* Huxley, J. London Math. Soc. (2) 3 (1971) 233–240 (large sieve for number fields III); Wilson,
  Mathematika 16 (1969) 189–204; Hinz, Acta Arith. 51 (1988) 173–193 (prime elements in boxes, ideal
  moduli). **[SEC: Baier–Molla arXiv 2509.03657 intro, `baier-2509.03657.pdf`]**: these are BV with
  IDEAL moduli m (level 1/2 in Nm). For rational q, N(qO_F) = q^{[F:Q]}, so only q ≤ x^{1/(2[F:Q])}.

---------------------------------------------------------------------------------------------------
## Q2. Unconditional Artin for unit groups ("O_K^× ↠ (O_K/P)^×")

Common skeleton (all Murty-school papers): (i) lower-bound linear sieve (Iwaniec) + BV of level 1/η gives
≫ x/log²x primes p ≤ x in a Chebotarev class with every prime ℓ | (p−1)/t_K exceeding x^{1/(2η)−ε}
(t_K = #roots of unity-type constant); (ii) then index [(O/P)^× : im O^×] is 1 or > x^{1/(2η)−ε}, so
|im O^×| < x^{1−1/(2η)+ε}; (iii) Gupta–Murty counting bound kills these if **(1 − 1/(2η))(1+1/r) < 1,
i.e. 2η < r + 1**. With η = 2 (level 1/2) this is **r ≥ 4** — that is the origin of the rank threshold.
Rank 3 would need level > 1/2 (BFI/Fouvry–Iwaniec), available only in abelian-over-Q settings.

### Gupta–Murty counting lemma
* Gupta & Murty, "A remark on Artin's conjecture", Invent. Math. 78 (1984) 127–130 —
  `gupta-murty-1984-invent.pdf` (GDZ scan) **[READ]**. Entirely over Q (13-element set S built from three
  primes q,r,s). **Lemma 2**: Γ = ⟨q,r,s⟩: #{p : |Γ_p| < y} = O(y^{4/3}). Lemma 1: ≫ x/log²x primes with
  all odd prime factors of p−1 > x^{α}, α = 1/4 − ε (Iwaniec + BV), and they assume α = 1/4+ε via
  Fouvry–Iwaniec to optimise. No number-field statement in this paper.
* Number-field form, **[READ]** in Murty–Petersen 2009 Prop 3.2 and Harper–Murty Prop 6 (both cite [GM]):
  K any number field, M ⊂ O_K a monoid with r multiplicatively independent elements:
  **#{P : |M mod P| ≤ Y} ≪ Y^{(r+1)/r}** (P over prime ideals coprime to M). Proof: pigeonhole among
  exponent vectors of ℓ¹-norm ≤ Y^{1/r}; P | N(b^{a} − 1) for a nonzero short vector; each norm has
  O(Y^{1/r}) prime factors. Full proof also in Graves' thesis Thm 2.3.5 (`graves-2009-dissertation.pdf`).
  (Matthews' Bull. LMS-type version: [RECALL], not checked.)

### Harper & Murty, "Euclidean rings of algebraic integers", Canad. J. Math. 56 (2004) 71–76 — `harper-murty-2004-cjm.pdf` **[READ]**
* Thm 1: K/Q finite Galois, unit rank **r > 3** ⇒ (O_K Euclidean ⇔ PID). Cor: Galois of degree > 8.
* Key lemma (§5): #{π : Nπ ≤ x, π of degree one (p splits completely), O_K^× mod π = (O_K/π)^×}
  ≫ x/log²x. Via Prop 2 (Harper's large-sieve criterion: B_1(x) ≫ x/log²x ⇒ Euclidean).
* Prop 5 (sieve): K/Q Galois, t = max{m : ζ_m ∈ K}, η from Prop 4 with **C = {1}**: ≫ x/log²x primes
  p ≤ x splitting completely in K with every ℓ | (p−1)/t satisfying ℓ > x^{1/(2η)−ε}.
* **Where Galois is used:** (a) "P degree one" is encoded as "p splits completely in K" = Chebotarev class
  {1} in Gal(K/Q), so ANY abelian A ≤ G meets C and d = [G:A] can be made small; (b) group theory: an
  abelian A of order e ≥ 4 gives d−2 < (r+1)/2 since r ≥ (n−2)/2 > 2n/e − 5; if no such A then |G| | 6;
  the non-abelian n = 6 (S_3) case uses that Artin holomorphy is known for S_3 (η = 2).
* No ray-class/Frobenius condition on P; no condition on Np mod q in this paper.

### Murty & Petersen, "The generalized Artin conjecture and arithmetic orbifolds", Groups and Symmetries, CRM Proc. Lecture Notes 47 (2009) 259–265 — `murty-petersen-2009-artin-orbifolds.pdf` **[READ]**
* **Thm 1.2**: K/Q finite Galois, unit rank > 3, 1 ≤ a < q, (a,q) = 1, **Q(ζ_q) ∩ K = Q**. Then infinitely
  many degree-one prime ideals π with |N π| ≡ a (mod q) and O_K^× ↠ (O_K/π)^×. (Proof gives ≫ x/log²x,
  Prop 3.3.) Mechanism: L = K(ζ_q), G ≅ (Z/q)^× × Gal(K/Q), class C = (a, 1); abelian A = (Z/q)^× × B with
  B ≤ Gal(K/Q) abelian, d = [Gal(K/Q):B]; same group theory as Harper–Murty.
* So a prescribed residue class of N(P) mod a fixed q IS allowed (q fixed; sieve moduli vary).
* §5: non-Galois K left open ("one would have to extend [MM] to the non-Galois situation").

### Murty & Petersen, "The Euclidean algorithm for number fields and primitive roots", Proc. AMS 141 (2013) 181–190 — `murty-petersen-eprint-euclid-primroots.pdf` (preprint) **[READ]**
* **Thm 1.3**: K number field, unit rank ≥ 4, and a subfield M with **K/M Galois, |Gal(K/M)| ≥ 4**. Then
  ≫ x/(log x)² prime ideals p of K with O_K^× ↠ (O_K/p)^×. Thm 1.4: then PID ⇔ Euclidean.
  Cor 1.5: totally real K of degree ≥ 5 having a proper subfield M with K/M Galois.
* Uses MP BV (base M) with C = "split completely in K, not split in Kummer fields K_ℓ (ℓ | t_K)"
  (Lemma 3.2) in L = K(ℓ-th roots of units)/M; η = max{n_E − 2, 2}, E fixed field of an abelian A ≤ Gal(K/M).
* **Caveat (my reading):** Lemma 3.2's claim "A lifts to an abelian subgroup of G (=Gal(L/M)) meeting C"
  is justified only by "G/H = N with H abelian", which does not by itself give an abelian lift with the
  same fixed field. Worth checking before relying on it.
* Non-Galois-over-every-subfield K and small degree: still open (authors' remark).

### Gupta, Murty, Murty, "The Euclidean algorithm for S-integers", CMS Conf. Proc. 7 (1987) 189–201
**[SEC: Moree survey Thm 7, `moree-artin-survey-2012.pdf` §9.6]**: K Galois over Q, g = gcd(NP − 1 :
P ∈ S∖S_∞). If (a) |S| ≥ max(5, 2[K:Q] − 3) and (b) K has a real embedding or ζ_g ∈ K, then R_S is
principal iff Euclidean. Uses Gupta–Murty + Murty–Murty BV. (2[K:Q]−3 reflects the level 1/(|G|/2)-type
basic MM theorem.)

### Clark & Murty, "The Euclidean algorithm for Galois extensions of Q", J. reine angew. Math. 459 (1995) 151–162
Not read. **[SEC]**: introduces admissible sets of primes (Harper–Murty §2; Srinivas–Subramani–Sangale
arXiv 2108.08049: suffices to check units ↠ (O/π_1²…π_s²)^×, p.160); Harper's Z[√14] abstract: "a theorem
of Clark and Murty giving a similar result when K is a totally real extension of degree at least three"
(presumably Galois, with an admissible prime). Exact hypotheses **unverified**.

### Narkiewicz
* "Units in residue classes", Arch. Math. 51 (1988) 238–241. **[SEC: Schinzel, "The work of W. Narkiewicz",
  Funct. Approx. 39 (2008), and MP-PAMS intro]**: if K ≠ Q is **real abelian**, there are infinitely many
  first-degree P such that every nonzero residue class mod P contains a unit, **with at most two
  exceptional fields** (either a single cubic one, or at most two quadratic ones). Method: Heath-Brown's.
  (Abelian ⇒ "split completely" is a congruence condition on p, so BV/Fouvry–Iwaniec over Q at level > 1/2
  can be used; that is why no rank ≥ 4 condition appears.)
* "A note on Artin's conjecture in algebraic number fields", J. reine angew. Math. 381 (1987) 110–115
  **[SEC: Moree §6.1.1, Schinzel]**: for a subclass of abelian fields (conductor conditions), of three
  multiplicatively independent a_1,a_2,a_3 ∈ O_K with norm conditions, one is a primitive root for
  infinitely many first-degree P.
* "Euclidean algorithm in small abelian fields", Funct. Approx. 37 (2007) 337–340 **[SEC]**: at most two
  real quadratic PID fields are non-Euclidean; at most one cyclic (Galois) cubic.

### Heath-Brown, "Artin's conjecture for primitive roots", Quart. J. Math. Oxford (2) 37 (1986) 27–38
**[SEC Moree survey; RECALL]**: lower-bound sieve + Chen–Iwaniec switching gives ≫ x/log²x primes with
p−1 = 2^e q or 2^e q_1q_2, p^{1/4} < q_1 < p^{1/2−δ}; ⇒ Artin for all but ≤ 2 primes / ≤ 3 squarefree.
Over Q (abelian) only; uses level > 1/2 (BFI/Fouvry–Iwaniec).

### Prescribed RAY CLASS for P — assessment (my analysis, no source found)
No paper found that allows "P in a prescribed ray class mod f" together with units ↠ (O/P)^×. With the
available tools it fails generically: impose the class via the ray class field K_f; the Frobenius class
then lies in Gal(L'/K) (L' = K_f·Kummer fields), whose natural abelian subgroup has fixed field E = K,
η = max{n_K − 2, 2}, and 2η < r+1 ≤ n_K is impossible for every K (n_K ≤ 4 ⇒ r ≤ 3; n_K ≥ 5 ⇒ 2n_K−4 ≥ n_K).
Works only if Gal(L'/Q) has a large abelian subgroup meeting the class (e.g. conditions that factor
through N(P) mod q, as in MP2009; or everything abelian over Q).

---------------------------------------------------------------------------------------------------
## Q3. Exponential congruences / two-variable Artin / power sums

Observation: for q ∤ abε, q | a + bε^k for some k ⇔ −a/b ∈ ⟨ε⟩ mod q. So "prime factors of a + bε^k"
= the two-variable Artin set P(ε, −a/b).

* **Schinzel, "Abelian binomials, power residues and exponential congruences", Acta Arith. 32 (1977)
  245–274** — `schinzel-1977-aa32-abelian-binomials.pdf` (scan; OCR'd pp. 1–3) **[READ]**. Thm 5: K number
  field, f ∈ K[t] of degree g, α_1…α_k ∈ K^×. If f(α_1^{x_1}⋯α_k^{x_k}) ≡ 0 mod p is soluble for almost all
  prime ideals p (all but a density-zero set), then f(α_1^{x_1}⋯α_k^{x_k}) = 0 is soluble in rationals with
  common denominator ≤ max{1, g−1}. Corollary: second-order integer recurrence u_n, if u_n ≡ c (mod p)
  soluble for almost all p and (b = 0, −1, or b = 1, a ≠ d²±3d…), then c = u_m. Thm 4: Chebotarev-type
  existence of prime ideals with prescribed n-th power residue symbols (Kummer/Čebotarev refinement).
  Note: these are failure-of-local-global statements (give positive upper density of p where a ∉ ⟨b⟩),
  not existence of p with a ∈ ⟨b⟩ in a class.
* Schinzel, "On power residues and exponential congruences", Acta Arith. 27 (1975) 397–420: PDF behind
  bot-wall (matwbn.icm.edu.pl). [RECALL]: Thm 2 = k = 1 linear case of the above (b^x ≡ a mod p for almost
  all p ⇒ a = b^n), over any number field.
* **Moree–Stevenhagen, "A two-variable Artin conjecture", J. Number Theory 85 (2000) 291–304**,
  arXiv math/9912250 — `moree-stevenhagen-math9912250.pdf` **[READ]**. Thm 1 (unconditional; special case
  of Pólya): a, b ∈ Q^× multiplicatively independent ⇒ {p : b ∈ ⟨a⟩ mod p} infinite. Thm 2 (GRH): density
  δ(a,b) = c_{a,b} ∏_p (1 − p/(p³−1)), c_{a,b} ∈ Q_{>0}. They state explicitly: positive lower density
  is NOT known unconditionally; "the best unconditional result available is Theorem 1". Multiplicatively
  dependent a, b: density unconditional (Stevenhagen, torsion sequences; Hasse-type).
* **Murty–Séguin–Stewart, JNT 194 (2019) 8–29**, arXiv 1711.06410 — `murty-seguin-stewart-1711.06410.pdf`
  **[READ]**: Thm 1.1: a, b ∈ Z^×, |a| ≠ 1 ⇒ #{p ≤ x : b ∈ ⟨a⟩ mod p} ≫ log x (unconditional). Thm 2.1:
  ω(∏_{n≤N} u_n) > (1 − 1/√2 − ε)N for non-degenerate binary recurrences. Disjunction theorem with Artin.
* **Hazra–Murty–Sivaraman, "A note on the two variable Artin's conjecture", JNT 262 (2024) 161–185** —
  `hazra-2024-two-variable-artin.pdf` **[READ abstract/intro]**: for m_1,m_2,m_3 multiplicatively independent
  with m_i, −3m_im_j, m_1m_2m_3 non-squares, some pair (a,b) from S has ≫ x log log x / log²x primes with
  a ∈ ⟨b⟩ mod p. The proof works inside an arithmetic progression p ≡ u (mod v) (so congruence conditions
  are built in), but no general "prescribed Chebotarev class" theorem is stated.
* **Nothing found** that unconditionally gives, for fixed multiplicatively independent a, b, a prime q in an
  arbitrary prescribed Chebotarev class with a ∈ ⟨b⟩ mod q. (Infinitely many q without class condition:
  Pólya/MS Thm 1. Dependent a, b: Chebotarev in Kummer fields suffices.)
* **Corvaja–Zannier**: [SEC: Bilu, "The many faces of the subspace theorem", Astérisque 317 (2008),
  arXiv 0907.2098, Thm 4.1]: Q-power sum u with positive roots, u(n) a q-th power for infinitely many n
  ⇒ u = (Q̄-power sum)^q, and u(Qn+R) = w(n)^q (Cor 4.2); also P(u(n), y) = 0 with infinitely many
  solutions ⇒ y = v(n) power sum on a progression (Corvaja–Zannier, Indag. Math. 9 (1998) 317–332,
  [RECALL]). **No result found** on a + bε^k being a norm from a quadratic field, or having all prime
  factors split in a fixed quadratic field, for all/infinitely many k. (Trivial examples exist, e.g.
  4^k + 1 = (2^k)² + 1.) Flag as open/unknown to me.
