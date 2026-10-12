# FUNCTIONFIELD_ES — Erdős–Straus over F_q[T]: the landscape at fixed q, deg P → ∞ (O161)

Status: in progress (O161). Scripts `scripts/ffl_*`. Background: `BRAINSTORM/ff_erdos_straus.md` (O140; Lemma 1.1,
Prop 1.2, Lemma 1.3, Thm 2.1), `BRAINSTORM/padic_functionfield_igusa.md` (+ errata), triage A/B. ES is not solved
anywhere; nothing here bears on ES over Z except as a model ("toy universe").

Literature (one web search, 2026-10-12): no treatment of a 3-term Erdős–Straus analogue over F_q[T] found
(hits: other Erdős conjectures over F_q[x] — arXiv:2407.15146, Xie arXiv:2510.17612; Guerrieri, "From ancient
Egyptian fractions to modern algebra", is about representability by Egyptian fractions in domains, not 3 terms).
Novelty therefore unverified but plausible.

## 1. The analogue, fixed precisely

Notation: q = p^r, R = F_q[T], P monic irreducible of degree n, A monic of degree k ≥ 1 with P ∤ A.
For a polynomial F write |F| = q^{deg F} (the place ∞).

**Definition 1.1 (ES_q(A, P), the faithful form).** There are monic X, Y, Z ∈ R with
`A/P = 1/X + 1/Y + 1/Z` and `|1/X|, |1/Y|, |1/Z| ≤ |A/P|` (i.e. every denominator has degree ≥ n − k).

The degree condition ("no cancellation at ∞", NC) is the ultrametric image of the archimedean fact that over Z,
`4/n = 1/x+1/y+1/z` with x, y, z > 0 forces every 1/x_i < 4/n. "Monic" is Hayes' sign normalisation of
positivity. Without any sign condition the problem degenerates (§1.4).

**Lemma 1.2 (NC is automatic in char ≥ 3; PROVED).** Let X, Y, Z be monic with A/P = 1/X + 1/Y + 1/Z, and let
m be the number of denominators of minimal degree d₁. The coefficient of T^{−d₁} in the expansion at ∞ is m·1.
(i) If m ≢ 0 (mod p) then d₁ = n − k and m ≡ 1 (mod p). Then NC holds.
(ii) char ≥ 5: m ∈ {1,2,3} is never 0 mod p, so every monic solution satisfies NC, with m = 1 (O140 Lemma 1.1).
(iii) char 3: m = 3 (cancellation, d₁ < n − k) is possible for monic solutions. But a monic solution with
some denominator of degree n − k satisfies NC: if deg Y < n − k, the minimal degree is attained by Y alone or by
Y, Z (m ∈ {1,2}, nonzero), giving degree −deg Y ≠ k − n for the sum.
(iv) char 2: m = 2 (cancellation) is possible; m ∈ {1,3} under NC.
*Proof.* Leading-term bookkeeping, as in O140 Lemma 1.1. ∎

So "monic" alone already gives the faithful analogue in char ≥ 5 (O149's worry that monic allows cancellation is
only realised in char 2 and 3, as triage B observed). In char 2 and 3 we take NC as part of the definition, and
study the monic-only variant M separately (§6).

**Lemma 1.3 (e-slice criterion, all characteristics; PROVED).** ES_q(A, P) holds iff there exist a monic X of
degree n − k and monic a, b | PX with E := AX − P dividing a + b ≠ 0 and lc(a + b) = lc(E).
*Proof.* O140 Lemma 1.3 verbatim; the char ≥ 5 restriction there was used only to locate X. Under NC some
denominator has degree n − k; call it X. Then E ≠ 0 (else A/P = 1/X, impossible by degrees) and deg E < n (AX
and P are monic of degree n). (⇐) gives Y = κPX/a, Z = κPX/b with κ = (a+b)/E monic. NC for Y: if P ∤ a then
deg a ≤ n − k and deg Y ≥ n. If P | a, P ∤ b then deg(a+b) = deg a and deg κ ≥ deg a − (n−1), so
deg Y ≥ n − k + 1. If P | a, b then E | (a+b)/P (gcd(E,P) = 1), deg κ ≥ n, deg Y ≥ n. Same for Z. (⇒) y + z ≠ 0 because y = z = 1 would give 2/g = E/N, and in char 2 this means
E = 0. ∎

**Proposition 1.4 (constant-E classes; degenerations; PROVED, elementary).** Let A be monic of degree k ≥ 1.
(i) If P ≡ −1 (mod A), ES_q(A, P) holds: with X = (P+1)/A, `A/P = 1/X + 1/(PX+1) + 1/(PX(PX+1))`.
(ii) If char ≠ 2 and P ≡ −2 (mod A), ES_q(A, P) holds: with X = (P+2)/A, `A/P = 1/X + 1/(PX) + 1/(PX)`.
(iii) Consequently, **for A = T: over F₂ and F₃ ES_q(T, P) holds for every P ≠ T** (P(0) ∈ F_q^* = {−1} resp.
{−1, −2}). The cases q ∈ {2, 3}, k = 1 are the analogue of "4/n with n ≡ 3 (mod 4) or n even" covering
everything. For q = 4 only the class P(0) = 1 is free; for q = 5, P(0) ∈ {3, 4}.
(iv) Without a sign condition (any nonzero denominators) and k = 1, every P has a solution: write P = AX₀ + r
with r ∈ F_q^*; then A/P = 1/X₀ − r/(X₀P), and the last term can be split into two (e.g. as 2·1/(−2X₀P/r) in odd
characteristic). This is the analogue of 4/(4m+1) = 1/m − 1/(m(4m+1)).
*Proof.* Direct verification. (i), (ii) are the Type II data (a, b, E) = (1, PX, 1) and (P, P, 2) of Lemma 1.3. ∎

Note on symmetries. T ↦ T + β preserves monic polynomials and degrees, so ES_q(A, P) ⇔ ES_q(A(T+β), P(T+β)).
All A of degree 1 are therefore equivalent to A = T. Scalings T ↦ αT do not preserve the problem, because the
denominators have different degrees.

So the data for q ∈ {2, 3} must use k ≥ 2. Below, "A = T" is studied for q ≥ 4 and "A = T²" for all q.

## 2. Engine and validation

`scripts/ffl_es.c` (C, 1 core): for given (q, A, n) it computes
* N_II(P) for **all** monic P of degree n, by the Type II parametrisation (Elsholtz–Tao chart, transported):
  Type II solutions (P | Y, Z) of A/P = 1/X+1/Y+1/Z with deg X = n − k are in bijection with monic (a, b, c, d),
  gcd(a, b) = 1, c | a + b, P = A·a·b·d − E, E := (a+b)/c (then X = abd, Y = acdP, Z = bcdP). Each (a, b, c)
  marks an arithmetic progression of P's (d monic of degree n − k − deg ab), so all of degree n are done at once;
* for every irreducible P with N_II(P) = 0, the complete Lemma 1.3 decision (all X of degree n − k, all divisor
  pairs of PX), which also finds Type I solutions (P divides exactly one denominator);
* optionally, on sampled P, the full count N(P) = #{ordered (X, Y, Z): deg X = n − k} (canonical pairs
  lcm(a, b) = PX in Lemma 1.3). This equals N_II + 2·N_I.
