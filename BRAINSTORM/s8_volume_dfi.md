# s8_volume_dfi — DFI is uniform in p; the obstruction is O(1) points per box (O258; §1.6)

**Idea.** Mandatory (i): can Kloosterman-fraction bilinear bounds (DFI 1997) count ES points at ONE p?
**Literature.** Duke–Friedlander–Iwaniec, Invent. Math. 128 (1997) 23–43, Thm 1 (uniform in the numerator a);
Bettin–Chandee, Adv. Math. 328 (2018); Shparlinski, *Modular hyperbolas* (2012) (PARITY_AUDIT rows B1, B7).
**Barrier screen.** The fixed numerator a = p is harmless (DFI is uniform in a). Lemma 1.6: the ES/MP indicator has expected count
≍ 1 per dyadic box, so completion leaves error ≍ (XY)^{1/2} even with square-root cancellation in every frequency. The method
violates "main term ≫ error". This is B3 in volume form, and it matches the R265 per-box Weil benchmark.
**Cheap numerics.** None needed beyond PARITY_AUDIT's R(p) ≈ (log p)²/8 (polylog total over ≍ log²p boxes).
**Assessment.** PROVED (density) + Assessment (completion). A one-p count needs cancellation across frequencies, beyond square
root. Closed.
