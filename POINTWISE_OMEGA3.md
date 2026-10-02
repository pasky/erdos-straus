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

## 3. Two-level composition: pushing heavy pairs into a graph level (PROVED)

§1 handles prime-local hub classes. The same idea works one level up, and
then no upper bound on pair codegrees is needed at all. Heavy pairs are
*moved* into a lower level that consists of singles and edges only. That
level is a graph system (O2 §2), so it has **no codegree condition**, and
its truncation level may be as large as we like. The hyperedge level keeps
a truncation tied only to *its own* mass, because the conditional local
lemma factors out the lower level.

**Setting 3.0.** O2 Setting 3.0 (Haar measure P on the free coordinates,
2|Q, all vertices are classes mod `ℓ^{e_ℓ}`). Two event families:

* **level 2:** singles and edges (Setting 2.0 of O2); `𝒜_2` = "no level-2
  event occurs", `F_2=1_{𝒜_2}`;
* **level 3:** hyperedges with 3 vertices at distinct primes (Setting
  10.0); `F_3=1_{𝒜_3}`, `S_H` = their total mass.

Per-prime masses: `g_ℓ` (level-2 singles), `w^{(2)}_ℓ`, `w^{(3)}_ℓ` (mass
of level-2 edges / level-3 hyperedges at ℓ). Assume

* (P) `g_ℓ + w^{(2)}_ℓ + w^{(3)}_ℓ ≤ 1/32` for every ℓ;
* (D2) every level-2 vertex has level-2 degree `≤ δ:=e^{−50}`;
* (D3) every level-3 vertex has level-3 degree `≤ δ_3` and every pair of
  level-3 vertices has codegree `Δ_O ≤ t`, where
  `t := δ_3/(C_3(S_H+1))` (constants of O2 Thm 10.3 for k=3, with the
  weight w=16 replaced by `w'=16e^{1/2}`; see Step 2 below).

**Lemma 3.1 (conditional local lemma; PROVED, standard).** Let 𝒜 be the
family of all level-2 and level-3 events, `x_E:=2P(E)`. Under (P):

1. `P(E | ∩_{E'∈S}Ē') ≤ x_E` for every E and every `S⊆𝒜∖{E}`; hence
   `P(𝒜_2∩𝒜_3) ≥ P(𝒜_2)·∏_{E level 3}(1−x_E) ≥ P(𝒜_2)e^{−3S_H}` and
   `P(𝒜_2) ≥ e^{−3(S_1+S_2)}`.
2. For every event B determined by the coordinates of a prime set U,
   `P(B ∩ 𝒜_2) ≤ P(𝒜_2)·P(B)·e^{|U|/2}`.

*Proof.* Two events are adjacent iff their supports meet. For E at the
primes U_E, `Σ_{E'∼E}x_{E'} ≤ Σ_{ℓ∈U_E}2(g_ℓ+w^{(2)}_ℓ+w^{(3)}_ℓ) ≤ 3/16`,
so `∏_{E'∼E}(1−x_{E'}) ≥ 1/2` and `P(E)≤x_E∏(1−x_{E'})`: the asymmetric
local lemma holds. Item 1 is its standard proof (Alon–Spencer Lemma
5.1.1): the bound `P(E|∩_S Ē')≤x_E` holds for all S, and
`P(𝒜_2∩𝒜_3)=P(𝒜_2)∏_i P(Ē_i | 𝒜_2∩Ē_1∩…∩Ē_{i−1})` over the level-3
events. Item 2 is the conditional form (Haeupler–Saha–Srinivasan, J. ACM
58 (2011) Thm 2.1; used already in O2 Thm 3.1) applied to the level-2
family alone: `P(B|𝒜_2) ≤ P(B)∏_{A∈Γ(B)}(1−x_A)^{−1}`, where Γ(B) is the
set of level-2 events meeting U. Then
`∏(1−x_A)^{−1} ≤ exp(1.2Σ_{A∈Γ(B)}x_A) ≤ exp(1.2·|U|/16) ≤ e^{|U|/2}`. ∎

*Constants.* `w:=16`, `w':=16e^{1/2}`, `δ_3:=[4e·3·(1+w')³]^{−1}`,
`δ:=e^{−50}`. For `Ŝ≥S_H` put
`Λ_3:=6e(1+w')³Ŝ`, let `L_3` be least with `4^{L_3+1}≥400e^{Λ_3+3Ŝ}`,
and `t(Ŝ):=δ_3/(3(L_3+1))`. So `L_3=O(Ŝ+1)` and `1/t=O(Ŝ+1)`.
Condition (D3) reads: level-3 degrees `≤δ_3`, pair codegrees `≤t(Ŝ)`.

