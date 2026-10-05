# EXCEPTIONAL_SPW — towards SPW (task O40)

Status: **work in progress (O40).** Labels as in `DISCOVERIES.md`. PROVED =
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
| §2 | obstructions to simple constructions: rigidity below support length deg Ψ_D ≈ 0.3D²; one-interval-per-sample impossible; block re-randomisation cannot spread moduli built from prime powers ≤ √D | PROVED |
| §3 | HL numerics | EVIDENCE |

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
