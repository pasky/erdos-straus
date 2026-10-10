# Referee report R134 — paper/es-automorphic-barrier-note.tex

Referee: R134 (hostile, independent). Branch `side-agent/referee-automorphic-note`, merged from
`side-agent/automorphic-note`. ES is not proved anywhere; the paper says so (abstract, §1, §8).

## Per-claim verdicts (filled in progressively)

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
