# Hostile review of §76 and the unpruned three-quarter route

**Verdict: SOUND-AFTER-REPAIRS.** The weighted-moment/Cauchy–Schwarz argument survives independent calculation; I found no counterexample or irreparable mathematical gap in the exceptional-set implication. The submission is **not SOUND as written**: its promoted label carries an unsupported review-count/independence claim (HIGH), and its proof and dependency descriptions need the MEDIUM repairs below. This verdict does not certify external validation, novelty, or the claimed independence of previous agents.

Reviewed snapshot: `59c718b`, exclusively in `/tmp/es-sec76`. I read all 1,400 lines of `paper/es-threequarter-note.tex`, the previous standalone review, all of notes §76, §39.7, the §41 protocol/verdict, and the second-moment/pruned-supply argument in §34. No changes to the notebook, TeX source, or verifier are made by this review.

## Numbered defects and exact repairs

1. **HIGH — unsupported provenance for the promoted label.** Locations: TeX lines 24, 45–48, 73–79, 1307–1310; notes §76 status and §76.6(1). The cited artifacts do **not** document “three independent maximum-severity internal reviews of the chain.” §39.7 explicitly calls itself **Self-review**, with a list of steps needing a referee. §41 is a blind construction/reconciliation, explicitly takes Theorem 34.8 as an input rather than re-proving it, and makes blindness a self-attestation. The standalone review explicitly says it is not blind. §76.4 supplies a further internal re-derivation record, not independent evidence of its isolation. These are worthwhile checks, but relabelling their number, type, scope, and independence is not justified. The previous standalone audit also says SOUND-AFTER-REPAIRS; “no load-bearing gap found” must not be confused with “no defects found.”

   **Exact repair:** replace the date with `\date{INTERNALLY PROVED; internal checks only, not externally refereed}`. Replace the review-history paragraph in Theorem 1.1 with:

   > The internal record comprises a self-review (notes §39.7), a blind construction and reconciliation taking Theorem 34.8 as input (notes §41), a standalone internal audit (`reviews/es-threequarter-note-review.md`), and a checkpoint re-derivation (notes §76.4). The standalone audit found no load-bearing gap and recorded repairs. The blindness of the §41 construction is self-attested, not independently audited. These records are not three independent full-chain hostile reviews, and the theorem has not been verified by an external expert.

   Use the same account in §76, the abstract and Section 11; replace their numerical/independence claims with:

   > The argument has undergone the internal checks described in Theorem 1.1; these do not constitute external refereeing.

   An “internally proved” label can describe the repaired mathematical argument, but cannot be justified by the currently asserted review history. This HIGH finding concerns that rationale, not a disproof of the bound. Do not retroactively erase the historical provisional status in §§39.7/41.

2. **MEDIUM — Lemma 5.1/76.1 invokes Shiu at the excluded modulus 1 and omits the last-box convention.** Locations: TeX 635–647; notes 29597–29617. The displayed input (10) requires `q>=2`. Since `1 in J` in every application to Theorem 5.2, the pair `(k,k')=(1,1)` necessarily gives `d=1`. Section 3's explicit modulus-one treatment covers two different functions, not this new F. The convolution argument later in Lemma 5.1 readily fills the omission, but must be applied to the inner sum too. Also the full boxes described as subsets of `(H,z]` do not generally cover its terminal remainder.

   **Exact repair:** replace “Apply (10) ... in each box ... subset of (H,z]” by:

   > Cover `(H,z]` by consecutive boxes `(U,(1+1/20)U]` starting at `U=H`, enlarging the last box when necessary. For `d>=2`, apply (10) to `F(n)=2^{omega(n)}n/phi(n)` in these full boxes. For `d=1`, the nonnegative convolution `F=1*h` below gives `sum_{n<=V} F(n) << V log V`; hence each box contributes at most `U^{-1} sum_{n<=(21/20)U} F(n) << log U`. This is the same desired estimate, since `phi(1)/1^2=1`.

   Retain the following local-factor calculation for `d>=2`. All enlarged endpoints are at most `(21/20)z`, which does not affect any logarithmic bound. Apply this repair in both texts. The case `J={1}` then has a complete proof without appealing to a version of Shiu not stated in the paper.

