Result: The r-generic line has sterile points for every prime r ≥ 177505, and growing prime cores of every fixed norm form x²+Dy² give negative length-three witnesses for almost all primes in any fixed reduced progression inside 1 mod 4. Label: PROVED (computer-assisted relative to the SE/ZL inputs for the first result; relative to ring class field theory, Chebotarev and Bombieri–Vinogradov for the second)
Scope: An improved sufficient threshold, not sterility at 17 or Conj 4.2; the norm theorem is relative density one, not pointwise ES or a theorem on G_d(p). Conjecture 0.2 at q=3 is open. The inherited SE/ZL tables assume the documented accuracy of long-double libm; P rows 600–799 were not independently recomputed (ZL §2).
Review: cross-model (`PROOF_LIFT_REVIEW.md`, Opus, smart-mode replay and hostile review)
Triage: RECORD (sterility threshold only)
STATUS delta: propose replacing the §1D sterile-point sentence with “Sterile Mordell points on the r-generic line exist for every prime r ≥ 177505 (`notes/z76/PROOF_LIFT.md`).” Keep both §2.5 open targets unchanged.

## 1. Counting boxes, not ET data

For odd prime r put N=r^K, K odd, W=r^{(K+1)/2}. Use the covering theorem of `STERILE_EXPLICIT.md` (SE) §3.1 and the in-cell identities of SE §§1–2. A Type P datum has 4abd=N+e, a+b=ce, r∤abcd, all variables positive. With **ordered** (a,b) its box centre is −a/b mod W. Q-data have level k, k odd, and at most two boxes per unordered datum. If the sum of measures of these boxes is < (r−1)/(2r), some r-adic nonsquare gives a sterile point on the r-generic line; in particular no finite list of ET Prop 1.9 classes covers all sufficiently large primes having least QNR r. This is the prior implication; we improve the P-box upper bound. We do **not** improve the bound for the sum with multiplicities S(r) of SE.

**Compression lemma.** At fixed e let M=(N+e)/4, an integer prime to e, r∤M. Each box comes from a positive divisor h|M² in the class −M mod e. Indeed h=Ma/b=a²d; the congruence follows from a≡−b mod e and gcd(e,b)=1, and the centre is −h/M mod W. Thus one h contributes at most one box, even when many data give it. For any g|M the number of such divisors is at most

* τ((M/g)²) if g²≤e;
* 2τ((M/g)²) if g≤e.

Write each h as h₀h₁ with h₀|g² and h₁|(M/g)² (no coprimality needed, nor uniqueness). For fixed h₁ the allowed h₀ lie in one unit class; there is at most one integer in that class in [1,e]. For the second bound at least one of h₀ and g²/h₀ lies in [1,g]; each lies in a specified unit class. This proves both bounds, including e=1. The input gcd(e,M)=1 is SE Lemma 1.1(iv).

## 2. A short-interval upper bound using only integer arithmetic

Let 2^i ≤ e < 2^{i+1}, H=⌈2^i/4⌉, so M runs through at most H consecutive integers with M≤m=⌊(n+2^{i+1})/4⌋ whenever N≤n. We may count the whole interval before the unit filters. In each compression bound take g=gcd(M,G), with G a fixed wheel (largest successive lcm(1,…,l) before the first value >2^{⌊i/2⌋} or >2^i respectively). Fix k∈{3,…,7}. The multiplicative function τ((M/g)²) is at most M^{1/k}F(M), where at each prime ℓ, with α=v_ℓ(G), F(ℓ^j) majorises the running maximum, starting at 1, of

    (2 max(0,j−α)+1) / ℓ^{j/k}.

Take nondecreasing F rounded **up** in units 2⁻⁴⁰. Only finitely many levels increase: past α the unrounded successive ratio is ℓ^(−1/k)(2(j−α)+3)/(2(j−α)+1), decreasing. For ℓ≥3^k no increase is possible. Set F(1)=1, F=1*Δ via Dirichlet convolution. Δ is multiplicative with Δ(ℓ^j)=F(ℓ^j)−F(ℓ^{j−1})≥0. Thus the short-interval sum of τ((M/g)²) is bounded by

    m^{1/k} ( H ∏ℓ (1+Σ_{j≥1} Δ(ℓ^j)/ℓ^j) + ∏ℓ F(ℓ^∞) ).                    (1)

Indeed an interval of H integers has ≤H/d+1 multiples of d. The second product bounds the *total endpoint error*, once, not once per tuple box. Round upward again in both products (`major`); taking the minimum over k and the two wheel choices, then summing bands, gives `moment(n,j)` for e<2^j, counting **oriented boxes** already. This is a finite explicit upper bound, not an asymptotic estimate with a hidden short-interval constant.

## 3. Large shifts: a determinant on the integer lift

