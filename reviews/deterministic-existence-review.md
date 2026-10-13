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

(continued below as the review proceeds)

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
