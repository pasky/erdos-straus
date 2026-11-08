# Precedents from combinatorics / Diophantine approximation — literature verification

Access date for every URL below: **2026-11-08** (system clock of the verifying machine).
Status marks: **V** = read in the source itself; **V2** = read in a later source (named); **NA** = not accessed.
Quotes are taken from `pdftotext` / OCR output (OCR = tesseract on scanned PDFs, checked against
page images where formulas were garbled). `[...]` marks my ellipsis; `<...>` marks a formula
I reconstructed from a garbled text layer (reason given each time).

Legend for the notes: (i) pointwise for every input in an infinite class? (ii) expected number of
witnesses in the guaranteed window; (iii) proof mechanism; (iv) does the analogue fail on an
explicit infinite set / at composite inputs?

---

## 1. Hurwitz existence problem — the prime-degree conjecture

### 1a. Edmonds–Kulkarni–Stong 1984 — **V**
- A. L. Edmonds, R. S. Kulkarni, R. E. Stong, *Realizability of branched coverings of surfaces*,
  Trans. Amer. Math. Soc. 282 (1984), no. 2, 773–790.
- Accessed: https://courses.mai.liu.se/GU/TA1022/Edmonds-Branched%20coverings.pdf (a 10-page scan
  of the article, AMS pages incl. 773–775, 786–787; the AMS-hosted PDF was behind a Cloudflare check).
- The conjecture is only posed as a **question**. It is not a numbered conjecture in EKS:
  - p. 774, after the theorems: "(1) To what extent can the bound n(d) = 3(d − 1) above be improved? In
    particular, if d is prime, is every element of A(d) realizable by a connected branched covering of S²?"
  - p. 775: "the results of §5 reduce the problem when d is prime to the consideration of the 3 branch
    point case. But to date no conclusive results have been obtained."
  - p. 787 Remark: "One would also like to decide whether all allowable data 𝒟 is realizable when d is
    prime. The reduction techniques of this section reduce the latter question to the case of data with
    just 3 entries. Hand and computer checks have shown that the answer is yes for d = 3, 5, 7."
- Composite degree always fails (p. 774): "Theorem. If d is not prime, then there exists 𝒟 ∈ A(d) which
  is not the branch data for a connected branched covering of S²." Proved as **Proposition 5.7** (p. 786):
  "If d = ab, a, b > 1, then 𝒟 = {[a,...,a], [b+1,1,...,1], [a, a(b−1)]} satisfies v(𝒟) = 2d − 2, but is
  nonrealizable." Proof: fix β = (1,...,b+1), enumerate transitive α of type [a,...,a]; then αβ ∈ [x, d−x]
  with a ∤ x.
- Degree 4: p. 774: "The elements of A(4) are realizable with the exception of the sequence of data of the
  form {[3,1], [2,2], ..., [2,2]}." So ([2,2],[2,2],[3,1]) is non-realizable (it is Prop. 5.7 with
  a = b = 2), and there is an infinite sequence of non-realizable data in the single degree 4.
- Also **Corollary 6.4** (p. 787): "If d = 2r, then the data 𝒟 = {[x, 2r − x], [2,...,2], [2,...,2]},
  with x ≤ r, is realizable as the branch data for a connected branched covering of S² if and only if
  x = r." (An infinite family, all of even degree.)
- Also (p. 774): "If d ≠ 4, then there are at most finitely many elements of A(d) which are not
  realizable [...] In particular, if v(𝒟) ≥ n(d) = 3(d − 1) then 𝒟 is realizable."

