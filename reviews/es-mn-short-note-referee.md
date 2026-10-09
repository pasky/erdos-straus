# Hostile referee report R97 on `paper/es-mn-short-note.tex`

("The exponent 3/4 for the exceptional set of m/n, in short intervals and progressions";
author report `reviews/agent-reports/AGENT_REPORT_O97.md`; merged from `side-agent/mn-short-note`.)

Everything is relative to `paper/es-threequarter-note.tex` (= [TQ]; internally proved, not
externally refereed). I checked the [TQ] labels against my own fresh two-pass compile of [TQ]
(aux file), not against the author's claims. Sources consulted: `sources/pw.txt` (= arXiv v1 /
author draft of 20 Nov 2025), `sources/pomerance-weingartner-2511.16817/…v2.pdf` (the cited
version), `sources/elsholtz-tao-1107.1010.pdf`, `sources/vaughan-1970-access-log.md`. **Not
accessible locally:** Vaughan 1970, Baker–Harman–Pintz 2001, Montgomery–Vaughan 1973, Li 1981,
Yang 1982, Davenport.

From-scratch scripts (EVIDENCE only, independent of the author's `scripts/emn_*`):
* `scripts/review_r97_arith.py`: an exact-rational check of the identity (3000 random instances, 0
  failures). It also brute-forces m-representability for m ∈ {4,…,9,12,13}, n ≤ 1200 (two-unit
  test via `(ay−b)(az−b)=b²`). Results: every n in every forced class `−uv⁻¹ (mod kℓ)` with
  `kℓ+1 = muvw`, `kℓ ≤ 1200`, is representable (≈25 000 classes, 0 violations). Smooth-part
  closure (Lemma 7.3(a)) has 0 violations for y ∈ {2,…,11}. n = 1 is exceptional for m ≥ 4, and
  no n < 300 is exceptional for m ≤ 3. The m = 8 exceptions 2, 3 agree with PW §3.
* `scripts/review_r97_analytic.py`, covering these checks:
  * harmonic remainder: `|θ_y| ≤ 0.541` (≤ 1 is needed);
  * Lemma 4.1(a)–(c): 0 failures for m = 4..60, 210, 2310, 5040, 30030 (and the primorials) with
    K ≤ 2·10⁵;
  * the ratio `S_m/((φ(m)/m)log K)` lies in [1.05, 1.37];
  * `min h_m/S_m = 0.635` (≥ 0.54 is needed);
  * Rankin (Lemma 7.3(b),(c)): exact for y ≤ 13;
  * Lemma 7.1: max |θ| = 0.42 over 1000 random windows, with exact rationals and a random signed
    class combination;
  * Lemma 7.2: 0 violations;
  * the algebra of Cor D and the √2·log(N/2) ≥ log N threshold: N ≥ 10.7, so N ≥ 16 suffices;
  * eq. (ratio): `min_{4≤m≤2·10⁶} φ(m)loglog(3m)/m = 0.354` at m = 6.

## Recommendation

**Accept after minor revision (one MAJOR citation defect).** I re-derived every new proof line by
line and found no FATAL defect and no mathematical gap. The labels are honest: everything is
"proved relative to [TQ]", and the abstract, intro and bibliography say so. The only MAJOR defect
is a misquotation of the cited version of Pomerance–Weingartner, which bears on the literature
and novelty paragraph (D1). The rest are wording, quantifier and attribution repairs.

## Per-section / per-claim verdicts

| item | verdict |
|---|---|
| Abstract, §1 statements vs SHORT/MN + reviews R88, R94A/B | SOUND. They are no stronger than the reviewed sources. Every repair from R88 D1–D8 and R94A/B D1–D7 is reflected: ineffective constants; asymptotic-only PW comparison; PW *proof* range; the c/2 and (4/c) constants in the AP prime clause; the q₁ caveat; Assessment labels. Wording issues are in D2–D4 and D8. |
| §2 black-box list (labels) | SOUND. Every cited [TQ] number matches the compiled aux, from Lemma 2.1 through §§10–11 (Lemma 2.1/2.2/3.1/3.2/3.3/4.1, Thm 4.2, Cor 4.3, §5, Lemmas 6.1/6.2, Thm 6.3, Lemma 7.1, Lemma 8.1, Thm 8.2, §9, (2)(3)(7)(8)(9)(12)(26)(39)(40)(43)(44)(48)(49)(50)). [TQ] Lemma 4.1 does use only 𝒥 ⊆ [1,K]: its proof sums over all k,k′ ≤ K. [TQ] Lemma 3.1/3.3 are stated for every k ≤ K, (c,k)=1. The "only occurrences of 4" sentence is incomplete but harmless (D5). |
| Def 2.1 / Prop 2.2; m = 4 package from [TQ] Thm 8.2 | SOUND. The paper notes that [TQ] states ν ≥ 1 only for primes > max(K,y). Its proof (identity + Q_r(0)=1) gives (P1) for every exceptional n coprime to P_y, as claimed. (P2) follows from (44) and (7), and (P3) from (43), with s = t³/4. |
| Lemma 3.1 (identity), Def 3.2, Lemma 3.3 (dedup/CRT, every m) | SOUND. Re-derived: `muv ∣ kℓ+1` forces (ℓ,m)=(k,m)=1. Distinct projections follow from `z_j² < ℓ`, and `muv > K` gives k = k′. No bound on m is needed. |
| Lemma 4.1 (h_m) | SOUND. Re-derived (a)–(d): the Möbius/f′(1) ≥ 0 step, then `2^{ω(m)}/x ≤ 1/m < γφ(m)/m`, Σp⁻² < 0.4523, and the Euler-product upper bound for K ≥ m. Numerics are clean. |
| Prop 5.1 (prime slice for m) | SOUND, uniformly in 4 ≤ m ≤ t³. Re-derived as follows. The retained harmonic mass is ≥ (1/64)(log z)²h(𝒥): Lemma 3.3 gives 1/32, and the congestion loss is ≤ C₂(log z)²(1+κt)³/t⁴. The main term uses φ(muv) ≤ φ(m)uv. The BV level is q ≤ t³x^{1/3}, multiplicity W(q) ≤ t^{4+D log 2} and R = D log 2+17, so the error is O(x(log x)^{−13}). The main term is ≫ x(log x)^{−2}, using h ≥ 1 and φ(m) ≤ t³. The upper bound uses BT with q ≤ x^{0.34} and φ(ab) ≥ φ(a)φ(b) for all a,b. The new step (using φ(muv) ≤ φ(m)uv directly on the *retained* mass) is valid and simpler than [TQ]'s O(log t) step. |
| Cor 5.2 (fibre masses ≍ t³/m) | SOUND. K ≥ t⁶ ≥ m² for X ≥ X_h, uniformly over m ≤ t³. The upper bound holds for every c, the lower bound for reduced c. |
| Lemma 6.1 (void, η = 1/4) | SOUND. Re-derived. Given S_y = 1, the events p∣c for p∣L_K, p > y are independent of probability 1/p. E e^{yZ} ≤ e^{C_Z} for every y ≥ 2, and h(𝒥_c) ≥ (0.54 − Z)S_m(K) by 4.1(b),(c). With B = 8a_v, the bad fibres have probability e^{−y/4+C_Z} = e^{−2a_v s+C_Z}. Nothing in this step depends on m. |
| Lemma 6.2, Thm 6.3 (moments, Bonferroni, ledger) | SOUND. I re-derived C_L = B+3D_B+8 term by term (π(y)log 2 ≤ y ≤ (B+2)ts, etc.). The ledger e^{O(t⁴/m)} is correctly *not* e^{O(s)}. |
| Lemma 7.1 (local mean) | SOUND (also numerically exact). Shift-uniformity is genuinely just "each class meets any half-open interval of length H in H/q′ + θ points, \|θ\| ≤ 1". |
| Lemma 7.2 (large-prime moduli) | SOUND. q₂ is the X-rough part, so (Q_{d,1}, q₂) = 1 automatically. |
| Lemma 7.3 (smooth-part decomposition) | SOUND. Convexity: −log(1−u) ≤ 2u on [0, 2^{−1/2}] (end value 1.228 ≤ 1.414). |
| Prop 7.4 (transfer) | SOUND. d ↦ n′ = n/d is injective for fixed d. lcm(d′,q) is a multiple of d′q₂. Q_d = q/(d,q) has X-rough part q₂. ν ≥ 0 covers n′ ≤ 0. |
| Proof of Thms A, B | SOUND. I checked C₂ = C_L+a+B+3 (log(yD₀+D₀e^{C_Lts}) ≤ 1+(B+2)s+as+C_Lts) and the choice t⁴ = m𝓗/(2C₂), which makes e^{C₂ts} = (H/q)^{1/2}. The side conditions are X ≥ X_a (via t³ = ms ≥ 4s), s ≥ 1 and s ≥ s₀, s₁. The trivial range is s < s_* ⇒ 𝓗^{3/4}m^{−1/4} < C₃, and H/q₂ = q₁H/q. The constants are absolute (κ = 1/480 fixed; ineffective via BV). |
| Remark 7.5 (q₁, prime moduli) | SOUND. The ratio log X_q/(𝓗^{3/4}m^{−1/4}) = α(m/𝓗)^{1/2} is right. Wording issue: D6. |
| Cor C (+ AP variant) | SOUND (trivial from A/B; the constants 2/c, (2/c)^{4/3}m^{1/3}, c/4, 4/c check out). |
| Remark 7.6 (BHP) | SOUND *conditionally on the quoted BHP lower bound*, which I could not verify (no source; D7). The tiling and the extra log x factor are handled correctly. |
| Cor D | SOUND. I re-derived f′ > 0 for L > (8/(3c))^{4/3}m^{1/3}, and f(L₀) ≥ (cA^{3/4} − 10/3 − 2log A/log 4)log m. L ≥ ½ log N ≥ L₀ for N ≥ 4, and N/(2L²) ≤ N/(log N)² for N ≥ 10.7. |
| "The other side" (PWrange) | SOUND as a reading of [PW v2, pp. 6–8]. The Type I count ≪ (N/φ(m))log²N log²m for e^{m^{1/4}} ≪ N < e^m and the Type II count ≪ (N/φ(m))log²N loglog N are verbatim there. "Most primes in (N/2,N] uncovered" follows for log N ≤ (φ(m)/(C log²m))^{1/3}. Attribution wording: D8. |
| eq. (ratio) and the PW comparison | SOUND asymptotically. The quantifier and range should be tightened (D3). |
| Assessment 8.1 | Assessment, correctly labelled. The algebra (tμ ≍ L ⇒ μ ≍ L^{2/3}φ^{−1/3}, resp. L^{3/4}m^{−1/4}) checks out. Attribution to "Vaughan's" argument: D9. |
| Prop E, Prop 9.1 | SOUND (trivial). Quantifier wording: D10. |
| Assessments 9.2, 9.3 | Correctly labelled heuristics. The claim "M ≤ x for H ≤ exp{c(loglog x)⁴/m}" checks out (log 𝓜 = O(X)). |
| §10 Literature | GAP in citation accuracy (D1, D2). The novelty hedging itself is appropriate. |
| §11 Open problems | One false side-claim, inherited from SHORT (D4). |
| Interface with [TQ] (task item 3) | SOUND. Nothing unproved in [TQ] is used. Uniformity in m is *not* taken from [TQ]: Prop 5.1, Cor 5.2, Lemma 6.1 and Thm 6.3 are re-proved here with all m-dependence explicit. The only [TQ] statements used for general m are Lemmas 3.1 ((12) only), 3.3 and 4.1, Lemma 8.1 and the analytic inputs (8), (9). All of these are m-free and stated for every k ≤ K. The void lemma is a statement about the CRT space, so no "shifted void" is needed. Shifts enter only through Lemma 7.1. |

## Numbered defects

**D1 (MAJOR — misquoted source; §10 bullet 2, also §1 "Background").** The paper cites
`arXiv:2511.16817v2` but quotes the *v1* abstract ("generalize a result of Vaughan", as in
`sources/pw.txt` l.19–20). The v2 abstract (cited version, `…v2.pdf` p.1) reads instead: "A result
of Vaughan is that for each m, most n's have m/n representable; we make the dependence on m in
this result explicit." This matters for two reasons.
1. It is a misquotation of the cited text.
2. It is the one available secondary statement that **settles the question the paper leaves
   open**, namely "Whether Vaughan's paper … itself treats general m we could not check". Per PW v2,
   Vaughan's 1970 theorem treats each fixed m.

*Repair.* Quote the v2 abstract verbatim. In §10 replace "Whether Vaughan's paper … could not
check" with: "According to [PW, abstract], Vaughan's result already covers each fixed m. We could
not read Vaughan's paper, so we rely on this secondary statement for the dependence on m." Keep
"[PW, Thm 1.3] is the first bound *explicit* in m that we can cite" (still correct). In §1
Background, add after the Vaughan sentence: "(for each fixed m, according to [PW]; the
m-dependence was made explicit in [PW])." The novelty claims (Thm A new for m ≠ 4 at exponent
3/4; m-uniformity) are unaffected.

