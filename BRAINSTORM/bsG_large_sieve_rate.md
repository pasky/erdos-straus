# bsG_large_sieve_rate — an unconditional rate for Lorenzini's exceptional set (O180)

## Idea
Exceptions avoid τ(p+1) − 2 classes mod every prime p ≤ √N (prime-modulus (x,y) families). The sieve dimension grows like log p.
Montgomery's large sieve with k-fold products of primes then gives a sub-power saving.

## Result (LORENZINI_W Prop 6.1; PROVED relative to the Titchmarsh divisor asymptotic Σ_{p≤y} τ(p+1) ~ C y)
#{n ≤ N : n not a value of xyz − x − z, x,y,z ≥ 2} ≪ N exp(−c √(log N)).

## Literature
Montgomery, *The analytic principle of the large sieve* (BAMS 1978). Titchmarsh divisor problem: Linnik (1961), Halberstam (1967),
Bombieri–Friedlander–Iwaniec (1986). ES analogue: Vaughan (1970), N exp(−c log^{2/3} N). Lorenzini Thm 4.2 and Wang (EJC 2026) give density 1.

## Barrier screen
B6: averages say nothing pointwise. This cannot reach finiteness. With prime moduli only, the large sieve cannot exceed
exp(O(√log N · …)). Composite moduli with non-CRT class sets (all (x,y), (x,z) families) would be needed. Vaughan's ES method suggests exp(−c log^{2/3} N).

## Cheap numerics
The true count is 11 (E_W) up to 10⁹. The bound is very weak in comparison.

## Assessment
PROVED (modest). Possibly new as a quantitative statement for Lorenzini's question. Promise 1/5 (for the paper-B appendix), 0 for ES.
Spark: transfer Vaughan's argument.
