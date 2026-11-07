# Z61 PIGEON — hostile non-author audit of board finalist F1

**ES remains OPEN. Verdict: bank the elementary criterion and the repaired asymptotic Linnik corollary; do not promote either to a positivity mechanism.**

Lane PIGEON, wave z61. Sources audited: board `~/.pi/boards/20261107-es-newmech/memo.md`, `items/fable.md` §fable-1, rounds 1–4 (especially `04-fable.md`). This auditor is not either board author. Labels: **PROVED** = mathematical statement using named established inputs; **CERTIFIED** = exhaustive exact-integer computation in the stated finite domain; **EVIDENCE** = empirical interpretation; **CONDITIONAL** = named unproved assumption; **CONJECTURE**; **Assessment**. No new conjecture or conditional analytic input is needed for the banked results.

## 1. Exact statements and proof audit

Let n ≥ 1, n ≡ 1 (4), ρ ≥ 3, ρ ≡ 3 (4), and M = M_ρ = (n+ρ)/4. Define

- W_ρ(n): there are positive a,b,c,d with 4abcd = a+b+nc and 4abd−n = ρ;
- S_ρ(n) = {u mod ρ : u | M, gcd(u,ρ)=1}, a **set of distinct unit residues**, not a multiset;
- PH_ρ(n): 2|S_ρ(n)| > φ(ρ).

At composite n, W means the unrestricted algebraic N_II family, not necessarily ET's coprime Type II family. At a prime p the coprimality is automatic, so W gives a genuine Type II ES solution.

### Proposition 1 — coprime-divisor collision and pigeonhole (PROVED)

For every such n,ρ, S ∩ (−S) ≠ ∅ iff W_ρ(n) has a witness with gcd(ab,ρ)=1. In particular PH_ρ(n) ⇒ W_ρ(n).

**Proof, every cancellation explicit.** The reverse implication follows because ab | M makes a,b divisors of M. For the forward implication choose u,v | M, both units modulo ρ, with u ≡ −v (ρ). Put g = gcd(u,v), a=u/g, b=v/g. Then gcd(g,ρ)=1, so division by g preserves the congruence. Moreover gcd(a,b)=1 and

ab = uv/g² = lcm(u,v)/g | lcm(u,v) | M.

Thus c=(a+b)/ρ and d=M/(ab) are positive integers, and 4abcd=c(n+ρ)=nc+a+b. Since ρ is odd and u is a unit, u≡v would give 2u≡0, impossible; no degenerate equal-residue collision is being used. Finally, |S|+|−S|>φ(ρ) forces their intersection in the unit group. ∎

**Audit:** valid for composite ρ too. Coprimality to ρ is essential; dividing a nonunit gcd is invalid. The relevant denominator is φ(ρ), not ρ−1 except at prime ρ. Counting divisors with multiplicity or merely having τ(M)>φ(ρ)/2 is not enough.

### Proposition 2 — prime-level iff, including nonunits (PROVED)

If ρ is prime, then

W_ρ(n) ⇔ [S ∩ (−S) ≠ ∅] or [ρ² | M].

**Proof.** A witness satisfies ab | M and ρ | a+b. If ρ ∤ ab, Proposition 1 applies. Otherwise primality forces ρ | a and ρ | b, hence ρ² | ab | M. Conversely the second alternative gives (a,b,c,d)=(ρ,ρ,2,M/ρ²). ∎

At a prime input p≡1 (4), prime ρ≡3 (4) is distinct from p, so gcd(M,ρ)=1 and the second alternative is impossible. More generally, **at prime p the collision iff holds for every admissible level, including composite levels**: every witness obeys

ρ ≤ a+b ≤ ab+1 ≤ M+1 = (p+ρ)/4+1, hence ρ ≤ (p+4)/3 < p.

For every ρ in this complete range, gcd(M,ρ)=1: a common prime divisor would divide p and be ≤ρ<p. Consequently the full prime-input question is

