# Hostile review R30b of POINTWISE_OMEGA8.md (O30) — reviewer 2 of 2: inputs and interface

Reviewer branch `side-agent/review-omega8b`, merged `side-agent/haar-primes-2`
(ff). Scope (per task): (1) transfer via PO Thm 4.1 / Thorner–Zaman,
(2) O2 Lemma 4.3 (I), Lemmas 11.1–11.2, Thm 11.3 and the iterated quarantine,
(3) definition chain W(p), Mordell-hard, L_h(T), exponent bookkeeping to
`(log p)^{1/14}`, (4) Thm 4.4 asymptotics. The BRW sandwich / switching-lemma
machinery (Lemmas 3.1, 4.1) is the other reviewer's; I use it only at the
interface. From-scratch scripts: `scripts/review_o8b_*.py`.

(Work in progress; sections are appended claim by claim.)

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
  §5.)
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
