# Hostile review, Round 2: `notes/z78/F3_CONJ.md` §§6–7 (commits `dbcec7fc2..96ecbd9f3`)

Reviewer: Claude (Anthropic), an Opus-class model running as a pi subagent. I cannot see the exact model version. There were
no provider, auth or quota errors. I wrote only inside `data/z78/xreview/`. All scratch went there (`TMPDIR` was set there),
and nothing went to `/tmp`. The note, the scripts and the master files are unchanged. I did not commit, because the strict
write scope excludes `.git`. The orchestrator should commit this file together with `r2_*.py` and `r2_*_log.txt`.

## Verdicts (kept separate)

**Theorem verdict: ACCEPT. I found no mathematical defect.** I re-derived every step of §6 by hand:
* the key identity (6.1);
* both degree bounds, and the monicity and no-cancellation argument;
* the forced endpoint (P=1, δ=3, d=b, w=2, H=1);
* (6.2) and (6.3);
* both branches deg D ≥ 1 and D constant (including W=u²);
* the small levels s ≤ 6.

I also re-checked every RELATIVE input §6 consumes from §§1–4:
* d+r+P ≥ K, d ≤ b+Q, and w ≤ 1+P (via v ≥ r−Q−1);
* G′ ≠ 0;
* W monic with W(0) ≠ 0;
* H ≠ 0 and J ≠ 0;
* the c↔−c symmetry.

The scope chain also checks out:
* minimum level, then all levels;
* Case A exclusion;
* compactness;
* k=2.

Conclusion: x*_1, x*_2 ∈ O(3,T²), so ES₃(T²,·) has no finite linear covering. This is PROVED relative to §§1–3, the §4
sign-symmetry lemma, and the cited published-in-repo lemmas. It is not a statement about A=T, about individual P, or about
integer ES. The note scopes this correctly.

**Repairs verdict: form and label only.** None of the defects affects the theorem. R2-D1, R2-D9 and R2-D10 should be
applied before export. The rest are cosmetic.

**Gate status.** This review is one independent Anthropic review. Under AGENTS §3 a HEADLINE needs a review from the lab
other than the author's. That condition is met if the author lane is Astra, which the R1 framing implies. The orchestrator
should confirm this. A **priority check** is also required by the gate, and the note does not record one (R2-D10).

## 1. Re-derivation of §6 (all hold)

Notation is as in §3: c=1 after symmetry, P+Q=1, b=n−K, δ=N−b∈{3,4}, κ=(q−p)/T, h=deg H=b−d+Q.

**(6.1).** pMW = p(T^δSJ+κq) = pT^δS(MH−qT^b) + κu. Here pq=u is used, and this should be said explicitly; see R2-D4.
Next, pSMH = mH·pXS = mH(T^{b+1}W−qH) and δ+b+1 = K = N+1. These give
pMW = T^{N+1}mHW − T^δqmH² − uT^NS + κu, which is (6.1). ✔

**Degree of the second term.** δ+Q+z+2h = N+b+3Q−d−r. With d+r ≥ K−P this is ≤ N−δ+2−2P ≤ N−1. Its degree is ≥ δ ≥ 3,
since H, m and q are nonzero. ✔

**Degree of the first term.** deg pMW = P+d+w. Here d ≤ b+Q (because h ≥ 0) and w ≤ 1+P (because v ≥ r−Q−1 and
w = r−v+2P−1). So the degree is ≤ b+2+P ≤ N, with equality iff P=1, δ=3, d=b, w=2. ✔
* If the degree is < N, then the LHS is ≡ κu mod T^N and has degree < N, so LHS = κu.
* At c=1 the two leading coefficients are lc(p)·lc(W) = 1 and lc(q)³ = 1. They cannot cancel, so deg LHS ≥ δ > 1. This is a
  contradiction. ✔
* The restriction to c=1 is genuinely needed here. At c=−1 the lc's are ±1 and could cancel. The σ-symmetry removes this
  case. ✔

**Endpoint.**
* (6.2): T^NR = LHS−κu is monic of degree N, so R=1. ✔
* From uXS = T^{d+1}W−1 and uS = TmW−1: X(TmW−1) = T^{d+1}W−1, hence X = TW(M−T^d)+1 = TWJ+1. ✔
* Then u·(MW = T³SJ−1) gives (6.3). ✔
* D=T³−uW has D(0) = −W(0) ≠ 0.
* If deg D ≥ 1: the LHS has degree z+3+deg D+j > 3+j. ✔
* If D is constant: D(−1) = −1, so uW = T³+1 = u³ and W = u². Then ugJ = T^dW+1 ≡ 1 (mod u), a contradiction. ✔
* The alternative route via ug = T³S−W gives u|S, hence −1 ≡ 0 mod u. ✔

