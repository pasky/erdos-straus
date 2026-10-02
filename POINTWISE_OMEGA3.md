# Beyond exponent 3? The pair-codegree gap G_pair

Task O4. Labels follow the house rules. ES is not solved here or anywhere;
nothing below bears on whether `W(p)<∞`. Notation as in `POINTWISE_OMEGA.md`
(PO) and `POINTWISE_OMEGA2.md` (O2): `W`, atoms `(M,D)`, `A_M=(M+1)/4`,
survival, Settings 1.0/3.0/10.0, `Δ_O`, Lemmas 1.2, 10.1, 10.2, Theorem 10.3,
Lemma 11.2, Prop 11.4, §11.4 (G_pair).

**Status: work in progress (checkpoint 0).**

## 0. Plan and the two observations

G_pair (O2 §11.4) is a *circularity*: the support-truncation level L of
O2 Thm 10.3 is `≍` the total event mass Σ, the pair codegrees must be
`≲1/L`, and quarantining the `−4D` hubs as ordinary singles raises Σ by
more than L. Two observations break it.

1. **Decoupling (§1).** Prime-local forbidden classes need not be events of
   the truncated minorant. They can be imposed on the base measure by a
   separate Brun pure sieve, composed with the main minorant coefficient by
   coefficient. Their mass then costs only `O(S_hub)` in `log(M_1/μ)` and
   `O(S_hub)` extra primes per modulus. It does **not** enter the main
   truncation level. This is option (i) of G_pair.