### 1b. Pascali–Petronio — **V**
- M. A. Pascali, C. Petronio, *Branched covers of the sphere and the prime-degree conjecture*,
  arXiv:1010.2888 (v2, 15 Jan 2011); Ann. Mat. Pura Appl. 191 (2012) 563–594 (journal data V2 from
  Petronio's survey, ref. [28]). URL: https://arxiv.org/abs/1010.2888 (PDF https://arxiv.org/pdf/1010.2888).
- **Conjecture 1.2**: "If Σ̃ ⇢ S [degree d:1, data Π] is a candidate surface branched cover and the
  degree d is a prime number then the candidate is realizable." Attributed to EKS [2], "appears to be
  still open". **Proposition 1.3** (EKS): "If Conjecture 1.2 is true for candidate surface branched
  covers having n = 3 branching points, then it is true in general."
- "all exceptional candidate surface branched covers with n = 3 and d ≤ 20 were determined by computer
  in [25] [Zheng]. There are very many of them, but none occurs for prime d."
- Key remark (§2): for three families in the Euclidean subproblem "the candidate cover is 'exceptional
  with probability 1,' even though it is realizable when its degree is prime".
- §3: "all the exceptional candidates we have found occur for composite degree".

### 1c. Petronio survey (2020) — **V**
- C. Petronio, *The Hurwitz existence problem for surface branched covers*, Winter Braids Lecture Notes
  7 (2020), Course no. II, pp. 1–43, doi:10.5802/wbln.34. URL: https://www.numdam.org/item/10.5802/wbln.34.pdf
- §1.10, **Proposition 1.18**: "If d is a composite integer then there exist exceptional candidate branch
  data of the form (S, S, d, 3; π1, π2, π3)." Proof (dessins d'enfant): d = ab, π1 = [a,...,a],
  π2 = [b+1,1,...,1], π3 = [qa, (b−q)a] <variable letters were lost by the PDF font; reconstructed from
  EKS Prop. 5.7 and the proof text "Since 1 + y + x is never a multiple of a">.
- Then: "Prime-degree conjecture: If d is a prime number then every candidate branch datum
  (Σ̃, S, d, n; π1,...,πn) is realizable." **Proposition 1.19** = reduction to n = 3.
- **Theorem 3.13**: "(S, S, d, 3; [2,...,2,1], [4,...,4,1], [4,...,4,1]) is realizable if and only if
  d = x² + y² with x, y ∈ Z of different parity." Followed by: the odd d = x²+y² have density 0, "However
  an old theorem of Fermat says that an odd prime is always the sum of two squares. So the candidate
  branch datum [...] is exceptional with probability 1 but realizable when the degree is a prime."
  (Note: the partitions force d ≡ 1 mod 4, so the relevant primes are p ≡ 1 mod 4; the survey's
  phrase "an odd prime is always" is loose.)
- **Theorem 3.14**: data ([2..2,1],[3..3,1],[6..6,1]) and ([3..3,1]³) "are realizable if and only if
  d = x² + xy + y²"; "a prime of the form 3k + 1 [...] can always be written as x² + xy + y² by a result of
  Gauss."
- §3.9: Zieve's conjecture (private comm. 2019) would imply the prime-degree conjecture because "All the
  exceptional data of [27] occur when the degree is composite."
- §2.2: Zheng [H. Zheng, *Realizability of branched coverings of S²*, Topology Appl. 153 (2006)
  2124–2134] — complete computer classification for d ≤ 20 (via generating functions/characters of S_d).

### 1d. Pakovich, Laurent polynomials — **V**
- F. Pakovich, *Solution of the Hurwitz problem for Laurent polynomials*, arXiv:math/0611776 (v2, 2007);
  J. Knot Theory Ramifications 18 (2009) 271–302 (journal data V2 from Petronio's survey ref. [25];
  note: **not** "Moscow Math. J."). URL: https://arxiv.org/abs/math/0611776
- Intro: "the collection {2, 2}, {2, 2}, {3, 1} is compatible with (1) nevertheless it can not be the
  branch datum of a rational function (see [2], Corollary 6.4 and the Theorem below)."
- Main **Theorem** (unnumbered): "Any Laurent passport Π for which q > 3 is realizable. A Laurent passport
  Π for which q = 3 is realizable if and only if Π is distinct from the triplets listed below:
  1) {l,...,l}, {1,...,1,d}, {s, n−s}, where d ≥ 3, l ≥ 2, s ≥ 1, s ≡ 0 mod l,
  2) {2,...,2}, {2,...,2}, {s, n−s}, where s ≥ 1, s ≠ n/2,
  3) {2,...,2}, {1,...,1,d−1,d}, {2d−3, n−2d+3}, where d ≥ 3,
  4) {2,...,2}, {1,...,1,d,d}, {2d−3, n−2d+3}, where d ≥ 3,
  5) {2,...,2}, {1,...,1,d,d}, {2d−1, n−2d+1}, where d ≥ 3,
  6) {2,...,2}, {1,2,2,...,2,3}, {n/2, n/2},
  7) {2,2,2,2,2,2}, {1,1,1,3,3,3}, {6,6}."
  Every listed exception has composite n (a partition {l,...,l} with 2 ≤ l < n, or {2,...,2}, forces
  l | n or 2 | n). Mechanism: planar constellations / bicolored plane maps.