3. **MEDIUM — the literal dependency claim and “verbatim/same parameter order” claims are false as written.** Locations: TeX 105–116, 716–742, 826–841, 1015–1020, 1338–1343; notes Corollary 76.3 and §76.4(ii). The cutoff is used in Lemma 3.3, the retained-main-mass argument of Theorem 4.2, and the **separate lower `W_k` proof of Lemma 6.1**, not only in (26). Pruning likewise has a retained-mass calculation (24), not just (26). The new route does avoid all those uses for the main theorem, but only after replacing the whole supply argument and choosing the conditional-independence moment proof. The original D-dependent parameter declarations and references to the pruned lower bound do not hold literally “verbatim” for a D-free proof. Notes additionally include Lemma 6.1 in the claimed verbatim D-free list; the paper correctly omits it. Finally, the full checkpoint (ii) is not “bypassed entirely”: the lattice estimates, all-fibre quantifiers, and selector/bad-fibre argument remain necessary.

   **Exact repair:** replace the opening dependency explanation in both corollary proofs by:

   > In the original route, the cutoff and congestion threshold are used to establish low-omega mass, control retained main-term mass, and bound the BV multiplicity. The optional lower-`W_k` calculation in Lemma 6.1 also uses the cutoff. Theorem 5.2 replaces the entire pruned-supply argument. The proof of the main theorem then uses only the conditional-independence proof of Theorem 6.3, not Lemma 6.1 or the ordered-atom replay.

   In the notebook substitute “Theorem 76.2” for “Theorem 5.2.” Delete `Lemma 6.1` from the notebook corollary's list of statements needed for the D-free chain. Replace “hold verbatim” with:

   > hold with `A_X` replaced by `A'_X`, Theorem 4.2 replaced by Theorem 5.2, the references to a pruned lower estimate replaced by the unpruned supply estimate, and D deleted from all parameter dependencies

   (again use Theorem 76.2 in notes). Replace “same parameter order” by “the same order for the surviving parameters, with D and its dependencies deleted.” Append to the Section 1 parameter paragraph:

   > This D-dependent list describes the retained original route. For the simplified route of Section 5, omit D and its choice, use the family `A'_X`, and delete D from all dependencies. The remaining choices occur in the same order: kappa, K_0, eta and the void constant, B, D_B, C_0, and alpha.

   Replace “checkpoint (ii) can be bypassed entirely” and the corresponding Section 11/§76.4 wording by:

   > The pruned-supply component of checkpoint (ii) is replaced by the weighted moment and Cauchy–Schwarz/BV argument. The elementary lattice estimates, the `J_c` quantifiers and fibre bounds, and the selector's exponentially small bad-fibre estimate remain required.

   These repairs change the dependency account, not the resulting exponent or the validity of the downstream bounds.

4. **MEDIUM — incomplete stated scope of the distinctness argument.** Locations: TeX 656–658; notes immediately before Theorem 76.2. The assertion that distinctness “uses only” the upper cutoff, coprimality and divisibility omits the essential **lower floor relative to K**. The actual Lemma 2.2 proof does use `4uv>4H^2>K`; it does not use the omega cutoff. Without the floor, `(k,u,v)=(1,2,3)` and `(25,2,3)` at `ell=71` satisfy both divisibilities and give the same residue 23, even with `u,v<=4` and `4^2<71`.

   **Exact repair:** replace the parenthetical explanation in both places by:

   > whose distinctness argument uses coprimality, `u,v<=z_j` with `z_j^2<ell`, `H<u,v` with `4H^2>K`, and `4uv | k ell+1`, but no omega cutoff

   There is no collision in the theorem's actual range. This is a false scope description, not a counterexample to Lemma 2.2 or Theorem 5.2.

5. **MEDIUM — nonexistent lemma reference in Corollary 76.3.** Location: notes line 29710: `[TQ, Lemma 3.4] (low-omega mass)`. The compiled label `lem:omega` is **3.3**, not 3.4; inserting Section 5 did not change Section 3's theorem numbering.

   **Exact repair:** replace `[TQ, Lemma 3.4]` with `[TQ, Lemma 3.3]` there. The corresponding TeX uses a symbolic reference and is correct.

6. **LOW — ambiguous claim to remove “the second incidence moment.”** Locations: abstract 43–44 and Corollary 5.3's heading. The simplification introduces and uses a *weighted* second incidence moment. It removes the old unweighted lemma/pruning device, not second moments altogether.

   **Exact repair:** in the abstract replace “the second incidence-moment lemma” with “the unweighted incidence-moment lemma (Lemma 4.1).” Replace the corollary heading with `the theorem without $D$, pruning, or Lemma~\ref{lem:congestion}`. The notebook's more specific “Lemma 34.7 as a pruning device” is already appropriate.