For e≥2^j order a≤b and double the box count. Now acd≤(N/e+1)/2, by e≤2b/c and 4abd=N+e. For n=2^B and a,d,c in dyadic intervals with lower endpoints 2^x,2^y,2^z, put s=x+y+z. Then s≤B−j−1 (j<B), and 2a²d≤N by SE Lemma 1.2. The trivial count is 2^s. For a fixed pair (a,d), e≤N/(2acd−1) by the same inequality and e≡−N mod 4ad; e determines b,c. This gives the last bound in `boxes`.

Each of three other pair routes uses the *integer* lift f=4acd−1, a divisor of each of N+4a²d, Nc+a, 4c²dN+1. Fix (a,d), (a,c), or (c,d), respectively. Then f=uz−1 with u fixed at 4 times the fixed product (here z is the varying integer, not its dyadic exponent). If M₀ bounds the fixed integer V divisible by f, u≥2^b and z∈[2^l,2^{l+1}), then f≥2^{b+l−1}. In a subinterval of width 2^t there are at most w−1 choices when for some 1≤h<w

    M₀^{h(h+1)/2} (2^t)^{w(w−1)/2} < (2^{b+l−1})^{hw}.                     (2)

Proof: remove from V all prime factors dividing u, giving V₁, choose v=u⁻¹ mod V₁. For w purported distinct z_i form an evaluation matrix at them with columns V₁^{h−j}(Z−v)^j, j=0,…,h−1, and Z^j(Z−v)^h, j=0,…,w−h−1. The i-th row is divisible by (uz_i−1)^h since uz_i−1 divides both V₁ and z_i−v. Its nonzero determinant is the Vandermonde times V₁^{h(h+1)/2}, contradicting (2). The degree and height cost here count actual divisors of a specified integer, not arbitrary lifts mod p. Partition the dyadic interval equally into power-of-two widths, or use the trivial bound. This is a pair-route variant of Coppersmith interpolation (SE Lemma 1.3), not a new determinant method. `divcap` implements (2) entirely with integer exponents. The three bounds on V in bits are B+2, B+z_c+2, B+2z_c+y_d+6, with z_c,y_d the lower dyadic exponents of c,d. They follow directly from the identities and 4a²d≤2N. Take the minimum *per box*, sum up through layer s≤B−j−1, double, and minimise the sum with (1) over j. The resulting integer bounds the number of distinct oriented P-boxes, for **every** N=r^K≤2^B in scope, not just primes r on average.

## 4. Sterile-line certificate

**Theorem.** For every prime r≥177505 there exists a sterile point on the r-generic line. This lowers the in-repo sufficient threshold 2^{21.4375} of `STERILE_LOWER.md` (ZL) Thm 6.3 by a factor of about 16. This is not an external priority claim.

*Proof.* Above the old threshold invoke ZL. Below it cover the log₂r interval [558/32,686/32) (⌈2^{558/32}⌉=177505). For each cell the level-1 count is ZL's exact joint sweep, all rows and no cutoff (existing octave-21 sweep with its 3534 correction for ad≤300). On levels ≥3 use SE's certified P,Q tables, ZL's P high extension to 800 bits, taking the **smaller** of twice the P table and §§1–3 when B≤100. We use units of 1/32 bit for table intersections; worst numerator over the cell, least integer r in the cell in each denominator. Grid operations, decimal table import with ZL's upward 10⁻⁹ pad, and the final sums are rational/integer. For the infinite tails use ZL Lemma 1.2: at log₂N≥800, D_P(N)/√N≤0.014 (all terms exponent ≤0.48); at log₂N≥100, D_Q(N)/N≤0.000010 (exponent ≤0.76). In both lists the log powers are ≤2 by construction in `zl_tail.py` (at most two harmonic-sum factors per product). For r≥4096 each P term normalised by √N, from one tail level K to K+2, has log ratio ≤ (−0.02+2/(800 ln 2))·2 ln r, since ln(1+v)≤v. This is less than ln(0.8); similarly the Q ratio using −0.24+2/(100 ln 2) is < ln(0.5). Start at the **actual** first tail level of r in each series. Summing the two tails therefore costs at most 0.16/⌊√r⌋ + 0.000040 including their box factors of 2. Counting partial cutoff cells also in the finite part only overcounts. See `scripts/z76_sterile.py`, `data/z76/sterile.txt`: 128 contiguous cells, maximum upper bound rounded **up** to ppm is 497526, less than the nonsquare mass. This proves the theorem. ∎

The saving in §1 comes from counting distinct ratios: the programme never charges the ordered τ₃(M) candidates separately at fixed e, nor a separate worst divisor count for each M. Neither independence of boxes nor a conjecture on sibling multiplicities enters. At r=17 the surviving cell-specific margin is much smaller and the bound does not bridge the gap from the known depths. For q=3 the elimination of balanced approximants at the *particular* polynomial point x*_c is already `FF_THIRDS_CORNER.md` Cor. 1.3; an upper bound for the mass on a whole slice cannot certify that particular point. We obtain no proof on either of these individual targets.

## 5. Dense binary quadratic cores: the opposite of the thin-core theorem

