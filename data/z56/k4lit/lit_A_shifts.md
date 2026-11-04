# lit_A_shifts — primes with half-dimensional (sum-of-two-squares / S) conditions on shifts

> **Errata (z56 K4LIT internal review):** see `Z56_K4LIT.md` §9 — errata there override this report (Dimitrov local-density issue; Banks/Lü–Wang–Wu unrefereed, conditional readings; Sedunova counts are representation-weighted; Siegel-zero ≤0.52 levels are residue-uniform; "no parity barrier" means total-Ω_𝒬 parity only — at BV level there is the hidden-prime barrier, Lemma P).


Scope: questions (A1)–(A3) for P(4,15) = "∞ many primes p ≡ 1 (mod 8) with p+4 ∈ S and 4p+1 ∈ S".
Notation: S = {n : every prime factor ≡ 1 mod 4}; SOTS = sum of two squares; for **odd** n,
"n = ξ²+η² with (ξ,η)=1" ⇔ n ∈ S. All quotes below were read by me from the source file named
(PDF text extraction, or OCR + visual check of the page image for the scanned Acta Arith. papers).
"[inference]" marks my own deductions; "UNVERIFIED" marks things I could not read at source.
This report goes beyond data/z55/p415 and data/z54/hckill: it adds the exact FI-2009 lower-bound
mechanism, Iwaniec 1972/1976 theorem texts, Sedunova 2026, Kontorovich 2014, Nath–Xie v3 (Ω ≤ 9),
Matomäki 2007, Indlekofer 1974, Dimitrov 2024, GGPY, Bary-Soroker–Fehm.

---------------------------------------------------------------------------------------------------

## (A1) ONE shift: p+a SOTS / in S

### A1.1 Iwaniec 1972 — Theorem 1 (the S-version is already here: "proper" representation)
H. Iwaniec, "Primes of the type φ(x,y)+A where φ is a quadratic form", Acta Arith. 21 (1972) 203–234.
URL: https://matwbn.icm.edu.pl/ksiazki/aa/aa21/aa21118.pdf (scanned; read via OCR + page images, pp. 203–205).

Intro (p. 203), verbatim: "B. M. Bredihin [2] proved in 1965 that if a form φ(ξ,η) satisfies the
assumptions of the quoted theorem then for every integer A ≠ 0 there exist infinitely many primes of the
type φ(ξ,η)+A. Then Bredihin and Linnik [3] introduced a method of deriving the asymptotic formula for the
number of solutions of the equation φ(ξ,η)+A = p … The obtained asymptotic formula does not give any direct
information about the number S(φ,A,N) of the primes p ≤ N representable as φ(ξ,η)+A and even does not allow
one to determine the order of magnitude of S(φ,A,N). Recently Y. Motohashi [8] investigated the simplest case
φ(ξ,η) = ξ²+η², A = 1 and obtained the estimation S(ξ²+η²,1,N) ≫ N log⁻² N."

"THEOREM 1. Let φ₀(ξ,η) = aξ²+bξη+cη², a > 0, (a,b,c) = 1, let D = b²−4ac be not a perfect square,
B ≥ 1, A ≠ 0, (A,B) = 1, R_{φ₀} the genus of φ₀,
 S₁(N,φ₀,B,A) = Σ_{p≤N, p=Bφ(ξ,η)+A, (ξ,η)=1, φ∈R_{φ₀}} 1,  S_∞(N,φ₀,B,A) = Σ_{p≤N, p=Bφ(ξ,η)+A, φ∈R_{φ₀}} 1,
 S₂(N,φ₀,B,A) = Σ_{p≤N, p=Bφ₀(ξ,η)+A} 1,
 θ = sup_{1<s<4/3} { ∫₁ˢ dt/√(t(t−1)) − 8s²√(2(s−1)/s) log(2s−1) }, Ψ_{A,B,D} = √(2/π) ∏ … .
