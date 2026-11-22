# z81 literature hunt: divisor-closed sets and prime products

Search date range: arXiv 2024-01-01–2026-11-22. Proofs not audited; theorem wording below is quoted from the downloaded arXiv `pdftotext -layout` files. Line references are to those `.txt` files.

## Best hits

### arXiv:2610.19597 — Banks–Shparlinski, “On the Erdős–Odlyzko–Sárközy conjecture for prime-power moduli”
- **Theorem 1.2 (verbatim):** “For any fixed prime \(p\), there are constants \(\gamma_2\) and \(C_2>0\) such that for every modulus \(q=p^\gamma\) with \(\gamma\ge\gamma_2\) we have \((\mathbb Z/q\mathbb Z)^×\setminus EOS_2(q)\le \phi(q)\exp(-C_2(\log q)^{1/3}(\log\log q)^{-1/3})\).” (`src/2610.19597.txt:102–105`.)
- **Averaging/scope:** Counts exceptional reduced residue classes for each fixed prime-power modulus; the theorem is uniform over classes but says nothing pointwise about a given modulus outside this family. `EOS_2(q)` is the classes representable as a product of two primes (paper’s notation).
- **Verdict: USABLE-INPUT (narrow).** Strongest actual-prime hit for lane 4: nearly every class modulo large `p^γ` has a two-prime representation. Could bound how many classes are unavailable to a candidate `Ω_q` in this modulus family.
- **Trap:** Does not bound the number/weight of pairs landing in arbitrary `Ω_q`, nor handle a sparse selected prime set `P_E`, arbitrary q, or a fixed integer. “Almost all classes” is not the same as a bilinear estimate for a specified class set.

### arXiv:2609.37434 — Banks, “Products of two elements of Granville’s random model in residue classes”
- **Theorem 1.1 (verbatim, compact):** “Fix \(\Theta\in(3/4,1]\) and a choice of the parameter \(A\) in the definition of \(G\). … Then, almost surely, there is a number \(q_0\) such that for every modulus \(q\ge q_0\) and all \(a\in(\mathbb Z/q\mathbb Z)^×\), there exist distinct \(g_1,g_2\in G\cap(X_q,2X_q]\) with \(g_1g_2\equiv a\pmod q\).” (`src/2609.37434.txt:119–128`; theorem continues with uniform asymptotic representation counts at `129–133`.)
- **Averaging/scope:** Almost-sure statement over the random model; then uniform over every sufficiently large modulus and every reduced class. `G` discards integers with small prime factors and independently samples the remaining integers with model probabilities (`109–116`).
- **Verdict: INSPIRATION.** A clean model result for bilinear products, including all classes and near-expected representation counts; potentially a benchmark for what sieve information alone predicts.
- **Trap:** Not the primes, and requires factors of size about `q^Θ` with `Θ>3/4`; no deterministic theorem for a sparse `P_E` or for an exceptional set. Model choice matters (paper abstract notes the analogous Banks–Ford–Tao random-prime model fails with positive probability).

### arXiv:2506.04087 — Chan, “Close points on a modular hyperbola”
- **Theorem 2 (verbatim, statement with conclusion):** “Given any real number \(\epsilon>0\), prime number \(p>2\), and integer \(c\) with \(\gcd(c,p)=1\). Let \(M\) be a multiplicative closed set with positive lower density \(\delta\). Then there exists a constant \(C_{\delta,\epsilon}>0\) such that … \((x+h,y+k)\in H_{pc}\) for some \((x,y)\in H_{pc}\) and some \(h,k\in M\cap[1,C_{\delta,\epsilon}p^{1/4}\exp((\log p)^{1/2+\epsilon})]\).” (`src/2506.04087.txt:68–79`; multiplicatively closed is defined at `56`.)
- **Averaging/scope:** For every individual prime `p` and nonzero `c`, obtains a pair of nearby points, with both coordinate offsets in `M`; no averaging over p. But the set `M` must have positive lower density.
- **Verdict: INSPIRATION, not usable for E.** An explicit pointwise theorem where multiplicative closure of the allowed offsets is exploited.
- **Trap:** This is a modular-hyperbola close-points theorem, not a count of divisor-closed sets. `M` is *multiplicatively* closed, not divisor-closed, and positive lower density is incompatible with the extremely sparse `P_E`-generated family in the campaign. No savings for `E(N)` follow.

## Targeted query log
- `all:"multiplicatively closed" AND all:"density"` — 4 hits; one relevant result was Chan 2506.04087, others irrelevant.
- `all:"integers composed of primes" AND all:"set of primes"` — 0 hits.
- `abs:"products of two primes" AND abs:"residue class"` — 2 hits: Banks 2610.19597; Banks 2609.37434.
- `abs:"multiplicative energy" AND abs:"primes" AND abs:"modulo"` — 0 hits.
- `all:"multiplicatively closed sets" AND all:"primes"` — 1 hit: Chan 2506.04087.
- `all:"divisor-closed" AND all:"integers"` — API returned HTTP 429 on retries; no count/result.

## Bottom line
No recent theorem found that bounds a divisor-closed `E⊂[1,N]` from a sparse prime support `P_E`, improves the `3/4` exponent via prime-factor structure, or bounds products of primes from a sparse set into an arbitrary large `Ω_q`. The direct actual-prime result is strong but only says almost all reduced classes are representable by two primes for prime-power moduli; it does not control arbitrary class avoidance or the sparse exceptional primes. No verified classical Wirsing/Hall–Tenenbaum theorem was surfaced/cited in the papers inspected; their multiplicative-function / smooth-number average results would require checking hypotheses before transfer to a divisor-closed set supported on an extremely sparse prime set.