### 1e. Current status (as of the access date) — **V** (preprints; unrefereed)
- Wang, Li, Zhou, Wei, Ye, Shi, Xu, *The Hurwitz existence problem and the prime-degree conjecture:
  A computational perspective*, arXiv:2512.06545 (v2, 9 Dec 2025). Abstract: "we achieve a complete and
  non-redundant enumeration of all non-realizable partition triples for positive integers up to 31 [...]
  we verify the prime-degree conjecture for all primes less than 32." Intro: Zheng confirmed it "for
  primes less than 20"; Baroni "for all primes d ≤ 29".
- Song, Wen, Zhang, *The Hurwitz existence problem in prime degree*, arXiv:2609.20572 (v1, 17 Sep 2026).
  **Theorem 1.1**: "Let p be a prime. Every branch datum of degree p satisfying (1.1) is realized by a
  connected branched cover Σ_g → S²." Mechanism (abstract): three-point case "constructed in residue
  characteristic p" (stable reduction, Henrio's moment theorem, special deformation data, Wewers's
  lifting theorem → three-point Galois cover in char. 0; quotient by a point stabilizer has degree p),
  then the EKS reduction for arbitrary numbers of branch values. The paper itself records "Meng–Wei–Zhou
  described the prime-degree conjecture as unresolved in May 2026". **Status: claimed proof, ~7 weeks
  old, not refereed; treat as open-but-claimed.** It also cites Chenakkod–Faraco–Gupta (all but one
  profile pure cycles) and Ciliberto–Knutsen–Torelli arXiv:2604.18782 (all profiles pure cycles) as
  partial results (V2, via Song–Wen–Zhang).

**Notes (1).** (i) Yes as a conjecture/claim: every compatible datum of every prime degree (pointwise,
infinite class). (ii) The "witness" is one permutation triple; counts (Hurwitz numbers) are not part of
the statement — Song–Wen–Zhang only claim the count is nonzero. In the Euclidean families the
realizing degrees are norms x²+y², x²+xy+y² (density 0 among all d, but containing all primes in the
right class). (iii) EKS: permutation/monodromy combinatorics + reduction to 3 branch points; Pascali–
Petronio: orbifold-cover geometry (lattices in E², H²), dessins; Song–Wen–Zhang: p-adic stable reduction
and lifting. (iv) **Yes, sharply:** for *every* composite d there is a non-realizable datum (EKS Prop. 5.7;
Petronio Prop. 1.18); degree 4 alone has infinitely many ({[3,1],[2,2],...,[2,2]}); Thm 3.13/3.14
families are non-realizable on a density-1 set of degrees yet realizable at every prime of the right
residue class. This is the closest structural precedent: "prime ⇒ always, composite ⇒ fails on explicit
infinite sets".

---

## 2. Hadamard conjecture

### 2a. Smallest open order — **V** (survey preprint); the 668 answer is now outdated
- R. Egan, I. S. Kotsireas, S. London, P. Ó Catháin, *Recent progress in the construction of Hadamard
  matrices*, arXiv:2610.27175 (v2, 3 Nov 2026). URL: https://arxiv.org/abs/2610.27175
- Abstract: "for approximately the last twenty years, the smallest open case of this conjecture was
  order 668. In August 2026, Alpöge, Voinov and Reynolds-Haertle announced Hadamard matrices at the twelve
  orders below 2000 at which none was known. In this paper we verify and analyse the claimed matrices."
