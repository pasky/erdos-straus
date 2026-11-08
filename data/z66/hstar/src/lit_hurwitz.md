# Literature check: arithmetic in Hurwitz realizability and lifting invariants

Flags: **V** = read statement in the cited source; **V2** = statement verified only through a secondary source; **NOT FOUND** = no reliable statement located. Branch-data notation below is the unordered partition notation of the sources. “Realizable” means realized by a branched cover with the indicated surfaces/degree/branch points.

## (a) Arithmetic-dependent realizability

### (a1) Corvaja–Petronio–Zannier
**Bibliography:** Pietro Corvaja, Carlo Petronio, Umberto Zannier, “On certain permutation groups and sums of two squares,” *Elemente der Mathematik* **67** (2012), no. 4, 169–181. Preprint arXiv:0810.0591 (2008).
**Source read:** https://arxiv.org/html/0810.0591v1 — **V**.
**Theorem 1.1 (the paper restates the result as [4, Theorem 0.4]):** for `d=4k+1`, the following are equivalent: (I) there is a degree-`d` cover of `P¹(C)` ramified over three points with branching types `(1,4,…,4)`, `(1,4,…,4)`, `(1,2,…,2)`; (II) `d=x²+y²` for integers `x,y`. Near-verbatim source quote: “There exists a branched cover … of degree d … with branching types …” iff “d = x² + y² for some x,y ∈ N.” The source’s remark says these types force the source to be `P¹` as well. Thus this is exactly an arithmetic obstruction, not merely a group-theoretic analogy. For odd d, x,y necessarily have different parity. (The paper writes natural numbers; allowing zero gives the same criterion here.)

### (a2) Petronio survey
**Bibliography:** Carlo Petronio, “The Hurwitz existence problem for surface branched covers,” *Winter Braids Lecture Notes* **7** (Winter Braids X, 2020), Exposé 2, 1–43. DOI 10.5802/wbln.34.
**Source read:** https://www.numdam.org/item/10.5802/wbln.34.pdf — **V**.
- **Theorem 3.13:** `(S,S,d,3; [2,…,2,1], [4,…,4,1], [4,…,4,1])` is realizable iff `d=x²+y²` with `x,y∈Z` of different parity. Quote: “is realizable if and only if d = x² + y² with x, y ∈ Z of different parity.”
- Immediately after Theorem 3.13 the survey gives the related variants (not separately numbered): `(S,S,4k+2,3; [2,…,2], [4,…,4,2], [4,…,4,1,1])` iff `d=2(x²+y²)`; and `(S,S,4k+4,3; [2,…,2], [4,…,4], [4,…,4,2,1,1])` iff `d=4(x²+y²)`.
- **Theorem 3.14:** each of `(S,S,d,3; [2,…,2,1], [3,…,3,1], [6,…,6,1])` and `(S,S,d,3; [3,…,3,1], [3,…,3,1], [3,…,3,1])` is realizable iff `d=x²+xy+y²`, `x,y∈Z`. Quote: “are realizable if and only if d = x² + xy + y².”
- On other arithmetic conditions: section 2.7, Definition 2.12/Proposition 2.13, uses `k|d` for block decompositions/factorization of covers (a structural criterion, not a degree-only iff obstruction). Theorems 3.13–3.14 and the immediately stated variants are the survey’s explicit degree arithmetic iff results located in this review. They are quadratic norm forms with asymptotic zero-density degree sets, not perfect-square criteria.

