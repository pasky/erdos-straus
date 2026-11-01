# Z2094 literature notes (2026-11-01)
* Premise: "Hooley's GRH result for x^2+y^2+z^3" -- not found. Searches: web "Hooley sum of two squares and a cube ...", "\"two squares and a cube\" every sufficiently large integer";
  arXiv API ti/abs "two squares and a cube" (0 hits).
* Jagy & Kaplansky, "Sums of squares, cubes, and higher powers", Experiment. Math. 4(3) (1995) 169-173 (abstract read on Project Euclid):
  every integer is x^2+y^2+z^3 with mixed signs; for all-positive x^2+y^2+z^3 "computations support the possibility that there are only finitely many exceptions";
  x^2+y^2+z^9 has infinitely many positive exceptions.  => the positive x^2+y^2+z^3 problem is OPEN (no GRH theorem known to us).
* The actual Hooley GRH theorem: C. Hooley, On the representation of a number as the sum of two squares and a prime, Acta Math. 97 (1957) 189-210
  (read: intro + Theorem 1, p. 209): on ERH, #{n = p + u^2 + v^2} = (pi n/log n) prod_p (1 + chi(p)/(p(p-1))) prod_{p|n, p≡1(4)} (p-1)^2/(p^2-p+1)
  prod_{p|n, p≡3(4)} (p^2-1)/(p^2-p-1) + O(n/log n (loglog n)^{-delta}); every large n is p + u^2 + v^2. Method: sum_p r(n-p) = 4 sum_d chi_4(d) pi(n; n, d)
  (Titchmarsh divisor problem with the FIXED character chi_4), GRH for d up to ~sqrt n, Brun sieve + asymptotic invariant-sieve formulae for the exceptional d
  (the sign changes of chi_4). Made unconditional by Linnik (dispersion method).