Validation: (i) `scripts/ffl_brute.py`, an independent brute force (enumerate X, Y, solve for Z; no Lemma 1.3),
gives the same N(P) for every irreducible P for (q, A, n) ∈ {(2,T,3..6), (2,T²,4), (2,T²+T,4), (3,T,3..4), (3,T²,4),
(3,T²+T,4), (3,T²+T+2,4), (5,T,3), (5,T²,3), (7,T,3)}; (ii) on every sampled P, the Type II part of the full
count equals the global N_II(P) (checked in-run, no mismatch ever); (iii) O140's table for A = T (q = 5, 7, 11;
n ≤ 6) is reproduced exactly. Field tables: GF(p) and GF(4, 8, 9, 16, 25, 27) via fixed irreducible moduli.
Results: `data/ffl/grid.txt` (one line per run), failure lists `data/ffl/fail_*.txt`.

## 3. Data: A = T (k = 1)

FAIL = #{irreducible P of degree n with no solution} / #irreducible (EVIDENCE: exhaustive, exact).
q = 2, 3: no failures by Prop 1.4(iii) (q = 2 also run to n = 21: minimum N_II = 738 at n = 21).

| q \ n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 0/6 | 0/20 | 0/60 | 0/204 | 0/670 | 0 | 0 | 0 | 0 | 0/381300 |
| 5 | 2/10 | 2/40 | 1/150 | 0/624 | 0 | 0 | 0 | 0 | 0 | 0/4438920 |
| 7 | 6/21 | 21/112 | 25/588 | 16/3360 | 4/19544 | 0/117648 | 0/720300 | | | |
| 8 | 15/28 | 15/168 | 12/1008 | | | | | | | |
| 9 | 18/36 | 56/240 | 94/1620 | 68/11808 | | | | | | |
| 16 | 92/120 | 540/1360 | 2192/16320 | | | | | | | |
(table being extended; see grid.txt)

