# Z60_LOPEZT — tryhard lane: the two-branch divisor statement (4/p, Type II sub-family)

Fresh attack (no FRONTIER / Z5*/Z6* memos read). Data used: `data/z58/screens/` only.

## §0 Problem, exact reformulations, and the four mandatory falsifiers

**Statement S(p).** For a prime p ≡ 1 (mod 24) (large), there is y ≥ 1 and a divisor f | p + y with f ≡ −1 (mod L_y),
L_y = y if 4 | y, L_y = 4y otherwise. Branches (corrected brief):
* **B4** (4 | y, modulus y): fails alone at the primes 193, 2521, 66529 (≤ 10¹⁰ per brief; verified ≤ 2·10⁵ by `scripts/z60_lopezt_branches.c`).
* **BN** (4 ∤ y, modulus 4y): fails alone at the 14 primes of `data/z58/screens/star_prime_zeros.txt` (409 … 8 813 281); verified ≤ 2·10⁵.
* Both branches together: fails at every odd square and, among odd non-squares ≤ 10¹⁰, only at 105 and 4545 (verified ≤ 6·10⁴).

### §0.1 Exact equivalences (PROVED, elementary)

Lemma 0.1 (BN identity). If p + y = f g with f = 4yk − 1 (k ≥ 1), then p = 4ykg − y − g and
  4/p = 1/(ykg) + 1/(pgk) + 1/(pyk).