**D2 (MINOR — ET paraphrase; §1 Background l.~"quoted as the state of the art by Elsholtz and
Tao [§1]" and §10 bullet 1 "as the only exceptional-set result").** ET §1 actually says: "For
instance, it was shown by Vaughan [82] … (Compare also [48, 84, 39, 89] for some weaker results)."
ET say neither "only" nor "state of the art". *Repair:* "ET [§1] cite Vaughan's bound, and
list Nakayama, Webb, Li and Yang as weaker results". In Background, keep "state of the art" for
PW only, since PW p.2 says the count "has been strongly improved, though not recently: In 1970,
Vaughan …".

**D3 (MINOR — PW comparison quantifiers; §1 after Cor D, eq. (ratio) paragraph).**
1. "Theorem A and (PW) have unrelated ineffective constants": PW do not claim ineffectivity (the
   large sieve plus elementary steps). *Repair:* "unrelated constants (ours ineffective)".
2. "Theorem A is stronger than (PW) whenever (Lm)^{1/12} ≥ Λ₀(loglog 3m)^{1/3}" should be stated
   only inside PW's range m ≤ L². Outside it, (PW) is not a theorem. Also, "stronger" needs
   S′ := L^{2/3}φ(m)^{−1/3} ≥ 1 to absorb the prefactor C of Thm A (cΛS′ − C_PW S′ ≥ log C), and
   S′ ≥ 1 holds exactly because m ≤ L². *Repair:* "Hence there is Λ₀ such that, for 4 ≤ m ≤ L²,
   Theorem A is stronger than (PW) as soon as (Lm)^{1/12} ≥ Λ₀(loglog 3m)^{1/3}; in particular
   for all such m once N ≥ N₀."

**D4 (MINOR — false side-claim; §11 Problem 1, inherited from SHORT Remark 2.2).** "Fixing the
coordinates n mod ℓ for ℓ ∣ q₁ changes the fibre product by a factor ≤ exp{Σ_{ℓ∣q₁}2ℓ^{−2/3}}
= 1+o(1)" is not true for general q₁. The sum over the primes in (X^{1/2}, X] dividing q₁ can be
as large as Σ_{X^{1/2}<ℓ≤X} 2ℓ^{−2/3} ≍ X^{1/3}/log X → ∞. *Repair:* "by a factor
≤ exp{2ω(q₁)X^{−1/3}} (using f_c(ℓ) ≤ z_j² ≤ ℓ^{1/3}, [TQ, proof of Lemma 2.2]), which is 1+o(1)
when ω(q₁) = o(X^{1/3})".

**D5 (MINOR — §2.2 "It appears only in …").** The list of places where the numerator 4 occurs
in [TQ] omits several:
* the dedup step `4uv > 4H² > K` (Lemma 2.2), which is re-run here as Lemma 3.3;
* `q ≤ 4x^{1/3}` in (8)/(9);
* the main-term step in Thm 4.2 (1/φ(4uv) ≥ 1/(4uv) and the O(log t) removal);
* §5 (W_c(q) with q/4; φ(4uv) ≥ 2φφ there);
* the "L_𝒥 odd" remark after (21);
* "p ≡ 3 (mod 4)" in the proof of Lemma 7.1.

All of these lie in statements that are re-run or not used, so there is no gap. *Repair:* "Apart
from the unused §5, the (21)-remark and §§10–11, it appears only in statements that are re-run
below."

**D6 (MINOR — Remark 7.5).** "every prime modulus q with H/q large is covered without loss":
the bound obtained is the halved-exponent consequence of Thm B (c/2). *Repair:* "without the
factor q₁ (with saving constant c/2)".

**D7 (MINOR — Remark 7.6, bibliography [BHP]).** The BHP lower bound
π(u) − π(u − u^{0.525}) ≫ u^{0.525}/log u is not in `sources/` or in LITERATURE_2026.md. The
author flags this ("did not re-check"). The bibliographic data agree with my knowledge, but I
could not verify the statement. *Repair:* label the remark's conclusion explicitly as
**CONDITIONAL** (on the cited BHP statement), in line with the status labels. Optionally add a
source file.

**D8 (MINOR — §8 "The other side" and abstract).** "(This reading of [PW] … it is not a
statement made in [PW].)" is slightly too strong. PW p.2 state: "In our proof of Theorem 1.1 we
actually show that not only is there one exceptional n > exp(m^{1/3−ε}), but that most prime
values of n near this bound are exceptions." Only the extension to the whole range (PWrange) is
the authors' reading. Conversely, the abstract's "locating the transition at log n = m^{1/3+o(1)}"
does not say that the lower side rests on that reading of PW's proof. *Repair:* cite the p.2
sentence. Change the parenthetical to "PW state this for N = N(m); the extension to the range
(PWrange) is our reading of their proof, checked by two internal reviewers". In the abstract,
add "(the lower side from the proof of [PW, Thm 3.1])".