### (a3) Pakovich / Laurent passports
**Bibliography:** Fedor Pakovich, “Solution of the Hurwitz problem for Laurent polynomials,” *Journal of Knot Theory and Its Ramifications* **18** (2009), no. 2, 271–302; arXiv:math/0611776.
**Source read:** https://www.math.bgu.ac.il/~pakovich/Publications/lau.pdf — **V**.
**Theorem 1.1:** for a Laurent passport (one partition has two elements), if `q>3` it is always realizable. If `q=3`, it is realizable iff it is not one of seven listed triplets. Relevant families include (1) `Π₁={l,…,l}`, `Π₂={1,…,1,d}`, `Π₃={s,n−s}`, with `d≥3,l≥2,s≥1,s≡0 (mod l)`; and (2) `Π₁=Π₂={2,…,2}`, `Π₃={s,n−s}`, with `s≥1,s≠n/2`. Other exceptions are the theorem’s listed specific families (including the exceptional degree-6 triplet). This is a classification of **nonrealizability** in the Laurent setting; it includes divisibility/modular conditions on `s`, not a general “d is square” criterion. Quote: “A Laurent passport Π for which q=3 is realizable if and only if Π is distinct from the triplets listed below.” This addresses a two-part partition `[k,d−k]` only within that specific Laurent-passport framework; do not read it as a classification of all sphere branch data.

### (a4) Pervova–Petronio
**Part I bibliography:** Ekaterina Pervova, Carlo Petronio, “On the existence of branched coverings between surfaces with prescribed branch data, I,” *Algebraic & Geometric Topology* **6** (2006), 1957–1985. Source: https://arxiv.org/pdf/math/0508434 — **V**.
- **Proposition 1.2:** even-degree sphere-to-sphere compatible data with three branch points and first partition `(2,…,2)`; for source torus, realizability iff its third-branch partition is not `(d/2,d/2)`; for source sphere (four third-partition entries), realizability iff that partition is neither `(k,k,d/2−k,d/2−k)` nor (when `6|d`) `(d/2,d/6,d/6,d/6)`.
- **Proposition 1.3:** for even `d` and first partition `(2,…,2)`, when the second partition is `(3,3,2,…,2)` or `(3,2,…,2,1)`, realizability iff the first entry of the third partition is not `d/2`.
- **Theorem 1.4 (necessary divisor criterion):** “Suppose that d and all dᵢⱼ for i=1,2 are multiples of some k with 1<k<d. If … realizable then dᵢⱼ≤d/k for i=3,…,n and all j.”
- **Theorem 1.5:** if `d` and all entries in the first two partitions are even, then every later partition refines `(d/2,d/2)` if realizable. Corollary 1.6 gives further necessary bounds involving `2k|d`. These are divisibility/factorization constraints and exhibit composite-degree exceptional families; they are not an iff “d square” statement.

**Part II bibliography:** Ekaterina Pervova, Carlo Petronio, “On the existence of branched coverings between surfaces with prescribed branch data, II,” *Journal of Knot Theory and Its Ramifications* **17** (2008), no. 7, 787–816. Search located arXiv:math/0611267, https://arxiv.org/abs/math/0611267. No separate Part-II gcd/divisor iff criterion was verified here; **NOT FOUND** for an additional such criterion. (Part I supplies the explicit divisibility criteria above.)

### (a5) Perfect-square / residue-class screening
No exact family found in the checked sources whose nonrealizability is **equivalent to d being a perfect square**, nor a verified family “realizable iff d has a divisor in a specified residue class.” The strong positive matches are CPZ/Petronio’s sum-of-two-squares and Eisenstein norm conditions, and Pakovich/Pervova–Petronio’s congruence/divisibility constraints on partition entries. Treat these as distinct patterns; no implication to an Erdős–Straus square obstruction is established by these references. **NOT FOUND** for a perfect-square iff family in the reviewed sources.

### (a6) EKS and Barański
**Edmonds–Kulkarni–Stong bibliography:** Allan L. Edmonds, R. S. Kulkarni, R. E. Stong, “Realizability of branched coverings of surfaces,” *Transactions of the American Mathematical Society* **282** (1984), no. 2, 773–790. The requested **Proposition 5.7** exact text was not directly retrieved. Pervova–Petronio I, p. 1964, explicitly attributes to [4, Proposition 5.7] the result: **“For all non-prime d there exist exceptional branch data of degree d with n=3 and Σ̃=S.”** In other words, every composite degree has at least one compatible but nonrealizable 3-branch-point sphere datum; this is not the claim that a particular fixed datum fails exactly at square degrees. URL read for this statement: https://arxiv.org/pdf/math/0508434 — **V2** (secondary quotation; not original proposition).

