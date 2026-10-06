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
