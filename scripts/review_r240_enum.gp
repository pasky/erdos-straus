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
gg = ffgen([3,2], 'a);
o = gg^0;
EL = vector(9, k, ((k-1)%3 + ((k-1)\3)*gg) * o);
TF(P) = polcoef(P, 0) != 0;
ismon(P) = pollead(P) == o;
\\ result accumulators (global): CNT[1] = all slices, CNT[2] = P8 (E(0)^4 = -1), CNT[3] = law failures, CNT[4] = duplicates
chk(s, a, z, y, t, m, w, C, g, v) = {
  my(E0);
  if (poldegree(m) != z || poldegree(w) != a || poldegree(C) != s-a-z || poldegree(g) != y || poldegree(v) != t, return(0));
  if (!ismon(m) || !ismon(w) || !ismon(C) || !ismon(g), return(0));
  if (!TF(m) || !TF(w) || !TF(C) || !TF(g) || !TF(v), return(0));
  if (m*w*C != x^s + v || w + C != g*v, return(0));
  E0 = (polcoef(w,0)*o) / (polcoef(C,0)*o);
  CNT[1]++;
  if (E0^4 == -o, CNT[2]++);
  if (E0^s != (-1)^(t + t*z + z*(1+s) + t*s) * o, CNT[3]++);
  if (E0 == -o, CNT[3]++);
  1;
}
\\ the k-th (0 <= k < nmon(d)) polynomial lead*(monic of degree d with nonzero constant term); all coefficients t_FFELT
nmon(d) = if (d == 0, 1, 8 * 9^(d-1));
mk(d, k, lead = 1) = {
  my(P = lead * o * x^d, c);
  if (d == 0, return(lead * o));
  P += lead * EL[2 + k % 8]; k \= 8;
  for (i = 1, d - 1, c = k % 9; k \= 9; P += lead * EL[c + 1] * x^i);
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