Then the following estimations hold:
(1.1) θΨ_{A,B,D}Ω_{A,B,D} N/(log N)^{3/2} (1+o(1)) + O(N log⁻⁵N) < S₁(N,φ,B,A) < 2Ψ_{A,B,D}Ω_{A,B,D} N/(log N)^{3/2}(1+o(1)) + O(N log⁻⁵ N),
(1.2) N/(φ(B)(log N)^{3/2}) + O(N log⁻⁵N) ≪ S_∞(N,φ,B,A) ≪ N/(φ(B)(log N)^{3/2}),
(1.3) [same for S₂] … The constants implicit in the symbols O, ≪, depend only on φ and A. Also o(1) is
uniform with respect to B."
COROLLARY (p. 204): (θ/2)∏_{p≡−1(4)}(1−1/p²)^{−1/2}(1−1/(p(p−1))) N/(log N)^{3/2}(1+o(1)) < S(ξ²+η²,1,N) < ∏(…) N/(log N)^{3/2}(1+o(1)).
p. 204–205: "Theorem 1 implies that for A ≠ 0, (A,B) = 1 the order of magnitude of S_δ(N,φ,B,A) (δ = 1, ∞, 2)
is N/(log N)^{3/2}."

Relevance: with φ₀ = ξ²+η², B = 1, A = −4, S₁ counts primes p ≤ N with p+4 properly represented, i.e.
(p+4 odd) **p+4 ∈ S**: ≍ N/(log N)^{3/2} unconditionally. So the single condition "p+4 ∈ S" is a 1972
theorem [inference: specialization]. The shift 4p+1 is not literally of the shape p = Bφ+A; it is covered
by the same semilinear sieve on {4p+1} (BV level 1/2 suffices) [inference; no verbatim theorem found for 4p+1].

### A1.2 Iwaniec 1976 — "The half dimensional sieve": conditional ASYMPTOTICS (one shift; integer pairs)
H. Iwaniec, "The half dimensional sieve", Acta Arith. 29 (1976) 69–95. EuDML https://eudml.org/doc/205410 ;
PDF https://matwbn.icm.edu.pl/ksiazki/aa/aa29/aa2914.pdf (scanned; pp. 72–74 read from page images).
Definitions (p. 72): "b(a) = 1 if a = u²+v², 0 otherwise; b*(a) = 1 if a = u²+v², (u,v) = 1, 0 otherwise."
Theorem 3 (p. 72): "Let us assume, that a∈𝒜 ⇒ a ≡ 1, 2 or 5 (mod 8), 𝒫 ⊂ {p ≡ −1 (mod 4)}. Then for Q⁶ < A we
have Σ_{a∈𝒜} b*(a) = √2 ∏_{p≡−1(4)}(1−1/p²)^{−1/2}(1−ω(p)/p)(1+1/p) X log^{−1/2}A × {1+O(e^{6K}((L+log Q)/log A)^γ)}
+ θ Σ_{d<A/Q, d|P(√A)} |R(𝒜,d)|."  (Theorem 4: same for b(a).)
Corollary 2 (p. 73), with E(X,Q) = Σ_{q<Q} max_{(l,q)=1}|π(X,q,l) − Li X/φ(q)| and B(X,Q) the analogous
quantity for b(n): "Let ε > log log N/log N. Then we have
(2.1) Σ_{p<N} b(p−1) = (1/√2)∏_{p≡−1(4)}(1−1/p²)^{−1/2}(1−1/(p(p−1))) N/log^{3/2}N × (1+O(ε^γ)) + θ₁E(N,N^{1−ε}),
(2.2) Σ_{p<N} b(N−p) = … ,
(2.3) Σ_{n<N} b(n)b(n+1) = (3/8)(N/log N){1+O(ε^γ)} + θ₃{B(N,N^{1−ε}) + B(N/2,N^{1−ε})}."
p. 73–74: "(2.1) implies that Motohashi's conjecture … follows in its corrected form … from Halberstam's
well-known conjecture [5] that E(N,N^{1−ε}) = O(N/log⁴N). Similarly, (2.3) implies that Hooley's conjecture
about Σ b(n)b(n+1) would follow from the estimate B(N,N^{1−ε}) = o(N/log N)."
Relevance: even for ONE shift, the asymptotic for #{p: p−1 SOTS} needs level ~N^{1−ε} (Elliott–Halberstam);
unconditionally only the order of magnitude (A1.1) is known. Nath–Xie (2026, v3, p. 2) confirm: "We still do
not have an asymptotic formula for the number of primes of the form p = m²+n²+1 up to any positive real
number x unconditionally. See [11, Corollary 2] for a conditional asymptotic formula."

