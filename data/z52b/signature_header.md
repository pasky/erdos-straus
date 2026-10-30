# z52b lane `signature` — signature matching for Erdős–Straus (ES is OPEN)

*Wave z52b, breadth-first, DONE (awaiting merge). Nothing here proves or claims ES; items are candidate connections, filtered only for
obvious nonsense.*

## Summary

{{HISTOGRAM}}

### 10 items I find most exciting
1. **signature-0001 — ES words are Frobenius numbers.** Brute-force-checked identity g(⟨tu, tv, u+v⟩) = tuv − u − v (Johnson gluing). So the (★)
   slice of ES ⟺ p is the Frobenius number of a glued 3-generated semigroup ⟨4Cu, 4CB, u+B⟩. Rosales et al. (Math. Scand. 2004) proved every
   integer is the Frobenius number of *some* 3-generated semigroup. That makes the (★) slice a structured restriction of a solved universality
   theorem; neighbours are signature-0002 to 0005. Not seen in the repo before.
2. **signature-0424 — Erdős–Tetali thin bases.** Random bases with Θ(log n) representations of *every* n. This is the only solved theorem in
   exactly ES's polylog pointwise regime, and it works because the witnesses are independent. Question for ES: how far are its witnesses from
   that independence?
3. **signature-0012 — Haag–Kertzer–Rickards–Stange.** Apollonian local-global fails through quadratic and quartic reciprocity, which is the
   closest published analogue of T1. Their refined conjecture has the same shape as "U(n) fails only at squares + a finite set".
4. **signature-0006 / 0008 — xy+yz+zx (Borwein–Choi) and Weinberger.** Same symmetric σ₂ as the ES surface, with an "all but at most one (or
   two) ineffective exceptions" theorem shape. A Siegel–Tatuzawa dichotomy on the BM characters χ_{−4uB} is a concrete target.
5. **signature-0019 — Maier's matrix method run on ES.** Build primes that are quadratic residues modulo many small primes, then test whether
   R(p)/M_BM(p) is systematically depressed. This is the most direct stress test of H⁻_BM.
6. **signature-0431 — triangle orbifolds.** ES(n) ⟺ some triangle orbifold S²(x,y,z) has Euler characteristic (4−n)/n. Riemann–Hurwitz then
   gives |G|(n−4) = 2n(g−1) for every finite quotient. This brings in triangle groups, quasiplatonic surfaces and genus spectra (0432, 0433).
7. **signature-0426 — Sawin–Shusterman.** Pointwise twin-prime and Chowla results over F_q[T] via étale cohomology. Test: does ES over
   F_q[T] (fixed large q, growing degree) have such a proof, and which moduli space of ES words would it use?
8. **signature-0016 — Ford-style anatomy model.** Witnesses should live at levels C ≲ (log p)^{log 2}; this is cheap to test against the
   smallest working level.
9. **signature-0449 — Paley–Zygmund rung.** R(p) ≥ c·log²p for a positive proportion of primes, from first and second moments. A likely
   provable intermediate theorem at the right order of magnitude.
10. **signature-0025 / 0030 — calibration pair.** Linnik's p + x² + y² is the solved dispersion analogue (its family length is n against ES's
    log p). Crocker's p + 2^a + 2^b has a polylog expected count and still infinitely many failures, which warns that the count alone proves
    nothing.

## Method
1. Wrote ES's structural signature as 40 features F01–F40, plus weakened variants, in `data/z52b/signature_features.md`. Items tag matched
   features by id.
2. Searched for problems sharing ≥ 3 features, solved ones first. Five research sub-agents covered:
   - erdosproblems.com, mostly the unit-fraction tag (#298–#327, #355, #825);
   - arXiv API keyword queries;
   - MathOverflow, Guy's UPINT and OEIS "numbers not of the form …";
   - problem lists outside analytic number theory: Zaremba, Collatz, Apollonian, Markoff, Frobenius, addition chains, SL₂ reachability,
     absorption, lonely runner, greedy expansions, triangle geometry;
   - classical solved pointwise theorems and the tool that cracked each.

   On top of that come the integrator's own matches and a systematic **feature-flip** pass (≥ 1 flip per feature: numerator 4→5/8/3, terms 3→2/4,
   positivity, S-integrality, totally real fields, cubic→quadric, symmetric→weighted, SL₂(ℤ)→SL₂(ℤ[i]), CF length 3→2, etc.). A first
   sub-agent run got a garbled prompt and produced generic topic items (`gen:sub-generic`); they were kept (minus duplicates) because they are
   not nonsense.
3. Filter: obvious nonsense, false premises and literal duplicates only. Three reviewer passes (`drops_1/2/4.json`) checked citations and
   small mathematical claims, dropped 25 raw items (false premise or duplicate) and fixed about 100 statements and citations. Examples: Weinberger
   allows at most *two* further idoneal numbers; Lenstra's paper is "Divisors in residue classes", Math. Comp. 1984; the ES cubic is
   multilinear, so there is no Vieta root swap. Integrator fixes are in `drops_3/5.json`. No barrier (B1–B6) screening was applied.
4. Two cheap computations were made along the way:
   - `scripts/z52b_signature_frob_check.py` checks the Frobenius identity (488 triples, 0 mismatches).
   - `scripts/z52b_signature_parity.py`: for primes p ≡ 1 (mod 4) below 1500 there are no diagonal solutions (x = y or y = z), so S₃ acts
     freely. The unordered count is odd for 58 of these primes and even for 58, so a Zagier-style parity argument has nothing to work with.

## Coverage notes and what I did NOT get to
- erdosproblems.com: the unit-fraction tag was covered well. Other tags (primes, divisors, additive bases, covering systems) were sampled only
  through specific items such as Crocker, Romanoff and Hough. A systematic pass over every tag remains to be done.
- Guy's UPINT was used only through secondary sources (D11 Egyptian fractions). The book's sections were not read directly.
- MathOverflow was searched by keyword (about 10 threads). Kourovka and Open Problem Garden were only skimmed by the sub-agent.
- Citations marked `unverified:` in refs are leads, not facts. Each such item is phrased as "check whether" or carries a citation flagged by
  the reviewer.
- None of the `first_step` computations was run, apart from the two scripts above. Natural cheap next batch: signature-0001/0002 (semigroup
  slices), 0016 (anatomy), 0019 (Maier primes), 0449 (second moment), 0465 (small-prime-factor witnesses), the OEIS queries for the U(n) and
  (★) failure lists, and the 5/n T1-analogue check.
- Physics, music theory and coding theory were skipped: no match with ≥ 3 features came up.
