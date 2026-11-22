# Second hostile cross-lab review (Claude Opus, `smart`) of the z81 cap records

**Scope.** `notes/z81/CAP_ZERO.md` §1 (Lemma I and Theorem I) and §5 (Theorem V), and `notes/z81/SPECIFIC_CLASS.md` §8
(Theorem C1), as they stand at `0a08080ce`. Both lanes were written by GPT-6.2 Astra (`deep`). I audited the proofs from
scratch, line by line. I read the earlier Opus reviews (CAP_ZERO R1–R3, SPECIFIC_CLASS R4) only after finishing my own
audit, to compare verdicts. **ES in ℕ is open.** Nothing below proves ES, an infinite case of ES, or any bound on the
integral exceptional set. Every statement here concerns the cap relaxation ES^{(y,e)} of `EXSET_LINNIK_CAPS.md` §1.

## Verdicts

| item | verdict | summary |
|---|---|---|
| (a) CAP_ZERO Lemma I + Theorem I (prime-power root at all three QR rates) | **ACCEPT** (wording nits only) | algebra exact; every analytic step checks; z80 citations match; no circularity |
| (b) CAP_ZERO Theorem V (4/5 at cap 1; (3/4, 1/4) for root 1 or prime) | **ACCEPT-WITH-FIXES** (wording/scope only) | packet, distinctness, masses, BV incidence, transfer and optimisation all check |
| (c) SPECIFIC_CLASS Theorem C1 (4/5 at cap 1) | **ACCEPT** (one export caveat) | composite-input valuation dictionary, (10), BV incidence and transfer all check |

I found no mathematical gap. All the fixes requested below concern wording, scope or export, not mathematics.

---

## (a) Lemma I and Theorem I

### Lemma I algebra (verified by hand and replayed)
* **Window.** m₀ is a product of an odd number of primes ≡3 (4), so m₀≡3 (4). Also p≡1 (4), so 4 | p+m₀. From m₀≡−p (s)
  we get s | p+m₀.
* **Lift.** F=s²−s+1 satisfies F≡1 (4) (because s≡1 (4)), F≡1 (s) and F≡1−s (s²). If s² | p+m₀, then
  p+m₀F ≡ (p+m₀) − s·m₀ ≡ −s·m₀ (mod s²). Here s∤m₀, because m₀≡−p≢0 (s); note s≠p since (s/p)=−1. Hence v_s(p+m)=1
  and s∥K. Divisibility m | s^h+1 holds because 3 | h and h is odd, so F | s³+1 | s^h+1, and gcd(m₀,F)=1.
* **p∤m.** No t equals p, since t≡3 and p≡1 (mod 4). If p | F, then s³≡−1 (p), so ord_p(s) | 6. But a quadratic
  nonresidue mod p has v₂(ord_p s)=v₂(p−1)≥3. This is a contradiction. Then 4K=p+m gives gcd(K,pm)=1.
* **Identity.** 1/(pA)+d/(pKA) = (K+d)/(pKA) = m/(pK), and 1/K+m/(pK) = 4K/(pK) = 4/p.
* **Root.** z=pA/s^h with A=K(1+s^h)/m, so v_s(A)=1+0−0=1. Hence the reduced denominator is exactly s^{h−1} and
  r=s^{(h−1)/2}. Also s | A | y and (r,p)=1. ✓

