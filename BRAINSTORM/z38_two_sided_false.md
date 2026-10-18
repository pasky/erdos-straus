# z38_two_sided_false — "|X(p)| < M(p) for all large p" is false infinitely often (O268)

**Idea.** Test O260's H_X (and its BM version) for internal consistency before asking whether a standard conjecture implies it.

**Result (PROVED, BM_CORRECTED_COUNT Prop 3.1).** Linnik: primes p ≡ −1 (mod Q_k), p ≡ 1 (4), Q_k = product of the first k
primes ≡ 3 (4), have ≥ 2^{k−1} u = 1 hits (u, B, C) = (1, (p+1)/d, (d+1)/4), d | Q_k with an odd number of prime factors.
So R(p) ≥ exp(c·log p/log log p) infinitely often, while M_BM ≪ log² p and M_gen ≪ log⁴ p. Any two-sided polylog-error
hypothesis fails i.o.; only H⁻ (R ≥ εM) can be true. EVIDENCE: at primes p ≡ 1 (4) in [3·10⁵, 10⁶), 2.9 % have R > 2M_BM.

**Literature.** Linnik's theorem (Xylouris: L = 5). Same mechanism as the τ(p+1) upper tail of shifted-divisor problems.

**Barrier screen.** B3 reinforced: the count is not concentrated in either direction at polylog scale; the lower tail is the
only relevant one, and it is a large-deviation statement.

**Cheap numerics.** `scripts/z38_hx.py` on `z38_mbm` output.

**Assessment.** PROVED (negative, exact scope: two-sided bounds with E = (log p)^{O(1)}).
