# R188 — hostile review of O188 STERILE_STEER.md (+ BRAINSTORM/bsM_*.md)

Reviewer: side agent R188 (branch side-agent/review-sterile-steer). Reviewed: STERILE_STEER.md as merged from
side-agent/sterile-steer (checkpoint 1), memos bsM_*.md, AGENT_REPORT_O188.md. From-scratch scripts:
`scripts/review_ss_*.py` (none of the author's code is reused; `mordell_lib` is used only as an *a posteriori*
cross-check of my own class tables).
Sources checked: Elsholtz–Tao arXiv:1107.1010 (sources/elsholtz-tao-1107.1010.pdf, text read directly).

**ES is not solved; nothing in O188 claims otherwise, and nothing in this review changes that.**

## Summary verdicts

| Claim | Verdict |
|---|---|
| §1 Lemma 1.1 (escape) | SOUND (minor wording, D6) |
| §2 EVIDENCE (r = 17, u = 5, 180 cases) | (in progress) |
| Prop 3.1 (S closed; ES(p) ⟺ p ∉ S; SQ ⟺ S ∩ ℕ_odd = odd squares) | SOUND-AFTER-REPAIRS (wrong citation, D1; Type I/II vs N-point wording, D2) |
| Prop 3.2 (divergent side, second Borel–Cantelli) | SOUND (BC II not even needed, D4) |
| Cor 3.3 (density 1/4) | SOUND; the "Reading" overstates what it says about integers (D3) |
| §4 Lemma 4.1 | SOUND for odd r; false for r = 2 (D5) |
| §4 Lemma 4.2 | (in progress) |
| §5 Prop 5.1 | (in progress) |
| §6 r₀ table (Assessment) | (in progress) |

## Claim-by-claim

### Prop 3.1

Re-derived from ET's text. (i) *Class ⇒ N-point at every n ≥ 1.* I re-checked the seven ET §10 tuples
(ET p. 37–38) for positivity at every n ≥ 1 in the class, not just n large: I1 c = (n+f)/4ad ≥ 1 and
b = ce − a > 0 because ce = (n+f)(4a²d+1)/(4adf) > a; I2, I3, II3 all coordinates are quotients of positive
integers; I4 f = na/b + (a+b)/(be) > 0; II1 f = 4acd − 1 ≥ 3; II2 ce = (f+1)(n+4a²d)/(4adf) > a. So every n ≥ 1 in
a class has an N-point of Σ^I_n or Σ^II_n, i.e. an element of V_I(n) ∪ V_II(n), and hence an ES solution via π^I / π^II.
Numerically confirmed by `scripts/review_ss_classes.py` (below). (ii) *N-point ⇒ class.* V_I: 4abd = ne+1,
a+b = ce gives e(4acd − n) = 4a²d + 1, so f := 4acd − n ≥ 1, f | 4a²d+1, n ≡ −f (mod 4ad): I1 class (a, d, f).
V_II: 4abd = n+e gives e(4acd − 1) = n + 4a²d, so with f := 4acd − 1, 4ad | f+1 and n ≡ −4a²d (mod f): II2 class.
Both hold with **no coprimality hypothesis**, which is what (b) needs for composite n. (iii) For an odd prime p
every solution of 4/p has p dividing one or two denominators (none: p | 4xyz impossible; three: RHS ≤ 3/p), and
ET Props 2.2 / 2.6 put Type I / II solutions on Σ^I_p / Σ^II_p. p = 2 lies in II2(1,1,3) = {n ≡ 2 (3)}.
(iv) S is the complement of a union of clopen sets, hence closed. (v) SQ as recorded in DISCOVERIES (J)-list is
literally "V_I(n) ∪ V_II(n) = ∅ ⟺ n square, n odd", so by (i)–(ii) it is S ∩ ℕ_odd = odd squares. SOUND, with D1, D2.

### Prop 3.2

ν_T makes the x_q (q ∈ T) independent, each uniform on the non-squares of ℤ_q^×; reduction mod q maps this
uniformly onto the (q−1)/2 non-residues, so P(x_q ≡ −4 mod q) = 2/(q − 1) when q ≡ 3 (4) (−4 is then a non-residue)
and 0 when q ≡ 1 (4). II2(1,1,q) needs 4·1·1 | q+1, residue −4 mod q: correct (checked against ET's family
"−4a²d mod f, 4ad | f+1"). The off-T coordinates (x = 1) play no role because the modulus of II2(1,1,q) is q.
Σ 2/(q−1) = ∞ along T ∩ {q ≡ 3 (4)} gives P(no event) = ∏(1 − 2/(q−1)) = 0. SOUND (D4: only *one* event is needed).
Measure: ν_T is a product of probability measures, well defined for infinite T. No hidden uniformity issue.

### Cor 3.3

