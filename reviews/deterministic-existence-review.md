# R168 — hostile review of O168 `DETERMINISTIC_EXISTENCE.md` (branch side-agent/deterministic-existence @ ff4f59d5)

Reviewer: R168. From-scratch scripts: `scripts/review_de_*.py`. ES is not solved anywhere; nothing here changes that.
Every proof below was re-derived by hand; every finite claim was re-checked with independent code.

## Summary verdicts

| claim | verdict | key defect |
|---|---|---|
| Prop 3.1 (isotropy = congruences + "all prime factors split") | SOUND-AFTER-REPAIRS | D3 (statement vague; squarefree reduction itself needs factorisation of c(p,θ)) |
| Prop 3.2 (Type I ⇒ χ_{−4d}(p) = −1; conic anisotropic) | SOUND | — (checked 1491 triples, 0 violations) |
| Prop 3.3 (Σ ⊆ H; odd-character dual; e \| 24 ⇒ Σ = H; e = 3 norm form) | SOUND-AFTER-REPAIRS | D4 ("norm-form representation" false for e = 24 via ℚ(√−6), h = 2), D5 (quantifier order in (a)) |
| Prop 3.4 (Jacobi forcing) | SOUND-AFTER-REPAIRS | D6 (missing hypothesis p ≡ 1 (4) / e < p); 6816 cases, 0 violations |
| §4 Pell, PROVED core (Rédei relations) | SOUND (core); surrounding "invisible to every genus mechanism" is Assessment | D9 |
| Prop 5.1 | SOUND | — |
| Cor 5.2 / §5 "closed for every quadric piece" | GAP (overclaimed scope) | D1 (MAJOR: "without positivity" is false — integral points exist), D2 ("every quadric piece") |

| Prop 6.1 (box form) | SOUND | — |
| Prop 6.2 (group-level forcing ⇔ −1 ∈ ⟨r_e⟩; 2-adic criterion) | SOUND (forward + criterion); converse SOUND only in the abstract-integer model | D7; criterion checked for all odd e < 400, all r: 0 mismatches |
| Prop 6.3 (Σ = H ∀N ⇔ e \| 24; Σ-forcing ⇔ p ≡ −4 (e)) | SOUND-AFTER-REPAIRS | D8 (order-3 counterexample to the ⇒ proof step), D7 |
| Prop 7.1 (sharing dichotomy) | SOUND | — |
| Prop 7.2 (joint data force exactly block witnesses) | SOUND-AFTER-REPAIRS | D7 (model), D10 (the "therefore" sentence overreaches) |
| Thm 7.3 | SOUND | from-scratch: E ∈ {7,11,15,19,23}, 12 primes each, s_e = (1+e)/4 and 0 block witnesses |
| Cor 7.4 (Linnik) | SOUND | D11 (MINOR: say which E defines "block witness"; monotonicity) |
| §7 EVIDENCE (block-witness rates) | SOUND (reproduced on p < 3·10⁵, E = 40) | — |
| Prop 8.1 (Type I forcing side empty) | SOUND in the abstract-integer model | D7 |
| §3.4 EVIDENCE (Jacobi table) | SOUND (reproduced qualitatively on p < 6·10⁴) | — |
| §1 catalogue, rows 1, 4, 9, 23, 25 | SOUND for 1, 4, 9, 23; row 25 loosely paraphrased | D12, D13 (remarks inconsistent with ○ entries) |

## Defects