**Small levels (s ≤ 6).** Each case below was rechecked by hand, and by enumeration (§3a).
* s ≤ 3: no tuple. ✔
* s=4: K=3=s−1, so Lemma 1.2 applies. Only A with d=0 survives, giving V=1, B=T²+1 and T∤X+B. ✔
* s=5: A with d=0 has z=0, which violates parity since n=3. ✔
* s=6: K=n=4=s−2, so Lemma 3.1 applies.
  * In A: z even gives m=1. Mg is monic, so d+y ≥ 3 and V=1. Then X²+u is nonzero of degree ≤ 2. ✔
  * In B: d=0 and y ≥ 2, so u+V is nonzero of degree ≤ 1. ✔
* Lemma 3.1 is correctly *not* used at s=4,5, where K > n.

## 2. RELATIVE inputs consumed by §6 (re-checked)

* **Orientation dichotomy and L>r+1.** These come from Lemma 1.2 at m=K ≤ s−1, which needs s ≥ 4. A gives L ≥ N and B gives
  L ≥ N+1. Both orientations give r ≤ N−2 < L−1. ✔
* **Short-side congruences.** A: Mg ≡ −c. B: uMg ≡ c mod T^N, since α=(1−u⁻¹)/T ≡ c/u. These give d+y ≥ N (A) and
  ≥ N−1 (B), hence v+Q < K, hence **d+r+P ≥ K**. Nonvanishing comes from Cor 3.2. ✔
* **G′ ≠ 0.** A cube G forces every prime of V off u(q+p) to have multiplicity ≡ 0 (3). The reason is A₀ ≡ −(q+p)X mod V,
  together with gcd(X,V)=1 and gcd(m,V)=1. Then R₃(F) | rad(u(q+p)M) has degree ≤ d+2 ≤ N < K. This contradicts
  deg R₃(F) ≥ K. That bound needs F′≠0, and §2's inseparable case analysis gives it:
  * I re-derived TUf′−jTf = T^n(nU−jT);
  * M is supported on squares, so d ≤ 2;
  * when 3∤n, f is squarefree;
  * when 3|n, V=1 and 2≠0.
  ✔
* **v ≥ r−Q−1.** This is n ≤ deg R₃(G) ≤ z+(L+Q)+1+v. The bound only needs deg A₀ ≤ L+Q. ✔
* **W.** W is integral because T^δSJ ≡ −qT^NS ≡ −qκ mod M. W(0) = κ/M(0) ≠ 0. W is monic because lc S = lc J = lc p (using
  deg pMg ≥ N > 0 and deg pMX ≥ K > Q+v) and lc(p)² = 1 in F₃. The sign is therefore right for both c, not only for c=1. ✔
* **c-symmetry σ.** This needs z≡v≡n and r≡L (the parity law, Cor 1.7, valid for s ≥ 3). σ preserves mXB=T^n+V and
  X+B=TgV, and maps w₁+uC₁ to ±(w₁+u(−T)C₁)(−T) at the same depth. ✔
* **Scope chain.**
  * Every valid Case B family comes from a tuple (ES3 L2.1 needs only u ≡ 1+cT mod T²).
  * Its depth k+j satisfies j ≥ ⌈(s−2)/2⌉ (γ ≤ j), so validity at any level implies E ≡ −u mod T^{⌈s/2⌉+1}. That is exactly
    what §§1–6 exclude (ES3 Lemma 3.1; FF_THIRDS_CORNER N(s)).
  * Case A is excluded by ES2 §0.2, proved for k ≥ 2.
  * Exact tuples are excluded by Lemma 1.2(ii) for deg u=1.
  * By compactness (ES2 §0.1), x* ∈ O implies there is no finite cover.
  ✔
* **A = T² specifically.** k=2 enters through N(s)=⌈s/2⌉, so that δ∈{3,4}. For A=T the tuple shape (w=Tw₁) and the depth
  both differ. The note does not claim A=T, correctly.
  * Unclaimed remark: for A=T^k with k ≥ 3 one gets δ∈{k+1,k+2}, so the §6 degree test looks only easier. A one-line remark
    or a follow-up lane may be worth it. Unchecked.

## 3. Computational falsification attempts (fresh code; `r2_*.py`, logs `r2_*_log.txt`)

(a) **Independent tuple enumeration** (`r2_check.py`), with its own F₃ arithmetic over all monic T-unit triples, n ≤ 8.
* The tuple sets are identical to `census_s4_17.txt` for every n ≤ 8.
* At x*_c (both c) the maximum depth is 2,2,2,3,2,2 for n=2..7, against the needed 3,4,4,5,5,6. There are no coverings.
* This confirms the s ≤ 6 paragraph independently. It is nonvacuous: 2, 4, 10 and 8 tuples exist at n=2..5.