## 5. Theorem: at fixed q the failures have density 0 (the rigorous counterpart of O140 Thm 2.1)

**Lemma 5.1 (one-prime identity; PROVED).** Let A be monic of degree k ≥ 1, P monic of degree n > k, and let h, g
be monic with g | P + 1, h | P + 1, gcd(g, h) = 1, and A·h·g | P + 1 + h·g, with deg(Ahg) ≤ n. Put
d := (P + 1 + hg)/(Ahg) (monic). Then
`A/P = 1/(hgd) + 1/(dP) + 1/(hgdP)`,
and all three denominators are monic of degree ≥ n − k.
*Proof.* The right side is (P + hg + 1)/(hgdP) = Ahgd/(hgdP). Monic: clear. Degrees: deg(hgd) = n − k. ∎
(It is the Type II datum (a, b, c) = (1, hg, 1), E = 1 + hg.)

**Fact 5.2 (prime polynomial theorem in progressions, RH for curves; standard).** For monic M of degree D ≥ 1 and
r coprime to M, let π(n; M, r) be the number of monic irreducible P of degree n with P ≡ r (mod M). Then
|π(n; M, r) − q^n/(n·Φ(M))| ≤ (D + 2)·q^{n/2}/n, where Φ(M) = |(F_q[T]/M)^*|.
(Rosen, *Number Theory in Function Fields*, Ch. 4, Thm 4.8 and its proof: for each nontrivial χ mod M, L(u, χ)
is a polynomial of degree ≤ D − 1 whose inverse roots have absolute value ≤ √q, by Weil. Hence
|Σ_{deg f = n} Λ(f)χ(f)| ≤ (D − 1)q^{n/2}. Proper prime powers of degree n contribute ≤ 2q^{n/2}.)

**Theorem 5.3 (PROVED, given Fact 5.2).** Fix q and a monic A of degree k ≥ 1. Then
`#{P irreducible, deg P = n : ES_q(A, P) fails} / #{P irreducible, deg P = n} ≤ (Φ(A) + o(1))/log n` as n → ∞.
In particular the failure proportion → 0. Contrast O140 Thm 2.1 (char ≥ 5): at fixed n it → 1 as q → ∞.

