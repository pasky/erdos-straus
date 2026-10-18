# R274 — hostile review of O262 (DISPROOF_AVENUES.md, BRAINSTORM/z32_*, scripts/logs z32_*)

Reviewer branch `side-agent/review-disproof`; author files merged from `side-agent/disproof-avenues`.
From-scratch scripts: `scripts/review_r274_*`. Labels as in DISCOVERIES.md. ES is not solved; nothing below changes that.

(Work in progress — verdict table filled claim by claim.)

## Verdict table

| # | claim | verdict |
|---|---|---|
| 1 | §1–2 citations (BL Thms 1.6/1.8/1.9, Rem 1.10; Markoff; Lyczak; Mihnea–Dumitru 10¹⁸; PW) | SOUND-AFTER-REPAIRS (D1, D2, D3) |
| 2 | Prop 3.1 (n = 1 shadow) | pending |
| 3 | §4.1–4.3 ladder counts, zero law, crossover law | pending (counts SOUND so far) |
| 4 | §4.4 expected-failure numbers | pending |
| 5 | §4.5 heavy tails self-refuting | pending |
| 6 | §5 adversarial search, hardest prime | pending |
| 7 | labels, P(ES false) < 10⁻³ | pending |

## Claim 1 — citations (§§1–2)

Checked against `sources/bright-loughran-1908.02526.pdf` (full text extracted), `sources/pw.txt`, and arXiv abstract
pages fetched 2026-10-18 (1807.10223 Loughran–Mitankin, 1808.01584 CT–Wei–Xu, 2202.07142 Dao, 2005.14013 Lyczak /
AIF 10.5802/aif.3529, 2509.00128 Mihnea–Dumitru). Full texts of the Markoff papers were NOT accessed (abstracts only).

* BL Thm 1.6 (Br U_n/Br ℚ ≅ ℤ/2, transcendental (−u₁/u₃, −u₂/u₃)): quoted correctly.
* BL Thm 1.8 (1.4), (1.5): quoted verbatim ("For all n ∈ ℕ"). But see D1: the proof (BL §3.8) uses "some prime
  p | n" with surjective local invariant (Lemmas 3.6, 3.7), so it needs n ≥ 2 (Thm 1.1 says n ≥ 2). At n = 1 the
  statement is false: by BL Lemma 3.1/3.5/3.8 the invariant is −1 at ∞ on U₁(ℝ)₊ and +1 at every finite place, so
  (U₁(ℝ)₊ × ∏ U₁(ℤ_p))^{Br} = ∅. n = 1 is BM-obstructed (Thm 1.2 with the empty product).
* BL Thm 1.9 and its proof (non-Zariski-density via (3.6) + Lang–Weil + [6, Lem 6.5]): quoted correctly.
* BL Rem 1.10: quoted correctly, but BL only says "versions of Theorems 1.5, 1.8, and 1.9 also hold" with no
  hypotheses stated (D2).
* PW Table 1 (`sources/pw.txt` l. 840–896): m = 8 exceptions 1, 2, 3, 11, 17, 131, 241 (N = 10¹³); m = 15: 32
  exceptions up to 20 521 (N = 10¹²), including n = 1…5, 8, 16, 34, 122, 226 (composites). Quoted correctly.
  PW §6: m = 5 to 10¹⁸, m = 6, 7, 8 to 10¹³: correct. PW Thm 1.1 (exception n > exp(m^{1/3−ε}) for m ≥ m(ε)) and
  Thm 1.2 (prime in (m², 2m²) for m ≥ 6.52·10⁹): quoted correctly in memo z32_numerator_ladder.
* Mihnea–Dumitru arXiv:2509.00128 exists (Aug 2025), abstract: "improving computational bounds to 10^{18}"; PW §6
  cites it as the record. It is an unrefereed preprint (D3).
* CT–Wei–Xu abstract: strong approximation fails away from any finite set of places; "for m ≠ 0, 4 the Brauer group
  does not control strong approximation". Dao abstract: "counterexamples to the integral Hasse principle which cannot
  be explained by the (algebraic) Brauer–Manin obstruction". Loughran–Mitankin abstract does not itself state the
  "infinitely many non-BM failures" claim; I could not access the body (it is the commonly cited content of LM Thm 1.4 —
  unverified here). Lyczak: AIF 2023, order-5 BM obstructions to integral HP on log K3 surfaces: correct.

## Defects

**D1 (MINOR→MAJOR for the "Reading", §1 bullet "BL Thm 1.8 (1.4)", §1 Reading 1, §3 Prop 3.1 Reading, §6 last
paragraph).** BL Thm 1.8 holds for n ≥ 2 only; for n = 1 there IS a Brauer–Manin obstruction (all finite
invariants trivial — Lemma 3.5 for odd p ∤ n, Lemma 3.8 at 2 — and inv_∞ = −1 on U(ℝ)₊). Consequences: (i) "no BM
obstruction to ES at any n" must read "at any n ≥ 2" (harmless for ES). (ii) The Prop 3.1 Reading calls n = 1 "the
**archimedean** exceptional point", contrasting it with n = m²; in BL's language both are *Brauer–Manin* points:
n = 1 is the n for which the real invariant −1 cannot be compensated because no prime divides n, and n = m² is
Cor 1.4 (derived from Thm 1.2). So §6's "find a third exceptional point of Ẑ × ℝ" programme should say that both
known exceptional points are BM-obstructed specialisations, and that a prime p can never be BM-obstructed (Thm 1.8,
n = p ≥ 2) — which sharpens, not weakens, the author's conclusion: a "prime T1" would have to be a non-BM
mechanism, unlike both known templates. *Repair:* replace "for every n ∈ ℕ" by "for every n ≥ 2 (BL Thm 1.1; at
n = 1 the Br-set is empty)"; replace "archimedean exceptional point" by "the BM-obstructed point n = 1 (empty
product in Thm 1.2)"; add one sentence to §6.

**D2 (MINOR, §1 Reading 2).** "8/n … 15/n failures with no BM obstruction (Rem 1.10 version of Thm 1.8)" overstates
what BL say: Rem 1.10 gives no hypotheses, and by D1 the m = 4 version already fails at n = 1; small exceptional n
such as 15/n with n = 1, 2, 3, 4, 5 (n ≤ m/3 region) are plausibly BM/real-obstructed. For n = 11, 17, 131, 241
(m = 8) the claim is plausible (prime n, n ∤ m) but not proved in BL. *Repair:* label as Assessment ("presumably not
BM-explained; BL Rem 1.10 states versions of Thm 1.8 without proof") and restrict to the prime exceptions n > m.

**D3 (MINOR, §2 bullet "Verification record", §4.5, §6 table).** "ES holds for all n ≤ 10¹⁸" rests on an
unrefereed arXiv preprint (PW cite it). §4.5's whole self-refutation argument is conditioned on it. *Repair:* say
"reported (Mihnea–Dumitru, arXiv preprint 2025; cited by PW §6)", and note that §4.5 also works with the refereed
Salez 10¹⁷ bound (the β-table changes only marginally — checked in Claim 5 below).
