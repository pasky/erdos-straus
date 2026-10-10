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
Closure: `vu = 1 − uv`, `u·uv = −dv`, `uv·v = −mu`, `v·uv = v − (vu)v`… all in the ℤ-span; fine.

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