**Theorem 3.2 (two-level minorant; PROVED).** In Setting 3.0 assume (P),
(D2), and (D3) with some `Ŝ≥S_H`. Put `Σ:=S_1+S_2+Ŝ`. There is a real
combination B of unit cells such that

1. `B ≤ F_2F_3` pointwise (for every integer n);
2. `F_2F_3−B ≥ 0` and `E[F_2F_3−B] ≤ 0.01·P(𝒜_2∩𝒜_3)`; hence
   `μ:=EB ≥ 0.99·e^{−3Σ}`;
3. `log(M_1(B)/μ) ≤ C(Σ+1)`, and every cell of B involves at most
   `C(Σ+1)` primes (C absolute);
4. the twist condition of PO Thm 4.1: `|E[Bψ]| < μ/4` for every real
   primitive ψ of conductor `f>1` whose primes are free.

*Proof.* **Step 1 (top level).** Let `B_3:=B_{L_3}−4^{L_3+1}G^{cov}_{L_3+1}`
be the O2 Lemma 10.1 minorant of `F_3`, built from level-3 events only.
Pointwise `B_3≤F_3` and `|F_3−B_3|≤2·4^{L_3+1}G^{cov}_{L_3+1}`.

* *Tilted moment.* O2 Lemma 10.2's proof starts from the pointwise bound
  `Σ_{u≤U_0}w^uG^{cov}_u ≤ Σ_{C private,|C|≤U_0}(1+w)^{|π(C)|}1[C occurs]`.
  Multiply by `F_2` and take expectations. Lemma 3.1(2) with `U=π(C)`
  gives `E[F_2 1[C]] ≤ P(𝒜_2)P(C)e^{|π(C)|/2}`. The rest of the proof of
  Lemma 10.2 runs with `1+w'=(1+w)e^{1/2}` in place of `1+w`. Its
  hypothesis `D≤[2e·3(1+w')³]^{−1}` with `U_0=L_3+1` reads
  `deg + 3(L_3+1)Δ^{(2)} ≤ 2δ_3`, which (D3) gives. Hence
  `E[F_2G^{cov}_{L_3+1}] ≤ P(𝒜_2)w^{−(L_3+1)}e^{Λ_3}`, and

  ```
  E[F_2(F_3−B_3)] ≤ 2·4^{L_3+1}16^{−(L_3+1)}P(𝒜_2)e^{Λ_3} ≤ P(𝒜_2)e^{−3Ŝ}/200 ≤ P(𝒜_2∩𝒜_3)/200,
  ```
  by the choice of `L_3` and Lemma 3.1(1).
* *Haar mass.* The same lemma without tilt gives
  `M_1(B_3) ≤ Σ_{u≤L_3}2^uEG^{cov}_u + 4^{L_3+1}EG^{cov}_{L_3+1} ≤ 2e^{Λ_3}`.
  Every cell of `B_3` involves at most `3(L_3+1)` primes.

**Step 2 (bottom level, cell by cell).** Write `B_3=Σ_ic_i1_{C_i}` with
cells `C_i=(P_i,x_i)`. Fix i.

* If `x_i` realises a level-2 single at some `ℓ∈P_i`, or both ends of a
  level-2 edge inside `P_i`, then `F_2=0` on `C_i`. Put `β_i=α_i=0`.
* Otherwise, on `C_i` we have `F_2=F_2^{(i)}`. Here `F_2^{(i)}` is the
  void indicator of the *cell-conditioned* level-2 system on `𝒫∖P_i`:
  the original singles and edges there, plus the induced singles
  `{w : {v,w} level-2 edge, v realised by x_i}`. Its masses are
  `S_1^{(i)}≤S_1+δ|P_i|` and `S_2^{(i)}≤S_2`, and its degrees are `≤δ`.
* O2 Lemmas 1.2, 1.3, 2.1 (`z=16`, `δ=e^{−3z−2}`) give, for every L,
  `B^{(i)}_L` and `G^{(i)}_{L+1}` with
  `|B^{(i)}_L−F_2^{(i)}|≤4^{L+1}G^{(i)}_{L+1}`,
  `EG^{(i)}_{L+1}≤16^{−(L+1)}e^{Λ^{(i)}}`, `M_1(B^{(i)}_L)≤e^{Λ^{(i)}}`,
  where `Λ^{(i)} ≤ Λ_2:=16(S_1+3δ(L_3+1))+16e^{98}S_2`.
