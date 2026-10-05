# Review 3 of POINTWISE_OMEGA13.md §5 / Thm 5.1 (R48c, hostile reviewer 1 of 2)

Reviewed: branch side-agent/beyond-fifth at d1a680b/ac109c3 (§5 "interface checks I1–I3", Thm 5.1).
Status: round 1 complete.

## Summary verdicts

| claim | verdict |
|---|---|
| §5 Setting (fixed good realisation `(Q,r)` of Thm 3.4) | SOUND (deterministic by existence; see C0) |
| I1(a) BRW minorant + EL_mod with `S_res` | SOUND |
| I1(b) twist, `|μ_ψ|≤μ/4` for `η≤0.19` | SOUND |
| I2 junta via digit filtration | SOUND |
| I3 coset transfer (Case A/B, item 1, consistency) | SOUND-AFTER-REPAIRS (m1: class of r mod `ℓ_aux`) |
| I3 property (I) via Lemma 3.1; Mordell-hardness | SOUND |
| Thm 5.1 exponent chain to `1/4`, `(loglog p)^{−1/4}` | SOUND-AFTER-REPAIRS (m1) |

### C0. Is the final statement deterministic? (brief's explicit question)
Yes. Thm 3.4 shows that, under the law of the square-class process (a finite tree: at most
`Σ_{ℓ≤Y}f_ℓ` steps, each with finitely many outcomes), the three bad events have total
probability `≤3/4`, so some leaf `(Q,r)` is good. For each T this is a *fixed* pair, chosen
before B is built; every later object (`F`, `B`, `u_j`, `τ`, `d_i`, `ℓ_aux`, `x`) is a
deterministic function of `(T,Q,r)`. Randomness is used only as an existence device
(non-constructive, but `(Q,r)` could be found by exhaustive search over the finite tree).
Nothing in O9 Thm 1.1 / O11 Lemma 3.1 is averaged over r. The only realisation-dependent
quantities fed forward are `S_res` and `log Q`, and both are bounded on the good leaf
(`S_res≤4E S_res≪𝓛³log𝓛`, `log Q≤4E log Q≪𝓛³(log𝓛)^5`). No circularity: `Y=𝓛^{C_0+4}`
uses only the Y-uniform Ξ bound (as R48a m5 already noted).

## Defects

### C1. I1(a) — BRW minorant + EL_mod with `S_res` — SOUND
Re-derived. O8 Lemma 3.1 is algebraic (any events `A_j`, any real `u_j`):
`F−B=Σ_iA_i(Σ_{j<i}A_je_j)²≥0`, `E[F−B]≤m²Σ_jP(E_j)E[e_j²|E_j]`. O11 Lemma 1.1 with
`λ_ℓ=2^{logℓ/(2𝓛)}` needs only `∏ℓ^{v_ℓ(E)}=M≤T` (edge weight `2^{logM/𝓛}≤2`) and gives
`Σ_{log m_U>τ}‖F^{(j)=U}‖²≤2^{−τ/(2𝓛)}=2^{−⌈log₂(100m²(S_res+1)e^{3S_res})⌉}`. Hence
`E[F−B]≤S_res e^{−3S_res}/(100(S_res+1))≤e^{−3S_res}/100≤δ/100`, because
`ΣP(E_j)≤Σβ^{s}P(E)=S_res` and `δ≥e^{−(4/3)S_res}≥e^{−3S_res}` (Lemma 1.1 needs `x_E≤η≤1/4`,
true). `μ≥0.99δ`, and O9 Lemma 2.1 (`B^-≤F−B`) gives `A≤1+2/99≤1.03`. Both use only
`E_{rH}`, never the class. `τ≍𝓛S_res+𝓛²` (with `log m≤2𝓛`), as claimed.
Toy check (i) in `scripts/review_o13c_twist.py`: `exp(−(4/3)S)/δ≤0.98` over ~19k events,
β up to `e^{1/3}` (`data/review_o13c/twist.txt`).

