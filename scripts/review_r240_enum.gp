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
\\ iterate monic T-free polynomials of degree d (lc lead), calling f
itp(d, f, lead=1) = {
  if (d == 0, f(lead*o); return);  \\ all coefficients are t_FFELT (never t_INT)
  forvec(v = vector(d, i, [0, 8]), if (v[1] > 0, f(lead*o*x^d + sum(i = 1, d, EL[v[i]+1] * x^(i-1)))));
}
divs_deg(P, d) = {
  my(L = divisors(factor(P / pollead(P))), R = List());
  for (i = 1, #L, if (poldegree(L[i]) == d, listput(R, L[i] / pollead(L[i]))));
  Vec(R);
}
pattern(s, a, z, y, t, route) = {
  my(b = s - a - z, Ts = o*x^s, lam = if (a < b, 1, 2), dE = z + y + a);
  CNT = vector(4);
  if (route == 1,
    itp(z, m -> itp(a, w -> itp(y, g -> my(den = g*m*w - 1, C, v);
      if (den != 0, my(num = w + g*Ts); if (num % den == 0, C = num / den; v = m*w*C - Ts; chk(s, a, z, y, t, m, w, C, g, v)))))));
  if (route == 2,
    itp(t, v -> my(P = Ts + v, Lm = divs_deg(P, z));
      for (i = 1, #Lm, my(m = Lm[i], Q = P / m, Lw = divs_deg(Q, a));
        for (j = 1, #Lw, my(w = Lw[j], C = Q / w, gq);
          if ((w + C) % v == 0, gq = (w + C) / v; chk(s, a, z, y, t, m, w, C, gq, v))))), lam));
  if (route == 3,
    itp(z, m -> itp(y, g -> my(P = 1 + Ts*m*g^2, LE = divs_deg(P, dE));
      for (i = 1, #LE, my(E = LE[i], Ep, w, C, v);
        if ((E + 1) % (m*g) == 0, w = (E + 1) / (m*g); Ep = P / E;
          if ((Ep + 1) % (m*g) == 0, C = (Ep + 1) / (m*g); v = m*w*C - Ts; chk(s, a, z, y, t, m, w, C, g, v)))))));
  if (route == 4,
    itp(a, w -> itp(y, g -> my(P = g*Ts + w, LE = divs_deg(P, dE));
      for (i = 1, #LE, my(E = LE[i], C = P / E, m, v);
        if ((E + 1) % (g*w) == 0, m = (E + 1) / (g*w); v = m*w*C - Ts; chk(s, a, z, y, t, m, w, C, g, v))))));
  if (route == 5,
    itp(z, m -> itp(a, w -> my(P = Ts + m*w^2, LE = divs_deg(P, dE));
      for (i = 1, #LE, my(E = LE[i], v = P / E, C, g);
        if ((Ts + v) % (m*w) == 0, C = (Ts + v) / (m*w);
          if ((w + C) % v == 0, g = (w + C) / v; chk(s, a, z, y, t, m, w, C, g, v)))))));
  CNT;
}
