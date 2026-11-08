# Number-theory precedents: verified statements

Access date for every URL below: **2026-11-08**.
Status key: **V** = statement read in the source itself; **V2** = read in a later source that restates it (named); **NA** = not accessed.
OCR note: Elkies 1987 and Cochrane–Mitchell 1998 are scans; I read them via `tesseract` OCR, and checked key formulas against page images where noted. Quotes marked "(OCR)" may contain glyph errors in the mathematics. The wording is reliable.

---

## 1. Legendre: x² − p y² = −1 is solvable for every prime p ≡ 1 (mod 4)

**Status: V2** (textbook exercise, read through a reproduction). I did not access Legendre's original (*Essai sur la théorie des nombres*, 1798). That makes the attribution to Legendre second-hand.

- **Textbook source:** Niven, Zuckerman, Montgomery, *An Introduction to the Theory of Numbers* (5th ed., Wiley 1991), §7.8, Exercise 12, as reproduced at
  https://solverer.com/solutions/ivan-niven/an-introduction-to-the-theory-of-numbers/exercise-7-8-12::160?lang=en .
  The exercise text is verbatim from that page:
  > "Suppose that p ≡ 1 (mod 4). Show that if x² − py² = 1, then x is odd and y is even. Suppose that x₀² − py₀² = 1 with y₀ > 0, y₀ minimal. Show that g.c.d.(x₀+1, x₀−1) = 2. Deduce that one of two cases arises: Case 1. x₀ − 1 = 2pu², x₀ + 1 = 2v². Case 2. x₀ − 1 = 2u², x₀ + 1 = 2pv². Show that in Case 1, v² − pu² = 1 with |u| < y₀, a contradiction to the minimality of y₀. Show that in Case 2, u² − pv² = −1 …"
  The same exercise text is quoted in Math.SE Q11305 (read via the StackExchange API, `https://api.stackexchange.com/2.3/questions/11305?site=math&filter=withbody`). The accepted answer gives the key step: "exactly one of x₀+1 and x₀−1 is divisible by p … two co-prime integers whose product is a square, therefore each must be a square".