**Theorem.** Fix any positive integer D and any reduced prime progression contained in p≡1 mod 4. There is a fixed endpoint u (any prime u≡3 mod 4 with u∤2D works) such that the following holds. Given any boundary f(p)≥1 with log f(p)=o(log p), a relative-density-one set of primes in the progression has a length-three witness

    p=tuv−u−v,     tu−1=q=x²+Dy² ≥ f(p),     (q/p)=−1,

with t,u,v≥2 and x,y positive integers. In fact the number of distinct such q tends to infinity in probability. Here the core **is** the full word divisor and divides p+u, not a trivial square borrowed from the multiplier. Contrast z75 `PROOF_WILD2.md` §2: for exponent α<1 and any f→∞ the relative density is zero. A class-number-one assumption is unnecessary.

*Proof.* Let L be the ring class field of the order ℤ[√−D] (discriminant −4D). Away from 2D the primes represented by the principal form [1,0,D] are precisely those splitting completely in L (principal-form theorem of complex multiplication). The extension L/ℚ is finite Galois, unramified at u. The intersection with ℚ(ζ_u) is trivial since u is totally ramified in every nontrivial subextension of the cyclotomic field. Chebotarev in the compositum therefore gives a set Q of primes q splitting in L, q≡−1 mod u, of prime density δ=1/([L:ℚ](u−1)). In particular #Q∩[1,z]∼δ z/log z. For large q both coordinates can be taken positive: y=0 or x=0 yields no such prime q∤D. Discard all q dividing the fixed progression modulus m, u or 2D, and q≤2u. For any remaining q|p+u, p≡1 mod 4, put t=(q+1)/u and v=(p+u)/q. Then (q/p)=(p/q)=(−u/q)=(q/u)=−1 by quadratic reciprocity (u≡3 mod 4). If q<p, the endpoint v exceeds 1. This constructs the desired negative witness from a prime divisor of a single shifted integer.

For clarity on the growing cutoff, restrict to primes in the progression in (X/2,X], use Y=max(log X, sup_{X/2<s≤X} f(s)) over the integer domain of f (over primes if defined there). Then Y=X^{o(1)}. Count q∈Q in (Y,X^{1/5}] dividing p+u by Z(p). With B=Σ_q 1/(q−1), partial summation of the Chebotarev PNT gives B→∞: for arbitrarily large fixed H integrate over [X^{1/(5H)},X^{1/5}] to get δ log H+o_H(1). Uniformity in a growing H is not required. The mean of Z is B+o(1), and its variance is ≤B+o(1), with a negligible error even after multiplying the first-moment error by B. Indeed the diagonal is counted with modulus mq and distinct ordered pairs with mqq′; the simultaneous conditions select one reduced residue by CRT. Each pair modulus occurs at most twice. The Li main terms divided by the expected number of progression primes give exactly 1/(q−1), 1/((q−1)(q′−1)). The summed absolute errors in π(X) and π(X/2) are O_A(X/log^A X) by Bombieri–Vinogradov in its prime-counting form for every fixed A, since mX^{2/5} is below its range. Replacing the expected denominator by the actual prime count costs negligibly by the fixed-modulus PNT with log-power savings and B≪log log X. Chebyshev gives P(Z<B/2)=O(1/B); dyadic summation gives the ordinary relative prime density. ∎

This answers the dense-core question on the same density scale where z75 gave a no-go. It does **not** lower the pointwise ES exceptional set to zero: for instance by CRT any finite menu of these q can all be avoided by primes p≡1 mod 4, avoiding p≡−u mod q. Classical ES exceptional-set bounds are much stronger for unrestricted witnesses; §5 is about the *shape* of an almost-all witness, not an ES density record. For an odd square n and any q coprime to n the Jacobi symbol (q/n) is +1; the proof uses primes and their distribution. There is no 8-bridge here and no assertion of a Type II solution from a negative character at composites. No assertion of priority for the sieve or prime-ideal ingredients; it is the norm-core/word intersection that is being counted.

## 6. Replay (from the repository root)

```
(ulimit -v 1500000; timeout 600 bash -ec '
  gcc -O3 scripts/zl_sweep.c -lm -o data/z76/sweep.bin
  for j in 17 18 19 20; do x=$((1<<j)); ZL_SHORT=4 data/z76/sweep.bin $x $((2*x)) $((2*x+1)) 0 32 | diff - data/z76/l1_$j.txt; done
  rm data/z76/sweep.bin')
(ulimit -v 1500000; timeout 300 uv run --offline --no-project python -B scripts/z76_sterile.py 558 685) | diff - data/z76/sterile.txt
```

Optional tails: `(ulimit -v 1500000; timeout 240 env SE_W=40 uv run --offline --no-project python -B scripts/zl_tail.py P 32 800)` (likewise Q 16 100). Outputs `data/z76/tail_{P,Q}.txt`. Dependencies on reviewed finite-table and sweep code are as in ZL, not independent recomputations of the old tables. The combiner is new and uses exact arithmetic after import of those inputs. The small-shift and determinant proofs do not require floating-point estimates.