**D9 (MINOR — Assessment 8.1).** "Both our argument and Vaughan's balance a fibre mass μ against
a ledger e^{O(tμ)}." Nobody in the campaign has read Vaughan's paper (see
`sources/vaughan-1970-access-log.md`). *Repair:* "Vaughan's argument as reconstructed in
[PW, §4]".

**D10 (MINOR — Prop E hypothesis).** "some function H₀(x) ≥ 1 with C H₀(x)e^{−c(log x)^{3/4}} < 1"
should read "… < 1 for all x ≥ x₀". The proof uses it at every x ≥ x₀.

**D11 (MINOR — §1 after Thm A).** "For m ≤ ε(log H)³ with ε = ε(C) small": the saving there is
cε^{−1/4}, so ε depends on c and C. *Repair:* "ε = ε(c,C)".

**D12 (MINOR — Lemma 3.3(3)).** "conditional on any residue c (mod L_K) (and on S_y = 1)": the
conditioning event is empty when a prime p ≤ y divides (c, L_K). This is harmless, since only
c compatible with S_y = 1 are averaged. *Repair:* "on any residue c compatible with S_y = 1".

**D13 (MINOR — bibliography, verification status).** [Li] and [Yang] match ET's bibliography
(entries [39], [89]), which is only a secondary check. [MV], [Davenport] and [BHP] are not in
`sources/`. [Vaughan] is inaccessible (access log). The data agree with my knowledge.
*Repair:* none required. Optionally add one sentence in §10 saying which entries were read.

