\\ z58 FFIELD: per-polynomial decider for (★)_q.  R_q(P) >= 1 iff there are monic u (deg a), d with
\\ d | P+u, d ≡ -1 (mod u), deg d - a odd, a < deg d < n - a  (WLOG deg u < deg v; v = (P+u)/d, t = (d+1)/u).
\\ ffdec(P, q): returns [u, d] (first witness, a increasing) or 0.  P must be monic of EVEN degree n >= 2 with
\\ coefficients Mod(.,q), q PRIME (prime fields only).  (For odd n the trivial word (P+2,1,1) always exists and the
\\ WLOG deg u < deg v step is invalid, so odd n is rejected.)
ffmku(k, a, q) = Pol(apply(c -> Mod(c, q), digits(k + q^a, q)));
ffdec(P, q) = {
  my(n = poldegree(P));
  if (n % 2 || n < 2 || pollead(P) != 1, error("ffdec: need monic P of even degree >= 2"));
  for (a = 0, (n - 2) \ 2,
    for (k = 0, q^a - 1,
      my(u = ffmku(k, a, q), F = factor(P + u), fs = F[, 1], ms = F[, 2], L = #fs);
      forvec(e = vector(L, i, [0, ms[i]]),
        my(dd = sum(i = 1, L, e[i] * poldegree(fs[i])));
        if (dd > a && dd < n - a && (dd - a) % 2 == 1,
          my(d = prod(i = 1, L, fs[i]^e[i]));
          d = d / pollead(d);
          if ((d + 1) % u == 0, return([u, d]))))));
  0
};