- **Proof outline (factor argument):** Take the minimal solution of x² − py² = +1. Then x₀ is odd (mod 4), gcd(x₀−1, x₀+1) = 2, and (x₀−1)(x₀+1) = p y₀². Because p is prime, it lies wholly in one factor, so {x₀−1, x₀+1} = {2pu², 2v²}. The split "p with x₀−1" gives a smaller solution of the +1 equation, which contradicts minimality. So the split must be x₀+1 = 2pv², x₀−1 = 2u², and this gives u² − pv² = −1.
- **Composite counterexamples (D ≡ 1 mod 4, non-square, every prime factor ≡ 1 mod 4, but x² − Dy² = −1 has no solution):**
  - **205 = 5·41**
  - **221 = 13·17**
  - **305 = 5·61**
  - **377 = 13·29**
  - **505 = 5·101**
  - also 545, 689, 725 = 5²·29, 745, 793

  I checked these by computer (uv python + sympy, `/tmp/negpell.py`): the continued fraction of √D has even period (8, 6, 4, 4 for the first four), and no convergent gives −1. The same run confirmed odd period for every prime p ≡ 1 (mod 4) below 1200.
  OEIS A031398 (https://oeis.org/search?q=id:A031398&fmt=text) is "Squarefree m with no 4k+3 factors such that Pell equation x^2 − m*y^2 = −1 is insoluble". Its terms are 34, 146, 178, 194, **205, 221, 305, 377**, 386, 410, 466, 482, **505**, 514, **545**, … A031396 is "Numbers k such that Pell equation x^2 − k*y^2 = −1 is soluble". A003814 (odd period) has the comment "All primes of the form 4m + 1 are here."
  Trivially failing composites, because they have a prime factor ≡ 3 mod 4: 21, 33, 57, 69, 77, …
- **Notes:**
  - (i) **Pointwise:** yes, for every prime p ≡ 1 (4).
  - (ii) **Expected witnesses:** O(1). There is exactly one solution class: the fundamental unit has norm −1, and all solutions are its odd powers. The window is huge, since the fundamental solution can be as large as exp(O(√p log p)). Nothing here counts witnesses.
  - (iii) **Mechanism:** algebraic identity plus descent/minimality, with unique factorisation (coprime factors whose product is a square). This is essentially a sign forcing: the +1 equation has only two "trivial" splittings, and one of them is excluded by minimality.
  - (iv) **Where it fails:**
    - D a square >1: no solutions.
    - Composites D = ab: the extra splittings x₀∓1 = 2au², 2bv² give bv² − au² = ±1 instead of −1. This is exactly where primality is used, and it fails for 205, 221, … above.
    - D ≡ 3 mod 4 primes: parity/mod-4 obstruction.

## 2. Elkies: infinitely many supersingular primes for every E/Q

**Status: V** (both papers read).

- **Source 1:** N. D. Elkies, "The existence of infinitely many supersingular primes for every elliptic curve over Q", *Invent. Math.* 89 (1987), 561–567. I read the scan from GDZ: https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0089/LOG_0030.pdf (OCR). The metadata page is https://eudml.org/doc/143494.
  - **Main theorem (OCR, verbatim):** "Theorem 1. Let S be a finite set of primes. Then E has a supersingular prime outside S."
  - **Proposition (§2) (OCR):** for l a prime ≡ −1 mod 4, "modulo l, P_l(X) and P_{4l}(X) factor into (X − 12³)R²(X), (X − 12³)S²(X)". Here P_D is the monic polynomial of CM j-invariants of discriminant −D.
  - **Proof (OCR):** "By Dirichlet's Theorem there exists a prime l > L_J such that (−1/l) = −1 but (p/l) = +1 for every p∈S. We claim that the factorization of the numerator of either P_l(J) or P_{4l}(J) contains a prime which is either l itself or a quadratic non-residue of l … P_l(J)P_{4l}(J) is a negative rational number whose denominator is a perfect square … would therefore be a quadratic non-residue of l. But by our Proposition, P_l(X)P_{4l}(X) is a square mod l — contradiction!"
  - The sign comes from the fact that j((1+√−l)/2) and j(√−l) are the only real roots, tending to −∞ and +∞. Hence "for fixed J, P_l(J) > 0 and P_{4l}(J) < 0 for l sufficiently large, say l > L_J."
  - **Explicit bound: none in the 1987 paper.** The paper states no bound for the least supersingular prime in terms of conductor or j-invariant. §4 adds that a supersingular p is detected by some D < 2p^{2/3}, using geometry of numbers on End(E_p)/Z.
  - Theorem 2 covers E over K with [K:Q] odd. For [K:Q] even the method only works for "most" J. Elkies gives a Q(i) example where heuristically only C log log x supersingular primes exist up to x.
- **Source 2:** N. D. Elkies, "Distribution of supersingular primes", *Astérisque* 198-199-200 (1991), 127–132. I read https://smf.emath.fr/download/pdf/42001 (numdam AST_1991__198-199-200__127_0).
  - The iteration gives "an implicit upper bound on p_n … Dirichlet's theorem gives an effective bound on the least admissible l, and the absolute value of the numerator of P_D(J_E) … is easily bounded above by O(exp C·D^{1/2} log² D). Unfortunately this bound on p_n is astronomical—an n-fold iterated exponential!—unless we assume the GRH for real Dirichlet characters. Applying the standard explicit formulas for the number of primes in an arithmetic progression, we then find that π₀(x) ≫ log log log x; this bound, since independently discovered by Brown [1], has been improved by R. Murty to π₀(x) ≫ (log log x)^{1/2}."
  - "THEOREM A: Under GRH for real Dirichlet characters, π₀(x) ≫ log log x." This is Theorem 2 of Elkies' thesis.
  - "THEOREM B: π₀(x) ≪ x^{3/4}." This one is unconditional, via Kaneko's D < 4√p/3.
  - Conjecture (Lang–Trotter): π₀(x) = (C+o(1)) x^{1/2}/log x.
- **Best unconditional lower bound (V):** É. Fouvry, M. R. Murty, "On the distribution of supersingular primes", *Canad. J. Math.* 48 (1996), 81–104. I read https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008414X00034076 and checked the formula against the page image.
  - "THEOREM 1. For any elliptic curve E and for any positive δ, there exists x₀(E,δ) such that the inequality π₀(x) ≥ log₃x/(log₄x)^{1+δ} holds for x > x₀(E,δ)." Here log_k is the k-fold iterated logarithm.
  - They also state that Elkies–Murty obtained π₀(x) > log₂x under RH for Dirichlet L-functions, and Brown obtained log₃x.
- **Notes:**
  - (i) **Pointwise:** yes, for every E/Q (every rational J), and for every finite exclusion set S.
  - (ii) **Expected witnesses:** heuristically ≍ √x/log x supersingular primes up to x, which is a power. The theorem guarantees only one new prime per step, inside an astronomically large window (iterated exponential). Proven counts are triple-log.
  - (iii) **Mechanism:** sign/reciprocity forcing.
    - P_l(J)P_{4l}(J) < 0 (the archimedean sign).
    - It is a square mod l (the CM congruence).
    - Then (−1/l) = −1 forces an odd number of non-residue prime factors.
    - Dirichlet's theorem selects l.
  - (iv) **Limits:** the argument needs J real, i.e. a real embedding. It does not apply to CM-free curves over totally imaginary fields. In Elkies' Q(i) example the expected count drops to ~C log log x. For CM curves the result is trivial: density 1/2.

## 3. Holzer's theorem (small solutions of Legendre's equation)

**Status: V** (original and modern source both read).

- **Original:** L. Holzer, "Minimal solutions of Diophantine equations", *Canad. J. Math.* 2 (1950), 238–244, doi:10.4153/CJM-1950-021-0. Open access: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7016D74F58D7A99CB28679798A61AD2B/S0008414X00025797a.pdf/minimal-solutions-of-diophantine-equations.pdf .
  - Opening statement, verbatim (checked against the page image):
    > "If a, b, c are positive integers, if ab > 1, if a, b, c are relatively prime in pairs, and all are free of squares, if − ab is a quadratic residue of c, bc of a, ca of b, and if F(x, y, z) = ax² + by² − cz², we have non-trivial solutions of (1) F(x,y,z) = 0 with the inequalities |x| < √(bc), |y| < √(ca), |z| < √(ab)."
  - In the case ab = 1 one inequality becomes an equality.
  - Lemma 1 is a pigeonhole statement: it uses more than abc triples in the box [0,√bc]×[0,√ca]×[0,√ab], so two collide mod abc for a linear form. A descent/case analysis (Lemmas 3–5 …) follows.
- **Modern source:** T. Cochrane, P. Mitchell, "Small solutions of the Legendre equation", *J. Number Theory* 70 (1998), 62–66. I read the author PDF (scan, OCR): https://www.math.ksu.edu/~cochrane/research/legendre.pdf .
  - Abstract (OCR): "Holzer, using a deep theorem, proved that if the Legendre equation ax² + by² − cz² = 0 is in normal form and has a nonzero solution then there is a solution with |x| ≤ √bc, |y| ≤ √ac and |z| ≤ √ab. The first elementary proof of this result was given by Mordell with a small gap filled by Williams. We give a new elementary proof … the lattice of solutions of the congruence ax² + by² − cz² ≡ 0 (mod abc) that is constructed in most textbook proofs of Legendre's theorem always contains such a solution."
  - Body text: Holzer used "a deep theorem of Hecke". The bound is equivalent to ax² + by² + cz² ≤ 2abc and cannot be sharpened (example x² + y² − cz² = 0).
  - The OCR renders the inequality signs as "<". They may be ≤ in the scan; I did not check the page image. Holzer's own statement uses strict "<" when ab > 1.
- **Mordell's proof:** L. J. Mordell, "On the magnitude of the integer solutions of the equation ax² + by² + cz² = 0", *J. Number Theory* 1 (1969), 1–3. **NA**: seen only as citations (Semantic Scholar, ADS 1969JNT.....1....1M, and Cochrane–Mitchell). Williams' gap-filling paper is cited by Cochrane–Mitchell, and I did not access it.
- **Notes:**
  - (i) **Pointwise:** yes, for every solvable normal-form equation. Solvability is Legendre's local residue conditions.
  - (ii) **Expected witnesses:** O(1). The box has volume ≍ abc, and the congruence lattice mod abc has index ≍ abc, so the box holds O(1) lattice points. This bound is the natural "one-witness" scale.
  - (iii) **Mechanism:** pigeonhole/collision (Holzer Lemma 1), i.e. geometry of numbers on the lattice mod abc, followed by descent. Holzer additionally used Hecke.
  - (iv) **Where it fails:** it fails whenever the local residue conditions fail. In that case there are no solutions at all, and the obstruction is local/Hilbert-symbol rather than "squares". No primality is needed. Squarefreeness and pairwise coprimality (normal form) are hypotheses.

## 4. Deuring / Waterhouse: every |t| ≤ 2√p is a Frobenius trace over F_p

**Status: V** (Waterhouse read; Deuring original NA).

- **Source:** W. C. Waterhouse, "Abelian varieties over finite fields", *Ann. Sci. ÉNS* (4) 2 (1969), 521–560, **Theorem 4.1 (p. 536)**. I read http://www.numdam.org/item/ASENS_1969_4_2_4_521_0.pdf. The text layer is OCR, and I fixed obvious glyphs.
  - The setup is a finite field k with q = p^a elements.
  - Verbatim: "THEOREM 4.1. — The isogeny classes of elliptic curves over k are in one-to-one correspondence with the rational integers β having |β| ≤ 2√q and satisfying some one of the following conditions:
    - (1) (β, p) = 1;
    - (2) If a is even: β = ±2√q;
    - (3) If a is even and p ≢ 1 mod 3: β = ±√q;
    - (4) If a is odd and p = 2 or 3: β = ±p^{(a+1)/2};
    - (5) If either (i) a is odd or (ii) a is even and p ≢ 1 mod 4: β = 0."
  - Chapter 4 opens: "Most of the results are from Deuring's classical paper [6]". That is M. Deuring, "Die Typen der Multiplikatorenringe elliptischer Funktionenkörper", *Abh. Math. Sem. Hansischen Univ.* 14 (1941), 197–272. **NA** for the original.
- **Consequence for q = p prime (a = 1):** every integer t with |t| ≤ 2√p occurs as a trace.
  - Condition (1) covers p ∤ t.
  - In the window, p | t only for t = 0 (and t = ±p when p ≤ 4, i.e. ±2 for p = 2 and ±3 for p = 3). Condition (5) gives 0 and condition (4) gives ±p for p = 2, 3.
  - The trace is β, since #E(F_p) = p + 1 − β.
- **Notes:**
  - (i) **Pointwise:** yes, for every prime p and every t in the Hasse window.
  - (ii) **Expected witnesses:** a power. The number of curves with trace t is ≍ H(t² − 4p), a Hurwitz class number of size ≈ √p up to logs.
  - (iii) **Mechanism:** algebraic (Honda–Tate / Deuring lifting). One needs an imaginary quadratic order of discriminant t² − 4p and CM theory. It is not analytic.
  - (iv) **Where it fails:** over F_{p^a} with a > 1, multiples of p are restricted, so "every t" is false for prime powers. Primality of the field size is exactly what makes the statement clean.

## 5. Lehmer's conjecture τ(n) ≠ 0

**Status:** the record is **V**. Lehmer's 1947 statements are **V2** (from Wikipedia and Derickx–van Hoeij–Zeng). Lehmer's Duke paper itself was not opened.

- **Original:** D. H. Lehmer, "The vanishing of Ramanujan's function τ(n)", *Duke Math. J.* 14 (1947), 429–433, doi:10.1215/s0012-7094-47-01436-1. **NA** for the text.
  - Wikipedia (https://en.wikipedia.org/wiki/Ramanujan_tau_function): "Lehmer (1947) conjectured that τ(n) ≠ 0 for all n … Lehmer verified the conjecture for n up to 214 928 639 999 (Apostol 1997, p.22)."
  - Wikipedia's progress table: 3 316 799 (Lehmer 1947); 214 928 639 999 (Lehmer 1949); 10^15 (Serre 1973/1985); 1 213 229 187 071 998 (Jennings 1993); 22 689 242 781 695 999 (Jordan–Kelly 1999); 22 798 241 520 242 687 999 (Bosman 2007); 982 149 821 766 199 295 999 (Zeng–Yin 2013); **816 212 624 008 487 344 127 999 (Derickx–van Hoeij–Zeng 2013)**.
- **Current record, read in source:** M. Derickx, M. van Hoeij, J. Zeng, "Computing Galois representations and equations for modular curves X_H(ℓ)", arXiv:1312.6819v2 (18 Mar 2014). I found it via http://export.arxiv.org/api/query?search_query=all:%22modular%20curves%22%20AND%20au:Derickx%20AND%20au:Hoeij and read the PDF at https://arxiv.org/pdf/1312.6819v2. I found no journal version.
  - "Corollary 1.2. The non-vanishing of the Ramanujan tau function τ(n) holds for all n with n < 816212624008487344127999 ≈ 8·10²³."
  - "Remark 1.3. In [16] this was verified for n < 982149821766199295999 ≈ 9·10²⁰" ([16] = Zeng–Yin, *Math. Comp.*).
- **Method (§4 of DHZ, verbatim-ish):**
  - By Serre, "if p is prime number satisfying τ(p) = 0 then p can be written as p = hM − 1 with M = 2¹⁴3⁷5³691, ((h+1)/23) = 1, and h mod 49 ∈ {0, 30, 48}". The exponents are read from OCR'd PDF text.
  - Lemma 4.1: τ(p) ≡ 0 mod ℓ iff Q^red_{12,ℓ}(x) mod p has an irreducible quadratic factor. This uses explicit projective mod-ℓ Galois representations for ℓ ∈ {11, 13, 17, 19, 29, 31, 41}.
  - "the first prime number p satisfying Serre's criteria as well as τ(p) ≡ 0 mod 11·13·17·19·29·31·41 is 816212624008487344127999."
  - Lehmer's reduction: the least n with τ(n) = 0 would be a prime. This follows from multiplicativity and the Hecke recursion; it is standard and stated in the Wikipedia/MathOverflow context, but I did not read it in Lehmer's paper.
- **Status:** **open.** arXiv:1406.3607 (2014) claims a proof that has not been accepted. I saw only its search abstract and did not evaluate it.
- **Notes:**
  - (i) **Pointwise:** verified for every n below the bound; conjectured for all n.
  - (ii) **Expected witnesses:** heuristically, P(τ(p) = 0) ~ p^{−11/2}·(stuff). The sum converges, so the expected number of zeros is finite and tiny, i.e. 0. This is a "no-witness" (non-existence) statement, not an existence statement.
  - (iii) **Mechanism:** congruences / Chebotarev (Galois-representation sieve over residue classes). Serre's results give density zero of primes with τ(p) = 0.
  - (iv) **Contrast:** for CM newforms a_p = 0 for half of all primes, and for weight-2 non-CM forms Elkies (item 2) gives infinitely many zeros. Non-vanishing therefore depends on weight and non-CM. No primality condition is involved.

## 6. 15-theorem (Conway–Schneeberger) and 290-theorem (Bhargava–Hanke)

**Status: V** (both read).

- **15-theorem:** M. Bhargava, "On the Conway–Schneeberger Fifteen Theorem", in *Quadratic Forms and Their Applications* (Dublin 1999), Contemp. Math. 272, AMS 2000, pp. 27–37. I read the proceedings PDF https://webhomes.maths.ed.ac.uk/~v1ranick/books/dublin.pdf .
  > "Theorem 1 ("The Fifteen Theorem"). If a positive-definite quadratic form having integer matrix represents every positive integer up to 15 then it represents every positive integer."
  - The theorem was announced by Conway and Schneeberger in 1993. The original proof was unpublished, and a sketch appears in Schneeberger's thesis. The proof uses escalator lattices and the "truant" (the smallest non-represented integer).
- **290-theorem:** M. Bhargava, J. Hanke, "Universal quadratic forms and the 290-Theorem", preprint (2005/2011). I read https://math.stanford.edu/~vakil/files/290-Theorem-preprint.pdf (8 pp.).
  > "Theorem 1 ("The 290-Theorem") If a positive-definite quadratic form with integer coefficients represents the twenty-nine integers 1, 2, 3, 5, 6, 7, 10, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 34, 35, 37, 42, 58, 93, 110, 145, 203, and 290 then it represents all positive integers."
  - Theorem 2 says each of the 29 integers is critical. Theorem 3 says that representing every positive integer below 290 implies representing every integer above 290. Theorem 4 says "There are exactly 6436 universal quaternary forms."
  - Publication status: Wikipedia (https://en.wikipedia.org/wiki/15_and_290_theorems) says "a 2011 preprint … as of 2026 it has not been published". Older citations say "Invent. Math., to appear".
- **Notes:**
  - (i) **Pointwise:** yes, for every positive integer, for each universal form.
  - (ii) **Expected witnesses:** a power. The representation numbers r_Q(n) for quaternary forms grow like n^{1−ε}, from Eisenstein-series main terms. The theorem is "every n has ≥ 1".
  - (iii) **Mechanism:** escalation (finite combinatorial reduction), then the local–global principle with effective bounds. For 290 this means Fourier coefficients of weight-2 theta series: Eisenstein main term against cusp-form error (Deligne), plus massive computation for the small exceptional n.
  - (iv) **Where it fails:** ternary forms are never universal. For example, x²+y²+z² misses every n = 4^a(8b+7) (Legendre–Gauss; standard, not re-read here). Quaternary forms with an anisotropic prime can miss infinitely many n. Universality needs ≥ 4 variables, and the 15/290 lists are exactly the finite obstruction sets. No primality condition is involved. (My own commentary; not quoted.)