### Theorem I, step by step
1. **Supply.** The indicator [2d|t−1]−[4d|t−1] selects t≡3 (4), t≡1 (d) for odd d. Its main coefficient is
   1/φ(2d)−1/φ(4d) = 1/(2φ(d)). The moduli jd₁ with j∈{2,4} sit inside z80 §10's Maynard boxes (there j≤24), with the
   same fixed residue 1. The rest of z80 §§10/12 (the m-fold products of (15), the common t₀, the multiplicity
   τ(d)=y^{o(1)}, log L ≪ z+log y) carries over unchanged. CAP_ZERO needs no quartic colour split, which is a
   simplification. Since t−1 | L=t₀L₀² and (t−1)/2 is odd, (t−1)/2 | L_odd | h. I checked z80 `BEYOND_34.md` (15):
   log z ≈ (10⁴/B′)·log U·log₃U/log₂U. This gives the stated log(1+e) ≤ log 3h ≤ exp((c+o(1))·log U·log₃U/log₂U).
   **Citation match ✓.**
   *Montgomery branch.* Here L=t₀L₀, using one box. Primes t≡7 (24) are ≡3 (4), and (t−1)/2 = 3·odd divides h. The
   modulus 24d is a multiple of 24 and lies below x^{(1+a)/2}, as z80 §12 requires. The resulting P ≥ Y^{1/2+4γ} needs
   no colour halving. ✓
2. **Carrier.** Fix one reduced class mod 4p with s≡1 (4) and (s/p)=−1. At X=R^D ≥ p^D, the z80 §11 TZ/Stark argument
   gives ≫X/((4p)² log X) ≥ X^{.999} primes. *Optional simplification:* IK Cor. 18.8 (Linnik with
   π(x;q,a) ≫ x/(φ(q)√q log x) for x ≥ q^L) gives the same count with no exceptional-zero case analysis.
   *GRH branch.* One only needs the character χ_p to take the value −1. The error is √X·log²(4pX) against a main term
   ≍X, with X=(log R)^D and D>4. This is Ankeny-type and correct, even though p may be as large as R. At most log R/log 2
   primes divide R, which is negligible. ✓
3. **Large sieve.** a_n counts ordered l-tuples, so Σa_n² ≤ l!·P^l. The moduli are primes s≤X, and every nonprincipal
   character is primitive. The length is (2Y)^l ≤ X². So the number of bad s is at most 2X²·l!·P^l/(P/10)^{2l} ≤
   2X²(100l/P)^l. Numerically, P^l = X^{1.008−o(1)} and (100l)^l = X^{1/5000+o(1)}, so the count is X^{.9922+o(1)}. This
   is below X^{.997}, consistent with the note's "≤ 2−2(.503)". In the Montgomery branch the count is
   X^{1−7.9γ+o(1)} < X^{1−5γ}. ✓
4. **Selection of the t.** Every t ≤ 2Y < √X < s. Since s≡1 (4), reciprocity gives (s/t)=η(t)=−1. Because
   ((t−1)/2)·odd = h, s^h ≡ −1 (mod t). The count satisfies |T₋| ≥ (P−P/10)/2 − O(log X) ≥ .44P. For χ∉{1,η}, χη is
   nonprincipal, so |Σ_{T₋}χ| ≤ .1P+O(log X). ✓
5. **Fourier inversion.** For |z|=1, |(1+z)/2| = √((1+Re z)/2) ≤ exp(−(1−Re z)/4). So every nontrivial coefficient is
   ≤ e^{−.0825P}, and the η coefficient is exactly 0. Since (s−2)e^{−.08P} < 1 (P ≥ U^{5040}, log s ≤ DU), every unit
   class is hit. η(−p) = η(p) = (p/s) = (s/p) = −1, so every subset hitting −p has odd cardinality, hence is nonempty and
   ≡3 (4). Squarefreeness and the exclusion t∤F give gcd(m₀,F)=1. **All hypotheses of Lemma I hold.** ✓
6. **Radical reduction.** Scaling by n/p keeps x and y integral and gives z′=nA′/s^{h−1} with s∤n. So the reduced
   denominator and s | y are preserved, and (r,n)=1. A nonhard factor (2, or a prime ≢1 (8)) gives r=1 by z75. ✓

