# z15_other_sterile_families — 7·4^s + 9, 15·2^s + 1, 63·2^s + 1, 255·2^s + 1 under window menus (O240)

## Idea
Run the hybrid ET + exponential-window machinery on the other PROVED ET-sterile families ((J)22 Cor 1.5, (J)68 Lemma 3.1).
## Results (EVIDENCE)
* 7·4^s + 9: SG window m = 19 covers the μ = 0 neighbourhood (s ≡ 0 mod 90); left: s ≡ 20 (mod 90) partly — at
  L* = 128520 only 2 of 1785 lifts remain (s ≡ 8570, 104960); windows firing there have periods 99, 1329, 7158.
* 15·2^s + 1, 63·2^s + 1, 255·2^s + 1: no SG window found firing at μ = 0 within t ≤ 301 / 15 (finite menu, Prop 4.3); μ = 0 open for richer menus.
* 23·4^s + 41, 31·4^s + 33, 7·4^s + 57: at L = 360 few windows are periodic; residuals unchanged (not pursued).
## Literature
EXP_NEAR_SQUARE (J)68; EXPONENT_COVERING (J)22.
## Barrier screen
As z15_proth_sophie_germain; T1 automatically respected.
## Cheap numerics
`z15_hybrid_exp.py c k beta L Mmax JMAX TMAX EMAX`, `z15_tree.py 7 9 2 360 128520 3000 12 5 9`, `z15_rules_at.py`.
## Assessment
EVIDENCE. At L* = 128520·11 the two stuck residues reproduce themselves (one lift each survives): self-similar stuck nodes; 7·4^s + 9 not decided.
