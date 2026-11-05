\\ z58 FFIELD: targeted family  P = c0 + M*h  (h monic of degree n - deg M), P irreducible, decided by ffdec2.
\\ M = lcm of all monic polynomials of degree <= m over F_q, times the first K3 monic irreducible cubics
\\ ("maximal small-modulus avoidance": P ≡ c0 = square mod every d | M, so no witness d | M exists, by the colour
\\ lemma).  Set q, n, m, K3, c0, nsamp (0 = exhaustive), amax before reading.
\\ Output: ZERO lines (certified: no witness with deg u <= (n-2)/2), HARD lines (no witness with deg u <= amax,
\\ undecided), SUMMARY with the histogram of a*(P) = least deg u of a witness (the smaller cofactor).
read("scripts/z58_ffield_decide.gp");
ffdec2(P, q, amax) = {
  my(n = poldegree(P));
  for (a = 0, min(amax, (n - 2) \ 2),
    for (k = 0, q^a - 1,
      my(u = ffmku(k, a, q), F = factor(P + u), fs = F[, 1], ms = F[, 2], L = #fs);
      forvec(e = vector(L, i, [0, ms[i]]),
        my(dd = sum(i = 1, L, e[i] * poldegree(fs[i])));
        if (dd > a && dd < n - a && (dd - a) % 2 == 1,
          my(d = prod(i = 1, L, fs[i]^e[i]));
          d = d / pollead(d);
          if ((d + 1) % u == 0, return([u, d]))))));
  if (amax >= (n - 2) \ 2, 0, -1)
};
fflcm(q, m) = { my(L = Mod(1, q) * 1); for (k = 1, m, for (j = 0, q^k - 1, L = lcm(L, ffmku(j, k, q)))); L };
ffcubics(q, K) = { my(L = Mod(1, q) * 1, c = 0); for (j = 0, q^3 - 1, if (c >= K, break); my(l = ffmku(j, 3, q)); if (polisirreducible(l), L *= l; c++)); L };
{
  my(M = fflcm(q, m) * ffcubics(q, K3), dM = poldegree(M), dh = n - dM, tot = q^dh, cand = 0, irr = 0, zer = 0, hard = 0,
     ah = vector(n));
  if (dh < 0, error("n too small"));
  setrand(12345 + n + 1000 * m + 100000 * K3);
  for (it = 0, if (nsamp, nsamp, tot) - 1,
    my(k = if (nsamp, random(tot), it), P = Mod(1, q) * c0 + M * ffmku(k, dh, q));
    cand++;
    if (!polisirreducible(P), next);
    irr++;
    my(w = ffdec2(P, q, amax));
    if (w == 0, zer++; print("ZERO ", lift(P)),
      if (w == -1, hard++; print("HARD ", lift(P)), ah[poldegree(w[1]) + 1]++)));
  print("SUMMARY q=", q, " n=", n, " m=", m, " K3=", K3, " degM=", dM, " c0=", c0, " mode=", if (nsamp, "sample", "exhaustive"),
        " amax=", amax, " cand=", cand, " irr=", irr, " zeros=", zer, " hard(undecided)=", hard, " hist a*=", ah);
}
