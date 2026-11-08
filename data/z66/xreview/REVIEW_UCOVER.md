# z66 UCOVER — Astra hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES (minor scope/output fixes; central theorems survive).**
Reviewed `side-agent/z66-ucover` at `ec712c7f1c2e42f64d474da13ea0b4a26ebbf9a4`.
Theorem T really establishes U strictly larger than the unit squares, relative to the stated ET input; Cor T.1 follows relative to LOGIC2 Thm D. ES remains OPEN.
No provider/authentication/quota error occurred. No subagent was used. All computations used `ulimit -v 4000000`, timeouts ≤1800 seconds, and at most two compute processes (driver plus one serial child).

## Per-claim verdicts

| Claim | Classification | Hostile check / qualification |
|---|---|---|
| Lemma 1, all seven families | CORRECT | CRT, Jacobi parity and the three redundant-family reductions check. The repaired statement is about generators across levels, NOT exact-level equality. |
| Mixed I-4/II-1 reduction | CORRECT | Divide a,b,c by ℓ^min(v(a),v(b)); level drops by twice that minimum. A level-zero parent would contain 1, impossible. |
| §2.2 injections and completeness | CORRECT | F→ΣI at ℓ^k; pure E/D→ΣII at ℓ^k; A→ΣII at ℓ^(k+k₁). Maps are injective for each fixed split. |
| ET §3 transfer to all positive sextuples | CORRECT | Verified directly in the PDF, not inferred merely from the statement about Type I/II solutions; details below. |
| Theorem T / exponent −2/5+o(1) | CORRECT | Uniform divisor bounds permit summation over every k. The A scale ℓ^(2k−1) is essential and is handled correctly. |
| Effective, uncomputed ℓ₀ | CORRECT | Only effective divisor estimates and geometric sums enter. No small numerical threshold follows from the argument or finite trees. |
| Cor T.1 | CORRECT relative to Thm D | Count completely caught first-level cylinders, not cylinders merely intersecting Cℓ. The same uncovered profile works for every q coprime to ℓ. |
| §3 finite-level CERTIFIED statements | CORRECT in checked runs | Reproduced 11,13 level 1 and 17 through level 4, plus literal seven-family brute force at 17. Infinite survival at 17 is still only EVIDENCE. |
| §5 two-prime K evidence | CORRECT as upper bounds | All three revised counts reproduce, only over (2,2). Missing larger/mixed-support events remain possible; no proof of K∩U≠∅. |
| S-family classification / S1 | CORRECT | Eventually positive polynomial words have exactly one linear coordinate; W1 character and W2 2-adic quotient are correct. Not a classification of non-polynomial methods. |
| S2 and S2′ | CORRECT | Checked both large-variable scans, harmonic bounds and numerical constants. The analytic count, not finite-width execution, controls the infinite tail. |
| Theorem S(a–c), including interval tail | CORRECT in checked certificates | Independent closed-form interval tail verifies 11,17,101; level-one failures at 3,5,7 reproduce. Other listed certificates were inspected, not all rerun. |
| C word-parameter output | CORRECT-WITH-FIX | Some printed W2 parameters overflow signed 64-bit casts. Residue/goodness calculations remain in 128-bit arithmetic and the survivor certificate ignores these columns. |
| Four unresolved S classes / numerator extension | CORRECT-WITH-FIX | Two scope statements need qualification; see required fixes. No central proof depends on them. |

## Proof audit

Source checked: `sources/elsholtz-tao-1107.1010.pdf`, printed pp. 7–8 (polynomial solvability/Prop 1.9), 11–18 (varieties, Lemma 2.8, §3), and 49 (A.6); `Z65_LOGIC2.md` §5.5; `Z64_SDEEPF.md` §§2–3.

