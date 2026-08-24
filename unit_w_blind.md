# Unit W blind attack log (phase 1)

Only notes.md §3 and §17.1 were consulted in this phase.

## Angle I: bounded multiplicative residues in criterion B

For q ≡ 3 (mod 4), x=(p+q)/4, write x=∏r^α.  Criterion B is exactly the bounded subset-product condition

    ∏ r^t_r ≡ -1 (mod q),       -α_r ≤ t_r ≤ α_r,

because d=x∏r^t_r runs through the divisors of x².  This makes the global obstruction explicit: subgroup membership without the exponent bounds is only a local shadow and is insufficient.

For hard p ≡1 (mod 24), q=3 gives x=(p+3)/4≡1 (mod 3).  Therefore q=3 works iff x has a prime factor r≡2 (mod 3): such an r itself is a valid d, while if there is no such r every divisor of x² is 1 mod 3.  More generally, for any q, a prime factor r≡-1 (mod q) of x suffices by taking d=xr.

An unconditional infinite family follows.  Fix a prime r≡5 (mod 6). Every prime

    p ≡ 20r-3 (mod 24r)

is hard and is solved at q=3, since x=r(6t+5).  The residue is coprime to 24r, so Dirichlet gives infinitely many primes in each such progression.  At r=5 this is p≡97 (mod 120).

Computation (SymPy, exact divisors): among the 9,732 hard primes below 10^6, q=3 covers 5,192 (53.35%), and q∈{3,7,...,63} covers all 9,732.  Death point: q=3 leaves 4,540 cases; p=73 already fails it.  The congruence x≡1 mod3 does not force a 2 mod3 prime factor.

## Angle II: shifted factors and the conic

Set a=1 in Type II.  This is equivalent to finding c≥1 and

    D | p+4c,                 D ≡ -1 (mod 4c).

Indeed k=(D+1)/(4c), t=(p+4c)/D, b=kt-1 give p=4bc-t and t=(b+1)/k, hence kp=4bck-b-1.  Conversely D=4ck-1 from any a=1 tuple divides p+4c.  For c=1, any 3 mod4 prime factor of p+4 settles p.  More generally fixed c,k settle the arithmetic progression p≡-4c mod (4ck-1), whenever it meets the hard primes.

Exact computation below 10^6: c≤1,2,4,8,16,32,64,128 cover respectively 4,850, 7,824, 8,962, 9,525, 9,680, 9,719, 9,726, 9,727 of the 9,732 hard primes.  A complete finite scan uses c≤(p+2)/4 and proves that exactly p=193,2521,66529 have no a=1 Type-II tuple.  They are not counterexamples: tuples (a,b,c,k)=(2,5,5,1), (2,159,2,7), (5,832,4,27) solve them.

For the geometric attack put h=(a+b)/k and r=b-a.  Then

    a=(hk-r)/2, b=(hk+r)/2,
    p=c(h²k²-r²)-h,
    (hk-r)(hk+r)=(p+h)/c.

The diagonal r=0 gives p=h(chk²-1), so no hard prime can lie on it (h≡3 mod4 and h≥3).  Fixing p,h,c does not produce a genuine Pell equation: the would-be quadratic coefficient h² is a square and the conic splits into the displayed factorization.  Continued fractions therefore return to the same exact-divisor problem.  In an exhaustive q≤63 scan of all 1,181 hard primes below 10^5, the smallest |a-b| among those witnesses reaches 535 at p=87049, via (h,a,b,c,k)=(47,38,573,1,13).  Thus even a generous bounded-near-diagonal ansatz has no observed stable bound, and the exact diagonal is impossible.

## Angle III: a Type-I divisor-cover sieve

Set a=1 in Type I and let D=4ck-p.  Then bD=p+k.  Since p∤ck for a Type-I tuple, gcd(D,p)=1; multiplying the divisibility by 4c shows D | 4c+1.  Conversely, a positive divisor D|4c+1 with

    p ≡ -D (mod 4c)

produces

    k=(p+D)/(4c), E=(4c+1)/D,
    b=(pE+1)/(4c)=(p+k)/D,

and p(1+b)=k(4bc-1).  For hard p necessarily D≡3 mod4.  This gives unconditional prime residue families.  For c=5, D=3,7 settle respectively all hard primes p≡97,73 (mod 120), with explicit a=1 Type-I tuples.

The sieve is unexpectedly strong computationally.  Every one of the 82,887 hard primes below 10^7 has such an a=1 Type-I witness.  The scan is finite: D is a proper divisor of 4c+1, hence D≤(4c+1)/3 and k≥1 implies c≤(3p+1)/8.  Searching c upward, the largest first witness in this range was c=107,588 at p=8,604,961 (D=2,079).

Death point: this is not a pointwise proof.  It replaces the conjecture by the demand that some moving number 4c+1 have a 3 mod4 divisor exactly matching p modulo 4c.  Local congruence or p-adic solvability does not force that divisor.  A finite collection of c gives only a finite union of progressions; the impressive coverage supports a density heuristic, not the missing no-exception theorem.
