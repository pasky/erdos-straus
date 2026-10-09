# Referee report R120 — `paper/es-mn-short-note.tex`, round 3 (O113 Thm L′ section + O120 §9 "Under Selberg's eigenvalue conjecture")

Hostile referee (side agent, branch `side-agent/referee-mn-note`, merged `side-agent/mn-note-sel` at `cd68eb7`).
Compared against: `EXCEPTIONAL_MN3.md` + `reviews/exceptional-mn3-review.md`; `EXCEPTIONAL_MN4.md` +
`reviews/exceptional-mn4-review.md` (R117); `paper/es-typei-heegner-note.tex` ([HN]; compiled in `/tmp` to
read its numbering from the `.aux`); ET = arXiv:1107.1010v6. I did **not** re-access ET, PW, DI or Drappeau
for this round (ET/PW quotations were checked in R104; Drappeau in R117); I did not re-derive MN4 §§2–3
(R117 did, line by line) — §9 of the paper is a statement + sketch, and I checked it against MN4 and HN.

From-scratch checks: `scripts/review_r120_checks.py` → `.out.txt` (no author code; < 5 s; 0 failures):
* A. For m = 4..9 and primes 5 ≤ p < 110, p ∤ m (160 pairs), all ordered solutions of m/p = 1/x+1/y+1/z
  by exact rationals: every solution has p dividing exactly one or two denominators (never 0 or 3); a
  Type I solution exists ⇔ PW's (a,d,f)-condition (`f | ma²d+1`, `mad | p+f`) ⇔ some `w_{c,m}(p) ≥ 1`;
  a Type II solution exists ⇔ PW's (a,b,e)-condition; and `f_{I,m}(p) ≤ 2 Σ_c w_{c,m}(p)` (§9 reduction).
* B. Type II algebra of Prop 8.5: `p = (macd−1)e − ma²d`, `(e,a) = 1`, `(e,d) | p`, and
  `(made)(macd)(mab)^{1/2} ≤ 8 m^{1/2}(p+e)²` on 4130 tuples.
* C. Lemma 8.6(b)'s majorant `ρ(q₀) ≤ 1[(q₀,k)=1] Σ_{r|q₀} (−ka/r)` for odd q₀ < 400, k < 25, a < 13
  (57 600 cases) — the "only new input" of the coprimality gain.
* D. Lemma 8.4(a) normalised: for Y = 300 the LHS divided by `(φ(m)/m)log³Y + log²Y` is 1.35–1.44 for
  m = 4, 6, 30, 210, 2310, 30030 (no hidden m-dependence visible).
* E. Thm 9.3 case (i) (`L ≥ e^{20C}` ⇒ `CL/log L ≤ 0.65 log m` when `log m > L/10`) and case (ii)
  (`m > L⁵` ⇒ the two Thm L′ terms are `≤ m^{−2/5}log m/5`, `≤ m^{−3/5}log³m`, and `L ≤ m^{1/2}`) on grids.

## Verdict summary

| Claim (paper numbering, compiled) | Verdict |
|---|---|
| §8.3 set-up (Type I/II dichotomy, PW characterisations, list of losses) | **SOUND** (brute-forced, A) |
| Lemma 8.4 (two harmonic sums) | **SOUND-AFTER-REPAIRS** (m1: range of e) |
| Prop 8.5 (Type II) | **SOUND** (after m1) |
| Lemma 8.6 (ET Prop 1.4 with coprimality gain) | **SOUND** (re-derived; C) |
| Prop 8.8 (Type I with 1/m) | **SOUND** (re-derived hypotheses of Lemma 8.6 for the l = 30, k^{1/28} split) |
| Lemma 8.9 (very large m), proof of Thm L′ | **SOUND** |
| Thm L′ statement/label vs MN3 Thm L′ | **SOUND** (identical; header lists the inputs actually used) |
| §8.4 gap paragraph, Remark 8.10 | **SOUND-AFTER-REPAIRS** (m2: cite HN Thm 8.2, not only TTL) |
| Def 9.1 (SEL_m); "for m = 4 it is [HN, Hyp 1.1]" | **SOUND** (identical families, see §3) |
| Thm 9.2 statement vs MN4 Thm 4.1 | **SOUND**; label **SOUND-AFTER-REPAIRS** (m3: proof is in MN4, sketched here) |
| Thm 9.3 (Thm L″), incl. unconditional range m > L⁵ | **SOUND** |
| Cor 9.4 (sharp order) | **SOUND** (lower half conditional, upper = Thm U; quantifiers c_ε then m_ε) |
| Proof sketch of Thm 9.2: TTL→HN pointer mapping | **SOUND-AFTER-REPAIRS** (m4, m5: two pointers imprecise) |
| Remark 9.5 (what is unconditional) | **SOUND** (checked MN4 §6, LOGLOG2, HN §§9–10) |
| Abstract / intro / status / organisation / Problem 2 | **SOUND-AFTER-REPAIRS** (m6: dependency sentence) |

**No FATAL or MAJOR defect.** Six MINOR defects, all repaired in the paper (marked `% R120 repair`).

