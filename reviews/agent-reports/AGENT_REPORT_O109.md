# AGENT REPORT O109 — 2-adic closeness of fibre certificates to `w = 9` (sign point `x̂_9`)

Branch `side-agent/sign-point-2adic`. Deliverable: `POINTWISE_TYPEI7.md`; scripts `typei7_tab.py`, `typei7_xcheck.py`,
`typei7_unbounded.py`, `typei7_dense71.py`, `typei7_family.py`. Not reviewed.

## Outcome (one line)
A **precise negative result**: the requested bound on `v_2(F+9)` in terms of a fixed 2-adic precision does not exist — the
closeness is unbounded and the covered part of the fibre is open dense (PROVED, explicit certificates). The only bound that
would suffice, `v_2(F+9) < 2+⌈L/2⌉`, is equivalent to sterility of `x̂_9` and remains open.

## Results
* **Lemma 1.1 (PROVED).** `v_2(F+9) = 3 + v_2(5 − 9nδ − 2^{L−2}c_ok_o²)` exactly (`e − F = 16nδ`). So a fibre certificate
  is at `x̂_9` iff `nδ ≡ 5/9 (mod 2^{⌈L/2⌉−1})` (cofactor role: `−nδ`). The Pell structure imposes no local 2-adic
  constraint on `nδ` (§4, Hensel).
* **Theorem 2.1 (PROVED).** For every `m` there is a fibre certificate with `v_2(F+9) ≥ m` (`F = 7^s + 2^i`). Answers the open
  question of TYPEI4 §5 / Assess. 4.2(d) negatively: no ball around 9 in `Φ` is sterile.
* **Remark 2.1(b) (PROVED).** Every fibre triple `(c_o,k_o,F)` recurs at all levels `L ≡ L_0 (mod ord_F(2))` with constant
  closeness; it is at `x̂_9` for at most finitely many levels (`2+⌈L/2⌉ ≤ max(v_2(F+9), v_2(9F+1))`).
* **Cor 2.3 / Thm 2.4 (PROVED).** The covered part of `Φ ≅ 9+16ℤ_2` is open and dense; the sterile part is closed nowhere
  dense ("fat Cantor set" if TYPEI3's measure ≈ 0.6 evidence is right). Density holds already with `F = 71^e` (`e` odd),
  `c = 2^α·7·(71^e+1)/8`, `k = 2^γ` (`b = 0`, `k' = 1`), using `ord_71(2) = 35`, `2^{70} ≢ 1 (71²)`.
* **Comp 2.2 / 2.5 (CERTIFIED once replayed).** Explicit approximants of `x̂_9` with closeness 4, 5, 6, 10, 11, 14; their level
  is ≈ `F` (discrete log), so they are nowhere near `x̂_9`'s requirement.
* **Comp 3.1 / Cor 3.2 (CERTIFIED once replayed).** Complete `(L,b)` grid `2^{L−4}7^b ≤ 2^{28}` (b=0: L≤32; b=1: ≤29; b=2:
  ≤26; b=3: ≤23; b=4: ≤20; b=5: ≤17; b=6: ≤15; b=7: ≤12; b=8: ≤9) with `typei4_lb`: 67 fibre certificates, max closeness 10,
  `t_min −` max ≥ 1 (≥ 10 for L ≥ 28); **no certificate at `x̂_9`**. Extends TYPEI4 Cor 3.5 (b=0 to L=32, b=1 to 29, b=2 to 26,
  b=3 to 23, b=4..7 at L ≥ 11). Second engine (`review_typei4_jsearch.c`) cross-check: see the status line below.
* **§4 (Assessment).** Level-graded heuristic: expected hits in the grid 0.59 (observed 0), tail ≲ 10⁻².

## Caveats for the reviewer
* Cor 3.2's new cells rest on `typei4_lb` alone except where `typei7_xcheck.py` reports agreement (below).
* Thm 2.1 / 2.4 certificates have astronomically large height; they are valid Type-I certificates (TYPEI2 (2.2)) but say
  nothing about `C(7)` directly — their role is the scope statement (density / no neighbourhood test).
* STATUS.md / DISCOVERIES.md not edited (parent merges).

## Cross-check status
(updated at the end of the run)