**Barański bibliography:** Krzysztof Barański, “On realizability of branched coverings of the sphere,” *Topology and its Applications* **116** (2001), no. 3, 279–291. Search identified the paper and its description as a geometric method for deciding realizability, but its theorem text was not checked at source: **NOT FOUND** for an exact arithmetic theorem to quote. No arithmetic-degree iff result attributed to it here.

## (b) Serre lifting obstruction / theta characteristics

**Serre bibliography:** Jean-Pierre Serre, “Revêtements à ramification impaire et thêta-caractéristiques,” *Comptes Rendus de l’Académie des Sciences de Paris, Série I Mathématique* **311** (1990), 547–552. The original note’s full theorem text was not available among sources retrieved. **Important verified secondary source:** Michael D. Fried, “Alternating groups and moduli space lifting invariants,” *Israel Journal of Mathematics* **179** (2010) (page range not verified; arXiv:math/0611591), https://arxiv.org/pdf/math/0611591 — **V** for Fried’s statements below, but **V2** for attributing the formula to Serre.

Fried §2.3, Corollary 2.3, defines for odd-order `g∈Aₙ` `w(g)` as the sum over disjoint cycle lengths `ℓ` of `(ℓ²−1)/8 mod 2`; for a genus-zero Nielsen class of odd-order branch cycles `g=(g₁,…,gᵣ)`, the spin/lifting invariant is constant and equals `s(g)=(-1)^{Σᵢw(gᵢ)}`. Near-verbatim quote: “Generally, for any genus 0 Nielsen class of odd order elements … s(g) is constant, equal to (−1)^{Σᵢw(gᵢ)}.” For a cycle type with all ramification indices odd, this is the requested `(-1)^{Σ_cycles(e²−1)/8}` formula. Fried §6.15 / p. 36 explicitly calls this “Serre’s formula written multiplicatively” and connects it to theta characteristics. I did **not** verify the original Serre note’s precise general theta-characteristic theorem statement; exact original wording/theorem number: **NOT FOUND**.

Serre’s “L’invariant de Witt de la forme Tr(x²),” *Commentarii Mathematici Helvetici* **59** (1984), 651–676, bibliographic source https://eudml.org/doc/139995. Springer PDF found: https://link.springer.com/content/pdf/10.1007/BF02566371.pdf. Its main formula was not read/verified in this bounded pass; **NOT FOUND** for an exact theorem/formula (do not infer it from the title or snippets).

## (c) Fried: 3-cycles in alternating groups

**Bibliography:** Michael D. Fried, “Alternating groups and moduli space lifting invariants,” *Israel Journal of Mathematics* **179** (2010) (page range not verified); arXiv:math/0611591 (preprint 2006). **Source read:** https://arxiv.org/pdf/math/0611591 — **V**.

Write `H(Aₙ,C₃ʳ)^{in}` for inner and `H(Aₙ,C₃ʳ)^{abs}` for absolute Hurwitz spaces, with `r` branch cycles all 3-cycles. **Theorem 1.2:** for `r=n−1`, `n≥5` (genus-zero degree-`n` covers), the inner space has exactly one connected component; the inner-to-absolute map has degree 2. Quote: “For r=n−1, n≥5, H(Aₙ,C₃ⁿ⁻¹) has exactly one connected component.” The unique spin value is `(-1)^{n−1}` (Corollary 2.3 gives the genus-zero invariant).

**Theorem 1.3:** for every `r≥n≥5`, the inner space has exactly two connected components, `H₊` and `H₋`, distinguished by lifting invariant `+1` and `−1`; each maps with degree 2 to its connected image in the absolute space. Quote: “For each r≥n≥5 … has exactly two connected components.” Therefore the genus-zero case `r=n−1` has one, while `r≥n` has two. Fried’s abstract/main-result discussion says spin/half-canonical invariant parity identifies them. This is a topological/moduli component count, not degree-square dependence.
