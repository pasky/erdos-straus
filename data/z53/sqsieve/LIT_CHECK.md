# Literature check (primary sources where possible)

Legend: **[P]** I read it in the primary source. **[S]** secondary source only. **[own]** my own derivation or check.

## 1. Bourgain: (13/84+ε, 55/84+ε) is an exponent pair
- Source: arXiv:1408.5794v2, https://arxiv.org/pdf/1408.5794v2 (published as JAMS 30 (2017) 205–224; I did not check the JAMS page numbering against the arXiv version). **[P]**
- **Theorem 6** (§5 "Further comments"), quoted from the text: "*Theorem 6.* (ε + 13/84, ε + 55/84) is an exponent pair."
- The paragraph before it:
  "|S| ≪ M^{1/2} T^{ε+13/84} if 1/2 ≥ α = log M/log T > 0 (5.1) provided f is in the class of functions to which the exponent pair theory applies (see for instance [G-K], Ch. 3 for details)."
  [G-K] = Graham–Kolesnik, *Van der Corput's Method of Exponential Sums*, LMS LN 126.
- Setup in §3 (Theorem 4 / (5.1) are stated under it): "Let F be a smooth function on [1/2,1] satisfying, for some constant c∈(0,1], the condition min{|F''(x)|,|F'''(x)|,|F''''(x)|} > c. (3.1) Given T sufficiently large, M ≥ 1, put f(u)=T F(u/M) with M/2 ≤ u ≤ M and S=Σ_{m∼M} e(f(m)). (3.2) … we assume M ≤ √T".
- Restriction in §4 (p. 19): "(4.2) and also (4.1) assume additional hypotheses concerning the function F, beyond condition (3.1). … Assume henceforth that F is 'a suitable function' such that (4.1) and (4.2) are applicable." The paper does not list these conditions. It says they hold for F = log x.
- The proof of Theorem 6 is only a sketch. It deals with (a) M > √T by a B-process and "M ≥ T^{9/10}" via the pair (1/2,1/2). It deals with (b) sums over a subinterval [a,b] ⊂ (M/2,M] by extending f under "[G-K], Condition (3.3.3)" and using "[S], lemma 2.1" (Sargos, PLMS 70 (1995)), "at the cost of losing a harmless factor O(log M)".
- **So which class of phase functions?** The paper does not define one itself. It uses the G-K Ch. 3 class (monomial-type f' ≈ y x^{−s}, see item 2). Later uses also read it this way:
  - Trudgian–Yang, arXiv:2306.05599 §1.1, list θ=13/84 as "Bourgain [Bou16]" in the family (θ+ε, 1/2+θ+ε) under the G-K definition. **[P for T-Y]**
  - Tao–Trudgian–Yang, arXiv:2501.16779, restrict to "model phase functions" with F^{(p+1)}(u) − d^p/du^p u^{−σ} = o(1). They write: "In [Bou17], the exponent pair (13/84, 55/84) was established". **[P for TTY]**
- **[own] Does X/x or X/(x+a), 0≤a<1, qualify?**
  - f(x) = X/x: −f′ = X x^{−2} exactly, so it is in G-K's class with s=2, y=X, after conjugating the sum.
  - f(x) = X/(x+a): the derivatives of −f′ = X(x+a)^{−2} differ from those of X x^{−2} by a relative factor (1+a/x)^{−2−p} = 1+O_p(a/N). So it lies in F(N,P,2,X,ε) once N ≥ N₀(P,ε).
  - **Restriction to keep in mind:** the G-K/T-Y definition only claims the bound for y ≥ N^σ, i.e. L = |f′| ≍ X/N² ≥ 1, so N ≤ √X. For N > √X, use Kusmin–Landau / the first-derivative test instead.

## 2. Graham–Kolesnik definition of exponent pair (Ch. 3)
- I could not access the book, so this is **[S]**. The quote below is G-K's definition as restated by Trudgian–Yang, arXiv:2306.05599v3 §1.1 (https://arxiv.org/pdf/2306.05599v3), "we refer the reader to [GK91]":
  "Let F(N,P,σ,y,c) denote the set of functions f: I=(a,b] ⊆ [N,2N] → R, such that f has P continuous derivatives and for which |f^{(p+1)}(x) − d^p/dx^p (y x^{−σ})| ≤ c |d^p/dx^p (y x^{−σ})| (1.1) for all x∈I, 0≤p≤P−1. … (k,ℓ) ∈ {0≤k≤1/2≤ℓ≤1, k+ℓ<1} ∪ {(1/2,1/2),(0,1)}. Then, (k,ℓ) is a (one-dimensional) exponent pair if for all σ>0, there exists some P=P(k,ℓ,σ) and c=c(k,ℓ,σ)<1/2 such that Σ_{n∈I} e(f(n)) ≪_{k,ℓ,σ} (y/N^σ)^k N^ℓ, (y ≥ N^σ), (1.2) uniformly for all f ∈ F(N,P,σ,y,c)."
- Bourgain cites "[G-K], Condition (3.3.3)" for the derivative conditions, which fits (1.1) being G-K's (3.3.3). **[P: Bourgain's citation; S: content]**

