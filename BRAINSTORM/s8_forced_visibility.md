# s8_forced_visibility — forced windows and T1-visible levels are one Legendre parity (O258; §3)

**Idea.** Mandatory (iii): route a recombination lift through forced windows, where p's non-residue primes are supplied.
**Literature.** (J)64 CAP_DOWN Thm 1.2; (J)83 Lemma 1.1 (Jacobi transfer); (J)86 Thm 3.2/Cor 3.3; O257 NONCONG_LIFTS Thm 1.2,
§2.4 (read-only, branch side-agent/noncong-lifts).
**Barrier screen.** Lemma 3.1 (PROVED): (K_q/p) = (q/p), and every cap-0 certificate has (uv/p) = −1. So every certificate is
visible at its level 4uv, forced or not, and forcing only guarantees that K_q contains visible primes. The window q is the
residue, never in the level. O257's sufficiency needs favourable witnesses, which is the B2 choice of (u, v).
**Cheap numerics.** `s8_genus_checks.py`: 13 500 windows with (K/p) = (q/p) in every case; 15 498 certificates, 0 with
(uv/p) ≠ −1.
**Assessment.** PROVED identification; routing through forced windows adds no totality. Closed.