No other defects. In particular I found no quantifier error in the uniformity in m. Every
threshold (X_h, X_v, X_a, s₀, s₁, s_*) is absolute, because m ≤ t³ is built into the choice
t⁴ = m𝓗/(2C₂). The only constants that depend on parameters are κ and D, and both are fixed. I
found no circularity: the m = 4 route and the general-m route both feed the same Prop 7.4, and
neither uses [TQ] §9.

## Round 2: repairs applied

All repairs were applied by the referee to `paper/es-mn-short-note.tex` (commits d76ccca..52066b4).

| defect | repair applied |
|---|---|
| D1 (MAJOR) | §10: the v2 abstract of PW is now quoted verbatim, and the v1 wording is noted as such. "According to [PW], Vaughan's result already covers each fixed m", with an explicit caveat that this is a secondary source. The "first bound explicit in m" claim is kept. §1 Background now says that Vaughan's result covers each fixed m (per [PW, abstract]). |
| D2 | ET is now described as "cite Vaughan's bound … (for instance) … other results as weaker". "Only" and "state of the art" are no longer attributed to ET; "state of the art" is attributed to PW p.2. |
| D3 | "unrelated constants (ours ineffective)". The comparison is restricted to PW's range 4 ≤ m ≤ L², with the remark that the PW exponent is ≥ 1 there and absorbs C, and that (PW) is not available outside that range. |
| D4 | Open Problem 1: the factor is now ≤ exp{2ω(q₁)X^{−1/3}} (via f_c(ℓ) ≤ ℓ^{1/3}, only ℓ > X^{1/2} matter). This is 1+o(1) only when ω(q₁) = o(X^{1/3}). |
| D5 | §2.2: the list of occurrences of 4 in [TQ] is now complete, with the unused parts named. |
| D6 | Remark 7.5: "without the factor q₁ (with saving constant c/2)". |
| D7 | Remark 7.6: the conclusion is labelled CONDITIONAL on the quoted BHP statement, which is not checked against the source. |
| D8 | §8: PW's own p.2 sentence is quoted. The extension to (PWrange) is called "our reading of their proof". The abstract now says that the exceptional side comes from the proof of a PW theorem. |
| D9 | Assessment 8.1: "Vaughan's, as reconstructed in [PW, §4]". |
| D10 | Prop E: the inequality is assumed "for all real x ≥ x₀". |
| D11 | ε = ε(c,C). |
| D12 | Lemma 3.3(3): "any residue c compatible with S_y = 1". |
| D13 | §10: a new bibliographic-status item says which entries were consulted in full, checked secondarily, inaccessible, or not re-read. |

