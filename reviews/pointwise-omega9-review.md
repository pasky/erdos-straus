# Review R34a (reviewer 1 of 2): POINTWISE_OMEGA9.md — Theorem 1.1 (linear transfer)

Reviewer: side-agent/review-omega9a. Reviewed: branch `side-agent/omega9-exponent` at `9a21ffc`.
Scope: Thm 1.1 line by line, the quotation of (G) = MV III Thm 28.19, Cases 0/A/B, final inequality.
From-scratch scripts: `scripts/review_o9a_*.py`.

## Summary verdicts
(filled in at the end)

## 1. The quotation of (G) (MV III Thm 28.19, pp. 229–232 of the archived PDF)

Checked against `sources/omega9/montgomery-mnt3.pdf` (pdftotext; the SHA-256 in the README was
not re-verified by me beyond the file being the one present in the branch).

MV III Thm 28.19 (Gallagher), verbatim content: there are constants `c ≥ 1`, `κ_0 ≥ 3` such that if
`κ ≥ κ_0` is a constant and `1 < Q^{6c} ≤ x`, then
`Σ_{q≤Q} Σ*_{χ mod q} |ϑ(x;χ) − E_0(χ)x| ≪ x exp(−log x/(κ log Q)) + (log x/log Q)^2 x Q^{-1}`,
unless `F(s,Q)=∏_{q≤Q}∏*_χ L(s,χ)` (28.89) has an exceptional real zero `β_1` with
`1−β_1 < 1/(κ log Q)`, in which case the term of `χ_1` is replaced by `ϑ(x;χ_1)+x^{β_1}/β_1` and
the RHS by `(1−β_1)(log x)[x exp(−log x/log Q) + x log x/(Q log Q)]`.

* Author's transcription (OMEGA9 §1, "Cited input (G)"): **matches**, including the repaired
  exceptional RHS (prefactor `(1−β_1)log x` multiplying both terms; `exp(−log x/log Q)` without κ).
  The sum ranges over `q ≤ Q` including `q=1` (trivial character mod 1, `E_0=1`), as the author says.
* "unique, real" exceptional character: not in the theorem statement itself, but supplied by MV's
  "Exceptional Zero Statement" (28.61)–(28.62), p. 216 (at most one zero with `Re s > 1−c_1/log T`,
  real, χ_1 quadratic). OK provided `κ ≥ 1/c_1` — which MV's choice `κ_0 = 3max(c, c_1, …)` does
  NOT obviously ensure (c_1 vs 1/c_1); see minor m1.
* Page bound: MV (28.62) gives `1/(c_2 q_1^{1/2}(log q_1)^2) ≤ δ_1`, as quoted. OK.
* Effectivity: the statement does not say "effective", but §28.7 (p. 217) explicitly states that the
  setup is chosen to keep c_1 computable "especially in connection with bounding the least prime";
  all inputs (28.14, 28.15, 28.62) are effective. The author's "absolute effective" is acceptable.
* Uniformity in κ: the implied constant is uniform for κ ≥ κ_0 (proof: `c/κ' ≤ 1`). The author fixes
  κ, so no issue.
* Source quality: MV III is an unpublished course draft and its proof of 28.19 has visible internal
  slips (minor m2). The statement is the standard Gallagher (1970) Thm 7 shape; the original was not
  obtained by the author nor by me. Label "PROVED modulo (G)" is the right one.

**Verdict on (i): SOUND** (quotation exact, modulo minors m1, m2).

## 2. Character expansion (items 1–3, `S(x)`, `R_1`)

