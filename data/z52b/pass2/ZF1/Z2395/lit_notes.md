# Z2395 — de la Bretèche–Drappeau, arXiv:1703.03197v3 (JEMS 22 (2020)), read 2026-11-01
* Thm 1.1: for eta>0, Q <= x^{1+25/178-eta}, lambda bounded and well-factorable [FI83 p.199], D in Z non-square, V smooth compactly supported in R_+^*:
  sum_{q<=Q} lambda(q) ( sum_{n: q | n^2-D} V(n/x) - x Vhat(0) rho(q)/q ) <<_{eta,V,D} x^{1-eta/3}.
* Thm 5.2 (bilinear): M,N>=1, MN<=x^2, |a_m|,|b_n|<=1, (m,n)=1:
  sum a_m b_n ( sum_{k: mn | k^2-D} V(k/x) - x Vhat(0) rho(mn)/(mn) ) <<_{eps,D,V} x^{1/2+eps} M^{1/2} + x^{1+eps} N^{3/2-theta} M^{-1/4+theta/2}  (theta<=7/64 Kim–Sarnak).
  Thm 1.1 follows with M <= x^{1-eta/2}, N <= x^{25/178-eta/2}. General quadratic reduced to X^2-D via 4a(aX^2+bX+c)=(2aX+b)^2-(b^2-4ac).
* Constants depend on D (not uniform); variable n ranges over all integers ~x (no residue condition on n), modulus weights lambda(q) independent of n.
## ES check (derivation)
1. Residue condition on the modulus f ≡ a (mod K): allowed for FIXED K: chi(q) completely multiplicative => chi*(lambda1*lambda2) = (chi lambda1)*(chi lambda2) stays well-factorable,
   and in Thm 5.2 chi(mn)=chi(m)chi(n) is absorbed into a_m,b_n; cost phi(K) characters, constants unchanged in x.
2. ES Type I: f | p^2+4c^2 d, f ≡ -p (mod 4cd). With polynomial variable c (p fixed): 4d(4dc^2+p^2)... i.e. (2dc)^2 ≡ -d p^2 (mod f): D = -d p^2 depends on p,
   and the relevant range c <= p/(4d) gives |D| ≍ x^2 (x = range of c) -- outside "<<_D". Worse, the residue modulus 4cd depends on the polynomial variable c:
   1[f ≡ -p (4cd)] = phi(4cd)^{-1} sum_{chi mod 4cd} chi(-p)^{-1} chi(f) has characters whose modulus moves with the summation variable -> not of the form lambda(q) or a_m b_n (tied modulus).
3. With polynomial variable p (c,d fixed): D = -4c^2 d fixed, K = 4cd fixed -> applicable (twisted weights), and divisor switching f <-> (p^2+4c^2d)/f preserves the class -p
   (f f' ≡ p^2 ≡ (-p)^2), so level 1 already suffices; this is the averaged-over-p Type I count (B6), the route of the repo's (D)32 Type I note.
