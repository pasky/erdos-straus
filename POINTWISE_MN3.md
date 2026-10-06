# POINTWISE_MN3 — hypothesis SI for the class-of-one prefix (task O82, branch `side-agent/sierpinski-si`)

Status: CLOSED as an obstruction/localisation write-up (parent decision (c), O82). SI is **not**
proved. Labels as in DISCOVERIES.md. Notation as in POINTWISE_MN.md (MN),
POINTWISE_MN2.md (MN2), POINTWISE_OMEGA12.md (O12). Fixed `m ≥ 4`, `m ≢ 0 (4)` (main case m = 5);
constants may depend on m. Atoms `(M,D)`: `M ≡ −1 (m)`, `A = (M+1)/m`, `D | A²`, event `n ≡ −mD (M)`.

## 0. Summary

Prefix law `ν = δ_1` (class of one mod `Q_0 = Q(q_0)`), hypothesis SI of MN2 Prop 5.1. Result: SI is
not proved; its main term is localised at an Erdős–Straus-type multiplicity `R(N)` (Lemma 5.1), and
a route (M2) ⇒ SI exists only as a SKETCH with five missing pieces (§5.4).

| item | statement | label |
|---|---|---|
| Lemma 1.1 | `E_ν[p_0(E^-)] ≤ ℓ/φ(N)`, `N = M/gcd(M,mD+1)`; so `E^ν_1(q) ≤ 2ℓU_1(q)` | PROVED |
| Lemma 2.1 | N-parametrisation (`f | aN+c`, `cM = N(a+b)`, `acd ≤ N`); `R(N) < ∞` | PROVED |
| Lemma 3.1 | with three admissible levels, SI(δ_1) ⟸ (R_a) + `U_1(q) ≪ q^{−1/2−δ}` (proper prime powers) | PROVED (given MN2 Thm 3.1's set-up) |
| §4 route table | four linear routes (sum over c, d via N, d via e, a), each expected closable by (H) when long | Assessment (proofs not written) |
| Lemma 4.1 | `s = gcd(g,Q_0)`; exact weight `≤ ℓ/(φ(N)φ(g/s))` | PROVED |
| residual (§4) | region where all four routes are short (Kloosterman range of `ef ≡ 1 mod ma²`) | description: Assessment; mass share 72–91% of `U_1(q)`, `q ≤ 199`: EVIDENCE |
| Lemma 5.1 | `U_1(ℓ) ≥ R_ℓ(ℓ)/(ℓ−1)`; on the all-ones path the level-0 count is `Y(ℓ) ≤ 2R_ℓ(ℓ)` | PROVED |
| Lemma 5.2 | `R(N) ≪_ε N^{2/3+ε}` | PROVED |
| Conjecture 5.3 (M2) | `Σ_{N≤X} R(N)² ≪_ε X^{1+ε}` | CONJECTURE (EVIDENCE to `3·10⁴`) |
| §5.4 | (M2) + (H) ⇒ SI(δ_1) | SKETCH only (five missing pieces listed) |
| SI for `ν = δ_1`; ADM_m; `W_5` exponent 1/4 | — | OPEN / OPEN / CONDITIONAL on SI |

## 0′. Target and notation

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

**EVIDENCE for the residual (`scripts/mn3_resid.py 5 3000000`).** Share of `U_1(q)` (K = 1, atoms with
`M ≤ 3·10⁶`) lying in the residual (`c < q`, `d < fq`, `d < eq`, `a < fq`; exponents δ = 0): 0.91, 0.82,
0.80, 0.81, 0.78, 0.73, 0.74, 0.72, 0.72, 0.79, 0.74 for `q = 11, 13, 17, 23, 29, 31, 47, 53, 97, 101, 199`.
So the residual is not a corner: at accessible scales it **is** `U_1(q)`. Its mass sits mostly on
`N = q·N''` with `N''` small (atoms whose class-of-one gcd g is all of M except the new digit and a few
small primes).

## 5. The exact missing input (where SI fails for the available tools)

**Lemma 5.1 (the dominant term is a pointwise multiplicity; PROVED).** For a prime `ℓ > q_0`,
`U_1(ℓ) ≥ R_ℓ(ℓ)/(ℓ−1)`, where `R_ℓ(N) := #{atoms in C_ℓ, D ≤ A : M/gcd(M,mD+1) = N}`. Moreover, if the
earlier stage-A digits all equal those of 1 (an admissible path: the class 1 is never forbidden,
TRANSFER Lemma 5.1(ii)), the number of consistent completed atoms at the level-0 step ℓ is exactly
`Y(ℓ) = #{(M,D) : M = ℓM_1, M_1 | L(ℓ), M_1 | mD+1} = #{atoms in C_ℓ (all D) with N = ℓ} ≤ 2R_ℓ(ℓ)`
— the deterministic count of `scripts/mn3_first.py`.

*Proof.* Atoms with `N = ℓ` have weight `K^{ω}/φ(ℓ) ≥ 1/(ℓ−1)`. Consistency with r ≡ 1 on all revealed
digits means `M_1 | mD+1` (`M_1 = M/ℓ` is fully revealed at a level-0 step); then `M_1 | g`, so
`N ∈ {1, ℓ}`, and `N = 1` (`M | mD+1`) is impossible by TRANSFER Lemma 5.1(ii). The involution
`D ↦ A²/D` preserves N, giving the factor 2. ∎

**Lemma 5.2 (a weak pointwise bound; PROVED).** `R(N) ≪_ε N^{2/3+ε}`.

*Proof.* Lemma 2.1: `acd ≤ N`, so one of `ac, ad, cd` is `≤ N^{2/3}`. Given `(c,d)`, `u = mcd` and
`(ua − N) | N² + mc²d` leave `≤ τ(N²+mc²d)` values of a; given `(a,c)`, `f | aN + c` leaves `≤ τ(aN+c)`
values of f and then `d = (N+f)/(mac)`; given `(a,d)`, `f | P` leaves `≤ τ(P)` values and then
`c = (N+f)/(mad)`. All arguments are `≤ N^{O(1)}`; the divisor bound and `#{xy ≤ N^{2/3}} ≪ N^{2/3}log N`
finish. ∎

(`scripts/mn3_first.py 5 q0 4`: along the all-ones path the level-0 forbidden fractions at
`ℓ = 11, 13, 17, 19, 23, 29, 31` are `0.20–0.46`; they are not small at accessible ℓ, consistent with
`Y(ℓ) ≍ (log ℓ)³`.)

So SI for `ν = δ_1` contains, as its main term, averages over primes ℓ of
`(1/ℓ)Σ_{N''} R_ℓ(ℓN'')/N''`, where `R(N) ≤ #{(f,δ) : f ≤ N+1, δ | (N+f)², δ ≡ −1 (mod f), m | δ}`
(from `(ef−1) | (N+f)²`, Lemma 2.1 and `D | A²`) is an Erdős–Straus-type representation count
(it is a Type II solution count of the shape `μyz − y − z = K` after the substitutions of §2).
What a proof of SI at level 0 needs is, roughly, **one** of:

* (P) a pointwise bound `R(N) ≪ N^{θ}` with `θ < 1/K_0`, where `N ≤ ℓ^{K_0}` is the residual scale
  (`K_0 ≈ 10` from §4 and Lemma 4.1). The best pointwise bounds of this type known for ES counts are
  `n^{3/5+o(1)}` (Elsholtz–Tao, `sources/elsholtz-tao-1107.1010.pdf`, via "one of e, f, cd, ac is
  `O(n^{3/5})`"); the same device gives only Lemma 5.2's `N^{2/3+o(1)}` here. Far from `1/K_0`.
* (AP) equidistribution of `R(N)` over `N ≡ 0 (mod ℓ)`, `N ≤ X`, with saving `ℓ^{−δ}` relative to
  `X/ℓ`, for `ℓ` up to `X^{1−δ}` — a level of distribution beyond what is known even for `τ_3`.
* (M2) via Cauchy–Schwarz over `ℓ ~ L` (only averages over ℓ enter SI, Lemma 3.1): a
  congruence-free second moment of R, Conjecture 5.3 below.

**Conjecture 5.3 (M2; CONJECTURE).** Fix `m ≥ 4`, `m ≢ 0 (4)`, and let
`R(N) := #{atoms (M,D) with D ≤ A and M/gcd(M, mD+1) = N}`. Then for every `ε > 0`
`Σ_{N≤X} R(N)² ≪_{m,ε} X^{1+ε}` (strong form: `≪_m X(log X)^{C}` for some C).
*Data (m = 5, `scripts/mn3_rn.py 5 30000 moments`, exact counts):*

| Y | 10³ | 3·10³ | 10⁴ | 3·10⁴ |
|---|---|---|---|---|
| `Σ_{N≤Y}R(N)/Y` | 11.2 | 16.3 | 23.5 | 31.7 |
| `Σ_{N≤Y}R(N)²/Y` | 367 | 803 | 1679 | 3082 |
| `Σ_{N≤Y}R(N)²/(Y log⁶Y)` | 0.0034 | 0.0030 | 0.0028 | 0.0026 |
| mean / max of `R(ℓ)`, primes `ℓ ∈ (Y/2,Y]` | 35 / 111 | 57 / 223 | 78 / 386 | 106 / 663 |

The normalised second moment is slowly decreasing, so `X(log X)⁶` is an upper envelope over this
range; the data do not determine the log-power. Only the weak form with `ε < 1/K_0` would be used in
§5.4. Proving (M2) is a count of pairs of O12 tuples with equal N (6 free variables), whose
"first-term" regime is again of Kloosterman type.

### 5.4 (M2) ⇒ SI: SKETCH (not a proof)

Idea. Split `U_1(ℓ) = U^N(ℓ) + U^e(ℓ)` according to `ℓ | N` or `ℓ | e = g`. In the small box
(`M ≤ (Q_0ℓ)^{K_0}`) bound the multiplicative weights pointwise by `(Q_0ℓ)^{O(ε)}`; then
`U^N(ℓ) ≲ ℓ^{−1}Σ_{N''} R(ℓN'')/N''`, Cauchy–Schwarz in `N''` and summation over `ℓ ~ L` give
`Σ_{ℓ~L} U^N(ℓ)² ≲ (log X)² L^{−1} Σ_{N≤X} R(N)²/N`, which is `≪ L^{−δ}` under (M2) with `ε < 1/K_0`;
this is the off-diagonal part of (R_a). For (R_b) (`q = ℓ^k`, `k ≥ 2`) the same with
`ω_{L,k}(N) = #{ℓ ~ L : ℓ^k | N}` gives `Σ_{ℓ~L} U^N(ℓ^k) ≲ L^{−1/2}(Σ R²/N)^{1/2}`.

**Missing pieces** (each needed for a proof):
1. **Correlation terms of `E^ν_2`**: pairs `E ≠ E'` in `C_ℓ` whose `M_1, M_1'` share post-prefix
   prime powers (factor `G/gcd(G,Q_0)`, `G = gcd(M_1,M_1')`); only the uncorrelated part is
   covered by the sketch.
2. **The large-scale regime**: residual boxes with `B ≥ (Q_0q)^{O(1)}` (Lemma 4.1's power saving
   against pointwise weights is only an Assessment), and the whole range `q_0 < q < Q_0 = e^{(1+o(1))q_0}`,
   where the prefix part s can be huge and the pointwise loss `(Q_0ℓ)^{O(ε)} = e^{O(εq_0)}` is not
   absorbed (this also affects the small-box step above).
3. **The long-route proofs**: the four (H)-applications of the §4 table with explicit coefficients,
   discriminants, Rankin weights and the q-progression, including the short-range cut-offs.
4. **The `ℓ | e` part `U^e`** (`q | P`, O12 Lemma 4.1 type, with the multiplicative weights) and the
   mixed splits `ℓ^i ‖ e`, `ℓ^j ‖ N`.
5. **The diagonal / first-moment totals** `Σ_{ℓ~L} U_1(ℓ^k) ≪ L^{o(1)}` uniformly in the scale
   (Rankin-weighted class-of-one masses; the residual again blocks a direct proof at large scales).

**Assessment.** All the difficulty found is concentrated in the class-of-one multiplicity `R(N)` at
`N` a small multiple of the new prime (Lemma 5.1, EVIDENCE §4). Its pointwise version is open (ET's
`3/5` for the analogous ES counts; Lemma 5.2's `2/3` here), and the averaged versions (AP to moduli
`≈ X^{1−δ}`, or (M2)) are not available from (H), ET Prop 1.4/Thm 7.1, Weil, or elementary counting.

## 6. Status

See the table in §0.

## Replay

```
cd scripts
(ulimit -v 8000000; timeout 900 uv run python mn3_u1.py 5 1000000 1)       # §2 U_1(q), ~5 s
(ulimit -v 8000000; timeout 900 uv run python mn3_rn.py 5 3000)            # §2 R(N) maxima, <1 s
(ulimit -v 8000000; timeout 900 uv run python mn3_rn.py 5 30000 moments)   # §5 (M2) data, ~10 s
(ulimit -v 8000000; timeout 1500 uv run python mn3_resid.py 5 3000000)     # §4 residual share, ~1 min
for q0 in 8 12 18 24; do (ulimit -v 8000000; timeout 600 uv run python mn3_first.py 5 $q0 4); done  # §5
```
