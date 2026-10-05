# Hostile review R30b of POINTWISE_OMEGA8.md (O30) — reviewer 2 of 2: inputs and interface

Reviewer branch `side-agent/review-omega8b`, merged `side-agent/haar-primes-2`
(ff). Scope (per task): (1) transfer via PO Thm 4.1 / Thorner–Zaman,
(2) O2 Lemma 4.3 (I), Lemmas 11.1–11.2, Thm 11.3 and the iterated quarantine,
(3) definition chain W(p), Mordell-hard, L_h(T), exponent bookkeeping to
`(log p)^{1/14}`, (4) Thm 4.4 asymptotics. The BRW sandwich / switching-lemma
machinery (Lemmas 3.1, 4.1) is the other reviewer's; I use it only at the
interface. From-scratch scripts: `scripts/review_o8b_*.py`.

## Summary verdict

| Claim | Verdict |
|---|---|
| (1) PO Thm 4.1 (Thorner–Zaman, λ, Lemma 3.2) applies to the OMEGA8 minorant (Thm 3.4 interface, Lemma 3.3 twist, Lemma 3.2 sizes) | **SOUND** (minor D1–D3, D5) |
| (2) O2 Lemma 4.3 (I), Lemmas 11.1–11.2, Thm 11.3, ET Prop 1.4 ⇒ `S*≪𝓛^4log𝓛`; iterated-quarantine Π supplies what OMEGA8 needs | **SOUND** (minor D4) |
| (3) W(p) / Mordell-hard / L_h chain; `log L_h(T)≪𝓛^{14}` ⇒ `W(p)≥exp(c(log p)^{1/14})` | **SOUND** |
| (4) Thm 4.4 `(1/(2log2)−o(1))log₂p·log₃p`, modulo TZ only | **SOUND** |
| **Thm 4.3 overall** | **SOUND given the new machinery**: the inputs and the interface carry no gap; the theorem stands or falls with Lemma 3.1 (BRW) and Lemma 4.1 (bit encoding + Håstad/LMN), which are reviewer 1's. My toy checks of those (B≤F pointwise, `E[F−B]≪EF`, Lemma 3.3 chain, twist ≤ μ/4) found nothing wrong, and a light pass over Lemma 4.1(c) (fibre density `≤e^{1/2}`, blockwise junta of `E[χ_S\|π(U)]`) agrees. |

