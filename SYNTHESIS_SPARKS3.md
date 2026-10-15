# SYNTHESIS_SPARKS3 — cross-combinations of (J)13–(J)38 aimed at the two exits (task O208, spark synthesis III)

Exits (STATUS "Spark-relay wave", Assessment): **(E1)** transport ES^{(S)} / ES^□ / V_φ / ES^{(y)} certificates back into
the O(p²) box; **(E2)** a genuinely new finite-search mechanism. Memos: `BRAINSTORM/s3_*.md`; scripts `scripts/s3_*`.
Earlier syntheses: SYNTHESIS_SPARKS.md (O171, (J)1–(J)10), SYNTHESIS_SPARKS2.md (O192, (J)13–(J)25); their combinations
are not repeated. ES is not solved; nothing below claims an infinite case of ES.

## 0. Iteration log (construction → kill → which hypothesis → modification)

(I1) Seed: "(J)23/(J)28 relaxations × (J)31/(J)32 numerator data". Question: is the □/mute relaxation sensitive to
whether the exact finite problem is solvable? Test case: the numerator M = 8, whose exact problem 8/n FAILS at
3, 11, 17, 131, 241 (Pomerance–Weingartner; (J)31/(J)32). Construction: the shot identity with 4 → M (§1). Result:
**M^□ is a theorem for every M ≡ 0 (mod 4) at every odd non-square coprime to M, and its shot mechanism has T1 exactly** (Thm 1.1), and it
holds at all 278 known failing pairs (M, p), M ∈ {8, 12, 16, 20, 24} (also with a FIXED mute set S = {3,5,7,11}).
So the relaxation is *numerator-blind* while the exact problem is not: a relativisation-type barrier for (E1) and
(E2) (§2, Cor 2.1). This is the main finding; it is a barrier, not a route (R207 repair D1/D2: its "4-specific input" reading assumes an
argument uniform in M without threshold, and (J)31 already drew the threshold-correct conclusion; see the note before Cor 2.1).
(I2) Steering: the barrier's hypothesis is "the argument is valid with 4 replaced by M". Known 4-specific inputs:
(J)32 (five slices = a χ-fibre only for m = 4), the parity split f₄ = f₈ + f₄^{odd} ((J)32 Lemma 2.1), and the
empirical absence of failures. §3 examines transports that use them.

## 1. The M-shot identity and M^□ at every non-square (PROVED, elementary)

