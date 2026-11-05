\\ z58 FFIELD: census of irreducible zeros of R_3 at degree n, restricted to P ≡ 1 (mod T^3 - T)
\\ (necessary at q = 3: P(c) = -1 gives the word d = T - c, u = 1; P(c) = 0 is impossible for irreducible P).
\\ Uses translation invariance R(P(T+1)) = R(P): only the lexicographically least translate (by lift coefficient
\\ vector) is decided; zeros of the other translates are listed by orbit.
\\ a* = least deg u of a witness (u the smaller cofactor), histogram over orbit representatives.
\\ Set n, part, nparts before reading.  Prints "ZERO <P>" lines and a summary line.
read("scripts/z58_ffield_decide.gp");
{
  my(q = 3, T3 = Mod(1, 3) * (x^3 - x), N = q^(n - 3), cand = 0, irr = 0, reps = 0, zer = 0, ah = vector(n));
  forstep (k = part, N - 1, nparts,
    my(P = 1 + T3 * ffmku(k, n - 3, q));
    cand++;
    if (!polisirreducible(P), next);
    irr++;
    my(P1 = subst(P, x, x + 1), P2 = subst(P, x, x + 2), key = Vec(lift(P)));
    if (lex(Vec(lift(P1)), key) < 0 || lex(Vec(lift(P2)), key) < 0, next);
    reps++;
    my(w = ffdec(P, q)); if (w == 0, zer++; print("ZERO ", lift(P)), ah[poldegree(w[1]) + 1]++));
  print("SUMMARY n=", n, " part=", part, "/", nparts, " candidates=", cand, " irreducible=", irr, " orbit_reps=", reps, " zero_reps=", zer, " hist a* (orbit reps)=", ah);
}