Recompiled twice: there are no undefined references and no overfull boxes. The six underfull
hboxes were present before the repairs (bibliography and one display-heavy paragraph). The paper
is 18 pp. No mathematical statement or proof was changed apart from the D4 side-remark in an open
problem and the D3/D10/D12 quantifier tightenings.

**Final recommendation: ACCEPT (as an internal note).** All results are SOUND relative to [TQ],
and the labels and status statements are honest. The only remaining caveats are inherent and are
disclosed in the paper:
* [TQ] itself is internally proved and externally unrefereed;
* Vaughan 1970 and BHP were not read;
* the PW range (PWrange) is a reading of PW's proof.

## Post-referee addition (O104)

*Added by the O104 author after R97; not covered by R97's verdicts above.* §8 ("The density
transition") was rewritten into a full section from `EXCEPTIONAL_MN2.md` (DISCOVERIES (D)31
follow-up; independent reviews `reviews/exceptional-mn2-review-A.md`, `-B.md`, no FATAL/MAJOR,
minors repaired). New material:

* §8.2 Theorem U (PROVED rel. [TQ] via Cor 5.2, Bombieri–Vinogradov, Shiu; ineffective):
  Lemma 8.1 (reduced CRT model), Lemma 8.2 (Shiu multiplicities), Theorem 8.3, proof of U —
  full proofs, = MN2 Lemma 1.1, 1.2, Thm 1.3, Thm U.
