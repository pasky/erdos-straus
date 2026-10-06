# POINTWISE_MN3 — hypothesis SI for the class-of-one prefix (task O82, branch `side-agent/sierpinski-si`)

Status: work in progress. Labels as in DISCOVERIES.md. Notation as in POINTWISE_MN.md (MN),
POINTWISE_MN2.md (MN2), POINTWISE_OMEGA12.md (O12). Fixed `m ≥ 4`, `m ≢ 0 (4)` (main case m = 5);
constants may depend on m. Atoms `(M,D)`: `M ≡ −1 (m)`, `A = (M+1)/m`, `D | A²`, event `n ≡ −mD (M)`.

## 0. Target

Prefix law `ν = δ_1`: `r_0 ≡ 1 (mod Q_0)`, `Q_0 = Q(q_0)` (times 8 for `m ≡ 2 (4)`, MN2 §1 note;
no atom involves 2 then). For `q = ℓ^{a+1} ∈ 𝒫`, `q > q_0`, the completed atoms are
`C_q = {(M,D): M = qM_1, M_1 | L(q)}` (MN2 Lemma 1.2); `E^-` is the restriction of E to
`M^- := M_1ℓ^a`. SI (MN2 Prop 5.1, precise form of R74 D9) asks that, as `q_0 → ∞`,

```
Σ_{ℓ>q_0} E^ν_2(ℓ)/(θ(ℓ−1))² + Σ_{(b)} E^ν_1(q)/(θℓ) + Σ_{(c)} E^ν_1(q) → 0,
E^ν_1(q) = Σ_{E∈C_q} K^{ω(M^-)} E_ν[p_0(E^-)],   E^ν_2(ℓ) = Σ_{E,E'∈C_ℓ} K^{ω(M_1)+ω(M_1')} E_ν[Π_0(E^-,E'^-)].
```

(b): `q = ℓ^{a+1}`, `a ∈ {a_ℓ, a_ℓ+1}`, `a ≥ 1`; (c): `a ≥ a_ℓ+2`; `ℓ^{a_ℓ} ‖ Q_0`.

Throughout, for an atom put `P := mD+1`, `g := gcd(M, P)`, `N := M/g`. For `D ≤ A`, O12 Lemma 2.1
(with `4 ↦ m`, MN Cor 6.1 (0)) writes `D = da²`, `A = dab` (d squarefree, `b ≥ a`), `P = ma²d+1`,
`e := g`, `f := P/e`, `c := (a+b)/e`, and then `N = madc − f ≥ acd`, `M = eN`; the map atom ↦ `(a,c,d,f)`
is injective, and `D ↦ A²/D` preserves M and g.

## 1. Reduction: the ν-weights are dominated by class-of-one weights `1/φ(N)`

**Lemma 1.1 (PROVED).** Let `E = (M,D) ∈ C_q`, `q = ℓ^{a+1} > q_0`, and `s := gcd(M^-, Q_0)`. Then
`s = gcd(M, Q_0)`, `E_ν[p_0(E^-)] = 1[s | P]·φ(s)/φ(M^-)`, and

```
E_ν[p_0(E^-)] ≤ ℓ·1[s | g]/φ(M/s) ≤ ℓ/φ(N).
```

*Proof.* `v_ℓ(Q_0) = a_ℓ ≤ a` (as `ℓ^{a_ℓ} ≤ q_0 < ℓ^{a+1}`), so `gcd(M^-,Q_0) = gcd(M,Q_0)`. Under ν,
`n ≡ 1 (Q_0)`; the Haar probability of `n ≡ −mD (M^-)` given this is `1[−mD ≡ 1 (s)]·φ(s)/φ(M^-)`
(`φ(lcm)φ(gcd) = φ(M^-)φ(Q_0)`). `−mD ≡ 1 (s)` iff `s | P`; with `s | M` this is `s | g`.
`φ(M) = φ(M^-)·ℓ` (a ≥ 1) or `·(ℓ−1)` (a = 0), so `1/φ(M^-) ≤ ℓ/φ(M)`. Always `φ(xy) ≥ φ(x)φ(y)`, so
`φ(M) ≥ φ(s)φ(M/s)`, and `M/s = N·(g/s)` gives `φ(M/s) ≥ φ(N)`. ∎

So with the **class-of-one completed sum**

```
U_1(q) := Σ_{(M,D)∈C_q, D≤A} K^{ω(M)}/φ(N)        (M = eN in O12's parametrisation)
```

one has `E^ν_1(q) ≤ 2ℓ·U_1(q)` (factor 2: the involution preserves M, g, N).

## 2. The multiplicity `R(N)` and the size of `U_1(q)`

**Lemma 2.1 (N-parametrisation; PROVED).** For an atom with `D ≤ A` in O12's coordinates
`(a,c,d,f)`: `b = (aN+c)/f`, `cM = N(a+b)`, `f | aN + c`, `f | N² + mc²d`, `1 ≤ f ≤ (m−1)N`,
`acd ≤ N`. Hence for each `N ≥ 1`

