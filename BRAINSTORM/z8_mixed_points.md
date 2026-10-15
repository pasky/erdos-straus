# z8_mixed_points — mixed exponent points: CRT-glued integer squares as the sterile candidates of exponential families (O232)

**Idea.** For n_s = 4^s + k, take integer exponents ℓ₁, ℓ₂ with n_{ℓ_i} (rational) squares and glue them in Ẑ =
Π_ℓ ℤ_ℓ: μ* = ℓ₁ in some ℓ-adic components, ℓ₂ in others (possible when ℓ₁ ≡ ℓ₂ modulo the shared part). At primes q whose
ord_q(4) only involves the first (second) set of ℓ, n_q is the square n_{ℓ₁} (n_{ℓ₂}); only "mixed-order" primes see a
generic value. Such μ* are the natural candidates for sterile points of Λ_k — and the place where coverings get expensive.

**Literature.** (J)22 §4.3 (single near-square points); Sierpiński numbers with "partial coverings" and the role of
algebraic factorisations (Filaseta–Finch–Kozek, J. Number Theory 2008: Sierpiński numbers whose covering must mix
algebraic and congruence pieces) — analogous mixing phenomenon.

**Barrier screen.** Not a barrier itself; it is the exponential analogue of B1's square point. Unlike Sq^× points,
mixed points are not unit squares (generic at mixed-order primes), so Thm 1.2/1.4's T1 argument does not make them
sterile; their sterility depends on the ET class supply (the non-square part of S′, (J)54-type).

**Cheap numerics.** k = 105 (`scripts/z8_point.py 1 105 300000 4 3:-2`): μ* = (4 off 3, −2 at 3) explains the residual
class s ≡ 124 (360) / 844 (2520); n ≡ 19² resp. (41/4)² at unmixed primes; non-residue at q = 181 (ord 90) without an ET
class; μ* itself lies in II2 (2, 23, 919). Adaptive lifting (`z8_adaptive.py`): uncovered Haar measure 8·10⁻³ → 8·10⁻⁵
over 28 refinements, non-terminating within the run.

**Assessment.** EVIDENCE + description. CONJECTURE (weak): every mixed point of 4^s + 105 lies in some ET class (no
sterile point found), so a finite covering exists, but its period is ≥ 10⁸. A sterile mixed point would give a clean
uncoverability theorem — the pursuit is a finite-but-large computation, not a mechanism.