### A1.3 Linnik / Bredikhin: weighted sum Σ_p r(p−a) (asymptotic, unconditional)
Source read: Matomäki 2007 intro (A1.4) verbatim: "In 1960 Linnik [5] proved an asymptotic formula for
Σ_{p≤N} r(p−a), where the summation runs over primes, a is a fixed non-zero integer and r(n) is the number of
representations of n as a sum of two squares. This implies the first unconditional proof that there are
infinitely many primes of the form p = m²+n²+1." (Linnik's original: UNVERIFIED at source.)
FI 2009 Thm 5 (A2.1) is a modern instance (Σ_{p≤x} r(p−4) log p, via BFI Theorem 9).
Relevance: r-weighted single-shift sums are "easy" (r = 4·1*χ is a divisor-type sum of length √x, so BV
suffices); the hard part is the indicator b/b* (half-dimensional sieve, order of magnitude only).

### A1.4 Short intervals: Huxley–Iwaniec, Wu, Matomäki — with (m,n)=1, i.e. the S-version
K. Matomäki, "Prime numbers of the form p = m²+n²+1 in short intervals", Acta Arith. 128.2 (2007) 193–200.
PDF: https://www.impan.pl/shop/en/publication/transaction/download/product/82095 (text extracted).
Verbatim: "Huxley and Iwaniec [1] considered primes of the form m²+n²+1 with (m,n) = 1 in the short interval
(x, x+x^θ]. They proved that for θ = 99/100 this interval contains primes of this type for every sufficiently
large x and more precisely that the number of them is of the expected order of magnitude, that is,
≫ x^θ/(log x)^{3/2}. Wu [7] improved this result to θ = 115/121 ≈ 0.9504."
"Theorem 1. For every θ ≥ 10/11 = 0.9090... and x ≥ x₀(θ), we have Σ_{x<p≤x+x^θ} b*(p−1) ≫ x^θ/(log x)^{3/2},
where b*(a) = 1 if a = m²+n² with (m,n) = 1, 0 otherwise." Method: "applying the half-dimensional sieve to
the set A = {p−1 | x < p ≤ x+x^θ, p ≡ 3 (mod 8)}".
(Huxley–Iwaniec, Mathematika 22 (1975) 188–194; Wu, Proc. AMS 126 (1998) 1–8: statements only via this
secondary quote; Semantic Scholar snippet of Wu: "for every θ ≥ 115/121 … the short interval (x,x+x^θ] contains
at least one prime number of the form p = 1+m²+n²" — originals UNVERIFIED.) No later improvement of 10/11 found.
Relevance: b*(p−1) is exactly "(p−1)/2 ∈ S"; shows the S-condition (not just SOTS) on one shift is standard.

### A1.5 Distribution / additive variants of the one-shift set P = {p : p−1 SOTS}
- Teräväinen, Mathematika 64 (2018) 20–70, arXiv:1611.08585 (read v2): Thm 1.1 "Almost all even positive
  integers n ≢ 5, 8 (mod 9) can be represented as n = p+q with p,q ∈ P"; Thm 1.2 ternary; and "the primes of
  the form x²+y²+1 contain infinitely many three term arithmetic progressions". Also: "the arguments of this
  paper would easily generalize to primes of the form x²+y²+a, where a ≠ 0 is any integer." Thm 1.4: P in Bohr
  sets (αp mod 1). Note: binary Goldbach for P is an *averaged-over-n* two-condition statement (p−1 and
  (n−p)−1 both SOTS, q = n−p prime) — it does NOT give a fixed second shift.
- Bienvenu–Shao–Teräväinen, Algebra & Number Theory 17 (2023) 231–273, arXiv:2106.09001 (abstract read):
  finite-complexity linear systems in primes of form x²+y²+1 "determined by natural local conditions". Fixed
  shifts (binary, infinite complexity) are not covered.
- Dimitrov, arXiv:2402.16425 (v2 read) Theorem 1: Σ_{q≤log^A X, (q,a)=1} |Σ_{p≤X,p≡a(q)} r(p−1) − (1/φ(q))Σ_{p≤X} r(p−1)|
  ≪ X(log log X)⁷/(log X)^{1+θ₀}; author: "the range of moduli q ≤ log^A X … is a lot shorter than the one in the
  classical Bombieri-Vinogradov theorem. This is due to the fact that in addition to the X^{1/2}-barrier are
  added the restrictions of the enveloping sieve." → The distribution of {p : p−1 SOTS} in APs is known only
  to tiny level; this is exactly the input a second half-dimensional sieve on another shift would need (A2.1).
- Chebotarev/AP variants: Iwaniec 1972 Thm 1 already has p ≡ A (mod B) (B uniform) and genus restriction;
  Iwaniec 1976 Cor. 1 has n ≡ l (mod k). Nothing beyond that specifically found.

---------------------------------------------------------------------------------------------------

## (A2) TWO simultaneous half-dimensional conditions on prime shifts

### A2.1 Friedlander–Iwaniec 2009 — exact statements (the det-1 analogue: p−2, p+2)
J. B. Friedlander, H. Iwaniec, "Hyperbolic prime number theorem", Acta Math. 202 (2009) 1–19.
PDF: https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6709-11511_2009_Article_33.pdf (text extracted).
- Theorem 1: "The number of integer points (x₁,x₂,x₃) with x₁²+x₂²+x₃² = p ⩽ x satisfies π₃(x) ∼ 4πx^{3/2}/(3 log x)."
- p. 2: "In this paper we are able to show that this order of magnitude is correct, that is c₁x/log x < π_Γ(x) <
  c₂x/log x, (1.4) for suitable positive constants c₁ and c₂, and all large x, subject to a standard conjecture
  concerning the distribution of rational primes in arithmetic progressions."
- (1.5)–(1.6): E(x;q,a) = ψ(x;q,a) − x/φ(q); E(x,Q) = Σ_{q⩽Q} max_{(a,q)=1} max_{y⩽x} |E(y;q,a)|.
- "Assumption A(θ). The bound E(x,Q) ≪ x(log x)^{−A} holds for Q = x^{θ−ε}, for every ε>0 and A>0, with an
  implied constant that depends only on ε and A." "We remark that A(1/2) is known to be true, the famous
  Bombieri–Vinogradov theorem, and that the expectation that A(1) holds is also well-known, as the conjecture of
  Elliott and Halberstam."
- "Theorem 2. If A(θ) holds for some θ, less than 1 but sufficiently close to 1, then there are positive
  constants c₁ and c₂ such that c₁x/log x < π_Γ(x) < c₂x/log x (1.7) for all x⩾2."
  "Actually, the upper bound is unconditional and an easy consequence of the sieve … We stress that we do not
  need to assume A(θ) for θ=1. … The method allows for the determination of an admissible value for θ but we
  did not carry this out. We actually need a considerably weaker form of the conjecture and some results in this
  direction have been provided by Fouvry [Fo], and by Bombieri, Friedlander and Iwaniec [BFI]."
- "Theorem 3. Under the same assumption as Theorem 2, we have Σ_{x₁²+x₂²+x₃²+x₄²⩽x, x₁x₄−x₂x₃=1} Λ(x₁²+x₂²+x₃²+x₄²) ≍ x. (1.11)"
- (1.14): number of solutions for n odd is ½ r(n−2)r(n+2).
- "Theorem 4. Under the same assumption as Theorem 2, we have S(x) = Σ_{n⩽x} r(n−2)r(n+2)Λ(n) ≍ x. (1.15)"
- (1.16)–(1.17): T(x) = Σ_{n⩽x} r(n−2)r(n+2)Λ(n+2) = Σ_{p⩽x} r(p−4) log p + O(√x), "which, using [BFI, Theorem 9],
  we shall directly and unconditionally evaluate". "Theorem 5. We have T(x) = πx ∏_p (1 + χ(p)/(p(p−1))) +
  O(x(log x)^{−A}), for any A>0, with an implied constant depending on A."
**Why the lower bound is conditional (§§5–7, verbatim):**
- §5: upper bound is "a linear sieve problem for the sequence A = {a_n} with a_n = r(n−2)r(n+2) … this sequence
  has a level of distribution D = x^{1/12−2ε}" (Lemma 4.2: Σ_{n⩽x, n≡3(4), d|n} r(n−2)r(n+2) = g(d)8x + O(x^{11/12+ε})).
- §6: "We are going to use the semilinear sieve and hence it will be convenient to replace the function r in one
  factor by b, the characteristic function of such integers. Define b(n)=1 if all prime factors of n are
  congruent to 1 (mod 4) and zero otherwise". Then S(x) ⩾ 4 Σ_{δ⩽Δ} b(δ) Σ_{n⩽x, n≡2 (δ)} b(n−2)r(n+2)Λ(n) (6.2):
  i.e. they lower-bound **p−2 ∈ S, p+2 SOTS**. Sifting sequence A^{(δ)} = {r(n+4)Λ(n+2)}, primes P = {p ≡ 3 (4)}.
  "The function g(d) in (6.6) is a linear sieve density, but we shall be sifting by only half of the primes, so
  this becomes a semilinear sieve problem … Since the sieving limit for the semilinear sieve is β=1 and our level
  of distribution is D=D(x)<√x, we cannot successfully apply the lower bound sieve to S(A^{(δ)},P,√x), but we can
  come close to this." Level chosen "D = D(x) = x^{θ−1/2−ϑ−ε} (6.10)".
- §7: the switching term T(A^{(δ)},P,z) (two large primes ≡3 mod 4) is bounded above by (7.1); it beats the sieve
  lower bound only "when θ<1 is near 1 and ϑ is even closer to zero"; "we conclude from (6.2) that S(x)≫x
  subject to the condition A(θ)." "Note that we actually require A(θ) for the sum weighted by a divisor function".
- Closing remark (p. 14): "the sum S(x) … bears some resemblance to the twin prime sum Σ Λ(n)Λ(n+2), not just
  superficially but also from a sieve-theoretic viewpoint. The latter counts survivors of two linear sieves,
  while the former counts survivors of one linear and two semi-linear sieves. The assumption of the full
  conjecture A(1) narrowly misses resolving the twin prime conjecture, see [Bo], whereas the extra flexibility in
  the sum S(x) allows us to succeed, even with the weaker assumption."
Diagnosis [inference from the quoted mechanism]: the obstruction is a **level-of-distribution** obstruction, not
the parity barrier per se: the weight r(p+2) already costs √x of the modulus range (divisor sum of length √x),
so with BV (θ=1/2) the residual level for the semilinear sieve on p−2 is x^{0} (D = x^{θ−1/2−…}), while β=1
requires D near √x. With θ near 1 the parity problem does not bite because the "switching" (two P-prime factors)
term is small. P(4,15) has the identical structure (Σ_p r(p+4) b(4p+1) or b·b); FI's argument would plausibly
give it under A(θ), θ near 1 (but with only ONE of the two in S unless one also sieves the r-factor) — not in the
literature [inference].

### A2.2 Citing literature: all describe FI as CONDITIONAL (up to 2026)
- A. Sedunova, "On the hyperbolic prime number theorem", arXiv:2609.28200v1 (Sept 2026), PDF read. Abstract:
  "Friedlander and Iwaniec proved that the number of points … lying at a distance p−2 … is of order x/log x;
  the upper bound is unconditional, while the lower one rests on a strong hypothesis concerning the distribution
  of primes in arithmetic progressions." Intro: "(the upper bound π_Γ(x) ≪ x/log x being unconditional, hence
  A(θ) is essential only for the lower bound)".
  "Theorem 1. For x ≥ 2 and any ε > 0 we have s_Γ(x) = 6Cx + O(x^{11/12+ε})" (n squarefree);
  "Theorem 2. For x > 3 we have s_Γ^{(7)}(x) ≫ x/log x" (n squarefree, ω(n) ≤ 7);
  "Conjecture 2 (Hypothesis R(θ)) … Σ_{d≤x^{θ−ε}, d odd squarefree} |Σ_{n≤x, n≡3(4), n≡0(d)} r(n−2)r(n+2) − 8g(d)x| ≪ x/(log x)^A";
  "Theorem 3. Let 0<θ≤1 and assume R(θ). Then, with N = ⌊2/θ⌋, … s_Γ^{(N)}(x) ≫ x/log x." "By Lemma 2, R(θ) holds
  for θ = 1/6." Remark 1: "the number 7 is not improved by any rearrangement of the sieve, only by a larger level
  of distribution."
  Relevance: the strongest unconditional "two SOTS shifts + almost-prime centre" result: ∞ many squarefree n with
  ω(n) ≤ 7 and n−2, n+2 both SOTS (weighted count). Not primes.
- A. Kontorovich, "Levels of distribution and the affine sieve", Ann. Fac. Sci. Toulouse Math. (6) 23 (2014)
  933–966, https://www.numdam.org/item/AFST_2014_6_23_5_933_0.pdf, §3.6.2 "Prime Norms in SL₂(Z)": "the problem
  can be converted into solving the system x²+y² = p+2, z²+w² = p−2 (3.31) for primes p … we must write both
  p+2 and p−2 as sums of two squares. Using a "half-dimensional" sieve and assuming the Elliott-Halberstam
  Conjecture, Friedlander-Iwaniec are able to solve the system (3.31), thereby (conditionally) resolving the
  problem in this setting."
- Bourgain–Kontorovich, "On a theorem of Friedlander and Iwaniec", arXiv:1008.0825 (abstract read): "Under the
  Elliott-Halberstam conjecture, they proved the existence of such … We prove unconditionally that for every odd
  n>=3, there is a gamma in SL(2,Z[i]) such that |gamma|^2 = n." (Gaussian-integer analogue; irrelevant to primes.)
- Nath–Xie (2026, v3) p. 2: "Assuming the Elliott-Halberstam Conjecture, they showed that x ≪ Σ_{n≤x} Λ(n)r(n−2)r(n+2) ≪ x"
  with footnote "The upper bound is established without any assumption."
- Shparlinski–Xiao, arXiv:2609.21460 (abstract only): squarefree values of a₁²+…+a₄² on SL₂(Z) in boxes; no primes.

### A2.3 Integer analogues (two/three half-dimensional conditions, no prime) — KNOWN unconditionally
- Indlekofer, "Scharfe untere Abschätzung für die Anzahlfunktion der B-Zwillinge", Acta Arith. 26 (1974)
  207–212, https://matwbn.icm.edu.pl/ksiazki/aa/aa26/aa2629.pdf (page image read). B = set of SOTS;
  "SATZ. Für die Anzahl der B-Zwillinge unterhalb x gilt (1.3) B₂(x) ≫ x(log x)^{−1}." (with Rieger's (1.1)
  B₂(x) ≪ x(log x)^{−1}). Proof "mit Hilfe des Selberg'schen Siebes".
- Cochrane–Dressler, "Consecutive triples of sums of two squares", Arch. Math. 49 (1987) 301–304 (citation per
  GGPY ref. [5]); manuscript https://www.math.ksu.edu/~cochrane/research/sumsquare.pdf (OCR): "J. E. Littlewood
  asked the more general question whether for given unequal positive numbers h,k there exist infinitely many
  numbers n such that n, n+h, n+k are all sums of two squares and Hooley (1973) gave an affirmative answer."
  "Hooley (1974) and Indlekofer (1974) using different methods established that B₂(x) ≫ x/log x." "THEOREM.
  B₃(x) ≪ x/(log x)^{3/2}." (Hooley originals, JNT 5 (1973) 215–217 and Crelle 267 (1974) 207–218: UNVERIFIED.)
- Goldston–Graham–Pintz–Yıldırım, "Small gaps between products of two primes", arXiv:math/0609615 (read):
  "Theorem 5. Under the conditions of Theorem 1, we have infinitely many n such that at least ν+1 linear forms
  L_ij(n) take simultaneously E₂-values (with both prime factors above D) which are sums of two squares" — and
  (1.33) "p₁p₂ = x²+y² ⇔ p₁,p₂ ≡ 1 (mod 4)", i.e. several linear forms simultaneously in S ∩ E₂ (integer n, not
  fixed shifts of a prime).
- Function-field analogue: Bary-Soroker–Fehm, arXiv:1701.04092, Theorem 4.7 (large-q limit) evaluates
  ⟨1_P(f) b_q(f+h)⟩ (prime + ONE SOTS shift); it is derived from their general k-fold Theorem 3.11 [whether a
  two-shift prime statement is stated explicitly: UNVERIFIED].

### A2.4 Searches for an unconditional prime two-shift theorem (none found)
Queries run (Jina search + arXiv API): "primes p such that p−2 and p+2 are sums of two squares", "shifted primes
two shifts both sums of two squares sieve", "primes p with p+1 and p+2 sums of two squares", "p−1 and p+1 both
sums of two squares", FI-2009 citation followers ("hyperbolic prime number theorem", Kontorovich, Bourgain–
Kontorovich, Nevo–Sarnak [no FI citation in arXiv:0902.0692], Sedunova, Shparlinski–Xiao), arXiv abstract
searches for "sums of two squares" AND {"shifted primes", "vector sieve", "semi-linear", "simultaneously",
"almost prime(s)", "consecutive"}, "x²+y²+1"/"m²+n²+1", Linnik primes, and a date-sorted scan of all arXiv
abstracts with "two squares" AND prime* (60 newest). Plaksin 1981/82 turned out to be about p₁²+p₂²+x²+y² (not
relevant). **No paper proves, unconditionally, infinitely many primes p with two distinct fixed shifts both SOTS
(or in S).** (Bounded search; not a proof of non-existence.)