```
R(N) := #{atoms (M,D), D ≤ A : M/gcd(M, mD+1) = N}
     ≤ #{(a,c,d) : acd ≤ N, f := macd − N ≥ 1, f | ma²d + 1}  <  ∞ .
```

*Proof.* `fb = f(ce−a) = cP − af = c(ma²d+1) − af = a(madc − f) + c = aN + c`. `M = eN`, `a+b = ce`
give `cM = N(a+b)`. `f | P` and `f | fb` give `f | aN+c`; with `u := mcd`, `ua = f + N`, so
`u(aN+c) = N(f+N) + uc ≡ N² + mc²d (mod f)`, and `f | u(aN+c)` gives `f | N²+mc²d`. `N ≥ acd` is O12
Lemma 2.1, so `f = madc − N ≤ (m−1)N`. Given `(N,a,c,d)`, `f` and then `e = P/f`, `b`, `M` are determined. ∎

So the class-of-one mass is `Σ_atoms g/M = Σ_N R(N)/N`, and `U_1(q) ≤ Σ_{N} K^{ω(N)}φ(N)^{−1}
Σ_{tuples↦N, eN∈𝓜_q} K^{ω(e)}` (`𝓜_q := {qM_1 : M_1 | L(q)}`).

**EVIDENCE (m = 5; `scripts/mn3_u1.py 5 1000000 1`, `scripts/mn3_rn.py`).**
* `q·U_1(q)` (K = 1, truncated at `M ≤ 10⁶`) for `q = 11, 23, 47, 97`: `11.3, 35.3, 61.0, 85.4`, versus
  `(log q)³ = 13.8, 30.1, 57.2, 95.6`: consistent with `U_1(q) ≍ (log q)³/q` (the Haar analogue is
  `S_1(q)/q`). 70–95% of the mass of `U_1(q)` (q prime) has `q | N`, and 75–90% has `N < q²`.
* `R(N)`: `Σ_{N≤10³}R(N) = 11158`, `Σ_{N≤10³}R(N)/N = 34.2`; `max_{N≤Y}R(N) = 127, 287, 406, 534` for
  `Y = 10³, 5·10³, 10⁴, 2·10⁴` (attained at `N ≡ −1 (mod 30)`). `R(N)` is not bounded by `τ(N)τ(N+1)`:
  `R(9973) = 154` (N prime). Its main families are `f` small: e.g. `f = 2` gives every factorisation
  `acd = (N+2)/m` with a, d odd. So `R(N) ≈ Σ_{f} #{acd = (N+f)/m : f | ma²d+1}` — a sum of divisor
  functions of the shifts `N + f`.

## 3. What SI needs: three admissible levels and `U_1(q) ≪ q^{−1/2−δ}`

Modify MN2 Thm 3.1 to allow `L` levels: a step at `(ℓ,a)` is *bad* if `a ∈ [a_ℓ, a_ℓ+L−1]` and `Y > θN`,
or `a ≥ a_ℓ+L` and `Y ≥ 1`. No bad step ⇒ `Λ(ℓ) ≤ K := (1−θ)^{−L}` (same proof as MN2 Thm 3.1; K is
still a constant, which is all MN Thm 5.1 needs).

**Lemma 3.1 (PROVED, given MN2 Thm 3.1's first/second-moment set-up and Lemma 1.1).** For `ν = δ_1`
and `L = 3`, SI follows from

* (R_a) `Σ_{ℓ>q_0} E^ν_2(ℓ)/(ℓ−1)² → 0` (level 0, Chebyshev);
* (R_b) `U_1(q) ≪ q^{−1/2−δ}` for proper prime powers `q ∈ 𝒫` (some fixed `δ > 0`).

*Proof.* (b) steps have `a ≥ 1`, `N ∈ {2, ℓ}` fibre lifts, and `E[Y1_alive] ≤ E^ν_1(q) ≤ 2ℓU_1(q)`
(Lemma 1.1), so `P(bad) ≤ 4U_1(q)/θ`; every (b) step has a proper prime power `q > q_0`, distinct
for distinct steps, and `Σ_{q proper pp > q_0} q^{−1/2−δ} ≪ Σ_{ℓ} min(ℓ^{−1−2δ}, ·) → 0`
(`#{proper pp in (x,2x]} ≪ x^{1/2}`). (c) steps: `P(Y ≥ 1) ≤ 2ℓU_1(q)`. If `ℓ > q_0` then
`q = ℓ^k`, `k ≥ L+1 = 4`, and `Σ_ℓ Σ_{k≥4} ℓ^{1−k/2−kδ} ≪ Σ_{ℓ>q_0} ℓ^{−1−4δ} → 0`. If `ℓ ≤ q_0` then
`q ≥ ℓ^{a_ℓ+L+1} > q_0ℓ^{3}`, so `ℓq^{−1/2−δ} ≤ q_0^{−1/2}ℓ^{−1/2}` and the geometric sum over k and the
sum over `ℓ ≤ q_0` give `≪ q_0^{−1/2}·q_0^{1/2}/log q_0 → 0`. (a) is (R_a). ∎

So the target is a **square-root saving** for the q-divisibility in the class-of-one completed sums
(the Haar analogue MN2 Lemma 2.1 has the full saving `q^{−1+ε}`), plus the level-0 pair sums.

## 4. Regime map for `U_1(q)`: linear routes and the residual (analysis; Assessment where marked)

Write `a ~ A`, `c ~ C`, `d ~ D`, `e ~ E`, `f ~ F` (dyadic), so `EF ≍ mA²D` (`ef = P`), `B ≍ CE`
(`b = ce − a ≥ a`), `N ≍ mACD` (`A CD ≤ N ≤ mACD`), `M = eN`. Since `b ≥ a`, `E ≳ A/C`.
The multiplicative weights to be averaged are `h(e)h(N)` with `h(n) = K^{ω(n)}(n/φ(n))·v_q(n)·n^σ`
(Rankin, `σ ≍ 1/log q`; `v_q(n) = 1[all p^ν ‖ n have p^ν ≤ q]`), and `q | eN`. Each of the following
*routes* fixes three variables and sums the fourth along an arithmetic progression on which `N` (and
`e`, where it moves) are polynomials; Henriot's (H) then applies (coefficient-uniform, discriminant
bounded by the fixed variables) as soon as the progression is longer than `‖Q‖^δ`, and the
condition `q | N` is a further progression (the gain `q^{−1}` is automatic once the length exceeds the
modulus by `‖Q‖^δ`):