1. For I-1, f≡−1 mod 4a′d′ and f | 4ℓ^(2k₁+k₂)a′²d′+1 give A. The character χ₋₄d forces k₂ odd and g a non-residue. The Jacobi fact remains valid for composite f, not just primes.
2. I-4/II-1 give e=4a′b′D−1 and c e=ℓ^k₁a′+ℓ^k₂b′. Removing common ℓ-powers gives a pure generator containing the original cylinder. Quadratic reciprocity forces its level odd.
3. II-2 gives f=4acd−1 and f′ | a+c, using c(4a²d+1)−af=a+c and gcd(c,f′)=1. Its Jacobi symbol is −1; hence k odd. I-2 reduces to E/F, I-3 to A or an impossible quadratic-root condition, II-3 to A/F. The reverse constructions are genuine primitive family classes.
4. The four-variable equations imply all six defining coordinates are positive integers. In particular the F extra coordinate is (Na+w)/c; the E and A embeddings use (2.15). A has K′=k+k₁≤2k−1. F's twin is counted by the swapped point, not an unaccounted extra factor.
5. ET Lemma 2.8's proofs use positivity and the defining equations, not coprimality or primitive normalization. Reflection preserves positive integral sextuples and permits a≤b. The bounds give e f(cd)²(ac)≪n³ and e²(ad)(ac)(cd)≤n².
6. Each of ET §3's four cases for each type fixes a parameter/product ≤n^(3/5) or n^(2/5), then counts divisors of a positive, polynomially bounded integer. Thus the argument bounds ALL positive sextuples, including non-normalized ones; there is no missing normalization multiplicity.
7. Put α=3/5+η, β=2/5+η, η=sup_{n≥ℓ}η(n). With x=ℓ^(α−1), y=ℓ^(β−1), z=ℓ^(2β−1), the displayed union bound is at most
   `(1−1/ℓ)^−1 [x/(1−x) + 2y/(1−y) + ℓ^(−β) z/(1−z)²]`.
   For η≤1/20 this converges uniformly. F starts at ℓ^(−2/5+η), whereas E and A start at ℓ^(−3/5+η); hence the asserted exponent follows. This formula plus an effective divisor-bound threshold supplies an effective sufficient ℓ₀, but none is evaluated here.
8. The effective nature does not require a potentially ineffective prime-distribution estimate: for any fixed ε>0 the elementary τ(n)≤Cε n^ε has computable Cε, obtained by treating finitely many small primes separately. ET's bounded divisor-product operations preserve effectivity.
9. At most (ℓ−1)μℓ entire first-level cylinders lie in Cℓ. Each other non-residue cylinder contains an uncovered g, and eℓ,g has component 1 at every prime dividing q. LOGIC2 Thm D(iv)⇒(i), contraposed, is exactly the NOI conclusion. This audits the application of Thm D, not a fresh reconstruction of its U64 model-theoretic dependencies.
10. For S2's W1 large-X scan, X | N+s, t≥X−1 and ts=N+X bound s and the complementary divisor by √(N/2)+O(1). For W2, both factors are positive; if s>X₀, their smaller factor r<s satisfies s | M+r. Then s≤N+r and r²≤N+s≤2N+r, giving the advertised r and cofactor bounds. No negative-factor branch is omitted.
11. The S2′ constants work at N=10⁵ and improve thereafter: the W1 bracket is ≤√N(1.37 ln N+7.02), W2 ≤√N(2.44 ln N+9.88). Summing the resulting Tk is legitimate independently of observed candidate counts.
12. The original interval tail and ratio bound are sound. The final `mpf` integer conversions are exact for the reported ranges: every reduced mass denominator divides φ(ℓ^K₂)<2·10¹²<2⁵³, and numerators are smaller. The `1+10^−30` factor rounds to 1 at default precision and supplies no protection, but none is needed here. The independent checker uses interval conversions throughout and confirms positivity with large margins.

## Replays and independent certificate

Archive extracted into `/tmp/xrev_UCOVER`; compiled archive-local `zlev`, `zlev2`, `zsw` with gcc -O2 (swords also -lm).
Committed replay driver: `scripts/z66_xrev_ucover_check.py`; run under the resource limits with `uv run --with sympy --with mpmath python scripts/z66_xrev_ucover_check.py /tmp/xrev_UCOVER`.
The driver uses the original enumerators but independently accounts for branches and evaluates the infinite Tk sum using closed-form geometric moments, not the original finite-sum/remainder code.

