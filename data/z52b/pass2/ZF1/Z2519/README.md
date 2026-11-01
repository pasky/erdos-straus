# Z2519 — ES (★) certificates vs the Strömbergsson–Venkatesh (SV) small-solution law
SV (Acta Arith. 118 (2005) 41–78; read from https://www.math.ias.edu/~akshay/research/andreas.pdf, Thms 1–4, Props 2–3):
for a uniformly random system of j linear congruences in n variables mod a prime p, the number of solutions in
p^{j/n}Ω has a limit law c_r = Haar measure of {lattices g : |Z^n g ∩ Ω| = r} (error O(p^{-δ})). For n = 2, j = 1
(homogeneous) this is the law of the lattice L_A = {(x,y): y ≡ Ax (mod p)}, A uniform: P(λ1(L_A) ≤ r√p) → 3r²/π (r ≤ 1).
Premise check: the item's "linear congruence mod 4cd" has the roles inverted — in every ES divisor form the modulus
(4uC−1, 4cdk−1, …) is the unknown and p is the residue, so SV (fixed modulus p, random coefficients) does not apply to it.
Exact linear dictionary used instead (PROVED, one line): p = 4uBC − u − B ⟺ B·A − p = u with A = 4Cu − 1, i.e. the
certificate is the solution (x,y) = (B,u) of y ≡ A x (mod p) with A = 4Cu − 1 (and the lift k = 1 exact).
Run: gcc -O2 -o z scripts/z52d_p2_ZF1_Z2519_sv_lattice.c -lm; ./z 1000000 1200000 4 100 1 > sv_1e6.txt;
     ./z 100000000 100012000 4 100 2 > sv_1e8.txt   (~2 min and ~7 min).
Columns: CDF over certificates of λ1(L_A)/√p; same for 100 uniform A per prime; Haar 3r²/π; CDF of ‖(B,u)‖/√p;
CDF over primes of min ‖(B,u)‖/√p; then the distribution of log_p max(B,u).
