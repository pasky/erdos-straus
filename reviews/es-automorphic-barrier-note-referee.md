# Referee report R134 — paper/es-automorphic-barrier-note.tex

Referee: R134 (hostile, independent). Branch `side-agent/referee-automorphic-note`, merged from
`side-agent/automorphic-note`. ES is not proved anywhere; the paper says so (abstract, §1, §8).

## Recommendation

**ACCEPT (internal) after the R134 repairs, which are applied** (commit "R134 repairs D1-D10"). No FATAL defect.
One MAJOR defect (D9: an overclaimed universal sentence in the abstract and in Thm 3.2(ii)) and ten MINOR ones,
all local. Every key statement matches its source after the earlier review repairs: scale constraint (merged form,
ET Prop 1.7 verified in the PDF), ternary theorem (fixed Q, κ, η, fixed-complexity recipes; thin-piece caution),
thickening, odd-square wording ("locally soluble and globally soluble up to one sign"), BM-only ⟺ ES(n) for n ≥ 2
(with a correct n = 1 remark against BL Thm 1.8 as printed), Thm 3.2(iii) CONDITIONAL on H, GZ formal analogy only,
Brauer = genus folklore/Yamamoto. All short proofs re-derived; dictionaries and the full slice table re-checked by
from-scratch code (`scripts/review_r134_slices.py`, `review_r134_dict.py`, `review_r134_counts.py`). The
abstract, intro and summary state that ES is not proved.

R134 repairs applied to the paper (marked here only, not in the PDF): D1, D2, D3, D4, D5, D6 (incl. Planck-scale
sentence after Prop 2.4), D7, D8, D9 (abstract + Thm 3.2(ii)), D10. Recompiled: 3 passes from clean, 0 errors,
0 LaTeX warnings, 0 overfull boxes, 18 pp.

## Per-claim verdicts

### §2 Dictionaries
* Lemma 2.2 (three shapes): **SOUND-AFTER-REPAIRS** (D1: quantifier of d resp. a in (ii)/(iii)). Proof re-derived line by
  line; identities checked by `scripts/review_r134_slices.py` (all tuples, p<400).
* Prop 2.3 (T_p Hecke form): **SOUND** (coefficients and root relation re-derived; numerically checked).
* Prop 2.4 (wedge, width): **SOUND** (x/y = 2a√d, √d/y = f; edges are rays from 1/(2c), i.e. hypercycles of
  Re z = 1/(2c); width = arsinh difference, derivative ≈ 2/√(p²+4c²d) re-derived).
* Lemma 2.5 (genus): **SOUND** (gcd(f,2cd)=1 follows from gcd(n,2cd)=1 and f ≡ −n mod 4cd; Kronecker period 4d).
* Prop 2.6 (Type II): (a),(c),(d) **SOUND** (re-derived; lattice 4·[−dp,1,c²] checked). (d) uses gcd(dp,f)=1
  without comment (MINOR D2). (b) is a pointer to O128/TH (not re-derived here beyond a numerical check).
* Prop 2.7 (Brauer = genus): **SOUND** as a folklore attribution; proof (b) reciprocity step re-derived.
* Prop 2.8 (B_{p,∞}): **SOUND** (Gram det −(4dm−1)² and ramification {p,∞} checked on 2632 Type I tuples p<300 by `scripts/review_r134_dict.py`; w = 2dv+u anticommutes, w² = −d(4dm−1); Hilbert symbols at p, ℓ|e, ℓ|d, ∞
  re-derived). GZ correctly labelled formal analogy.
* Lemma 2.9, Prop 2.10, Prop 2.11: **SOUND** (re-derived).

## Defects

D1 (MINOR, Lemma 2.2, statement (ii),(iii)). As stated "Let a,c,d,f ≥ 1 ... equivalent: (ii) f | ap+c and
4ac | p+f; (iii) ... f ≡ −p (mod 4cd)". For fixed d (resp. a), (ii) (resp. (iii)) does not imply (i): (ii) does not
pin d and (iii) does not pin a. The proof silently uses 4acd = p+f. The source POINTWISE_SPECTRAL Lemma 2.1 has the
parentheticals "(then d = (p+f)/(4ac))", "(then a = (p+f)/(4cd))". Repair: write (ii) as "f | ap+c and
p+f = 4acd", (iii) as "f | p²+4c²d and p+f = 4acd". (R134 repair applied.)

D2 (MINOR, Prop 2.6(d) proof). "gcd(dp,f)=1" is asserted. Repair: add "(f = 4acd−1 is prime to d, and p | f
would force p | 2ad, whence f ≡ −1 (mod p))". (R134 repair applied.)