For n > 0 not a square, the Kronecker character χ_D of ℚ(√n) is non-trivial and ≠ χ_{−4} (ℚ(√n) is real), so
χ_{−4} and χ_D are independent quadratic characters and {q : q ≡ 3 (4), (n/q) = −1} has Dirichlet density 1/4
(no Chebotarev needed beyond Dirichlet for the biquadratic field). Primes q | n are excluded because n_q is not a
unit. SOUND. But see D3 on the "Reading".

### §1 Lemma 1.1

x(p) ∈ C ⟺ (p ≡ ρ mod M_r and 1 ≡ ρ mod M'); with p ≡ ρ (mod M) this is M' | p − 1. (b): if v_r(M) ≤ L and
M' | p − 1 then x(u)_r = u ≡ p ≡ ρ (mod M_r) and x(u)_q = 1 ≡ p ≡ ρ (mod q^v), so x(u) ∈ C, a box of level v_r(M) ≤ L.
"E = 1 impossible": E = 1 means M | p − 1, so 1 ∈ C; but 4/1 = 1/x+1/y+1/z has no solution (RHS ≤ 3) while
every n ≥ 1 in a class has one (Prop 3.1(i)). SOUND. D6 is wording only.

### §4 Lemma 4.1

Limit set: for μ ∈ Ẑ, m_i → ∞ with m_i → μ in Ẑ gives 2-component k·2^{m_i} + c → c and q-components → k·2^μ + c
(m ↦ 2^m mod q^j is periodic, so extends continuously to Ẑ). For **odd** r the proof is right. For r = 2 the
r-generic line imposes nothing at 2, and c = −1, k = 2^j gives ν(1 − j) = (−1 at 2, 1 at every odd q), a point of the
2-generic line (e.g. Mersenne numbers 2^m − 1, μ = 1). See D5.

## Defects

**D1 (MINOR; Prop 3.1 header and proof, "relative to ET Props 1.3/1.4 and §10").** ET has no Prop 1.3, and Prop 1.4
is the average of τ(kab²+1). The parametrisation results are ET **Props 2.2 and 2.6** (with the equivalent
characterisations Props 2.3, 2.7). *Repair:* cite ET Props 2.2/2.6 (for (a)) and §10 (for (i)); state that (b)
uses only the bare identities above, no ET proposition.

**D2 (MINOR; Prop 3.1(b) "an ET N-point (a Type I or Type II parametrised solution)").** In ET, "Type I/II
solution" carries coprimality conditions (abcd or abd prime to n), and for composite n an N-point of Σ_n need not
give a Type I/II solution. The statement is true for V_I(n) ∪ V_II(n) (N-points, no coprimality), which is also how
SQ is defined. *Repair:* replace the parenthesis by "(an element of V_I(n) ∪ V_II(n), no coprimality conditions;
for composite n this is weaker than an ET Type I/II solution)". Also add the missing case "p divides no
denominator" to the proof of (a) and treat p = 2.

**D3 (MAJOR as framing; §3 "Reading (Assessment)" and AGENT_REPORT SHARP 1, "Every non-square integer sits in the
divergent regime … ES lives exactly on the divergent side … at a ν-null point").** An integer n is not merely
ν-null in G_{T(n)}: it is **not in G_T for any T** (its components off T(n) are n_q ≠ 1, or non-units). The
dichotomy is a statement about the slices G_T ("1 off T"); n lives on a different slice (n_q a non-trivial square
off T). Prop 3.2 does extend to the slice "x_q prescribed squares off T" (its proof only uses coordinates in T), but
the convergent side (O178) does **not**: O178 is specific to x_q = 1 off r, and on a slice with other square
coordinates the box dictionary changes (a class meets the slice iff ρ ≡ x_q at the other primes, not ρ ≡ 1).
So "ES lives on the divergent side of a Borel–Cantelli dichotomy" compares objects on different slices.
*Repair:* say "the non-square pattern of an integer is divergent; the dichotomy itself is proved only on the
slices G_T, which contain no integer", and drop "exactly".

**D4 (MINOR; Prop 3.2 proof).** "Second Borel–Cantelli: a.s. infinitely many occur" is true but more than needed;
one occurrence suffices, and P(none) = ∏(1 − 2/(q−1)) = 0 is the whole proof. *Repair:* optional.

**D5 (MINOR; §4 Lemma 4.1 "for any r").** False for r = 2 (counterexample above). *Repair:* "for every odd prime r".

**D6 (MINOR; §1 Lemma 1.1(a)).** "The ET classes of p with M' | p − 1 are exactly the boxes on the r-generic line
containing u = p" is ambiguous: a box containing u = p can come from a class with ρ ≡ 1 (M'), ρ ≡ p (M_r) but
p ≢ 1 (M'), which does not contain p. Correct reading: "C ↦ C ∩ line is a bijection from the classes of p with
M' | p − 1 onto the boxes containing u = p whose class has M' | p − 1". *Repair:* reword as above, or simply
state (a) as "x(p) ∈ C".