* Put `β_i:=B^{(i)}_{L_2}−4^{L_2+1}G^{(i)}_{L_2+1}` and
  `α_i:=B^{(i)}_{L_2}+4^{L_2+1}G^{(i)}_{L_2+1}`. Then
  `β_i≤F_2^{(i)}≤α_i`, and both differ from `F_2^{(i)}` by at most
  `2·4^{−(L_2+1)}e^{Λ_2}` in Haar mean. Choose `L_2` least with
  `4^{L_2+1} ≥ 800e^{Λ_2+Λ_3+3Σ}`.

Define

```
B := Σ_{c_i>0} c_i β_i 1_{C_i} − Σ_{c_i<0} |c_i| α_i 1_{C_i}.
```

All functions here are combinations of unit cells: `β_i,α_i` live on
`𝒫∖P_i`, so `β_i1_{C_i}` is a product of cells on disjoint prime sets.

1. *Minorant.* `B ≤ Σ_ic_iF_21_{C_i} = F_2B_3 ≤ F_2F_3`.
2. *Mean.* `β_i,α_i` are independent of `1_{C_i}`. So

   ```
   E[F_2F_3−B] ≤ E[F_2(F_3−B_3)] + Σ_i|c_i|P(C_i)·2·4^{−(L_2+1)}e^{Λ_2}
              ≤ P(𝒜_2∩𝒜_3)/200 + 2e^{Λ_3}·2·e^{−Λ_3−3Σ}/800 ≤ P(𝒜_2∩𝒜_3)/100,
   ```
   using `P(𝒜_2∩𝒜_3) ≥ e^{−3Σ}` (Lemma 3.1(1)).
3. *Mass and supports.*
   `M_1(B) ≤ Σ_i|c_i|P(C_i)(e^{Λ_2}+4^{L_2+1}16^{−(L_2+1)}e^{Λ_2}) ≤ 4e^{Λ_3+Λ_2}`,
   and `log(1/μ) ≤ 3Σ+1`. A cell of B involves at most
   `3(L_3+1)+2(L_2+1)` primes. Since `L_3=O(Ŝ+1)`, we get `Λ_2`,
   `Λ_3`, `L_2 = O(Σ+1)`.
4. *Twist.* As in O2 Thm 3.1 Step 4, `μ_ψ=E[Bψ]` and
   `|E[Bψ]| ≤ E[F−B] + |E[Fψ]|` with `F=F_2F_3`. Fix a prime `ℓ_0|f`, and
   let `𝒜'` be "no event (either level) avoiding `ℓ_0` occurs". Then
   `|E[Fψ]| ≤ P(𝒜'∩{an event at ℓ_0 occurs})`. That is at most
   `P(𝒜')(g_{ℓ_0}+1.3(w^{(2)}_{ℓ_0}+w^{(3)}_{ℓ_0})) ≤ P(𝒜')·0.05`. Here
   the conditional local lemma for the family defining `𝒜'` bounds the
   probability of the remaining part `e∖u` of an event through `ℓ_0`
   by `1.3P(e∖u)`: its neighbours meet at most two primes, with
   `∏(1−x)≥(1−1/16)²`. Since `P(𝒜_2∩𝒜_3) ≥ 0.95P(𝒜')`, we get
   `|μ_ψ| ≤ (0.01+0.053)P(𝒜_2∩𝒜_3) < μ/4`. ∎

*Why this closes G_pair's circularity.* The codegree threshold `t(Ŝ)`
depends only on the level-3 mass Ŝ. The level-2 mass `S_1+S_2` can be
arbitrarily large compared with Ŝ: it enters only `L_2`, and level 2
has no codegree condition. In O2's one-level scheme, the hub pairs had
to be paid for inside the same truncation that set the threshold.

**Lemma 3.3 (pushing hubs and heavy pairs down; PROVED).** Start from
one system of singles, edges and 3-vertex hyperedges (Settings 2.0/10.0,
all vertices classes mod `ℓ^{e_ℓ}`), with masses `S_1,S_2,S_H`. Suppose
every prime has total mass `g_ℓ+w^{(2)}_ℓ+w^{(3)}_ℓ ≤ c_0`. Fix
`Ŝ≥S_H`, put `t=t(Ŝ)`, and assume `c_0 ≤ δδ_3t/288`. Perform, in order:

