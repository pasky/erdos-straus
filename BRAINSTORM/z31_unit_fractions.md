# z31 — Unit-fraction theorems: Bloom, Liu–Sawhney, Croot, Graham's 77, Sierpiński/Schinzel, Vaughan (O261 field memo 5; DEEP: Bloom)

Labels as in DISCOVERIES.md. Excerpts: `sources/lit2026g/{bloom_unit, croot_coloring, graham77, vaughan1970}.txt` (research
agent D; Bloom Thm 2, Croot's abstract, Graham's statement read verbatim; Vaughan's bound secondary). Builds on
BRAINSTORM/addcomb_unit_fraction_density.md, LITERATURE_2026, PARITY_AUDIT row E2 (Elsholtz–Tao).

## (a) Counterparts
1. **Bloom** (arXiv:2112.03726; JEMS 2025) Thm 2: "If A ⊂ ℕ has positive upper density … then there is a finite S ⊂ A such that
   Σ_{n∈S} 1/n = 1." Liu–Sawhney (arXiv:2404.07113) Thm 1.1: A ⊆ [1, N] with Σ_{A} 1/n ≥ (log N)^{4/5+o(1)} contains S with
   Σ_S 1/n = 1 (research agent, arXiv abstract).
2. **Croot** (Ann. Math. 157 (2003)): ∃ b: every r-colouring of [2, b^r] has a monochromatic S with Σ 1/n = 1.
3. **Graham 1963** (J. Austral. Math. Soc. 3): every integer > 77 is a sum of distinct positive integers whose reciprocals sum
   to 1; 77 is not.
4. **Sierpiński 5/n, Schinzel k/n**: open; same class as ES. Vaughan (Mathematika 17 (1970)): #exceptions ≤ N exp(−c(log N)^{2/3})
   (secondary). Elsholtz–Tao (arXiv:1107.1010): Σ_{p≤N} f(p) ≍ N log² N (up to log log), f(p) ≪ (log p)³ log log p for almost
   all p (abstract read by agent D; PARITY_AUDIT row E2 has the theorem numbers).
5. "Conway–Guy": research agent D found no Conway–Guy theorem on single-target unit-fraction existence (Guy's UPINT §D11 is a
   problem survey; the Conway–Guy sequence concerns distinct subset sums). **I could not identify what the brief meant; no
   claim is made.**

## (b) Pointwise? Mechanisms
* (1)/(2): **not pointwise in a target** — the target is fixed (= 1) and the freedom is a huge set of denominators (positive
  density, or Σ1/n ≥ (log N)^{4/5}). Mechanism: smooth-number restriction + Fourier analysis of Σ_{n∈S} 1/n mod 1 /
  random-subset second moment ("the number of S is enormous, exponential in |A ∩ [1, N]|").
* (3): **pointwise for every n > 77**, by an *affine self-similar recursion on the sum of denominators* (memory: if n works,
  so do 2n + 2 via 1 = 1/2 + Σ 1/(2x_i), and 2n + 9 via 1 = 1/3 + 1/6 + Σ 1/(2x_i), plus a finite base range). Count of
  representations: grows with n (at most the number of partitions of n, exp(O(√n)); R-O261 repair M8).
* (4): almost all only.

## (c) Transfer to B2
* **Bloom/Liu–Sawhney/Croot: blocked by F1 + F2.** ES fixes the *target* 4/p and allows 3 terms; Bloom fixes the target 1 and
  allows unboundedly many terms from a dense set. The ES count at p is ≍ log³ p (F2) versus exp(c|A ∩ [1, N]|) candidate
  subsets in Bloom. Bloom's Fourier step ("Σ_{n∈S}1/n lands in a short interval around 1 with the right probability") is a
  *distributional* statement for sums of many independent-ish terms; a 3-term sum has no central-limit behaviour.
  Sharp formulation of the gap (Assessment): Bloom's theorem is an additive-combinatorial Roth-type density theorem with
  the target fixed and the set varying; B2 is a single-target problem with the "set" (divisors of 4Cp + 1) supplied by p.
* **Graham's 77: blocked by the multiplicative structure.** Graham's recursion acts on the *sum of denominators* (an additive
  statistic), so n ↦ 2n + c preserves representability. For ES the parameter is a denominator of the target: the
  representability-preserving maps one knows are multiplicative, n ↦ mn (ES(n) ⟹ ES(mn)), which never reach a prime. What is
  PROVED in the campaign is narrower than "no recursion reaches primes": Mordell/B1-type statements that restricted finite
  menus of polynomial identities miss infinitely many primes ((J)3, (J)78–(J)79). A non-polynomial recursion is not excluded
  (R-O261 repair M9).
* **Sierpiński/Schinzel: INSTANCE-level siblings**, not counterparts: they are B2-type problems with numerator 5 or k, open
  for the same reasons; F5 (numerator 8 fails at 131, 241 for the single-prime event) shows that any proof of B2 must use
  the numerator 4 specifically, so even a proof of Schinzel's k/n for "large n" (which does not exist) would have to
  specialise differently.

## (d) Verdicts
Bloom / Liu–Sawhney / Croot: ANALOGUE (same equation family, different quantifier structure) — NOT SHARP.
Graham 77: ANALOGUE (pointwise, but via an additive recursion unavailable for denominators) — NOT SHARP.
Sierpiński 5/n, Schinzel k/n: same open class (UNRELATED as a source of mechanisms; INSTANCE of the same open problem type).