**D1 (MAJOR) — Cor 5.2, "with or without positivity" is false.** Location: §5, Cor 5.2 and the last sentence of §5
("the descent would have to manufacture integral points that provably do not exist"); AGENT_REPORT_O168 item 5.
Prop 3.2 only excludes **positive** f (it uses χ_{−4d}(f) = +1 for f > 0; for f < 0 one gets χ_{−4d}(f) = −1 and
hence χ_{−4d}(p) = +1, no contradiction). The conic C_{c,d,p}: 4cd·ea − 4da² − pe = 1 does have integral points
when χ_{−4d}(p) = +1: e.g. p = 5, c = d = 1: (a, e) = (1, −5) and (−6, −5); p ≡ 1 (mod 4cd) always gives
a = (p−1)/(4cd), f = −1, e = −(1+4da²). `scripts/review_de_props.py`: 230 integral points on C_{c,d,p} with
χ_{−4d}(p) = +1 (p < 120, c ≤ 3, d ≤ 5, |a| ≤ 300), none positive; 1192 negative-f divisor solutions with χ = +1.
So a rational ⇒ integral principle *without* positivity is **not** refuted by Prop 5.1 on this family — and it can be
true (integral points exist). What is refuted is exactly "positive rational ⇒ positive integral" (which is the only
version relevant to the triage-errata loophole, so the conclusion "row 6 ✗" survives).
*Repair:* replace "with or without positivity" by "for any rule that outputs **positive** integral points (in
particular any positivity-preserving descent)"; add one sentence: "without positivity integral points can exist
(e.g. f = −1 when 4cd | p − 1), so the obstruction is the sign, not integrality."

