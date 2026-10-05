# EXCEPTIONAL_SPW — towards SPW (task O40)

Status: **checkpoint 1 (O40).** Headline: the O40 target SPW(2, 2/5 − ε) is FALSE for large N (Thm 3.2); the weak form needed by IF2 Thm 5.2 remains open. Labels as in `DISCOVERIES.md`. PROVED =
proved here, internal checks only. Notation: `EXCEPTIONAL_INTERFREQ2.md`
(IF2) §9. N ≥ 2, D := ⌊N/2⌋, `c(b,d) = #{1 ≤ n ≤ N : n ≡ b (d)}`,
`λ_N = 1_{[1,N]}`, L₀ = lcm(1..D). For a measure μ on ℤ and a class s,
`μ(s) = Σ_{x∈s} μ(x)`; the *profile* of μ mod d is `b ↦ μ(b mod d)`.

SPW(C, σ, Δ₀) at N (IF2 §9): R ≥ 0 summable on ℤ with (P1) profile of R
mod d equals c(·,d) for every d ≤ D; (P2) R(s) ≤ 1 − σ for every class s of
modulus > CN; (P3) |R(s) − c(s)| ≤ Δ₀ for classes of modulus in (D, CN].

## 0. Summary (so far)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | SPW at N ⟺ (up to ε) a *periodic* SPW on ℤ/Q′, Q′ = lcm(1..T), T ≥ T(N,C,Δ₀) | PROVED |
| Lemma 1.2 | profile criterion: R has the window profile iff mass N and ∂R ≡ δ₁ − δ_{N+1} (class sums) mod every d ≤ D | PROVED |
| Lemma 1.3 | **two-edge split**: the window profile is `N/d + {−b/d} − {(N−b)/d}`; SPW follows from a single *half-line* (left-edge) measure H (problem HL) | PROVED |
| Lemma 1.4 | **weak SPW suffices**: by Thm 5.2 remarks σ may be quasi-polynomially small, and then only *full* large classes need mass < 1; sparse ones may carry quasi-polynomial mass | PROVED implication |
| §2 | BDW (pointwise density ≤ A·uniform): LP optimum = trivial bound A*(N) for N ≤ 24, but **A(N) ≥ c√N** (exact values A(150) ≥ 1.55, A(400) ≥ 2.50) | EVIDENCE / PROVED |
| §3 | local single-modulus bounds: exact certificates **σ ≤ 72/185 < 2/5 at N = 300**, σ ≤ 0.3811 at N = 1150; LP 0.3737 at N = 4400 | PROVED / EVIDENCE |
| Thm 3.2 | **fixed-σ SPW is false for large N**: σ ≲_C (log N)^{−1/2} (Fejér smoothing + Bernstein at the window edge, modulus e ≈ CN divisible by lcm(1..M)) | PROVED |
| Cor 3.3 | same bound for the Flat margin s₀ (any t) | PROVED |
| §4 | Thm 5.2 survives: only weak SPW (σ_N ≥ e^{−S_A}·c₀) is needed; weak SPW is open | Assessment |

## 1. Reformulations

**Lemma 1.1 (periodic reduction; PROVED).** (a) If R satisfies SPW(C,σ,Δ₀)
at N and Q′ is any multiple of L₀, its projection ρ(x mod Q′) = Σ_{y≡x}R(y)
satisfies (P1), (P2) for every class of modulus e | Q′, e > CN, and (P3) for
e | Q′. (b) Conversely let T ≥ 4(2 + Δ₀)CN, Q′ = lcm(1..T), and let ρ ≥ 0 on
ℤ/Q′ satisfy (P1), (P2) and (P3) for all moduli dividing Q′. For K ≥ N/ε
put `R(x) = ρ(x mod Q′)/K` for 0 ≤ x < KQ′, 0 elsewhere. Then R satisfies
SPW(C, min(σ, 1/2) − ε, Δ₀ + ε) at N.

*Proof.* (a) is immediate (classes mod e | Q′ are unions of classes
mod Q′). (b) For e | Q′ every class mod e meets [0, KQ′) in exactly
K·Q′/e points, whose residues mod Q′ run K times through the class in
ℤ/Q′; so R(s) = ρ(s) exactly — this gives (P1), (P3) (all e ≤ CN ≤ T
divide Q′) and (P2) for e | Q′. If e ∤ Q′ then e > T; put g = gcd(e,Q′).
Since gcd(e/g, Q′/g) = 1, the points s + ke run through the class s mod g
of ℤ/Q′ once per Q′/g consecutive k, and at most ⌈Kg/e⌉ such runs fit in
[0, KQ′). So R(s) ≤ (g/e + 1/K)ρ(s mod g). If g ≤ CN then
ρ(s mod g) ≤ N/g + 2 + Δ₀ and (g/e)ρ ≤ (N + (2+Δ₀)CN)/T ≤ 1/2; if g > CN
then ρ(s mod g) ≤ 1 − σ and g/e ≤ 1/2. The 1/K term is ≤ N/K ≤ ε. ∎

