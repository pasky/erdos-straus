\\ z58 FFIELD: targeted family  P = c0 + M*h  (h monic of degree n - deg M), P irreducible, decided by ffdec.
\\ M = lcm of all monic polynomials of degree <= m over F_q ("maximal small-modulus avoidance": P ≡ c0 ≡ square
\\ mod every d of degree <= m, so no witness d of degree <= m exists, by the colour lemma).
\\ Set q, n, m, c0 (a polynomial), nsamp (0 = exhaustive) before reading.  Prints ZERO lines + SUMMARY.
read("scripts/z58_ffield_decide.gp");
fflcm(q, m) = { my(L = Mod(1, q) * 1); for (k = 1, m, for (j = 0, q^k - 1, L = lcm(L, ffmku(j, k, q)))); L };
{
  my(M = fflcm(q, m), dM = poldegree(M), dh = n - dM, tot = q^dh, cand = 0, irr = 0, zer = 0, wdeg = vector(n + 1));
  if (dh < 0, error("n too small"));
  setrand(12345 + n + 1000 * m);
  for (it = 0, if (nsamp, nsamp, tot) - 1,
    my(k = if (nsamp, random(tot), it), P = Mod(1, q) * c0 + M * ffmku(k, dh, q));
    cand++;
    if (!polisirreducible(P), next);
    irr++;
    my(w = ffdec(P, q));
    if (w == 0, zer++; print("ZERO ", lift(P)), wdeg[poldegree(w[2]) + 1]++));
  print("SUMMARY q=", q, " n=", n, " m=", m, " degM=", dM, " c0=", c0, " mode=", if (nsamp, "sample", "exhaustive"),
        " cand=", cand, " irr=", irr, " zeros=", zer, " first-witness deg d histogram=", wdeg);
}
