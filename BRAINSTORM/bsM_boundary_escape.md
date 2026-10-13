# bsM_boundary_escape — what primes near a sterile point actually use (O188)

**Idea.** O178 (DEPTH_ASPECT Thm 3.1) proves sterile points x(u) on r-generic lines for large r. Primes p close to
x(u) (p ≡ 1 mod lcm(1..B), p ≡ u mod r^L) must still satisfy ES. Which classes certify them?
**Result.** Lemma (STERILE_STEER 1.1, PROVED): every ET class of such p has r-level > L or a prime power q^v ∥ M,
q ≠ r, q^v ∤ p − 1 (the *escape modulus*). EVIDENCE (`scripts/ss_escape.py`, r = 17, u = 5, B = 23, 47, 97,
30 primes per population, all classes of modulus ≤ 10⁵, witnesses re-solved): near x(5) and near the profinite square 1
the behaviour is identical. Escape happens in all 180 cases (≈ 150 distinct primes; R188 reproduced this independently)
at a single prime q > B, almost always among the first few primes after B, with Mordell height of order B
(1.5B–3B; R188 repair of "≈ 2.5B"). The r-adic depth never matters.
**Screen.** B1/B2: this is the ordinary moving-modulus lottery (H-A) at the boundary primes. The sterile point adds
nothing beyond the square point.
**Verdict.** Deflationary: sterility is not where hardness sits. Promise 0–1.