**Lemma 1.0 (M-shot identity; PROVED, algebra).** Let M ≥ 1, n ≥ 1, Q ≥ 1, and g ≥ 1 with g | n + MQ², g ≡ −1 (mod M).
Put m′ := (n + MQ²)/g, x := (n + m′)/M, y := n(g+1)/M, z := nx(g+1)/(MQ²). Then x, y ∈ ℤ_{>0} and
`M/n = 1/x + 1/y + 1/z`, and if gcd(Q, n) = 1 then **den(z) = (Q/gcd(Q, k))²**, k := (g+1)/M.
*Proof.* m′g = n + MQ² ≡ n and g ≡ −1 (mod M) give m′ ≡ −n (mod M), so x ∈ ℤ. Mx − n = m′, so
M/n − 1/x = m′/(nx), and m′/(nx) − M/(n(g+1)) = (m′g + m′ − Mx)/(nx(g+1)) = (m′g − n)/(nx(g+1)) = MQ²/(nx(g+1)) = 1/z.
z = n·x·k/Q² with k = (g+1)/M ∈ ℤ. *(den(z); repair after self-review R-O208 #2.)* From gMx = n(g+1) + MQ² we get
**gx = nk + Q²**. Let ℓ | Q, c = v_ℓ(Q), σ = v_ℓ(k) (ℓ ∤ n). If σ = 0: ℓ ∤ nk and ℓ | Q², so ℓ ∤ gx, v_ℓ(x) = 0, v_ℓ(z) = −2c.
If σ ≥ 1 then ℓ | g + 1, so ℓ ∤ g, and v_ℓ(x) = v_ℓ(nk + Q²): if 1 ≤ σ < 2c: v_ℓ(x) = σ, v_ℓ(z) = 2σ − 2c. If σ ≥ 2c: v_ℓ(x) ≥ 2c,
v_ℓ(z) ≥ σ ≥ 0. In all cases the ℓ-part of den(z) is ℓ^{2·max(0, c − σ)}; primes ∤ Q do not occur in den(z). ∎
(For M = 4 the identity is UNIT_ORBIT_ES Prop 2.1 and the den formula EXPONENT_CAP Prop 1.2; R207 repair m10.)

Definition. **M^□(n)**: M/n = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, den(z) an odd square coprime to n.
**M^{(S)}(n)**: the same with den(z) = Q², Q ∈ ⟨S⟩ (S a finite set of odd primes ∤ n). M^□ ⊇ M^{(S)} ⊇ (M/n).

**Theorem 1.1 (M^□ is numerator-blind; PROVED, relative to Dirichlet's theorem only).** Let M ≡ 0 (mod 4) and let
n > 1 be odd with gcd(n, M) = 1.
(a) If n is not a square, there are a prime g ≡ −1 (mod M), g ∤ n, and an odd Q prime to n with g | n + MQ²; hence
M^□(n) holds (Lemma 1.0), with a solution of Type II shape.
(b) (T1 for M-shots.) If n = k² is a square, there is NO pair (g, Q) with g > 1, g ≡ −1 (mod M), gcd(Q, k) = 1 and
g | n + MQ².
*Proof.* Key computation: for every odd g ≡ −1 (mod M), the Jacobi symbol (M/g) = +1. Indeed (4/g) = 1; if 8 | M then
g ≡ 7 (mod 8) and (2/g) = 1; for an odd prime ℓ | M, reciprocity gives (ℓ/g) = (g/ℓ)(−1)^{((ℓ−1)/2)((g−1)/2)}
= (−1/ℓ)(−1)^{(ℓ−1)/2} = 1, since g ≡ −1 (mod ℓ) and (g−1)/2 is odd. Also (−1/g) = −1 (g ≡ 3 mod 4). Hence
**(−M/g) = −1 for every odd g ≡ −1 (mod M).** (∗)
(a) Write n = n₀k², n₀ > 1 squarefree, gcd(n₀, M) = 1 (below, "k" in den(z) = (Q/gcd(Q, k))² means (g+1)/M, not √(n/n₀);
R207 repair m1). For a prime g ≡ −1 (mod M), g ∤ n:
(n/g) = (n₀/g) = ∏_{ℓ|n₀} (g/ℓ)(−1)^{(ℓ−1)/2} = (g/n₀)(−1/n₀). The Jacobi character (·/n₀) is non-trivial, so there is
a class a (mod n₀) with (a/n₀) = −(−1/n₀); CRT (gcd(n₀, M) = 1) and Dirichlet give a prime g ≡ −1 (mod M), g ≡ a (mod n₀),
g ∤ k. Then (n/g) = −1, so by (∗) (−Mn/g) = 1: −n/M ≡ s² (mod g). Choose Q ≡ ±s (mod g), Q odd, Q ≢ 0 mod every prime
of n (CRT modulo 2g·rad n; g ∤ 2n). Then g | n + MQ², gcd(Q, n) = 1, and Lemma 1.0 applies; den(z) = (Q/gcd(Q, k))² is an odd
square prime to n.
(b) Let ℓ be a prime dividing n + MQ² = k² + MQ². ℓ ∤ 2 (the number is odd), ℓ ∤ M (else ℓ | k, and gcd(k, M) = 1),
ℓ ∤ Q (else ℓ | k). So −M ≡ (k/Q)² (mod ℓ): (−M/ℓ) = 1. By multiplicativity (−M/g) = 1 for every divisor g, contradicting
(∗) for g ≡ −1 (mod M), g > 1. ∎

*Remarks.* (o) (R207 repair m3) (b) concerns shots only: M^□ ⊇ (M/n) holds at most odd squares, e.g.
8/9 = 1/2 + 1/3 + 1/18. (i) (b) is the M-shot form of ET Prop 1.6 / UNIT_ORBIT Cor 1.2; for M = 8 it matches (J)31 Prop 5.1 (8/n has
T1). (ii) For the fixed mute set version, the Gupta–Murty sieve of (J)23 Thm 2.4 should transfer (R207 repair D3: routinely only when n has a prime
ℓ₀ ≥ 5 of odd valuation — in particular for every prime p ≥ 5, all that Cor 2.1 uses; at n = 3k², 3 ∤ M, M ≠ 4, the
requirement (3/r) = −1 forces 3 | (r−1)/2, so the index-3 case is not sifted, and Thm 2.4's Q = 1 shortcut has no
M-analogue: a Kummer–Chebotarev condition would be needed; EVIDENCE: no failure for M ∈ {8,16,20,28}, k < 80) with the
sifted prime r ≡ −1 (mod M) in place of r ≡ 3 (mod 4) (for r ≡ 3 (mod 4) squares and 4th powers coincide, so the index-2
case of ⟨S⟩ is handled as there). This transfer is an **Assessment (not re-derived)**; the EVIDENCE below is independent
of it.

**EVIDENCE / CERTIFIED examples (`scripts/s3_numerator_blind.py 60`, < 1 s; `scripts/s3_mute_S.py 100000`, < 1 s;
every solution verified in exact rational arithmetic).** For all 278 failing pairs (M, p) of the census
`data/ms/prime_fail_1e8.txt` with M ∈ {8, 12, 16, 20, 24}, p ∤ M (5 + 20 + 37 + 62 + 154 primes; p ≤ 10⁸, the exact
problem M/p has NO solution there — MODEL_SPECIFIC §1, CERTIFIED, reproduced by R197), Thm 1.1(a)'s Dirichlet
certificate exists with g ≤ 239. Smallest example:
`8/131 = 1/20 + 1/131 + 9/2620`   (g = 7, Q = 3; 8/131 itself has no solution in unit fractions).
With the FIXED mute set S = {3, 5, 7, 11}: every failing pair with p ∉ S has an M^{(S)} shot solution, Q ≤ 385.
Triple-check of Thm 1.1(a) (`scripts/s3_mbox_check.py 1000000 100000`, 12 s): for each M ∈ {4, 8, 12, 16, 20, 24},
every prime 3 ≤ p < 10⁶ with p ∤ M and every odd non-square n < 10⁵ prime to M gets an exactly verified M^□ solution
(max Dirichlet g over the primes: 131, 271, 251, 863, 659, 839).
T1 control: odd squares k² (k < 120, gcd(k, M) = 1), Q < 40, M ∈ {4, 8, …, 24}: 0 shots g ≡ −1 (mod M) (as proved).
Overflow profile (R207 repair m4: Q odd; 8 pairs, e.g. (16, 97), (24, 1657), have no odd-Q shot with Q ≤ 60, and with even Q
Q₁ = 2 occurs, e.g. (8, 241) with Q = 2, g = 7): the least overflow Q₁ = Q/gcd(Q, (g+1)/M) over shots with odd Q ≤ 60 is ≥ 3 at every failing pair having one
(necessarily: Q₁ = 1 would be an M/p solution); it equals 3 at 131 and 241 (M = 8).

## 2. The barrier: relaxations are numerator-blind, the finite problem is not

*(R207 repairs D1, D2, D4: the PROVED/CERTIFIED content of Cor 2.1 is only the implication failure R_8(131) ∧ ¬(8/131)
(and likewise at 241 and the other pairs); the "Consequently …" reading below is an Assessment with the hidden hypothesis
"the argument is valid for ALL p ∤ M, uniformly in M, with no threshold". A numerator-uniform input "p > n₀(M)" is false
at (8, 131), and Schinzel's conjecture / the PW lottery heuristic are themselves threshold statements, so "false at
(8, 131)" does not mean "4-specific". Threshold-robust form: by Thm 1.1(a) + PW Thm 1.2, for every M ≡ 0 (4),
M ≥ 6.52·10⁹, some prime p ∈ (M², 2M²) has M^□(p) and ¬(M/p); so an M-uniform transport needs n₀(M) > M² (and
> exp(M^{1/3−ε}) by the proof of PW Thm 1.1). Novelty: (J)31 already concluded that an ES proof needs something specific to 4
(threshold-correct form), and (J)32 already used 8/131 to refute the χ-fibre mechanism for m = 8; the increment here is
(∗) + Thm 1.1 for all M and the fact that the □/mute relaxations with exact-T1 shot mechanisms and Dirichlet/sieve
existence are also blind — extending B7's list "BM + T1". BM: the certificates at 131, 241 are TES_FINITE Thm 5.3
(rel. BL Thm 1.6 / Rem 1.10); for M = 12–24 the BM status was NOT computed, and (16,3), (16,5), (20,3), (24,5), (24,7)
are trivial size failures, M/p > 3.)*
**Corollary 2.1 (numerator-blindness barrier for (E1) and (E2); formal part PROVED given Thm 1.1 and the CERTIFIED census; the "Consequently" reading is an Assessment, R207 repair D1).**
For M = 8 and p ∈ {131, 241} (likewise M = 12, 16, 20, 24 at the 20, 37, 62, 154 listed primes): M^□(p) holds, and
M^{(S)}(p), S = {3, 5, 7, 11}, holds whenever p ∉ S (264 of the 278 pairs; EVIDENCE), T1 holds for the M-shot family (Thm 1.1(b)), every Brauer–Manin / local
condition of the M-problem is satisfied (no BM obstruction to 8/p at 131, 241: Bright–Loughran Rem 1.10), and M/p has
no solution. Consequently, for any family of implications {"∀ prime p ∤ M: R_M(p) ⇒ M/p solvable"}_{M ∈ 4ℕ} with
R_M ∈ {M^□, M^{(S)}}, the member M = 8 is false. A proof of ES that transports relaxed certificates (E1), or a
finite-search existence mechanism (E2), must therefore use at least one input that is FALSE for M = 8 at p = 131 or
241 — an input specific to the numerator 4.

*Which campaign tools are numerator-uniform (hence cannot be that input)?* (Assessment, item by item; each is either
stated for general numerators in its source or its proof uses 4 only through "4 | M".)
* Shot identity, overflow ↔ growing-modulus duality ((J)34 Prop 1.3: replace 4 by M), the cap hierarchy, the archimedean
  wall: uniform.
* T1 / Diff-parity / Brauer–Manin ((J)13, (J)17, (J)21 Thm 2.1: the place 2 gives 0 for every numerator ≡ 0 mod 4 —
  the BL local lemma; (J)31 Prop 5.1 for 8): uniform. BM is silent at 131, 241 (TES_FINITE Thm 5.3, rel. BL Rem 1.10; R207 repair D4).
* Finiteness of the box ((J)25; (J)31 Prop 1.1 / BL Lemma 3.10 for any numerator): uniform.
* Sieve / Dirichlet / Chebotarev existence of firing primes ((J)23, (J)28, Thm 1.1): uniform (the (J)23 transfer is an
  Assessment, see Remark (ii)).
* Composition, Vieta/Pell moves, class-group pigeonhole on V_n ((J)36–(J)38): the surfaces are those of the shot
  family; replacing 4 by M changes only the congruence g ≡ −1 (mod M) — uniform in form.
* Function-field and ℤ[ω] analogues: the analogous relaxation-vs-exact blindness (same numerator; R207 repair m5) holds there — FF: ES_q^{(s)} is a theorem at every P
  ((J)30 Thm 3.5) while ES_q fails at some P (e.g. q = 5, A = T, degree ≤ 4; (J)4) and has no finite linear covering (all ET types: FF_INVERSION_CHECK Cor 2.6) for
  q = 3^r, r ≥ 27 ((J)26); ℤ[ω]: TES^{□₃} holds at every 2-primary non-cube prime to 6 ((J)28 Thm 3.5, relative to Chebotarev) while TES
  fails at 16 2-primary split primes ((J)31 Thm 2.1, stated for 2-primary π); these are non-cubes prime to 6, so Thm 3.5
  covers them (PROVED by combination), and (J)28's EVIDENCE (2) explicitly solved TES^{□₃} at all 2-primary split
  primes with N(π) ≤ 6000, which include 15 of the 16 (R207 repair m6: the same recipe run to N(π) ≤ 27000, `scripts/syn2_tes_shots.py 27000 50`,
solves all 5856 such primes, including all 16).

*Numerator-specific inputs known in the campaign (candidates for the missing input; the list is not claimed to be
exhaustive — a different numerator-dependent argument, possibly combined with uniform tools, is not excluded):*
(α) **(J)32 Thm 3.1(a): the five slices S₄ = {χ = −1} on positive words — FALSE for 8** (at 131: 29 χ = −1 words,
    S₈ = ∅); its geometric forms (J)33 (χ = −ε₂(Q_w), certificates ⟺ B_{p,∞}) and (J)35 (2-isogeny edges);
    (J)9 Thm 4.5 (HJ length 3).
(β) (J)32 Lemma 2.1: f₄ = f₈ + f₄^{odd}; ES at 131, 241 lives entirely in the one-odd half.
(γ) The bare numerical fact "no failure ≤ 10⁸" (EVIDENCE; not an input).

*Reading (Assessment; R-O208 #5 softened).* Cor 2.1 proves only that some 4-specific input is needed (R207 repair D1: or an M-dependent threshold; and only for arguments uniform in M). Among the known
ones, (α) is the cleanest: it is **numerator-free** ("some positive word of n has χ = −1", SQ₅/(S)), so it is not itself
refuted by the 8/n failures, and it implies the five-slice part of ES. The barrier therefore *steers* (E1) towards SQ₅ as
the natural known target (not the only conceivable one). §3 examines that target.

## 3. Steering: the natural target, and a falsification harness

**3.1 What the barrier leaves (Assessment, with PROVED components).** By Cor 2.1 an exit needs a 4-specific input.
Among those known, (α) is numerator-free: SQ₅/(S) — "some positive word tuv − u − v = n has χ(w) = (−A/n) = −1" —
implies the five-slice part of ES ((J)32 Thm 3.1(a)) and is *consistent* with the failure of 8/131 (29 such words
exist at 131; S₈(131) = ∅). So SQ₅ is the natural known target for (E1)/(E2). What the relaxed certificates can contribute
to SQ₅ is then exactly one bit per modulus:
* (PROVED, BRAINSTORM/s3_box_bit) for a prime g ≡ 3 (mod 4): a □-shot at g exists ⟺ (p/g) = −1, and every Type II ES
  certificate at modulus g forces (p/g) = −1; numerically the box fires in 9.5% of the (p/g) = −1 pairs and in 0% of
  the others. The □ relaxation is the sign layer of the prime-modulus certificate; the box is the class layer (B2).
* (PROVED, BRAINSTORM/s3_eps_mu_sieve) the (J)23 sieve variable and the (J)38 ES slot are the same shot n + 4t² with
  Q = t; the ES side forces Q ≤ (g+1)/4, the sieve side lets Q run through ⟨S⟩ (overflow).
* (EVIDENCE, BRAINSTORM/s3_min_scale) both the relaxed and the exact search terminate at polylog scale in practice
  (h_min ≤ 0.82 log³p for all p ≡ 1 (4) < 10⁷; Dirichlet g ≤ 1.46 log²p). Finiteness of the ES box is not the
  operative difference; the type of firing condition (character vs box) is.
So transporting relaxed certificates into SQ₅ means converting a character event into a divisor-box event — B2, the
same core every earlier synthesis reached ((J)11 skeleton). No new hatch opens; the barrier sharpens the old one by
removing every numerator-uniform tool *without an M-dependent threshold* from consideration (R207 repair D1: threshold-bearing
uniform tools are not excluded, see the note before Cor 2.1).

**3.2 Falsification harness (a practical by-product; Assessment).** Any proposed (E1)/(E2) mechanism should be run on:
(i) 8/n at n = 131, 241 (and M = 12, …, 24 at the listed primes): a mechanism that "proves" these is wrong;
(ii) TES at N(π) = 7, 13, 19, 61, … (16 primes): genuine non-T1, non-BM failures with TES^{□₃} true (BRAINSTORM/
s3_order3_numerator) — a mechanism that transplants to ℤ[ω] is wrong;
(iii) ES_q over F_q[T] at its known failures (e.g. q = 5, A = T, degree ≤ 4; NOT the q = 3^r covering result of (J)26,
which exhibits no failing P — FF_MUTE warns against that inference; R-O208 #8) where
ES_q^{(s)} is a theorem ((J)30);
(iv) odd squares (T1) — the classical control.
(i)–(iii) are controls *beyond* T1: places where every local, Brauer–Manin, sieve and relaxation input holds and the
exact finite search fails. The campaign's barrier screens (B1–B6, T1) were run against (iv); 8/131, 8/241 appeared
before as Brauer–Manin controls (TES_FINITE Cor 5.4) and as a mechanism test for the χ-fibre ((J)32, MODEL_SPECIFIC: S₈(131) = ∅),
with (J)31 already drawing the "4-specific input" conclusion (R207 repair D2: the earlier "not as a test for proof mechanisms"
was false). For M = 12–24 the BM status is not computed and some failures are trivial size failures (R207 repair D4).

**3.3 Brief items screened and where they landed** (memos BRAINSTORM/s3_*; each combines ≥ 2 wave results):
| memo | combination | outcome |
|---|---|---|
| s3_numerator_blind | (J)23/(J)28 × (J)31/(J)32 | **barrier, PROVED** (§1–§2) |
| s3_order3_numerator | (J)19/(J)28 × (J)31 × (J)32 | order-3 blindness PROVED + EVIDENCE; SQ₅₃ consistency constraint |
| s3_box_bit | (J)28 × (J)25 × (J)38 Prop 4.1 | □ = sign layer exactly (PROVED); slicing across n relabels the box |
| s3_eps_mu_sieve | (J)23 × (J)38 | sieve variable = ES slot, Q = t forced small (PROVED); collapses to (J)25 |
| s3_min_scale | (J)25 × (J)28 × (J)30 | box size is not the obstacle (EVIDENCE) |
| s3_lll_lenstra | (J)25 × (J)38 × Lenstra/Coppersmith | LLL = ≤ 11 per line + decision; no existence (PROVED rel. Lenstra) |
| s3_words_parity | (J)33 × (J)15 × involution parity | no parity law (EVIDENCE); σ forces nothing |
| s3_isogeny_mixing | (J)35 × (J)16 × expander mixing | mixing cannot robustly force a certificate (Assessment; counts PROVED/EVIDENCE) |
| s3_vphi_ringmaps | (J)21 × (J)25 × (J)17 | ring maps / Galois averaging / norms give only local or B2 data (PROVED for these operations) |
Not re-done: "(J)36 Pell orbits × (J)37 CF depth" is already MARKOFF_ES Prop 7.1(b) (an orbit reaches B = 1 iff it is
the ES point's orbit) and COMPOSITION_ES Thm 1.3.

## 4. Verdict (Assessment)
No route to ES. The one new structural result is the **numerator-blindness barrier** (Thm 1.1, Cor 2.1): for every
M ≡ 0 (mod 4) the □-relaxation (and empirically the fixed-S mute relaxation) is a theorem at all non-squares prime to M (R207 repair m2), its
shot mechanism having T1 exactly, while M/p fails at 278 known (M, p) pairs; the same blindness holds over ℤ[ω] (TES) and F_q[T]. Hence (Assessment, R207 repair D1/D2:
under the hidden hypothesis of an argument uniform in M with no threshold — (J)31 already drew the threshold-correct form)
the wave's two exits both need a numerator-4-specific input or an M-dependent threshold n₀(M) > M²; the natural known one is SQ₅ ((J)15/(J)32), toward which
the relaxed certificates contribute exactly the sign bit. The harness §3.2 gives three new failure controls
beyond odd squares.
