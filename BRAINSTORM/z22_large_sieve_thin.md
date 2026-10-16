# z22_large_sieve_thin — GRH-quality caps outside explicit thin sets (O250; CAP_BOUNDED §3)

**Idea.** Goal (C) pointwise is Burgess-blocked (p^{1/4+ε}); trade pointwise for an explicit exceptional set
𝒫(y) = {p ≡ 1 (8): every prime q ≡ 3 (4), q ≤ y, is a QR mod p} and use Linnik's large sieve.
**Result (PROVED rel. Montgomery's large sieve, PNT in APs, Pollack JNT 2018).** #{p ≤ X: e*(p) > (log X)^A/4}
≤ X^{2/A+o(1)}; #{p ≤ X: e*(p) > p^ε} ≪_ε (log X)^{⌈4/ε⌉}.
**Barrier screen.** B6 (it is an exceptional-set statement); bounded C impossible this way (𝒫(4C+3) has positive density).
Weaker in range than CAP_INTERPOLATION Rem 3.2(b)'s sketch (A > 1) but complete, with an explicit Chebotarev set.
**Label.** PROVED (routine combination). Improvement spark: a density lower bound |𝒜(N, N^{ε})| ≫ N/√log N would give
(log X)^{1/2}-type exceptional sets in (b).