| Replay | Result |
|---|---|
| ET tree 11,13 level 1 | All 5/5 and 6/6 non-residue branches caught. |
| ET tree 17 levels 1–4 | Event counts 6,46,300,564; survivor counts 2,26,396,6664; final mass 0.084775. |
| ET literal brute 17, modulus≤10⁵ | Byte-identical stored output; all 106 distinct (level,residue) keys occur in exact enumeration. |
| S literal brute 17, A,uv≤30000 | Byte-identical output; exact equality on 38 unit-profile keys / 61 emitted unit good rows. The memo's 79-row count before unit filtering includes non-unit events (45 distinct keys before filtering). |
| S certificate 11, K₁=6,K₂=11 | 311256 tree survivors; branches 2,6; minimum lower endpoint 0.095565607023; tail <0.001066561. |
| S certificate 17, K₁=5,K₂=9 | 329990 survivors; branches 3,5,6,7; minimum lower endpoint 0.060628906803; tail <0.000994781. |
| S certificate 101, K₁=3,K₂=6 | 387550 survivors, 38 branches; minimum lower endpoint 0.009904933021>0.0099; tail <0.000089186. |
| S(b), original and independent interval sum at 10⁵ | Both enclose 0.36546306656825321908718346956; <0.3655<1/2. Termwise monotonicity checks. |
| S(c), levels 1 at 3,5,7 | Caught non-residues respectively {2}, {2,3}, {3,5,6}. |
| K, all seven families≤10⁶ plus levels2 | 37/8580, 269/94380, 397/111540, all over (2,2), exactly as stated. |

## Falsifier table and scope

| Screen | Independent assessment |
|---|---|
| F1 odd squares | PASS: no caught unit-square profile; the Jacobi arguments explain this structurally. The claim concerns non-square *profiles/classes*, not integer counterexamples. |
| F2 12 C-even/numerator-8 zeros | Properly outside the theorem's scope: no numerator-8 positivity mechanism is proposed. Do not promote the speculative numerator extension into a result. |
| F3 285 composite zeros | Properly outside the ET unit-profile conclusion. In fact no positive integer >1, composite OR prime, embeds as a unit of Ẑ. The S setting allows non-units but asserts no pointwise solution at these zeros. |
| F4 14 (★)-zero / 38 𝔊*-zero primes | Properly outside scope: failure of those restricted representations neither falsifies nor establishes a polynomial-cover obstruction. No claim to solve any listed prime is made. |

The screen definitions/counts were checked against `data/z58/screens/README.md`; the zero searches were not rerun because no assertion here depends on their numerical values. “No HOT LEAD,” K remaining CONJECTURE, finite-tree survival only EVIDENCE, and no conclusion about ES truth are honest. “Strengthened” follows from T, not from the finite trees.

## Required fixes, in priority order

1. **Scope:** replace “their profiles need two small primes” for all four unresolved S classes by “at least two.” Class 825 mod 840 requires nontrivial components at THREE primes: residues (0,0,6) at (3,5,7). Classes 265 and 321 also require a non-unit component. The example for 769 and its proposed (5,7) tail remain valid; they do not describe all four classes.
2. **Output correctness:** print W2 parameters in 128-bit decimal or explicitly label/remove truncated parameter columns. Re-running `zsw 11 11` prints `W2 285311670610 -2732209869866826865 285311670612 1`; the actual positive u is 81402749387410384454543=N(N+2), N=11¹¹. Residue and good bit are correct, so this does NOT invalidate the certificate, but the emitted witness is false as printed.
3. **Scope:** downgrade “method transfers to any numerator with a Prop 1.9 analogue” to an unproved possible extension requiring suitable counts and square obstructions. A family classification alone is insufficient: for numerator 1, x=y=z=3n covers every class, including squares. ET Remark 1.10 is not a proof of this memo's obstruction for every numerator.

Recommended hardening, not a theorem gap: assert the <2⁵³ conversion range or use `iv.mpf` for both exact integers in the original comparison; remove its ineffective 10^−30 safety factor. Clarify that the 79-row S cross-check includes non-unit rows.

**Bottom line:** accept the mathematical core, preserve its explicit dependencies and asymptotic quantifiers, fix these ancillary scope/output assertions before export. No finite-prime ES claim or resolution of the fixed K-question is established. WAIT.