2. **The hub classes are the small-height rationals (§2).** Every atom is a
   triple `(s,a,b)` with `4sab=M+1` and class `−a/b ≡ −4sa² ≡ −1/(4sb²)`
   mod M. Fixing two of `s,a,b` and letting the third run gives a class that
   is the same rational `−u/v` at every M of a progression mod `4uv`-ish.
   There are three such families (Prop 10.6's `−4d²` is one of them).
   Numerically, the heavy pairs are exactly classes `≡−u/v` with small `uv`.

What remains is an upper bound (Lemma B, §3) for pair codegrees of classes
that are *not* small-height rationals.

## 1. Decoupling prime-local quarantines from the truncation level (PROVED)

**Setting 1.0.** As O2 Setting 3.0: `2|Q`, a finite set 𝒫 of primes coprime
to Q, exponents `e_ℓ`, coordinates `X_ℓ=n mod ℓ^{e_ℓ}`, Haar measure P
(uniform on `∏_ℓ(ℤ/ℓ^{e_ℓ})^×`). A *cell* is a pair `(P_i,x_i)` with
`P_i⊆𝒫` and `x_i∈∏_{ℓ∈P_i}(ℤ/ℓ^{e_ℓ})^×`; its indicator is
`1[X_ℓ=x_{i,ℓ} ∀ℓ∈P_i]`, a unit class modulo `d_i=∏_{ℓ∈P_i}ℓ^{e_ℓ}`.

* *Hub sets.* `H_ℓ⊆(ℤ/ℓ^{e_ℓ})^×` with `h_ℓ:=|H_ℓ|/φ(ℓ^{e_ℓ})≤1/2`;
  `S_hub:=Σ_ℓ h_ℓ`, `V:=∏_ℓ(1−h_ℓ)`, `𝒜_1:={n : X_ℓ∉H_ℓ ∀ℓ}`.
* *Conditioned measure.* `P'` = the product of the uniform measures on
  `(ℤ/ℓ^{e_ℓ})^×∖H_ℓ`; `E'` its expectation.
* *Main minorant.* `B_2=Σ_i c_i 1_{cell_i}` (real `c_i`) with
  `B_2(n)≤1_{𝒜_2}(n)` for every integer n, for some set `𝒜_2`. Put
  `μ':=E'B_2` and `M_1':=Σ_i|c_i|P'(cell_i)`.

**Theorem 1.1 (decoupling; PROVED).** Let `J≥S_hub` be odd and put
`ε_J:=S_hub^{J+1}/(J+1)!`. There is a
combination of cells B with:

1. `B(n) ≤ 1_{𝒜_1∩𝒜_2}(n)` for every integer n;
2. `μ(B) := E B ≥ V μ' − ε_J M_1'`;
3. `M_1(B) ≤ e^{S_hub} M_1'`;
4. every cell of B is a cell of `B_2` refined by at most J further primes
   of 𝒫: its modulus is `d_i∏_{ℓ∈R}ℓ^{e_ℓ}`, `|R|≤J+1`, `R∩P_i=∅`;
5. for every character `ψ=∏_{ℓ|f}χ_ℓ(X_ℓ)` (f squarefree, primes in 𝒫,
   `χ_ℓ` nontrivial mod ℓ), `|E[Bψ] − V·E'[B_2ψ]| ≤ ε_J M_1'`.

*Proof.* Put `s_ℓ:=1[X_ℓ∈H_ℓ]`.

* **Pruning.** Delete from `B_2` every cell with `x_{i,ℓ}∈H_ℓ` for some
  `ℓ∈P_i`; call the result `B_2'`. Deleted cells vanish on `𝒜_1`, so
  `1_{𝒜_1}B_2'=1_{𝒜_1}B_2≤1_{𝒜_1∩𝒜_2}`. Deleted cells have `P'`-measure
  0, so `μ'` and `M_1'` are unchanged.
* **Brun on the complement.** For a surviving cell i put
  `β_i:=Σ_{j=0}^{J}(−1)^j e_j(s|_{𝒫∖P_i})` and
  `α_i:=Σ_{j=0}^{J+1}(−1)^j e_j(s|_{𝒫∖P_i})` (`e_j` = elementary symmetric
  function). By the Bonferroni inequalities (J odd, J+1 even), `β_i ≤ ∏_{ℓ∉P_i}(1−s_ℓ) ≤ α_i` pointwise. On
  cell i, `1_{𝒜_1}=∏_{ℓ∉P_i}(1−s_ℓ)`. Define
  `B := Σ_{c_i>0} c_iβ_i1_{cell_i} − Σ_{c_i<0}|c_i|α_i1_{cell_i}`.
  Then `B ≤ Σ_i c_i 1_{𝒜_1}1_{cell_i} = 1_{𝒜_1}B_2'`, which gives 1.
* **Means.** `β_i, α_i` depend only on coordinates outside `P_i`, so
  `E[β_i1_{cell_i}]=P(cell_i)Eβ_i`, and likewise for `α_i`. Put
  `V_i:=∏_{ℓ∉P_i}(1−h_ℓ)` and `h^{(i)}:=h|_{𝒫∖P_i}`. The Bonferroni
  inequalities in expectation (independent coordinates) give
  `0≤V_i−Eβ_i≤e_{J+1}(h^{(i)})` and `0≤Eα_i−V_i≤e_{J+2}(h^{(i)})`. Both
  are `≤ε_J`, because `e_{j+1}≤e_j·S_hub/(j+1)` and `J+2>S_hub`. Next,
  `P(cell_i)V_i=V·P'(cell_i)`: both sides equal
  `∏_{ℓ∈P_i}φ(ℓ^{e_ℓ})^{−1}·∏_{ℓ∉P_i}(1−h_ℓ)`. Also
  `P(cell_i)≤P'(cell_i)`. Hence

  ```
  E B ≥ Σ_i c_iP(cell_i)V_i − ε_JΣ_i|c_i|P(cell_i) ≥ Vμ' − ε_J M_1'.
  ```
* **Mass and moduli.** Expanding `e_j(s)` as a sum over j-sets R of
  products of single-coordinate classes, the term `(i,R)` has mass
  `|c_i|P(cell_i)∏_{ℓ∈R}h_ℓ`. Summing over `|R|≤J+1` gives
  `M_1(B)≤Σ_i|c_i|P(cell_i)∏_ℓ(1+h_ℓ)≤e^{S_hub}M_1'`. Merging equal cells
  only lowers the mass. Item 4 is read off.
* **Twists.** The same factorisation gives
  `E[1_{𝒜_1}1_{cell_i}ψ]=P(cell_i)ψ(x_i)∏_{ℓ∉P_i}E[(1−s_ℓ)ψ_ℓ]`, where
  `ψ_ℓ=χ_ℓ` for `ℓ|f` and `ψ_ℓ=1` otherwise. This equals
  `V·E'[1_{cell_i}ψ]`, by the same identity as for the means. Hence
  `E[1_{𝒜_1}B_2'ψ]=V·E'[B_2ψ]`. Finally
  `|E[(β_i−∏_{ℓ∉P_i}(1−s_ℓ))ψ_{rest}]| ≤ E[∏(1−s_ℓ)−β_i] ≤ ε_J`, and
  the same holds for `α_i`. Summing over i with weights `|c_i|P(cell_i)`
  gives item 5. ∎

**Corollary 1.2 (what decoupling buys).** Choose
`J := 2⌈e²S_hub + log(4M_1'/μ') + 2S_hub⌉+1`. Then `ε_J ≤ e^{−J} ≤ Vμ'/(4M_1')`
(using `V≥e^{−2S_hub}`, from `h_ℓ≤1/2`), so

```
μ(B) ≥ (3/4)Vμ',   log(M_1(B)/μ(B)) ≤ log(M_1'/μ') + 3S_hub + 1,
#primes per modulus ≤ (#primes per modulus of B_2) + J + 1.
```

*Proof.* `S^{J+1}/(J+1)! ≤ (eS/(J+1))^{J+1} ≤ e^{−(J+1)}` once
`J+1 ≥ e²S`. And `log(1/V) ≤ 2S_hub`. ∎

*Point.* The hub mass `S_hub` enters `log(M_1/μ)` additively and the
number of primes per modulus additively. It does **not** enter the
truncation level of `B_2`. That level is governed by the main system's
own mass `Σ_main`, and so is the codegree threshold `≍1/Σ_main` of
O2 Thm 10.3. This is exactly option (i) of G_pair.

**Lemma 1.3 (the main minorant under P'; PROVED).** O2 Theorems 3.1 and
10.3 hold verbatim with the Haar measure replaced by `P'`, provided
`h_ℓ≤1/100` for every ℓ, with these changes:

* vertex probabilities `p'(v)=P'(X_ℓ∈V_v)≤p(v)/(1−h_ℓ)`, and all of
  `g_ℓ, w_ℓ, S_1, S_H, deg, Δ_O` computed with `p'`;
* in the twist step, `E'χ_0(X_{ℓ_0})` is no longer 0. It satisfies
  `|E'χ_0(X_{ℓ_0})| ≤ h_{ℓ_0}/(1−h_{ℓ_0}) ≤ 0.011`, which adds at most
  `0.011` to the bracket `≤0.073` of O2 Thm 10.3 Step 4 (and `0.064` of
  Thm 3.1). The conclusion `|E'[B_2ψ]|<μ'/4` survives:
  `0.01+(0.084/0.916)<0.25`.

*Proof.* Lemmas 1.1–1.3, 2.1, 2.2, 10.1, 10.2 of O2 use only that the
coordinates are independent and that cells/events have the stated
probabilities. The local lemma likewise. The only place where uniformity
on units is used is `Eχ_0(X_{ℓ_0})=0` in the twist step. There
`|E'[1[X∉Forb]χ_0]| ≤ |E'χ_0| + P'(Forb)`, and
`|E'χ_0| = |Σ_{h∈H_{ℓ_0}}χ_0(h)|/(φ(ℓ_0^{e})−|H_{ℓ_0}|) ≤ h_{ℓ_0}/(1−h_{ℓ_0})`. ∎

Combining Theorem 1.1 (item 5) with Lemma 1.3 gives the twist condition
of PO Thm 4.1 for B: `|E[Bψ]| ≤ V|E'[B_2ψ]| + ε_JM_1' < Vμ'/4+Vμ'/4·…`.
We record the exact constants in §4 when assembling.

## 2. Atoms as triples; the hub classes are small-height rationals

**Lemma 2.1 (triples; PROVED).** The map `(s,a,b) ↦ (M,D)=(4sab−1, sa²)`
is a bijection from `{(s,a,b)∈ℕ³ : s squarefree}` onto the atoms
(`M≡3 (4)`, `D|A_M²`). For every atom:

1. the class is `−4D ≡ −a/b ≡ −4sa² ≡ −1/(4sb²) (mod M)`;
2. `gcd(M,4D+1)` divides `a+b`;
3. `D*:=sa` is the least integer with `D|D*²`, and `D|A_M² ⟺ sa|A_M`.

The same formulas define an atom `(4sab−1, sa²)` for *every*
`(s,a,b)∈ℕ³`, but then the map is no longer injective.

*Proof.* Write `D=sa²` with s squarefree (unique). For each prime p,
`v_p(s)+2v_p(a)≤2v_p(A)` iff `v_p(s)+v_p(a)≤v_p(A)`, since `v_p(s)≤1`.
So `D|A²` iff `sa|A`; put `b=A/(sa)`. Conversely `sa|sab=A`. Since
`4sab≡1 (M)`, `−4sa² = −a(4sab)/b ≡ −a/b` and
`−4sa²(4sab)²/(4sab)² ≡ −1/(4sb²)`. Finally
`b(4sa²+1)−a(4sab−1)=a+b`. If `(s,a,b)` is arbitrary,
`sa² | s²a²b²=A²` still holds. ∎

**Proposition 2.2 (three hub families; PROVED, using the prime number
theorem in progressions for fixed moduli).** Fix `θ<1/3`, the
`Π_0`-system at `y=T^θ`, `R=(y,T^{1/3}]`, `c_θ=log(1/(3θ))`. Fix positive
integers and consider the vertices `(ℓ,κ mod ℓ^{e_ℓ})` for `ℓ∈R` coprime
to the parameters, where κ is one of the rationals

* (F1) `κ=−4sa²` with `(s,a)` fixed; the modulus condition is `4sa | M+1`;
* (F2) `κ=−1/(4sb²)` with `(s,b)` fixed; condition `4sb | M+1`;
* (F3) `κ=−a/b` with `(a,b)` fixed; condition `4ab | M+1`.

For distinct `ℓ_1,ℓ_2∈R`, the pair of κ-vertices has codegree
`≥(c_θ−o(1))/φ(4n)`, where `n=sa`, `sb`, `ab` respectively.

*Proof.* As O2 Prop 10.6. Take `ℓ_3∈R` with `ℓ_1ℓ_2ℓ_3≡−1 (mod 4n)`
(one unit class mod 4n) and `M=ℓ_1ℓ_2ℓ_3≤T`. The free variable of the
family is then the integer `(M+1)/(4n)`. Lemma 2.1 (non-injective form)
gives an atom of class κ mod M. It has `m=1`, so it survives `Π_0`. ∎

(F1) with `s=1` is O2 Prop 10.6, and (F1) in general is O2 Prop 11.4
(`D=sa²`, `D*=sa`). (F2) is its image under `D↦A²/D`. (F3) is new: it
gives heavy pairs at classes such as `−2/3`.

**Definition 2.3 (hub set of level X).** `𝓗_X` is the set of rationals

```
−u/v (u,v≥1, uv≤X),    −4sa² (sa≤X),    −1/(4sb²) (sb≤X)      (s squarefree).
```

It has `|𝓗_X| ≤ X(1+log X)+2X(1+log X) ≤ 3X(1+log X)` elements. At a
prime ℓ, its *reduction* `𝓗_X(ℓ^e)` is the set of classes mod `ℓ^e` of
those members whose numerator and denominator are prime to ℓ.

Note the asymmetry. Under (F1) the class `−4a²` has height `4a²`, but its
codegree is `≍1/a`. So the hub set must contain `−4a²` up to `a≤X`, not
only up to height X.

**EVIDENCE 2.4** (`scripts/omega3_codeg.py`; `data/omega3/codeg_pairs.txt`).
For one pair `ℓ_1<ℓ_2` just above y, all pair codegrees Δ(c), c mod
`q=ℓ_1ℓ_2`, of the `Π_0`-system (exact, distinct hyperedges merged):

| T | θ | y | q | `max Δ` (class) | max Δ outside `𝓗_16` | `𝓗_64` | `𝓗_256` | `𝓗_1024` |
|---|---|---|---|---|---|---|---|---|
| 10⁹ | .28 | 331 | 116939 | 0.214 (−1) | 0.034 | 0.013 | 0.0074 | 0.0067 |
| 10¹¹ | .27 | 933 | 1022117 | 0.259 (−1) | 0.052 | 0.019 | 0.0068 | 0.0032 |
| 10¹² | .26 | 1318 | 1752967 | — | 0.086 | 0.033 | 0.0091 | 0.0036 |
| 10¹³ | .26 | 2399 | 5973127 | — | 0.089 | 0.038 | 0.0095 | 0.0048 |

* Every class among the top 40 is a member of some `𝓗_X`, with X small:
  `−1, −4, −1/4, −2, −1/2, −8, −2/3, …`, and `−4·36²`, `−4·21²`, which
  are (F1) with `sa=36, 21`.
* Outside `𝓗_X` the maximum falls roughly like `X^{−0.7}` and does not
  grow with T. This is the shape of Lemma B (§3).
