# z52d Pass 2 — batch SK0 (86 items)
Counts: nothing 83 · interesting 2 (Z0245, Z0666) · covered 1 (Z0665, depth doc: dividing_indep_qnr.txt l.8) · needs-compute 0 · skipped 0.
Interesting: Z0245 (numerators representable as 3 unit fractions are depleted in m≡0 mod 4: share 0.226 vs 0.25, stable over p ≤ 3·10^4); Z0666 (residue model with general-m families: survivors first appear at m=8, where PW Table 1 first lists nontrivial exceptions).
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

## Z0666 — residue model for general m: survivors start where PW exceptions start (EVIDENCE, model only)
- **What.** Pomerance–Weingartner (arXiv:2511.16817) Props 2.1 and 2.3 give Type I families n ≡ −f (mod m·a·d) with
  f | m·a²d+1, and Type II families n ≡ −e (mod m·a·b) with e | a+b. Script `scripts/z52d_p2_SK0_avoid_m.py` runs the repo's
  residue model (same sampling as scripts/z52b_dividing_avoid.py, 2·10^7 samples, parameter products ≤ 3000) for general m.
  For m=4 it reproduces the repo's δ(1000) = 1.2·10^-4.
- **Survivor fraction δ at X=1000**: m=4: 1.2·10^-4 · m=5: <5·10^-8 · m=6: 1·10^-7 · m=7: 2.6·10^-6 · m=8: 7.4·10^-3 ·
  m=12: 4.8·10^-2 · m=15: 4.0·10^-3.
- **Comparison.** PW Table 1 (n ≤ 10^12) lists only the trivial exception n=1 (or n ∈{1,2}) for m=5,6,7, and first lists
  nontrivial exceptions at m=8 (n = 1,2,3,11,17,131,241). The model's survivors jump by ~3 orders of magnitude between
  m=7 and m=8, the same place.
- **Caveats.** Not a perfect ordering: m=4 has δ = 1.2·10^-4 but no known exceptions. The sampling uses the mod-840 classes
  chosen for m=4 and is not justified for other m. Only X ≤ 3000. The m=8..15 comparison is qualitative.
- **Reproduce.** `uv run --with numpy --with sympy python scripts/z52d_p2_SK0_avoid_m.py <m> 3000 20000000 5000000`
  (≈15–45 s each); outputs data/z52b/pass2/SK0/avoid_m{4,5,6,7,8,12,15}_X3000_2e7.txt.
- **Next.** Fit the m-dependence of ln δ over m=4..15 and compare with the per-decade PW exception counts.