---------------------------------------------------------------------------------------------------

## (A3) Chen-type mixed results (one half-dimensional condition + almost-prime)

### A3.1 Nath–Xie — now Ω(p+2) ≤ 9 (published version)
K. Nath, L. Xie, "Almost primes and primes that are sums of two squares plus 1", arXiv:2501.16723
(v1 Jan 2025 had Ω(p+2) ≤ 11; **v3, 17 Aug 2026, "Final version, published in Acta Arithmetica",
DOI 10.4064/aa250227-19-11**; v3 PDF read). Impan landing snippet also says "at most 9 prime factors".
"Theorem 1.1. We have #{p ≤ x : p prime, p = m²+n²+1, m,n ∈ N, Ω(p+2) ≤ 9} ≫ x/(log x)^{5/2}."
"Remark 1.1. Assuming a version of the Elliot-Halberstam conjecture³ … it is possible to show that
#{… Ω(p+2) ≤ 3} ≫ x/(log x)^{5/2}." (³: "(3.3) in Lemma 3.2 holds for q ≤ x^{1−ε}.")
"Remark 1.2. … application of vector sieves of mixed dimensions (see Proposition 3.10). First, we apply the
vector sieve with a semi-linear sieve and a linear sieve in conjunction with Iwaniec's argument".
"Remark 1.3. … our approach could also be extended to study primes of the form p = m²+n²+1 such that
∏(p+a_i) is an almost prime … #{…, Ω((p+2)(p+6)) ≤ r} ≫ x/(log x)^{5/2} for some positive integer r".
Intro: "It is reasonable to expect that there are infinitely many primes of the form p = m²+n²+1 such that p+2
is also a prime. In fact, it is expected that … ∼ C x/(log x)^{5/2}."
Relevance: strongest verified prime + half-dim shift + second-shift result; second shift only almost-prime,
no 3-mod-4 control. (Note the conditional remark still needs EH and still only gets Ω ≤ 3.)