- Intro: "From the construction of order 428 by Kharaghani and Tayfeh-Rezaie [59], the smallest open
  order was 668. On 12 August 2026 Alpöge, Voinov and Reynolds-Haertle announced Hadamard matrices at
  the twelve orders 668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964, which were the
  only open orders below 2000 [3]." [3] = announcement, https://epoch.ai/frontiermath/open-problems/hadamard
  (NA — not opened).
- §4: "The smallest open order is now 2396 = 4 · 599. Every prime appearing in this table is congruent to
  3 mod 4." (95 open orders ≤ 10 000.)
- So: smallest open order **2396** (per this Nov-2026 survey); **668** was the answer from Kharaghani–
  Tayfeh-Rezaie (2005, J. Combin. Des.; journal data NA) until Aug 2026.

### 2b. Seberry (Wallis) 1976 — **V2** (+ search-index snippet of the original)
- J. Seberry Wallis, *On the existence of Hadamard matrices*, J. Combin. Theory Ser. A 21 (1976) 188–195.
- Original PDF not readable (ro.uow.edu.au returned 403; citeseerx dead; ScienceDirect HTML only).
  The search-engine snippet of the UOW repository PDF reads: "Given any natural number q > 3 there exists
  an Hadamard matrix of order 2^s q for every s ≥ [2 log₂ (q – 3)]." (unverified snippet; theorem number NA).
- V2 (de Launey arXiv:1003.4001 abstract): "Since Seberry's ground-breaking result, which showed that we
  may take a = 0 and b = 2, there have been several improvements where b has been by stages reduced to 3/8."
- V2 (Du–Jiang arXiv:2401.15381, intro): "The first asymptotic result of t = ⌊2 log₂(m − 3)⌋ + 1, m > 3 was
  established in 1976 [22]". So the exact additive constant differs between secondary sources (+0 vs +1).