## 3. Weil bound and the twisted Legendre sum
- **Iwaniec–Kowalski, *Analytic Number Theory* (AMS Colloq. 53, 2004), Ch. 11.** Kowalski hosts the chapter at https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf. **[P]**
  - "Theorem 11.11 (Weil). Assume that ψ and ϕ are non-trivial and p ≠ 2. Then the roots α and β for the Kloosterman sum S(ψ,ϕ) satisfy |α|=|β|=√q, and therefore we have |S(ψ,ϕ)| ⩽ 2√q. (11.15)"
  - "Corollary 11.12. Let a, b, c be integers, c positive. We have |S(a,b;c)| ⩽ τ(c)(a,b,c)^{1/2} c^{1/2}. (11.16)" For c=p prime with p∤ab this gives |S(a,b;p)| ≤ 2√p. The proof also covers p=2.
- Original: A. Weil, "On some exponential sums", Proc. Nat. Acad. Sci. USA 34 (1948) 204–207. I took the reference from IK's bibliography [We1] and Tolev arXiv:1007.2054. I did not open the PNAS paper.
- Salié sums: IK Ch. 11 (right after (11.7)) say "T(a,b;p)=Σ* (x/p) e((ax+b x̄)/p) … can be explicitly computed (see Lemma 12.4…)". **[P for the remark; Lemma 12.4 not read]**
- **The evaluation of Σ_x ((x²−d)/p) e(lx/p)** **[own]**. I found no citable source with a theorem number. The derivation is short:
  - For p odd, #{y : y² ≡ x²−d} = 1 + ((x²−d)/p). So for p∤l, Σ_x ((x²−d)/p) e(lx/p) = Σ_{x²−y²=d} e(lx/p).
  - Put u = x+y, v = x−y, so uv = d. Then the sum is Σ_{u≠0} e(2̄ l(u + d ū)/p).
  - Result: for p∤ld it equals **S(2̄l, 2̄ld; p) = S(1, 4̄ l² d; p)**, which is a *Kloosterman* sum, not a Salié sum. So it is ≤ 2√p by Weil.
  - For p | d and p∤l the sum equals −1.
  - Checked numerically for every d, l mod p with p ∈ {3,5,7,11,13,101}; maximum error 8e−13.

## 4. Titchmarsh, Theorem 5.11 (third-derivative test)
- Source: Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown (OUP 1986), p. 106. Scanned copy: https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf (PDF page 58). I read it from the rendered page image. **[P]**
- Verbatim: "**5.11. Theorem 5.11.** *Let f(x) be real and have continuous derivatives up to the third order, and let λ₃ ⩽ f‴(x) ⩽ hλ₃, or λ₃ ⩽ −f‴(x) ⩽ hλ₃, and b−a ⩾ 1. Then* Σ_{a<n⩽b} e^{2πif(n)} = O{h^{1/2}(b−a)λ₃^{1/6}} + O{(b−a)^{1/2}λ₃^{−1/6}}."
- Note: the constant is called **h**, not α. The O-constants are absolute.
- The proof uses Theorem 5.9 (second-derivative test) and Lemma 5.10 (Weyl–van der Corput).
- Restatement with C(α) and α≥1: O. Robert, hal-01464831, Theorem 2. That version has a typo, f'' in place of f‴. **[P]**