*Proof.* Let H := ⌈log_q n⌉ and m₂ := ⌊n/5⌋. For irreducible P (P ∤ A, deg P = n > k) let h = h(P) be the
A-part of P + 1, i.e. the largest monic divisor of P + 1 whose prime factors all divide A. Then v := (P+1)/h is
coprime to A.
(a) *Large A-part.* For fixed h, the P with h | P + 1 lie in one class mod h, so by Fact 5.2 their number is
≤ q^n/(nΦ(h)) + (deg h + 2)q^{n/2}/n. Fix an A-supported monic h of degree D. Then Φ(h) ≥ |h|·∏_{ℓ|A}(1 − 1/|ℓ|)
≥ q^D/2^{ω(A)}. The number of such h is ≤ (D + 1)^{ω(A)}. Summing over D ∈ (H, n] gives a proportion
O_A(H^{ω(A)} q^{−H}) + O(n^{ω(A)+2}q^{−n/2}) = o(1/log n).
(b) *Fixed small A-part.* Fix h (A-supported, deg h ≤ H) and v₀ ∈ (F_q[T]/A)^*. Consider the irreducible P in
the class 𝒞 = {P ≡ −1 + h·v₀ (mod hA)}; there the A-part of P + 1 is exactly h, and (P+1)/h ≡ v₀ (mod A). (The
factor gcd(h, A^∞)-structure makes "mod hA" the right modulus: v₀ is a unit mod every prime of A.) Let
𝒢 := {g monic irreducible: 1 ≤ deg g ≤ m₂, g ∤ A, g ≡ −v₀ (mod A)}.
For g ∈ 𝒢 with g | P + 1, Lemma 5.1 applies. We have gcd(g, h) = 1. Also A·h·g | P + 1 + hg, since
h | P + 1, g | P + 1, and (P + 1 + hg)/h = v + g ≡ v₀ − v₀ ≡ 0 (mod A) (and A, g, h-cofactor coprimality is
handled by CRT). Finally deg(Ahg) ≤ k + H + n/5 ≤ n for n large. So P ∈ 𝒞 is solvable unless
N(P) := #{g ∈ 𝒢 : g | P + 1} = 0.
First moment: P ∈ 𝒞 and g | P + 1 is one class r_g mod hAg, coprime to hAg. By Fact 5.2,
Σ_{P∈𝒞} N(P) = Σ_{g∈𝒢} [q^n/(nΦ(hA)(|g| − 1)) + O(n·q^{n/2}/n)].
Write Π := #𝒞 = q^n/(nΦ(hA)) + O(H q^{n/2}/n) and μ := Σ_{g∈𝒢} 1/(|g| − 1). By Fact 5.2 for the modulus A,
#{g ∈ 𝒢, deg g = m} = q^m/(mΦ(A)) + O(k q^{m/2}/m). Hence μ = (1/Φ(A))·Σ_{m≤m₂} 1/m + O_A(1)
= (log n)/Φ(A) + O_{A}(1).
Second moment: for g₁ ≠ g₂ the conditions form one coprime class mod hAg₁g₂, of degree ≤ k + H + 2n/5. So
Σ_{P∈𝒞} N(P)² = Σ N(P) + Σ_{g₁≠g₂} [q^n/(nΦ(hA)(|g₁|−1)(|g₂|−1)) + O(n q^{n/2}/n)] ≤ Π(μ + μ²) + R, where
R ≪ |𝒢|²·q^{n/2} ≤ q^{2n/5 + 2 + n/2}. The first-moment error is similarly ≪ q^{n/5+1+n/2}. Both are
o(Π) = o(q^{n−k−H}/n), because 2/5 + 1/2 < 1.
So Σ_{P∈𝒞} (N(P) − μ)² ≤ Π·μ + o(Π)·(1 + μ), and Chebyshev gives #{P ∈ 𝒞 : N(P) = 0} ≤ Π·(1/μ + o(1)).
The classes 𝒞 (over h with deg h ≤ H and v₀) partition the irreducible P with deg h(P) ≤ H. Summing,
the failure proportion is ≤ 1/μ + o(1/log n) = (Φ(A) + o(1))/log n. ∎

*Remarks.* (1) The bound 1/log n is an artefact of using one sparse family (prime g). The data (§3) show
the failure proportion decaying like exp(−θ·n³/q^k) and vanishing identically from a finite degree on.
(2) The same proof works over Z: "p + 1 has a prime factor g ≡ −(p+1)/h (mod 4)". It is the classical "almost all
primes" mechanism. It says nothing about every P, which is the lottery (B2).
(3) No characteristic-specific input is used. RH (Weil) only replaces Bombieri–Vinogradov.
