# z52d Pass 2 — batch SK0 (86 items)
Counts: nothing 84 · interesting 1 (Z0245) · covered 1 (Z0665, depth doc: dividing_indep_qnr.txt l.8) · needs-compute 0 · skipped 0.
Interesting: Z0245 (numerators representable as 3 unit fractions are depleted in m≡0 mod 4: share 0.226 vs 0.25, stable over p ≤ 3·10^4).
Main negatives: Z0098 and Z0345 (norm-cone / Gaussian-conjugate versions are trivial without positivity), Z0265 and Z0271 (premises collapse to Z), Z0004 (no polylog support proved; data show a 21 % tail at p~3·10^4).
Not done (explicit in outcome_SK0.jsonl): Z0106, Z0257, Z0561, Z0666 (step not executable as specified or needs derivation), Z0619 (κ not fitted), Z0618 (table from memory).

## Z0245 — numerators ≡ 0 mod 4 are depleted among 3-term representable numerators (EVIDENCE)
- **What.** For prime p let A3(p) = #{m ≤ 3p, gcd(m,p)=1 : m/p = 1/x+1/y+1/z}. Among all such m with p ≤ 30000, the
  fraction with 4 | m is 0.226, against 0.25 for the uniform baseline on m coprime to p. The share is flat across p-bins:
  0.225 (p<1000), 0.225 (1000–5000), 0.225 (5000–10⁴), 0.225 (10⁴–2·10⁴), 0.227 (2·10⁴–3·10⁴).
- **Mod-8 shares of the representable numerators** (p ≤ 30000, 1,146,244 numerators): class 0: 0.112, class 4: 0.114, class 1: 0.125, class 2: 0.115, class 3: 0.138.
- **Why it might matter.** The Type I/II parametrisation (Mond–Portier arXiv:2201.11805 Lemma 2.1) has numerator
  m = (p+(a+b)/c)/(abu) or (1+p(a+b)/c)/(abu). The parity of m is then governed by the parity of abu and of the
  numerator, so a residue bias is plausible; the proportion of m ≡ 0 mod 4 among representable numerators is a
  positive-proportion statement that is not provided by the Mond–Portier or Luca–Pappalardi counting methods, which
  count all m uniformly. A lower bound of the order A3(p) for m ≡ 0 mod 4 would be what the item's question needs.
- **Reproduce.** `gcc -O2 -o a3 scripts/z52d_p2_SK0_a3.c -lm && ./a3 30000 > a3_p30000.txt` (≈100 s); columns 2–4 and 8–11
  give A3, #(m≡0 mod 4), and the mod-8 histogram 0..3 (class 4–7 counts = total − rest).
  Data: data/z52b/pass2/SK0/a3_p30000.txt. The C counter agrees with brute force for p ≤ 53.
- **Next.** Derive the residue distribution of m mod 4 from the Type I/II formulas; test whether 0.226 is forced by
  the parametrisation (e.g. by a count of (a,b,c,u) with abu odd versus even); extend to p ≤ 10⁶.
- **Caveats.** Only p ≤ 3·10⁴; mod-8 classes 5–7 are not printed separately; no proof.
