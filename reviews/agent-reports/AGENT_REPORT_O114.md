# AGENT_REPORT_O114 — paper/es-typei-heegner-note.tex

Branch `side-agent/typei-heegner-note`. Deliverable: `paper/es-typei-heegner-note.tex` / `.pdf`
(amsart 10pt, 25 pp incl. TOC + bibliography; two pdflatex passes, 0 warnings / undefined refs / over-/underfull
boxes); `paper/README.md` entry.

## Content
§1 intro (ET Thm 1.1 quoted exactly: `N log²N ≪ Σ_p f_I(p) ≪ N log²N log log N`, `Σ_p f_II(p) ≍ N log²N`;
ET p. 5: log log from BT in very short progressions, "we conjecture that it should be eliminated"; ET §9 p. 36
parenthesis "[no] similar trick ... in the Type II case" reproduced literally, with the MN3 reading as Type I
marked as interpretation); Hypothesis (SEL); Theorem A; status/dependencies; literature (search-limited).
§2 Type I weight, MN3 Lemma 3.1 (SL₂), Lemma 3.2, Prop 3.3 (R_bad), Prop 2.3, LOGLOG Lemmas 8.2–8.4 (BT outside
R_bad), large-c input. §3 Heegner forms, distance formula, uniform separation (Lemma 2.2), coordinates, sieve
group, boxes. §4 Sobolev duality (L4.1–4.4). §5 DI Thm 2 / Drappeau Prop 4.7, Prop 5.1 (variance, CONDITIONAL).
§6 Lemma 6.1, Thm 6.2 (per-d, CONDITIONAL), Lemma 6.3. §7 Prop 7.1 (K_a, Poisson + Weil). §8 Lemma 1.1, Thm 8.1.
§9 unconditional discussion (Kim–Sarnak strip ≈ 7/32; DI Thm 5/6 partial; no unconditional improvement).
§10 open problems.

## Deviations from the source EXCEPTIONAL_TYPEI_LOGLOG.md (for the referee to check)
1. **Thm 6.2:** the source's `#Λ_d(q) ≪ q² #Λ_d(1)` uniformly in c fails for `(q,c) > 1` (a split prime ℓ | c
   contributes `2ℓ(ℓ−1)`); the note keeps a factor `κ_c(q)^{1/2} = 2^{ω((q,c))/2}`. Harmless: the assembly sieve
   uses only ℓ ∤ 2cs, so `(q,c) = 1` there (checked in §8 step 4).
2. **q = 1 normalisation:** the source writes the character projector `2/φ(q)` also at q = 1, where the index is 1;
   the note uses index⁻¹ (absolute constants only).
3. **Primitivity (Lemma 6.3):** only the Type I subset 𝓕_d^I is primitive (`[2,6,6] ∈ 𝓕_3` is not); the note
   restricts the class-number argument to it, as its application already was.
4. MN3 Thm 3.8 (LD reduction) is not used by the assembly; only the large-c input from its proof (step (1)) is
   stated and cited.
5. Iwaniec-book section/theorem locators (§§4–5) are inherited and unverified (book not in sources/); stated
   visibly in §1. DI and Drappeau statements/normalisations were checked against the sources by the drafting agent.

## Process / honesty notes
Drafted by three deep subagents (§§1–3, 4–6, 7–10) under a shared conventions file, then one deep consistency +
trim pass; I spot-checked the intro, Theorem 8.1 statement and the ET quotations against the PDF myself. I did
**not** re-derive §§4–8 line by line; the mathematical content rests on the source and R111 rounds 1–2. Items
1–3 above are corrections found during drafting that are not in the reviewed source — the referee should
confirm them and, if accepted, the parent may back-port them to EXCEPTIONAL_TYPEI_LOGLOG.md.
Status: CONDITIONAL on (SEL); internal review only; ES not claimed.