### C2. I1(b) — twist — SOUND
Re-derived. f is odd, because `8|Q` and `gcd(f,Q)=1`. So ψ is a product of Legendre symbols at
the primes of f, and each `ℓ_0|f` is an `a=0` unit coordinate. Write `F=F'·1[X_{ℓ_0}∉Forb(X_{−ℓ_0})]`.
Since `E_{X_{ℓ_0}}ψ_{ℓ_0}=0`, we get `|E_{X_{ℓ_0}}[1_{∉Forb}ψ_{ℓ_0}]|≤P_{X_{ℓ_0}}(Forb)`, so
`|E[Fψ]|≤Σ_{E∋ℓ_0}p_{ℓ_0}(E)P(E∖ℓ_0∩F')`. The general conditional bound
`P(A|∩_𝒮F̄)≤P(A)∏_{F∈𝒮,F∼A}(1−x_F)^{−1}` is standard (HSS 2011 Thm 2.1). It needs:
* the LLL condition for 𝒮, inherited by subfamilies;
* A mutually independent of the 𝒮-events with disjoint supports, true in a product space.

The product is `≤exp((4/3)Σ_{ℓ∈supp A}w̃_ℓ)≤β^{|supp A|}`, using sums over a subfamily
`≤w̃_ℓ≤η`. With `|supp(E∖ℓ_0)|=s(E)−1` and `P(E)=p_{ℓ_0}(E)P(E∖ℓ_0)`, this gives
`|E[Fψ]|≤β^{−1}w̃_{ℓ_0}EF'`. The same computation without ψ gives `EF≥(1−η)EF'`.

Numerics: the requirement is `(0.01+η/(1−η))/0.99≤1/4`, i.e. `η≤0.19192`. With
`β=1+1/log𝓛`, `η≤0.19` iff `𝓛≥32.2` ("large T"). Also `w̃_{ℓ_0}≤η` holds at `ℓ_0>Y`, by
the good-realisation choice, and at `ℓ_0≤Y`, by stopping.

Toy checks (ii)–(iv), exact enumeration including a fibre coordinate with `a=1`, all `≤1`:
* conditional bound ratio ≤0.981;
* `|E[Fψ]|/(β^{−1}w̃_{ℓ_0}EF')` ≤0.68;
* `(1−η)EF'/EF` ≤0.997.

### C3. I2 — junta via digit filtration — SOUND
O11 Lemma 1.1 uses only the following:
* independence of the digit blocks `(δ_{ℓ,i})_{i≥i_0(ℓ)}` across ℓ and i, under the fibre
  measure. Digit 0 is uniform on `{1..ℓ−1}` when `a_ℓ=0`; this is still an independent block,
  and its uniformity is never used.
* events that fix initial segments `i_0..v−1` of free digits.
* the edge-weight bound `∏λ^{2v}≤2`.

On `n≡r (ℓ^{a_ℓ})`, the digits `<a_ℓ` are the constants `r`'s digits, and the digits `≥a_ℓ`
are i.i.d. uniform on `{0..ℓ−1}`, for *every* r. A surviving event agrees with r on the fixed
digits (`−4D≡r mod ℓ^{a_ℓ}`). Its free part is therefore an initial segment, and the same holds
on the conditioned systems `F^{(j)}` (`i_0=max(a_ℓ,v_ℓ(E_j))`, O11 Remark (ii)). So r enters only
through which atoms survive, which fixes the family, and never through the measure.
**Answer to the brief:** once `(Q,r)` is fixed, the random square class does not enter O11
Lemma 1.1.

One point worth a sentence in §5: `E[F|X_W]` for a non-initial digit set W is still a function
of `n mod m_W`. Its cells are the fibre classes mod `m_W`, so they are consistent with r. Weights
are absolute (`m_U` includes the fixed fibre digits), so `log m_U≤τ` bounds the true modulus.
Cells of B: three event moduli (`≤T` each) and two `u_j`'s (`≤e^τ` each), so `≤e^{2τ+3𝓛}`.