### A3.2 Related Chen-type benchmarks quoted by Nath–Xie (secondary)
"Heath-Brown and Li [8] … #{p ≤ x : Ω(p+2) ≤ 2, Ω(p+6) ≤ 76} ≫ x/(log x)³ … The bound 76 has been reduced to
14 by Cai [1], and Zhu [26] further improved it to 11." (Cai, Acta Arith. 179 (2017); Zhu, IJNT 21 (2025).)
No 2025–2026 paper found with "p+a ∈ S (or SOTS) and bp+c almost prime" other than Nath–Xie; no "Chen primes
that are sums of two squares plus one" result found. Wu/Cai/Matomäki/Teräväinen/Lichtman/Dartyge searches gave
nothing beyond A1.4–A1.5 (UNVERIFIED as exhaustive).

---------------------------------------------------------------------------------------------------

## VERDICT

(i) **Neither P(4,15) nor the det-1 analogue (p−2, p+2 both SOTS) is known unconditionally.** The only proof of
infinitely many primes with p−2 and p+2 both SOTS is FI 2009 Theorem 4, explicitly "Under the same assumption as
Theorem 2", i.e. A(θ) for some θ < 1 "sufficiently close to 1" (a BV/EH-type level for primes, needed with a
divisor-function weight). Its lower-bound argument actually gives p−2 ∈ S, p+2 SOTS (via b(n−2)r(n+2)Λ(n)).
Every citing source through 2026 (Kontorovich 2014; Nath–Xie 2026; Sedunova Sept 2026: "the lower one rests on a
strong hypothesis") still calls it conditional. No source gives P(4,15) even conditionally; FI's method would
plausibly adapt under A(θ) [inference].

(ii) **Strongest unconditional results with ≥ 1 half-dimensional condition:**
 - prime p + one S/SOTS shift: order of magnitude only — Iwaniec 1972 Thm 1 (proper rep ⇒ p+A ∈ S),
   ≍ N/(log N)^{3/2}; short intervals x^θ, θ ≥ 10/11 (Matomäki 2007, with b*); asymptotic only under EH
   (Iwaniec 1976 Cor. 2 (2.1)).
 - prime p + SOTS shift + second shift almost-prime: Nath–Xie Thm 1.1, p−1 SOTS and Ω(p+2) ≤ 9, ≫ x/(log x)^{5/2}.
 - prime p + two SOTS shifts, r-weighted with one factor collapsing to p itself: FI Thm 5 (only a one-shift sum
   in disguise).
 - non-prime centre + two SOTS shifts: Sedunova 2026 Thm 2 (n squarefree, ω(n) ≤ 7, n±2 SOTS, weight ≫ x/log x);
   integers: Hooley 1973 (n, n+h, n+k all SOTS), Indlekofer/Hooley 1974 B₂(x) ≫ x/log x; GGPY Thm 5 (several
   linear forms simultaneously E₂ ∩ S).

(iii) **Explicit statements of conditionality / obstacle:** FI 2009 p. 2 ("subject to a standard conjecture
concerning the distribution of rational primes in arithmetic progressions"), §6 ("Since the sieving limit for the
semilinear sieve is β=1 and our level of distribution is D<√x, we cannot successfully apply the lower bound sieve
… but we can come close"), and p. 14 (one linear + two semi-linear sieves; A(1) "narrowly misses" twin primes,
whereas this problem succeeds "even with the weaker assumption"); Kontorovich 2014 "(conditionally) resolving";
Sedunova 2026 abstract + Remark 1 (the sieve exponent "is not improved by any rearrangement of the sieve, only by
a larger level of distribution"); Dimitrov 2024 (BV for r(p−1) only to moduli log^A X, "X^{1/2}-barrier" + enveloping
sieve). I found **no** sentence explicitly calling "p+a and bp+c both SOTS for infinitely many primes" an open
problem, and **no** source attributing the failure to the parity barrier; FI's own analysis locates it in the
level of distribution (r-weight eats √x of BV), with parity defused only when θ ≈ 1.