## 5. Priority search
- **No hit found** for either of these:
  - the square sieve, or a Poisson/Kloosterman treatment of the strip, applied to 4uBC − u − B = n or to Erdős–Straus counts;
  - counting xy ≡ 1 (mod N) with x ≡ y ≡ −1 modulo a varying modulus.
- Searches performed:
  - arXiv API: all:"Erdos-Straus"; all:"Erdős-Straus"; abs:"square sieve"; abs:"unit fractions" AND abs:"Kloosterman" (0 results).
  - Web (Jina): "square sieve Erdős-Straus equation number of solutions"; "Kloosterman sums Erdős-Straus Type II solutions pointwise upper bound"; "upper bound number of solutions Erdős-Straus equation improvement n^{3/5} 2/5 type II"; "Heath-Brown square sieve unit fractions 4/n count solutions"; "modular hyperbola xy≡1 mod p points with x y in arithmetic progression Kloosterman". The last one only returned Shparlinski's modular-hyperbola survey (arXiv:1103.2879), which is generic and does not match.
  - I skimmed all the abstracts these searches returned.
- **Known pointwise bounds** **[P]**:
  - Elsholtz–Tao, arXiv:1107.1010v6, Prop. 1.7: "f_I(n) ≪ n^{3/5+O(1/log log n)} and f_II(n) ≪ n^{2/5+O(1/log log n)}". The proof (§3) uses only the divisor bound. They add: "Proposition 1.7 appears to be the limit of what one can obtain purely from the divisor bound (A.6) alone".
  - Elsholtz–Planitzer, arXiv:1805.02945, Thm 1: O_ε((n^{3/5}/m^{2/5}) n^ε)-type bound for general m/n, i.e. n^{3/5+ε} for fixed m. It has no Type II or per-slice bound below n^{1/3}.
- **Closest recent items (not priority conflicts):**
  - arXiv:2609.09204 (X. Jiang, 2026), "Counting Type I and Type II solutions…": #Type II solutions with Y ≤ K is ≤ Σ_{n≤K} τ(n) = K log K + O(K), uniformly. This is a parametrised count, not a pointwise n^θ bound. It uses no square sieve or Kloosterman sums.
  - arXiv:2608.24035 (Dahan, 2026): sieve dimension and search depth. Not related.
- Conclusion: I found nothing that gives f_II(n) (or its c=1 slice) below n^{1/3}. The best stated bound is still n^{2/5+o(1)}.

## 6. Heath-Brown & Pierce, class numbers, Compositio Math. 153 (2017) 2287–2309, arXiv:1409.3177
- **[P]** The premise is **wrong**. This paper does **not** use the square sieve. "square sieve" never appears in the arXiv v2 text.
- What it does: "Our approach is to develop an unconditional upper bound for h_ℓ(−d) that holds for almost all d, by using the relation between h_ℓ(−d) and small split primes … To treat higher moments, we combine this with upper bounds for the number of simultaneous representations of integers by certain polynomials". The large sieve (§2, (2.6)) is used to show few d have |Σ_{Z≤p<2Z} χ_d(p)| large.
- The square/power sieve combination by these authors is **Heath-Brown & Pierce, "Counting rational points on smooth cyclic covers", arXiv:1109.1455** (J. Number Theory 2012). Abstract: "…a new bound for the number of perfect r-th power values of a polynomial with nonsingular leading form, obtained via a combination of an r-th power sieve and the q-analogue of van der Corput's method." **[P: abstract]**
- Square sieve + large sieve is in S. Baier, arXiv:1506.06148: "a short alternative proof using Heath-Brown's square sieve of a bound of the author for the large sieve with square moduli." **[P: abstract]**