### C4. I3 — coset transfer — SOUND-AFTER-REPAIRS (m1)
Re-derived from O9 Thm 1.1 / O11 Lemma 3.1:
* *Coefficients.* On `G=(ℤ/N)^*`, `N=lcm(Q,D)`, `G→(ℤ/Q)^*` is onto with fibres the cosets
  of H. So `c(χ)=E_{rH}[Bχ̄]/φ(Q)`, `|c(χ)|≤Aμ/φ(Q)`, `c(χ_0)=μ/φ(Q)`.
* *Item 1.* Every cell is consistent with r, so it meets rH in one class mod `lcm(d_i,Q)≤Z`.
* *Case A.* For χ trivial on H, `c(χ)=χ̄(r)μ/φ(Q)`. A real character mod Q is a product of a
  character mod 8 and Legendre symbols at the odd `p|Q`: the only quadratic character of
  `(ℤ/p^a)^*` is `(·|p)`, so this list is complete. At r all factors are 1: `r≡1 (8)`, and r is
  a QR at each `p|Q`. The exceptional `χ_1` is real (LP), so O9's λ-argument is verbatim.
  Non-real χ appear only through `|c(χ)|` (Case 0 and the (G) error).
* *Case B.* `c(χ)=ψ_1(r)E_{rH}[Bψ_2]/φ(Q)` with `ψ_1(r)=1`, and `c(χ)` is real. The averaging
  argument (a cell with `f_2∤d_i` has zero `ψ_2`-mean) uses a prime `p|f_2` coprime to Q, so it
  is uniform on units on rH.
* *Property (I).* As written; uses Lemma 3.1's consequence for `M|Q`.
* *Mordell-hardness.* r is a unit square mod 840, and these are exactly
  {1,121,169,289,361,529}.

From-scratch checks (`scripts/review_o13c_jacobi.py 40000`, `data/review_o13c/jacobi.txt`):
* Lemma 3.1(a),(b) on all 363 982 atoms `M≤4·10⁴`: 0 failures. Also 0 hits of `r≡−4D (M)` for
  random unit squares r.
* The unit squares mod 840 are the Mordell list.
* For four moduli Q (up to `8·27·5·49·11·17`), the listed real characters mod Q number exactly
  `#{x²=1}` (so the list is complete), and all equal 1 at every admissible r (0 failures).

Defect m1 (class of r mod `ℓ_aux`) is listed below.

### C5. Thm 5.1 — the exponent chain — SOUND-AFTER-REPAIRS (m1)
Re-derived on the good leaf, with `Y=𝓛^{C_0+4}`, `logY≍log𝓛`, `1/η≍log𝓛`:
* `log Q≤4E log Q≪(1/η)𝓛³(logY)^4≪𝓛³(log𝓛)^5`;
* `S_res≤4S_H^β≪𝓛³log𝓛`;
* `τ=2𝓛⌈log₂(100m²(S_res+1)e^{3S_res})⌉≤2𝓛(4.33S_res+5.8𝓛+O(log S_res))≪𝓛⁴log𝓛`;
* `log max d_i≤2τ+3𝓛`, `log ℓ_aux≤log max d_i+1`.

So `log Z≪𝓛⁴log𝓛`, which dominates the quarantine `𝓛³(log𝓛)^5`. O9 Thm 1.1 with `A≤1.03`
gives a prime `p≤x` with `log x≍log Z`. Inverting `log p≪𝓛⁴log𝓛` gives
`𝓛≫(log p/loglog p)^{1/4}`, hence `W(p)>T=e^𝓛≥exp(c(log p)^{1/4}(loglog p)^{−1/4})`. The
loglog exponent `−1/4` is correct: it comes from the junta factor `log𝓛` in `S_res`, not from
`log Q`.

Distinctness of the p's as `T→∞` requires `p>T`, and this is defect m1.

Dependency list: (G), NT, OMEGA10 Thm 3.4 are the non-elementary inputs. Classical inputs are
also used, as in all previous theorems of the chain:
* Landau–Page and the Page bound inside O9;
* the HSS conditional LLL bound. HSS is not in `sources/`, so I did not check the theorem
  number. The bound is standard, and I re-derived it in one line:
  `P(A|∩F̄)≤P(A∩_{F≁A}F̄)/P(∩_{F∼A}F̄|∩_{F≁A}F̄)≤P(A)/∏_{F∼A}(1−x_F)`.