∃ ρ≡3 (4), 3≤ρ≤(p+4)/3, with S_ρ(p) ∩ (−S_ρ(p)) ≠ ∅.

For arbitrary n the same bound ρ≤(n+4)/3 holds for every witness. Since PH produces a witness, **there can be no pigeonhole level beyond that bound either**. This justifies the global finite census below. Also abd=M≤(p+1)/3<p, proving gcd(abd,p)=1 and the genuine Type II assertion. The denominators are (abd, acdp, bcdp).

### What was false or overstated in the item

1. **Deficient ⇒ few divisors/nearly prime: false**, already withdrawn in round 2. For example ρ=7, n=4·2³⁷−7=549755813881 gives M=2³⁷, τ(M)=38, but S={1,2,4}, exactly half the six units. More generally multiplicity can grow without increasing the residue set. No pointwise short-block factorisation theorem follows from the lemma.
2. **105 is not an N_II-zero.** At ρ=3, M=27, (a,b,c,d)=(3,3,2,3) works via the ρ²|M alternative. It is a U_II-zero and a pigeonhole failure. Round 2 correctly repaired the original item.
3. **Ratio, not single divisor.** At p=1153,ρ=7, S={1,2,3,5} contains no −1, but 2+5≡0 and (2,5,1,29) works. The round-4 ratio repair is necessary.
4. **Only N_II=0 implies every level is PH-deficient.** R=0 for the c=1 sub-line does not: p=409,ρ=7 is a PH hit. The board withdrew that separate overreach in round 2.

## 2. Patched Linnik corollary: source-pinned audit

Put α=1/(4√e), where e is Euler's number, and let q=n_p be the least positive quadratic nonresidue modulo the prime p≡1 (4). The least such integer is prime: a composite nonresidue has a smaller nonresidue prime factor. Also q<p, so gcd(p,4q)=1.

### External inputs actually checked

**Burgess (primary source).** D. A. Burgess, *The distribution of quadratic residues and non-residues*, Mathematika 4 (1957), 106–112, **Theorem 2, p.107**, states n_p=O(p^a) for every fixed a>α. The downloaded page image was inspected because PDF text extraction corrupts the exponent. Thus for each δ>0,

n_p ≤ C_δ p^{α+δ}.

Theorem 1 and §5, p.112, give the character-sum/Vinogradov argument. Its applicable modulus is the **prime p**, not the possibly composite shift ρ. Source: https://www.cs.umd.edu/users/gasarch/TOPICS/res/burgess.pdf ; DOI https://doi.org/10.1112/S0025579300001157 . Cross-check: McGown–Treviño, *The least quadratic non-residue*, §2, Theorems 2.4/2.6 and the deduction on p.6, https://campus.lakeforest.edu/trevino/SurveyLeastNonResidue.pdf ; repo `sources/lit2026/lau-wu-least-quadratic-nonresidue.txt` equation (1.5).

**Linnik–Xylouris (primary source).** T. Xylouris, *Über die Nullstellen der Dirichletschen L-Funktionen und die kleinste Primzahl in einer arithmetischen Progression*, Bonn dissertation (2011), **Theorem 2.1, p.12**: P(Q)≪Q⁵, with an effectively computable implied constant. Here P(Q) is defined on p.9 as the worst least prime over all reduced residue classes modulo Q. See also (2.6), p.10. Source: https://bib.math.uni-bonn.de/downloads/bms/BMS-404.pdf ; institutional record https://bonndoc.ulb.uni-bonn.de/xmlui/handle/20.500.11811/5074 .

This is an unconditional theorem, uniform in the reduced class, with a multiplicative constant. It is **not** a bound with constant 1 for every modulus. The thesis distinguishes its exponent 5 from the earlier paper's 5.18; do not cite the earlier paper as the exponent-5 theorem. Theorem 2.2(a)'s ineffective large-modulus threshold is unnecessary here. Source statements/hypotheses and their use are audited; this is not an independent re-proof of Xylouris's analytic/numerical estimates. Download hashes and verification details are in `data/z61/pigeon/source_audit.md`.

