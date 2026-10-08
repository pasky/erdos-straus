# AGENT REPORT O97 — `paper/es-mn-short-note.tex` (draft, 18 pp., 10pt amsart)

Branch `side-agent/mn-short-note`. Title: "The exponent 3/4 for the exceptional set of m/n, in short
intervals and progressions". Compiles cleanly (two passes, no undefined refs, no overfull boxes).
Sources: EXCEPTIONAL_SHORT.md ((D)30, R88), EXCEPTIONAL_MN.md ((D)31, R94A/B), the 3/4 note (= [TQ]).

## Structure
1. Intro: Thm A (m-uniform windows), Thm B (progressions, q_1 loss), Cor C (primes, no prime input),
   Cor D (density transition), PW comparison (asymptotic; ratio ≫ (Lm)^{1/12}/(log log 3m)^{1/3}),
   Prop E pointer; status + hedged novelty.
2. Black box: exact list of [TQ] statements **used verbatim** (Lemmas 3.1, 3.3, 4.1, Thm 6.3
   cond.-indep. proof, Lemma 8.1; Thm 8.2 + Lemma 2.1 for m = 4), **re-run** (2.1, 2.2, 3.2, 4.2, 4.3,
   7.1, 8.2), **replaced** ((50) counting step, §9 semigroup/Rankin), **not used** (§5, ordered-atom
   replay, §§10–11). Substitution table 4 → m. New abstraction: *(m;X,s,y)-package* (P1–P3); Prop 2.2
   (packages exist); m = 4 package directly from [TQ] Thm 8.2 (s = t³/4), incl. the remark that [TQ]
   states ν ≥ 1 only for exceptional primes > max(K,y) but its proof gives (P1).
3. Atom family for m (identity, Def., CRT lemma with full proof).
4. h_m lemma (full proof). 5. Prop 5.1 pruned prime slice for m (full proof of the changed steps),
   Cor 5.2 fibre masses ≍ t³/m (toy EVIDENCE quoted). 6. Void (η = 1/4), moments, Thm 6.3 assembly
   (explicit ledger).
7. Local transfer: Lemma 7.1 (local mean, class by class), 7.2 (large-prime moduli independent),
   7.3 (smooth-part decomposition + Rankin), Prop 7.4 (transfer from any package), proofs of A, B,
   Remark 7.5 (smooth/prime moduli caveat; m = 4 covers all primes q, general m does not), Cor C,
   Remark 7.6 (relative density via BHP — quoted, labelled conditional).
8. Cor D proof; PW proof range (eq. PWrange) with the "reading of PW's proof" caveat; gap
   (log m)²(m/φ(m))^{1/3}; monotonicity unknown; nothing on the largest exception; Assessment 8.1.
9. Prop E (lower end, any m), window exponent θ_win(m), Prop 9.1 (a),(b) PROVED; Assessments 9.2 (three
   regimes) and 9.3 (shift-uniform methods, position) labelled Assessment.
10. Literature (ET, PW, Li, Yang, Vaughan access caveat). 11. Open problems (smooth q; transition gap
   incl. large m; position-dependent input / θ_win; the exponent).

## Deviations from the source files (please check)
* Lemma 3.3 (CRT): stated for **every** m ≥ 4 (MN Lemma 1.3 had m ≤ t³): `(ℓ,m) = 1` is forced by
  `m | kℓ+1`, and `muv > H_K² > K` needs no bound on m.
* Prop 5.1 lower bound: uses `φ(muv) ≤ φ(m)uv` directly on the *retained* harmonic mass instead of the
  note's "removed weighted mass ≪ log t × removed harmonic mass" step (simpler, same conclusion).
* Lemma 4.1(a): final inequality simplified (`2^{ω(m)}/x ≤ 1/m < γφ(m)/m`).
* Thm A/B proof: second constant made explicit, `C_2 = C_L + a + B + 3` (covers the `yD_0` term;
  MN had `C_L + a_v + 1`).
* Remark 7.6 (BHP relative density): the ratio carries a factor log x, so for m-uniformity it needs
  `(log x)^{3/4} m^{−1/4} ≥ (2/c′) log log x`; SHORT Cor 3.2(a) (m = 4 fixed) absorbed it silently.
  SHORT Cor 3.2(b),(c) (Huxley almost-all; APs) only mentioned as unchecked.
* Window exponent is defined per m; Prop E generalised to m.
* PW Type I/II counts are quoted from R94A/B's reading of the rendered PDF (pw.txt drops superscripts);
  the text says this reading is ours, not a statement in PW.

## Status / labels
Everything in §§3–9 marked PROVED is relative to [TQ] (internally proved, not externally refereed);
abstract and intro say so. Toy masses: EVIDENCE. §8 Assessment, §9 Assessments, §10: Assessment.
No claim that ES or Schinzel is proved; no claim of improving 3/4; method novelty disclaimed.

## Self-check done
Against SHORT + R88 (D1–D8), MN + R94A (D1–D7) + R94B (D1–D6): all repairs reflected (ineffective
constants; M_𝔊 not equality; exact Lemma 1.1 form; c/2 and C_3′ = (4/c)^{4/3}-type constants in the AP
prime clause; Remark 2.2 non-overclaim; BHP caveat + tiling + 2x^{0.525}; Assessment labels;
asymptotic-only PW comparison; nontrivial-range wording; PW proof range; heuristic "up to bounded
and log log factors"; dedup toy; explicit ledger; simplified-route scope; Vaughan-for-general-m
unverified; t³ = ms ≥ 4s side condition; no Euler-factor claim). Equation/statement numbers of [TQ]
cited from its compiled aux.

Stopping here for the referee.
