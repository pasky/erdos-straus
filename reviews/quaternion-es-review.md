# R130 — hostile review of O130 (QUATERNION_ES.md, AGENT_REPORT_O130{,b}.md, scripts/quat_*)

Reviewer: side-agent/review-quaternion. Reviewed: QUATERNION_ES.md as merged from `side-agent/quaternion-es`.
From-scratch scripts (none reuse the author's code or `geo_common`):
* `scripts/review_quat_hilbert.py` — my own Type I enumeration over (a,c,d) (f = 4acd − p | 4a²d+1) and my own
  Hilbert symbol (Serre's formulas, incl. ℓ = 2). Log `logs/review_quat_hilbert_3000.txt`.
* `scripts/review_quat_brute.py` — raw brute force of `4/p = 1/x+1/y+1/z`, split into Type I / II, compared with
  the parameterisations of Lemma 1.1 and Prop 3.2. Log `logs/review_quat_brute_200.txt`.
* `scripts/review_quat_symbolic.py` — my own quaternion multiplication in (α,β), symbolic in d,m,a,b,c,p.
  Log `logs/review_quat_symbolic.txt`.
* `scripts/review_quat_fixed_de.py` — §3.4 pairs and the 40/93, 120/450 counts. Log `logs/review_quat_fixed_de.txt`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (K-factorisation) | SOUND |
| Lemma 1.2 (Λ_{d,m}, disc 4dm−1) | SOUND |
| Prop 1.3 (Λ ⊂ B_{p,∞}, reduced disc pe) — algebra/ramification part | SOUND-AFTER-REPAIRS (minor: p ∤ e used silently) |
| Prop 1.3 — "Gross–Zagier parameter x = 2" | GAP in the citation (GZ hypotheses fail); the arithmetic identity is trivial and correct |
| Remark after 1.3 (minimal hypotheses for B_{p,∞}) | SOUND-AFTER-REPAIRS (add v_p(pe) odd) |
| Prop 2.1 + isogeny reading | SOUND |
| Prop 2.2 | SOUND (mathematically trivial); one heuristic sentence over-labelled |
| Lemma 3.1 | SOUND (symbolically verified) |
| Prop 3.2 + ideal reading | SOUND |
| §3.3 | SOUND as Assessment; cited facts correctly stated |
| §3.4 (EVIDENCE) | SOUND — every number reproduced |
| §4 (ET Prop 1.6, square-mimicking) | SOUND (minor: same p ∤ e point) |
| Prop 5.1 | GAP — "PROVED modulo cited shape" cites a shape (GZ coprime-fundamental F(n)) that does not apply; conclusion repairable by a direct local argument (given below) |
| Novelty of x = 2 dictionary | UNVERIFIABLE (no hits; see §N) |
| Labels / scope of negative statement | Mostly honest; scope paragraph in §6 adequately limited |

## Claim-by-claim checks

### Lemma 1.1 — SOUND
`(1+2aw)(1+2bw) = 1 − 4abd + 2(a+b)w`; comparison with `e(2cw − p)` gives `4abd − 1 = pe`, `a+b = ce`, i.e.
ET's Type I tuple with `(x,y,z) = (abdp, acd, bcd)`. The bracketed equivalence `e | a+b ⟺ e | 4a²d+1` (given
`4abd ≡ 1 (e)`) is correct: `4ad(a+b) = (4a²d+1) + (4abd−1)` and `gcd(4ad,e) = 1`.
Brute force (`review_quat_brute.py 200`): for all 45 primes 3 ≤ p < 200 the set of Type I triples from raw
Egyptian-fraction search equals the set produced by the (a,c,d)-parametrisation. Note the map tuple → triple is
not injective (ET Prop 2.2: uniqueness only after imposing gcd(a,b,c) = 1, "quotienting by dilations"); e.g.
p = 107 has 17 triples but 23 tuples. Lemma 1.1 is an existence statement, so this is harmless (see MINOR-4).

### Lemma 1.2 — SOUND
Symbolic check: with `u = i`, `v = (j − i)/(2d)` in `(−d, −d(4dm−1))` one gets `u² = −d`, `v² = −m`,
`uv + vu = 1`; Gram `trd(x_i x_j)` on `(1,u,v,uv)` is exactly the author's matrix, determinant `−(4dm−1)²`.
Closure: `vu = 1 − uv`, `u·uv = −dv`, `uv·v = −mu`, `v·uv = (1−uv)v = v + mu`, `uv·u = u(1−uv) = u + dv`; all in the ℤ-span; fine.

### Prop 1.3 (ramification part) — SOUND-AFTER-REPAIRS
Re-derivation. `(−d, −dpe)`, `pe = 4abd − 1` odd, `gcd(d, pe) = 1`.
* ℓ odd, ℓ | e, ℓ ≠ p: `4a²d ≡ −1 (e)` ⇒ `−d ≡ (2a)^{−2}` is a unit square ⇒ symbol 1. ✓
* ℓ odd, ℓ | d: `(−d,−1)_ℓ(−d,pe)_ℓ = ((−1/ℓ)(pe/ℓ))^{v_ℓ(d)}` and `pe ≡ −1 (ℓ)` ⇒ 1. ✓
* ℓ = p: `(−d,−dpe)_p = (−d/p)^{v_p(pe)}` — this equals `(−d/p)` **only if p ∤ e**, which the proof uses silently.
  It is true: if p | e then p | a+b, `b ≡ −a`, `−4a²d ≡ 1 (p)`, so `(−d/p) = +1`, contradicting GEOMETRY Prop 5.1
  (whose proof I re-checked: `p ≡ −f (4d)`, `(−4d/f) = 1`, odd character ⇒ `(−4d/p) = −1`). (MINOR-1)
* ℓ = 2 via product formula: legitimate. Independently, my script evaluates the 2-adic symbol directly.
* ∞: both entries negative ⇒ −1. ✓

Numerics (own enumeration, own Hilbert symbol, p < 3000, all ET tuples with a ≤ b — 26007 tuples, i.e. all
dilates, more than the author's 19690 normalised triples): **Ram = {p, ∞} in every case; directly evaluated
symbol at 2 is +1 in every case; p | e never occurs.** The author's "27–42% failure of other splits" was not
re-checked (unimportant EVIDENCE remark).
Index e in every maximal order: reduced disc of maximal order of B_{p,∞} is p ⇒ index pe/p = e. ✓
Deuring step: Λ ⊂ some maximal O ≅ End E (Deuring); Deuring lifting of `(E,u)` and `(E,v)` separately gives CM
curves with CM by orders containing ℤ[√−d], ℤ[√−ab] reducing to E. Correct, with the author's own hedge that the
optimally embedded orders may be larger (e.g. `d ≡ 3 (4)`: `(1+u)/2` may lie in O). See MAJOR-1 for "x = 2".

### Prop 1.3 — "Gross–Zagier parameter x = 2": GAP (citation)
What is *proved*: the identity `(D₁D₂ − 4)/4 = 4abd − 1 = pe` for `D₁ = −4d`, `D₂ = −4ab`, and that the order
generated by ℤ[√D₁/2]=ℤ[u] and ℤ[v] (with `uv+vu = 1`) has reduced discriminant `(D₁D₂ − x²)/4`, x = 2 — this
matches the standard "order generated by two quadratic orders with relative trace x" computation (verified).
What is *cited*: Gross–Zagier, *On singular moduli* (Crelle 355, 1985). Their factorisation of
`J(d₁,d₂) = ∏(j(τ₁) − j(τ₂))` with factors `F((d₁d₂ − x²)/4)` is proved under the hypotheses **d₁, d₂ < 0
fundamental and coprime**. Here `D₁ = −4d`, `D₂ = −4ab` are never coprime (both ≡ 0 mod 4) and −4d is often
non-fundamental. So GZ's theorem does not apply; the correct framework is Lauter–Viray ("On singular moduli for
arbitrary discriminants", IMRN 2015), or a direct count of embeddings of Λ. (Source PDFs not in sources/; I
state GZ's hypotheses from memory — they are the well-known hypotheses of the main theorem.) → MAJOR-1.

### Remark after Prop 1.3 — SOUND-AFTER-REPAIRS
The listed sufficient conditions (`4dm ≡ 1 (p)`, `(−d/p) = −1`, `(−d/ℓ) = 1` for ℓ ∥^{odd} e) also need
`v_p(pe)` odd (e.g. p ∤ e); for general m (not from a Type I solution) p | e is not excluded a priori. Same in
Prop 2.1(i). (MINOR-1.)

### Prop 2.1 and the isogeny reading — SOUND
Prop 2.1 is Lemma 1.1 with b eliminated; `gcd(c,p)=1` automatic: `p | c` ⇒ `a+b ≥ pe = 4abd−1`, but
`a+b < 4ab−1` for a,b ≥ 1. ✓
Isogeny reading: I re-derived all pairings `⟨x,y⟩ = ½tr(x ŷ)` on `(φ₁, φ₂, uφ₁, uφ₂)`:
`⟨φ₁,φ₂⟩ = ½tr(v̂) = 0`, `⟨φ₁,uφ₂⟩ = ½tr(\widehat{uv}) = ½tr(uv) = ½`, `⟨φ₂,uφ₁⟩ = ½tr(vū) = −½`,
`⟨φ_i,uφ_i⟩ = ½deg φ_i·tr(ū) = 0`, `⟨uφ₁,uφ₂⟩ = ½d·tr(v̂) = 0`. So Gram = `[a,1,bd] ⊥ [b,−1,ad]`, det
`(4abd−1)²/16` (symbolic check), and Hom(E',E) has det `p²/16` ⇒ index e. Separability: `p ∤ ab` since
`4abd ≡ 1 (p)`. Converse direction: from such data, a = deg φ₁, b = deg φ₂, e := index, `4abd − 1 = pe` and
`e | deg(φ₁+φ₂) = a+b` ⇒ Type I. ✓ (Sound but, as the author says, a re-encoding.)

### Prop 2.2 — SOUND (trivially); one over-labelled sentence
`4dm − 1 = pe` with fixed (d,e) ⟺ `p ≡ −e^{−1} (4d)` (gcd(e,4d) = 1 is forced), m determined. ✓ The rewriting
`X² − Y² = 4ab = 4m`, `e | X` is correct. The sentence "The Siegel-theta reading … does not absorb (ii) …
p-dependent target set" is a heuristic, not a proof, but sits under a PROVED heading. (MINOR-2.) "Exactly the
shape of GEOMETRY_ES Prop 3.2" not re-checked by me.

### Lemma 3.1 — SOUND
Own quaternion arithmetic in `(−d,−p)`: `(2ai+j)(2bi−j) = (p − 4abd) − 2(a+b)k` exactly; norms
`N(2ai+j) = 4a²d + p`, `N(1+2ck) = 1 + 4c²dp`. With ET Type II (`4abd − p = e`, `a+b = ce`) this is
`−e(1+2ck)`; the identities `ef = 4a²d + p` (f = 4acd − 1) and `ff' = 1 + 4c²dp` check by hand
(`4acd·e = 4a²d + p + e`).

### Prop 3.2 + ideal reading — SOUND
Brute force: for all 45 primes p < 200 the Type II triples of raw search coincide with those generated from
"`4d | p+e`, `a | m = (p+e)/4d`, `e | a + m/a`" (`(x,y,z) = (abd, acdp, bcdp)`). `p | e` ⇒ `4abd ≤ 2(a+b)` ⇒
a=b=d=1, p=2: ✓.
Ideal reading: R = ℤ⟨i,j⟩ has reduced disc 4dp ✓; `α, β` primitive (j-coefficient ±1) ✓; for primitive
2×2 matrices over ℤ_ℓ with det ≡ 0 (ℓ^k), Smith form `U diag(1,δ) V` shows ker/im mod ℓ^k are free rank-1
summands, so `αβ ≡ 0 (ℓ^k) ⟺ im β̄ = ker ᾱ` ✓. Small point: the restriction "ℓ ∤ 2dp" is automatic for every
ℓ | e (e odd; gcd(e,d) | p; p ∤ e) — worth saying, otherwise it reads as if some primes of e were excluded.
"Brandt/Hecke T_e adjacency" is interpretation, fine.

### §3.3 — SOUND (as Assessment)
`disc[f,4ad,de] = 16a²d² − 4def = −4dp` ✓. √−dp of degree dp with p ramified factors as `ψ∘Frob`, ψ of degree d
between E^{(p)} and E ✓; d = 1 ⟺ E ≅ E^{(p)} ⟺ j ∈ 𝔽_p ✓ (Delfs–Galbraith: not accessed, statement standard).
The two matrices preserve the shape `[A, 4d·, d·]` (checked by hand: `[[1,2d],[0,1]]`: B ↦ B + 4dA,
C ↦ C + 2dB + 4d²A; `[[1,0],[2,1]]`: A ↦ A+2B+4C, B ↦ B + 4C) ✓; infinitude of representatives ✓ (stabiliser of
a definite form is finite). "Finitely many ES-good" relies on GEOMETRY Prop 4.1 (not re-checked).

### §3.4 — SOUND (all EVIDENCE reproduced)
`review_quat_fixed_de.py`: (5,23): p = 313, m = 360, a = 10, b = 36, a+b = 2·23 (ES); p = 73, m = 84, no divisor
(no ES); `(−5/313) = (−5/73) = −1`, `(−5/23) = 1`, and m ≡ 15 ≡ (4d)^{−1} (mod 23) in both. (10,7): 457 (a = 2,5)
vs 97 (none) ✓. Type II (1,7): 73 vs 97; (1,11): 73 vs 193 ✓. Filtered counts: **40/93 and 120/450 reproduced
exactly.**

### §4 — SOUND
ET Prop 1.6 checked against `sources/elsholtz-tao-1107.1010.pdf`: "For any odd perfect square n,
f_I(n) = f_II(n) = 0" ✓. Type I(n): GEOMETRY 5.1's argument gives `(−4d/n) = −1`, impossible for n an odd square
✓. "Symbol at p is `(−d/p)^{v_p(n)}`" again assumes p ∤ e (MINOR-1). Type II: `(n/f) = (−d/f) = −1` needs
gcd(n,f) = 1, which holds since p ∤ abd. Square-mimicking: `(f/p) = −(−1/p) = −1` for p ≡ 1 (4) forces a prime
ℓ | f with `(ℓ/p) = −1` ✓ (this is GEOMETRY Prop 5.2; "Lemma CT" not looked up).

### §5 / Prop 5.1 — GAP (misapplied citation; conclusion repairable)
1. The displayed sum and "F depends only on n and the genus characters ε at primes of n" is the shape of the
   **coprime, fundamental** Gross–Zagier theorem. For `D₁ = −4d`, `D₂ = −4m` (never coprime) Lauter–Viray's
   local factors for ℓ | gcd(D₁,D₂) (here ℓ = 2, and ℓ | gcd(d,m) if any) involve more than ε; so "PROVED modulo
   the cited shape" rests on a shape that is not the one in the literature for these discriminants. (MAJOR-1.)
2. Within Type I the ε-data are in fact *constant*: `(−d/p) = −1` and `(−d/ℓ) = +1` for all ℓ | e are forced
   (Prop 1.3 proof). So in the claimed shape the term depends only on n = pe, and the (5,23) pair has different
   n (313·23 vs 73·23). The argument therefore silently needs "the p-part of the term is a factor depending only
   on p" (true in GZ: the ramified prime with v_p = 1 contributes a trivial/log p factor). Should be stated.
3. **Concrete repair (my derivation; I recommend the author adopt it instead of the citation).** Fix Λ = Λ_{d,m}
   ⊂ B = B_{p,∞} (all embeddings Λ → B are B^×-conjugate by Skolem–Noether, applied to the generating pair). The
   x = 2 collision count, in the form `Σ_{[O]} #{Λ ↪ O}/|O^×/±1|` (free action: the centraliser of Λ is ℚ^×), equals
   `Σ_{O' ⊃ Λ} [N(O') : O'^×ℚ^×]·…`, i.e. `#{maximal O' ⊃ Λ}` up to a normalisation constant ≤ 2 independent of
   (d,m,p) (Atkin–Lehner at p / the curve↔type correspondence for E vs E^{(p)}; fix the convention), and `#{maximal O ⊃ Λ} = ∏_ℓ #{maximal O_ℓ ⊃ Λ_ℓ}` (local–global for lattices). At ℓ = p: 1 (unique maximal
   order). At ℓ ∥ e: Λ_ℓ has reduced disc ℓ, so has index ℓ in any maximal O_ℓ ⊃ Λ_ℓ, hence contains ℓO_ℓ and
   `Λ_ℓ/ℓO_ℓ` is a 3-dimensional unital subalgebra of M₂(𝔽_ℓ), i.e. a Borel: Λ_ℓ is Eichler of level ℓ, contained
   in exactly 2 maximal orders. So **for squarefree e the x = 2 count is `2^{ω(e)}` (times the fixed
   normalisation), independent of p and of m.** Since (5,23) has e = 23 prime, both p = 313 and p = 73 give the
   same count while ES differs: Prop 5.1's conclusion becomes PROVED for these pairs without any GZ citation
   (non-squarefree e needs the ℓ^k local count, also purely local; optimality conditions, if imposed, are local
   too). Caveat: whether the GZ/Lauter–Viray "x-term" is exactly this embedding count (vs optimal embeddings of
   O_{D₁}, O_{D₂}) should be stated explicitly; either way it is local data at primes of pe and 2.
4. "Type I forces x = 2" is relative to the orders ℤ[√−d], ℤ[√−m]; if the optimally embedded orders are larger
   (d or m ≡ 3 mod 4), the relevant (D₁, D₂, x) change. Minor wording (MINOR-3).
5. *Assessment* paragraph ("class-number size comes from ≍ √(dm) values of x") is fine as Assessment.

### §N — Novelty
I searched (Jina web search, 3 queries: "Erdős–Straus quaternion order supersingular", "Erdos Straus 4/n
Gross-Zagier singular moduli", "Erdős–Straus quaternion algebra Hilbert symbol 4abd−1"): no hit links ES to
quaternion orders, supersingular curves or Gross–Zagier; I know of no such source from memory. The underlying
identity `4abd − 1 = pe` is classical (Mordell/Yamamoto/ET), and its reading as `(D₁D₂ − x²)/4` is a one-line
observation, so novelty is at most "presentation". **UNVERIFIABLE** — the document makes no novelty claim, which
is correct; keep it that way.

### Labels / scope
* Report O130 item 3 calls Prop 2.2 a "Negative structural finding (PROVED)". The PROVED content is the trivial
  congruence statement; the negative *interpretation* is Assessment (the doc's §2.2 does label it so). Align the
  report (MINOR-2).
* §6 scope paragraph is correctly limited to "these dictionaries"; the last sentence ("cannot come from any
  quadratic map of the ES parameters (a,b) alone") is unproved — the isotropy of `X² − Y² = 4m` shows the
  *given* binary form is split, not that no other quadratic map exists. Label it Assessment or weaken. (MINOR-5.)
* Nothing is labelled CONDITIONAL that should be; no claim about ES itself. ✓

## Numbered defects

**MAJOR-1 (Prop 1.3 bold claim, §5 Prop 5.1, §6 first bullet).** Gross–Zagier "On singular moduli" is invoked for
`D₁ = −4d`, `D₂ = −4ab`, which violate its hypotheses (coprime fundamental discriminants). The "x = 2" name is
fine as notation, but Prop 5.1's "PROVED modulo the cited shape of the GZ local factor" relies on a shape that is
not established for these discriminants. *Repair:* (a) in Prop 1.3 say "x = 2 in the sense of the order generated
by ℤ[√−d], ℤ[√−ab] with relative trace 1 (the parameter of GZ/Lauter–Viray; GZ's theorem itself assumes coprime
fundamental discriminants)"; (b) replace the citation in Prop 5.1 by the local embedding-count argument of §5
item 3 above (Eichler-level-ℓ at ℓ ∥ e, 2^{ω(e)}), or cite Lauter–Viray precisely and check their x-term.

**MINOR-1 (Prop 1.3 proof, "At p"; Remark after 1.3; Prop 2.1(i); §4 first bullet).** `(−d,−dpe)_p = (−d/p)`
silently uses p ∤ e. *Repair:* add "p ∤ e, since p | e would give p | a+b and −d ≡ (2a)^{−2} (mod p),
contradicting (−d/p) = −1"; in the Remark/Prop 2.1(i) (general m) add the hypothesis "v_p(pe) odd". Numerically
p | e never occurs (p < 3000).

**MINOR-2 (Prop 2.2 Siegel-theta sentence; AGENT_REPORT_O130 item 3).** Heuristic under a PROVED heading.
*Repair:* move to the *Assessment* paragraph.

**MINOR-3 (§5 "Type I forces x = 2"; Prop 1.3 parenthesis).** Relative to the non-maximal orders ℤ[√−d],
ℤ[√−ab]. *Repair:* one clause noting dependence on the choice of orders.

**MINOR-4 (Prop 1.3 check line; scripts/quat_typeI.py).** "All 19690 Type I solutions" counts gcd(a,b,c)=1-
normalised triples (via `abcd()` with d = gcd); the tuples (a,b,c,d) satisfying the hypotheses of Prop 1.3 number
26007 for 3 ≤ p < 3000 (dilates included). Prop 1.3 holds for all of them (my check), so no harm. *Repair:* say
"triples (x,y,z)" and/or note ET Prop 2.2's normalisation.

**MINOR-5 (§6 last sentence).** Over-stated impossibility. *Repair:* label Assessment or restrict to "the
binary form in Prop 3.2 is isotropic".

**MINOR-6 (Prop 3.2 ideal reading).** State that every ℓ | e satisfies ℓ ∤ 2dp (automatic), so the local
description covers all of e.

No FATAL defects. All identities and all numerical claims I could test are correct.

## Repairs applied (round 1, at parent's request)
All repairs above were applied by the reviewer directly in QUATERNION_ES.md and in AGENT_REPORT_O130{,b}.md. Each is
marked "(R130 repair)":
* MINOR-1: p ∤ e in Prop 1.3 and the §4 symbol at p. Also: v_p(pe) odd in the Remark and in Prop 2.1(i).
* MAJOR-1: the GZ reading is qualified (x is notation only). Prop 5.1 is rewritten as the direct count
  `C(d,m) = #{maximal O ⊇ Λ} = ∏ N_ℓ`, which is `2^{ω(e)}` for squarefree e. The new derivation includes the Deuring
  weight `2/[N(O):ℚ^×O^×]` (1 or 2 curves per type).
* MINOR-2: the Siegel-theta sentence is now Assessment.
* MINOR-3: x = 2 is stated relative to the chosen orders.
* MINOR-4: the 19690 figure is explained as triples, versus 26007 tuples.
* MINOR-5: §6 last sentence weakened.
* MINOR-6: Prop 3.2 now states that ℓ ∤ 2dp holds automatically for every ℓ | e.
