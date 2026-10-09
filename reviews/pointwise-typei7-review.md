# R109 — hostile review of POINTWISE_TYPEI7.md (O109, 2-adic closeness to `w = 9`)

Reviewer: side agent R109 (branch `side-agent/review-typei7`), merged `side-agent/sign-point-2adic`.
From-scratch scripts (no author code imported): `scripts/review_typei7_check.py` (certificate checker straight
from the TYPEI2 §0/§3 definition, Thm 2.1/2.4/Rem 2.1(b)/Comp 2.5 numerics), `scripts/review_typei7_lemma11.py`
(direct divisor enumeration of `N = 1+4ck²`, `ck ≤ X`, and brute-force test of Lemma 1.1 / (1.2)). Second-engine
re-runs of grid cells with R89's `review_typei4_jsearch.c` (independent of the author's `typei4_lb.c`).

## Summary verdicts

| Claim | Verdict |
|---|---|
| Criterion (top), Lemma 1.1, (1.2), cofactor clause | SOUND |
| Thm 2.1 (unbounded closeness, `F = 7^s+2^i`) | SOUND |
| Remark 2.1(a),(b) | SOUND |
| Comp 2.2 | SOUND (replayed from scratch) |
| Cor 2.3 (covered part open dense) | SOUND; one MINOR overstatement in the "upgrades Prop 4.1" sentence |
| Thm 2.4 (`F = 71^ν`, `k = 2^γ`) | SOUND |
| Comp 2.5 | SOUND (rows ν = 1, 3, 7, 15, 143 replayed; `ν` and closeness for all m = 4..14 replayed) |
| Comp 3.1 / Cor 3.2 / Comp 3.4 | SOUND as CERTIFIED-once-replayed; see §3 below for the extra second-engine cells |
| Obs 3.3, §4 (labels EVIDENCE / Assessment) | SOUND (numbers re-derived) |
| §5 labels | SOUND-AFTER-REPAIRS (MINOR wording, applied) |

No FATAL or MAJOR defect found.

## 1. Criterion and Lemma 1.1

Re-derived from TYPEI2 (2.2) + §3. At `x̂_w` the odd components are `±1`, so `(c,k,F)` is a certificate iff
`F | 1+4ck²`, `F ≡ −1 (mod c'k')`, `F ≡ 1 (mod 7^{v_7(ck)})`, `F ≡ −w (mod 2^{v_2(4ck)})`, `(F,4ck)=1`, `v_7(c)` odd.
Only the last congruence and `v_2(4ck) = 2+α+γ = t` depend on the split `α+2γ = L`; `N` depends on `L` only. So
"some split" ⟺ minimal `t = 2+⌈L/2⌉` (`γ = ⌊L/2⌋`). ✔

`e ≡ F (mod n)` (both `≡ −1` mod `c'k'`, both `≡ 1` mod `7^{a+b}`, and `e ≡ F^{−1}`), and
`e ≡ F^{−1} (mod 2^{L+2})` with `v_2(1−F²) = 1+3 = 4` for `F ≡ 7 (16)`, so `v_2(e−F) = 4` (`L ≥ 3`). ✔
Identity: `(G−9)² + 16nδ(G−9) − 1 = G(G−18+16nδ) + 80 − 144nδ`, and LHS `= 2^{L+2}c_ok_o²`, hence
`G(G−18+16nδ) = −16E` with `E = 5 − 9nδ − 2^{L−2}c_ok_o²`. ✔ `16 | G` ⇒ `v_2(G−18+16nδ) = 1`. ✔
(Also `E ≠ 0`, since both factors on the left are non-zero — implicit, harmless.)
(1.2): `⌈L/2⌉−1 ≤ L−2` for `L ≥ 2` ✔; `5·9^{−1} ≡ 285 (2^9)`, `≡ 797 (2^{10})` ✔ (script).
Cofactor: `δ ↦ −δ` ✔.

*Numerical (from scratch).* `review_typei7_lemma11.py 400000`: direct divisor enumeration finds 64 oriented fibre
certificates (`L ∈ {11,14,16,18,21,27}`, 9 distinct `(L,b,{F,e})`). For each: `v_2(F+9) = 3+v_2(E)` and the cofactor
version; for **every** split the direct TYPEI2 test `cert_at(c,k,F,9)` agrees with the congruence mod `2^{t−3}`; and
for every `1 ≤ j ≤ L−2`, `v_2(F+9) ≥ j+3 ⟺ nδ ≡ 5·9^{−1} (2^j)` (so the positive side of the "iff" is exercised at
small `j`). 1442 checks, 0 failures. All 9 pairs occur in the author's complete `typei4_lb` lists of the same cell.

MINOR m1 (no repair needed). Lemma 1.1 lists "`nδ` odd" as a hypothesis; the proof never uses it (only `16 | 16nδ`).
Harmless.