## 1. Thm L′ section (§8.3, O113)

Re-derived line by line against MN3 §2 and MN2 Prop 3.2 / Lemma 3.5:
* Prop 8.5: the three moduli `made`, `macd`, `mab`; product `m^{5/2}a^{5/2}b^{1/2}cd²e ≤ m^{5/2}a²b·ce·d² ≤
  2m^{1/2}(mabd)² ≤ 8m^{1/2}N²` (a ≤ b, ce = a+b ≤ 2b); hence one modulus `≤ (8m^{1/2}N²)^{2/5} ≤ 3m^{1/5}N^{4/5}
  ≤ 3N^{0.82}` (log m ≤ L/10). (i) class mod made with `(e,m) = 1` (as (e,m) | p, m < p) and `(e,ad) = 1`;
  (ii) `p ≡ −ma²d (mod macd−1)`, multiplicity τ₃(u); Lemma 8.4(b) needs `U ≥ m`, true; (iii) class `−e mod mab`.
  Totals as stated, using `φ(xy) ≥ φ(x)φ(y)` and `φ(m) ≫ m/log log m`, `log log m ≤ L`.
* Lemma 8.6 hypotheses in Prop 8.8: case (a) (linear d′, D′ ≥ max(A′, k^{1/28})) needs `kA′² ≤ D′^{30}` ✓ and
  `D′ ≥ ω(k)+2` ✓ (choice of m₀); case (b) (A′ > max(D′, k^{1/28})) needs `kD′ ≤ A′^{30}` ✓ (`kD′ < A′^{29}`).
  Λ ≤ 2 iff `D′ ≥ k^{1/3}log²(2kD′)`, implied by the stated `D′ ≥ k^{1/3}log²(2kX)`; `≪ log(2k)+log L` such dyadic
  boxes. `φ(k)/k ≤ φ(m)/m` as m | k. Block weight `≍ 1/j`, j ≤ 2L, sum `log L`. ✓
* Lemma 8.9 and the "consequence": `e^{CL/log L} ≤ m^{10C/log L}` in `log m > L/10`, and `L ≥ log(m/3)` when
  ρ_rep > 0. ✓
* Status/label: identical to MN3 Thm L′ (MN3's dependence on "MN2 Prop 3.2 / Lemma 3.5" is written out in the
  paper as Prop 8.5 / Lemma 8.9). "Effective" ✓ (BT, Shiu, PV, ET Thm 7.1 are effective).

## 2. §9 statements vs MN4

* Thm 9.2 = MN4 Thm 4.1 verbatim (absolute N₀, `4 ≤ m ≤ L⁵`, same bound). Thm 9.3 = MN4 Thm 5.1, with the
  conditional/unconditional split stated *more* precisely than MN4's header (MN4 labels the whole theorem
  CONDITIONAL; its case (ii) and (i) are unconditional — the paper is right). Cor 9.4 = MN4 Thm 5.2. No
  strengthening anywhere.
* Unconditional range `m > L⁵` (Thm 9.3 (i)+(ii)): re-derived (E). Note it is a disjoint union of
  `log m > L/10` (Lemma 8.9) and `log m ≤ L/10, m > L⁵` (Thm L′, whose `L ≤ m^{1/2}` holds as `L < m^{1/5}`). In
  case (iii) Prop 8.5 needs only `log m ≤ L/10` (true for N ≥ N₀). Thm 9.3 therefore covers **all** (m, N),
  including `L > m^{1/2}` (where it is conditional but trivial, as `L³/m ≥ L`). ✓
* The f_{I,m} definition (p | x, (p,yz) = 1, ordered y, z) is consistent with §8.3's "Type I" (p divides exactly
  one denominator; A). ✓

## 3. (SEL_m) vs [HN, Hyp 1.1]