* §8.3 Theorem L (PROVED rel. ET Thm 7.1 + structure of ET's proof of Prop 1.4, BT, Shiu;
  effective): Lemma 8.4 (two harmonic sums; (b) condensed), Prop 8.5 (Type II), Lemma 8.6
  (ET Prop 1.4 + Pólya–Vinogradov, *proof sketch with exact pointers* to ET pp. 30–32, (7.11)),
  Prop 8.7 (Type I, condensed), Lemma 8.8 (very large m) — = MN2 Lemma 3.1–3.5, Prop 3.2/3.4.
* §8.4 gap `(m log m/φ(m))^{1/3}`, comparison with PW (proof range (PWrange) retained, improved by
  min(log m, L/log m)) and Elsholtz 2001 Rem 7.3 (reaches only log N ≫ m^{1/2}); Pomerance 2026
  talk cited for the open transition question (novelty audit 2026-10c §1).
* §8.5 numerics (EVIDENCE; even-m table, odd-m parity effect, non-shrinking window,
  overdispersion) and Conjecture C2 (CONJECTURE).
* Abstract, intro (Theorems U and L stated after Cor D), status/novelty, organisation, literature
  and open problems (gap problem rewritten; new problem "the profile") updated. Cor D and its
  proof unchanged. 25 pp; two compiles, no undefined references, no overfull boxes.

