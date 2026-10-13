# AGENT REPORT O165 — H-B: parity-breaking at a fixed prime (checkpoint 1)

Main file: `PARITY_FIXED_P.md`. Scripts: `scripts/pf_dict_check.py`, `scripts/pf_mass.py`, `scripts/pf_spin.py`.
Logs: `logs/pf_mass_h1.txt`, `logs/pf_mass_1e8.txt`, `logs/pf_spin.txt`. **ES is not solved; no infinite case is claimed.**

## Results
1. **Dictionaries (PROVED, brute-checked).** Lemma 1.1: row II{a,d} hits ↔ triples (h,k,d) with (4dhk−1) | hn+k
   (bijection, all n ≤ 119). Lemma 1.2: Type I is p-free up to one congruence: ∃ m, k | m, f | 4mk+1, p ≡ −f (mod 4m).
2. **Spin lemma (PROVED).** For p ≡ 1 (4) and a prime ℓ | p+4a²d, ℓ ∤ 2pad: χ_{−4d}(ℓ) = (ℓ/p). On Type I slices,
   χ_{−4d}(ℓ) = +1 always. So the genus layer of Type II is "N_θ has a QNR-mod-p prime factor", and for Type I it is
   pure congruence data on p. 18950 instances were checked.
3. **Prop 2.1 (PROVED relative to Burgess; Brun's sieve at depth 2).** Among slices II{1,d} with (d/p) = +1, at most
   5/8 + o(1) are χ_{−4d}-obstructed. It passes T1: at squares, QNR primes have no roots. Numerics: the pass rate is
   0.39–0.60 at four p ≡ 1 (840) up to 10¹², and 0 at the controls 10001² and 100001².
4. **Main finding (Assessment).** H-B is mis-targeted. The parity/sign-type bad classes (prime, Q, Q′) need only
   *upper* bounds, and sieves give those without breaking parity. The irreducible layer is the canonical
   unit-coefficient divisor sum (★) R(p) = #{(j,f): f | p+j, f ≡ −1 (4j)}. That is a Type I/dispersion object, not a
   Type II one. Its best pointwise tool is Weil on the modular hyperbola xy ≡ 1 (mod 4p) (§3.4 dictionary), which falls
   short by p^{1/2}. So H-B collapses into H-A. This sharpens corr_parity_layers §4 and the triage's "untested
   coupling" question. It is mechanism-level, not a theorem (CONDITIONAL_ES Remark 2.4 still stands).
5. **EVIDENCE.** R(p) = 44, 52, 68 for p ≈ 10⁸, 10⁹, 10¹⁰ with p ≡ 1 (840), using the full range. Dyadic blocks hold 0–8
   successes each, and no block grows with p. Liouville sums over successes are O(√R), so the solutions show no
   parity bias.
6. **Construction log** (§4, I1–I8): weights; norm composition (an identity, but solutions are not transported);
   subset-product upgrade (rarer than the lottery); Weil on 𝓗; sign layer; joint sign+divisor (bounded gain ≤ 8/3);
   Möbius; windows. Each one records which barrier hypothesis it violates and why it still fails.

## Caveats for the reviewer
* The Prop 2.1 proof is short. Check the Burgess-in-progression step (moduli r ≤ p^{1/2+2ε}, length ≥ p^{1/2−3ε}) and
  the uniformity of o(1) when summing over pairs.
* Lemma 1.2 is likely folklore (Mordell/ET Type I in p-free form). Novelty is modest throughout.
* The 10¹² run covers only b ≤ 2·10⁹ of the range.

## Sparks (not pursued)
* Find exact-incidence counts on 𝓗 ∩ {4C | x+1, y+1} via the reciprocity x̄/4p + 4̄p̄/x ≡ 1/(4px). Is there a
  Farey/continued-fraction description of successes, i.e. "p/b has a convergent-like rational 1/(4C − 1/A)"?
* Type I and Type II both favour (d/p) = −1: Type I needs it (genus), and for Type II it makes χ_{−4d} automatic.
  Is there a joint Type I/II certificate on QNR levels d with more structure?
* For the full quadratic layer (all characters mod 4ad), a union bound over 2^{ω(q)} characters gives pass
  proportion → 1 like 1 − 2^{ω(q)}(log p)^{−1/2}. A precise theorem with uniform q might be a clean by-product.
* For the Vinogradov least-QNR trick: is there any multiplicative structure in the set of moduli b at which p is
  *not* forced? (No composition law was found; 4AC−1 is not closed under products.)
