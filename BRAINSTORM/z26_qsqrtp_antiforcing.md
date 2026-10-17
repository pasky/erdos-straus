# z26_qsqrtp_antiforcing — CF of √p, Pell, near squares only give residue windows (O254; JOINT_BUDGET §4.2)

**Idea (candidate (i)).** Choose the window/auxiliary from the arithmetic of ℤ[√p]: continued-fraction norms
|P_k² − pQ_k²|, Pell data, next-square windows m = w² − p, or p + m = c·w².
**Result (Prop 4.2, PROVED).** (K/m) = (p/m) = (c/m) = (c/p). For c = 1 and for every m | A² − pB² (gcd(B, m) = 1) the
window has (p/m) = +1: never Jacobi-forced. Forced windows need an odd number of ℚ(√p)-inert primes to odd power —
invisible to the c = 1 / norm constructions above. General c is forced iff (c/p) = −1 (p = 17, m = 7, c = 6 fires): then the
non-residue comes from c, an (R2)-type choice. Structural reading of near-square hardness.
**Barrier screen.** Genus (Prop 10.3 door): the only forcing is a character value; c must itself be a non-residue mod p,
i.e. the least non-residue (back to (R2)).
**Numerics.** z26_checks (c): 368 689 windows, p < 2·10⁵, 0 violations.
**Label.** PROVED (negative).
