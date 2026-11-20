## §0

Result: Independent hostile review of `notes/z75/ANALYTIC_BREAK.md` (commit c49b5f41e) and of two proposed extensions. Verdict: ACCEPT WITH MINOR FIXES. No mathematical error found.        Label: Assessment (review)
Scope: Correctness of the note's theorem (e*(p) ≤ exp(C√(log p·log log 3p)), effective; 4e*(p)+3 ≤ √(4p/3) at p ≡ 1 (8)), and of extensions (1) all n via rad(n) and (2) Dirichlet-GRH-only polylog-free bound. Capped ES only. Nothing here concerns ES itself.
Review: this file is the review. Reviewer: Claude Opus. This is a same-lab review (the note's author lane is Claude-family), so the cross-lab (Astra) review required by AGENTS.md §3 is **still owed**.
Triage: DATA (review record)
STATUS delta: none from this file. See §6 for what the export should touch.

# Hostile review of ANALYTIC_BREAK (z75)

I read the note line by line and re-derived every step. The source checks were Montgomery–Vaughan III draft Thm 28.19–28.21
(`sources/omega9/montgomery-mnt3.pdf`, sha256 ef098f0a…e7855, printed pp. 229–234) and Pollack JNT 187 (2018) §2
(`sources/pollack_jnt2018_least_nonresidue_mod4.pdf`). I also checked the comparison text in `CAP_DOWN.md` Lemma 1.1,
Prop 1.3 and Cor 2.2, `PHASE_DIAGRAM.md` Thm 5.1, `CAP_INTERPOLATION.md` Thm 4.2 and `EXSET_LINNIK_CAPS.md` Lemma 4.3. I ran two small exact-arithmetic scripts
(Appendix; run from /tmp under `ulimit -v 6000000`, `timeout 1800`, one process, all under 1 min). Per instructions
nothing outside this file was written.

## 1. Verdicts

| item | verdict |
|---|---|
| §1 free carrier (= CAP_DOWN Prop 1.3) | correct |
| §1 planted carrier (any odd NR s, q ≡ 3 (4), q ≡ 4s−p (s²)) | **correct**: v_s(K)=1, (s/q)=(−1/s)(q/s)=(−1/s)(−p/s)=(p/s)=−1; one reduced class mod 4s²; cap (j−1)/2 ≤ (q−3)/4 |
| §1 explicit bound 4e*(p)+3 ≤ √(4p/3), p ≡ 1 (8) | **correct**; checked for all 796 primes p ≡ 1 (8) < 3·10⁴ by enumerating the reduced forms |
| §2 dichotomy and L(1,χ) ≥ exp(−O(T)) | **correct, effective** |
| §3 Gallagher input: exact source and use | **correct**; the statement matches MV III Thm 28.19 verbatim (see §2) |
| §3 exceptional-character bookkeeping (two alphabets, signs) | **correct** |
| §4 deletion count, Minkowski II, index correction | **correct**; the algebra was verified exactly on 132 (p,q) pairs |
| §4 final exponent (log(X/B^{k−1}) formula) | **correct**; all costs are O(T), T=√(u log u), u=log p |
| finite / non-1-mod-8 cases | **correct** (Lemma 4.3 identities re-derived; small p is absorbed effectively) |
| Extension (1): all odd n via d = rad(n) | **correct as sketched** (§4 below); write it out before promotion |
| Extension (2): Dirichlet GRH only ⟹ exp(O(√(log₂p·log₃p))) | **correct** (§5 below); this supersedes the Dedekind-GRH hypothesis of CAP_INTERPOLATION Thm 4.2(b) |

Overall: the theorem appears to be a genuine improvement of the campaign's unconditional pointwise cap, from effective
(p−5)/8 and ineffective p^{1/4+ε} to an effective subpower bound. It removes exactly the obstacle recorded in
PHASE_DIAGRAM Thm 5.1 Remark (2), the exceptional modulus dividing 4·rad(n), by two devices. First, an elementary dichotomy:
either a small non-residue exists (and then the planted carrier with Linnik applies), or the only harmful exceptional
character has 1−β ≥ exp(−O(T)). Second, quotient correction by the index j, which uses the independently available free
carrier. The result is about the cap relaxation only. It is not ES, not a bound on n₃(p), and not an exceptional-set result.

## 2. Gallagher: exact source check

MV III draft Thm 28.19 (p. 229–230) states the following. There are c ≥ 1 and κ₀ ≥ 3 such that for κ ≥ κ₀ and 1 < Q^{6c} ≤ x,
  Σ_{q≤Q} Σ*_{χ mod q} |ϑ(x;χ) − E₀(χ)x| ≪ x exp(−log x/(κ log Q)) + (log x/log Q)² x Q^{−1},
unless F(s,Q) = ∏∏* L(s,χ) has an exceptional real zero with 1−β₁ < 1/(κ log Q). In that case the χ₁ term becomes
ϑ(x;χ₁) + x^{β₁}/β₁ and the right side becomes (1−β₁)(log x)·(x exp(−log x/log Q) + x log x/(Q log Q)).
With x = Q^A this gives exactly the note's two bounds, X(e^{−A/κ} + A²/Q) and (1−β)log X·X(e^{−A} + A/Q). The
condition "A ≥ 6c" is the hypothesis Q^{6c} ≤ x. The sum uses ϑ (primes only) over *primitive* characters,
including the trivial one, which is how the note uses it.

Points checked:
* **Uniform-coefficient trick.** On units mod pB_i the detector 1_{a_i}(1−χ_p)/2 has 2φ(B_i) characters. Each has
  coefficient of modulus exactly μ_i = 1/(2φ(B_i)), and each has a distinct primitive inducing character of conductor ≤ pB_i ≤ Q.
  So the weighted error is ≤ μ_i·(Gallagher sum), with no loss of φ(B_i). Passing to primitive characters costs ≤ log(pB_i)
  per character in ϑ, hence O(log Q) after weighting (ℓ¹ = 1). This is correct.
* **Exceptional bookkeeping.** A real primitive ψ₁ of conductor ≤ Q lies in the support of alphabet i iff its
  conductor divides pB_i. Since B₁ and B₂ share only the factor 4 and 8 ∤ B_i, the common candidates are 1, χ₋₄, χ_p and χ₋₄χ_p. Their coefficients are
  μ, μχ₋₄(3) = −μ, −μ and +μ. Only χ₋₄χ_p subtracts from the main term. ζ has no real zeros in (0,1). This is correct.
* **Gain versus error.** With h = (1−β)log X < A/κ, we have 1 − X^{β−1}/β ≥ c·min(1,h). The (1−β)log X factor in the
  exceptional error makes the ratio error/gain ≤ C(1 + A/κ)(e^{−A} + A/Q), which is small for large A. This is the same
  Deuring–Heilbronn cancellation as in MV's effective proof of Linnik (Thm 28.21, p. 233–234). §2 is needed for the
  **size** of the count, X·exp(−O(T)), not for its sign. Without §2 the count could be as small as X·p^{−1/2}, and §4 would
  then give only p^{1/2+o(1)}. The note uses §2 for exactly this purpose.
* **Threshold compatibility.** 1−β < 1/(κ log Q) ≤ 1/log(4p), so §2's hypothesis on β holds.
* **Effectivity.** c, κ₀ and the implied constants come from the log-free density theorem and the Exceptional Zero
  Statement (Deuring–Heilbronn), both effective. MV's Linnik proof is effective.
* **Draft caveat (cosmetic, not an error in the statement).** The MV *draft* proof splits cases at 1/(κ₀ log T)
  and 1/(κ′ log T) (T = Q³, κ′ = κ/3), which leaves a nominal gap. A zero in the gap is handled by the first-case density
  integral run up to 1 − 1/(κ′ log T). The statement is the standard Gallagher form (Invent. Math. 11 (1970), Thm 7),
  which the README says was not itself obtained. **Fix M1:** label the result "rel. Gallagher's theorem in the form
  MV III (course draft) Thm 28.19". If possible, add a published-edition cross-reference before promotion.

## 3. Dichotomy, constants, exponent, finite cases

* **Alternative 1.** s ≤ w = p^{3/k} is an NR. It is odd because p ≡ 1 (8). Effective Linnik gives q ≤ c(4s²)^L, so
  e* ≤ exp(O(log w)) = exp(O(u/k)) = exp(O(T)).
* **Alternative 2 (§2).**
  * f = 1*χ ≥ 0. There are ≥ C(N,k) ≥ (N/k)^k distinct k-products of primes ≡ 1 (4) in (w/2, w], and each is ≤ w^k = Y = p³.
    This gives Y(c/(3u))^k = Y·exp(−O(k log u)) = Y·exp(−O(T)).
  * The hyperbola split at D = √(mY) gives error O(√(mY)) = O(p²), which is negligible.
  * The derivative bound |L′(σ,χ)| ≪ log² m holds on [1 − 1/log m, 1] (head ≤ e·log²m, tail by parts).
* **§3 costs.** log B_i = O(k log k) = O(T), 1/μ_i ≤ B_i and log X = O(u). So the count is ≥ X·exp(−(c₂+c₃+o(1))T), and D must
  exceed c₂+c₃+1.
* **§4 deletion.**
  * A relation of sup-norm ≤ B forces q | N_a ≠ 0 with |N_a| ≤ (∏v)^{2B}, giving ≤ 2B·log∏v/log 2 prime divisors. So the bad
    count is ≤ (3B)^k·O(BT) = X·e^{−DT}·e^{O(k)}·O(T). This is correct.
  * Injectivity on [0,⌊B⌋]^k gives |H| > B^k and j < X/(2B^k), with j odd.
  * Minkowski II with the sup-norm cube (volume 2^k) gives λ₁⋯λ_k ≤ det Λ = |H|, hence λ_k < X/B^{k−1}.
  * Babai-type rounding in k independent vectors gives sup-norm ≤ kλ_k. The shift by ∏v^{−2L} gives exponents in [0, 2L].
    This is correct.
* **Correction.** (−s/q) = 1 and U/H is cyclic of order j, so (−s)^{−j} ∈ H. Then d = K·s^j·∏v^{2a_v} ≡ K·s^j·(−1)·s^{−j} = −K.
  The exponents are: b_s + j, which is even; 2 + 2a_v, which is even; and the 2-exponent unchanged. Lemma 1.1 applies with cap
  max((j−b_s)⁺/2, max_v(a_v−1)) ≤ max(j, 2L). The exact check (Appendix B) confirms the cap formula on every tested pair.
* **Exponent.** log(X/B^{k−1}) = (2 log X + (k−1)DT)/(k+1). The algebra is correct, and the result is O(u/k + T) = O(T).
  The balance k ≍ √(u/log u) is optimal for the three costs u/k, k log k and k log u.
* **Finite and non-1 (8) cases.** p = 2 is trivial. p ≡ 3 (4) and p ≡ 5 (8) have the integral identities, re-derived:
  4/(8k+5) = 1/(2k+2) + 1/(n(k+1)) + 1/(2n(k+1)). The threshold p₀ is effective but not computed. Below it the explicit
  bound (or CAP_POINTWISE's rad^5) is absorbed into C. **Fix M2:** say "C effective, not computed" in §0, since the
  theorem is not explicit.
* **Explicit bound.**
  * (a/p) = −1 holds even for even a, because a·F ≡ (aX+bY)² (mod p) and the form represents an odd value coprime to p.
  * c ≤ (p+1)/2 < p, and all forms of discriminant −4p are primitive.
  * (2/p) = 1 gives an odd q | a with (q/p) = −1. Then b² ≡ −p (mod q) gives q ≡ 3 (4), and q ≤ a ≤ √(4p/3).
  * This strictly improves CAP_DOWN Cor 2.2(a), (p−5)/8, to e*(p) ≤ (√(4p/3) − 3)/4. Pollack's Remark (ii) gives only
    p/(log p)^{1/2−ε}. No literature priority search was done for the elementary bound "n₃(p) ≤ √(4p/3) at p ≡ 1 (8)"
    (**M3:** flag it as unchecked priority, not as new).

Minor presentation points (non-blocking):
* **M4.** §4 "cap ≤ max(j, 2L)" can read max((j−b_s)/2, 2L−1).
* **M5.** §3: say that A depends on κ (MV take A ≍ κ log(const)), and that "large X" in 1 − X^{β−1}/β ≥ c·min(1,h) uses
  h/log X → 0.
* **M6.** §4's bad count has a "1 +" that is redundant but harmless.

## 4. Extension (1): all odd n via d = rad(n). Verdict: correct

* If n has a prime factor 2, a prime ≡ 3 (4), or a prime ≡ 5 (8), that prime has an integral ES solution. Scaling it by the
  cofactor gives e*(n) = 0. Otherwise d = rad(n) > 1 is squarefree, ≡ 1 (8), and all its primes are ≡ 1 (8).
* **The window.** q ≡ 3 (4) is coprime to d. gcd(K, d) = 1, because s | K and s | d imply s | q. The Jacobi symbol gives
  (K/q) = (d/q) = (q/d) = χ_d(q), with χ_d primitive, even and of conductor d, since d ≡ 1 (4) is squarefree. The parity at
  2 is as for primes, because d ≡ 1 (8).
* **The planted carrier.** χ_d(s) = −1 forces s ∤ d, and (s/q) = (d/s) = −1.
* **§2.** Use χ₋₄χ_d, which is primitive with conductor 4d. Discard the ≤ ω(d) = O(u) primes of d from the
  ≍ w/log w primes in (w/2, w]. This is harmless, because w = e^{Θ(T)} ≫ u.
* **§3.** Alphabets of primes ≡ 3 (4) (the first 2k of them, so log B_i = O(k log k) by PNT mod 4) are automatically
  coprime to d.
  * The support characters are ψ (mod B_i) and ψχ_d, with conductor cond(ψ)·d.
  * A real primitive ψ₁ with no alphabet prime in its conductor lies in a support only if it is 1, χ₋₄, χ_d or χ₋₄χ_d.
    Characters χ_{d′} with d′ a proper divisor of d (d′ ≠ 1) are not in any support, because the support always carries
    the full χ_d. The signs are as before.
* **§4.** It is unchanged. The alphabet primes and the free carrier s are coprime to d.
* **Scaling.** The overflow primes divide K, which is coprime to d, so they are coprime to n. Multiplying (x, y, z) by n/d
  keeps den z = r², because gcd(r, n/d) = 1, and rad r | y. This is CAP_DOWN Cor 2.1 Remark (3) with rad(n/d) | d.
  Checked exactly (Appendix C): 630 cases with d = p₁p₂, both carriers, n ∈ {d, d·p₁, d·p₁·p₂²}.
* **Small d.** Use CAP_POINTWISE's effective rad(n)^5. The explicit √ bound is primes-only, as the proposer says.
* **Result.** e*(n) ≤ exp(C√(log rad n·log log(3 rad n))) for every odd n > 1 with e*(n) > 0, and C is effective. This also
  subsumes odd squares, because rad(a²) is not a square. So it is consistent with the note's T1/F1 remark, which concerns
  running the argument at n itself.
* **Optional refinement, not checked in detail.** One could run at n with χ_{n₀}, where n₀ is the squarefree part, for
  non-squares, giving a bound in log n₀. It is not needed for the claim.

## 5. Extension (2): Dirichlet GRH alone. Verdict: correct

* **Setup.** Take X = (log p)^8, u = log log p, k = ⌊√(u/log u)⌋, one alphabet of the first k odd primes, and
  B = e^{O(√(u log u))} = X^{o(1)}.
* **Errors.** Under GRH for Dirichlet L-functions (including RH), θ(X,χ) − E₀X ≪ √X·log²(pBX) per character. Weighting
  by ℓ¹ = 1, the total error is ≪ X^{1/2}(log p)² = X^{3/4}, plus O(log p) from primitive passage.
* **Main term.** μX = X^{1−o(1)}, which dominates. No exceptional zero exists, so §2 and alternative 1 are unnecessary. The count is X·e^{−O(T)}.
* **Exponent.** §4 then gives cap ≤ exp(O(log X/k + T)) = exp(O(√(log₂p·log₃p))).
* **Comparison.** This matches the shape of CAP_INTERPOLATION Thm 4.2(b) and needs only Dirichlet GRH, not the Dedekind GRH
  for the Kummer fields. The index correction removes the need for ⟨S⟩ = all squares. For large p it also supersedes the
  (16 log n + 70)² GRH bound (which stays as the explicit all-n statement). It extends to all n as in §4.
* **Scope reminder.** This is still not (log₂p)^{O(1)}. It is consistent with FRONTIER "GRH alone does not reach
  (log₂p)^{O(1)} this way".

## 6. Hostile items checked and found not to bite

* (i) The subpower cap does not yield a small witness modulus. The q used has size up to p^{O(1)}, so the Type II
  witness barrier (FRONTIER: witness ≤ g(p) ⟹ n_p ≤ g(p)) is not contradicted. No bound on n₃(p) or n_p is implied.
* (ii) No sign or parity slip. The planted valuation is exactly 2, j is odd, and the target (−s)^{−j} lies in H. Exact
  rationals confirm all three (App. B).
* (iii) The free carrier s is never an alphabet prime, because of the parity of b_s.
* (iv) An exceptional conductor that meets both alphabets lies in neither support.
* (v) Gallagher is applied at fixed p with modulus pB_i ≤ Q. No BV or Siegel–Walfisz range issue arises.

**For the orchestrator at export (not done here):**
* **STATUS §1 "Capped relaxation" row** (lines ~72–76): replace the e*(p) refinements with the new effective subpower
  bound and (√(4p/3)−3)/4. Add the rad(n) form if extension (1) is written into the note. Replace the GRH clause by
  Dirichlet-GRH exp(O(√(log₂n log₃n))) (large n) and keep (16 log n+70)² as explicit.
* **FRONTIER 1097–1098.** The almost-all count #{p : e*(p) > p^ε} ≪ (log X)^{⌈4/ε⌉} is now superseded pointwise:
  the set is finite, with an effective bound.
* **FRONTIER 1190–1192.** This passage quotes the old effective and ineffective bounds.
* **CAP_INTERPOLATION Thm 4.2 Remark (3)** ("Unconditionally nothing of this shape is known") **and PHASE_DIAGRAM Thm 5.1
  Remark (2)** (the exceptional-modulus obstacle) are now outdated Assessments. An erratum pointer is optional. These are
  upgrades, not errors, so they go through the export after the **cross-lab (Astra) review**, which is still owed.

## Appendix A–C: scripts (run from /tmp; replay with `uv run --offline --no-project python check.py 30000`, then check2.py)

Output: `explicit-bound check primes p≡1(8) < 30000 : 796 ok` / `§4 construction verified exactly on 132 (p,q) pairs`
/ `extension(1) carriers+scaling verified: 630`.

```python
# Independent sanity check of ANALYTIC_BREAK §1 explicit bound and §4 index-correction algebra.
import sys, math
from fractions import Fraction
def isprime(n):
    if n<2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0: return n==p
    d=n-1;s=0
    while d%2==0: d//=2;s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,n)
        if x in(1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
def leg(a,p):
    r=pow(a%p,(p-1)//2,p); return -1 if r==p-1 else r
def factor(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def mult_order(a,q):
    o=q-1
    for l in factor(q-1):
        while o%l==0 and pow(a,o//l,q)==1: o//=l
    return o
def verify(p,x,y,z):
    assert Fraction(4,p)==Fraction(1,x)+Fraction(1,y)+1/z, "identity"
    r2=z.denominator; r=math.isqrt(r2); assert r*r==r2 and r%2==1 and math.gcd(r,p)==1
    for l,e in factor(r).items(): assert y%l==0
    return max([e for e in factor(r).values()],default=0)
# (A) explicit bound: reduced forms in nonprincipal genus, p ≡ 1 (8)
N=int(sys.argv[1]) if len(sys.argv)>1 else 30000
bad=0;cnt=0;worst=0
for p in range(17,N,8):
    if not isprime(p): continue
    cnt+=1; found=False
    A=math.isqrt(4*p//3)+1
    for a in range(2,A+1):
        if 3*a*a>4*p: break
        for b in range(0,a//2+1):
            if (b*b+p)%a: continue
            c=(b*b+p)//a
            if c<a: continue
            m=a if a%2 else c
            if leg(m,p)!=-1: continue  # principal genus
            assert leg(a,p)==-1
            ao=a
            while ao%2==0: ao//=2
            qs=[q for q in factor(ao) if leg(q,p)==-1]
            assert qs and all(q%4==3 for q in qs) and max(qs)<=math.sqrt(4*p/3)
            found=True;break
        if found: break
    assert found
print("explicit-bound check primes p≡1(8) <",N,":",cnt,"ok")
# (B) §4 construction with alphabet S={3,5}, p≡1(8) small
S=[3,5]; B=4
for v in S: B*=v**3
tested=0
for p in range(17,1200,8):
    if not isprime(p) or p in S: continue
    a=None
    for t in range(B):
        if t%4==3 and all(t%(v**3)==(4*v*v-p)%(v**3) for v in S): a=t;break
    qcount=0; q=a
    while qcount<3:
        q+=B
        if not isprime(q) or leg(q,p)!=-1: continue
        qcount+=1
        K=(p+q)//4; fK=factor(K)
        assert all(fK.get(v,0)==2 for v in S)
        s=[l for l,e in fK.items() if l%2 and e%2 and leg(l,q)==-1][0]
        assert s not in S
        U=(q-1)//2
        # H = <v^2>, index j: |H| = lcm of orders? compute subgroup generated by v^2 in cyclic group: order = lcm(ord(v^2))
        o=1
        for v in S: oo=mult_order(v*v%q,q); o=o*oo//math.gcd(o,oo)
        j=U//o; assert j%2==1
        target=pow((-s)%q,-j,q)
        # find nonnegative a_v with prod v^{2a_v} ≡ target (BFS over small grid)
        o3=mult_order(9,q); o5=mult_order(25,q)
        sol=None
        t9=1
        tab={}
        t=1
        for a5 in range(o5): tab.setdefault(t,a5); t=t*25%q
        t=1
        for a3 in range(o3):
            need=target*pow(t,-1,q)%q
            if need in tab: sol=(a3,tab[need]);break
            t=t*9%q
        assert sol is not None
        d=K*s**j*3**(2*sol[0])*5**(2*sol[1])
        assert (d+K)%q==0
        Aq=(K+d)//q; x=K; y=p*Aq; z=Fraction(p*K*Aq,d)
        cap=verify(p,x,y,z)
        bs=fK[s]
        pred=max((j-bs)//2 if j>bs else 0, sol[0]-1, sol[1]-1,0)
        assert cap==pred,(p,q,cap,pred)
        tested+=1
print("§4 construction verified exactly on",tested,"(p,q) pairs")
```

```python
# Extension (1): planted + free carriers for composite squarefree d ≡ 1 (8) with all primes ≡ 1 (8), then scaling to n.
import math
from fractions import Fraction
from check import isprime, factor, mult_order, verify
def jac(a,n):
    a%=n;r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in(3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
P=[p for p in range(17,400,8) if isprime(p)]
ds=[]
for i in range(len(P)):
    for k in range(i+1,len(P)): ds.append((P[i]*P[k],(P[i],P[k])))
ok=0
for d,(p1,p2) in ds[:300]:
    for mode in ("planted","free"):
        if mode=="planted":
            s=next(l for l in range(3,10**4,2) if isprime(l) and jac(l,d)==-1)
            q=next(t for t in range(3,10**9,4) if isprime(t) and (t-(4*s-d))%(s*s)==0)
            K=(d+q)//4; assert factor(K)[s]==1 and jac(s,q)==-1
        else:
            q=next(t for t in range(3,10**7,4) if isprime(t) and jac(t,d)==-1)
            K=(d+q)//4
            s=next(l for l,e in factor(K).items() if l%2 and e%2 and jac(l,q)==-1)
        assert math.gcd(K,d)==1
        j=mult_order(s,q)//2; assert j%2==1
        D=K*s**j; assert (D+K)%q==0
        A=(K+D)//q
        for n in (d, d*p1, d*p1*p2*p2):
            m=n//d
            x,y,z=K*m,d*A*m,Fraction(d*K*A,D)*m
            cap=verify(n,x,y,z)
            assert cap<=(q-3)//4
            ok+=1
print("extension(1) carriers+scaling verified:",ok)
```