* (a) every vertex of hyperedge-degree `>δ_3` becomes a level-2 single,
  and the hyperedges through it are deleted;
* (b) every vertex pair O with codegree `Δ_O>t` (computed after (a))
  becomes a level-2 edge, and the hyperedges containing it are deleted;
* (c) every vertex of level-2 degree `>δ` (after (b)) becomes a level-2
  single, and the edges and hyperedges through it are deleted.

The result is a two-level system that satisfies (P), (D2) and (D3)
with this Ŝ. Every original event either occurs only if some level
event occurs, or is itself a level event. So `F_2F_3 ≤ 1[no original
event]`. Its masses satisfy

```
S_H^{new} ≤ S_H,   S_2^{new} ≤ S_2 + 3S_H/t,   S_1^{new} ≤ S_1 + 3S_H/δ_3 + 2S_2^{new}/δ.
```

*Proof.* Deletions only lower degrees and codegrees. So after (c) all
level-3 degrees are `≤δ_3` and all pair codegrees are `≤t`. (Pushed
pairs have codegree 0 because all their hyperedges are gone.) All
level-2 degrees are `≤δ`. A deleted hyperedge contains a level-2
single or edge, so it cannot occur when no level-2 event occurs; the
same holds for deleted edges.

*Masses (Markov).* Per prime:

* (a) adds `≤w^{(3)}_ℓ/δ_3`: each hyperedge at ℓ has one vertex there,
  and `Σ_{v at ℓ}p(v)deg(v)=w^{(3)}_ℓ`;
* (b) adds `≤Σ_{O∋v at ℓ}P(O)Δ_O/t = 2w^{(3)}_ℓ/t`: each hyperedge at ℓ
  contains two pairs through its ℓ-vertex;
* (c) adds `≤w^{(2),new}_ℓ/δ`.

So the new per-prime total is
`≤c_0(2+1/δ_3+(1+2/t)(1+1/δ)) ≤ 9c_0/(tδδ_3) ≤ 1/32`, since
`t,δ,δ_3<1` give `(1+2/t)(1+1/δ)≤6/(tδ)`. This is (P). The global bounds are
the same Markov sums over ℓ, with `Σ_ℓw^{(3)}_ℓ=3S_H` and
`Σ_ℓw^{(2)}_ℓ=2S_2`. ∎

**Theorem 3.4 (criterion for supports ≤3; PROVED).** Setting 3.0 of O2
(congruence system, 2|Q), with singles, edges and hyperedges on at most
3 free primes, and with (I) of O2 Thm 3.1. Let `Ŝ≥S_1+S_2+S_H`. If
every free prime has total mass `≤c_0(Ŝ):=δδ_3t(Ŝ)/288`, there is a
minorant B as in PO Thm 4.1 (moduli coprime to Q, unit classes,
`B≤1[W>T]` on `n≡1 (Q)`, twist condition) with

```
log(M_1/μ) ≤ C(Ŝ²+1),   log(1/μ) ≤ C(Ŝ²+1),   #primes per modulus ≤ C(Ŝ²+1).
```

*Proof.* Lemma 3.3, then Theorem 3.2 with
`Σ = S_1^{new}+S_2^{new}+Ŝ = O(Ŝ/t+Ŝ) = O(Ŝ²+1)`. (I) transfers because
`B≤F_2F_3≤1[no original event]≤1[W>T]`. ∎

*Remark (what replaced the codegree hypothesis).* O2 Thm 10.3 needed
(CD_3), an upper bound on **all** pair codegrees, and §11.4 showed it
fails for the `−4D` hubs. Here no such bound is assumed. Heavy pairs are
moved down by the first-moment (Markov) bound `Σ_OP(O)Δ_O=3S_H`, at cost
`O(Ŝ/t)=O(Ŝ²)` in the *level-2* mass. That mass never feeds back into t.
The `−4d²` clusters of O2 §11.4 (reviewer r3) now become dense level-2
edges. Their vertices have level-2 degree `≍c_θ>δ`, so step (c) turns
them into singles. That is exactly the joint hub-vertex quarantine of §1,
with cost `O(Ŝ²)` instead of the impossible `O(L log L)` *inside* the
level-3 truncation.

## 4. Exponent 4: `W(p) > (log p)^{4−o(1)}` infinitely often