Elsholtz–Tao is indeed not used: all masses are Haar masses (Lemma 3.2–3.3), and S♯ never
enters §5. The label is honest.

## Defects

No FATAL or MAJOR defects found in §5 / Thm 5.1.

**m1 (MINOR, needed for "infinitely many"; §5 I3 and Thm 5.1 proof, bullet "ℓ_aux appended
to Q").** The class of r modulo `ℓ_aux` is never specified. Two things use it:
1. I3's hypothesis "r a square mod every odd prime of Q". Once `ℓ_aux|Q`, this must hold at
   `ℓ_aux` too, otherwise Case A's "`χ(r)=1` for all real χ" fails for the Legendre symbol mod
   `ℓ_aux`.
2. `p>T`. With class 1 this followed from `p≡1 (ℓ_aux)`, `ℓ_aux>T`. For a general class the
   transfer can a priori return a prime `p<ℓ_aux` (the least representative of r), and then
   the T→∞ limit need not give distinct primes.

*Repair:* add "and `r≡1 (mod ℓ_aux)`" (CRT; 1 is a square, `ℓ_aux>T` so no atom sees it).
Then `p≡1 (ℓ_aux)` gives `p>2ℓ_aux>T`, exactly as in O9 Thm 2.2.

**m2 (MINOR; I2, cell consistency).** I2/I3 say "`u_j` are functions of fibre coordinates, so
the argument of O11 Thm 3.2 applies". Spell out the one point that is not literally an
initial-segment statement. `E[F|X_W]` for a non-initial digit set W is a function of
`n mod m_W` with absolute `m_W`. Its cells are fibre classes mod `m_W`, so they are consistent
with r, and the `u_j`-moduli are `≤e^τ` because the weights are absolute. (This is true, see
C3. It is only a missing sentence.)

**m3 (MINOR; explicit range).** §5 Setting and Lemma 1.1 "Range" use `η≤0.19`, i.e.
`(3/4)log(1+1/log𝓛)≤0.19`. This needs `𝓛≥32.2` (`T≥e^{33}`). State it, or say "for T large",
as Thm 3.4 does. The exact threshold is `η≤0.1919`.

**m4 (MINOR; stale text).** These passages still say the interface checks "have not been done"
or label them OPEN:
* Cor 3.5's closing paragraph ("These are checks … They have not been done.");
* Prop 1.3(c).

§4's heading says "checkpoint 1" but its table has the §5/Thm 5.1 rows. Add "(done in §5)"
pointers, and retitle §4 "checkpoint 2".

**m5 (MINOR; citation hygiene).** Lemma 1.1's general conditional bound is attributed to "O8
Lemma 3.3; Haeupler–Saha–Srinivasan". Give the theorem number (HSS, J. ACM 2011, Thm 2.1 in
the arXiv version, to be verified) or the one-line proof in C5 above. The source is not
archived in `sources/`.

## Verdict
§5 and Thm 5.1 are **SOUND after the MINOR repair m1**. The others are presentation.

The prime-side exponent `1/4` with `(loglog p)^{−1/4}` follows from:
* Thm 3.4's good leaf (deterministic by existence);
* Lemma 1.1;
* O8 Lemma 3.1 / O11 Lemma 1.1, Cor 1.2;
* O9 Thm 1.1 / O11 Lemma 3.1 on the coset rH.

Its label is "PROVED modulo (G), NT, OMEGA10 Thm 3.4", with Thm 3.4's own inputs (Lemma 3.3,
reviewed in R48a/R48b) taken as given.

The random square class causes no problem:
* it is fixed before anything else is built;
* it does not enter the digit filtration;
* real characters are 1 at r, so Case A is verbatim;
* Lemma 3.1 (re-verified from scratch) rules out fired events.

Toy checks are in `scripts/review_o13c_*.py` and `data/review_o13c/`.
