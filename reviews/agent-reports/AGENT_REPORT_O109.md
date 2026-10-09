# AGENT REPORT O109 — 2-adic closeness of fibre certificates to `w = 9` (sign point `x̂_9`)

Branch `side-agent/sign-point-2adic`. Deliverable: `POINTWISE_TYPEI7.md`; scripts `typei7_tab.py`, `typei7_xcheck.py`,
`typei7_unbounded.py`, `typei7_dense71.py`, `typei7_family.py`. Not reviewed.

## Outcome (one line)
A **precise negative result**: the requested bound on `v_2(F+9)` in terms of a fixed 2-adic precision does not exist — the
closeness is unbounded and the covered part of the fibre is open dense (PROVED, explicit certificates). The only bound that
would suffice, `v_2(F+9) < 2+⌈L/2⌉`, is equivalent to sterility of `x̂_9` and remains open.

## Results
* **Lemma 1.1 (PROVED).** `v_2(F+9) = 3 + v_2(5 − 9nδ − 2^{L−2}c_ok_o²)` exactly (`e − F = 16nδ`). So a fibre certificate
  is at `x̂_9` for some split (⟺ the minimal split `t = 2+⌈L/2⌉`) iff `nδ ≡ 5·9^{−1} (mod 2^{⌈L/2⌉−1})` (cofactor role: `−nδ`). The Pell structure imposes no local 2-adic
  constraint on `nδ` (§4, Hensel).
* **Theorem 2.1 (PROVED).** For every `m` there is a fibre certificate with `v_2(F+9) ≥ m` (`F = 7^s + 2^i`). Answers the open
  question of TYPEI4 §5 / Assess. 4.2(d) negatively: no ball around 9 in `Φ` is sterile.
* **Remark 2.1(b) (PROVED).** Every fibre triple `(c_o,k_o,F)` recurs at all levels `L ≡ L_0 (mod ord_F(2))` with constant
  closeness; it is at `x̂_9` for at most finitely many levels (`2+⌈L/2⌉ ≤ max(v_2(F+9), v_2(9F+1))`).
* **Cor 2.3 / Thm 2.4 (PROVED).** The covered part of `Φ ≅ 9+16ℤ_2` is open and dense; the sterile part is closed nowhere
  dense (of positive measure if TYPEI3's ≈ 0.6 evidence is right). Density holds already with `F = 71^ν` (`ν` odd),
  `c = 2^α·7·(71^ν+1)/8`, `k = 2^γ` (`b = 0`, `k' = 1`), using `ord_71(2) = 35`, `2^{70} ≢ 1 (71²)`.
* **Comp 2.2 / 2.5 (CERTIFIED once replayed).** Explicit approximants of `x̂_9` with closeness 4, 5, 6, 10, 11, 14; in these rows the least level is
  of the size of `F` (observation), so none is at `x̂_9`.
* **Comp 3.1 / Cor 3.2 (CERTIFIED once replayed).** Complete `(L,b)` grid `2^{L−4}7^b ≤ 2^{28}` (b=0: L≤32; b=1: ≤29; b=2:
  ≤26; b=3: ≤23; b=4: ≤20; b=5: ≤17; b=6: ≤15; b=7: ≤12; b=8: ≤9) with `typei4_lb`: 67 fibre certificates, max closeness 10,
  `t_min −` max ≥ 1 (≥ 10 for L ≥ 28); **no certificate at `x̂_9`**. Extends TYPEI4 Cor 3.5 (b=0 to L=32, b=1 to 29, b=2 to 26,
  b=3 to 23, b=4..7 at L ≥ 11). Second engine (`review_typei4_jsearch.c`) cross-check: see the status line below.
* **§4 (Assessment).** Level-graded heuristic: expected hits in the grid 0.59 (observed 0); beyond the grid ≲ 2·10⁻³ per
  `b`-row *if* cell counts stay ≤ 10 (no model for the infinitely many `b`-rows).
* Self-review (deep reviewer, no FATAL): repairs applied (sign `−16E`, modulus of `5/9`, split wording, Remark 2.1(a)
  made unconditional, heuristic labels, completion records + nonzero exit in the cross-check tooling).

## Caveats for the reviewer
* Cor 3.2: see the cross-check status below for which cells are two-engine.
* Thm 2.1 / 2.4 certificates have astronomically large height; they are valid Type-I certificates (TYPEI2 (2.2)) but say
  nothing about `C(7)` directly — their role is the scope statement (density / no neighbourhood test).
* STATUS.md / DISCOVERIES.md not edited (parent merges).

## Cross-check status
`review_typei4_jsearch.c` on the new cells b=0 L=27–32, b=1 L=24–29, b=2 L=25,26, b=3 L=23 (+ (22,0),(24,0)):
17/17 cells agree with `typei4_lb` (`typei7_xcheck.py`, exit 0). Single-engine cells of Cor 3.2: b=2 L=19–24,
b=3 L=18–22, b=4–7 at L ≥ 11 (Comp 3.4).