### Theorem 3 — corrected quantitative non-confinement (PROVED)

Let L be an admissible uniform Linnik exponent (L=5 suffices). For every ε>0 and every prime p≡1 (4), there is a prime ρ_L such that

ρ_L ≡ −p (mod 4n_p),    ρ_L ≪_ε p^{L/(4√e)+ε},    n_p | M_{ρ_L},    (n_p/ρ_L)=−1.

In particular S_{ρ_L}(p) contains a quadratic nonresidue. For every fixed

0<ε<1−L/(4√e),

and **all sufficiently large p**, one can choose

ρ_L ≤ p^{L/(4√e)+ε} < (p+4)/3.

For L=5, L/(4√e)≈0.75816<1. An older exponent 5.5 would also suffice for sublinearity; exponent 5 is not essential to this qualitative conclusion.

**Proof, step by step.**

1. The progression class −p modulo 4q is reduced since q<p and p is odd. It is 3 modulo 4. Linnik gives a prime ρ_L≡−p (4q), with ρ_L≤C_L(4q)^L. Consequently ρ_L≠q and ρ_L≠p.
2. The congruence is exactly 4q | p+ρ_L; hence q | M. Since ρ_L≠q, q mod ρ_L is in S.
3. For an odd prime ℓ | M, necessarily ℓ≠p,ρ_L. Quadratic reciprocity gives

   (ℓ/ρ_L) = (−ρ_L/ℓ) = (p/ℓ) = (ℓ/p).

   The first equality uses ρ_L≡3 (4), the middle equality p≡−ρ_L (ℓ), and the last p≡1 (4).
4. If ℓ=2 | M, then ρ_L≡−p (8). The supplementary law gives (2/ρ_L)=(2/p), since the symbol is unchanged under negation of an odd residue modulo 8. Explicitly p≡1 (8) gives ρ_L≡7 (8) and both signs +1; p≡5 (8) gives ρ_L≡3 (8) and both signs −1. Applying steps 3–4 to ℓ=q proves (q/ρ_L)=−1.
5. Use Burgess with δ=ε/(2L). Then

   ρ_L ≤ C_L 4^L C_δ^L p^{Lα+ε/2}.

   For sufficiently large p the fixed constant is at most p^{ε/2}. This proves the coefficient-1 asymptotic statement. If Lα+ε<1, p^{Lα+ε}=o(p), giving the complete-range inequality. Keeping a constant instead yields the all-prime ≪_ε version. ∎

**Required corrections to round 4.** Its line “ρ_L≤(4n_p)^L≤p^{L/(4√e)+ε}<(p+4)/3” drops both constants and a large-p qualification. Its claim that 2|M forces ρ_L≡7 (8) is false for p≡5 (8); p=5,ρ_L=3,M=2 is the smallest example. The equality of characters nevertheless holds by step 4. These are repairable scope/proof defects, not a failure of the asymptotic corollary. No GRH, Dickson hypothesis, or average-over-p theorem is used.

### What non-confinement does NOT prove

For prime ρ≡3 (4), its unit group is cyclic of order 2m with m odd. A subgroup avoids −1 iff it has odd order, hence lies in QR_ρ. Thus Theorem 3 ensures −1 is in the group **generated** by S. It does not ensure −1∈S·S⁻¹: divisors have bounded prime-exponent budgets.

At the Linnik-selected level, W_ρ(p) is still exactly the collision question, not an equivalence between full Type II at p and a collision at this one level. **Concrete counterexample to that stronger reading:** p=601, q=7, least prime ρ_L≡−601 (28) is 43; M=161=7·23 and S={1,7,23,32} contains nonresidues but S∩(−S)=∅. Yet ρ=7 works, e.g. (a,b,c,d)=(2,19,3,4). Likewise the selected levels for 67369 and 87481 are 43 and 331 and both fail. Certificates: `linnik_fixtures.json`.