**Edge cases checked.** t=p is impossible mod 4. p | F is excluded by the order argument. s | R, s=t and s | m are
excluded. A small p with a large R is harmless. The finite R-range is irrelevant to an "as R→∞" statement.
**Circularity.** None: the supply T depends only on U, and only s depends on p. **Uniformity.** All constants are
absolute, or depend on c, C or γ only. No distribution statement in p is used.
**Barrier remark.** Distinct t give distinct divisors (t−1)/2 of h, so N ≤ τ(h). Combined with 2^N ≥ s−1 and log s ≫ U,
this gives log h ≫ log U·log₂U. The remark is correctly scoped to this full-coverage certificate.

**Wording nits (optional).** (i) In the unconditional branch, the only ineffective input is Maynard's theorem (through
Siegel–Walfisz), if the carrier is taken from IK 18.8. The note could say so. (ii) The label's "TZ Thm 1.4 + Stark" for
the carrier count could be "(or IK Cor. 18.8)".

---

## (b) CAP_ZERO Theorem V

### Packet
**Identity.** Multiplying 4/n = 1/x+1/y+1/z by narvwS gives 4arvwS = nv+S+ar³. This is (f+1−1)S = nv+ar³, as stated. ✓

**Divisibility and root.** f≡−1 (mod arv), so v and the class −ar³/v are units mod f. For l | r, the relation
fS = nv+ar³ gives −S ≡ nv ≢ 0 (mod l), so (r,S)=1. Together with (r,v)=(r,w)=(r,n)=1, the denominator of z is exactly r².
Also r | y. ✓

**The (r,w)=1 test is needed.** The replay finds 33 cases with (r,w)>1 where den z ≠ r².

**Dictionary cross-check (new).** The packet has y = n(f+1)/4. Its CAP_INTERPOLATION Prop 5.1 shot label is
D = xf − nA = a²r⁴w (replayed). This lies in 𝒟₁(f): a has valuation 2 ≤ 2σ, r has valuation 4 = 2σ+2 with σ=1, and w
has valuation ≤ σ. So V is an honest ES^{(y,1)} shot certificate. Its class is the reduced ratio −ar³/v, not the small
cube label used by C1.