(b) **Random algebraic check of (6.1) and §3/§7 identities (nonvacuous).**
* Setup: every census tuple (n ≤ 15), every K ≤ n with δ ≥ 1, both orientations. The tuple is placed at its *own* polynomial
  slice point u := −w₁/C₁ mod T^K, so that deg u ≤ K−1 is generic and pq=u.
* All of the following hold in every case, with **0 failures**:
  * MH, VS, W integrality, VW, pXS, T^δSH−W=ug, pgJ: 3,804 each;
  * **(6.1)**: 3,804;
  * the square identity mA₀²+uV=T^nD: 3,804;
  * the degree formula of the second term: 1,694 (where deg qB > deg pX).
* This supports the note's §7 claim that (6.1) holds for general polynomial u.
* **§7 L₀ formula.** At c=1, κ is constant and the formula is right: L₀(0)=nκ/W(0) holds in 3,532/3,532 cases.
  * My first test of the *verbatim* formula at general u failed beyond the constant term (2,972/3,532).
  * Adding the term T·κ′/κ inside the bracket makes it hold to full precision min(δ,2K−n,K) in 3,532/3,532 cases.
  * So the formula is correct as stated for x*. It does **not** transfer verbatim to general u (R2-D6). The note does not
    claim that it transfers, but the "General polynomial slice" paragraph should say so.

(c) **Second contact at x*_c itself** on deep non-covering tuples. Selection: 2·dep ≥ n, with census plus the n=25..28 lop
tuples.
* 26 cases. In 8 of them G is a cube, which is allowed because these tuples do not cover, so R₃(F) ≥ K is unavailable.
* In the other 18: deg R₃(G) ≥ n and v ≥ r−Q−1, with 0 violations. This is small but nonvacuous.

(d) **Pattern-level check of the §6 degree test** (`r2_patterns.py`).
* Inputs: all integer degree patterns allowed by §§1–3 (c=1, both n, both orientations, N=4..150), 647,200 patterns.
* The degree test leaves exactly one survivor class, (B, δ=3, d=b, w=2, h=0), with 2,701 patterns. There are no anomalies.
* deg(2nd) = δ+Q+z+2h was asserted in every pattern.

(e) **Endpoint system** (`part_d`).
* Brute force for d ≤ 11 over the endpoint relations M=T^d+J=mX, X=TWJ+1, uS=TmW−1, with W monic of degree 2.
* Only 4 solutions satisfy all relations except MW=T³SJ−1. None satisfies the full system. This is consistent with (6.3) but
  weak.

(f) **"Does the skeleton prove too much?" probe** (`r2_q5.py`). This looked for Case B tuples over F₅ (k=2) covering
1+cT at n ≤ 9.
* Over F₅ the §6 skeleton is valid only for c=±1, and only if the char-3 inputs (§2 and Cor 3.2) are redone. There is no
  cancellation for c ≠ −1.
* Result: no covering exists at any level reached (N ≤ 6), so the probe is **vacuous**.
* So no falsification of an over-strong argument was available. I report this as a limitation, not as support.

I see no way to falsify the theorem nonvacuously at x* itself. No tuple at x* reaches even δ ≥ 1, since the maximum depth is
about n/2, as in the n=27 depth-14 tuples. The proof therefore rests on the hand re-derivation, backed by (b) and (d).

## 4. Defects and repairs

* **R2-D1 (labels and dependencies; apply before export).**
  * The §0 label reads "rel. §§1–4, §6". §4 is mostly a CERTIFIED census, which the proof does not use. *Repair:*
    "PROVED (rel. §§1–3, the §4 sign-symmetry lemma, §6; FUNCTIONFIELD_ES2 §0.1–0.2; FUNCTIONFIELD_ES3 L1.1, L2.1,
    L2.2, L3.1; FF_THIRDS_CORNER L1.1, L1.2, L3.1, C3.2; FF_ODD_ABSENCE C1.7)". Until the gate is passed, keep the
    CLAIMED / "cross-review owed" wording.
  * The Sources list omits **ES3 Lemma 3.1**. That lemma underlies "all families of a tuple lie in its minimum-level
    cylinder" and N(s)=⌈s/2⌉. Add it.
* **R2-D2 (Scope wording).** "Only the monic linear families of FUNCTIONFIELD_ES2 §0" is wrong. Families are not
  restricted to be monic; monicity of E is a *consequence* in Case B. *Repair:* "all linear families (FUNCTIONFIELD_ES
  §6.2), Case A and Case B".
* **R2-D3 (notation and wording in §6/§7).**
  * D=T³−uW clashes with D=mT^{2K−n}H²−u from §3. Rename it, e.g. Δ.
  * a=1+P−w clashes with a=deg w from FF_THIRDS_CORNER.
  * "all but the extreme coefficient of B" should read "all but the extreme degree pattern of B".
* **R2-D4 (exposition of (6.1)).** Write the three-line derivation and state that pq=u is used, in the step
  pqT^NS = uT^NS. Readers otherwise have to reconstruct it.