No FATAL or MAJOR defect found in my scope. Labels ("PROVED modulo TZ and ET
Prop 1.4", resp. "modulo TZ only") are accurate for my scope; "effective
if ET's constant is" is the right hedge.

## 1. Transfer to primes: PO Thm 4.1 applied to the OMEGA8 minorant

**Source check.** TZ arXiv:2108.10878v2 is archived
(`sources/lit2026/arxiv-2108.10878-thorner-zaman-pntap.{pdf,txt}`). I read
Cor. 1.4 and Remark 1.5 there: `Σ_{p≤x,p≡a(q)} log p = (λx/φ(q))[1+O(exp(−c_4
log x/log q) + exp(−c_4(log x)^{3/5}/(log log x)^{1/5}))]` for coprime
`q≥2, a`, `x≥q^{12}`; constants absolute and effective; `λ=1−χ_1(a)x^{β_1−1}/β_1`
if β_1 exists; (1.7) gives `0<λ<2`. PO Thm 3.1 quotes this correctly. The
McCurley region is quoted by TZ (p. 1); McCurley's paper itself is not in
`sources/` (as PO already states). Published Math. Z. version not compared.

**Re-derivation of PO Thm 4.1** (independently, line by line). With
`q_i=Qd_i`, `gcd(d_i,Q)=1`, `a_i` the CRT class (≡1 mod Q, ≡b_i mod d_i):
`φ(q_i)=φ(Q)φ(d_i)` (needs the coprimality), so the TZ main terms sum to
`(x/φ(Q))Σ_i c_iλ_i/φ(d_i)`. Case A (`q*|Q`): `χ*(a_i)=χ*(1)=1`, common
λ_*>0, bracket `μ−C_0E_1M_1`. Case B: for i with `q*|q_i`, since the Q-part of
`q_i` is exactly Q, `q*|q_i ⟺ q*_Q|Q and q*'|d_i`; then `χ_1(a_i)=χ*_Q(1)ψ(b_i)
=ψ(b_i)`, ψ:=χ*' real primitive with conductor `q*'>1` coprime to Q, so the
exceptional contribution is `−(x^{β*−1}/β*)μ_ψ` with `x^{β*−1}/β*≤2`
(β*>1/2). Other i: `|λ_i−1|≤2E_2`. Errors `≤M_1(2C_0E_1+2E_2)` since `λ_i<2`.
I agree with the proof. Note the theorem does **not** depend on the number of
cells, only on `M_1, μ, Z`; so the astronomically many cells of B are harmless.

**Interface (OMEGA8 Thm 3.4 → PO Thm 4.1).** Checked item by item:

* *Unit cells, `gcd(b_i,d_i)=1`.* A_i are single-value cells on ≤k free
  coordinates `X_ℓ∈(ℤ/ℓ^{e_ℓ})^×`; `u_j=Σ_W c_W E[F^{(j)}|X_W]` is a
  combination of unit cells on W. Products of unit cells are unit cells or
  empty. ✓ (B also has the constant term 1, cell `d=1`.)
* *`gcd(d_i,Q)=1`.* Every `d_i` is a product of `ℓ^{e_ℓ}`, ℓ free (z<ℓ≤T,
  ℓ∉𝓑), and Q_Π is supported on Π. ✓ With the auxiliary ℓ_0∈(R,2R] (R ≥ T,
  ≥ max d_i) still coprime. ✓
* *Positivity.* `μ=E_Haar B ≥ δ−E[F−B] ≥ 0.99δ>0` (μ:=Σc_i/φ(d_i) equals the
  Haar mean over units mod lcm d_i). ✓
* *Twist.* For real primitive ψ, conductor f, `gcd(f,Q)=1`, f | some d_i:
  `Σ_{i:f|d_i}c_iψ(b_i)/φ(d_i) = E_Haar[Bψ]`, because for a unit cell
  `(b,d)` the Haar sum of ψ over `x≡b (d)` is `ψ(b)/φ(d)` if f|d and **0** if
  f∤d (otherwise ψ would be trivial on `ker((ℤ/lcm)^×→(ℤ/d)^×)` and factor
  through d). So Lemma 3.3's `μ_ψ` is PO's `μ_ψ`. f is odd (840|Q) and all
  its primes are free, so a free ℓ_0|f exists with `ψ_{ℓ_0}` = Legendre mod
  ℓ_0 lifted to `(ℤ/ℓ_0^{e})^×`, mean zero. ✓ (Numerically checked on toys,
  §6.)
* *Lemma 3.3 constants.* Conditional LLL (HSS): neighbours of `E∖ℓ_0`
  (≤k−1 primes) have `Σx ≤ 2(k−1)/(64k) < 1/32`, `∏(1−x)^{−1} ≤ e^{0.033}
  ≤ e^{1/16}` ✓; `1.07·w_{ℓ_0} ≤ 1.07/64 ≤ 0.017` ✓; `0.01+0.021<1/4` ✓.
* *Modulus size.* Cells on ≤3k+2t free primes, each `ℓ^{e_ℓ}≤T`:
  `log d_i ≤ (3k+2t)𝓛` ✓. `log Q_Π ≤ (π(z)+|𝓑|)𝓛+log 24` ✓.
  `x≥Z^{12}` is absorbed in `C_1≥12`. Linnik range (`log x ≫ K log Z`, not
  `(log Z)^2`) is what TZ gives ✓.
* *K.* `log μ^{−1} ≤ 2.07S+0.01` (LLL with `x_E=2P(E)≤1/32`:
  `−log(1−x)≤1.04x`), `log M_1 ≪ log m + t log N + (k+t)𝓛 ≪ (k+t)𝓛`
  (m≤T^{k+2}, N≤T). So `K ≤ 4S*+C'(k+t)𝓛` ✓.
* *(I) on the class.* `F ≤ 1[W>T]` on n≡1 (Q_Π) — see §2.

Verdict (1): **SOUND**, with the minor defects D1–D3 below.

## 2. Haar-side inputs: O2 Lemma 4.3 (I), Lemmas 11.1–11.2, Thm 11.3, ET Prop 1.4

**(I) for an arbitrary quarantine Π.** Re-derived: for n≡1 (Q_Π), Q_Π =
lcm(24, ℓ^{e_ℓ}: ℓ∈Π), and `M≤T`, `M≡3 (4)`: the Π-part m of M divides Q_Π
(each `ℓ^v‖M` has `ℓ^v≤T`, so `v≤e_ℓ`), so n≡1 (m). If r=1, Fact 1.1. If
`n≡−4D (M)`, `D|A_M²`, then `m|4D+1` (survival) and `n≡−4D (r)` (the event
occurs). Only "Π-part divides Q_Π" is used, so (I) holds verbatim for the
output of Lemma 11.2 (any Π). The events are unit single-value conditions
(`gcd(D,M)=1` since `gcd(A,M)=1`). Supports: primes `>z` dividing `r≤T`
number at most `k=⌊𝓛/log z⌋` ✓. **SOUND.**

*From scratch* (`scripts/review_o8b_quarantine.py`, output
`data/review_o8b/quarantine.txt`): (a) `{−4D: D|A²} = {−uv^{−1}: uvw=A}`
(the blind51 (B1.1) witness definition) and `1∉𝓡(M)` for all M≤2000;
(c) actual integers n≡1 (Q_Π) built by CRT, W(n) computed by brute force over
all M≤T: in 5 configurations (T=3000–5000, z∈{3,5,7,11}, c_0 = 1/(64k) and
larger, supports up to 2) all 510 forced survivors have W(n)>T, and on 1500
unconditioned samples `[no event] = [W(n)>T]` with 0 mismatches.

**Lemma 11.1 (S*).** Re-derived: survival forces `m_Π | g:=gcd(M,4D+1)`;
`D↦A²/D` preserves g (in ℤ/g, `D≡−1/4`, `A≡1/4`, so `4A²/D≡−1`); with
`D=sr'²≤A=sr'k`: `g | 4sr'(r'+k)` and `gcd(g,4sr')=1`, so `g|r'+k`; least k
is `≥g/2`, k-sum `≤(3+log X)/g`. ✓ Numerically S* (exact max over all Π,
per atom) is 38.9 (T=3000), 43.5 (4000), 47.1 (5000), far below the majorant
(even without the `C log log T` factor). **ET Prop 1.4** read in
`sources/elsholtz-tao-1107.1010.pdf` (p. 4): `Σ_{a≤A,b≤B}τ(kab²+1) ≪
AB log(A+B) log(1+k)` for `A,B>1`, `k≪(AB)^{O(1)}` — matches PO Lemma 9.2's
quotation; dyadic blocks (`O(𝓛²)` of them, each `O(𝓛)` with k=4) give
`Σ τ(4sr'²+1)/(sr') ≪ 𝓛³`, hence `S*≪𝓛^4 log𝓛` ✓. (Effectivity of ET's
constant: ET's proof is an Erdős-type elementary argument; I did not check
effectivity line by line — Thm 4.3 correctly makes effectivity conditional
on it.)

**Lemma 11.2 (iterated quarantine).** Re-derived: a prime added at stage i
has `c_0<w_ℓ(Π_i) ≤ Σ_{atoms surviving Π_i, ℓ|r} 1/φ(r) ≤ Σ_{atoms, ℓ|M, ℓ>z}
(S*-contribution)`; each atom has ≤k primes >z, and each ℓ is added once, so
`|𝓑|c_0 < kS*`. Termination: Π only grows within a finite set. At the end all
free ℓ have `w_ℓ≤c_0` ✓. Numerically `|𝓑|` ≤ kS*/c_0 and final
`max w_ℓ ≤ c_0` in all runs ✓. With c_0=1/(64k): `|𝓑|≤64k²S*` ✓.

**Thm 11.3 / the LLL lower bound used in Thm 3.4.** With `x_E=2P(E)`,
`P(E)≤w_ℓ≤c_0`, neighbourhood sum `≤2kc_0` (=1/32 for c_0=1/(64k)); then
`δ ≥ ∏(1−2P(E)) ≥ e^{−2.07S}` (`−log(1−x)≤1.04x` for x≤1/32) ✓ —
numerically `log∏(1−2P) ≥ −2.07S` in all runs. O2's arithmetic
`log(1/δ*) ≤ (π(z)+8k²S*)𝓛+4S* ≪ 𝓛³+𝓛³S*/(log𝓛)²` with z=𝓛² ✓.

**What OMEGA8 needs from Π** — supports ≤k, `w_ℓ≤1/(64k)` for all free ℓ,
`S≤S*`, (I), `840|Q_Π` (z≥7), `log Q_Π≤(π(z)+64k²S*)𝓛+log 24` — all
delivered. Verdict (2): **SOUND.** (Minor: D4.)

## 3. Definition chain and the conversion to `(log p)^{1/14}`

**Definitions.** PO §0: `A_M=(M+1)/4`, `𝓡(M)={−4D mod M: D|A_M²}`,
`W(n)=min{M≡3 (4): n mod M∈𝓡(M)}`. This agrees with the multiplier-witness
definition blind51 (B1.1) `min{M: (M+1)/4=uvw, pv≡−u (M)}`: `v^{−1}≡4uw`
gives `−uv^{−1}≡−4u²w`, and every `D|A²` is `u²w` with `uvw=A` (per prime:
`d≤a`: x=0,z=d,y=a−d; `d>a`: x=d−a, z=2a−d, y=0) — checked by brute force
for all M≤2000 (§2 script, part (a)). "Hard" = one of Mordell's six classes
mod 840, contains 1 mod 840. `L_h(T)=min{p>T prime, p≡1 (24), W(p)>T}`
(notes l. 21604).

**Produced primes.** Π ⊇ {ℓ≤z}, z=𝓛²≥7, so `840 | Q_Π` and every
`p≡1 (Q_Π)` is ≡1 (840) (Mordell-hard) and ≡1 (24); `p>Q_Π>T` (already
`5^{e_5}7^{e_7}>T²/35`), so the auxiliary ℓ_0 is not even needed for `p>T`.
PO Thm 4.1 returns a **prime** p≡1 (Q_Π ℓ_0) with `B(p)>0` for some such p,
hence `W(p)>T` ✓, so `L_h(T)≤p` ✓.

**Exponents (re-derived; `scripts/review_o8b_exponents.py`,
`data/review_o8b/exponents.txt`).** With z=𝓛²: `k≤𝓛/(2log𝓛)`,
`b≍𝓛`, `k_0 ≍ S + k𝓛 ≪ 𝓛^4log𝓛` (ET), so `t=2C_Hkbk_0 ≪ (𝓛/log𝓛)·𝓛·𝓛^4log𝓛
= 𝓛^6` (the logs cancel); `K ≪ S*+(k+t)𝓛 ≪ 𝓛^7`;
`log Q_Π ≤ (π(𝓛²)+64k²S*)𝓛+log24 ≪ 𝓛^7/log𝓛`; `log Z ≤ log Q_Π + log ℓ_0 +
log max d ≪ 𝓛^7`; `log p ≤ C_1K max(log Z,K) ≪ 𝓛^{14}`. Then `𝓛 ≥
(log p/C)^{1/14}` and `W(p)>e^𝓛 ≥ exp(c(log p)^{1/14})`, `c=C^{−1/14}` ✓.
Numerically (all absolute constants =1, C_H=5, worst case S=S*), the ratios
`log t/log𝓛, log K/log𝓛, log log Z/log𝓛, log log p/log𝓛` are
`6+4.1/log𝓛, 7+6.2/log𝓛, 7+5.5/log𝓛, 14+12.4/log𝓛` at every 𝓛 from 10³ to
10³⁰ — i.e. exactly `𝓛^6, 𝓛^7, 𝓛^7, 𝓛^{14}` up to absolute constants, no
hidden `log𝓛` powers and no parameter-dependent constants ✓.

Verdict (3): **SOUND** (minor D2).

## 4. Thm 4.4 (modulo Thorner–Zaman only)

Unconditionally `S* ≤ C log𝓛(3+𝓛)(1+𝓛)²τ*(4T+1)` and Wigert
(`log τ(n) ≤ (log2+o(1))log n/log log n`) give `log S* ≤ (log2+o(1))𝓛/log𝓛`.
Every quantity in §3 is `≤ 𝓛^{O(1)}(S*+1)` (t ≪ k𝓛(S+k𝓛), K, log Z), so
`log p ≪ 𝓛^{O(1)}S*²`, `log₂p ≤ 2log S*+O(log𝓛) ≤ (2log2+o(1))𝓛/log𝓛`.
`x/log x` increasing ⇒ `𝓛 ≥ (1−o(1))·(log₂p/(2log2))·log log₂p`, i.e.
`log W(p) > 𝓛 ≥ (1/(2log2)−o(1))log₂p·log₃p` ✓. Numerically (log-space,
Wigert main term) `𝓛/(log₂p·log₃p)` decreases 0.866 → 0.741 for
𝓛=10⁴…10⁸⁰ towards `1/(2log2)=0.7213` from above ✓ (convergence is slow, as
expected of `log₃`). Inputs: TZ, Wigert (classical), LLL + its conditional
form, Håstad/LMN (textbook). No ET. The label "modulo Thorner–Zaman only" is
correct. It beats O4 Cor 3.2 (`log₂p·log₄p/log₅p`) ✓.

Verdict (4): **SOUND.**

## 5. Defects

**D1 (MINOR; PO Thm 4.1 hypothesis vs OMEGA8 Thm 3.4).** PO Thm 4.1 asks for
`B(n)≤1[W(n)>T]` for **every** integer n≡1 (Q). OMEGA8 proves `B≤F` only on
unit residue vectors (Lemma 3.1 is over `X_ℓ∈(ℤ/ℓ^{e_ℓ})^×`); for n≡1 (Q)
divisible by a free prime the cell expansion of B is evaluated at a
non-unit and nothing is proved. Harmless: the proof of PO Thm 4.1 evaluates B
only at primes `p≡1 (Q)`, `p>Q>T≥` every free prime. *Repair:* in Thm 3.4's
proof say "B≤1[W>T] for every n≡1 (Q_Π) coprime to all d_i, which is all PO
Thm 4.1's proof uses (it evaluates B at primes p>Q)"; or weaken PO Thm 4.1's
hypothesis accordingly (campaign-wide nit, the O2–O4 minorants have the same
feature).

**D2 (MINOR; Thm 3.4 display, log Z).** With the auxiliary prime
`ℓ_0∈(R,2R]`, `R=max(T,max d_i)`, `log Z = log Q_Π + log ℓ_0 + log max d_i
≤ log Q_Π + 2(3k+2t)𝓛 + log 2`, not `log Q_Π + (3k+2t+2)𝓛`. No effect on any
exponent. *Repair:* write `2(3k+2t+1)𝓛`, or drop ℓ_0 altogether (it was
only used in O2/O3 to force `p>T`, which here already follows from
`Q_Π>5^{e_5}7^{e_7}>T`; all `μ, M_1, μ_ψ` are unchanged either way).

**D3 (MINOR; notation).** "ℓ_0" denotes both a prime dividing the
conductor f (Lemma 3.3) and the auxiliary prime of O4 Thm 2.1 (Thm 3.4
proof). *Repair:* rename the auxiliary one (e.g. `ℓ_aux`).

**D4 (MINOR; Haar-side citation).** Header item 1 and the Comparison
paragraph state the Haar side as `log(1/δ*) ≪ 𝓛^7 log𝓛`; O2 Thm 11.3 proves
`≪ 𝓛^7/log𝓛` (its `8k²S*𝓛` with `k≤𝓛/(2log𝓛)`, `S*≪𝓛^4log𝓛`). The
statement is weaker than what is proved, so not wrong, but "the prime side
costs its square" should compare `𝓛^{14}` with `(𝓛^7/log𝓛)²`. *Repair:*
quote O2's `𝓛^7/log𝓛`.

**D5 (MINOR; Thm 3.4, `m` and splitting).** Splitting distinct events into
single values mod `ℓ^{e_ℓ}` can create *duplicate* single-value events (e.g.
`n≡a (ℓ)` and `n≡a' (ℓ²)` with `a'≡a (ℓ)` share values). Nothing breaks
(Lemma 3.1 does not need distinctness, the LLL tolerates duplicates, and the
split mass still equals the pre-split mass ≤ S*), but the text says "the
distinct surviving events, split" and then treats `E_1,…,E_m` as a list.
*Repair:* one sentence: "duplicates are kept (or merged); either way the
total mass is ≤S and per-prime masses ≤c_0".

## 6. Scripts and data (from scratch; none of the author's code used)

* `scripts/review_o8b_quarantine.py` → `data/review_o8b/quarantine.txt`:
  𝓡(M) ↔ uvw witness set, Fact 1.1, iterated quarantine (Lemma 11.2
  bounds, final `w_ℓ≤c_0`), exact S* (max over all Π per atom) vs
  `S_tot(Π)`, LLL premise, and (I) on CRT-built integers with brute-force
  W(n) (510 forced survivors + 1500 random samples, 0 mismatches).
* `scripts/review_o8b_interface.py` → `data/review_o8b/interface.txt`:
  `μ=E B`, `μ_ψ=E[Bψ]` for random unit-cell combinations incl. prime-power
  moduli (err ≤ 5e−16); the M_1 product inequality; Lemma 3.2's `c_W`
  formula for the Efron–Stein truncation; toy BRW systems on units mod
  31·37·41·43 with `w_ℓ≤1/(64k)`: `B≤F`, Lemma 3.3 chain, twist ≤ 0.005μ.
* `scripts/review_o8b_exponents.py` → `data/review_o8b/exponents.txt`:
  exponent bookkeeping for Thm 4.3 (ratios → 6, 7, 7, 14) and Thm 4.4
  (→ 1/(2log2) from above).

Replay: `PYTHONPATH=scripts uv run python scripts/review_o8b_quarantine.py
3000 5 100 300 4 0.5` (≈1 min; other configurations as in the data file),
`uv run --with numpy python scripts/review_o8b_interface.py 3 1 60`,
`uv run python scripts/review_o8b_exponents.py`.