**D2 (MINOR) — scope of "every quadric piece".** Location: §5 last sentence, §9 bullet 3, report item 5 ("on any quadric
piece"). Prop 5.1 covers the two explicit families {C_{c,d,p}} (Type I, fixed (c,d)) and the Type II hyperbolas.
It says nothing about other quadric substructures (POINTWISE_TERNARY Comp 6.1 lists 57), nor about the surface X_d itself
(ef − 4da² = 1 without the side condition has integral points, e.g. e = f = 1, a = 0). *Repair:* "on every Type I level
conic C_{c,d,p} and every Type II hyperbola"; drop "any/every quadric piece" unless the 57 pieces are each checked.

**D3 (MINOR) — Prop 3.1 is a paraphrase, not a statement.** Location: §3.2. (i) "Reduce to the squarefree, pairwise
coprime case in the standard way" already requires the squarefree kernel and the gcd's of a(p,θ), b(p,θ), c(p,θ), i.e.
factorisation data, and may move p-dependent factors between coefficients; the clean split "congruence conditions at
p-free coefficients / all-primes-split at ℓ | c" holds only after this reduction and only if a, b are p-free. (ii) The
condition at ℓ | c(p,θ) also needs the ℓ | a, ℓ | b conditions (bc, ac squares mod ℓ), which involve c(p,θ) mod ℓ —
congruences of p only if c is polynomial in p. (iii) "strictly stronger than ... one divisor in a class" is not
proved anywhere. Label should be "PROVED (restatement of Legendre, under the stated reductions)" with (i)–(ii) spelled
out, and the comparison sentence labelled Assessment. Also §3.1 "−ab is a square mod c, bc..." is truncated: the three
conditions for aX² + bY² = cZ² are −ab □ mod c, bc □ mod a, ac □ mod b.

**D4 (MINOR) — Prop 3.3(b)/§3.3 closing paragraph: "fail exactly when a quadratic norm-form representation exists".**
For e | 24 the failure is: ∃ odd quadratic χ mod e with χ(ℓ) = 1 ∀ ℓ | N. For e = 24 the odd characters are
χ_{−3}, χ_{−4}, χ_{−8}, χ_{−24}; for χ_{−24} the field ℚ(√−6) has class number 2, so "all ℓ | N split" means N is a
norm of an *ideal* (represented by x² + 6y² or 2x² + 3y², i.e. by the genus/some form), not a norm-form
representation. True as stated for e ∈ {3, 4, 6, 8, 12} (class number 1 fields) and in particular for e = 3 (the only
case used for p ≡ 1 (4)). *Repair:* "…exactly when N is (primitively) represented by one of the forms of
discriminant −3, −4, −8 (or a form of discriminant −24)"; or restrict the sentence to e = 3.

**D5 (MINOR) — quantifier order in Prop 3.3(a).** "every prime factor of N splits completely in some imaginary cyclic
subfield K_χ" reads ∀ℓ ∃K; the correct statement is ∃ odd χ (one K_χ) ∀ ℓ | N. *Repair:* "there is one imaginary
cyclic subfield K_χ ⊂ ℚ(ζ_e) in which every prime factor of N splits completely".

**D6 (MINOR) — Prop 3.4 hypothesis.** N_e = (p+e)/4 is an integer only for p ≡ −e ≡ 1 (mod 4); gcd(N_e, e) = 1
needs e ≠ p (e < p). Add "p ≡ 1 (mod 4), e < p". Proof otherwise correct (Jacobi multiplicativity over prime factors
with multiplicity; non-residue in a cyclic group of order 2·odd has even order, hence a power equals −1). From-scratch
check: p ≡ 1 (4) < 2·10⁴, prime e ≡ 3 (4) < 80, 6816 Jacobi-firing slices, 0 violations.

**D7 (MAJOR, quantifier/model) — "residue data force / do not force" is a statement about abstract integers, not about
primes p.** Locations: Prop 6.2 converse ("N prime ≡ r_e has H = ⟨r_e⟩"), Prop 6.3 "residue data alone force
Σ-success iff r_e ≡ −1", Prop 7.2 "⇒" ("the data are consistent with P_e prime (Dirichlet …)"), Prop 8.1 ("minimal
consistent H is ⟨p²⟩ (N prime)"), and the labels "PROVED rel. Dirichlet". Dirichlet supplies a *prime N* (resp. P_e)
in the residue class; it does not supply a *prime p* with N_e(p) = (p+e)/4 prime (resp. (p+e)/(4s_e) prime), which is a
prime-pair (Dickson/Schinzel) statement and open. So the converses establish only: "no argument that uses nothing
about N_e beyond its class (and the smooth part) can force success" — a meta-statement about proof methods in a model
where N_e (or P_e) is an arbitrary integer with the given data. They do **not** establish that, for primes p in the
relevant class, slice e fails (or lacks group-level success) for any p. The text never says the latter, but "forced
iff" invites it, and §9 ("characterised exactly") reads as if it were about p. Note Thm 7.3 is genuinely about primes
p and is unaffected. *Repair:* add a definition before Prop 6.1: "We say data D *force* a property of N if it holds
for every integer N (coprime to e) with data D; the converse directions below exhibit such integers via Dirichlet
and say nothing about whether N_e(p) for a prime p can realise them (that would need a prime-pair hypothesis)."
Relabel the converse halves "PROVED (abstract-integer model)".

**D8 (MINOR) — Prop 6.3 "⇒" proof step is false as written.** "N = ℓ prime of order > 2 gives Σ = {1, ℓ^{±1}} ≠ ⟨ℓ⟩":
for ord ℓ = 3, ⟨ℓ⟩ = {1, ℓ, ℓ²} = {1, ℓ, ℓ⁻¹} = Σ (e.g. e = 7, ℓ ≡ 2; e = 9, ℓ ≡ 4; `review_de_props.py`). The
conclusion survives: if G_e has exponent > 2 it has exponent ≥ 4 (exponent is even since −1 has order 2 for e ≥ 3, and a
finite abelian group has an element of order equal to its exponent), so take ℓ of order ≥ 4, where |Σ| ≤ 3 < |⟨ℓ⟩|.
*Repair:* replace "order > 2" by "order equal to the exponent of G_e (≥ 4)". (Verified: exponent ≤ 2 ⇔ e ∈ {1,2,3,4,6,8,12,24}.)

**D9 (MINOR) — §4 interpretation and labels.** (i) 17.8 % vs 14.3 % over 1681 slices is ≈ 4 binomial standard errors
(s.e. 0.85 %), so "essentially a random splitting" is not what the raw numbers say. My from-scratch replication
(own Pell solver; `review_de_evidence.py`) reproduces 1681 / 0.2855 / 0.1779 / 0.1428 exactly and shows the excess
is a composition effect: restricted to non-trivial Pell splittings, hits 0.2065 vs 0.1954 for a uniformly random
non-trivial splitting (1201 slices; difference < 1 s.e.). State this. (ii) For even N_e, D₁ = gcd(N_e, x − 1) always
contains the factor 2 (x is odd), and Legendre's "each prime of D divides exactly one of x ± 1" fails at 2; either
restrict to odd N_e or say how 2 is assigned. (iii) The Rédei relations (PROVED core) hold for odd ℓ only; re-derived:
correct. (iv) "invisible to every genus/Rédei/ambiguous-class mechanism" is Assessment, not a consequence of Prop
3.3(b) (which concerns Σ vs H, not whether a condition is quadratic); label it so.

**D10 (MINOR) — Prop 7.2's closing "therefore".** "Any pigeonhole/Hall/LP argument that uses only Γ_p(E)'s incidence
structure and residue classes therefore proves at most 'some slice has a block witness'". Γ_p(E) as defined contains
the private primes as vertices; an argument using *their* residue classes has the full box Σ_e(N_e) and can certify
any witness. *Repair:* "…uses only the congruence part of Γ_p(E) together with the classes c_e of the private
cofactors…", labelled Assessment (it is a meta-statement, cf. D7).

**D11 (MINOR) — Cor 7.4: block witnesses depend on E.** s_e is the ((E+1)/4)-smooth part, so "block witness at
slice e" is relative to E. In Cor 7.4 E = E(p) (the E for which p is the Linnik prime) and the conclusion is about
slices e ≤ c₀ log p ≤ E with block witnesses relative to that E. Since Σ_e(s'_e)·{1, c'^{±1}} ⊆ Σ_e(s_e)·{1, c^{±1}}
for E' ≤ E (a block for E' is a product of primes of s_e and the block P_e), the conclusion also holds relative to
E' = ⌊c₀ log p⌋. Say so. Otherwise re-derived and SOUND: log M_E = ψ(E) + O(log E) + Σ_{ℓ ≤ (E+1)/4}(K_ℓ+1)log ℓ
≤ (1 + 1/4 + 1/4 + o(1))E (numerically log M_E/E = 1.38, 1.49, 1.47, 1.49 at E = 50, 200, 1000, 4000); Linnik
gives p_E ≡ 1 (M_E), p_E ≪ M_E^L, p_E > M_E → ∞; c₀ = 1/(1.5L) − ε (≈ 0.133 with Xylouris' L = 5). Thm 7.3's proof
re-derived line by line (N_e ≡ (1+e)/4 mod ℓ^{K_ℓ+1} and mod 2^{K₂+1}; v_ℓ((1+e)/4) ≤ K_ℓ; c_e ≡ 1;
a'+b' ≤ (1+e)/4 + 1 < e): correct. Minor wording: "∏_{3 ≤ ℓ ≤ (E+1)/4}" should say ℓ prime. Interesting
from-scratch side fact: of the first 4 Thm-7.3 primes for each E ∈ {7,…,23}, 18/20 are nevertheless solved at some
slice e ≤ E by a private-prime witness — Thm 7.3 is a statement about certificates, not about ES failure (the text
says so; good).

**D12 (MINOR) — §1 row 25 paraphrase.** Schur (1912)/M. R. Murty (1988): a "Euclidean proof" for primes ≡ a (mod k)
exists iff a² ≡ 1 (mod k); the mechanism is a polynomial whose prime divisors lie (up to finitely many) in the
classes 1, a. The "shape" cell ("if N ≡ a (k) with a² ≡ 1, some prime factor of N lies in a non-trivial class") is
not that theorem: for a ≢ 1 it is trivially true (if all prime factors were ≡ 1 then N ≡ 1), and it omits the
polynomial construction that is the content of Schur–Murty. Rephrase the cell. Rows 1 (Thue's lemma; 0 < x²+y² < 2p), 4 (Legendre's
three conditions; Holzer/Mordell bound |X| ≤ √(bc), |Y| ≤ √(ac), |Z| ≤ √(ab)), 9 (Legendre: negative Pell for
p ≡ 1 (4); x² − py² = −2 for p ≡ 3 (8), +2 for p ≡ 7 (8)) and 23 (Croot 2003 colouring; Bloom 2021 positive upper
density) checked: accurate. (Primary sources not in sources/; checked against standard statements.)

**D13 (MINOR) — §1 remarks / §9 / report inconsistent about which rows are open.** The remark says rows 1, 4, 6, 9, 10
are the only ones not failing at a proved barrier; but rows 11, 16, 18, 29 carry ○ (open) in the table. §9 lists
4, 9–10, 11; the report says "only rows 4, 6, 9, 10". *Repair:* one consistent list, e.g. "not closed by a proved
statement: 1 (?), 4, 9, 10, 11 (○), 16, 18, 29 (○ for growing parameters); 6 closed by §5 (for positive points, D1)".