### 2c. Later improvements — **V2** (Du–Jiang; formulas reconstructed from garbled text layer)
- Du–Jiang, *Golay Complementary Sequences of Arbitrary Length and Asymptotic Existence of Hadamard
  Matrices*, arXiv:2401.15381 (27 Jan 2024), intro (fractions lost in PDF text; reconstructed):
  Craigen 1995 [J. Combin. Theory Ser. A 71 (1995) 241–254, signed groups]: t = 4⌊(1/16) log₂((m−1)/2)⌋ + 6;
  Craigen–Holzmann–Kharaghani 1997 [J. Combin. Des. 5 (1997) 319–327]: t = 4⌊(1/10) log₂(m−1)⌋ + 6;
  Livinskyi 2012 (M.Sc. thesis, Manitoba): t = 6⌊(1/26) log₂((m−1)/2)⌋ + 11 (a 1/30 variant "is
  problematic since it relies on [23, Theorem 4], which is incorrect").
  **Theorem 3** (Du–Jiang): "There exist block-circulant Hadamard matrices of order 2^t m with block size
  2^{t−2} for any odd number m, where t = 6⌊(1/40) log₂ m⌋ + 10."
  Caveat: de Launey and Egan et al. both say b was reduced "to 3/8" before Livinskyi; this does not match
  the reconstructed Craigen coefficient 4/16 = 1/4 — unresolved discrepancy between secondary sources.
- de Launey, *On the asymptotic existence of Hadamard matrices*, arXiv:1003.4001; J. Combin. Theory Ser. A
  116 (2009) 1002–1008 (journal_ref from arXiv API). **V**. **Theorem 1.1**: "Let ε > 0. Let H(x) denote the
  number of odd positive integers k ≤ x for which there is a Hadamard matrix of order 2^ℓ k, for some
  positive integer ℓ ≤ 2 + ε log₂ k. Then there is a constant c₁(ε), dependent only on ε, such that, for
  all sufficiently large x, H(x) > c₁(ε)x." Reduced to **Theorem 1.2**: positive density of odd k with
  2^m k − 1 prime for some m ≤ ε log₂ k (Erdős–Odlyzko argument), plus Paley + Sylvester.
  **Proposition 1.3** (limits of the method): "There is a positive number δ₀, such that, for all ε > 0,
  there are infinitely many x ≥ 0 for which M_ε(x) ≤ ½(1 − δ₀)x." Reason given: Riesel numbers — "for any
  m ≥ 0, at least one of the primes 3, 5, 7, 13, 17 or 241 divides 2^m k − 1, where k = 509203 +
  11184810r" — an explicit infinite (arithmetic-progression) set on which the prime-shift witness never
  exists, by a covering congruence.

**Notes (2).** (i) Seberry/Craigen/Du–Jiang: pointwise for every odd q, but only with a power-of-2 blow-up
2^{O(log q)} = q^{O(1)}; the conjecture itself (t = 2 for all q) is not pointwise-proved. de Launey: only
positive density. (ii) Witnesses: constructive (one matrix); de Launey's witness is a prime 2^m k − 1
with m ≤ ε log₂ k — expected count ≈ Σ_m 1/log(2^m k) ≍ ε (O(1)), hence only density, not pointwise.
(iii) Recursive/algebraic constructions (Williamson/Golay/signed groups, Kronecker products) + prime
supply (Paley). (iv) The *method* fails on an explicit infinite set (Riesel numbers, covering
congruences) — exactly analogous to a sieve-witness obstruction; no failure of the conjecture is known.

---

## 3. Graham 1963 — n > 77 as a sum of distinct integers with reciprocal sum 1 — **V** (OCR)
- R. L. Graham, *A theorem on partitions*, J. Austral. Math. Soc. 3 (1963) 435–441 (received 17 March
  1963). **Not** Pacific J. Math. (Graham's 1964 Pacific J. Math. 14, 85–92 paper is "On finite sums of
  reciprocals of distinct nth powers".) URL: https://fanchung.ucsd.edu/ron/papers/63_02_partitions.pdf
  (scanned; OCR'd).
- Intro: "In this paper we prove that all integers exceeding 77 possess this property."
  **Theorem 1**: "If n is an integer exceeding 77 then there exist positive integers k, a₁, ..., a_k such
  that: 1. 1 < a₁ < a₂ < ... < a_k. 2. n = a₁ + a₂ + ... + a_k. 3. 1 = a₁⁻¹ + a₂⁻¹ + ... + a_k⁻¹."
- Mechanism: explicit table for 78 ≤ n ≤ 333 (e.g. "78: 2, 6, 8, 10, 12, 40"), then two transformations
  "(a) 1 = 1/2 + Σ 1/(2d_i)" and "(b) 1 = 1/3 + 1/7 + 1/78 + 1/91 + Σ 1/(2d_i)" (the second reconstructed
  from OCR; 1/3+1/7+1/78+1/91 = 1/2 and 3+7+78+91 = 179) which "keeps the denominators distinct as long as
  no d_i is 1 or 39. The new sums of the denominators are 2U+2 and 2U+179 respectively"; induction
  doubles the covered range. **Theorem 2**: generalization to any rational target α and denominators > β
  (for n > r(α, β)).
- That 77 itself fails: V2 — Alekseyev, arXiv:1801.05928 abstract: "Graham proved that all integers
  greater than 77 (but not 77 itself) can be partitioned [...]".

**Notes (3).** (i) Yes, every n > 77. (ii) Proof gives one witness per n; counts not studied.
(iii) Finite computer-free table + affine self-similarity n ↦ 2n+2, 2n+179 (induction). (iv) Only finitely
many failures (n ≤ 77), no composite/prime dichotomy.

---

## 4. Unit-fraction colouring/density (Croot, Bloom, Liu–Sawhney)

### 4a. Croot 2003 — **V**
- E. S. Croot III, *On a coloring conjecture about unit fractions*, Ann. of Math. (2) 157 (2003), no. 2,
  545–556; arXiv:math/0311421. URL: https://arxiv.org/abs/math/0311421
- Abstract: "There exists a constant b > 0 such that if we r-color the integers in [2, b^r], then there
  exists a monochromatic set S such that Σ_{n∈S} 1/n = 1." **Corollary**: "There exists a constant b so
  that for every partition of the integers in [2, b^r] into r classes, there is always one class containing
  a subset S with the property Σ_{n∈S} 1/n = 1." (b = e^{167000} admissible for large r; b ≥ e necessary.)
- **Main Theorem**: "Suppose C ⊂ C′(N, N^{1+δ}; θ), where θ, δ > 0, and δ+θ < 1/4. If N ≫_{θ,δ} 1 and
  Σ_{n∈C} 1/n > 6, then there exists a subset S ⊂ C for which Σ_{n∈S} 1/n = 1." (C′ = integers in [N, N^{1+δ}]
  with all prime-power divisors ≤ N^θ and ω(n) ∼ Ω(n) ∼ log log n.)
- Mechanism: pick D ⊂ C with Σ1/n ∈ [2 − 3/N, 2) (Proposition 1); count via the circle method
  #{S ⊂ D: Σ1/n = 1} = (1/P) Σ_{−P/2<h≤P/2} E(h) − 1, E(h) = Π_{n∈D}(1 + e(h/n)), P = lcm D; major arcs
  |h| < N/6 contribute > 2^{|D|} (positive real parts), minor arcs bounded by |E(h)| < 2^{|D|−1}/P using that
  many n ∈ D do not divide any integer near h. The number of solutions is ≫ 2^{|D|}/P — **exponentially
  many** witnesses.

### 4b. Bloom 2021 — **V**
- T. F. Bloom (appendix with B. Mehta), *On a density conjecture about unit fractions*, arXiv:2112.03726
  (v2, 12 Oct 2023). URL: https://arxiv.org/abs/2112.03726 (journal publication: NA).
- **Theorem 2**: "If A ⊂ N has positive upper density (and hence certainly if A has positive density) then
  there is a finite S ⊂ A such that Σ_{n∈S} 1/n = 1."
- **Theorem 3**: "There is a constant C > 0 such that the following holds. If A ⊂ {1,...,N} and
  Σ_{n∈A} 1/n ≥ C (log log log N / log log N) log N then there is an S ⊂ A such that Σ_{n∈S} 1/n = 1."
  Known: (log log N)² ≪ λ(N) ≪ (log log log N / log log N) log N. Proof formally verified in Lean.
- Mechanism: strengthened Croot Fourier method (smoothness threshold n^{1/4−o(1)} → n^{1−o(1)}).

### 4c. Liu–Sawhney 2024 — **V**
- Y. P. Liu, M. Sawhney, *On further questions regarding unit fractions*, arXiv:2404.07113 (10 Apr 2024).
  URL: https://arxiv.org/abs/2404.07113
- **Theorem 1.1**: "Let ε > 0, with N sufficiently large depending on ε. For any set A ⊆ [1, N] satisfying
  Σ_{n∈A} 1/n ≥ (log N)^{4/5+ε}, there is a subset B ⊆ A with Σ_{n∈B} 1/n = 1."
- **Theorem 1.2**: #{S ⊆ [1,N]: Σ_{s∈S} 1/s = 1} = e^{γ*N ± o(N)}, e^{γ*} ≈ 1.88057.
- **Theorem 1.3**: |A| ≥ (1 − 1/e + ε)N ⇒ some A′ ⊆ A with Σ1/n = 1 (sharp constant).
- Mechanism: "a variation of the Fourier analytic techniques used by Croot [7] and Bloom [4]".

**Notes (4).** (i) Statements are about every colouring / every dense set (pointwise over an infinite
class of sets, but *not* over prescribed targets — target is fixed = 1). (ii) Witness count exponential in
|D| (circle-method main term ≍ 2^{|D|}/P). (iii) Fourier/circle method over Z/P with P = lcm, major/minor
arcs, divisibility structure for minor arcs. (iv) Thresholds are near-sharp (b ≥ e; 1 − 1/e sharp; primes
give λ(N) ≫ log log N): failure on explicit sets (e.g. integers with a large prime factor) but not a
prime/composite dichotomy.

---

## 5. Oppenheim conjecture and effective versions

### 5a. Margulis (1987/89) — **V2** (Wikipedia "Oppenheim conjecture", accessed
https://en.wikipedia.org/wiki/Oppenheim_conjecture via Jina reader; original NA)
- "Let Q be a real nondegenerate indefinite quadratic form in n variables. Suppose that n ≥ 3 and Q is not a
  multiple of a form with rational coefficients. Then for any ε > 0 there exists a non-zero vector x with
  integer components such that |Q(x)| < ε." Proved 1987 by Margulis via unipotent orbits on SL₃(R)/SL₃(Z).

### 5b. Lindenstrauss–Margulis (logarithmic rate) — **V2**
- [LM14] cited in LMWY as "An effective version with a logarithmic rate was proved by the first named
  author and Margulis [LM14]" (Israel J. Math., 2014 — exact data NA; not found on arXiv by title search).
  The user's "Lindenstrauss–Margulis–Mohammadi–Shah ~2022" is a conflation: LMMS is arXiv:1904.00290,
  *Quantitative behavior of unipotent flows and an effective avoidance principle* (J. Anal. Math. 2023),
  which contains no explicit Oppenheim statement (grep: no occurrence of "Oppenheim").

### 5c. Lindenstrauss–Mohammadi–Wang–Yang 2023 (polynomial rate) — **V**
- E. Lindenstrauss, A. Mohammadi, Z. Wang, L. Yang, *An effective version of the Oppenheim conjecture with
  a polynomial error rate*, arXiv:2305.18271 (29 May 2023). URL: https://arxiv.org/abs/2305.18271
- **Theorem 1.1**: "Let Q be an indefinite ternary quadratic form with det Q = 1. For all R large enough,
  depending on ‖Q‖, and all T ≥ R^{A₁} at least one of the following holds. (1) For every s ∈ [−R^{κ₁},
  R^{κ₁}], there exists a primitive vector v ∈ Z³ with 0 < ‖v‖ < T so that |Q(v) − s| ≤ R^{−κ₁}. (2) There
  exists an integral quadratic form Q′ with ‖Q′‖ ≤ R so that ‖Q − λQ′‖ ≤ R^{A₁}(log T)^{A₁} T^{−1} where
  λ = (det Q′)^{−1/3}. The constants A₁ and κ₁ are absolute."
- **Corollary 1.2** (algebraic, non-rational ternary Q): for all T ≥ R^{A₂} and every s ∈ [−R^{κ₂}, R^{κ₂}]
  there is a primitive v, 0 < ‖v‖ < T, with |Q(v) − s| ≤ R^{−κ₂}. Taking R = T^{1/A₂} gives
  |Q(v)| ≤ T^{−κ₂/A₂} — i.e. **yes, |Q(v)| < T^{−δ} with primitive ‖v‖ ≤ T, for ternary forms that are
  algebraic and not proportional to rational forms (Diophantine condition), δ absolute**; for general Q
  only the dichotomy.
- **Theorem 1.4** (counting): either #{v ∈ Z³: ‖v‖ ≤ T, a ≤ Q(v) ≤ b} ≥ C_Q(b − a)T + (1+|a|+|b|)^N T R^{−κ₄}
  <sign before the error term lost in text layer; presumably "−"> or Q is R^{A₄}(log T)^{A₄}T^{−1}-close to
  a scaled integral form. Proof: effective equidistribution of a_{log T} u_r x₀ (Thm 1.3) using the
  Gan–Guo–Wang restricted projection theorem.

**Notes (5).** (i) Margulis: pointwise for every irrational indefinite form, n ≥ 3. Effective version:
pointwise only for forms with a Diophantine (e.g. algebraic) condition; otherwise dichotomy. (ii) Number
of v with ‖v‖ ≤ T, Q(v) ∈ [a,b] is ≍ (b−a)T in dim 3 (power of T) — so many witnesses; a small value
T^{−δ} is a "polylog/power-saving" target. (iii) Ergodic theory: unipotent orbit closures/equidistribution
on SL₃(R)/SL₃(Z). (iv) Fails for forms proportional to rational forms (explicit infinite class; then
|Q(v)| ∈ (1/c)Z) and is false in n = 2 (binary forms with badly approximable coefficient ratio) —
the latter is standard knowledge, not re-verified in a source here. The dichotomy "either works or Q is
close to a rational form of small height" is the structural analogue of "works except at arithmetic
obstructions".

---

## 6. Breusch / Stewart 1954 (odd denominators) and Graham 1964 — **V2** for 1954, **V** for Graham 1964
- R. Breusch, *A special case of Egyptian fractions*, solution to Advanced Problem 4512, Amer. Math.
  Monthly 61 (1954) 200–201 (bibliographic data V2: Eppstein's reference list
  https://ics.uci.edu/~eppstein/numth/egypt/refs.html, search snippet: "Shows that every x/y with y odd
  [...]"); B. M. Stewart, *Sums of distinct divisors*, Amer. J. Math. 76 (1954) 779–785 (data V2 from Graham 1964 ref. 5;
  original NA — not opened).
- V2 statement (Graham 1964, Introduction): "In 1954 it was shown by B. M. Stewart (5) and independently by
  R. Breusch (1) that if p/q > 0 and q is odd, then p/q is the sum of a finite number of reciprocals of
  distinct odd integers."
- R. L. Graham, *On finite sums of unit fractions*, Proc. London Math. Soc. (3) 14 (1964) 193–207
  (received 21 Jan 1963). URL: http://fanchung.ucsd.edu/ron/papers/64_01_unit_fractions.pdf (scan; read
  via OCR + page images). **V**.
  - **Theorem 1** (p. 196): "Let S = (s₁, s₂, ...) be a sequence of positive integers such that (1) M(S) is
    complete, (2) s_n is unbounded, (3) s_{n+1}/s_n is bounded. Suppose that p/q is a rational number, with
    (p, q) = 1, such that (4) p/q is (M(S))⁻¹-accessible, (5) q divides some term of M(S). Then
    p/q ∈ P((M(S))⁻¹)." (M(S) = increasing sequence of all finite products of distinct s_k; P(·) = finite
    subsums; "complete" = all sufficiently large integers are subsums.)
  - **Theorem 5** (p. 205), main result: same with (1) M(S) complete, (2) s_{n+1}/s_n bounded; then
    "p/q ∈ P((M(S))⁻¹) (where (p, q) = 1) if and only if (3) p/q is (M(S))⁻¹-accessible, (4) q divides some
    term of M(S)." Example S = (4, 1, 3, 3², ...) shows condition (1) cannot be dropped (1/2 is accessible,
    2 | 4, yet 1/2 ∉ P(M(S)⁻¹)).
  - §4 remark (1) (p. 206): "p/q = Σ_{i=1}^n 1/(ak_i + b) for some positive integers n and k₁ < k₂ < ... < k_n
    if and only if (q/(q,(a,b)), a/(a,b)) = 1" — "obtained by considering the sequence (a+1, 2a+1, ...)". With
    a = 2, b = 1 this is exactly the Breusch–Stewart odd-denominator theorem. Remark (2): p/q is a finite sum
    of reciprocals of distinct squares iff p/q ∈ [0, π²/6 − 1) ∪ [1, π²/6).
  - Mechanism: greedy/accessibility approximation from below by finitely many terms (Lemma 1), then the
    remainder, written over a common denominator s₁⋯s_r, is absorbed by "completeness" of M(S) (every
    large integer is a sum of distinct products ⇒ remainder numerator = sum of distinct divisors) —
    the Stewart "sums of distinct divisors" idea; Brown's completeness criterion used.

**Notes (6).** (i) Yes: every positive rational with odd denominator (and Graham: every p/q satisfying
the two necessary conditions). (ii) Constructive, number of terms unbounded (not a fixed-length
representation); counts not addressed. (iii) Greedy approximation + completeness of a multiplicative
semigroup's subset sums. (iv) The necessary condition q | some term of M(S) is a genuine local obstruction
(e.g. even q fails for odd denominators — an explicit infinite set, all with even q); Graham's
example shows failure without completeness even when local conditions hold.