“Starved” can correctly mean **S⊄QR_ρ and S∩(−S)=∅ at that prime level**. A hypothetical Type II counterexample would have such a level (for sufficiently large p). It is not proved that every hard prime's every level, or least level, lies in this branch. Many least levels are composite; the cyclic prime-group argument does not apply there (at ρ=15, {1,11} avoids −1 but contains a Jacobi nonresidue).

## 3. Census reproduction (CERTIFIED)

Script: `scripts/z61_pigeon_audit.py`; all arithmetic is exact, no probabilistic primality or floating-point comparisons. A smallest-prime-factor sieve generates primes, divisors and totients. Least witnesses are found by **direct enumeration of ab | M and ρ | a+b**, checked against unit collisions; PH is separately computed from distinct unit divisor residues. For each prime without a PH hit through 400, every remaining admissible ρ through ⌊(p+4)/3⌋ is checked. The complete bound in §1 excludes all later levels.

| Claim | Independent result |
|---|---:|
| Primes p≡1 (24), p≤2,000,000 | 18,507 |
| PH holds at the least working ρ | 18,217 (98.43%) |
| Least ρ≥50 | 9 |
| PH holds at those nine least levels | 0/9 |
| No PH level ≤400 | 17 |
| No PH level anywhere | exactly the same 17 |

The original board `/tmp/f1_census.py 2000000 400` scans only through **403**, due to `range(RMAX//4+1)`. It therefore did not itself justify “17 have none at all.” Astra independently completed two cases. Our full extensions supply the missing certification for all 17; the off-by-one does not change these results.

| p | least ρ | occupancy / φ(ρ) there | least PH level |
|---:|---:|---:|---:|
| 87481 | 63 | 8/36 | none |
| 118801 | 59 | 16/58 | 63 |
| 386401 | 55 | 15/40 | none |
| 496609 | 51 | 8/32 | 63 |
| 529489 | 51 | 16/32 | 95 |
| 532249 | 55 | 20/40 | none |
| 806521 | 59 | 12/58 | none |
| 1430641 | 71 | 18/70 | 159 |
| 1450849 | 59 | 12/58 | none |

The complete PH-zero list is

18481, 67369, 87481, 94441, 386401, 427249, 474049, 532249, 546841, 670849, 806521, 878089, 944329, 1282009, 1299601, 1450849, 1915201.

At 67369 the first full witness is (3,137,4,41), ρ=35, occupancy 8/24. At 87481 it is (1,62,1,353), ρ=63, occupancy 8/36. At the outside-census record 8803369, the least ρ is 107, occupancy 36/106, intersection {1,11,14,93,96,106}; its first PH level is 151. All reproduced independently.

**EVIDENCE/Assessment:** the half-density condition explains the bulk but none of this nine-prime hard tail's *first* witnesses. Four of the nine do have later PH levels. The 17 finite counterexamples refute all-prime PH positivity; they do **not** refute eventual PH positivity or every future growing-block strategy. Nothing here proves an asymptotic hard-tail frequency.

## 4. Mandatory falsifiers

Screen inputs are the four files in `data/z58/screens/`; their SHA256 hashes are recorded per certificate in `screens.json`. Existing zero claims for the restricted screen families are used as fixtures, not re-certified to their original 10¹⁰ range. What is independently certified here is the listed full-family rescue/absence and PH status.