7. **LOW — the toy replay's scope should be explicit.** Locations: notes §76.5(iv), verifier comments 15294–15297. The replay retains `Hh=1` from part (ii); it does not use `H=5^10`, which would make this slice empty. It enumerates prime progressions and checks distinctness, but does not itself compute the prime-first left side independently. Also distinctness is needed to identify triple counts with *class* counts, not for the interchange of two finite triple-counting sums.

   **Exact repair:** replace the end of §76.5(iv) by:

   > With `H_toy=1`, `x=2*10^5`, `floor(x^{1/6})=7`, `K=5`, `J={1,5}` and `c=2`, the code enumerates the progression side of the triple-counting identity and checks that the resulting classes at each prime are distinct. The comparison to the logarithmic-integral main term is informational, not an asymptotic test in the theorem's `H=K^10` range. Distinctness makes the same count a class count.

   The present fixed run has no endpoint or arithmetic bug. For a reusable progression iterator, use `start = x + 1 + ((int(a) - (x + 1)) % q)` rather than permitting the endpoint `x`. Here `x` is composite (and incompatible with these reduced odd classes), so this latent endpoint issue does not change the run.

8. **LOW — the PDF build is not warning-free.** TeX 700–705 produces an overfull hbox of **17.91861pt** at line 705. Both LaTeX passes complete and the PDF has 21 pages, but “built cleanly” should not mean zero box diagnostics.

   **Exact repair:** replace that display by an `aligned` display, breaking after the weighted double sum:

   ```tex
   \[
   \begin{aligned}
   \sum_qW_c(q)^2E^*_x(q)
   &\ll\frac{x}{\log x}
   \sum_{\substack{H<u,v\leq z\\(u,v)=1}}
   \frac{2^{\omega(uv)}r_{\J}(u,v;c)^2}{\varphi(4uv)}\\
   &\ll\frac{x}{\log x}(\log z)^4(1+\log K)^3
   \ll x\,t^6.
   \end{aligned}
   \]
   ```

## Independent mathematical audit

### Weighted second incidence moment

- If `u,v` are coprime and odd, `phi(4uv)=2phi(u)phi(v)`. If exactly one is even, the ratio is 4. Both cannot be even. Thus the stated inequality and parity explanation are correct, including `u=1` or `v=1`.
- Expanding `r_J^2` gives ordered pairs `(k,k')`, with `d=lcm(k,k')<=K^2` and `(c,d)=1`. If a prime divides `v` and `d`, it also divides `u`, a contradiction. Hence `(v,d)=1`; now `-cv mod d` is reduced, and `(u,d)=1` follows too. Dropping `(u,v)=1` only **after** factoring `2^{omega(uv)}` and comparing totients is legitimate. The retained positive product weight defines the enlarged sum.
- `F` is nonnegative and multiplicative. For every `a>=1`, `F(p^a)=2p/(p-1)<=4<=4^a`. Also `F(n)<=4^{omega(n)}<=tau(n)^2 <<_epsilon n^epsilon`, proving the requisite growth condition without growing parameters.
- For `d>=2`, set Shiu's endpoint `V=21U/20`, length `Y=U/20`, and `alpha_s=beta_s=1/4`. Since `d<=K^2<=U^{1/5}`, both `d<Y^{3/4}` and `V^{1/4}<Y` hold uniformly for sufficiently large absolute `K_0`. Every prime dividing d lies below V. Enlarging the last box is essential and harmless. The omitted `d=1` case is covered by defect 2's elementary argument.
- `sum_{p<=V} F(p)/p = sum 2/(p-1) = 2 log log V+O(1)`. The logarithm of the local-factor ratio is

      sum_{p|d} [-2/(p-1) - 2 log(1-1/p)] = sum_{p|d} O(p^-2).

  The convergent error proves two-sided comparability uniformly in d, not just an upper bound with a hidden `log log d` loss. Shiu gives a box sum of F at most `C U log U phi(d)/d^2`; division by U gives precisely the claimed harmonic/totient box weight.