**Distinctness.** ar³v′ ≤ x^{.126} < ℓ, so a collision forces ar³v′ = a′r′³v. Then v=v′ (each side is coprime to the
other's v), and (a,r) is recovered from the valuations {1,3}. Finally 4arv > x^{.08} > K₀ forces k=k′. ✓ The replay found
0 collisions among 20,718 labels mod 10⁹+7.

### Masses
**Lower bound.** k ranges over odd G-supported integers with Σ_{l|k}1/l ≤ D₀. They have positive lower density, so
Σ1/k ≫ t.
* Squarefree r: the B-rough density is ≫1/log B. The removals (bad primes > B, squares > B², and the Markov bound on
  Σ_{l|r, l>B}1/l > 1/4) cost O((log B)^{−A}+1/B) in absolute density, which is smaller than 1/log B for B large. This
  gives ≫t.
* Prime r: Mertens gives log t − O_{B,D₀}(1).
* v: a positive proportion per dyad, giving ≫t.
* a: Möbius over h² | a. Terms with h sharing a prime with 2rv or k vanish because a≡unit (mod k). The main term is
  ≥ A·φ(2rv)/(2rv·k·ζ(2)), and the error O(√A·τ(2rv)) is o(A/k). This gives ≫t/k.

Altogether the mass is ≫ t³R_t per block. The (r,w) loss is ≤ Σ_{l|r}1/l ≤ 1/4, because l | q₀ gives
φ(q₀l) = lφ(q₀). ✓

**Upper bound** (needed so that the Taylor degree D ≍ M_t is uniform over fibres). BT plus
Σ_{a≡b (k)}1/φ(a) ≪ t/k (from a/φ(a) = Σ_{d|a}μ²(d)/φ(d)) give μ_c ≪ t³R_t. ✓

**BV incidence.**
* Ordered quadruples: at most τ(q)^4.
* d | r gives τ(rd) ≤ τ(r)² and φ(q₀d) = dφ(q₀).
* Pairs of active k: for fixed (r,v), a lies in one reduced class mod b = [k,k′] ≤ K₀² < x^{.00005}, which is inside
  Shiu's range for F = τ^C·j/φ(j).
* Σ_{k,k′}1/φ([k,k′]) ≪ t³·log t.

This gives ΣW²E* ≪ x·t^{C″}. Cauchy against BV (all q < x^{.13}) then gives an error of x·t^{(C″−A)/2}, which is far
below the main term x·t²R_t per block. The bound is uniform in the unit fibre c. ✓

### Transfer
**Model.** The repair acts on n mod p^{v_p(k)} and depends on n mod p, so each repaired atom depends only on n mod kℓ.
Given the fibre, the ℓ-digits are independent, and the atoms at one ℓ are mutually exclusive. So Z is a sum of
independent Bernoullis with mean μ_c ≍ M_t.

**Majorant.** I re-derived it: for D even and x=−1/2, the Lagrange remainder of (1+x)^Z has the sign of x^{D+1} < 0.
Hence T_D(Z) ≥ 2^{−Z} ≥ 1[Z=0], and the remainder is ≤ 2^{−D−1}·C(Z,D+1). We have E·C(Z,D+1) ≤ μ^{D+1}/(D+1)!.

**Boundary.** There are exp(O(t))^D intersections, each a union of exp(O(tD)) classes. So the boundary term is
exp(O(tM_t)). ✓

**Failing n.** A failing n has no prime factor in G (by scaling). So the repair is invisible, and (r,n)=1 because r is
G-supported.

### Optimisation
* Squarefree row: M_t = t⁴ and t = αL^{1/5}, giving N·exp(−cL^{4/5}).
* Prime row: M_t = t³·log t. Take t⁴·log t = α′L, i.e. t ≍ (L/log L)^{1/4}. Then M_t ≍ L^{3/4}(log L)^{1/4}. ✓

### Required fixes (wording/scope only)
* **V1.** The sentence "Allowing *one* prime to overflow does not yield the entire fourth power of the supply logarithm"
  is inside a PROVED block but is not proved as a barrier. Scope it to "in this construction (the prime-r row has
  harmonic mass log t, not t)", or label it Assessment.
* **V2.** "Establishes the e=1 prediction of `CAP_INTERPOLATION.md`" should be made precise. V proves the "3/4-note
  multipliers" row at e=1 (an Assessment there, for primes), and on all integers. The "KARY3-type ceiling" row at e=1
  (also 4/5) remains an Assessment. No optimality of 4/5 at cap 1 is claimed or implied. C1 already says this; V should
  match it.
* **V3 (export).** The two derivations, V and C1, are independent in their **packet and supply** (ratio class −ar³/v
  versus cube label −4uv²w⁴). They **share** the transfer: the z79 `WILD_ES.md` §3 finite transfer, the Vaughan unit
  repair, and the BV/BT/Shiu incidence pattern. A STATUS or WAVES row may say "two derivations". It must not say "two
  independent proofs" without this caveat, because an error in the z79/TQ transfer would affect both.

---

## (c) SPECIFIC_CLASS Theorem C1

**Identity.** VA − D = (Vf + V − 4D)/4 = (n+V)/4. This is CAP_INTERPOLATION Prop 5.1 with M=f and an arbitrary input n.
The sum is verified. ✓

**Valuations.** Let s | D, so σ = v_s(A) ≥ 1 (s | Q | f+1, s odd).
* t = 1 or 2: v_s(x) ≥ 1, so v_s(z) ≥ 0.
* t = 4 and s | n: s | V, so v_s(x) ≥ 2 and v_s(z) ≥ 0.
* t = 4 and s∤n: V is an s-unit. Then σ ≥ 4 gives v_s(z) ≥ 0; σ = 2 or 3 gives 2σ−4 ≥ 0; σ = 1 gives exactly −2.

