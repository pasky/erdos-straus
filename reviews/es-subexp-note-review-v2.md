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
