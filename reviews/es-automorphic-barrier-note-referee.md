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
