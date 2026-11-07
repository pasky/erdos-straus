# Z62_INVERSEF — inverse theorem for R(n) = 0 (tryhard lane, wave z62)

Lane: INVERSEF. Fresh attack; only data used: `data/z58/screens/`. Scripts: `scripts/z62_inversef_*`, data `data/z62/inversef/`.

R(n) := #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}. Goal: an inverse theorem "R(n)=0 ⟹ square-like structure", then "structure + p prime ⟹ another explicit ES solution (or impossible)".

## §0 Mandatory falsifiers (stated up front; re-checked in §9)

* (F1) odd squares n = m²: R(m²) = 0. Any structure I claim forced by R(n)=0 must HOLD at odd squares; any "second step" (structure ⟹ other solution) must FAIL at odd squares, i.e. must genuinely use that p is prime / not a square.
* (F2) R₈ (the C-even half of R) vanishes at 12 primes in [10¹⁰, 1.1·10¹⁰] with R ≥ 12 (`r8_zeros_1e10.txt`). My inverse statement must distinguish "R = 0" from "R₈ = 0" (the odd-C conditions are part of the structure).
* (F3) 285 non-square composites n ≡ 1 (4), n ≤ 8·10⁶ have R(n) = 0 (`composite_zeros_le8e6.txt`, mostly 3,5,7 | n). The inverse statement must hold for them; the second step may fail for them.
* (F4) the 14 prime zeros 409 … 8 813 281 (`star_prime_zeros.txt`) DO have other ES solutions; the second step must find them.

Status tags: PROVED / CONDITIONAL / CERTIFIED (by computation, script named) / EVIDENCE.

(memo under construction — see git log)