So the root is ∏{s | w : s∤n, s∥A}. It is odd, squarefree, coprime to n, and divides A | y. The argument is complete for
composite n with (n,D) > 1. ✓ The replay ran 2,741 random packets (323 with composite roots, 741 with (n,D) > 1), plus
1,879 forced s | gcd(n,w) cases. All were exact.

**Distinctness.** 4D < 4H^{.014} < ℓ, and D determines (u,v,w) through the valuations {1,2,4}. Since
Q ≥ Z^{3/2000} > K₀, k is determined as well. ✓

**Mass (10).**
* k: the loss from (vw,k) > 1 is O((log P₀)^{−5}), small against the initial (log P₀)^{−2}.
* u: a reduced class mod k, with fixed-modulus roughness at primes ≤ P₀. These moduli are coprime to k, which is
  P₀-rough.
* Removal of squares and non-coprime pairs costs O(1/P₀ + k/√Y₁ + k·log Z/Y₁), small against (log P₀)^{−3}.
* Upper bound: through Σ_{a≡b (k)} a/φ(a).

✓

**BV.**
* W_Q² ≤ τ₃(Q/4)·Σ I².
* Jointly active pairs: u lies in one class mod [k,k′] ≤ U^{.004}.
* Shiu for τ₃, and Σ_{k,k′}1/φ([k,k′]) ≪ t^{O(1)}.
* Cauchy against BT (E_Q ≪ H/(φ(Q)t)) and BV (Q ≪ H^{.006}) gives an error of o(H/t), against a main term ≍ H·t³ per
  dyad.

So the mass is ≍ t³ per dyad and ≍ t⁴ in total, uniformly in the pin. ✓

**Transfer.** As in V. There are exp(O(t)) atoms, the degree is O(t⁴), and the boundary is exp(O(t⁵)). With
t = c₃L^{1/5} this gives (9). ✓

**Export caveat.** C1's label already says the z79/TQ transfer is internal and unrefereed. Apply V3 to the shared row.

---

## CAP_INTERPOLATION cross-check (exact)

* **The table** (`CAP_INTERPOLATION.md` lines 269–271), at e=1:
  * "prime-modulus LS 3/4: PROVED (CAP_GROWING Thm 1.4; Thm 2.1 uniform)". This holds for **primes** only.
  * "3/4-note multipliers 4/5: **Assessment** (only the class supply changes, Cor 5.2)".
  * "KARY3-type ceiling 4/5: Assessment (KARY3 itself does NOT apply for e ≥ 1)".

  Before z81, therefore, no repo theorem stated 4/5 at cap 1. The cap-1 record was 3/4: for primes from
  CAP_GROWING Thm 1.4, and on all integers trivially from the ES 3/4 bound (cap 0 ⊂ cap 1). **V/C1 upgrade the e=1
  multiplier entry from Assessment to PROVED, and extend it from primes to all integers.** There is **no conflict**:
  * Cor 5.2 gives supply dimension e+3 = 4. With the mass-driven θ = 𝓑/(𝓑+1), this gives exactly 4/5, matching the t⁴
    masses computed in V and C1.
  * Prop 5.1 is the dictionary behind both packets. I checked that V's D = a²r⁴w and C1's D = uv²w⁴ both lie in 𝒟₁(f).
  * Thm 3.1 (the ceiling) concerns the truncated prime-modulus family, and KARY3 concerns 𝒟₀, so neither applies to
    V/C1.
* **CAP_GROWING Thm 1.4** proves 4/5 at cap **2** for primes. V/C1's cap-1 all-integer 4/5 supersedes that in scope,
  with the same exponent. The rows e ≥ 3 ((e+2)/(e+3) ≥ 5/6, primes) remain separate and are not superseded.
