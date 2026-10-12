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
(rows end where the run stopped; `data/ffl/grid.txt` is authoritative.)

**k = 2** (FAIL counts; exhaustive):

| (q, A) \ n | 3 | 4 | 5 | 6 | 7 | 8 | 9–15 |
|---|---|---|---|---|---|---|---|
| (2, any A of deg 2) | 0 | 0 | 0 | 0 | 0 | 0 | 0 (T², T²+T+1 run to n = 22–23) |
| (3, T²) | 3/8 | 2/18 | 2/48 | 0/116 | 0 | 0 | 0 (to n = 15, 956576 P) |
| (3, T²+1) | 2/8 | 0 | 0 | 1/116 | 0 | 0 | 0 (to n = 15) |
| (4, T²) | 8/20 | 12/60 | 16/204 | 6/670 | 4/2340 | 0/8160 | 0 (n = 9..11) |
| (5, T²) | 24/40 | 49/150 | 82/624 | 81/2580 | 38/11160 | 15/48750 | running |

## 4. Obstruction structure: what replaces the odd-square obstruction

**Proposition 4.1 (sign of a Type II class; PROVED, O140 §3.2 made exact).** For a Type II datum (a, b, c, d) of P
(P = Aabd − E, Ec = a + b, gcd(a, b) = 1) put f := A·a·c·d − 1 (monic, ≡ −1 mod Ad and mod a). Then
E·f = P + A·a²·d, so P ≡ −A·a²·d (mod f), and the Jacobi symbol satisfies
`(P/f) = (−Ad/f) = (−1)^{((q−1)/2)·((1 + deg f)(1 + deg Ad) − 1)}`.
*Proof.* Ef = Aacd·E − E = Aad(a + b) − E = Aa²d + (Aabd − E). Quadratic reciprocity in F_q[T] for monic
coprime f, g: (g/f) = (−1)^{((q−1)/2)·deg f·deg g}(f/g). With (f/Ad) = (−1/Ad) = (−1)^{((q−1)/2)deg Ad} and
(−1/f) = (−1)^{((q−1)/2)deg f}, the exponents add up as stated. ∎
Checked by `scripts/ffl_jacobi_check.py` (sympy): all 3953 Type II data on irreducible P with deg f ≥ 1, for
(q, A, n) = (5, T, 4), (7, T, 4), (3, T², 5), (7, T², 4), with 0 mismatches.