Proof: 4ykg = p + y + g; divide by p·ykg. ∎ (No condition on y is needed; BN restricted to 4 ∤ y is only the brief's bookkeeping. The modulus-4y divisor condition for 4 | y is strictly stronger than B4.)

Lemma 0.2 (B4 identity). If 4 | Y, Y = 4Y', p + Y = f g with f = Yk − 1 (k ≥ 1), then p + g = Y(gk − 1) and
  4/p = 1/(Y'(gk−1)) + 1/(pY'k) + 1/(pY'k(gk−1)).
Proof: fg = Ykg − g = p + Y ⇒ p + g = Y(gk−1) = 4Y'(gk−1). Then 1/(pY'k) + 1/(pY'k(gk−1)) = g/(pY'(gk−1)), and adding
1/(Y'(gk−1)) gives (p+g)/(pY'(gk−1)) = 4/p. ∎
(Numerically found: among the Type I/II parametrizations of all solutions of 4/p for 681 B4-hits with p < 1500, the choice c = g in the
Type II form below always worked, with (a, b, m) = (1, gk−1, k).)

Lemma 0.3 (complete Type II parametrization; p prime). Solutions 4/p = 1/x + 1/(py') + 1/(pz') (p ∤ x) are exactly
  p = 4abd' − (a+b)/m with m | a + b,   x = ab d', y' = a d' m, z' = b d' m   (a, b, d', m ≥ 1).
Equivalently: ∃ a, b, c ≥ 1 with c | a + b and 4ab | p + c.
Proof: 4xy'z' = py'z' + x(y'+z'). Put d = gcd(y',z'), y' = da, z' = db, gcd(a,b)=1: x(4dab − a − b) = p d ab; since
gcd(4dab−a−b, ab) = 1, ab | x, x = ab x', and x'(4dab − a − b) = p d. If p | x' then 4dab − a − b ≤ d, impossible. So
4dab − a − b = mp and then d = x' m (as x'·mp = pd); substituting, 4x'mab − (a+b) = mp ⇒ p = 4x'ab − (a+b)/m, with d' := x'. ∎
  * BN ⟺ Type II with m = 1 (a = y, b = g, d' = k).
  * B4 ⟺ Type II with a = 1 (c = g, b = gk − 1, m = k, d' = Y').
So S(p) is the sub-family {m = 1} ∪ {a = 1} of the Type II parameter family (§2), hence S(p) ⇒ Type II(p) ⇒ ES(p); nothing here is easier
than ES for large primes. (Whether the existence statements differ *on primes* is open: no prime ≤ 10¹⁰ separates them.)

Lemma 0.4 (complete Type I parametrization; p prime). Solutions 4/p = 1/x + 1/y + 1/(pz') with p ∤ xy are exactly
  m p = 4abw − 1, a + b = d' m,   x = w d' a, y = w d' b, z' = abw.
Equivalently ∃ a, w, c with c | 4a²w + 1 and 4aw | p + c; equivalently ∃ m ≡ 3 (mod 4): (mp+1)/4 = a·b·w with m | a + b.
(Proof as in 0.3; the gcd step uses gcd(ab, a+b) = 1 and p ∤ ab; the "m ≡ 3 (4)" form assumes p ≡ 1 (mod 4). In the (⇐) direction
the solution is genuinely Type I: p | 4abw − 1 (= mp) forces p ∤ abw, and d' = p(a+b)/(4abw − 1) < p, so p ∤ wd'a, wd'b.)
For p ≡ 1 (4), every ES solution is Type I or Type II (p divides 1 or 2 of x, y, z; not 0 since 4xyz = p(xy+yz+zx); not 3 since 4 ≤ 3 fails).

**Unified forms of S(p)** (PROVED, by Lemmas 0.1–0.2 and their converses):
  (U1) ∃ a ≥ 1, ε ∈ {1, 4}: p + εa has a divisor ≡ −1 (mod 4a).        [ε = 1: BN; ε = 4: B4 with Y = 4a]
  (U2) ∃ y, e ≥ 1: 4ye | p + y + e (BN) or 4ye | p + y + 4e (B4).
  (U3) ∃ t ≥ 1: 4tp + 1 (BN) or tp + 1 (B4) has a divisor D ≡ −1 (mod 4t).
  (U4) ∃ (t, a, b) ∈ ℕ³: p = 4tab − a − b (BN) or p = 4tab − 4a − b (B4).
Converse checks: (U3) BN: 4tp+1 = DE with D ≡ −1 (4t) forces E ≡ −1 (4t), so D = 4ta−1, E = 4tb−1, p = 4tab − a − b.
(U3) B4: tp + 1 = DE, D = 4ta − 1 ⇒ E ≡ −1 (t), E = tb − 1 ⇒ p = 4tab − 4a − b ⇒ p + 4a = b(4ta−1): Y = 4a, f = D. ✓
This is the brief's "T-form" (L_T = T for 4 | T is the BN case with t = T/4; L_T = 4T otherwise is the B4 case t = T).

### §0.2 The four falsifiers — what any proof must respect

**(F1) odd squares n = m².** Lemma 0.5 (PROVED; n any odd integer coprime to D). If D | tn + 1 or D | 4tn + 1 with D ≡ −1 (mod 4t), then the Jacobi symbol (n/D) = −1.
Proof: D ≡ 3 (mod 4) so (−1/D) = −1, and tn ≡ −1 (resp. 4tn ≡ −1) mod D gives (t/D)(n/D) = −1. Claim (t/D) = +1: write
t = 2^s t₀, t₀ odd. If s ≥ 1 then 8 | 4t | D+1, so (2/D) = 1. For t₀: D ≡ −1 (mod t₀) gives (D/t₀) = (−1/t₀) = (−1)^{(t₀−1)/2},
and reciprocity with (D−1)/2 odd gives (t₀/D) = (D/t₀)(−1)^{(t₀−1)/2} = +1. ∎
Hence for n = m² (gcd(m, D) = 1 automatically) no witness exists. **Any proof must produce a D with (p/D) = −1**: the step
that uses non-squareness is the one that supplies a prime q | D with (p/q) = −1. For p ≡ 1 (mod 24) that is a quadratic residue
modulo every prime ≤ z, every witness D must contain a prime q > z — no finite covering system can work on this class.

**(F2) numerator-8 analogue.** The same derivation for 8/p gives Type II: p = 8abd' − (a+b)/m; the two branches become
  ∃ t: 8tp + 1 or tp + 1 has a divisor ≡ −1 (mod 8t)   (equivalently p = 8tab − a − b or p = 8tab − 8a − b).
The brief: this fails at 45 primes ≡ 1 (4) ≤ 10⁸ (last 3 869 153). The expected number of witnesses with D ≤ X is
≍ (log X)² in both cases, with a smaller constant for 8. So a "generic" counting argument cannot distinguish 4 from 8; a
proof must either be quantitative with explicit constants that fail for 8 below 3.9·10⁶, or exploit a 4-specific
covering structure. (This is a check on explicitness, not a structural obstruction: heuristically both have finitely many zeros.)

**(F3) n = 105, 4545.** Non-squares where S fails; both composite. Any argument "for all large non-squares" is false below 4545;
an argument using primality must point to the step where p prime (not merely non-square) is used, or carry a threshold.

**(F4) single-branch zeros.** BN alone fails at 409 … 8 813 281; B4 alone at 193, 2521, 66529. A proof using one branch only
must have threshold > 8 813 281 (BN) or > 66 529 (B4), with a stated reason.

(Status tags below: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE.)

## §1 The witness-modulus form (U5) and the inversion symmetry of the two branches (PROVED)

Fix a witness modulus g ≡ 3 (mod 4) with gcd(g, p) = 1 (automatic for actual witnesses, which divide p + a or ap + 1 with a < g). Let Q := (g+1)/4 and R_g := { −a mod g : a | Q } ⊂ (ℤ/g)^× (all distinct, since a ≤ Q < g).

Lemma 1.1. Here "BN" means the enlarged modulus-4a condition for *any* a (Lemma 0.1 needs no restriction on a). The enlargement does
not change the branch's existence statement: if p = 4tab − a − b with 4 | a then b ≡ 3 (mod 4) (as p ≡ 1 mod 4), and swapping a ↔ b
gives a witness with 4 ∤ (new a). For fixed g, however, the two readings differ (e.g. p = 337, g = 31: Q = 8, only a = 4 works).
(BN with this g) ⟺ p mod g ∈ R_g.   (B4 with this g) ⟺ p^{−1} mod g ∈ R_g.   Hence
  **(U5)  S(p) ⟺ ∃ g ≡ 3 (mod 4) with p^{±1} mod g ∈ R_g = −Div((g+1)/4).**
Proof. BN: g | p + a with g ≡ −1 (mod 4a) ⟺ a | Q and p ≡ −a (mod g). B4 (U3 form, t = Q/a): g | tp + 1 ⟺ tp ≡ −1 ⟺
p ≡ −t^{−1} ≡ −4a (mod g) (as 4ta = g + 1 ≡ 1) ⟺ p^{−1} ≡ −(4a)^{−1} ≡ −t (mod g), and t | Q. ∎
Remarks. (i) R_g ⊂ {QNR mod g}: (−a/g) = −(a/g) = −1 by Lemma 0.5's argument (g ≡ −1 mod 4a ⇒ (a/g) = 1).
(ii) The g-range: BN witnesses have g ≤ (4p+1)/3, B4 witnesses g ≤ 2p + 1 (t = 1: g | p + 1; t ≥ 2: g(1 − 1/t) ≤ p + 1/t).
(iii) The numerator-8 analogue is literally: ∃ g ≡ 7 (mod 8) with p^{±1} mod g ∈ −Div((g+1)/8). Since Div((g+1)/8) ⊂ Div((g+1)/4),
S₈ ⟹ S₄. `scripts/z60_lopezt_u5.c` (which implements (U5) directly) reproduces: S₄ zeros ≤ 6·10⁴ among odd non-squares = {105, 4545},
no prime zeros ≤ 2·10⁵; S₈ prime zeros ≤ 4·10⁶: exactly 45, last 3 869 153 (`data/z60/lopezt/s8_zeros_le4e6.txt`) — matching the brief's
figures (the equivalence itself is the algebra above; the computation is a consistency check against the brief's independent count).
**Sharpened (F2)** (in (U5) coordinates — the divisor d ∈ Div(Q) with p ≡ −d (BN) or p^{−1} ≡ −d (B4), Q = (g+1)/4): every S₄-witness
that is not an S₈-witness has either g ≡ 3 (mod 8), or g ≡ 7 (mod 8) with d ∤ Q/2, i.e. v₂(d) = v₂(Q). In the shift coordinates of (P*)
below (a := −p mod g for BN, a := −p·4^{−1} mod g for B4, so that d = a resp. d = Q/a) this reads: v₂(a) = v₂(Q) on BN, but **a odd** on B4.
Cross-model review example: p = 83449 (an S₈-zero) has the B4 witness g = 679, Q = 170, shift divisor a = 17 | Q/2 = 85 — yet it is not
an S₈-witness because the (U5) divisor is d = Q/a = 10 ∤ 85. A proof of S₄ must produce such non-liftable witnesses for (at least) the
45 primes in the file, or carry a threshold > 3 869 153.

Lemma 1.2 (no finite covering, even inside p ≡ 1 (24)). For any M, let L = lcm{4m : m ≤ M}·24. Every prime p ≡ 1 (mod L) has no
witness with g ≤ M: for such p, p ≡ 1 is a square mod g, but R_g consists of non-residues. By Linnik there are such primes with
p ≤ L^{C} = e^{O(M)}, i.e. infinitely many primes p ≡ 1 (24) whose every witness has g ≥ c·log p. More generally, if p is a
quadratic residue modulo every prime ≤ z, every witness g has a prime factor q > z with (p/q) = −1. ∎
Consequence: no argument whose witness moduli stay bounded (g ≤ M for a fixed M) can prove S(p); the same holds verbatim for the
Type I/II families of §2, whose residue sets are also non-residue sets. Witness moduli must grow with p. This does not exclude
explicit constructions with growing moduli, nor pointwise analytic methods in general; it only fixes a necessary feature.

## §2 Where S sits inside ES: the (a, m)-lattice of Type II, and Type I (PROVED)

Lemma 2.1 (Type II, two-parameter divisor form). For p prime, 4/p has a Type II solution ⟺
  **∃ a, m ≥ 1 (WLOG gcd(a, m) = 1): mp + a has a divisor g ≡ −1 (mod 4am).**
Proof. (⇐) g = 4amd' − 1, b := (mp + a)/g. Then mp = 4abmd' − a − b, so m | a + b; with c := (a+b)/m, p = 4abd' − c and
  1/(abd') + 1/(p·ad'm) + 1/(p·bd'm) = (pm + a + b)/(p·abd'm) = (p + c)/(p·abd') = 4/p.
(⇒) Lemma 0.3 gives p = 4abd' − (a+b)/m, i.e. mp + a = b(4amd' − 1). If d = gcd(a, m) > 1 then gcd(g, d) = 1 and g | (m/d)p + a/d
with g ≡ −1 (mod 4(a/d)(m/d)), so (a/d, m/d) also works. ∎
**S(p) is exactly the union of the two axes**: m = 1 (BN: p + a has a divisor ≡ −1 mod 4a) and a = 1 (B4: mp + 1 has a divisor ≡ −1
mod 4m). In the (U5) language, for a modulus g ≡ 3 (4) with Q = (g+1)/4 the full Type II residue set is
R^{II}_g = { −a·m^{−1} mod g : am | Q } (ratios of divisors of Q, negated); S uses only {−a} ∪ {−m^{−1}}.
Off-axis witnesses are genuinely new: n = 105 has the Type II witness (a, m, g) = (3, 2, 71) (213 = 3·71, 71 ≡ −1 mod 24) although
S(105) fails; n = 4545 has no Type II witness at all (exhaustive: g = 4amk − 1 ≤ mn + a gives a ≤ (mn+1)/(4m−1) ≤ (n+1)/3, and
g | n + 4a²k gives m ≤ a + (n+1)/(4ak) ≤ 7(n+1)/12 < n + 1, so the search m ≤ n + 1 in `typecheck.py` is complete). Here "Type II
witness" for composite n means the algebraic family of Lemma 2.1, not Elsholtz–Tao's coprimality-based type definition.
So there is no *universal* (primality-free) algebraic map from off-axis Type II witnesses to axis witnesses (F3 is consistent with this: 105 is rescued by Type II
off-axis, 4545 only by non-Type-II solutions, which for composite n exist outside the prime classification).

Lemma 2.2 (Type I divisor form). For p prime, 4/p has a Type I solution ⟺ **∃ a, w, m ≥ 1: 4aw | mp + 1 and m | 4a²w + 1.**
Proof. (⇒) Lemma 0.4: mp + 1 = 4abw and a + b = d'm; then 4a²w + 1 = 4aw(a + b) − mp ≡ 0 (mod m). (⇐) b := (mp+1)/(4aw);
gcd(m, 4aw) = 1 from m | 4a²w + 1, and 4aw(a + b) = 4a²w + mp + 1 ≡ 0 (mod m), so m | a + b; then x = wd'a, y = wd'b, z = pabw with
d' = (a+b)/m is a solution. ∎   (Both lemmas checked against brute-force enumeration of all solutions for every n ≡ 1 (4), n < 700:
`scripts/z60_lopezt_typecheck.py`, 0 mismatches on primes; on composites the ⇐ directions hold as identities.)

Summary of the landscape (for prime p ≡ 1 mod 4):
  ES(p) ⟺ [∃ a, m: mp + a has a divisor ≡ −1 (4am)]  ∨  [∃ a, w, m: 4aw | mp + 1, m | 4a²w + 1];
  S(p)  ⟺ [∃ a: p + a has a divisor ≡ −1 (4a)]  ∨  [∃ m: mp + 1 has a divisor ≡ −1 (4m)].
All three divisor conditions are empty at odd squares n = s². Type II: (n/g) = −1 as in Lemma 0.5 (g ≡ −1 mod 4am ⇒ (am/g) = 1, and
m n ≡ −a mod g ⇒ (m/g)(n/g) = (−1/g)(a/g) = −(a/g), so (n/g) = −(am/g) = −1). Type I: m | 4a²w + 1 gives (w/m) = (−1/m) = −1 (m ≡ 3 mod 4);
but for every odd prime q | w, m s² ≡ −1 (mod q) gives (m/q) = (−1/q), and reciprocity (m ≡ 3 mod 4) gives (q/m) = (m/q)(−1/q) = 1; if w is
even then 8 | m s² + 1 forces m ≡ 7 (mod 8), (2/m) = 1. Hence (w/m) = 1, contradiction. The step "p is not a square" is used nowhere else.

## §3 The pointwise statement: what a proof must do, and where every route I tried stops

### 3.1 Symmetric form and the least-witness problem
(U6) (PROVED; identities below). S(p) ⟺ ∃ a, b ≥ 1 with ab | p + a + b such that 4 divides a, b, or k := (p+a+b)/(ab).
  Proof. With p = kab − a − b, for every (a, b, k): 4/p = 4/(kab) + 4/(pkb) + 4/(pka)  and  4/p = 4/(a(bk−1)) + 4/(pak) + 4/(pak(bk−1))
  (check: 4/(pak) + 4/(pak(bk−1)) = 4b/(pa(bk−1)), plus 4/(a(bk−1)) gives 4(p+b)/(pa(bk−1)) = 4/p). The first is three unit fractions
  iff 4 | k (BN), the second iff 4 | a (B4 with Y = a), and a ↔ b gives 4 | b. Conversely BN = (4 | k), B4 = (4 | a) by (U2). ∎
  (Without the "4 |" clause the condition is vacuous: k = 1 gives p + 1 = (a−1)(b−1) for any factorization. The 4 is the 4 of 4/p.)

Least witness. Let g*(p) := min{g ≡ 3 (4) : p^{±1} mod g ∈ R_g} (U5), with min ∅ = +∞ (finiteness for all p is the open statement). CERTIFIED (`scripts/z60_lopezt_leastg.c`,
`data/z60/lopezt/leastg_1e8.txt`): over the 719 781 primes p ≡ 1 (24) below 10⁸, g* ≤ 10487 (attained at p = 9 658 489; no new record
in [10⁷, 10⁸]); g* = 7 for 50.06 %, g* ≤ 23 for 90.1 %, g* > 1000 for 172 primes, g* > 3000 for 12. So the pointwise statement is a
Linnik-type problem ("least modulus g with p^{±1} ∈ R_g") whose worst cases are far above log p.

Proposition 3.1 (PROVED). For every M there are infinitely many primes p ≡ 1 (24) with g*(p) > M, and the least of them satisfies
log p ≤ (5 + o(1))·M (Xylouris' Linnik constant 5). Hence g*(p) ≥ (1/5 − o(1))·log p for infinitely many p ≡ 1 (24).
Proof. Take p ≡ 1 (mod L), L := lcm(24, {g ≡ 3 (4), g ≤ M}) ≤ 24·lcm(1..M) = e^{M(1+o(1))}. For every g ≤ M, p ≡ 1 is a square mod g,
while R_g ∪ R_g^{−1} ⊂ {x : (x/g) = −1} (Lemma 1.1(i)); so no witness g ≤ M. Dirichlet gives infinitely many such p, Linnik the size. ∎
Remark. Any witness g has a prime factor q with (p/q) = −1, so g*(p) ≥ n_p := least prime q with (p/q) = −1; the Graham–Ringrose
primes (n_p ≫ log p·log log log p) give a slightly better lower bound for infinitely many p (not checked that their construction
respects p ≡ 1 mod 24 — EVIDENCE level). Under GRH, n_p ≪ (log p)², but that is only a lower bound for g*, not an upper bound.

### 3.2 Constructive routes (scoped assessments: what is PROVED is stated as such; the rest is my judgement, not an impossibility theorem)
(C1) Finite covering by congruences on p: impossible by Lemma 1.2, even inside p ≡ 1 (24), even using all Type I/II families (all
     residue sets are non-residue sets; p ≡ 1 mod L defeats every modulus ≤ M).
(C2) "Explicit g as a function of p" (g > p). Witnesses satisfy g ≤ 2p + 1 (Lemma 1.1(ii)). For p ≡ 1 (mod 8) the witnesses with g > p
     are exactly the BN ones g = p + a with a | p + 1 and (p+1)/a ≡ 3 (mod 4) (a B4 witness g > p would be g = (tp+1)/(t−1) with
     4(t−1) | p + 1, impossible as p + 1 ≡ 2 mod 8; a BN witness g > p has p + a = g, i.e. 4a | p + a + 1). So witnesses above p exist iff
     (p+1)/2 has a prime factor ≡ 3 (mod 4) — the t = 1 covering condition — and otherwise every witness is a proper divisor of some
     p + a or ap + 1 with g ≤ p. (Checked for all primes p ≡ 1 (8), p < 6000.) Hence "g as a formula in p" is just the a = 1 case.
(C3) A single prime witness q: hit ⟺ p mod q ∈ S_q with |S_q| ≤ 2τ((q+1)/4) ≪ q^ε, versus (q−1)/2 non-residue classes. Knowing a prime q
     with (p/q) = −1 (even the least one) therefore gives nothing: p mod q must land in a q^{ε}-sized set.
(C4) Composite witnesses g = q₁q₂…: the same t must work for all q_i (t | (g+1)/4, tp ≡ −1 mod each q_i); choosing q₂ to fix the second
     condition means q₂ | tp + 1 — i.e. we must again *factor* tp + 1. Circular.
(C5) Additive flexibility (Type I: ab | (mp+1)/4 with m | a + b) does not escape (C1): sub-products of residues lying in a proper
     subgroup H ∌ −1 never sum to 0 mod m when −1 ∉ H (m ≡ 3 mod 4), the same non-residue wall.

### 3.3 Counting routes (why pointwise positivity does not come out)
N(p) = Σ_{g ≡ 3 (4)} 1[p^{±1} mod g ∈ R_g]. Swapping to "small divisors" does not help: for a fixed g the only candidate a is
a = (−p mod g), and the event a | (g+1)/4 is a single 0/1 event of "probability" τ((g+1)/4)/g. In the classical short-interval divisor
sum Σ_{n ∈ (p, p+A]} τ(n) every d ≤ A contributes ≥ 1 *pointwise* because the class condition is independent of the shift; here the class
is −1 mod 4(n − p), so the one candidate shift is pinned by g and nothing is forced. HEURISTIC model (not a theorem): treating the events as independent with
probability |R_g ∪ R_g^{−1}|/φ(g) ≤ 2τ((g+1)/4)/φ(g) (NOT /g: at g = 15, |R_g ∪ R_g^{−1}| = 4 and 4/φ(15) = 1/2 > 2τ(4)/15) gives an
expected count ≪ Σ_{g ≤ X} τ((g+1)/4)/φ(g) ≍ (log X)², and the same order with (g+1)/8 for the 8-analogue; I do not claim the
constants (conditioning on p ≡ 1 (24), the branch overlap and the φ(g)/g factor all enter), only that the 8-family is the thinner one. I did not prove any almost-all statement in this memo and claim none: a sieve for the exceptional primes would have unbounded
dimension and would at best give an almost-all bound, which the brief excludes anyway.

### 3.4 What exactly would suffice (the reduced analytic statement)
(P*) For every large prime p ≡ 1 (24) there is g ≡ 3 (mod 4), g ≤ 2p + 1, with  (−p mod g) | (g+1)/4  or  (−p·4^{−1} mod g) | (g+1)/4.
Equivalently (U1/U3/U4/U5/U6). I found no route to (P*) that is not equivalent to controlling the factorization of an individual
number of the form p + a or ap + 1 beyond its small prime factors. The 8-analogue (P*₈) has the identical shape with (g+1)/8, g ≡ 7 (8),
(and 8^{−1} in place of 4^{−1}), and is false 45 times below 4·10⁶; a proof of (P*) must therefore use witnesses with g ≡ 3 (mod 8), or
with (U5)-divisor d ∤ (g+1)/8 (a odd on the B4 shift coordinate; see Sharpened (F2) in §1) — the 2-adic slack between "4" and "8" — at
least below 3 869 153, and cannot be a pure main-term argument.

### 3.5 (U7): the four residue classes of a (PROVED; `scripts/z60_lopezt_u7.c` agrees with (U5) on all n ≡ 1 (4), n ≤ 2·10⁴)
Write p + a = d·b with d ≡ −1 (mod a) (U6 with k = (d+1)/a). Reducing the three 4-conditions mod 4 (p ≡ 1 mod 4):
  a ≡ 0 (4): hit ⟺ p + a has a divisor ≡ −1 (mod a)            [any d; b ≡ d ≡ 3 mod 4 automatically]
  a ≡ 1 (4): hit ⟺ (p + a)/2 has a divisor ≡ −1 (mod 4a)       [p + a ≡ 2 mod 4 kills 4 | b; need 4a | d + 1]
  a ≡ 2 (4): hit ⟺ p + a has a divisor ≡ −1 (mod 4a)           [p + a odd; need 4a | d + 1]
  a ≡ 3 (4): hit ⟺ (p + a)/4 has a divisor ≡ −1 (mod a)        [p + a ≡ 0 mod 4: 4a | d + 1 ⇒ 4 | b, so "4 | b" is the whole condition]
So S(p) has two *cheap* sub-families where the modulus is a itself (a ≡ 0, 3 mod 4) and two with modulus 4a. For p ≡ 1 (24), a = 3:
(p+3)/4 = 6j+1 needs a prime factor ≡ 2 (3); a = 4: p + 4 needs a prime factor ≡ 3 (4); a = 7: (p+7)/4 needs a divisor ≡ 6 (7).
(The a ≡ 3 case subsumes, for d even, B4-witnesses with Y = b, so the two branches are interleaved already at a = 3.)

**Status of the pointwise statement: NOT PROVED. No hot lead.** Items are labelled PROVED / CERTIFIED / HEURISTIC individually above;
nothing conditional is claimed, because every conditional form I could formulate was either equivalent to (P*) itself or an almost-all
statement (which I also do not claim to have proved).

## §4 Falsifiers re-stated against the final content, and verdict

(F1) odd squares. Assumptions used, by place: primality of p only in the classification Lemmas 0.3/0.4/2.1/2.2 (never in an existence
argument for S); p ≡ 1 (mod 4) in the "m ≡ 3 (4)" form of Type I and in the mod-4 case analysis of (U7); the obstruction Lemma 0.5/1.1(i)
holds for every odd n: every witness modulus g has (n/g) = −1, so S(m²) is empty. No argument in this memo produces a divisor witness
(g with p^{±1} mod g ∈ R_g, which is far more than (p/g) = −1, cf. (C3)) for all p; (P*) *is* that statement. Any proof must supply a
prime factor q of some p + a or ap + 1 with (p/q) = −1 inside such a witness — the step with no analogue at n = m².
(F2) numerator 8. The 8-analogue is (P*₈): g ≡ 7 (8), a | (g+1)/8 (Lemma 1.1(iii); certified: exactly the 45 primes of the brief). Any
argument for (P*) that only uses the main term Σ_g τ((g+1)/4)/g would apply to (P*₈) with half the constant and is therefore wrong below
3 869 153; a proof must use witnesses with g ≡ 3 (mod 8) or with (U5)-divisor d ∤ (g+1)/8 (§1, Sharpened (F2)).
  Screen rows (CERTIFIED by search, `scripts/z60_lopezt_screens.py`, output `data/z60/lopezt/screens_out.txt`): the 12 R₈-zero primes in
  [10¹⁰, 1.1·10¹⁰] (`r8_zeros_1e10.txt`) all have B4 witnesses (least g: 11, 3, 131, 87, 11087, 3, 3, 3, 15, 3, 39, 3), all have BN
  witnesses, and all have numerator-8 B4-analogue witnesses (least g: 1479, 159, 2239, 111, 11087, 143, 447, 143, 15, 1663, 39, 31).
  They refute the C-even star sub-line only, not S₈ or Type II.
(F3) 105 and 4545. S(105) and S(4545) fail; 105 has an off-axis Type II witness (a, m, g) = (3, 2, 71), 4545 none. So "S holds for all
non-squares" is false and "S ⟸ Type II" is false for general odd n (for primes it is open: no prime ≤ 10¹⁰ separates them, and 105 shows
there is no *universal* algebraic conversion of off-axis witnesses into axis witnesses; a conversion using primality is not excluded).
  Screen row (CERTIFIED, `screens_out.txt`): all 285 non-square composite BN-zeros of `composite_zeros_le8e6.txt` have BN count 0 by
  definition; 283 of them have a B4 witness (search g ≤ 4·10⁶), the two without are exactly 105 and 4545 (whose absence of any witness is
  certified by the exhaustive runs of §0/§1).
(F4) single-branch zeros. B4 alone fails at 193, 2521, 66529; BN alone at the 14 primes of `star_prime_zeros.txt` (both lists reproduced
≤ 2·10⁵ by the now cutoff-free `z60_lopezt_branches.c`). Screen rows (CERTIFIED, `screens_out.txt`): all 14 star zeros have B4 witnesses
(least g: 7, 7, 39, 111, 7, 679, 23, 15, 23, 7, 39, 1735, 87, 111); all 38 G*-zeros of `gstar_zeros.txt` have B4 witnesses, exactly 24 of
them also have BN witnesses (the two largest ones at g = 2 953 943 for p = 85 664 329 and g = 2 741 075 for p = 564 661 441,
`scripts/z60_lopezt_bnfind.c`), and the 14 BN-less G*-zeros are exactly the 14 star zeros (star ⊂ G*). In (U5) they are p ∉ R_g^{−1} ∀g resp. p ∉ R_g ∀g; the inversion symmetry (Lemma 1.1) shows the two branches are on equal
footing, and the record list in `leastg_1e8.txt` shows both branches supplying the least witness in the worst cases.

**Verdict.** NOT PROVED; no HOT LEAD. Delivered (all PROVED unless marked): the exact identities for both branches (B4's was not
obvious: 4/p = 1/(Y'(gk−1)) + 1/(pY'k) + 1/(pY'k(gk−1))), the complete Type I/II divisor-form classifications, the placement of S as the
two axes {a = 1} ∪ {m = 1} of the Type II lattice "mp + a has a divisor ≡ −1 (mod 4am)", the witness-modulus form (U5) with the
B4 = BN^{−1} symmetry, the forms (U6)/(U7), the no-finite-covering lemma and the Linnik lower bound g*(p) ≫ log p (Prop 3.1),
the certified 8-analogue, and the g*(p) statistics to 10⁸ (CERTIFIED). What is missing is precisely a pointwise handle on the
factorization of individual shifted numbers p + a, ap + 1 in residue classes tied to a — the same wall as ES itself.

Prior work (per the cross-model review; I did not read these memos, per the lane rules): (U5) and the B4 = BN^{−1} inversion symmetry,
including the full ratio set, are already in `Z59_CONV2.md` Lemma 1(vi), which also records the 45 S₈-union zeros ≡ 1 (4) below 10⁸
(61 over all odd primes) and the 285/12/38 screen behaviour and {105, 4545} to 10¹⁰; the branch identities, the three B4 exceptions and
the union conjecture are credited to López in `B1_LINE.md` §§0–2 (B4 census to 10¹¹); the Type II divisor forms, both axes, the Jacobi
obstruction and the no-finite-covering theorem are in `Z58_CONVF.md` Lemmas 1.1–1.4 (after Elsholtz–Tao and López); `CLASS_FORCING.md`
§1 has both the p + 4d and cp + 1 lines. So everything structural here is an independent rederivation and verification, not a discovery;
the incremental deliverables are the (U7) case split, Prop 3.1, and the least-witness census `leastg_1e8.txt`.

Cross-model review (`data/z60/xreview/REVIEW_LOPEZT.md`, verdict ACCEPT-WITH-FIXES) — fixes applied: (1) the 2-adic slack / Sharpened (F2)
statement is now given in (U5)-divisor coordinates with the branch-dependent shift-coordinate form and the p = 83449 example; (2) the
false inequality |R_g ∪ R_g^{−1}|/φ(g) ≤ 2τ(Q)/g replaced by the φ(g) version and the unsupported constants withdrawn; (3) the F2/F3/F4
screen rows (12 R₈-zeros, 285 composites, 14 + 38 primes) added and certified by `z60_lopezt_screens.py`; (4) prior-work attribution added;
(5) Lemma 0.4 typo (p | 4abw − 1), Type II search bound, enlarged-vs-restricted BN justification fixed; the heuristic cutoff removed from
`z60_lopezt_branches.c` (rerun ≤ 2·10⁵, identical output); (6) C2–C5 and the counting remarks re-scoped as assessments, not impossibility
theorems. The verdict (NOT PROVED, no hot lead) is unchanged.

Files: `scripts/z60_lopezt_{branches,u5,u7,leastg,bnfind}.c`, `scripts/z60_lopezt_{identsearch,typecheck,bigg,screens}.py`, `data/z60/lopezt/`.