| route | fixed | summed | progression modulus | long iff (up to `(·)^δ`) |
|---|---|---|---|---|
| c-route | a, d, f | c (`N = madc − f`) | `q` | `C ≥ q` |
| N-route | a, c, f | d (`f | aN + c`, `N ≡ −f (mac)`) | `f·q` | `D ≥ F q` |
| d-route | a, b, e | d (`e | mabd − 1`) | `e·q` | `D ≥ E q` |
| a-route | c, d, f | a (`f | ma²d+1`, quadratic) | `f·q` | `A ≥ F q` |

(The (a,d)-sums with `q | e` are the O12 Lemma 4.1 situation: `q | P`, ET/(H) in the larger of a, d.)

**Residual.** All four routes are short iff `C ≲ q`, `D ≲ min(E,F)·q`, `A ≲ Fq` (up to `(·)^δ`).
With `EF ≍ A²D` this is a genuine open region: e.g. `(A, D, E, F) = (X, X², X², X²)`, `C = 1`
(`P ≍ X⁴`, `b ≍ X²`, `N ≍ X³`, `M ≍ X⁵`) for every `X ≥ q^{O(1)}`. In it `g = e ≍ a+b` (`c` small):
the atom's class-of-one gcd is almost all of `a+b`. In the `(a,e,f)` coordinates `d = (ef−1)/(ma²)`, i.e.
the residual is the set of points of the hyperbola `ef ≡ 1 (mod ma²)` in boxes `E × F` with both sides
shorter than the modulus `ma²q` — the Kloosterman range. Counting such points (Weil) works when
`EF ≥ (A²q)^{3/2+δ}`, but not with the multiplicative weight `h(N)`, `N = (f(ce−a) − c)/a`.
**Assessment:** no combination of (H), ET and elementary counting known to us controls `h(N)` on the
residual; at the level of raw counts the residual is not sparse (each residual box carries mass `≍ 1`
before the q-condition), so it cannot be discarded either.

**Lemma 4.1 (prefix part; PROVED).** With `s = gcd(M,Q_0)` as in Lemma 1.1, `s = gcd(g, Q_0)`, and the
exact weight satisfies `φ(s)/φ(M^-) ≤ ℓ/(φ(N)φ(g/s))`. In particular, on atoms with `g ≥ Q_0·G`,
the class-of-one weight carries an extra factor `≤ 1/φ(G)`.

*Proof.* `s | g` (Lemma 1.1) and `gcd(g,Q_0) | gcd(M,Q_0) = s`. `M/s = N·(g/s)` and `φ(xy) ≥ φ(x)φ(y)`. ∎

*Consequence (Assessment, to be made precise).* On the residual `g ≍ B`; if `B ≥ Q_0²·q^{1+3δ}` the
factor `1/φ(g/s) ≤ B^{−1/2+o(1)}` is a power saving that beats the pointwise bound `h ≪ M^{ε}`
(all residual variables are `≤ B^{O(1)}`). So the residual is only dangerous at scales
`B ≤ (Q_0 q)^{O(1)}`: for `q ≥ Q_0` this is a **polynomially bounded box** (pointwise bounds for h,
q-gain needed from counting alone), and for `q_0 < q < Q_0 = e^{(1+o(1))q_0}` it is the range where the
prefix part s itself can be huge.
