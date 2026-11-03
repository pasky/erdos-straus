# P415 hostile cross-review — ACCEPT-WITH-FIXES

Reviewed `side-agent/z55-p415` at `069e2d599ab30dba2115cc5931d25ad76f0699ff`.
**ES remains OPEN.** The qualitative unconditional Theorem U survives, relative to the stated standard inputs.
The explicit Ω bounds and optimized levels do not become theorems. The required corrections below precede recording the memo.

## Per-claim decisions

| Claim | Classification | Finding |
|---|---|---|
| U, Step 1: parity reduction | CORRECT | Four surviving inert factors exceed x+4; zero or two remain, counting multiplicity. |
| U, Step 2: vector lower bound | CORRECT | NX's actual hypotheses, product, level and weighted remainder fit; details below. |
| U, Step 3: switched upper bound | CORRECT-WITH-FIX | Use (x+4)/a, not x/a; document the weighted BV and endpoint errors. The uniform bound is valid after this repair. |
| U, Steps 4–5: parameter choice | CORRECT | Positive main term ≍√η dominates O(η^(3/2)); no quantitative δ is established. |
| U: bounded even Ω; exchanged shifts | CORRECT | Size bound counts multiplicities; reversed switching uses modulus 32 and has the same fixed-constant estimates. |
| §1.4: δ≈.0315/.0138, Ω≤10/16 | CORRECT as Assessment | U/W/check reproduce; additional switched-distribution and constant assumptions remain unproved. |
| §2: sufficient-level ledger | CORRECT-WITH-FIX | E/L reproduce, but 0.9764 requires the GEH-type switched model; ordinary-EH/BV-switched figure is 0.9962. |
| §2(c): divisor-sum interpretation | CORRECT-WITH-FIX | r(N)>0 is not N∈S: p=41 gives N=45=3²+6² with an inert factor. Retain only a related weighted heuristic. |
| A1 and A1′ | CORRECT | CRT/character argument and finite factorization work; full-free-variable scope is essential and stated. |
| A2 and applications | CORRECT-WITH-FIX | Proof works; retain “nonconstant F” in its concluding Reading and use a generic linear plane through the origin for norm forms. |
| Prop C | CORRECT | Lemke Oliver's original Thm 1 explicitly supplies squarefree P₂ values; it does not assert composite outputs. |
| §4 quantitative aside | CORRECT-WITH-FIX | “≍√x/log x members” is not supplied by the citation; use the lower bound ≫√x/log x. “Positive-density” is also inaccurate. |
| §5 census and square controls | CORRECT | Full decisive census and independent small-bound factorizations agree; details below. |
| “narrowed”, with unconditional strengthening | CORRECT | One exact shift plus bounded anatomy is genuinely stronger than two roughly sifted shifts; P(4,15) and K(4) remain open. |

## Theorem U: source and step audit

1. **Vector input [S1].** Read v1 §§3.2–3.3 and §5, including the proof of Prop. 3.10; also compared the current v3 statement.
   Lemma 3.6 permits κ₁=κ₂=1/2 and β₁=β₂=1. Prop. 3.10 (3.12)–(3.14) gives precisely the stated bracket for sᵢ≥1,
   with remainder ∑_{d₁d₂≤D^(1+ε′)}τ(d₁d₂)^4|r(d₁,d₂)|. Fixed, possibly large S₀ meets sᵢ≪1 as x→∞.
   Its printed positive-valued codomain excludes zeros, but its own application has h(ℓ,ℓ)=0 for ℓ≥5.
   The proof uses nonnegativity, not strict positivity: empty incompatible divisor classes contribute zero throughout.
   Thus the memo's correction to [0,1] is justified, not an unproved extension of the application.
2. **Local arithmetic.** For q≥7 the two nonzero roots are distinct; q=3 has one common root of density 1/2.
   The joint survivor product divided by W(z₁)W(z₂) tends to (9/8)∏_{q≥7,q≡3(4)}q²(q−3)/(q−1)³>0.
   A2 holds with C₁=5; A3 follows from fixed-progression Mertens with dimension 1/2. No inadmissible local obstruction remains.
   The CRT modulus is 8l, l=lcm(d₁,d₂); compatible gcd(d₁,d₂) is only 1 or 3. Incompatible pairs have r=0.
3. **BV input [S2, Thm 3.4].** The source states max over all unit residues and all endpoints, up to x^(1/2)/log^B x.
   Grouping pairs by l gives only divisor-function weights. For E(l)=max_c|π(x;8l,c)−li(x)/φ(8l)|,
   Cauchy–Schwarz gives ∑τ(l)^j E(l)≤(∑E(l))^(1/2)(∑τ(l)^(2j)E(l))^(1/2).
   The trivial E(l)≪x/l and divisor moments bound the second square by x(log x)^O_j(1); BV supplies arbitrary savings in the first.
   Taking (1/2−2ε)(1+ε′)<1/2−ε therefore proves exactly the required weighted remainder. No EH input is hidden here.
4. **Switched sieve [S2, Thm 2.4, p.18].** Put Y=(x+4)/(mq). Then Y≥q≥x^(3/8), and all original p=mqq′−4 exceed w=x^(1/16).
   The root for p-primality is 4/a; the second is 15/(4a), distinct whenever both are unit roots. At 3 the second root is zero and can be omitted for an upper bound.
   Primes below w dividing a divide m∈S, so deleting their classes only reduces g. The undeleted envelope has dimension 3/2 and an absolute product-axiom constant.
   Ford's theorem actually needs only ∑_{d≤w}|r_d| for sifting to w; the memo's larger allowance d≤w² is harmless.
   Each r_d is bounded by 2^ω(d) times the maximal prime-progression error at modulus 8d. Weighted BV applies since 8w²≪Y^(1/2)/log^B Y.
   Consequently each (m,q) costs O_A(Y/log^A x), uniformly in a; summing gives O_A(x(log x)^(2−A)).
   Use li(Y)/4 as the progression main term; replacing it by π(Y)/4 costs a negligible PNT error.
   The product factorization is correct. Replacing the truncated compensation for primes dividing m by the full h(m) only enlarges the upper bound.