For m = 4: `(q, 2md) = (q, 8d) = 1` ⇔ q odd and `(q,d) = 1`; level `mdq² = 4dq²`; even characters mod q ↔ even
characters mod 2q via `(ℤ/2q)^× ≅ (ℤ/q)^×` (q odd; −1 ↦ −1), and the nebentypus values on Γ₀(4dq²) agree (the
lower-right entries are odd). HN's d is the Type I d (HN §3, `Γ'_q = Γ₀(2d) ∩ Γ(2q)`, `M = 4dq²`), and MN4's
m = 4 normalisation (level md = 4d, `Γ(q)`) lands on the same levels. **The families are identical**; the
paper's claim is correct. The embedding into `L²(Γ₁(mdq²)\ℍ)` is correct (χ(δ) = 1 for δ ≡ 1 mod q | M).

## 4. TTL → HN theorem-number mapping (from HN's compiled `.aux`)

`hyp:sel` = Hyp 1.1; `L:2.1`, `L:2.2` = Lemmas 3.1, 3.2 (distance formula, uniform separation); `L:5.1` = Prop 5.1
(box variance); `L:6.1`/`L:6.2` = Lemma 6.1 / Thm 6.2 (per-d); `L:7.1` = Prop 7.1 ((K_a)); `L:1.1` = Lemma 8.1
(linearly degenerating savings); `L:8.1` = Thm 8.2 (SEL); `E:main` = Thm 9.9; intro Theorem 1 = Thm 9.9(i)
(HN says so); §9 = level-averaged exceptional spectrum, §10 = single-level estimates. **All pointers resolve
to the intended statements.** Two imprecisions: m4 (Lemma 3.2 is stated for HN's family 𝓕_d, not the level-md
family), m5 (HN's proof steps 1–5 are not MN4's/TTL's steps (1)–(5)).

## 5. Remark 9.5

Checked: MN4 §6 records only that the Kim–Sarnak strip transfers; LOGLOG2 and HN §9 treat m = 4 only. So
"open" is correct. The claim "even an m-uniform transfer of [HN, Thm 1] would only improve Thm L′ by an
unquantified o(1)": with `Σ ≤ Cε₀NL²log L/m + O_{ε₀}(NL²/m)` one gets `ρ_rep ≤ C(ε₀A³log L + C_{ε₀}A³)`, i.e.
`ρ_rep → 0` for `L ≤ K(m/log L)^{1/3}` with any fixed K — an unquantified improvement, not the exact scale. ✓
The (EFF) sentence is a correctly-hedged hypothetical. ✓

## 6. Abstract / intro honesty

Abstract: "conditionally on Selberg's eigenvalue conjecture … this loss disappears", "range in which it actually
uses the conjecture is m ≤ (log N)⁵", "not externally refereed" — all accurate. The sentence "The conditional
sharp order is proved relative to a further internal note … and an internal working document" omits that its
upper half is Theorem U (relative to [TQ]) and that its lower half also uses Prop 8.5 / Thm L′ (m6). Intro
paragraph after Thm L′ and the status paragraph are accurate (HN, MN4 internal only; SEL_m used only for
m ≤ L⁵). Problem 2 is consistent with Remark 9.5.

## Defects (all MINOR; all repaired in the paper, marked `% R120 repair`)

**m1 (Lemma 8.4(a), Prop 8.5(iii)).** Lemma 8.4(a) sums over `e ≤ Y`, but in Prop 8.5(iii) the e's are divisors
of `a+b ≤ 2Y`, so `e ∈ (Y, 2Y]` occurs and is not covered. The proof works verbatim for `e ≤ 2Y` (the per-e
bound `≪ log²Y/e` does not use e ≤ Y; `S′_m(2Y) ≪ (φ(m)/m)log Y`). *Repair:* lemma stated with `e ≤ 2Y`.

**m2 (Remark 8.10).** The conditional m = 4 result is cited only as `[TTL, Thm 8.1]`, a working document whose
(b3) display needed an erratum (R117 D1), while §9 relies on the paper version `[HN, Thm 8.2]`. *Repair:* cite
`[HN, Thm 8.2]` (written-up version of `[TTL, Thm 8.1]`).

**m3 (Thm 9.2 header).** The theorem is labelled "conditional … relative to the inputs of [HN, Thm 8.2] and
[MN3]" but its proof is **not** in this paper (only a sketch); it is in the internal working document MN4.
*Repair:* header now reads "… proof in [MN4], sketched below".

**m4 (sketch, "Heegner forms").** "cosh dist ≥ 3/2, uniformly in m, by [HN, Lemmas 3.1–3.2]": HN Lemma 3.2 is
stated for its family 𝓕_d (level d); for level md one needs `4md | disc(Q−Q′)`, which is MN4 Lemma 2.2_m.
*Repair:* "by the distance formula [HN, Lemma 3.1] and the argument of [HN, Lemma 3.2], since 4t | disc(Q−Q′)
[MN4, Lemma 2.2_m]".

**m5 (sketch, "Assembly").** "Steps (1)–(5) of the proof of [HN, Thm 8.2]": HN's proof has five steps, but its
division (1 short progressions, 2 bands/layers, 3 cell estimates, 4 sieve, 5 summation) is not MN4's (TTL's)
(1)–(5); MN4 also adds a step (2b-low) for `D ≤ L^{100}`. *Repair:* "The steps of the proof of [HN, Thm 8.2]
(numbered (1)–(5) as in [TTL] in [MN4, Thm 4.1]), with the extra low-D step, hold …".

**m6 (abstract).** Dependency sentence for the conditional sharp order incomplete (see §6). *Repair:* "proved
relative to the inputs above together with a further internal note …".

## Recommendation

**ACCEPT** the O113 and O120 additions with the R120 repairs (applied). Labels are accurate: Thm L′ PROVED
(relative to ET Thm 7.1 + modified proof of ET Prop 1.4; effective); Thm 9.2 CONDITIONAL on (SEL_m) (proof in
MN4, relative to HN's inputs); Thm 9.3 CONDITIONAL for m ≤ L⁵ and PROVED for m > L⁵; Cor 9.4(a) CONDITIONAL,
(b) PROVED (= Thm U, ineffective). The weakest link remains that §9's proof lives in an internal working
document (MN4) on top of an internally reviewed note (HN); the paper says so in the abstract, intro and
status paragraph.