### §3 Divisor-class reduction
* Lemma 3.1 (slice table): **SOUND**. All D-row identities and converses re-derived by hand (I{c,d}: f' ≡ p²(−p)^{-1};
  II{a,c}: c(4a²d+p) = a(f+1)+cp; {a,e},{d,e}: gcd(a,e)=1 argument; C rows). Independently brute-force-checked
  by `scripts/review_r134_slices.py` (own code, not rt2_slices.py). Note: in II{a,d} positivity of b is automatic
  (ce − a = (fp+p+4a²d)/(4adf) > 0), so the side condition "(f+1)e/(4ad) > a" in Prop 2.11(i) is redundant (D3).
* Thm 3.2: (i) **SOUND**; (ii) **SOUND** as a collection of cited internal statements (not re-derived);
  (iii) **SOUND** (CONDITIONAL on H): I checked POINTWISE_SIZE §1.2 — DIVISORS(r) and `for e in L` are primitive
  bounded instructions (P5),(P7), so "factor N_θ(p), test each divisor" is a bounded program and Cor. C1 applies.
  Suggest saying so in the proof (D4).

### §4 Negative results (part 1)
* Thm 4.2 (ternary): sketch is faithful to O124 Thm 4.1/Cor 4.2 as summarised; scope sentences ("does not cover recipes
  of unbounded algebraic complexity, or families with a parameter that grows with p"; thin-piece caution example) are
  present. **SOUND** as a sketch-with-pointer (not re-derived beyond the Markov/first-moment step).
* Prop 4.4 (scale constraint, merged form): **SOUND**. Checked against sources/elsholtz-tao-1107.1010.pdf:
  ET Prop 1.7 indeed states f(p) ≪ p^{3/5+O(1/log log p)} for prime p (paper writes "≤"; harmless since the implied
  constant is absorbed in the O(1/log log p) exponent); ET Thm 1.1 gives Σ_{p≤N} f_I(p) ≪ N log²N log log N and
  Σ f_II(p) ≪ N log² N. Markov dyadically: (b) X^{1−δ}log²X loglogX ≤ N^{1−δ}log³N ✓; (c) X/(ξ log X) = o(π(X)) ✓.
* Prop 4.5 (local data): **SOUND-AFTER-REPAIRS** (D5: undefined c, t, m, m''). Counting of odd m ≡ m₀ (2Q) in
  (√X, √2X] re-derived (≍ X^{1/2}/Q ≥ X^ε).
* Prop 4.6 (thickening): **SOUND-AFTER-REPAIRS** (D6: the window f ≤ 2p and the width (2K+1)/p are imported from
  O123 Formulation A without being defined here, and the width is inconsistent with Prop 2.4's 2/√(p²+4c²d)).
* Prop 4.7 (odd squares): **SOUND**. q(Q₀) = −4dn, b(Q₀,S_c) = 4(cB−A) = 4, real point re-derived. Wording is the
  repaired "locally soluble and globally soluble up to one sign"; no "genus/spinor solubility" claim. Also checked
  that A > 0 forces a ≥ 1, e ≥ 1, b ≥ 1, so the A>0 problem is exactly Type II, and that gcd(dn,f)=1 holds for every
  n (so Prop 2.6(d)'s argument covers odd squares, consistent with ET Prop 1.6, verified in the PDF).
* Thm 4.8 (fibres): **SOUND**. BL Lemma 3.10 checked in sources/bright-loughran-1908.02526.pdf (finiteness of
  integral points off u₁u₂u₃=0 and u_i=−u_j). Lines M_k verified: u_k=n/4, u_j=−u_i lies on U_n.
* BL citations in §2.7: Cor 2.7 (Br Ũ_n/Br Q ≅ Z/2 generated by α) ✓; Lemma 2.1 (V_n ≅ G_m²) ✓; Thms 1.1, 1.8 ✓;
  Thm 1.2, Cor 1.4 ✓; Lemmas 3.1, 3.5, 3.8 (inv_∞ = −1 on positive part, inv_ℓ = 1 for ℓ∤2n, inv_2 = 1 for n odd) ✓;
  inv_p = (−ab/p) re-derived from (−u₁/u₃,−u₂/u₃)_p with u = (abdp, acd, bcd). One mis-citation (D7: Thm 1.9).

### §4 Negative results (part 2)
* Prop 4.9 (BM-only ⟺ ES(n), n ≥ 2): **SOUND**. For n ≥ 2 the positive Brauer set is non-empty (BL Thm 1.8 (1.4),
  verified), so the equivalence is immediate. The n = 1 remark is correct and worth keeping: with inv_∞ = −1 on
  U_1(R)⁺ (BL Lemma 3.1), inv_ℓ = 1 for odd ℓ (Lemma 3.5, ℓ ∤ 2n) and inv_2 = 1 (Lemma 3.8, n odd), the Brauer set is
  empty, so BL Thm 1.8 (1.4) as printed ("for all n ∈ N") fails at n = 1; Thm 1.1 assumes n ≥ 2. Consistent with BL
  Thm 1.2 (empty product = 1 ≠ −1).
* X_d paragraph: **SOUND** (f + p = 4acd is a congruence modulo a coordinate; finiteness/infinitude cited to O126).
* Prop 4.10 (H, target (1,3)): **SOUND**. Re-derived: x(x²+12) on x ≡ 5 (12) has no fixed prime divisor (q = 2, 3
  checked at x = 5; q ≥ 5 by degree); χ_{−12}(7) = 1 (genus-allowed); p²+12 ≡ 1 (mod 12), so neither divisor 1 nor
  p²+12 is ≡ 7. (The restriction "f ≤ p" in the proof is unexplained but irrelevant: D8.)
* Prop 4.11 (Dickson, Type II shell): **SOUND** (X(4c²dX+1) has no fixed prime divisor; 4c²dp+1 ≡ 1 mod 4cd).

### §5 Gaps (Assessment)
* Young: checked against arXiv:1405.5457. Thm 2.1 error ‖φ‖₂ D^{5/12+ε} V^{1+ε} ✓ (D^{1/4} under Lindelöf for
  L(u_j×χ_{−D}) and L(χ_{−D}), Young's remark after (2.4)). Re-derived: ball (‖φ‖₁≍V^{−2}, ‖φ‖₂≍V^{−1}) gives
  V ≪ D^{1/24} (D^{1/8} under Lindelöf) ✓; strip (‖φ‖₁≍V^{−1}, ‖φ‖₂≍V^{−1/2}) gives V ≪ D^{1/18} (D^{1/6}) ✓,
  hence the gaps D^{4/9}, D^{1/3} ✓. Prop 1.2(1): 4/9 < η ≤ 1/2, b ≍ D^η, ineffective, odd fundamental D ✓
  (a ≍ √D is from the proof, y ∈ [1,2]; fine).
* Bibliography: Young JEMS 19(5) (2017) 1545–1576 ✓; Humphries Math. Ann. 371(3–4) (2018) 1497–1543 ✓ (verified
  via UCL discovery / Springer DOI 10.1007/s00208-018-1677-9); HR CPAM 75(9) (2022) 1936–1996 ✓; GS Invent. 229(2)
  (2022) 689–749 ✓; ET, BL ✓ (PDFs in sources/). Not verified by me: Sardari, BKS (not cited in this paper at
  all — see D9), Pila, Schinzel 2000, Duke 1988, DSP 1990, Lenstra 1984, DFI 1995, FI98, HB 2001, Maynard 2020, ST
  2009, GZ 1985, Hooley 1963 (all standard and look right from memory, but unchecked).
* Assessment 5.1: correctly labelled; n_p ≪ 𝓛² under GRH (Ankeny/Bach) and Burgess p^{1/(4√e)+ε} are classical ✓;
  the "(−d/p) = −1 ⇒ n_p ≤ D(p)" step for p ≡ 1 (4) re-derived ✓.

### §6–§8, honesty, compile
* §6 Problems/Remarks: correctly labelled Assessment/open. Lenstra (≤ 11 divisors in a class once q > N^{1/3},
  gcd(r,q)=1) correctly stated. GS Thm 1.2 (infinitely many Hasse failures, almost-all Hasse) checked in
  arXiv:1706.06712 ✓. Notation T_2^+ undefined (D10).
* §7 EVIDENCE: two counts recomputed from scratch (`scripts/review_r134_counts.py`): 3630 primes p ≡ 5 (12) in
  [10⁶,3·10⁶) with p²+12 prime ✓; 14183 primes p ≡ 1 (24) below 1.5·10⁶ ✓. The other numbers (f_I, f_II ≥ 1 to
  10⁸, minima) were not recomputed (too costly for this pass); they are labelled EVIDENCE and attributed.
* Honesty: abstract, §1 ("What this note does not contain") and §8 all say ES is not proved; negative statements are
  scoped ("routes examined and known technology", "mechanism scope", Assessment 5.1 "by the routes of this note").
  Novelty: Brauer = genus marked folklore/Yamamoto; quaternion dictionary "novelty unverified"; GZ "formal analogy
  only"; no novelty overclaim found. One overclaimed *theorem* sentence (D9).
* Sardari and BKS are not cited in the paper (nothing to check; LITERATURE_AUTOMORPHIC discusses Sardari but the
  paper does not rely on it).
* Compile: from a clean checkout (no .aux/.toc) two passes leave "Label(s) may have changed"; a third pass is clean
  (0 errors, 0 LaTeX warnings, 0 overfull). 18 pp. (D11, cosmetic.)

## Defects (continued)

D3 (MINOR, Prop 2.11(i)). The side condition "(f+1)e/(4ad) > a" is automatic: with c = (f+1)/(4ad),
ce − a = (fp + p + 4a²d)/(4adf) > 0. Repair: say "(the cofactor condition is automatic)". (R134 repair applied.)

D4 (MINOR, Thm 3.2(iii) proof). The procedure enumerates all divisors of N_θ(p), a p-dependent number; one must
check this is "bounded" in the sense of [PS]. It is: DIVISORS(r) and `for e in L` are primitive bounded
instructions (P5),(P7) of POINTWISE_SIZE §1.2. Repair: add this sentence. (R134 repair applied.)

D5 (MINOR, Prop 4.5 statement). t, m, m'' and c are undefined; c is (m''+1)/t (CONDITIONAL_ES Lemma 1.1).
Repair: "(t ≥ 1, tn+1 = mm'', m ≡ m'' ≡ −1 (mod t), 4 | m, and c = (m''+1)/t)". (R134 repair applied.)

D6 (MINOR, Prop 4.6). The sum carries a window "f ≤ 2p" and the width "≈ (2K+1)/p", both from O123
Formulation A (size window f ∈ [1,2p], width 2/p + O(c√d/p²) for c√d ≪ p), neither defined in this paper; Prop 2.4
states the width as ≈ 2/√(p²+4c²d), which is ≍ 1/p only when c√d ≪ p. Repair: restrict R_c^{(K)} explicitly to the
window y ≥ √d/(2p) (i.e. f ≤ 2p) and say "width ≍ (2K+1)/p when c√d ≪ p"; likewise after Prop 2.4 say the target
is at scale ≲ 1/p (≍ 1/p for c√d ≪ p). (R134 repair applied.)

D7 (MINOR, §2.7 first paragraph). "α obstructs strong approximation [BL, Thms 1.8, 1.9]": Thm 1.9 says the
opposite kind of thing (Q-points are not dense in the Brauer set, i.e. failures of SA *not* explained by BM). The
SA obstruction by α is Thm 1.8 (1.5) with Thms 1.2, 1.5. Repair: cite "Thm 1.8 (1.5), Thms 1.2, 1.5", and add
"(and by Thm 1.9 not every failure of strong approximation is explained by α)". (R134 repair applied.)

D8 (MINOR, Prop 4.10 proof). "divisors f ≤ p of p²+12" — the bound f ≤ p is not part of Lemma 2.2(iii) and is not
needed (N ≡ 1 mod 12 itself is not ≡ 7). Repair: drop "≤ p". (R134 repair applied.)

D9 (MAJOR, abstract and Thm 3.2(ii) statement). "Every representative-independent invariant of these objects is
congruence or genus data" is literally false: e.g. the ideal class of a Heegner point of discriminant −4d (E1) or
of (f, α) in the ring class group (E5) is representative-independent and is not genus data. What (ii) actually
proves (and what RT2 §2 means) is that such invariants do not enter, or do not decide, the ES count: E5 non-genus
characters have coefficient 0; E3 the collision datum is genus/congruence data and automatic; E1/E2/E6 ES-goodness
is not a class invariant; E4 reduces to a one-variable polynomial. Repair: rephrase as "The only
representative-independent invariants of these objects that enter the ES count are congruence or genus data, in the
following precise senses", and similarly in the abstract. (R134 repair applied.)

D10 (MINOR, §6 H-E). T_2^+ is undefined. Repair: "the Type II count T_2^+(n) of EXACT_FORMULA (positive a, b; no
coprimality conditions) vanishes at every square n = m², odd or even". (R134 repair applied.)

D11 (MINOR, cosmetic). Report O134 says "pdflatex twice, 0 warnings"; from a clean checkout a third pass is needed
(toc + hyperref). No action needed in the paper.

---

# Round 2 (R138) — the O138 update (§6 long shots; abstract/intro/summary/hatches)

Referee: R138 (hostile, independent). Branch `side-agent/referee-note-r2`, merged from
`side-agent/barrier-note-longshots` (O138, report `reviews/agent-reports/AGENT_REPORT_O138.md`). Sources checked:
`LONGSHOT_PIGEONHOLE.md` [LP] + R135 (`reviews/longshot-pigeonhole-review.md`), `LONGSHOT_FIBRED.md` [LF] + R136
(`reviews/longshot-fibred-review.md`, D1–D14). From-scratch code: `scripts/review_r138_*.py`.

## §6.1 Covering in the e-slices — claim-by-claim

| claim (paper numbering) | source | verdict |
|---|---|---|
| Lemma 6.1 (e-slices) | LP Lemma 1.1 | SOUND (MINOR R138-1: p ∤ e not justified in the "every element has a value of e" sentence) |
| Lemma 6.2 (genus in a slice, ℓ = 2 incl.) | LP Lemma 1.2 | SOUND |
| Lemma 6.3 (collisions → signed solutions) | LP Lemma 1.3 | SOUND |
| Prop 6.4 (Kneser criterion + sharpness) | LP Prop 1.4, R135 D2 | SOUND |
| regimes paragraph (LP Lemmas 2.1, 2.3) | LP §2.1, §2.3 | SOUND (θ < 1 in Lemma 2.3 is fine: the proof never uses θ < 1/2) |
| Def 6.5 (TCC, index ≤ 2e^θ) | LP §2.2, R135 D3 | SOUND |
| Thm 6.6 (θ < 1/2, positive lower density) | LP Thm 2.2, R135 D3–D5 | SOUND |
| Remark 6.7 (all θ < 1) | R135 D6 | SOUND as a sketch, correctly attributed |
| Scope paragraph | LP §2.2 Reading, R135 D5 | SOUND-AFTER-REPAIRS (MINOR R138-2) |
| Conj 6.8 PH + EVIDENCE | LP Conj 5.1, §3, R135 §3 | SOUND; labels correct |

Re-derivations. *Lemma 6.1*: (i) 4N^I ≡ 1, 4N^II ≡ p (mod e), e odd; (ii)–(iv) as in the paper; |Σ| ≤ ∏(2v+1) =
τ(N²). *Lemma 6.2*: for odd ℓ | N, −e ≡ p (II) or p⁻¹ (I) mod ℓ, and for e ≡ 3 (4) Jacobi reciprocity gives
(ℓ/e) = (−1/ℓ)(e/ℓ) = (−e/ℓ) = (p/ℓ) = (ℓ/p); for ℓ = 2, 8 | p+e resp. 8 | pe+1 gives −e ≡ p (mod 8) (p² ≡ 1),
and (2/e) = Kronecker(−e/2) = (2/p). (ii) follows by multiplicativity. *Lemma 6.3*: two distinct unitary divisors
u₁ ≡ u₂ (mod e); after dividing by g = gcd the supports are disjoint, so ab | N, gcd(a,b) = 1; the identities
reduce to c(p+e)/(abcdp) and c(1+pe)/(abcdp). *Prop 6.4*: H = Stab(Σ) ⊂ Σ (1 ∈ Σ); any partial product with
stabiliser K makes Σ K-periodic, so all partial products in G/H have trivial stabiliser and Kneser iterates to
|Σ/H| ≥ 1 + Σ(|X_i| − 1) with |X_i| = min(2v_i+1, o_H(g_i)) (2v_i+1 consecutive powers). Sharpness: in ℤ/2m the
relevant subgroups are dℤ/2m with d ∤ m, the condition at d = 2m is 2k ≥ 2m−1 ⟺ k ≥ m and implies the others.
*Thm 6.6*: (a) all ℓ < e ≤ Y have (ℓ/p) = 1 (p ≡ 1 mod q₀, 8 | q₀), so R ⊂ K_e. (b) the greedy factor
u ∈ (x^{1/4}, x^{1/2}] exists because all prime factors of L are < e ≤ E₁ < x^{1/4}; Rankin saves
exp(−(1/4+o(1))(log x)^{2/3}) against 2E₁ = 2exp((log x)^{1/3}). h(ℓ^v) = (2v+1)² − (2v−1)² = 8v. Compatibility
with p ≡ 1 (q₀): ℓ ≤ Y, ℓ | m forces −e ≡ 1 resp. −e⁻¹ ≡ 1 (mod ℓ), i.e. ℓ | e+1; the local factor is then
1 + Σ_v 8v ℓ^{1−v} ≤ 1 + 8·(1−1/3)^{−2} = 19 — the constant 19 is right. The Y < ℓ < e product is ≍ (log e)^8 and
B_e^{−2} ≪ e^{2θ−2+ε}, so the tail is ≪ Y^{−1+2θ+ε}. (c) Σ_{n≤x/2} τ(n²)² ≍ x(log x)^8 (τ(ℓ²)² = 9); Shiu with
A = 9, k = e < X^{3/4} (X ≥ e²/4 for e ≤ x) gives X(log X)^8/φ(e); the E₁-tail beats (log x)^9. (d) e > x:
N ≤ e²/4 and τ(N²) ≤ τ(N)² ≤ exp(2·1.538·log 2·log N/log log N) ≤ exp(4.3 log e/log log e) eventually, against
B_e = e^{1−θ−o(1)}. Positive lower density: the complement has ≥ (1 − CY^{−1+2θ+ε} − o(1))π(x; q₀, 1)
≍ π(x)/φ(q₀) elements. *Remark 6.7*: with f_r = τ(·²)^r the local factors are ≪_r v^{r−1}, Markov gives
B_e^{−r} ≪ e^{−r(1−θ)+ε}, summable iff r(1−θ) > 1; (d) holds for every θ < 1. "coset of size ≥ e^δ" ⟺ θ = 1−δ.
*PH evidence* matches LP Table 3.1 (P20 = 0 exactly for 3529, 110881 among the 2370 MH primes < 10⁶) and R135 §3
(six primes re-run); "≈ 5% at 10⁸" matches LP §3 reading 1.

From-scratch code `scripts/review_r138_cover.py` (sympy): for all p ≡ 1 (4), p < 400, all e ≤ 3p+50, both types:
Σ_e(N) as a product set equals the ratio set; fibre non-empty ⟺ −1 ∈ Σ; every pair gives an ES solution; Lemma 6.2
(i)–(ii) for every prime factor including 2; Type II slices with p | e are empty in this range (Type I: impossible).
Lemma 6.3 identities verified exactly (Fractions) on every slice with 2^ω(N) > φ(e), p < 300, e < 400. Prop 6.4:
criterion ⇒ t₀ ∈ Σ on 4853 random cyclic instances where it applies (no counterexample); sharpness example
ℤ/2m (m < 15, k < 20): criterion ⟺ k ≥ m ⟺ m ∈ Σ.

## §6.2 Fibred encodings — claim-by-claim

| claim (paper numbering) | source | verdict |
|---|---|---|
| Setup, c(n) = Σ c_s | LF §1, Lemma 1.2 | SOUND-AFTER-REPAIRS (R138-3: Sol(n) vs f(n) for composite n) |
| Lemma 6.9 (rigidity) + Borel density | LF Lemmas 2.1–2.2 | SOUND |
| Thm 2.3 consequences (incl. R136 D2, D3) | LF Thm 2.3 | SOUND-AFTER-REPAIRS (R138-4: second half of D2 dropped) |
| Cor 6.10 (generic flatness, D4/D4b) | LF Cor 2.4 | SOUND (sketch; single D′ = lcm is fine) |
| Thm 6.11 (a)–(c) relative to (C), D9 | LF Thm 3.1 | SOUND relative to (C); second-hand citation caveat present and adequate |
| F4 / Pell example (D10) | LF §4, §6 | SOUND (EVIDENCE label correct) |
| Prop 6.12 odd-square test under (U), D12 | LF §5.1 | SOUND-AFTER-REPAIRS (R138-5: (U) too weak for the proof as written; inherited from LF, missed by R136) |
| Earnest spinor example | LF §5.2, R136 | SOUND (R136 checked the PDF) |
| Prop 6.13 (a), (b), D5, D6 | LF §5.3 | SOUND; numerics reproduced (MINOR R138-6: 10009 ∉ [10³,10⁴]) |
| Thm 6.14 items 1, 2, 4 (D13) | LF Thm 5.4 | SOUND-AFTER-REPAIRS (R138-7: Pell orbits in item 1 are not power-fibred; item 4 must say "all pieces X1") |
| Thm 6.14 item 3 | LF Thm 5.4(3), R136 D14 | CONDITIONAL — correctly labelled; CTX failure for the pair space stated |
| Exact-scope paragraph (E-a)–(E-d), D1 | LF §5.5, R136 D1 | SOUND: "not a theorem about all large-fibre encodings", T8 blind spot only partly closed |

Re-derivations. *Lemma 6.9*: U = dom φ irreducible, E ⊂ U dense, U = ⋃ φ⁻¹(sᵢ) finite closed cover ⇒ one piece.
*Cor 6.10*: s₀ ∈ ℚ(n)³ integral at infinitely many integers ⇒ polynomial (division with remainder; the remainder
term tends to 0); integrality of s₀(n) depends on n mod D′, so p ≡ m₀² (D′) and a Dirichlet prime m ≡ m₀ give a
Type I solution for m², contradicting ET Prop 1.6. *Thm 6.11*: (a) is (C) orbit by orbit; (b) conjugate compact
stabilisers have equal volume, finitely many real orbits, |Γ′_y| bounded (finitely many conjugacy classes of finite
subgroups); (c) is the contrapositive of (b). *Item 2*: c ≤ #orbits·max_O w_O ≤ μ f · R max_θ w_θ, so c ≥ M/2
forces M ≤ 2Rμf max_θ w_θ — the D13 normalisation is correct. *Prop 6.12*: see R138-5. *Prop 6.13*: (a) a
represented k prime to 4dm² has (−4dm²/k) = 1, hence χ₋₄d(k) = 1. (b) on represented values χ₋₄d = (·/p), which is
an assigned genus character; it is non-trivial on the class group iff there is a second assigned character
(Cox Thm 3.15 for D = −4dp: at 2 unless dp ≡ 3 (4), in which case d has a prime q ≡ 3 (4)) — matches the paper.

From-scratch code `scripts/review_r138_genus.py` (own reduced-form enumeration, own χ evaluation, own Type II
count): Prop 6.13(a) for all odd m < 60, d ≤ 12, gcd(m,2d) = 1 (𝔊⁻ empty); (b) #𝔊⁻_d(p) = h(−4dp)/2 for all
p ≡ 1 (4), p < 700, d ≤ 12, p ∤ d; the five test primes 1009, 2689, 4729, 9601, 10009 are squares mod 120, and
for d ≤ 8: #𝔊⁻ ∈ [10, 144], F_d(p) = 0 in exactly 19 of 40 pairs. Matches the paper.

## Consistency with the rest of the paper (R134 version)

Abstract, intro item, the sentence after Prop 4.4 (scale constraint), hatches intro, the non-escapes remark and the
Summary were all checked against §6. H-A/H-B are unchanged; ES is stated as not proved in the abstract, §1, §6
and §8. Cross-references: eq:VIVII, Prop 3.x (typeII)(c),(d), Prop locsq, Lemma slices, Prop scale all resolve
and are used in the sense in which they are stated. The R134 D9 wording ("invariants that enter the ES count") is
untouched. Two headline sentences over-reach (R138-8, R138-9); with those repaired, the labels are honest.

## Defects (R138)

No FATAL and no MAJOR defects. All repairs below are **applied** to `paper/es-automorphic-barrier-note.tex`
(commit "barrier note: R138 repairs").

* **R138-1 (MINOR, §6.1 set-up, Lemma 6.1 and the sentence after it).** The standing hypothesis "p ∤ e" was imposed
  for both types. The claim "every element of V_I ∪ V_II has a value of e" was then left unjustified. The source's
  justification for Type I ("p | 4abd = pe+1 is false") is a non sequitur: 4abd = pe+1 ≡ 1 (mod p) contradicts
  nothing. For Type I, though, p ∤ e is not needed at all: 4N^I ≡ 1 (mod e), so gcd(N, e) = 1 anyway, and
  Lemma 6.2 never uses ℓ = p. For Type II, e ≤ a+b ≤ ab+1 ≤ N+1 = (p+e)/4 + 1 gives e < p, so p ∤ e holds
  automatically. *Repair applied:* "p ∤ e for Type II", plus the one-line reason in the parenthesis. (In my
  runs, Type I slices with p | e were empty for p < 200 and e < 12p, but nothing relies on this.)
* **R138-2 (MINOR, §6.1 Scope).** The phrase "expected number … bounded by Σ_e (log e)^8 e^{2θ−2}, independently
  of p" mixes two things: the bound is an average over p ≤ x, and it is uniform in x. *Repair applied:*
  "averaged over p ≤ x, … uniformly in x".
* **R138-3 (MINOR, §6.2 set-up).** Sol(n) was defined as the whole solution set, but f(n) as the number of Type I
  and II solutions. Thm 6.11(a) bounds Σ over Sol(n) by μ(n)f(n)max w. That inequality fails for composite n
  with solutions of neither type. LF defines Sol = Sol_I ∪ Sol_II. *Repair applied:* Sol(n) is now the set of
  Type I and II solutions (all solutions for n prime), and f(n) = #Sol(n). The consequence of Thm 2.3 now ends in
  "s_i is a solution of (1.1)".
* **R138-4 (MINOR, consequences of LF Thm 2.3).** The second half of R136 D2 had been dropped: the ℤ_ℓ-point must lie
  in dom φ_i, with φ_i ℓ-integral there. "ℤ_ℓ-coefficients" alone does not give s_i ∈ ℤ_ℓ³, because a
  denominator can vanish mod ℓ at the point. *Repair applied.*
* **R138-5 (MINOR, Prop 6.12; inherited from LF §5.1 and missed by R136).** The proof read "every other factor takes
  the same value at p and at m²". Under (U) this is false for m_ℓ with ℓ ∉ S₀, where only positivity is assumed.
  Also, (U) never guaranteed that an Euler product of positive factors is positive. *Repair applied:* (U) now
  includes "∏_ℓ m_ℓ(n) > 0 when all its factors are". The proof now argues: if every factor at ℓ | m and at p is a
  unit, then by (U) the Brauer averages at p and m² agree and the remaining factors are positive, so M(p) > 0
  gives M(m²) > 0. The statement, with the D12 third alternative, is unchanged and now correct.
* **R138-6 (MINOR, Prop 6.13 evidence).** The test primes include 10009, which is not in [10³, 10⁴]. *Repair
  applied:* "[10³, 1.1·10⁴]". The numbers themselves are reproduced exactly (19/40; #𝔊⁻ ∈ [10, 144]).
* **R138-7 (MINOR, Thm 6.14 items 1 and 4).** (i) Item 1 listed "R = O(log n) for Pell orbits" inside a theorem
  about power-fibred encodings, but Pell orbits are only logarithmically fibred (δ = 0); the author's report says
  so too. *Repair applied:* removed from item 1. The Example paragraph after Thm 6.11 already covers the Pell
  orbits correctly. (ii) Item 4 is a statement about X1 pieces only, via Cor 6.10. *Repair applied:* "Θ finite,
  all pieces X1, and their data uniform".
* **R138-8 (MINOR, abstract).** "covering certificates from the prime factors below the modulus fail for a
  positive proportion of primes" drops the coset-size restriction. That is exactly R135 D5, the headline issue
  that the §6.1 Scope paragraph handles correctly. Arguments that merely hit −1 are not excluded. *Repair
  applied:* "covers of cosets of size ≥ e^δ in (ℤ/e)* by the prime factors below e fail …".
* **R138-9 (MINOR, Remark "non-escapes").** The flat statement "Covering reduces to H-A/H-B (Theorem 6.6)" is an
  Assessment: Thm 6.6 excludes only transparent covers of large cosets. *Repair applied:* the sentence is now
  labelled Assessment, with that scope. The Summary sentence is already inside an Assessment paragraph.
* **Layout.** The repairs pushed two bibliography lines onto a 25th page. I tightened four sentences (no content
  change: the Thm 6.6 "hence" sentence, the definition of a TCC, the second-hand-citation sentence, and the
  Assessment parenthesis in Scope) and put `\enlargethispage{3\baselineskip}` before [LA]. Result: 24 pp.

Points checked and found correct, no action needed:
* Thm 6.6 is stated for θ < 1/2 with C = C(θ, ε) independent of Y. The positive lower density follows for
  Y ≥ Y₀(θ, ε).
* The report's remark on Prop 6.4 sharpness is right: the conditions at the other subgroups H ∌ m are implied by
  the one at H = {0}.
* Earnest Prop 5.1 was checked by R136 against the PDF in `sources/r136`.
* DRS, EM, EMS, BR and CTX are not in `sources/`. I could not access them either. The paper says the statements
  were checked second-hand, which is the correct caveat. Thm 6.11 and Thm 6.14 item 2 are labelled "relative to
  (C)", and item 3 is CONDITIONAL.

## Compilation

pdflatex, three passes from a clean directory: 0 errors, 0 undefined references, 0 overfull boxes, 24 pp.
The 9 underfull boxes are the same as in O138 (bibliography URLs and one page break).

## Recommendation (Round 2)

**ACCEPT (internal) the O138 update, with the R138 repairs applied.**

§6 is a faithful and correctly labelled condensation of LP/R135 and LF/R136. I re-derived every proof sketch,
including the constant 19 and the (log e)^8 moments in Thm 6.6, the Kneser iteration, the genus symbols at ℓ = 2,
the generic-flatness corollary and the 𝔊⁻ genus count. I also checked the small cases with from-scratch code
(`scripts/review_r138_cover.py`, `scripts/review_r138_genus.py`).

The scope statements are honest:
* Thm 6.6 is restricted to transparent certificates of cosets of size ≥ e^δ.
* Thm 6.14 is explicitly "not a theorem about all large-fibre encodings", with (E-a)–(E-d) left open.
* Item 3 is CONDITIONAL, and the CTX hypotheses are shown to fail for the pair space.

ES is not proved, and the paper says so.