5. **Mean value [S3, original pp.162–163, Thm 1].** Set H(n)=1_S(n)h(n). Then H(ℓ^j)≤4/3, H(n)≪_εn^ε,
   and ∑_{ℓ≤t}H(ℓ)/ℓ=(1/2)log log t+O(1). Shiu with a=1, k=4, y=t proves ∑_{n≤t}H(n)≪t/√log(2t).
   This verifies the needed bound directly; separate Wirsing/Halberstam–Richert alternatives are unnecessary.
6. **Switching integral.** PNT in the fixed progression and partial summation give the displayed α-integral;
   ∫_θ^((1−β)/2)dα/[α(1−β−α)]=log((1−β−θ)/θ)/(1−β).
   The decreasing m-weight permits the preceding cumulative mean bound. With fixed η=1−2θ, the m=1 term and endpoint terms are lower order as x→∞.
   Hence T₁≤XW(z₁)W(z₂)[K₂η^(3/2)+o_{η,δ}(1)], with K₂ absolute. The bound C(θ)≤16η^(3/2) follows exactly as written.
7. **Closing the argument.** [S1, §5] gives f(s)=F(1)s^(−1/2)arccosh√s and the stated delay equations.
   The standard beta-sieve properties F≥1≥f, F decreasing and F−f→0 yield bracket ≥F(1)(√(η/2)/2−√η/100)>0.3F(1)√η.
   Indeed s₁−1=η/(4θ)≥η/2. Choose η small against K₂, then fixed S₀, δ=η/(8S₀), ε=η/16; δ≤1/128.
   All x-limits follow these choices. The positive lower bound is ≫x/log²x; Ω≤log(4x+1)/(δlog x) and evenness follow immediately.
   For the exchanged version, use 4p+1=mqq′≡5 (32), p=(aq′−1)/4, with second numerator aq′+15; only fixed constants change.

## Required fixes, in priority order

1. In U Step 3 replace every switched cutoff x/a by (x+4)/a. Alternatively retain an explicit O(1) loss for p∈(x−4,x].
   State the divisor-weighted remainder and fixed-parameter o(1) as above; these repairs do not weaken U.
2. Throughout §§0, 2, 8 distinguish **0.9962 (ordinary EH main sieve, BV switching)** from **0.9764 (additional GEH-type switched model)**.
   Do not call the latter an established sufficient value for HCKILL's ordinary-EH θ₀. Neither optimized number is audited as a theorem.
3. Correct the r-weight/exact-S conflation, the unsupported two-sided P₂ count, and “positive-density” (use “near-linear-count”).
   Carry nonconstancy into A2's Reading; the actual lemma already includes it.
4. Preserve the model-only labels on explicit δ/Ω bounds and the limited full-family scope of algebraic exclusions. No ES conclusion follows.

## Numerical reproduction

All shell runs used `ulimit -v 6000000` and explicit timeouts; Python used `uv`. No dense unbounded arrays were used.
U/W outputs match stored files byte-for-byte; check reproduces the Buchstab identity and F/f values. The independent auxiliary reviewer reran E/L byte-for-byte.
Full prime census at 10¹⁰: 113,758,759 primes, 22,280,854 with N₁∈S; conditional Ω=0,2,4,6,8,10 counts
**7,962,940; 12,902,238; 1,378,173; 37,005; 496; 2**, exactly matching the memo (65.42 s; 112,880 KiB RSS).
All stored smaller prime bounds, the integer census at 10⁹, and 50,000 odd squares at 10¹⁰ reproduce; zero square exceptions.
Independent SymPy factorization at 10⁵: prime total 2,384, N₁∈S total 635, Ω histogram (295,325,15);
integer total 12,500, N₁∈S total 4,814, histogram (2518,2216,79,1). These match the C program independently.
I checked the auxiliary review's key source, algebraic reasoning and census code; its conclusions are not accepted solely on delegation.

## Sources actually opened

- [S1] [Nath–Xie, arXiv:2501.16723v1](https://arxiv.org/pdf/2501.16723v1), pp.8–13 and 23; also v3. FI Thm 11.12 and (14.2)–(14.3) checked **as quoted here**, as the memo specifies. Direct AMS book access returned 403; no independent inspection of those book pages is claimed.
- [S2] [Ford, Sieve Methods (2023)](https://ford126.web.illinois.edu/sieve2023.pdf), product axiom and Thm 2.4, p.18; BV Thm 3.4, p.35.
- [S3] [Shiu, original article](https://eudml.org/doc/152201), GDZ scan of J. reine angew. Math. 313 (1980), pp.161–163; [theorem page image](https://images.sub.uni-goettingen.de/iiif/image/gdz:PPN243919689_0313:00000167/full/1400,/0/default.jpg). Also cross-checked Pollack's quotation, Theorem A.
- [S4] [Lemke Oliver, original author PDF](https://lemkeoliver.github.io/papers/04-Quadratic.pdf), P₂ definition p.1, Theorem 1 p.2, quantitative lower-bound discussion p.3.

**Final verdict: ACCEPT-WITH-FIXES.** No fatal gap found in qualitative U relative to its cited inputs. The narrowed verdict is justified; the numerical model and exact P(4,15) remain unproved.