- There are `O(log z)` boxes. For the outer sum, `h(p)=F(p)-1=(p+1)/(p-1)` and **`h(p^a)=0` for all `a>=2`**, since consecutive F prime-power values agree. Therefore

      sum_{n<=V} F(n) <= V product_{p<=V}(1+h(p)/p) << V log V,

  because `h(p)/p=1/p+O(p^-2)`. Partial summation gives `sum_{n<=z} F(n)/n << (log z)^2`. No extra logarithm is missing.
- Writing `k=ga`, `k'=gb`, `(a,b)=1`, gives

      sum_{k,k'<=K} phi([k,k'])/[k,k']^2
        <= sum gcd(k,k')/(kk')
        <= sum_{g<=K} (1/g)(sum_{a<=K/g}1/a)^2
        << (1+log K)^3.

  Thus Lemma 5.1's exact claimed powers and absolute constant are justified after defect 2.

### Unpruned supply and its quantifiers

For every admissible triple, k is odd and `(uv,k)=1`, so `(k,4uv)=1`. The equivalence `4uv | k ell+1` iff `ell=-k^{-1} mod 4uv` is exact, and that residue is a unit. Interchanging the finite sums counts each triple-prime pair once. Lemma 2.2, with its lower floor retained, makes it a distinct-class count as well. No cutoff is used in that lemma.

The main term is at least `x Lambda^2 h(J)/(16 log(2x))`: use `li(2x)-li(x)>=x/log(2x)`, `phi(4uv)<=4uv` and (11). Here `Lambda>=0.5 log z` and `log z=(log x)/6` with `log x` between `t/2` and `t`, so it is `>> x t h(J)` uniformly.

A positive integer m has exactly `2^{omega(m)}` ordered coprime factorizations (including m=1). Imposing both box bounds only removes factorizations. Consequently `W_c(q)^2 <= 2^{omega(q/4)} sum_{4uv=q} r_J^2` is correct for the *restricted* sums in the paper. Multipliers contribute through r, not through an extra unaccounted factor K.

BT at endpoint `2x` gives `E_x^*(q)<<x/(phi(q)log x)` for all `q<=4x^{1/3}` once x is sufficiently large, since `log(2x/q)>=(2/3)log x-log 2`; subtracting `pi(x;q,a)` only decreases the progression upper bound. The logarithmic-integral main term obeys the same bound. Therefore

    sum_q W_c(q)^2 E_x^*(q)
      << (x/log x)(log z)^4(1+log K)^3 << x t^6.

The other factor in weighted Cauchy–Schwarz is BV with fixed `R=26`, at most `C x t^-26`. The error is `O(x t^{3-13})=O(x t^-10)`. The extra condition `1 in J` gives `h(J)>=1`, so this is uniformly negligible even for the sparsest permitted family. All moduli are eventually below `x^{1/2}(log x)^-A_26`; the threshold may depend on kappa, but never on c, J, the particular K, or the block. Dividing lower counts by `2x`, upper counts by x, using `asymp t` full blocks and enlarging a partial final block proves the theorem. Constants do not depend on a choice of representative of c.

### Downstream proof, checkpoints, and scope

For every c, an active atom has a unit residue modulo k, so its multiplier lies in `J_c={(k,c)=1}`. This family contains 1 and c is reduced modulo its lcm, however nonreduced c is modulo the full `L_K`. Theorem 5.2 supplies its lower fibre mass, while BT and (12) supply the upper bound `mu_c<=C t^3` without any cutoff. Thus the actual content of Corollary 5.3 is sound.

Given c and the selector, the distinct large-prime coordinates remain independent and uniform in the exact CRT probability space. Same-prime distinctness makes `H_X` a sum of Bernoulli variables, hence its m-th falling factorial moment is bounded by `mu_c^m` for every m with a fixed base constant. Lemma 6.1 is not required for this argument: checkpoint (i)'s assertion of non-load-bearing status for the main implication is correct. The independent ordered prime-power table also checks out: for shared exponents it is `p^{min(e,f)-e}`, and the residue cancellation leaves `p/(p-1)` only at unselected shared primes.

The selector calculation still matters. On supported primes `p>y`, divisibility of c is independent with probability `1/p`. Its exponential moment is bounded by `exp((e-1)y sum_{p>y}p^-2)=O(1)`, and the lost multiplier mass is at most `2(log K)Z(c)`. Choosing eta then B makes bad fibres exponentially rare on the `t^3` scale. On the remaining fibres the lower mass gives the required void bound. These arguments hold unchanged in substance for the larger family, with the substitutions specified in defect 3.

The inventory `|A'_X|<=K X^(4/3)` counts choices of k, ell, u, v before imposing *any* arithmetic condition; it is unaffected by removing the cutoff. The even Bonferroni identity, upper factorial moments, degree `r asymp t^3`, selector expansion, and exact `N/q+O(1)` counts give the same `exp(O(t^4))` ledger, with no `L_K`-fibre enumeration. The Rankin transfer to all denominators is valid: `delta u<=eta_0 u^(3/4)` for `u<=log x` bounds the Euler product uniformly. No prime-distribution error is used at scale N. I found no mathematical obstruction to the main exponent here.

The §76.4 statement that its checks found no load-bearing gap can be retained as a bounded internal record, not as independently verified review provenance. It needs the more precise scope in defects 1–3: its proposed simplified proof had the modulus-one omission, and the full selector checkpoint has not disappeared. The repeated “All correct” does not excuse the inaccurate dependency and distinctness descriptions.

## Computations and build audit

1. **Requested isolated `(bx)` run: PASS**, 7.74 seconds. Exact output values:

       phi parity cases (odd, even): (18233, 36562)
       weighted-moment normalized range (rounded): (0.0029, 0.0030)
       pair-sum ratios K=100,200,400,800: 0.1284, 0.1216, 0.1165, 0.1123
       prime incidences: 18332; main term: 18203.4; collisions: 0

   The integer r/W/CS checks and totient sieve are correct. Moment/pair-sum/main-term ratios are floating-point informational calculations, not exact asymptotic estimates. The code additionally asserts loose finite bounds on those ratios; it does not establish an asymptotic constant. Its phi array reaches 640000 and covers all lcm accesses for K<=800.

2. **Independent prime-first enumeration:** I enumerated primes in `(200000,400000]` first and tested `(k ell+1) % (4uv)==0` directly, independently of the verifier's progression enumeration. There are 25 admissible triples with `H_toy=1,z=7,J={1,5},c=2`. Their counts are 16654 for k=1 and 1678 for k=5, totalling **18332**, at 4824 occupied primes; the maximum class count at a prime is 22. Every per-triple count agrees with the residue-progression count, and every per-prime residue list is collision-free. The exact main-term coefficient is **55/48**, giving `18203.361233345513` and ratio **1.0070667589905782**. Thus this is a correct finite instance of the counting identity and distinctness mechanism, though not of the theorem's asymptotic parameter regime.

3. **Independent exact convolution:** checked `F(n)=sum_{d|n}h(d)` with rational arithmetic for every `1<=n<=1000`, including repeated prime powers: PASS. Also computed the omitted-floor collision in defect 4 directly.

4. **Existing bounded CRT companion rerun:** `uv run python reviews/es-threequarter-note-check.py`: PASS, with 3014 profile counts, 120 prime-power relative probabilities, 404550 exact CRT residues/150 fibres and moments through order 7, 4221 Bonferroni inequalities, and 5620 rounding cases. This is a rerun of a prior author's finite companion, not new independent proof provenance.

5. **LaTeX:** two `pdflatex -interaction=batchmode -halt-on-error -jobname=wave32-sec76-review` passes: PASS, **21 pages**. The final log has **no undefined references/citations**; there is the overfull hbox in defect 8. Static checking finds **80 unique labels, 120 reference uses, 19 citation uses**, all resolved, and **zero percent characters in the new Section 5**. No silent percent-comment deletion is present. The TeX contains no remaining “provisional” text. Its symbolic Section references resolve correctly to Sections 6–11; explicit numerical Section references concern the separately cited LL note and are not stale internal references. The notebook's equation references (30)/(31), inventory (48), and Section 9/10/11 targets agree with the fresh auxiliary file; the erroneous Lemma 3.4 is listed above.

6. **Status/effectivity wording:** the title and main theorem distinguish the exceptional-set bound from the conjecture, and external/priority disclaimers remain. “Constants are not asserted to be effective” is appropriate for the stated BV input; the paper does not claim an effective numerical threshold. No additional objection to these qualifications is warranted.

All Python checks are memory-bounded. An initial attempt to put the *uv launcher itself* under a 1 GiB address-space cap failed during its Rayon worker-pool initialization before running the check. I inspected that failure, limited launcher threads, and instead capped the Python process at 1 GiB (512 MiB for the independent small checks); those runs passed. No dense Cartesian-product arrays or unbounded geometry routines were used. `git diff --check` passes.
