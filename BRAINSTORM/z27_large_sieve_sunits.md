# z27_large_sieve_sunits — large sieve over moduli q for the S-unit box: too sparse to bite (O256)

**Idea.** Pretentious characters make the S-unit box sum Σ_{h∈[0,H]^k} ψ(g^h) large (≥ (H+1)^k/2 when Hk𝔻 ≤ 1/4). The
multiplicative large sieve Σ_{q≤Q} Σ*_{χ mod q} |Σ_{n≤M} a_n χ(n)|² ≤ (M + Q²)Σ|a_n|² would bound the number of such q.
**Why it fails (PROVED arithmetic).** The S-units of the box go up to M = P^{2H}; M ≤ Q² forces H ≤ log Q/log P = O(1) when
P = Q^{Θ(1)}; then #bad ≤ 4Q²/(H+1)^k, useless against the needed Q/P (would need (H+1)^k ≥ QP = P^{O(1)}, but (H+1)^k = P^{o(1)}).
The S-units are too sparse among integers ≤ M for this ordinary large-sieve instantiation (other duality arguments are not
excluded); Fourier duality just returns the divisibility count of z27_fejer_blind_count.
**Literature.** Montgomery–Vaughan, Multiplicative Number Theory I, §27 (large sieve); Linnik's application to least
non-residues (works because all integers ≤ M are used, not a sparse multiplicative set).
**Barrier screen.** B4-like (sparse generator set), B6.
**Cheap numerics.** n/a.
**Assessment.** PROVED (negative, for this instantiation).