Put `𝓛=log T`, `y:=T^{1/4}exp(2𝓛/log 𝓛)` (so `y⁴>T`), `Π_0={ℓ≤y}`.
Let `S*` be the uniform mass of O2 Lemma 11.1,
`S*≤exp(O(𝓛/log 𝓛))`, and put `Ŝ:=S*+1`, `c_0:=c_0(Ŝ)` (Thm 3.4).
Then `1/c_0=O(Ŝ)`.

**Construction 4.1.**

1. Run O2 Lemma 11.2 (iterated quarantine) from `Π_0` with `z=y` and
   threshold `c_0`. It stops at `Π=Π_0∪𝓑` with `|𝓑|≤3S*/c_0=O(Ŝ²)`,
   and every free prime has `w_ℓ(Π)≤c_0`.
2. `Q:=lcm(24,ℓ^{e_ℓ}:ℓ∈Π)` with `e_ℓ=max{e:ℓ^e≤T}`, and
   `𝒫:={y<ℓ≤T}∖𝓑`.
3. Each atom surviving Π has rough part `r≤T` with all prime factors
   `>y>T^{1/4}`, so `Ω(r)≤3`. It gives a single, an edge or a 3-vertex
   hyperedge (class `−4D mod r`, lifted to classes mod `ℓ^{e_ℓ}` as in
   O2 §10.3). Identical events are merged.

**Lemma 4.2 (hypotheses of Thm 3.4; PROVED).** For T large:

* (I) holds (O2 Lemma 4.3 (I), verbatim);
* the per-prime total `g_ℓ+w^{(2)}_ℓ+w^{(3)}_ℓ = w_ℓ(Π) ≤ c_0` for every
  `ℓ∈𝒫`. Lifting preserves the mass at every prime, and `w_ℓ(Π)` is by
  definition the mass of the distinct events whose rough part ℓ divides;
* `S_1+S_2+S_H ≤ S_tot(Π) ≤ S* < Ŝ` (distinct events are at most atoms;
  O2 Lemmas 4.1, 11.1);
* `log Q ≤ (π(y)+|𝓑|)𝓛+log 24 ≤ 5y`, because `𝓛/log y→4`.

**Theorem 4.3 (PROVED modulo Thorner–Zaman, via PO Thm 4.1; effective).**
There is an absolute constant C such that for infinitely many
Mordell-hard primes p,

```
W(p) ≥ (log p)^4 · exp(−C log log p / log log log p).
```

More precisely, for every large T there is a prime `p≡1 (mod 840)` with
`W(p)>T` and `log p ≤ T^{1/4}exp(O(𝓛/log 𝓛))`. So
`log L_h(T) ≤ T^{1/4+o(1)}`, H_MIN(θ) holds for every θ>1/4, and
`H_MOD(A)` is refuted for every `A<4`.

*Proof.* Lemma 4.2 and Theorem 3.4 give a minorant B with
`K:=1+log(M_1/μ)=O(Ŝ²)=exp(O(𝓛/log 𝓛))`. Its moduli are products of
`O(Ŝ²)` prime powers `≤T`, so `log max d_i ≤ exp(O(𝓛/log 𝓛))`. It also
satisfies the twist condition, and `log Q≤5y`. The rest is O2 Thm 5.1's
proof verbatim:

* take a prime `ℓ_0∈(R,2R]`, `R=max(T,max d_i)`, and replace Q by
  `Qℓ_0`;
* PO Thm 4.1 then gives `p≡1 (Qℓ_0)` with `W(p)>T` and
  `log p ≤ C_1K max(log Z,K) ≤ y·exp(O(𝓛/log 𝓛))`;
* `840|Q` and `p>T`;
* invert: `log log p ≤ 𝓛/4+O(𝓛/log 𝓛)`. ∎

**Corollary 4.4 (PROVED modulo Thorner–Zaman).** For infinitely many hard
p, jointly `W(p)≥(log p)^{4−o(1)}` and `ck_min(p)≥(log p)^{1−o(1)}`.
(As O2 Cor 5.2: `p≡1` mod every prime `≤y`.)

*Scope.* The prime side now beats O2's exponent 3. The only inputs
beyond O2 are:

* the two-level composition (Thm 3.2);
* the conditional local lemma (Lemma 3.1);
* first-moment pushing (Lemma 3.3).

No arithmetic input about pair codegrees is used, so §2 is explanation
(EVIDENCE for *where* the heavy pairs are), not a step of the proof.