| Falsifier | Mathematical distinction and exact check |
|---|---|
| **Odd squares n=m²** | PH never fires; neither does full N_II. For unit divisors the Jacobi character (·/ρ) is +1 on every prime factor coprime to ρ, hence on S, but is −1 at −1; thus the occupancy is at most φ(ρ)/2. Do not claim this for nonunit prime factors: n=121,ρ=11 gives M=33 with (11/11)=0. The full square obstruction, including nonunit witnesses, is the standard (n/f)=−1 contradiction for f=4acd−1. Our exhaustive new-lemma test covers all n≡1 (4)≤2001 and every possible level, including their odd squares. |
| **Numerator-8 / C-even (★) sub-line** | The lemma produces arbitrary c,d; it does not force c=1 or d even. Full d-even Type II instead requires ρ≡−n (8) and ab dividing (n+ρ)/8, so its PH test must use divisors of M/2. At all 12 `r8_zeros_1e10.txt` inputs, a full first witness exists at ρ≤15 and is a PH hit; separately a d-even witness exists at ρ≤31, always c≥2. This rescues the full family, not the false c=1,d-even sub-line. Example n=10156800001: (17,53,10,2818202), ρ=7, is d-even. |
| **Composites / 4545** | Of all 285 `composite_zeros_le8e6.txt` inputs, 284 have full witnesses with least level ρ≤51; 202 of those first levels are PH hits. At 4545 none exists through the complete bound 1516, hence PH never fires. At ρ=11, M=1139=17·67, S={1,6} contains a quadratic nonresidue but has no opposite pair: escape alone fails. The 105 witness uses the prime-level nonunit alternative and PH fails at every level. Composite-input N_II witnesses need not be ET-coprime. |
| **Known prime zeros of restricted lines** | All 14 `star_prime_zeros.txt` inputs have first full witnesses at ρ≤23, all with c≥2; 13/14 first levels are PH hits. All 38 `gstar_zeros.txt` inputs have first full witnesses at ρ≤23, with 36/38 PH hits. No witness for either restricted zero family is claimed. |
| **Pigeonhole-specific zeros** | All 17 primes in §3 have no PH level anywhere despite full witnesses. This is a genuine falsifier of unqualified PH positivity, not a falsifier of the lemma's sufficient implication. |

For completeness, the full square obstruction used above is short. A witness gives f=4acd−1, −n≡ac⁻¹ (f), with ac a unit. If k=ac, then (k/f)=1: write k=2^t k₀; reciprocity and f≡−1 (4k₀) give (k₀/f)=1, and t>0 gives f≡7 (8), hence (2/f)=1. Since f≡3 (4), (n/f)=−1, impossible for n=m². At prime ρ dividing m, v_ρ((m²+ρ)/4)=1 also directly excludes the extra ρ²|M branch.

## 5. Novelty against the repository

Checked with `git grep` and direct reading, not just title matching:

| Existing result | Relationship to F1 |
|---|---|
| `Z58_CONVF.md` Lemma 1.1(E5), Lemmas 1.2–1.3 | Same σ=ρ form, sub-lines and square obstruction. Not new. Its Lemma 1.5 already identifies the exact ρ=3 criterion. |
| `Z59_CONVO.md` Criterion 3.1, Lemmas 3.3 and 4.1, §4 | Exact ρ-ratio criterion, global factor colouring, and explicit nonresidue-without-witness counterexamples already exist. The gcd reduction identifies that ratio set with S·S⁻¹ when all divisors are units; new presentation, not new solvability content. Its least-ρ census already extends to 10⁸. |
| `Z57_BFII.md` Lemma 1.1(a), Proposition 2.2, Corollary 2.4 | Full algebraic family, Jacobi obstruction and least-nonresidue witness constraint are prior. No new main-term or remainder bound here. |
| `JOINT_BUDGET.md` §3, §4.1 and Remark 4.4 | Coprime divisor-ratio window, exponent budget/Kneser criterion, and “nonresidue gives generated subgroup, not the bounded box” are prior. |
| `LONGSHOT_PIGEONHOLE.md` Lemma 1.1(iv), Lemma 1.2, §§1.3–1.4 | The signed exponent box and factor-colour identity (including 2) already appear. Its equal-residue pigeonhole gives the wrong sign; F1 instead assumes **distinct-residue half-density**, a stronger input that legitimately forces the opposite-sign target. These statements do not contradict each other. |
| `CAP_POINTWISE.md` §1; `BRAINSTORM/z52b_tools.md` item 55 | Linnik for auxiliary prime windows and even the class −p mod 4C are already suggested/used. I did not locate the exact choice C=n_p with the composed exponent L/(4√e) in these or the named memos. |