* **Export suggestion.** In STATUS §1B, use one shared row, as both lanes' deltas propose. Add a clearly marked
  `> **Erratum/update (z81):**` pointer in CAP_INTERPOLATION §5 at the e=1 multiplier entry. This is for the exporter
  to do; I am not editing old notes.

## Falsifier screen (F1–F4)

* **F1.** Both class families have Jacobi symbol −1 mod f. For V: (q/f) = 1 for each q | arv, because f ≡ −1 (mod 4q),
  and (−1/f) = −1. For C1 the same argument applies. So odd squares never lie in an atom. This was replayed on 761 V
  atoms and 980 C1 atoms. The upper bounds tolerate the squares, which fail only if built from G-free primes.
* **F2.** The same ratio identity at numerator 8, (8arvw−1)S = nv+ar³, gives **integral** 8/n solutions when r=1. The
  replay confirms that it never fires at 8/11, 8/17, 8/131 or 8/241 (a, v < 200), as it must. V/C1 claim nothing at
  numerator 8.
* **F3, F4.** Both results are upper bounds on exceptional counts. They make no pointwise claim at 4545, Z₇ or the (★)
  zeros. As a sanity check, the replay builds actual cap-1 packets at 409, 2521, 3361, 8,813,281 and 17,401,609. These
  are relaxed certificates and say nothing about (★) or integral ES.

## Replay

Script: `scripts/z81_xrev2_cap_records.py` (independent; exact `Fraction` arithmetic).
Command: `ulimit -v 6000000; timeout 300 uv run --offline --no-project python -B scripts/z81_xrev2_cap_records.py`.
It ran in 0.54 s with 34 MB peak memory and ended with `ALL CHECKS PASSED`.

* **Lemma I.**
  * The note's lift example (p=2281, s=17, m₀=31, h=15, root 17⁷) checks.
  * There are 64 inverse packets at the 16 hard primes 409, 2521, 3361, 8813281, 2281, 4201, 7321, 23929, 329617,
    1724209, 5212561, 577, 5569, 9601, 83449 and 102001. They are built exactly as in the proof: alphabet
    {t ≡ 3 (4) : (t−1)/2 | h} for h ∈ {15, …, 45045}, filtered by η(t) = −1 and t∤F, with t | s^h+1 verified, and a
    subset-product DP with parity tracking. 4 of them needed the F-lift.
  * 0 even-cardinality subsets hit −p (confirming η(−p) = −1).
  * 40 further forced-lift cases (s² | p+m₀) all have s∥K after the toggle.
  * For each packet I checked the sum, den z = s^{h−1} exactly, s∥K, gcd(K,pm) = 1 and m | s^h+1.
* **V.**
  * 910 random packets: exact sum, den z = r² exactly, (r,S) = 1, Prop 5.1 label D = a²r⁴w.
  * 33 controls with (r,w) > 1 have the wrong root.
  * 0 class collisions among 20,718 labels mod 10⁹+7.
  * Prime-root packets exist at 409, 2521, 3361, 8813281 and 17401609.
* **C1.** 2,741 random packets plus 1,879 forced s | gcd(n,w) packets; D ↦ (u,v,w) injective on 1,530 triples; Jacobi
  check on 980 atoms; packets at 409, 2521, 3361 and 8813281.

These are finite identity checks, **not** tests of the asymptotic savings.

## Bottom line

(a) Theorem I: ACCEPT. (b) Theorem V: ACCEPT-WITH-FIXES V1–V3, all wording, scope or export. (c) C1: ACCEPT, with the V3
export caveat.

Together with CAP_ZERO R1–R3 and SPECIFIC_CLASS R4, this is the second internal cross-lab review owed for I and V. It
supports the RECORD triage for the **relaxed cap-one family only**. Priority against the external literature is
unverified. There is no implication for integral ES, for the ambient 3/4 exponent, or for any pointwise cap.