* **R2-D5 (heading).** §5 is labelled "superseded by §6". Its residual test remains PROVED and correct; §6 makes it moot.
  *Repair:* "(Round 1; made moot by §6)".
* **R2-D6 (§7 small numerator).**
  * The label "PROVED, necessary classification before (6.1)" is wrong in two ways. §6 does not use this paragraph, and it
    gives coefficient constraints, not a classification. *Repair:* "PROVED; not used by §6".
  * Add that the displayed formula assumes constant κ, i.e. x*. For general u, the bracket acquires +T·κ′/κ (check (b)).
* **R2-D7 (§7 Frobenius label).** The successor of the §4 near-miss at 3k (M³, B³, V³, X_new=u²X³) is PROVED by the §4
  formulas in characteristic 3. It is not EVIDENCE. Only "occurs in the B log" is data. *Repair:* relabel.
* **R2-D8 (§7 Counting).** "(PROVED relative to §6)" only restates §6. "The analytic pruning … already runs to every level,
  including 39..48" reads as if a computation had been run. *Repair:* delete the paragraph, or replace it with "§6 proves
  emptiness at every level; no computation beyond N=38 was run; §§4–5 are now historical."
* **R2-D9 (§7 General slice; mixed labels; apply before export).** The paragraph is labelled PROVED but contains Assessment
  about integer settings ("no analogous control … follows", "4=1 is special"). *Repair:* split these off as "(Assessment)".
* **R2-D10 (STATUS delta and export flags; apply before export).**
  * The proposed row lacks a label and a path. *Repair:* "F₃[T], A=T²: x*_1, x*_2 ∈ O(3,T²), hence no finite linear covering
    of ES₃(T²,·) (PROVED rel. …; `notes/z78/F3_CONJ.md` §6; cross-review: `data/z78/xreview/REVIEW_F3_CONJ_R2_OPUS.md`).
    Not A=T, not individual P, not integer ES."
  * The export must also fix every master quote of "Conjecture 0.2 open":
    * STATUS.md:161;
    * FRONTIER.md:1261 ("Only q = 3 (CONJECTURE 0.2) is open");
    * FRONTIER.md:1336;
    * FRONTIER §7 item 10 (FRONTIER.md:2429);
    * WAVES "Open:" lists. These are historical, so leave them and add the new wave line.
  * The HEADLINE gate requires a **priority check**, which is not recorded. Function-field Erdős–Straus / finite-covering
    literature should be searched.
* **Nits.**
  * §6 "Its degree is at least δ>1": say "at least δ ≥ 3".
  * In the endpoint, note that r = 3+j follows from X=TWJ+1, which gives j = r−3 consistently.
  * The small-level paragraph could state that the c=1 reduction uses Cor 1.7 at s ≥ 3.

## 5. Debate and challenges

1. **Is it too easy?** The closing step is a three-line degree count once W is bounded. Its whole strength comes from the
   Round 1 bound w ≤ 1+P, i.e. from the second contact and G′≠0. I therefore re-derived that chain again rather than
   inheriting R1's acceptance. It holds. Check (c) exercises it at x* on real deep tuples, and check (d) shows that the
   inequality bookkeeping has exactly the claimed single escape. I could not construct any scenario in which a hidden
   cancellation, a sign or a non-monic leading coefficient defeats it at c=1.
2. **Why was the near-miss family not a counterexample to (6.1)?** On the §4 B-family (δ=4, d=k, w=0), deg pMW = k+1 < N.
   §6 would force LHS=κu, but g is not a polynomial there, so S, W and (6.1) are not polynomial identities. This matches the
   family failing exactly TV|X+B. It is a good sanity reading of §6.
3. **Reach.** The argument appears to extend to A=T^k for k ≥ 3 (δ only grows). For q=9 or 27 with A=T^k it would need c²=1
   or a non-cancellation check, together with char-3 §2. It does not touch A=T (q=3 is covered there) or integer ES.
4. **Lean.** The §6 algebra (polynomial identities plus degree bookkeeping) and the §§1–3 lemmas over F₃[T] look
   formalisable with moderate effort. Because this is a HEADLINE, that is recommended but not required by AGENTS.

## 6. Replay
```
cd data/z78/xreview; export TMPDIR=$PWD; ulimit -v 6000000
uv run --offline --no-project python r2_check.py 8 11   > r2_check_log.txt     # (a),(b),(c),(e) ~2 s
uv run --offline --no-project python r2_patterns.py 150 > r2_patterns_log.txt  # (d) ~7 s
uv run --offline --no-project python r2_q5.py 5 9       > r2_q5_log.txt        # (f) ~2 min, vacuous
```
`r2_l0dbg.py` is the diagnostic that found the κ′/κ term (R2-D6).