Over Z the corresponding sign is always −1, because f ≡ −1 (mod 4) fixes (−1/f). So every Type II class
is a non-residue class mod its own modulus, and perfect squares (residues mod everything) are never Type II
solvable. That is the T1/odd-square obstruction (ET Prop 1.6). Over F_q[T]:
* **q ≡ 1 (mod 4): the sign is always +1.** Type II classes are *residue* classes mod f, the opposite of Z.
  A P could be obstructed only if (P/f) = −1 for every monic f. For monic P the only candidates are
  P = u·M² with u a non-square constant: then (P/f) = (−1)^{deg f}·1 ≠ −1 when deg f is even. Since u = lc(P) = 1,
  no monic P is obstructed, squares included (cf. O157's example A = T², P = (T²+2)² over F₅).
* **q ≡ 3 (mod 4): the sign is −1 iff deg f odd or deg(Ad) odd.** These are only the parity sub-families
  (O140). Every class keeps the families with deg f and deg Ad both even, whose sign is +1, so again no monic P
  is obstructed. The infinite place enters through degree parity, and a degree is never forced by a
  congruence mod Ad. Over Z, "f > 0 and f ≡ −1 (mod 4)" forces the sign.
* **Conclusion (PROVED at the level of Type II classes; EVIDENCE for full solvability).** There is no
  obstruction class of monic P in F_q[T] for any q. Over Z, B5/T1 comes from the archimedean sign and the
  2-adic class of 4. Over F_q[T] both are replaced by degree parity, which no congruence controls.

**What survives (EVIDENCE).** Two biases, neither of them an obstruction:
(i) *Size class P ≡ 1 (mod W)* (O140 Prop 4.1: uncoverable by linear families). In the data every irreducible P
with N_II(P) = 0 at q = 5, n ≥ 8 has P(0) = 1. At q = 7, n = 6, 3 of the 4 failures have P(0) = 1 (the 4th has
P(0) = 2). The classes P(0) ∈ {−1, −2} never fail (Prop 1.4).
(ii) *Quadratic tilt.* Prop 4.1 makes Type II classes prefer (−AP/f) = +1 (always for q ≡ 1 mod 4; for 3 of the 4
parity patterns when q ≡ 3 mod 4). Class means of N_II by ℓ = T − c show it. Excluding the class P(c) = −1,
mean N_II is higher when χ(−c·P(c)) = +1. Pairs below are (mean over χ = +1 classes, mean over χ = −1 classes):
q = 5, n = 8: c = 1: 35.6, 34.5; c = 2: 38.2, 33.8; c = 3: 38.2, 34.1; c = 4: 38.6, 34.9.
q = 7, n = 7: c = 1: 17.9, 16.9; c = 2: 19.1, 17.2; c = 3: 18.4, 17.6; c = 4: 19.1, 17.2; c = 5: 18.4, 17.5;
c = 6: 18.4, 17.5.
The tilt is ~5–15 % per ℓ. Over Z it is ×14 across classes mod 840, because there the sign is rigid and the
small primes 3, 5, 7 have large weight 1/ℓ. Here each degree-1 ℓ has weight ~1/q, and the sign is not rigid
for q ≡ 3 (mod 4).

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
the class 𝒞 = {P ≡ −1 + h·v₀ (mod hA)}. For P in it, h | P + 1 and (P+1)/h ≡ v₀ (mod A) is coprime to A, so
the A-part of P + 1 is exactly h. Conversely every P with h(P) = h lies in exactly one such class. If
r := −1 + h·v₀ is not coprime to hA (possible when a prime ℓ | A does not divide h), the class contains no
irreducible P of degree n > k and can be dropped. Otherwise Fact 5.2 applies to it. Let
𝒢 := {g monic irreducible: 1 ≤ deg g ≤ m₂, g ∤ A, g ≡ −v₀ (mod A)}.
For g ∈ 𝒢 with g | P + 1, Lemma 5.1 applies. We have gcd(g, h) = 1. Also A·h·g | P + 1 + hg, since
(P + 1 + hg)/h = w + g with w := (P+1)/h; g | w (as g | hw, gcd(g, h) = 1) and w + g ≡ v₀ − v₀ ≡ 0 (mod A),
with gcd(A, g) = 1, so Ag | w + g. Finally deg(Ahg) ≤ k + H + n/5 ≤ n for n large. So P ∈ 𝒞 is solvable unless
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

## 6. Small characteristic: both covering obstructions vanish, and uniform proofs exist

**Theorem 6.1 (F₂, A = T²; PROVED).** Every irreducible P ∈ F₂[T] of degree n ≥ 3 satisfies ES₂(T², P), via
an explicit identity.
*Proof.* P has no root in F₂, so P(0) = P(1) = 1. If P ≡ 1 (mod T²), then P ≡ −1 and Prop 1.4(i) applies.
Otherwise P ≡ 1 + T (mod T²). Then R := (P + T + 1)/T² is monic of degree n − 2 ≥ 1 with R(1) = P(1) = 1. Hence
c := (R + 1)/(T + 1) is monic of degree n − 3, and
`T²/P = 1/R + 1/(cP) + 1/(cRP)`,
since cP + R + 1 = c(P + T + 1) = cT²R. The degrees are n − 2, ≥ n, ≥ n, so NC holds. ∎
(Type II datum (a, b, c, d) = (1, R, c, 1), E = T + 1; the family is linear in P in O140's sense.)
EVIDENCE consistent: the exhaustive run finds N_II(P) ≥ 1 for every irreducible P, n = 3..24.

**Why this exists over F₂ and not over Z (PROVED analysis).** Two mechanisms, both absent over Z:
(a) **Collapse of the size obstruction in char 2 and 3.** O140 Prop 4.1 (char ≥ 5) shows that no linear family
is valid on P ≡ 1 (mod W_F). The proof excludes E = −1 because lc(E) ∈ {1, 2}. In char 2, 1 = −1, and in
char 3, 1 = −2. So the "size-obstructed" class P ≡ 1 (mod A) *is* the trivially solvable class P ≡ −1 resp.
−2 of Prop 1.4. Over Z, 1 ≢ −1, −2 (mod 4): the class n ≡ 1 stays uncoverable (it is the class of the hard
primes).
(b) **T^q − T confines primes.** Every irreducible P of degree ≥ 2 is a unit modulo T^q − T = ∏_{c∈F_q}(T − c),
i.e. its class lies in (F_q^*)^q. For q = 2 this group is trivial, so *all* irreducible P lie in the single
class P ≡ 1 (mod T² + T). Over Z there is no modulus m > 2 for which all large primes share one residue class.
For q = 3 the group (F_3^*)^3 = {±1}^3 still has 8 classes.
Combined with the absence of the square obstruction (§4), char 2 and 3 have **neither** of the two Z
obstructions to a finite covering (Mordell/Theorem C: square classes; O140 Prop 4.1: the class 1). Whether a
finite covering exists is then a finite question per (q, A); §6.2 examines it.

### 6.2 Finite coverings: ES₄(T) is a theorem

A *linear family* F = (E; t_a, a₀; t_b, b₀) (O140 §4, all characteristics) consists of a nonzero E ∈ F_q[T],
monic a₀, b₀, and types t ∈ {0, 1, 2, 3} meaning a = a₀, P·a₀, X/a₀, P·X/a₀ (similarly b), with X := (P+E)/A.
F is *valid at P* if A | P + E, a₀ | X, b₀ | X, s := a + b ≠ 0, E | s and lc(s) = lc(E). Then Lemma 1.3 gives an
NC solution: X, Y = κPX/a, Z = κPX/b with κ = s/E. Put W_F := A·E·lcm(a₀, b₀) (E made monic).

**Lemma 6.2 (validity is a congruence condition; PROVED).** Let W_F | W, and let n_F be 1 + max(k + deg a₀ + deg b₀,
deg E). For monic P of degree n ≥ n_F, the validity of F at P depends only on P mod W.
*Proof.* A | P + E and a₀ | X ⇔ A·a₀ | P + E are conditions mod A·a₀ | W. The four types have degrees deg a₀,
n + deg a₀, n − k − deg a₀ and 2n − k − deg a₀. For n ≥ n_F, a type-t_a term and a type-t_b term with t_a ≠ t_b
have different degrees. Then s has the leading coefficient 1 of its higher term. If t_a = t_b, then
s ∈ {a₀ + b₀, P(a₀ + b₀), (X/L)(L/a₀ + L/b₀), P(X/L)(L/a₀ + L/b₀)} with L = lcm(a₀, b₀), so lc(s) and
"s ≠ 0" are fixed by (a₀, b₀). Finally s mod E is determined by P mod E and by X mod a₀E, b₀E, LE, i.e. by P
mod A·E·L = W_F. ∎

So a set of families whose classes cover all unit classes mod W proves ES_q(A, P) for every irreducible P of
degree ≥ max n_F (P ∤ W). The finitely many smaller degrees are then checked exhaustively.

**Theorem 6.3 (ES over F₄ with A = T; PROVED, computer-assisted).** For every monic irreducible P ∈ F₄[T] of degree
n ≥ 2, `T/P = 1/X + 1/Y + 1/Z` has a solution in monic X, Y, Z (with NC).
*Proof.* W = T⁴ − T = T(T+1)(T+ω)(T+ω²). Irreducible P of degree ≥ 2 lie in the 81 unit classes mod W, i.e.
(P(0), P(1), P(ω), P(ω²)) ∈ (F₄^*)⁴. `scripts/ffl_tree.c` (`ffl_tree 4 10 "10*11*12*13" "10" 9 0 100`) finds for
each class a linear family with W_F | W, k + deg a₀ + deg b₀ < 9 and deg E < 9. The certificate is
`data/ffl/cover_q4_A10.txt`. By Lemma 6.2 this settles every n ≥ 9. For 2 ≤ n ≤ 13 the exhaustive run (§3 table)
finds no failure. ∎
Independent check: each of the 81 families was re-verified on 100 random P of its class (degrees 10–25,
irreducible or not) by the direct identity A·XYZ = P(XY + YZ + ZX) with monic, NC denominators. That is 8100
checks, 0 failures. The certificate needs E only among the units and the monic divisors of degree ≤ 1 of
T⁴ − T (see the file).

### 6.3 Which (q, A) are theorems?

`scripts/ffl_tree.c` builds adaptive covering trees: an uncovered unit class r mod W is refined into its unit
subclasses mod W·ℓ along a fixed list of small primes ℓ. Each leaf carries a linear family with W_F | W_leaf and
n_F ≤ NTH. Each leaf family is re-verified on random P of its class by the direct identity. The theorem for
(q, A) follows from a complete tree plus an exhaustive check of degrees k < n < NTH (Lemma 6.2).
`scripts/ffl_q2_batch.sh` does this for every monic A over F₂ (root W = A·T·(T+1), NTH = 12, exhaustive
n ≤ 11). Results in `data/ffl/q2_batch.txt`.

**Theorem 6.4 (PROVED, computer-assisted).** ES_q(A, P) holds for **every** monic irreducible P of degree > deg A in
the following cases:
* q = 2, A = T or T + 1, and q = 3, A = T (Prop 1.4; no computation);
* q = 2, every monic A of degree 2 or 3 (all 12 of them), and the degree-4 A completed so far (T⁴ and T⁴ + 1:
  trees with 696 and 818 leaves, leaf moduli of degree ≤ 18). The batch over the remaining degree-4 and degree-5 A
  was still running at the time of writing; `data/ffl/q2_batch.txt` is authoritative. The exhaustive
  checks found no exception in degrees k < n ≤ 11;
* q = 4, A = T (Theorem 6.3).

**Not covered (status OPEN, with EVIDENCE).**
* q = 3, A = T²: exhaustive failures only at n = 3, 4, 5 (3 + 2 + 2 polynomials; `data/ffl/fail_q3_A100_n*.txt`),
  none for 6 ≤ n ≤ 13. Covering tree (root T²(T+1)(T+2), refinement by all primes of degree ≤ 2, NTH = 13):
  uncovered density 0.375, 0.236, 0.199, 0.130, 0.082, 0.0115, 0.0111 at depths 1–7. The tree stalls when the
  modulus degree reaches the family limit NTH. We do not know whether a finite covering exists. No obstruction
  is known: the size class P ≡ 1 (mod A) is the E = 2 class in char 3, and §4 excludes quadratic obstructions.
* q = 4, A = T²: uncovered density 0.43 at depth 3.
* **char ≥ 5: no finite covering exists for any A** (O140 Prop 4.1: the class P ≡ 1 (mod W) is uncoverable by
  linear families, and by Dirichlet it contains irreducible P of every large degree). Note: Prop 4.1 covers
  linear families only. A proof for char ≥ 5 would need a non-congruence mechanism, i.e. the lottery (B2).

**Why the theorems do not transfer to Z.** They rest on the two collapses of §6.1(a, b), the absence of the square
obstruction (§4), and (for q = 2, 4) the smallness of (F_q^*)^q. Over Z each fails: 1 ≢ −1, −2 (mod 4); primes
are not confined to few classes mod any m; odd squares are sterile. The function-field world with
char ≥ 5 keeps exactly one of the two Z obstructions (size, P ≡ 1). There, as over Z, the conjecture is a
lottery: the data (§3) show extinction of failures at a finite degree, but no proof mechanism is available.

## 7. Counts, the lottery model, and the two thresholds (EVIDENCE + Assessment)

**7.1 Mean count (EVIDENCE, exact over all irreducible P).** C(q, n) := q^k·mean N_II/n³ (`scripts/ffl_fit.py`):

| n | q=4 | q=5 | q=7 | (q=2, A=T) | (q=2, A=T²) |
|---|---|---|---|---|---|
| 4 | 0.504 | 0.497 | 0.483 | | 0.333 |
| 6 | 0.417 | 0.420 | 0.415 | | 0.337 |
| 8 | 0.382 | 0.382 | 0.370 | | 0.315 |
| 11 | 0.343 | 0.343 | | | 0.284 |
| 13 | 0.326 | | | | 0.272 |
| 20 | | | | 0.271 | 0.237 |

At fixed n the constant does not depend on q (within ±3%). So **mean N_II ≈ C·n³/q^k with C ≈ 0.25–0.5, slowly
decreasing in n**. This is the analogue of f(p) ≍ log³p: q^{−k} plays the role of 1/4 and n that of log p.
The full count N = N_II + 2N_I is ≈ 3–4·N_II in the samples (q = 5, n ≤ 6: mean N = 3.4, 13.1, 20.4, 44.1, 75.9
for n = 2..6).

**7.2 Overdispersion (EVIDENCE).** The zero-probability is far above Poisson:
P(N_II = 0) ≈ exp(−θ·mean N_II), with θ = 0.23–0.29 for q = 5, 7 and n ≥ 5 (Poisson would give θ = 1).
Solutions come in clusters: (a,b) ↔ (b,a), several c | a + b, and one residue condition shared by many data.

**7.3 Model and thresholds (Assessment).** Treat failure as an event of probability exp(−θ'·λ(n)) with
λ(n) = C'·n³/q^k. Two scales follow:
* *bulk transition* (failure fraction ≈ 1/2): n_{1/2} ≍ (q^k)^{1/3}. Below it, almost all P fail. This is O140
  Thm 2.1's regime, n fixed and q → ∞.
* *extinction* (expected number of failures (q^n/n)·e^{−θ'λ} drops below 1): n₀ ≍ q^{k/2}·(log q)^{1/2}, from
  θ'C'n² ≈ q^k·log q.
For N_II alone (θC ≈ 0.09): the last degree with some N_II(P) = 0 is predicted at ≈ 3.3·(q^k log q)^{1/2}. At
q = 5, k = 1 this gives 9.4; observed: the last N_II = 0 is at n = 9 (one P), and n = 10, 11, 12 have none.
For full failures, calibrating on q = 5 (last failure n = 4) and q = 7 (last failure n = 6) gives
n₀ ≈ 1.5·(q log q)^{1/2}.
**Predictions recorded before the runs (A = T):** last failing degree n₀ ≈ 6 (q = 8), 7 (q = 9), 8 (q = 11),
9 (q = 13). Char 2 and 3 may do better, as q = 4 (n₀ = 1, i.e. never) suggests.