**A referee pass on the new §8 (and the changed intro/abstract) is still required.**

## Post-referee addition (O113)

*Added by the O113 consolidation agent; not covered by any referee verdict above (nor by
`es-mn-short-note-referee-r2.md`).* Theorem L is replaced by **Theorem L′** from `EXCEPTIONAL_MN3.md`
(DISCOVERIES (D)31 follow-up 2; hostile review `reviews/exceptional-mn3-review.md`, no FATAL/MAJOR,
minors applied by the reviewer): `ρ_rep ≪ (L³ + L² log² m) log L/m + m^{−0.35}` (was
`L³/m + (L³ + L² log² m) log L/φ(m) + m^{−0.35}`), PROVED relative to ET Thm 7.1 and ET's proof of
Prop 1.4, with Brun–Titchmarsh, Shiu and Pólya–Vinogradov; effective. Changes:
* Lemma 8.6 is now MN3 Prop 2.3 (ET Prop 1.4 with the coprimality gain φ(k)/k; full proof incl. MN3
  Lemma 2.1 (coprime harmonic sums) and the PV/Kronecker-PV ranges of Lemma 2.2), followed by
  Remark 8.7 (comparison with ET; §2.6 numerics as EVIDENCE). The old "proof sketch with exact pointers"
  to ET (7.11) is gone.
* Prop 8.8 (Type I) is MN3 Prop 2.5 (`/m` instead of `/φ(m)`; l = 30, k^{1/28} box split; tiny boxes
  with the τ(st) grouping of the R108 repair); for m ≤ m₀ the bound is trivial (count ≤ N).
