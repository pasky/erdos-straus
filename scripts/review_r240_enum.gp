\\ R240 from-scratch enumerator (PARI/GP; run via scripts/review_r240_enum.py) of k = 1 Case B tuples at q = 9:
\\   m'wC = T^s + v,  w + C = g'v,  m', g', w, C monic,  T does not divide m'g'wCv   (FF_STERILE_SMALL (B^{k=1}))
\\ per pattern (s; a, z, y, t), a <= b = s - a - z, t = b - y.  Every candidate is re-verified from scratch by chk().
\\ Routes (all complete: each tuple of the pattern arises exactly once):
\\   1 NF : (m', w, g') -> C = (w + g'T^s)/(g'm'w - 1)                        cost q^(z+a+y)
\\   2 V  : v (lc 1 if a<b, 2 if a=b), ordered divisor triples of T^s + v      cost q^t
\\   3 MG : (m', g'), E | 1 + T^s m'g'^2 monic of degree z+y+a, w = (E+1)/(m'g') cost q^(z+y)
\\   4 WG : (w, g'),  E | g'T^s + w of degree z+y+a, C = cofactor               cost q^(a+y)
\\   5 MW : (m', w),  E | T^s + m'w^2 of degree z+y+a, v = cofactor             cost q^(z+a)
\\ where E := m'g'w - 1 (so E C = g'T^s + w, E v = T^s + m'w^2, E E' = 1 + T^s m'g'^2, E' = m'g'C - 1; re-derived in review).
\\ field: setq(p, r) (default q = 9); EL[1] = 0, EL[2..QQ] = the nonzero elements (same ordering as before for q = 9)
setq(p, r) = { gg = ffgen([p, r], 'a); o = gg^0; QQ = p^r; EL = vector(QQ, k, sum(i = 0, r - 1, (((k-1) \ p^i) % p) * gg^i) * o); }
setq(3, 2);
TF(P) = polcoef(P, 0) != 0;
ismon(P) = pollead(P) == o;
\\ result accumulators (global): CNT[1] = all slices, CNT[2] = P8 (E(0)^4 = -1), CNT[3] = law failures, CNT[4] = E(0) not in {1, -1}
chk(s, a, z, y, t, m, w, C, g, v) = {
  my(E0);
  if (poldegree(m) != z || poldegree(w) != a || poldegree(C) != s-a-z || poldegree(g) != y || poldegree(v) != t, return(0));
  if (!ismon(m) || !ismon(w) || !ismon(C) || !ismon(g), return(0));
  if (!TF(m) || !TF(w) || !TF(C) || !TF(g) || !TF(v), return(0));
  if (m*w*C != x^s + v || w + C != g*v, return(0));
  E0 = (polcoef(w,0)*o) / (polcoef(C,0)*o);
  CNT[1]++;
  if (E0^4 == -o, CNT[2]++);
  if (E0 != o && E0 != -o, CNT[4]++);
  if (E0^s != (-1)^(t + t*z + z*(1+s) + t*s) * o, CNT[3]++);
  if (E0 == -o, CNT[3]++);
  1;
}
\\ the k-th (0 <= k < nmon(d)) polynomial lead*(monic of degree d with nonzero constant term); all coefficients t_FFELT
nmon(d) = if (d == 0, 1, (QQ - 1) * QQ^(d-1));
mk(d, k, lead = 1) = {
  my(P = lead * o * x^d, c);
  if (d == 0, return(lead * o));
  P += lead * EL[2 + k % (QQ - 1)]; k \= (QQ - 1);
  for (i = 1, d - 1, c = k % QQ; k \= QQ; P += lead * EL[c + 1] * x^i);
  P;
}
\\ exact quotient N/D as a t_POL, or 0 if D does not divide N (N != 0); robust to scalar (t_INT / t_FFELT) inputs
exq(N, D) = { my(n = Pol(o*N, 'x), d = Pol(o*D, 'x)); if (n % d != 0, 0, n \ d); }
divs_deg(P, d) = {
  my(L = divisors(factor(P / pollead(P))), R = List());
  for (i = 1, #L, if (poldegree(L[i]) == d, listput(R, Pol(o * L[i] / pollead(L[i]), 'x))));
  Vec(R);
}
pattern(s, a, z, y, t, route) = {
  my(b = s - a - z, Ts = o*x^s, lam = if (a < b, 1, 2), dE = z + y + a, m, w, g, v, C, E, Ep, P, Q, den, num, LE, Lm, Lw);
  CNT = vector(4);
  if (route == 1,
    for (i1 = 0, nmon(z) - 1, m = mk(z, i1);
      for (i2 = 0, nmon(a) - 1, w = mk(a, i2);
        for (i3 = 0, nmon(y) - 1, g = mk(y, i3);
          den = g*m*w - 1;
          if (den != 0, C = exq(w + g*Ts, den);
            if (C != 0, v = m*w*C - Ts; chk(s, a, z, y, t, m, w, C, g, v)))))));
  if (route == 2,
    for (i1 = 0, nmon(t) - 1, v = mk(t, i1, lam); P = Ts + v; Lm = divs_deg(P, z);
      for (i = 1, #Lm, m = Lm[i]; Q = exq(P, m); Lw = divs_deg(Q, a);
        for (j = 1, #Lw, w = Lw[j]; C = exq(Q, w);
          g = exq(w + C, v); if (g != 0, chk(s, a, z, y, t, m, w, C, g, v))))));
  if (route == 3,
    for (i1 = 0, nmon(z) - 1, m = mk(z, i1);
      for (i3 = 0, nmon(y) - 1, g = mk(y, i3); P = 1 + Ts*m*g^2; LE = divs_deg(P, dE);
        for (i = 1, #LE, E = LE[i];
          w = exq(E + 1, m*g); Ep = exq(P, E);
          if (w != 0 && Ep != 0, C = exq(Ep + 1, m*g);
            if (C != 0, v = m*w*C - Ts; chk(s, a, z, y, t, m, w, C, g, v)))))));
  if (route == 4,
    for (i2 = 0, nmon(a) - 1, w = mk(a, i2);
      for (i3 = 0, nmon(y) - 1, g = mk(y, i3); P = g*Ts + w; LE = divs_deg(P, dE);
        for (i = 1, #LE, E = LE[i]; C = exq(P, E); m = exq(E + 1, g*w);
          if (m != 0 && C != 0, v = m*w*C - Ts; chk(s, a, z, y, t, m, w, C, g, v))))));
  if (route == 5,
    for (i1 = 0, nmon(z) - 1, m = mk(z, i1);
      for (i2 = 0, nmon(a) - 1, w = mk(a, i2); P = Ts + m*w^2; LE = divs_deg(P, dE);
        for (i = 1, #LE, E = LE[i]; v = exq(P, E);
          if (v != 0, C = exq(Ts + v, m*w);
            if (C != 0, g = exq(w + C, v); if (g != 0, chk(s, a, z, y, t, m, w, C, g, v))))))));
  CNT;
}
\\ ---- Case A (k = 1) at q = 9: data (a1', b1, K), a1', b1 monic, lc K in {1, 2}, T not dividing a1'b1K, E = a1'b1K - 1,
\\ F = (T^al a1' + b1)/E.  Route: z := (F + b1)/a1' (lc arbitrary, z(0) != 0, deg z <= tmax), then ordered factorisations
\\ T^al + z = b1 * K * F (identity b1 K F = T^al + z, re-derived in the review), a1' = (F + b1)/z.  Every candidate is re-verified.
\\ Returns a Map pattern [al, deg a1', be, ka] -> [n_all, n_offF3, n_P8, lawfail]
caseA(al, tmax) = {
  my(M = Map(), P, Ld, b1, K, Fp, a1, E, E0, key, cur, z, R, lk);
  for (t = 0, tmax, for (lz = 2, QQ, for (i1 = 0, nmon(t) - 1, z = mk(t, i1, EL[lz]);
    P = o*x^al + z; if (P == 0 || poldegree(P) < 0, next);
    Ld = divisors(factor(P / pollead(P)));
    for (i = 1, #Ld, b1 = Pol(o*Ld[i] / pollead(Ld[i]), 'x); R = exq(P, b1);
      my(Lk = divisors(factor(R / pollead(R))));
      for (j = 1, #Lk, for (c = 1, 2, K = Pol(c * o * Lk[j] / pollead(Lk[j]), 'x); Fp = exq(R, K);
        if (Fp == 0, next);
        a1 = exq(Fp + b1, z); if (a1 == 0 || pollead(a1) != o || polcoef(a1, 0) == 0, next);
        E = a1*b1*K - 1; if (E == 0, next);
        if (E*Fp != o*x^al*a1 + b1, next);
        if (pollead(E) != o && pollead(E) != 2*o, next);
        if (polcoef(b1, 0) == 0 || polcoef(K, 0) == 0, next);
        E0 = polcoef(E, 0) * o; if (E0 == 0, next);
        key = [al, poldegree(a1), poldegree(b1), poldegree(K)];
        cur = if (mapisdefined(M, key), mapget(M, key), [0, 0, 0, 0]);
        cur[1]++; if (E0 != o && E0 != -o, cur[2]++); if (E0^4 == -o, cur[3]++);
        if (E0^(2*al) != o, cur[4]++);
        mapput(M, key, cur)))))));
  M;
}