So SPW is a statement about measures on the finite group ℤ/Q′ with
prescribed Fourier coefficients at all characters of order ≤ D (= the
window's) and small mass on all cosets of subgroups of index > CN.

**Lemma 1.2 (profile criterion; PROVED).** For a summable μ on ℤ,
`∂μ(x) := μ(x) − μ(x−1)`. R has the window profile mod every d ≤ D iff
ΣR = N and ∂R − (δ₁ − δ_{N+1}) has zero class sums mod every d ≤ D.

*Proof.* ∂ commutes with taking profiles up to the shift b ↦ b − 1:
the profile of ∂μ mod d is `P(b) − P(b−1)`, P the profile of μ. So
∂(R − λ_N) has zero profile iff the profile of R − λ_N is constant in b,
and the constant is (ΣR − N)/d. ∎

**Lemma 1.3 (two-edge split; PROVED).** (i) For all d ≥ 1 and b,

    c(b,d) = N/d + {−b/d} − {(N−b)/d}.

(ii) *Problem HL(D, E₀, h, m):* find H ≥ 0 summable on ℤ with ΣH = m and,
for every d ≤ D, profile `H(b mod d) = {−b/d} + (m − (d−1)/2)/d`
(a "regularised half-line [1, ∞)"), with H(s) ≤ h for every class s of
modulus > E₀ and H(s) ≤ h_med for moduli in (D, E₀].
If HL(D, CN, h, m) is solvable with m ≤ N/2, then SPW(C, σ, Δ₀) holds at N
with

    σ = 1 − (N − 2m)/(CN) − 2h − ε,    Δ₀ = 3 + N/(D+1) + 2h_med.

*Proof.* (i) `c(b,d) = ⌊(N−b)/d⌋ − ⌊−b/d⌋`; write ⌊y⌋ = y − {y}. (ii) Put
H′(x) := H(N+1−x) and, for J a large multiple of L₀,
U := ((N − 2m)/J)·1_{[1,J]} (uniform profile (N−2m)/d mod d ≤ D, and
U(s) ≤ (N − 2m)/e + ε on classes mod e). The profile of H′ mod d at b is
H's at N+1−b, i.e. `{(b−N−1)/d} + const = 1 − 1/d − {(N−b)/d} + const`
(use {(−y−1)/d} = 1 − 1/d − {y/d} for integers y). Adding, the profile of
R := U + H + H′ is `{−b/d} − {(N−b)/d} + κ_d` with
κ_d = (N − 2m)/d + 2(m − (d−1)/2)/d + 1 − 1/d = N/d, which is c(b,d) by
(i). R ≥ 0. For a class s mod e > CN: R(s) ≤ (N−2m)/(CN) + ε + H(s) + H(s′)
with s′ = N+1−s a class of the same modulus. Medium: |R(s) − c(s)| ≤
max(R(s), c(s)) ≤ N/d + ε + 2h_med + 2. ∎

Notes. The constants are consistent with IF2 Lemma 9.3: m ≥ (D−1)/2 is
forced (class 0 mod D has H-mass (m − (D−1)/2)/D ≥ 0), so
(N − 2m)/(CN) ≈ 1/(2C), and σ ≤ 3/4 − 2h at C = 2. HL depends on N only
through D and E₀ = CN ≈ 2CD: the two edges of the window decouple
completely, and the right edge is the reflection of the left one.

**Lemma 1.4 (weak SPW suffices for Thm 5.2; PROVED implication).**
IF2 Thm 5.2 needs Flat with `t ≥ e^{−S_A}`, `Δ ≤ e^{S_A}`, `s₀ ≥ N^{−A₁}`
(its Remarks (i)–(ii)); Prop 9.1 gives t, s₀ ≍ σ and Δ = 6θ + Δ₀. Hence
SPW(C, σ_N, Δ_N) with `σ_N ≥ e^{−S_A}·c₀` and `Δ_N ≤ e^{S_A}/2` at every
large N already implies the 3/4 cap of Thm 5.2. Moreover it suffices to
find R′ ≥ 0 with (P1), with `R′(s) ≤ 1 − η` on every class of modulus
> CN **meeting [1,N]**, `R′(s) ≤ K` on every class of modulus > CN missing
[1,N], and |R′(s) − c(s)| ≤ Δ′ on medium classes: then
`R := (1 − 1/(2K))λ_N + R′/(2K)` satisfies SPW(C, η/(2K), Δ′/(2K)) (for
K ≥ 1): full classes get `1 − η/(2K)`, sparse ones `≤ 1/2`.
So η fixed and K quasi-polynomial (`K ≤ e^{S_A}/(2c₀)`) suffice.
*Proof.* Arithmetic from the statements quoted. ∎

So the hard part of SPW is only: *every class of modulus > CN through a
point of [1,N] must lose a fixed fraction of its mass*, with sparse classes
allowed quasi-polynomially large mass.

## 2. Bounded-density pseudo-windows (BDW): true for small N, false for large N

A natural strengthening of SPW: **BDW(A) at N** — a measure ρ ≥ 0 on ℤ/L₀
with the window profile mod every d ≤ D and *pointwise* density
`ρ ≤ A·N/L₀`.

**Lemma 2.1 (BDW ⇒ SPW; PROVED).** BDW(A) at N implies SPW(C, 1 − A/C − ε,
2A + 2) for every C > A. *Proof.* Lift ρ uniformly to ℤ/Q′ (Q′ as in
Lemma 1.1): ρ′(x) = ρ(x mod L₀)L₀/Q′ keeps (P1) and the density bound, so
every class mod e | Q′ has ρ′-mass ≤ AN/e (≤ A/C for e > CN, ≤ 2A for
e > D). Apply Lemma 1.1(b). ∎

**Lemma 2.2 (duality; PROVED).** BDW(A) at N holds iff for every g ∈ V_D
(the span of indicators of classes mod d ≤ D, as functions on ℤ/L₀)

    (1/N) Σ_{n=1}^{N} g(n) ≤ A · E_{x∈ℤ/L₀}[g(x)⁺].                       (2.1)

*Proof.* With y = ρL₀/N the primal asks for y ∈ [0,A]^{ℤ/L₀} with the
same V_D-projection as (L₀/N)λ_N. The set of projections of the box is
compact convex; separation by g ∈ V_D gives exactly the failure of (2.1)
(max of ⟨g,y⟩ over the box is A·Σg⁺). ∎
Taking g = indicator of one class gives `A ≥ A*(N) := max_{d≤D,b} c(b,d)d/N`
(= 3/2 − 3/N for even N ≥ 12, via d = N/2 − 1, c = 3).

**Numerics (EVIDENCE; `scripts/spw_bdw_lp.py`, HiGHS LP on ℤ/L₀).** The
optimum equals the trivial bound A*(N) exactly for every even N, 12 ≤ N ≤ 24
(A = 1.250, 1.286, 1.313, 1.333, 1.350, 1.364, 1.375), and the optimal y is
bang-bang: y ∈ {0, A} except at ≈ #constraints points, i.e. essentially a set
S ⊂ ℤ/L₀ of density 1/A on which a uniform element has exactly the window
law mod every d ≤ D. So at small N the window profile is as "un-rigid" as
possible.

**Proposition 2.3 (BDW fails for large N; PROVED).** Every BDW constant
satisfies `A(N) ≥ c·√N` for N ≥ N₀ (absolute c > 0, e.g. c = 0.05).
Rigorous values (`scripts/spw_bdw_l2bound.py`, exact integer arithmetic):
A(150) ≥ 1.55 > A*(150), A(200) ≥ 1.77, A(300) ≥ 2.20, A(400) ≥ 2.50.

*Proof.* Put E_d(b) = c(b,d) − N/d (so Σ_b E_d = 0) and
g := Σ_{2≤d≤D} d·E_d(x mod d) ∈ V_D. Then E g = 0, so
E g⁺ = E|g|/2 ≤ (E g²)^{1/2}/2.
*Window side.* Σ_{n≤N} E_d(n) d = d Σ_b c(b,d)E_d(b) = d Σ_b E_d(b)²
= r_d(d − r_d) with r_d = N mod d (E_d = 1 − r/d on r classes, −r/d on
the others). For d = D − k, 0 ≤ k < D/3, N = 2D or 2D+1 gives
r_d ≥ 2k, d − r_d ≥ D − 3k − 1, so (1/N)Σ_n g(n) ≥ (1/N)Σ_k 2k(D−3k−1)
= D³/(27N) − O(D²/N).
*L² side.* For d, d′ with g₀ = gcd(d,d′), E[d E_d | x mod g₀] = g₀E_{g₀}
(averaging c(·,d) over the d/g₀ lifts of a class mod g₀ gives c(·,g₀)·g₀/d),
and x mod d, x mod d′ are independent given x mod g₀ under the uniform
measure; hence E[dE_d · d′E_{d′}] = g₀² E[E_{g₀}²] = r_{g₀}(g₀ − r_{g₀}) ≤ g₀²/4.
Summing, E g² ≤ Σ_{g₀≤D} (g₀²/4)·#{(d,d′) : gcd = g₀} ≤ Σ_{g₀} (g₀²/4)(D/g₀)²
= D³/4. So A ≥ (D³/(27N) − O(D²/N)) / (D^{3/2}/4) ≍ √N. ∎

The Monte-Carlo ratio (1/N)Σg / E g⁺ (`spw_bdw_dualtest.py`, EVIDENCE) is
0.77, 0.93, 1.31, 1.47, 1.61, 1.95, 2.23 at N = 20, 32, 60, 80, 100, 150,
200 — the true A(N) exceeds 3/2 already near N ≈ 80.

*Consequence (Assessment).* SPW cannot be obtained from a pointwise-spread
pseudo-window: any SPW measure must have relative density ≳ √N somewhere
on ℤ/L₀. The dual of SPW (IF2 (9.1)) is not threatened by this g: its
negative part is "random-like", and covering a random-like function by
classes of modulus > CN costs ≍ e·max over a class, not e·mean. So SPW
needs constructions that are spread *on large classes* but not pointwise —
consistent with the LP optima, which are sparse.

## 3. Local (single-modulus) necessary conditions at large N

**Lemma 3.1 (local bound; PROVED).** Let e > CN. If R satisfies (P1)–(P2)
of SPW(C, σ, ·) at N, its projection ρ_e to ℤ/e satisfies: ρ_e ≥ 0, the
window profile mod every d | e with d ≤ D, and ρ_e(s) ≤ 1 − σ for every
class s mod e′ with e′ | e, e′ > CN (in particular pointwise). Hence
σ ≤ σ_loc(N, C, e) := the LP optimum of these conditions. IF2 Lemma 9.3 is
the sub-case using one divisor q = e/k. ∎

*Fourier form.* On ℤ/e the class sums mod d | e see exactly the characters
k with (e/d) | k. So the profile conditions fix ρ̂_e(k) = 1̂_W(k)
(W = {1..N} mod e) for all k with gcd(k, e) ≥ e/D, and leave free exactly
the characters with **gcd(k, e) < e/D** (≈ 4.2 when e ≈ 2.1N, C = 2). The
low frequencies |k| < e/D are always free; for e divisible by all primes
≤ P the remaining free characters are (small multiples of) P-rough k, a
set of density ≍ ∏_{p≤P}(1 − 1/p). So for primorial-like e the window is
pinned at all but a thin set of frequencies — a possible source of
rigidity as N → ∞ (Assessment; this is the mechanism to test).

**Numerics (EVIDENCE, `scripts/spw_local_lp.py`, `spw_local_scan.py`,
data/spw/local_scan_C2.txt; C = 2, e over 11-smooth numbers in (CN, 6000]).**
Worst local value: N = 100, 150, 200: 0.4000; N = 300: 0.3892 (e = 630,
1260, …); N = 400: 0.3961 (e = 840, …); N = 600: 0.3892 (e = 1260, …);
N = 800: 0.3961; N = 1000: 0.4000 (e ≤ 6000 only); N = 1430, e = 3003: 0.4286.
So composite e just above CN give local obstructions slightly *below*
σ_C(N) = 2/5 (first seen here; 0.3892 at N = 300), but no collapse up to
N = 1000 in this range of e.

**Exact certificates (PROVED; `scripts/spw_local_cert.py`).** The LP dual
is rounded to a rational g (combination of classes mod d | e, d ≤ D) and
rational patch weights z ≥ 0 on classes mod e′ | e, e′ > CN, with the point
patches recomputed so that Σ z_s 1_s ≥ g holds exactly on ℤ/e. For any
SPW measure R, Σ_{n≤N} g(n) = ⟨g,R⟩ ≤ Σ z_s R(s) ≤ (1−σ)Σ z_s. Results:

| N | C | e | certified bound on σ |
|---|---|---|---|
| 300 | 2 | 630 = 2·3²·5·7 | σ ≤ 72/185 = 0.38919 |
| 1150 | 2 | 2310 = 2·3·5·7·11 | σ ≤ 0.381132 (exact rational) |

So **SPW(2, σ) is false at N = 300 for σ > 72/185 < 2/5**: the optimum is
not σ_C(N) = 2/5 at all N (the R25 C10 pattern breaks beyond the tested
N ≤ 60). LP values (EVIDENCE) keep decreasing: 0.3849 (N = 3300,
e = 6930), 0.3737 (N = 4400, e = 9240) — data/spw/local_primorial.txt.

**Theorem 3.2 (fixed-σ SPW fails for large N; PROVED).** Let C > 1 (for C ≤ 1 SPW is impossible anyway, IF2 Lemma 9.3), let
M ≥ 2 with L_M := lcm(1..M) ≤ N, and let e be the least multiple of L_M
exceeding CN (so e ≤ CN + L_M, m₀ := e/D ≤ 2C + 3 for N ≥ N₀(C)). If R
satisfies (P1)–(P2) of SPW(C, σ, ·) at N, then

    σ ≤ 4·√(π m₀/(M+1)) · (1 + o(1))      (o(1) as M/… → ∞, uniformly).

Since one can take M ≍ log N (ψ(M) = log L_M ~ M), **σ ≲_C (log N)^{−1/2}**:
for every fixed C and σ > 0, SPW(C, σ, Δ₀) fails for all large N.

*Proof.* Project R to ρ on ℤ/e; then 0 ≤ ρ ≤ 1 − σ pointwise (points of ℤ/e
are classes mod e > CN) and ρ̂(k) = 1̂_W(k) whenever gcd(k, e) ≥ m₀
(Fourier form above; W = {1..N} ⊂ ℤ/e). Put f = ρ − 1_W. If
m₀ ≤ |k| ≤ M (integer representative) then |k| divides L_M | e, so
gcd(k, e) = |k| ≥ m₀ and f̂(k) = 0. Let K be the Fejér kernel of degree M
on ℤ/e, K(x) = (1/e)Σ_{|k|≤M}(1 − |k|/(M+1))e(kx/e) ≥ 0, ΣK = 1, and
K(x) ≤ e/(4(M+1)x²) for 1 ≤ |x| ≤ e/2 (sin(πx/e) ≥ 2|x|/e). Then
T := K∗f has Fourier support in {|k| < m₀}: it is the restriction to
ℤ/e of a real trigonometric polynomial T(θ) of degree n < m₀, T(x/e).
Also T = K∗ρ − φ with φ := K∗1_W ∈ [0,1] and 0 ≤ K∗ρ ≤ 1 − σ, so
|T| ≤ 1 on ℤ/e, and by sampling (Bernstein, nearest sample within 1/(2e))
‖T‖_{L^∞(𝕋)} ≤ 1/(1 − πm₀/e).
Edge: for 1 ≤ r < min(N−1, (C−1)N − 1)/2 take x_in = 1 + r ∈ W, x_out = −r ∉ W. The
tail bound gives Σ_{|t|≥a}K(t) ≤ e/(2(M+1)(a−1)), hence
1 − φ(x_in) ≤ e/(2(M+1)r) and φ(x_out) ≤ e/(2(M+1)r) (the far sides are at
distance ≥ N − r > r + 1 and ≥ e − N − r > (C−1)N − r > r + 1). So T(x_in) ≤ 1 − σ − φ(x_in)
≤ −σ + e/(2(M+1)r) and T(x_out) ≥ −φ(x_out) ≥ −e/(2(M+1)r), i.e.
T(x_out) − T(x_in) ≥ σ − e/((M+1)r). Bernstein:
|T(x_out) − T(x_in)| ≤ 2π m₀ ‖T‖_∞ (2r+1)/e. Therefore

    σ ≤ e/((M+1)r) + 2πm₀(2r+1)/(e(1 − πm₀/e)).

Take r = ⌈e/√(4πm₀(M+1))⌉ (which is o(N), hence admissible, once M is large): both terms
are √(4πm₀/(M+1))(1 + o(1)). ∎

*Remarks.* (i) The mechanism is the window's *jump*: once all
frequencies m₀ ≤ |k| ≤ M are pinned, a Fejér smoothing of ρ − 1_W at scale
e/M is a trig polynomial of bounded degree, which cannot jump by σ across
the edge of W. It is the edge problem of IF2 §5 in quantitative form.
(ii) The bound is useless numerically (it needs log N ≫ 50/σ²); the LP
values above show the actual decrease is slow but visible already at
N ≈ 10³–10⁴. The true rate of σ*(N) → 0 is open (between this
(log N)^{−1/2} upper bound and whatever constructions give).
(iii) **What survives.** By Lemma 1.4, Thm 5.2 (via Prop 9.1) only needs
SPW(C, σ_N, Δ_N) with σ_N ≥ c₀e^{−S_A}, S_A ≍ (log N)^{3/4}(log log N)^{3/4};
Theorem 3.2 only forces σ_N ≲ (log N)^{−1/2}, far above that threshold.
So the hybrid program is not refuted; the correct target is **weak SPW**
with slowly decaying σ_N, and the original fixed-σ SPW (in particular the
conjectured value 2/5) is false.

**Corollary 3.3 (Flat's margin also decays; PROVED).** If Flat(C, t, s₀, Δ)
(IF2 §5) holds at N, then s₀ ≤ 6√(πm₀/(M+1))(1 + o(1)) with M, e, m₀ as in
Theorem 3.2, for any t, Δ. *Proof.* Project F to F_e on ℤ/e. Since
F ≤ 1_{[1,N]} and F ≤ 0 off [1,N], F_e ≤ 1 on W and ≤ 0 off W; (F3)/(F4) at
modulus e give F_e ≥ M/e + s₀ on W and ≥ M/e − 1 off W. So
ρ := 1_W − F_e + M/e has the window profile mod d | e, d ≤ D, and
0 ≤ ρ ≤ 1 − s₀ on W, 0 ≤ ρ ≤ 1 off W. In the proof of Theorem 3.2,
K∗ρ(x_in) ≤ (1 − s₀)φ(x_in) + (1 − φ(x_in)), so T(x_in) ≤ −s₀ + 2ε with
ε = e/(2(M+1)r); the rest is unchanged (|T| ≤ 1 still). ∎
Thm 5.2 needs only s₀ ≥ N^{−A₁}, so this does not hurt it; it does show
that the decrease of the Flat margins in IF2 §5 (0.40 → 0.17 for
N = 20 → 100) is not only truncation: s₀ must tend to 0.

## 4. Status of the task and what is open

* SPW(2, 2/5 − ε, O(1)) for all large N — the target of O40 — is **false**
  (Thm 3.2; already σ ≤ 72/185 < 2/5 at N = 300). So is SPW(C, σ, Δ₀) for
  every fixed C and σ > 0, at all large N.
* The hybrid cap of IF2 Thm 5.2 via Prop 9.1 survives: it needs only
  **weak SPW**, i.e. SPW(C, σ_N, Δ_N) with σ_N ≥ c₀e^{−S_A},
  Δ_N ≤ e^{S_A} (Lemma 1.4), and Theorem 3.2 gives only σ_N ≲ (log N)^{−1/2}.
  Weak SPW is **open** (no construction for large N; LPs only at N ≤ 60,
  and §2 shows small-N LP evidence can be misleading).
* Useful reductions for weak SPW: periodic form (Lemma 1.1), two-edge split
  (Lemma 1.3: one half-line problem HL suffices), only full classes need
  mass < 1 (Lemma 1.4), and any construction must be pointwise
  non-spread (Prop 2.3) yet degrade the edge only at rate ≳ (log N)^{−1/2}.

## Replay

```
uv run --with scipy python scripts/spw_halfline_lp.py 10 40 -200 220 1        # HL at D=10: h=0.1889 (s)
uv run --with scipy python scripts/spw_bdw_lp.py 12 14 16 18 20 22 24          # BDW optimum = A*(N) (~1 min)
uv run --with scipy python scripts/spw_bdw_l2bound.py 150 200 300 400          # BDW fails: A >= 1.55..2.50 (exact; ~1 min)
uv run --with scipy python scripts/spw_bdw_dualtest.py d 20 32 60 100 200      # MC ratios (EVIDENCE)
uv run --with scipy python scripts/spw_local_cert.py 300 2 630                 # sigma <= 72/185 (exact)
uv run --with scipy python scripts/spw_local_cert.py 1150 2 2310               # sigma <= 0.381132 (exact)
uv run --with scipy python scripts/spw_local_scan.py 2 6000 100 150 200 300 400 600 800 1000   # local scan (~1 h)
```
