# Referee report R33b — paper/es-subexp-note.tex, Draft v2 (branch side-agent/omega-paper-v4)

Referee: hostile side agent (R33b). Scope: everything changed/added in v2.
Status: IN PROGRESS (written incrementally).

## Verdicts per claim (filled in as checked)

### Thm 4.1 (linear transfer), proof as written — line-by-line
- Character expansion c(χ)=E_D[B χ̄_D]/φ(Q): re-derived (sum over n≡1 mod Q
  units of QD, χ̄_Q(1)=1, CRT gives φ(D)/φ(QD)=1/φ(Q)). CORRECT.
- (a) conductor support: χ_D trivial on ker((Z/D)^×→(Z/d_i)^×) ⇔ χ_D factors
  mod d_i ⇔ cond(χ_D) | d_i. cond(χ) = cond(χ_Q)cond(χ_D) ≤ Q d_i ≤ Z. CORRECT.
- (b) |c(χ)| ≤ E_D|B|/φ(Q), c(χ_0)=μ/φ(Q). CORRECT.
- (c) twisted coefficient = μ_ψ/φ(Q) (cells with f∤d_i vanish by (a)). CORRECT.
- ≤ Z² characters: χ↦χ* injective at fixed modulus QD, #primitive mod q ≤ φ(q),
  Σ_{q≤Z}φ(q) ≤ Z². CORRECT.
- log(QD) ≤ 2Z: log Q ≤ Q, log D ≤ ψ(max d_i) < 1.04 max d_i (Rosser–Schoenfeld;
  citation not given — MINOR), sum ≤ 2Q·max d_i. CORRECT.
- |R_1| ≤ 2AZ³μ/φ(Q). CORRECT.
- Case 0 numerics: C_G A e^{-L} ≤ A/(400(A+1)) < 1/400; second term ≤ 1e-4. CORRECT.
- Exceptional case: u<L, u ≤ min(u,1)L (L≥2), Le^{-3L}≤e^{-L}. CORRECT.
- Case A: λ ≥ (1-e^{-1}-2/16)min(u,1) = 0.507 min(u,1). CORRECT (checked numerically,
  scripts/review_r33b_numerics.py). 1/λ ≤ 2+2/u ≤ 2+c_2 Z^{1/2}(log Z)²/8 uses
  q_1 | Q ≤ Z and Page bound. CORRECT given Thm 3.1.
- Case B: |c x^β/β| ≤ (μ/4φ(Q))·2x. CORRECT.

### Thm 3.2 (Gallagher) vs source — SOUND (statement), caveat paragraph needs repair
Checked against sources/omega9/montgomery-mnt3.pdf, Thm 28.19 (pp. 229–232 of the
draft incl. proof). The quoted statement matches verbatim: hypotheses κ≥κ_0,
1<Q^{6c}≤x (NO upper bound on x — so the choice Q_G=x^{1/(κL)} with L unbounded
is legitimate), main RHS, exceptional replacement θ(x;χ_1)+x^{β_1}/β_1 (sign
correct w.r.t. the explicit formula), replaced RHS. The implied constant may
depend on κ (proof ends with exp(c/κ')), so "≪_κ" is right.
The proof's case split is at 1-β<1/(κ_0 log T)=1/(3κ_0 log Q) (Case 1) vs
1-β_1<1/(κ' log T)=1/(κ log Q) (Case 2). Re-derived: Case 2 as printed works for
ANY real zero with 1-β_1<1/(κ_0 log T) (its last step needs only
log(κ_0/c_0)≥3c, guaranteed by (28.91)); and for κ≥3κ_0, if such a zero has
1-β_1 ≥ 1/(κ log Q), the Case-2 bound plus x^{β_1}/β_1 ≤ 2x e^{-log x/(κ log Q)}
and (1-β_1)log x·e^{-log x/log Q} ≤ (log x/log Q)e^{-log x/log Q} ≪ e^{-log x/(2 log Q)}
yields the non-exceptional bound. So the theorem holds for every κ≥3κ_0.