Re-derived. Since `gcd(Q,D)=1`, CRT gives `Σ_{n∈G} f(n)χ̄(n) = Σ_{b mod D} B(b)χ̄_D(b)` for every
`χ_Q`, hence `c(χ)=E_D[Bχ̄_D]/φ(Q)` (all `φ(Q)` choices of `χ_Q` occur with equal coefficients).
`E_D[1[n≡b_i (d_i)]χ̄_D]=0` unless `χ_D` factors through `(ℤ/d_i)^*`, i.e. `cond χ_D | d_i`. Hence
`cond χ ≤ Q·d_i ≤ Z`. Injectivity of `χ ↦ χ*` for fixed modulus QD is standard; count
`≤ Σ_{q≤Z}φ(q) ≤ Z²`. `μ=Σc_i/φ(d_i)=E_D B` (PO's definition) and PO's
`μ_ψ=Σ_{f|d_i}c_iψ(b_i)/φ(d_i)=E_D[Bψ]` for primitive ψ mod f, f|D. `|ϑ_{QD}(x;χ)−ϑ(x;χ*)| ≤ log(QD)`,
`log(QD) ≤ 2Z` (Rosser–Schoenfeld ψ(y)<1.04y), so `|R_1| ≤ 2Z³Aμ/φ(Q)`, which is
`≤ μx/(400φ(Q))` once `x ≥ 800AZ³`.

From-scratch check `scripts/review_o9a_charexp.py` (sympy; ALL characters mod N=QD built from
prime-power generators, conductors by brute force): on 40 random instances (Q∈{3,4,5,7,8}, 1–3 moduli
d_i ≤ 39, random real c_i, N ≤ 700) every assertion holds: coefficient identity, conductor support
`cond χ_D | d_i`, `cond χ ≤ Z`, `|c(χ)| ≤ E_D|B|/φ(Q)`, `c(χ_0)=μ/φ(Q)`, injectivity of χ↦χ* on the
support, `μ_ψ(PO) = φ(Q)c(χ)` for real χ with nontrivial χ_D, `#supp ≤ Z²`.

**Verdict: SOUND.**

## 3. Case 0 and the final inequality (the crux)

The key point is correct: (G) bounds the **sum** of `|ϑ(x;χ)−E_0x|` over **all** primitive χ of
conductor `≤ Q_G` (about `Q_G²` of them), so after pulling out `max|c(χ)| ≤ Aμ/φ(Q)` the number of
supported characters never multiplies the zero-density error; it enters only `R_1` (trivial
`log(QD)` per character), which is polynomial in Z and absorbed by `x ≥ Z^{C_2}`. This is exactly
Linnik's theorem with weights; no `max_y` is needed (only the single x is used).

Constants re-checked by hand: `C_G A e^{−L} = e^{−2c}A/(400(A+1)) < 1/400`;
`C_G A(κL)²/Q_G ≤ A/(10^4(A+1)) < 1/400`; sum `< 1/200` ✓. Side conditions: `κL ≥ 3·2c ≥ 6c` gives
`Q_G^{6c} ≤ x` ✓; `Q_G ≥ Z ≥ Q ≥ 2` ✓; `A ≥ 1` automatically (|B|≥B), so `1+log A ≥ 1`.
`A ≤ Z^{1/4}` is genuinely needed (else `Q_G ≥ C_G A` fails for `log A ≫ log Z`) and is assumed.

From-scratch check `scripts/review_o9a_params.py`: with `L=2c+log(400C_G(A+1))`,
`log Q_G=log x/(κL)`, `log x=C_2(1+log A)log Z`, it computes the least C_2 meeting every side
condition (incl. the Case-A `R_1` condition with Page, see m4) and verifies both error ratios
(`≤1/200`, `≤1/100`), over a grid `2 ≤ Z ≤ e^{700}`, `1 ≤ A ≤ Z^{1/4}`. The required C_2 is bounded
uniformly in (A,Z) (e.g. 617 for C_G=1,c=1,κ=3,c_2=1; 1.2·10^5 for C_G=10^9,c=5,κ=50,c_2=10^6), i.e.
C_2 depends only on (C_G, c, κ, c_2): **absolute**, as claimed. No constant secretly depends on Z,
A, the number of cells, M_1 or K.

**Verdict: SOUND.**

## 4. Exceptional case (Cases A, B)

* `u=(1−β_1)log x < L` since `1−β_1 < 1/(κ log Q_G) = L/log x` ✓. Replaced RHS of (G) is
  `C_G u x[e^{−κL}+κL/Q_G]` ✓ (`log x/log Q_G = κL`). With `u = min(u,1)max(u,1)`, `max(u,1) ≤ L`
  (L ≥ 2), the bound `≤ min(u,1)·μx/(200φ(Q))` follows from `2C_G A L(e^{−κL}+κL/Q_G) ≤ 1/100` ✓
  (`e^{−κL} ≤ e^{−L}e^{−2L}`; `2C_GAL·κL/Q_G ≤ 2A/(10^4κ(A+1))`).
* If χ_1 is not some χ*, χ_1's term is simply absent from our subsum ✓. Otherwise exactly one χ
  (injectivity) ✓; c(χ) real ✓.
* **Case A** (χ_D trivial, χ*=χ_Q*=χ_1, q_1 | Q): `c(χ)=μ/φ(Q)` ✓, `λ=1−e^{−u}/β_1` ✓.
  `λ ≥ min(u,1)/2` for `log x ≥ 16`: TRUE; from-scratch grid `scripts/review_o9a_lambda.py`
  (log x ∈ [16,10^8], u ∈ [10^{−12}, log x/2]) gives `min λ/(min(u,1)/2) = 1.215` (at u=1, log x=16).
  But one step of the written justification is wrong (m3). The (G) error `≤ λμx/(100φ(Q))` ✓.
  `R_1`: with `q_1 ≤ Q ≤ Z` and MV (28.62), `λ ≥ min(8/(c_2Z^{1/2}(log Z)²), 1/2)`; the needed
  inequality is then `x ≥ 400c_2 A Z^{7/2}(log Z)²/16`, not `x ≥ C·A·Z³` as written (m4). Harmless,
  since `x ≥ Z^{C_2}`; included in my C_2 computation above.
* **Case B** (χ_D nontrivial, real, induced by primitive ψ of conductor f>1, `f | D`, `gcd(f,Q)=1`,
  and `f | d_i` for some i by item 1): `c(χ)=μ_ψ/φ(Q)`, twist condition `|μ_ψ| ≤ μ/4`,
  `x^{β_1}/β_1 ≤ 2x` ✓. Total: `S ≥ (μx/φ(Q))(1−1/2−1/200−1/400) > 0` ✓.
* Conclusion `S(x)>0 ⇒ ∃p≤x, p≡1 (Q), p∤QD, B(p)>0 ⇒ W(p)>T` uses the hypothesis on `n≡1 (Q)`
  coprime to all d_i ✓ (weaker than PO's hypothesis, fine).

**Verdict: SOUND (after minors m3, m4).**