* Proof of Theorem L′: `φ(m)` → `m`; Type II (Prop 8.5) and Lemma 8.9 unchanged.
* Gap (§8.4, abstract, intro): `(m log m/φ(m))^{1/3}` → `(log L)^{1/3} = (log log N)^{1/3}`, a single
  remaining loss (ET's Type I Brun–Titchmarsh log log N). PW comparison factor now
  `(m/φ(m)) min(log m, L/log m)`.
* New Remark 8.10 citing EXCEPTIONAL_TYPEI_LOGLOG Thm 8.1 = DISCOVERIES (D)32 (CONDITIONAL on Selberg's
  eigenvalue conjecture for Γ₀(4dq²) with even nebentypus; m = 4 only) as the route to the exact scale;
  the m-uniform extension is stated as not carried out (MN3 remarks after Thm 3.8).
* Open problem "the transition gap" rewritten (one loss left; old item (ii) removed); bibliography
  [MN3], [TTL]; status/novelty paragraph updated. Section titles with `$m$` wrapped in
  `\texorpdfstring` (no hyperref warnings). 26 pp; two compiles, no warnings, no undefined
  references, no overfull boxes.

**A referee pass on Lemma 8.6 / Prop 8.8 / Remark 8.10 as written in the paper is still required.**

## Post-referee addition (O120)

*Added by the O120 agent; not covered by any referee verdict above.* New **§9 "Under Selberg's eigenvalue
conjecture"** from `EXCEPTIONAL_MN4.md` (DISCOVERIES (D)31 follow-up 3; hostile review R117
`reviews/exceptional-mn4-review.md`, no FATAL/MAJOR, minors applied):
* Def 9.1 (SEL_m): no eigenvalue in (0,1/4) on Γ₀(mdq²) with even nebentypus mod q, `(q,2md)=1` squarefree;
  implied by Selberg for all Γ₁(M); for m = 4 the family of [HN, Hyp 1.1].
* Thm 9.2 = MN4 Thm 4.1 (CONDITIONAL on SEL_m; 4 ≤ m ≤ L⁵): `Σ_{N/2<p≤N} f_{I,m}(p) ≪ N(L²+L log²m)/m + N m^{−0.35}/L`.
  Proof *sketch* with exact pointers (MN4 Lemma 0.1, Lemma 1.1, §2.1, §2.2, Thm 6.2_m, Lemma 6.1_m, §2.6, §3,
  §3.2(c) only for D,F ≥ L^100, §3.4, Thm 4.1; HN Lemmas 3.1–3.2, Prop 5.1, Thm 6.2, Prop 7.1, Lemma 8.1, Thm 8.2).
* Thm 9.3 = MN4 Thm 5.1 (Thm L″): `ρ_rep ≪ (L³+L² log² m)/m + m^{−0.35}`; conditional for m ≤ L⁵, PROVED
  (from Thm L′ + Lemma 8.9) for m > L⁵. Full proof given (three cases, from Thm 9.2, Prop 8.5, Lemma 8.9, Thm L′).
* Cor 9.4 = MN4 Thm 5.2 (sharp order): lower half CONDITIONAL, upper half = Theorem U (unconditional).
* Remark 9.5: unconditional content of MN4 §6; (D)32a (HN Thm 1 = Thm 9.9(i), unconditional o(N log²N log log N),
  m = 4) is **not** transferred to general m by MN4 or LOGLOG2 → stated as open; noted that even an m-uniform
  transfer would only give an unquantified o(1) gain over Thm L′, and an m-uniform (EFF) version would make
  Cor 9.4(a) conditional on (EFF) instead.
* Remark 8.10 (rem:sel) rewritten (extension now carried out, pointer to §9); §8.4 gap paragraph, abstract,
  intro (after Theorem L′), status/novelty, organisation, Problem 2 (now labelled, asks about the unconditional
  m-uniform transfer) updated. Bibliography: [HN] (`paper/es-typei-heegner-note.tex`, compiled numbering),
  [MN4]. 29 pp; two compiles; no warnings, no undefined references, no overfull boxes (the 10 underfull
  bibliography lines are pre-existing).

**A referee pass on §9 (esp. the proof sketch's pointers and Remark 9.5) is still required.**
