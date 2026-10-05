# Hostile review R57 of POINTWISE_OMEGA15.md (task O57, branch side-agent/beyond-ceiling)

Reviewer: side-agent/review-omega15. Reviewed state: side-agent/beyond-ceiling @ 3b0f26f
(merged into the review branch; author's document not edited).
From-scratch scripts: `scripts/review_o15_*.py` (no reuse of `omega15_pseudorandom.py`).

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND (re-derived; brute-forced) |
| Thm 1.2 | SOUND (labels match O14 Thm 4.5 inputs) |
| Def 2.1 / Thm 2.2 | SOUND (Def 2.1 is narrow by design, see D-notes) |
| Lemma 2.3 | SOUND (minor bookkeeping) |
| Cor 2.4 | SOUND-AFTER-REPAIRS (M2 Q-reduction; M1 headline) |
| Prop 2.5 | SOUND |
| Thm 3.1 | SOUND-AFTER-REPAIRS (Gauss-sum bound misstated; conclusion survives) |
| Prop 4.1 | SOUND as a Haar statement; certificate clause covers an accounting nobody uses for integers (scope MAJOR) |
| Remark 4.2 / Assessment 4.3 | SOUND as labelled (heuristic); its conclusion is restated as fact in §6/Answer (M3) |
| Lemma 5.1 / Prop 5.2 | SOUND (Linnik–Xylouris used correctly; modest scope, honestly stated) |
| §0, §6, §7 scope and labels | GAP (headline omits the full-orbit qualifier; "Covered" list overclaims) |

## Per-claim notes

### Lemma 1.1 — SOUND
Re-derived line by line. Conditional on x_s and on the bit pattern, the X_b are independent, so
`E_{δ_{1_y}}∏h_b=∏_{b∈y}β_b∏_{b∉y}γ_b`; the alternating sum over `y⊆J` factorises to
`−∏_{J}(γ_b−β_b)∏_{I∖J}γ_b` (factors with `b∈J∖I` vanish since `h_b≡1`). Bounds checked:
`|γ_b|≤(1/4+p*)/(1−p*)≤3/7<1/2` (needs p*≤1/8, stated); `e_{k+1}(r)≥1` from the O14 chain
(`n e_n≥e_{n−1}(R−(n−1)r*)≥(k+1)e_{n−1}` uses only (1.0)); `C(m,k+1)2^{−(m−k−1)}≤2^{k+1}`.
Bits with `p_b=0` (β_b undefined) carry `w_J=0`, harmless. Result `(4r*)^{k+1}` is correct.

From scratch: `scripts/review_o15_lemma11.py` builds ν from its *definition* (O14 Lemma 1.1 law
on bits, X_b uniform on ℤ/m_b conditioned on the bit, Ω_b depending on a small coordinate s),
computes `E_ρh` by summing over all bit patterns and residues (not via the closed form), exact
rationals. Seeds 1–3, 2360 instances (k∈{0,1}, n≤26 bits, random and adversarial h_b with
`|E h_b|=1/4`, `β_b=±1`): ν is a probability law with exact k-wise marginals and `ν(0)=0`
(n≤11), `E_ρh=0` whenever `|I|≤k` (47 cases), `|E_ρh|≤(4r*)^{k+1}` always (worst ratio 0.081),
and `|ρ|≤P_0 2^{k+1}≤e^{−(1−p*)R}2^{k+1}` (ratio 1.000: the σ_J charges never cancel at the
bit level for k≤1 — the TV bound is attained, see Prop 2.5).
Caveat (not a defect): toys reach only k≤1; the identity is k-independent and was checked.

### Thm 1.2 — SOUND
Checked against O14 Thm 4.5's proof: it does give `R(x)≥μ*=c_9ε³𝓛³/log𝓛` for *every* small
configuration (unit x) with `p*≤T^{−0.09}`, ε absolute (fixed in O14 Lemma 4.3), so η is
uniform in Q (log Q≤T^{0.05}), r and B. `k+1=⌊μ*/2⌋` satisfies (1.0) for T large;
`E_νB≤E_νF=0` needs only `B≤F` P-a.e. (`dν/dP≤2`, O14 m1(b)). `8r*≤T^{−0.08}` and
`(k+1)≥μ*/2−1` give `η=exp(−c𝓛^4/log𝓛)` with `c≍c_9ε³`. Remark (i): the level-D part lies in
`𝒱_k` and `E_ρ=0` there by O14 Thm 1.3 directly (no reducedness needed) — correct. Remark (ii)
fine (F is periodic, so `‖F‖_×<∞`). No hidden parameter dependence found.

### Def 2.1 / Thm 2.2 — SOUND
`m_ν=N_xν` is nonnegative, has mass N_x, accuracy `N_x|E_ρh|≤N_x(4r*)^{k+1}` on every reduced
product, and `ν(F=1)=0`. Correct. Note (feeds D-notes below): Def 2.1 lets a certificate use
*only* nonnegativity, total mass and the accuracy bounds; it may not use that `m_x` is a sum of
unit point masses at integers `≤x` (atomicity/integrality/support). The fake `N_xν` is a
diffuse measure. This is a legitimate modelling choice but it is exactly where (N2) lives, and
it should be said at Def 2.1, not only in the Reading after Cor 2.4.

### Lemma 2.3 — SOUND
Re-derived. (a) trivial. (b) characters: `Σ_χ|Σ_{p∤q}χ(p)|²=φ(q)N'` (distinct units), principal
term `N'²`. Additive: `Σ_aS(a)\overline{c_q(a)}=Σ_pΣ_ac_q(a)e(ap/q)=q·N'` (Ramanujan-sum
orthogonality, `c_q` real), giving `q(N_x−2N_xN'/φ+N_x²/φ)≥qN_x(1−N_x/φ)` because `N'≤N_x`; the
`a=0` term vanishes. All correct. From scratch (`scripts/review_o15_lemma23.py`, part A): 78
cases (Q∈{1,3,4,5,7}, x≤150, q>x prime or a product of two primes, characters built explicitly from
primitive roots): (a), both lower bounds of (b) and the identity `Σ_χ|·|²=φ(q)N'` hold.
Bookkeeping: `S(a)` is written over all `p≤x, p∈H` but must run over the primes counted by `m_x`
(m3). In Cor 2.4 the hypothesis `N_x≤φ(q')/2` is asserted via "`q'>x²`", but the case split only
gives `q'>x` (m4).

### Cor 2.4 — SOUND-AFTER-REPAIRS; is "full-orbit uniform" honest?
*Proof.* Correct given Def 2.1: shallow terms have `E_ρ=0`, deep terms (≥k+1 big primes, modulus
`>T^{0.6(k+1)}>x`) cost `≥1/2` (classes) / `≥√(N_x/3)` (characters) each by Lemma 2.3, and
`E_HB≤η·Σ_deep|c_i|`. The Q-reduction sentence is false when `v_p(q)>v_p(Q)` for some `p|Q`
(on H the p-adic digits above `p^{v_p(Q)}` are free, so a class mod q is a class mod q′
*intersected with a sub-class at p*, and a character mod q is not "a character mod q′ times a
constant") — see M2; repairable.

*The class.* Not tailored to make the result trivially true: it is exactly the standard sieve
remainder accounting `Σ_q|λ_q|·max_a|r(q,a)|` (BV/GRH-type statements are uniform in a), and the
quantitative core is Thm 1.2, not the definition. But the definition does make the
"any accuracy, GRH included" clause **vacuous**: by Lemma 2.3, for moduli `q>x` *no* true
orbit-uniform bound beats the trivial `≈1` per class (`≈√N_x` per character), and GRH's
`x^{1/2}log²` is already trivial for `q>x^{1/2}`. So Cor 2.4 really says: *a minorant whose positive
mean lives on moduli `>x` cannot be paid for with trivial per-term remainders; and if all moduli are
`≤x`, O14 Thm 4.5 applies.* The strength of the prime input plays no role at all; the
headline should say so rather than present GRH-independence as a strength (M1).
Robustness check (positive, suggested addition): *one-sided* orbit-uniform accounting is also
covered. For a deep class with `c_C>0` a certificate may use `m(C)≥0` (orbit-uniform cost
`N_xP(C)≈0`); dropping those terms gives `B'≤B≤F` with only negative deep class terms, each of
which needs an upper bound and costs `≥1/2` (some class of the orbit contains a prime). Thm 1.2
applied to B' gives the same `N_xη>1/2`. Worth one sentence, since one-sidedness is the first
thing a sieve theorist would try.

### Prop 2.5 — SOUND
(i) `|ρ_{x_s}|≤P_0Σ_Jw_J‖σ_J‖=P_02^{k+1}`, `P_0≤e^{−Σp_b}≤e^{−(1−p*)R}`, and
`(1−p*)−(ln2)/2≥0.6` needs `p*≤0.053` (true, `p*≤T^{−0.09}`; implicit). My toy runs show
`|ρ|=P_02^{k+1}` exactly (no cancellation), so (i) cannot be improved via cancellation.
(ii)–(iii) and the exponent algebra `N_xη>(1/2)(e^{0.6μ*}/4)^{s−1}` re-derived; the `s=∞` case is
right. The model (Hölder with the *true* error vector) dominates any valid Hölder certificate.

### Thm 3.1 — SOUND-AFTER-REPAIRS
`ν_1=(1−εχ_1)ν≥0`, `ν_1≪ν`, `E_{ν_1}h−E_{P_1}h=E_ρh−εE_ρ[χ_1h]`; for an atom h, `χ_1h` is again a
reduced product up to a unimodular constant: at big b, class×χ_{1,b} has mean `≤1/(b−1)`,
character×character is a character (dropped if trivial), additive×nontrivial multiplicative
is a normalised Gauss sum. **The stated bound `|τ|/φ(b^v)≤√(b^v)/φ(b^v)` is false for imprimitive
data** (e.g. b=3, v=2, χ of conductor 3, a=3: value 0.866 > 0.5); my script
(`review_o15_lemma23.py`, part B, all b≤13, v≤3, all χ, a) finds 13256 violations. The correct
bound is: if `e(a·/b^v)` has conductor `b^g` and χ has conductor `b^f`, the sum vanishes unless
`f=g` (or f=0), and then `|·|/φ(b^v)=b^{1−g/2}/(b−1)≤√b/(b−1)` — verified tight in part B — which is
`≤1/4` for `b≥19`, true for big b. So the conclusion stands (m1). The exact statement
(`B∈𝒱_{k−s}` ⇒ `χ_1B∈𝒱_k` ⇒ `E_{P_1}B=E_{ν_1}B≤0`) is correct. Side remark: if `s≤k` then
`E_ρχ_1=0`, so the mass discrepancy `ν_1(H)−P_1(H)` is exactly 0 in the relevant regime.

### Prop 4.1 — Haar part SOUND; certificate clause of limited relevance
Re-derived: union bound `Σ'1/v≥(c_3−C_6σ(x))log V/log y`; planting off `G'={σ>λ}` with
`k+1=⌊μ*/4⌋` satisfies (1.0) since `R≥μ*/2`; Lemma 1.1 is pointwise in x_s, so `ρ=0` on G' is
harmless; Chernoff bound `P(Σξ_p/p≥λ/2)≤e^{3−λy/2}` with `t=y`, `e^{u}−1≤(e−1)u` for u≤1, and
`Σ_{p>y}y/p²≪1/log y` — correct; `y=𝓛^6` is O14 §4's choice, so μ* is unchanged. ξ_p independent
of probability 1/p for `p∤dQ` under P_d — correct.
Slip: with `X_d:=` the actual count, `|m^{(d)}(C)−X_dP_d(C)|≤1+P_d(C)<2`, not `≤1` (exact AP count
is within 1 of `(x/dQ)P_d(C)`, and `X_d` is within 1 of `x/(dQ)`); constants only (m2).
Relevance: the certificate clause requires charging error 1 to *every* deep class. For integers
the support of `m^{(d)}` is known exactly; nobody evaluates `Σ_{n≤x,d|n}F(n)` by charging 1 to
classes mod `q>x` whose least representative exceeds x. The author concedes this in the
statement, but §6 item 3, §7 and the Answer (1b) then list "integer Type I sums" as **Covered**
and "Type II input is then moot" — overclaim (M3).

### Remark 4.2 / Assessment 4.3
Remark 4.2 checked: by O13 Lemma 3.1 every event class has Jacobi symbol −1 mod M, so `m²` with
`(m,P(T))=1` avoids all events; the count `≫_Q√x/𝓛` for `√x≥T²Q` (m with all prime factors >T)
is right when r is a square mod Q. At `log x≍C𝓛³` this is `√x≪xδ_H`, so it does not contradict
Assessment 4.3's premise. Assessment 4.3 is correctly labelled heuristic, but (i) the requirement
"relative precision o(1) for (a weighted majority of) d≤x^{1/3}" is not how Vaughan Type I sums
are used (one needs `Σ_{d≤U}μ(d)·(error_d)` small, with sign cancellation; the author does list
this as not excluded); (ii) the sentence "the bottleneck is the sieve dimension … prime-specific
input addresses the other half" is then promoted in the Answer to "The 1/4 ceiling is a
sieve-dimension barrier … invariant under any strengthening of prime equidistribution" without
the heuristic/full-orbit qualifiers (M1, M3). The Maynard comparison is fine as a reading
(additive characters are reduced products, so the additive-Fourier ℓ¹ norm dominates `‖F‖_×`);
the exponent `c_b<1/2` is flagged as from memory — acceptable.

### Lemma 5.1 / Prop 5.2 — SOUND
Lemma 5.1: Dirichlet on each unit class mod `lcm(L,Q)` — correct. Prop 5.2: the class
`{n∈c, n≡−4 (ℓ_0)}` is a unit class of modulus `≤qQℓ_0`; Linnik with Xylouris's exponent L=5
(Xylouris 2011 thesis; 5.18 in Acta Arith. 2011 — I could not access either here; the exponent 5
is the standard citation) gives a prime `≤C_L(qQℓ_0)^5`, effective (Linnik's theorem does not use
Siegel); GRH gives `≪(φ(m)log m)²` (Bach–Sorenson / Lamzouri–Li–Soundararajan), i.e. `m^{2+ε}` —
as stated. The atom `(ℓ_0,1)` (`ℓ_0≡3 (4)`, `1|A²`) holds at `n≡−4 (ℓ_0)`, so `F(p)=0` and
`B(c)≤0` on every *unit* class (non-unit classes are Haar-null; "every class" should read "every
unit class", m5). The §7 table drops `C_L^{1/5}` and the existence of `ℓ_0` (trivial since
`qQ<∏_{ℓ≤T,ℓ≡3(4)}ℓ` in range). Note the result is stronger than advertised in one way (B≤0
pointwise, B≤F not used beyond the ℓ_0-event) and weak in another (a single modulus); honest.

### §0, §6, §7, Answer — GAP (presentation/scope)
See M1, M3, m6. Missing from (N1)–(N4): certificates using *atomicity/integrality* of the prime
measure (`m` is a sum of unit masses at integers `≤x`), which Def 2.1 forbids and which is
broader than "support-aware" — e.g. `m(C)∈ℤ_{≥0}` for every class; this should be named in (N2).

## Defects

No FATAL defect. The mathematics (Lemma 1.1, Thm 1.2, Thm 2.2, Lemma 2.3, Prop 2.5, Thm 3.1,
Prop 4.1's Haar bound, Prop 5.2) checks out. The problems are one routine proof gap and scope /
rhetoric.

**M1 (MAJOR, scope/rhetoric) — the "GRH included" clause is vacuous and the §0 headline drops
the qualifier.** Locations: §0 ("This disposes of GRH-strength transfers, Siegel-zero main
terms, and Fourier (minor-arc) transfers … as long as they act linearly on a minorant"), Cor 2.4
(boldface "whatever true statement about the primes is used (GRH included)"), §6 Covered 1,
Answer ("invariant under any strengthening of prime equidistribution"), report/ledger (H)28.
For deep moduli `q>x`, Lemma 2.3 shows that *no* orbit-uniform statement about the primes beats
the trivial one, and GRH is trivial there anyway. So within the class the strength of the prime
input cannot matter, by construction. That is not evidence that the barrier is "a property of F
invariant under prime input". *Repair:* (a) put "full-orbit uniform" (and "linear, Def 2.1") into
§0 and into every restatement; (b) rephrase Cor 2.4's moral as: "positivity must come from
moduli `>x`, where no orbit-uniform information beats the trivial bound (Lemma 2.3); Thm 1.2 shows
trivial bounds cannot pay for it". Drop "GRH included" or explain that it is vacuous. (c) In the
Answer, qualify "invariant under any strengthening…" with "for full-orbit uniform linear
transfers".

**M2 (MAJOR, proof gap; routine repair) — the Q-reduction in Cor 2.4 / Prop 2.5 is false when
`v_p(q)>v_p(Q)` for some `p|Q`.** Location: Cor 2.4 proof ("on H a class mod q is a class mod q′ or
empty, and a character/additive character mod q restricts to one mod q′ times a constant"); Prop
2.5 ("coprime to Q after the reduction"). On H only `X_p mod p^{v_p(Q)}` is fixed; higher p-adic
digits are free. So `1_C|_H` is (class mod q′)×(sub-class mod `p^{v_p(q)}`), not a class mod q′.
Similarly χ mod q restricted to H is not χ′·const. *Repair:* prove Lemma 2.3 relative to H. The
image of H mod q is a coset `K` of a subgroup of `(ℤ/q)^×`, with `|K|=φ(q)/φ(gcd(q,Q^∞))·…`. The
primes `≤x<q` are distinct elements of K. Run (a) with `N_x≤|K|/2`, and (b) with the characters of
`(ℤ/q)^×` restricted to K. The mean square over the `|K|` restricted characters is
`|K|N'`, and the same algebra gives `≥N_x(1−N_x/|K|)`. Alternatively restrict Cor 2.4 to moduli
with `v_p(q)≤v_p(Q)` for all `p|Q`.

**M3 (MAJOR, overclaim) — "integer Type I sums" are listed as Covered and Type II as "moot".**
Locations: §6 Covered item 3 ("Type II input is then moot (Cor 4.3, Assessment …)"); §7 row
Prop 4.1 ("class-ℓ¹ certificates blocked", without the uniform-error qualifier); Answer (1b)
("Type II cannot help on its own: the Type I half already needs …", stated as fact); report
bullet "Prop 4.1 (integers)". Prop 4.1's certificate clause only covers accounting that charges
error 1 to every deep class. For integers that accounting is unnatural: supports are known
exactly, and the author's own (N2) calls support-aware accounting "the natural accounting" here.
"Moot"/"cannot help" rests on Assessment 4.3, which is heuristic. *Repair:* in §6 move item 3
under "Covered only under full-orbit-uniform accounting (not the natural one for integers)", and
delete "Type II input is then moot". Label Answer (1b) "Assessment". Fix the dangling "Cor 4.3"
reference (renamed to Assessment 4.3 per the report). Add the qualifier to the §7 row and the
report.

**m1 (MINOR) Gauss-sum bound in Thm 3.1's proof.** "`≤√b^v/φ(b^v)≤1/4`" is false for
imprimitive data (13256 counterexamples, b≤13, v≤3; `review_o15_lemma23.py` B). *Repair:* the
sum vanishes unless the conductors agree (`f=g`). Then `|·|/φ(b^v)=b^{1−g/2}/(b−1)≤√b/(b−1)≤1/4`
for `b≥19`. Tight; verified.

**m2 (MINOR) Prop 4.1 proof, "Certificates".** `|m^{(d)}(C)−X_dP_d(C)|≤1` should be `<2` when
`X_d` is the actual count (or use `x/(dQ)` as the mass). Constants only.

**m3 (MINOR) Lemma 2.3 proof.** `S(a)` must sum over the primes counted by `m_x` (coprime to 𝒬),
not all `p≤x, p∈H`; otherwise `S(0)≠N_x`.

**m4 (MINOR) Cor 2.4 proof.** It says "`>x²`", but the case split `log x<c′𝓛^4/log𝓛` only gives
`q′>x`. Lemma 2.3 also needs `N_x≤φ(q′)/2`. *Repair:* split at `log x<(c′/2)𝓛^4/log𝓛`; then
`q′>x²`, and `φ(q′)≫q′/loglog q′≥2x` (or use `|K|` from M2).

**m5 (MINOR) Prop 5.2.** "B≤0 on every class of H mod q" should read "every unit class" (the
others are Haar-null and contain ≤1 prime). The §7 row "q≤x^{1/5}/(QT)" drops `C_L^{−1/5}` and the
existence of `ℓ_0` (state it: automatic in range).

**m6 (MINOR) Consistency.** §0 states `(8r*)^{k+1}`, Lemma 1.1 proves `(4r*)^{k+1}`, and the
"slack for §3" is unnecessary (Thm 3.1 uses `2(4r*)^{k+1}`). Harmonise. The document's internal
self-review is called "R57", which collides with this review's tag. Rename it (e.g. "R57-self").

**m7 (MINOR) Def 2.1.** State at the definition that certificates may not use atomicity,
integrality (`m(C)∈ℤ`) or support of the prime measure (the fake `N_xν` is diffuse). List these
explicitly in (N2), which currently names only "support-aware".

**m8 (MINOR) Prop 2.5(i)** implicitly needs `p*≤0.053` (`(1−p*)−(ln 2)/2≥0.6`). Say so (true:
`p*≤T^{−0.09}`).

**s1 (suggestion, strengthens the paper).** Add the one-sided remark: certificates that use
`m(C)≥0` for positive-coefficient deep classes are still blocked (drop those terms, apply Thm 1.2
to the remaining minorant). See Cor 2.4 notes.
**s2 (suggestion).** Thm 3.1: if `s≤k`, then `E_ρχ_1=0`, so `ν_1(H)=P_1(H)` exactly; the mass
caveat is then unnecessary.

## Overall
The core new result, Lemma 1.1 ⇒ Thm 1.2 (Wiener-norm barrier `E_HB≤η‖B‖_×`), is correct, uniform
in the stated parameters, and brute-force confirmed. It is a genuine strengthening of O14 Thm
4.5. "Full-orbit uniform accuracy" is an honest, natural class: it is standard sieve-remainder
accounting. It is not tailored to make Cor 2.4 trivial. But it makes the prime-input-independence
("GRH included") automatic, and the presentation should say this instead of advertising it
(M1). The integer/Type II conclusions are scoped correctly in the body but overclaimed in §6,
§7 and the Answer (M3). M2 is a routine fix. Recommended label changes: none for the PROVED
items once M2 is repaired; §6 item 3 and Answer (1b) → qualified/Assessment.
