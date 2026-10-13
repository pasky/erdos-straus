# bsL_finite_mute — muting a finite prime by parity (O186, spark relay L)

Idea: the "mute place" of V_φ (a real place whose invariant is pinned to 0 by a sign pattern) can be a finite prime
q: allow q in the denominator of ONE variable, only to an even power. Lemma 1.1 of UNIT_ORBIT_ES.md: inv_q = 0 on all
such points; with odd powers inv_q is the free symbol ((−y/x)/q). Consequences: ES^{(S)} (4/n = 1/x + 1/y + Q²/Z,
gcd(Z, Q) = 1) is T1-bearing; the orbit {Q²} gives fixed-modulus shots n + 4Q²; with |S| ≥ 4, existence at every
non-square n is unconditional (Gupta–Murty sieve) — and by divisibility ES^{(S)}(n) then holds for every n > 1 coprime to 2S (Cor 2.5, R186 repair m4). Along the orbit, ES-solutions = ES^{(S)}-solutions with g ≡ −1 (mod 4Q) (Prop 6.1).
Open directions:
* Mute primes in OTHER variables/shapes (Type I analogue: a = pe + 4Q²?) and the full set of normalisations pinning
  inv_q = 0 (anchor calculus, TWISTED_T1 §2, applied to non-integral points): which ones are "Lagrangian" here?
* Order-3 analogue: TES over ℤ[ω][1/S] with cube-power denominators (mute via 3 | w) — an unconditional order-3 T1
  variant?
* Quantify: smallest Q needed (≤ 99 for n < 3·10⁵, S = {3,5,7,11}); an effective version needs an effective sieve.
* Does any "interpolation" between ES^{(S)} and ES (e.g. denominators bounded by a power of x) keep both the T1 and
  provability? The growing modulus 4Q of Prop 6.1 suggests a lottery exactly when Q is not allowed in denominators.
