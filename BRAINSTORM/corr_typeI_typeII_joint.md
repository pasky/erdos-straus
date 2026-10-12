# BRAINSTORM (O146 c): joint Type I ∪ Type II at one p — is there a forced (anti-)correlation?

Status: brainstorm memo. **ES is not solved here.** Labels as in DISCOVERIES.md.

## 1. Idea

H-G (redteam-automorphic-2 §3) says that the union of Type I and Type II is "not an escape by itself", because the
union has the same 𝓛³ mass structure. That verdict is a statement about means. A union *could* still escape
if the two lotteries were **anti-correlated** at fixed p, i.e. if a forced mechanism made Type I rich exactly when
Type II is poor (e.g. complementary genus conditions: Type I needs `(−d/p) = −1` at its level, Type II needs
`(f/p) = −(−1/p)`). Then "both empty" would be much rarer than the product of the marginals, and possibly
impossible. Here we test this and look for the common driver.

## 2. Literature anchor

ET Thm 1.1 (means of f_I, f_II over primes; checked in `sources/elsholtz-tao-1107.1010.pdf`). Genus
conditions: POINTWISE_SPECTRAL Lemma 2.4, POINTWISE_TYPEII_SPECTRAL genus lemma, GEOMETRY_ES Props
5.1/5.2. I know of no literature on the joint distribution of (f_I(p), f_II(p)) (not searched beyond ET).

## 3. Exact structure

**Lemma 3.1 (twin slices; PROVED, elementary).** Let a, b, e ≥ 1 with `e | a + b` and `e² ≡ 1 (mod 4ab)`,
and put c = (a+b)/e. Then for every odd prime p,
`(a, b, c, (p+e)/4ab, e) ∈ V_II(p)` ⟺ `(a, b, c, (pe+1)/4ab, e) ∈ V_I(p)`.
*Proof.* `pe + 1 ≡ pe + e² = e(p + e) (mod 4ab)` and `gcd(e, 4ab) = 1`, so `4ab | pe+1 ⟺ 4ab | p+e`. The
remaining conditions (`a + b = ce`, d ≥ 1) are the same on both sides. ∎
Example: b = a + 1, e = 2a + 1. Check: over all 2021 primes p ≡ 1 (24) in [10⁵, 3·10⁵], the number of
solutions on twin slices is identical for the two types (4158 each), as the lemma forces. They make up 1.7%
of f_I and 3.8% of f_II (`scripts/bs_corr_count_twin.c`, `logs/bs_corr_twin_p24.txt`).

More generally, the {a,b} rows of Lemma 2.1 make **both** counts congruence data modulo 4ab (Type II:
`p ≡ −e`, Type I: `p ≡ −e⁻¹`, with e | a+b). Every coincidence `ee' ≡ 1 (mod 4ab)` between divisors of a + b
couples the two types. So the forced correlations are positive and of congruence type.

## 4. Experiment (`scripts/bs_corr_typeIII.py`, `bs_corr_profile.py`, `bs_corr_driver*.py`, `bs_corr_split.py`; logs `logs/bs_corr_{typeIII,profile,driver,driver2,driver3,split}.txt`)

Exact counts f_I, f_II (a ≤ b) for all 2021 primes p ≡ 1 (24) in [10⁵, 3·10⁵].
* **Positive, not negative, correlation.** corr(log f_I, log f_II) = 0.75 (Spearman 0.72). Of the 101 primes in
  the bottom 5% of f_I, 53 are also in the bottom 5% of f_II, against 5 expected under independence. The
  hardest primes are hard for both types. (All primes: Pearson 0.97, inflated by mod-4 effects.)
* **What drives it** (nested least squares on log f; residual correlation of Type I vs Type II):

| covariates | R²(I) | R²(II) | resid. corr |
|---|---|---|---|
| none | 0 | 0 | 0.75 |
| quadratic profile (ℓ/p), 5 ≤ ℓ ≤ 100 | 0.52 | 0.34 | 0.66 |
| + residue classes of p mod 5,7,9,11,13,16,17,19,23 | 0.65 | 0.48 | 0.59 |
| + log L(1,χ_p), shift richness Σ log τ((p+e)/4), … | 0.67 | 0.51 | 0.58 |
| + quartic / cubic residue symbols of 2,3,5,7 (non-abelian Frobenius data) | — | — | 0.583 → 0.583 (no change; measured on the large-modulus parts, `driver2`) |
| M2 + log p + C-slice counts with 4ab ≤ 200 | 0.72 | 0.56 | 0.54 |
| M2 + log p + C-slice counts with 4ab ≤ 200 and ≤ 2000 | 0.84 | 0.71 | 0.34 |

The common driver is congruence data of p modulo **composite** moduli 4ab, the {a,b} C-slices. Each further
decade of moduli removes more of it. At full scale this is tautological (every Type II solution is a
C-slice event with 4ab | p + e). Residue symbols of higher order add nothing, as the abelian structure of
Lemma 2.1 predicts (H-D data have no visible coefficient).

Splitting each count at q = 4ad = √p: the small- and large-modulus parts of the two types are all positively
correlated (0.45–0.76 raw, 0.26–0.62 after regressing out M2).

## 5. Barrier screen

* B1/B2: the only forced correlations found are congruence identities (Lemma 3.1 and the class overlaps
  modulo 4ab). They make Type I and Type II succeed together, so the union fails together.
* B5/T1: at odd squares both counts vanish identically. That is the extreme case of the positive correlation,
  where one genus obstruction kills both types.
* B3/B6: no counting route is proposed. The data are per-p, so there is no averaging over p in the claim; the
  statistics are over p only as EVIDENCE about the per-p joint law.
* H-D: the quartic/cubic test is a (weak, 8-symbol) negative data point for non-abelian input entering the counts.

## 6. Viability Assessment

**COLLAPSES (confirms H-G quantitatively).** There is a forced correlation between the two lotteries at fixed p,
but it is **positive**: shared quadratic profile plus shared congruence classes modulo 4ab (Lemma 3.1 is the
exact part). So "both empty" is much likelier than independence would suggest. The hardest primes for the
union are those that are hard for each type (bottom-5% overlap is 10× the independent rate). No hedge exists.
By-products: Lemma 3.1 (PROVED; checked on 2021 primes); EVIDENCE on the joint law of (f_I, f_II), including
a residual correlation of ≈ 0.58 that is not explained by small-prime data and is largely explained by C-slice
data at moduli ≤ 2000. Non-abelian residue symbols show no signal.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-B.md (§0.2, §0.3 and the
per-memo paragraph). Counterexamples, where computational, re-verified by `scripts/errata_check.py` (tag in brackets).

* **§6 "COLLAPSES" and "No hedge exists" are withdrawn.** Lemma 3.1 identifies a shared success subset, not an
  implication between failures of the full types. Correlation of f_I and f_II across primes, or over successful
  primes, says nothing about the joint-zero event: X = Y taking values in {1,2} is perfectly correlated and never
  zero. The twin slices are only 1.7 %/3.8 % of the counts; bottom-5 % statistics concern small positive values.
* Redteam-automorphic-2 Thm 2.2(iii) excludes only fixed finite unions. **Corrected verdict:** PARTIAL → H-A (H-G);
  the data remain EVIDENCE about positive values only.