**Assessment of incremental content:** the compact half-density sufficient test; explicit nonunit prime-level alternative; source-checked quantitative construction of a *non-confined prime* level; and the PH-vs-least-witness census with complete PH zeros. The elementary iff is a repackaging of the existing ratio criterion, and the Linnik consequence is a standard composition, not a new analytic input. The substantive remaining collision/exponent-budget problem is already documented. Do not describe this as a new solution mechanism or a proof that every future mechanism is impossible.

## 6. Reproducibility and validation

```sh
ulimit -v 4000000
timeout 1800 uv run --no-project python scripts/z61_pigeon_audit.py check --limit 100000
timeout 1800 uv run --no-project python scripts/z61_pigeon_audit.py census
timeout 1800 uv run --no-project python scripts/z61_pigeon_audit.py screens --limit 100000
```

Standard library only. Sieve storage is O(limit), eight bytes per sieve index plus a prime list; census default limit 2,000,000. Divisors are generated for one integer at a time. Large screen integers are factored by trial division using the prime table, never by allocating to the screen input's magnitude. No Cartesian-product arrays. Each run is bounded by the stated memory/time limits.

Existing `scripts/z59_convo_check_lemmas.py` already checks the original equation; the added checks target the **new** gcd-collision implication, prime-level nonunit iff and character-2 repair. `checks.json`: 41,917 complete levels and 12,998 factor-colour comparisons pass. The direct divisor-pair enumerator cross-checks the intersection result without assuming Proposition 1 in its search. Every emitted witness is substituted into the original integer equation. The 349 input rows are preserved individually in `screens.json`.

Files under `data/z61/pigeon/`: `census.csv` (all 18,507 primes), `census_summary.json` (hard cases and complete absence bounds), `checks.json`, `screens.json`, `screen_summary.json`, `fixtures.json`, `linnik_fixtures.json`, `source_audit.md`. First checkpoint commit banks the lemma and complete census; final audit remains on this lane branch, **not merged**.

## 7. Proposed FRONTIER text (proposal only; FRONTIER not edited)

> **Divisor-residue pigeonhole audit (z61, `Z61_PIGEON.md`; PROVED + CERTIFIED).** For M_ρ=(p+ρ)/4, ρ≡3 (4), let S be its distinct unit-divisor residues modulo ρ. If |S|>φ(ρ)/2, opposite residues and gcd cancellation give Type II. At prime ρ the general-input iff is S∩(−S)≠∅ or ρ²|M_ρ; at prime p all admissible levels have gcd(M_ρ,ρ)=1, so the collision iff holds even for composite ρ. This repackages the prior ρ-ratio criterion, not a positivity theorem. Source-checked Burgess + Linnik (L=5) gives, for every fixed 0<ε<1−5/(4√e) and all sufficiently large primes p≡1 (4), a prime ρ_L≡−p (mod 4n_p), ρ_L≤p^{5/(4√e)+ε}<(p+4)/3, whose divisor set contains a quadratic nonresidue. It does **not** force a collision, nor reduce full Type II to that one level. Independently reproduced: 18,217/18,507 (98.43%) least witnesses at p≡1 (24), p≤2·10⁶, satisfy PH, but 0/9 with least ρ≥50; exactly 17 primes have no PH level anywhere (complete searches), including 67369 and 87481. All-prime PH positivity is false; eventual positivity is not excluded. **Assessment: useful criterion/census, no new forcing mechanism; ES remains OPEN.**
