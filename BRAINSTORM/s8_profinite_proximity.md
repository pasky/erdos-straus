# s8_profinite_proximity — smooth p − 1 = closeness to the T1 point 1 (O258; §5)

**Idea.** p ≡ 1 (mod p − 1) always, so every divisor of p − 1 is an invisible modulus (AMPLIFY Thm 3.2). Primes with smooth
p − 1 sit near the T1 point 1 in Ẑ. Is that a hardness coordinate beyond QR-richness?
**Literature.** AMPLIFY_EXCEPTION Thm 3.2; JOINT_BUDGET Prop 4.3 (p − 1 data pins p to the sterile point); s7_lvalue_proxy.
**Barrier screen.** Diagnostic only (B6: statistics over p). Not a mechanism.
**Cheap numerics.** `s8_proximity.py 10000 40000`: mean b1/c1 counts 16.0/19.3 (S < 50), 13.7/16.5, 11.3/14.5 (S ≥ 500).
`s8_lines count840`: within the six Mordell square classes (p ∈ [10⁶, 3·10⁶]) class 1 has mean b1 19.63 against 20.25–20.89.
All three b = 1 failures have p − 1 11-smooth.
**Assessment.** EVIDENCE (weak): a few per cent beyond squareness; mostly QR-richness.
