# Z65_LIFT — characteristic-p construction + lifting for ES certificates (wave z65, lane LIFT)

**ES is OPEN.** Nothing here proves or disproves ES, (MS) or any case of them. Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief: `z52bbriefs/z65_lanes.md` §LIFT (+ z58
common rules, z53 depth brief). Scripts `scripts/z65_lift_*`, data `data/z65/lift/`.

*Status: CHECKPOINT 1 (skeleton, first theorem, pre-registered kill tests). Final sections to follow.*

## 0. Mandatory falsifier table (checkpoint-1 version; restated at the end)

The mechanism under test: *build in characteristic p an object (curve with automorphisms, special G-deformation datum,
stable G-map) and lift it to characteristic 0 so that the lift is an ES certificate at p* (via Lemma A of
`Z64_EQUIV.md`: ES(p) ⟺ ∃ (X, G) in char 0 with |G|(p − 4) = p(2g − 2)).

| screen | behaviour of the mechanism |
|---|---|
| **F1 odd squares** | Characteristic p must be the prime p; at n = m² there is no characteristic m (one can only work in char ℓ \| m, where the wild denominators are ℓ, not m²). ES itself holds at m², so F1 bites only on (★)/Type II sub-statements: the lift of a char-p object is a cover whose signature is read off from char-p inertia data (§4), so a (★)-certificate at m² would have to be present as data — impossible by T1. The good-reduction branch (Theorem G) produces only Mordell's p ≡ 2 (3) identity, which never applies at m² ≡ 0, 1 (3). |
| **F2 C-even / numerator 8** | Lemma A has a numerator-8 twin (8/n − 1 as an orbifold χ); Theorem G's p-adic argument is numerator-specific (it uses 4/p), its 8/p analogue is a separate computation (§3.5). The lifting step is numerator-blind. |
| **F3 composites** | The characteristic is prime by definition; the mechanism is undefined at composite n except via a prime factor (where ES is inherited anyway). Primality enters as "the residue characteristic", nothing more. |
| **F4 known zeros** | The 14 (★)-zero primes are all ≡ 1 (mod 3) or ≡ 2 (mod 3)? — Theorem G only "proves" ES at p ≡ 2 (3) (Mordell, already known for all such p), so it cannot prove anything false at the zeros; the bad-reduction branch reduces to choosing the triple (type I), so it proves nothing at all by itself. |

No HOT LEAD at checkpoint 1.

## 1. Precise statements attacked

* **ES(p)** (p prime ≡ 1 mod 4, p ≥ 5) ⟺ (Lemma A of Z64_EQUIV, PROVED there) ∃ compact Riemann surface X, g ≥ 2, and
  finite G ≤ Aut(X) with |G|(p − 4) = p(2g − 2); for such p every such (X, G) has X/G ≅ P¹ with exactly three cone
  points of orders (x, y, z), 1/x + 1/y + 1/z = 4/p (Z64_EQUIV Cor. to Lemma A).
* **Mechanism (Ch-ES).** Construct, over k = F̄_p, an object Ω whose lift to characteristic 0 (via a lifting
  theorem: Grothendieck tame lifting; Oort–Sekiguchi–Suwa / Green–Matignon / Obus–Wewers–Pop for cyclic groups;
  Bouw–Wewers for dihedral; Wewers's lifting of special G-maps, the one SWZ use) is a pair (X, G) as in Lemma A.
  Two branches:
  * **(GR) good reduction:** Ω = a smooth projective curve X_k with a G-action; the lift is a smooth relative curve
    over a mixed-characteristic DVR with G-action.
  * **(BR) bad reduction:** Ω = a special stable G-map / special G-deformation datum (Raynaud, Wewers); the lift is
    a three-point G-cover whose stable reduction is Ω. This is the branch SWZ use for Hurwitz.
* **Questions (brief):** (1) SWZ's mechanism precisely; (2) can (GR) or (BR) produce ES certificates at p, and where
  does T1 bite; (3) a theorem, a precise obstruction, or a precise missing lemma.

**Why not already closed.** Z64_EQUIV Lemma H only shows prime-degree *realisability* carries no (★) information; it
does not test the *mechanism* (char-p construction + lifting) on the ES dictionary rows. `git grep` finds no prior
repo analysis of reduction types of ES covers (0 hits for "potentially good reduction", "Oort conjecture",
"deformation datum" outside Z64_EQUIV's precedent row).

## 2. SWZ's mechanism (✔ read from arXiv:2609.20572v1, PDF archived at `data/z65/lift/src/swz.pdf`)

(to be completed: §2 in the final memo — M1 EKS reduction to three branch values; M2 Henrio-moment primitive tails
P_Λ with P_Λ′ = c∏(y − a_j)^{e_j − 1} (Lemma 5.3), the step where Σe_j = p ≡ 0 and no proper sub-sum ≡ 0 (mod p) is
used; M3 logarithmic special G-deformation datum in G ≤ S_p with regular C_p and N(P) = P ⋊ F_p^× (Lemma 2.5);
M4 Wewers lifting interface (Thm 4.8) with tame inertia preserved (Lemma 4.7); M5 point-stabiliser quotient.)

## 3. First theorem: the good-reduction branch gives only Mordell's identity

**Theorem G (PROVED, modulo the standard facts cited in G0).** Let p ≥ 5 be a prime, p ≡ 1 (mod 4). Let K be a field
of characteristic 0, complete for a discrete valuation with residue characteristic p, X/K a smooth projective
geometrically connected curve of genus g and G ≤ Aut_{K̄}(X) a finite group with |G|(p − 4) = p(2g − 2). If X has
potentially good reduction, then p ≡ 2 (mod 3) and X/G has signature (0; m, p, pm) with m = (p + 1)/3 — Mordell's
identity 4/p = 1/m + 1/p + 1/(pm). Conversely, for every prime p ≡ 2 (mod 3) such (X, G) with good reduction exist
(G cyclic of order pm; special fibre z^m = y^p − y).

*Corollary (PROVED).* For p ≡ 1 (mod 3) — in particular for every p in Mordell's hard classes 𝔐 mod 840 — every ES
certificate (X, G) at p has bad reduction at p. So "construct a smooth curve with automorphisms in characteristic p
and lift it equivariantly" (any lifting theorem of Oort type) cannot give ES at any p ≡ 1 (mod 3).

### 3.1 Proof

**G0 (set-up; standard).** After a finite extension of K, X has good reduction: a smooth proper model X_R over the
valuation ring R (residue field k, which we may take algebraically closed after unramified base change and
completion). g ≥ 2 since p ≥ 5. The smooth model is the stable model, hence unique, so G acts on X_R; and G acts
faithfully on X_k (the automorphism scheme of a stable curve is finite and unramified, Deligne–Mumford 1969 Thm 1.11
— source check pending, §7). For a closed point τ̃ ∈ X_k with stabiliser (= inertia, k algebraically closed)
I ≤ G, the completed local ring is R[[Z]] with I acting R-linearly; write i(g) := ord_z(ḡ(z) − z) ≥ 1 for
g ∈ I ∖ {1} (finite because the action on X_k is faithful). Standard (Serre, Local Fields IV §1–2): I = P ⋊ C_m with
P the p-Sylow (normal), p ∤ m, and i(g) = 1 for g ∈ I ∖ P, i(g) ≥ 2 for g ∈ P ∖ {1}.

**G1 (fixed points, Weierstrass).** Let D be the open unit disc over ℂ_p (the C_p-points of X_K reducing to τ̃).
Every g ∈ I ∖ {1} has exactly i(g) fixed points in D, all simple. *Proof.* g(Z) − Z ∈ R[[Z]] reduces to
ḡ(z) − z ≠ 0 of order i(g); by Weierstrass preparation it is a unit times a distinguished polynomial of degree i(g),
so it has i(g) zeros in D counted with multiplicity. At a fixed point w the derivative g′(w) is a root of unity
(g has finite order and is linearisable at w in characteristic 0); g′(w) = 1 would make g the identity near w, hence
globally. So every zero is simple. ∎

**G2 (cluster identities).** Let τ ∈ X_k/G be the image of τ̃ and let c_1, …, c_s be the cone points of X_K/G whose
G-orbits meet D (the *cluster* of τ), with orders e_i = |Stab| and p-parts π_i (so e_i = π_i e′_i, p ∤ e′_i). Then
  (a) Σ_i (1 − 1/e′_i) = 1 − 1/m,
  (b) Σ_i (|P|·m/e_i)(π_i − 1) = Σ_{g ∈ P∖1} i(g) ≥ 2(|P| − 1).
*Proof.* If g ∈ G fixes w ∈ D then g fixes the specialisation τ̃, so Stab_G(w) ≤ I; the orbit of a cone point meets D
in one I-orbit of size |I|/e_i, whose stabilisers are conjugate cyclic groups of order e_i; as P is the unique Sylow-p
of I, Stab ∩ P has order π_i. Count pairs (g, w) with g ∈ I ∖ P, w ∈ D, gw = w: by G1 it is Σ_{g∈I∖P} 1 = |I| − |P|;
by points it is Σ_i (|I|/e_i)(e_i − π_i). Divide by |I| = |P|m: (a). Count pairs with g ∈ P ∖ 1: by G1,
Σ i(g) ≥ 2(|P| − 1); by points Σ_i (|I|/e_i)(π_i − 1): (b). ∎

**G3 (cluster shapes).** (i) If τ is unramified (I = 1) its cluster is empty. (ii) If τ is tame (P = 1, m ≥ 2) its
cluster is one cone point of order m. (iii) If τ is wild (P ≠ 1) its cluster has ≥ 2 points; if m ≥ 2 exactly one of
them has e′ = m and all others are pure p-powers (e = π ≥ p); if m = 1 all are pure p-powers.
*Proof.* Terms 1 − 1/e′ with e′ ≥ 2 are ≥ 1/2 and 1 − 1/m < 1, so (a) allows at most one non-zero term, equal to
1 − 1/m; it is present iff m ≥ 2. (i), (ii) follow ((ii): the point has e′ = m and π = 1). In (iii), if the cluster
had a single point, (b) would read (|P|/π)(π − 1) < |P| ≤ 2(|P| − 1) (m-point, or m = 1), a contradiction. ∎

**G4 (assembly).** By §1, X_K/G ≅ P¹ with three cone points (x, y, z), Σ 1/· = 4/p. Each cone point lies in exactly
one cluster. Since 4/p = Σ 1/· forces p | lcm(x, y, z), some cone point has p | e, and its cluster belongs to a wild τ
(its stabiliser lies in I_τ). Two wild clusters would need ≥ 4 points (G3(iii)), so there is exactly one wild cluster W,
|W| ∈ {2, 3}, and the remaining cone point (if any) is a tame singleton with order prime to p.
* |W| = 3. All but at most one of x, y, z are powers of p. If all three are p-powers p^{b_i}: with B = max b_i,
  4p^{B−1} = Σ p^{B−b_i}; B = 1 gives 4 = 3; B ≥ 2 gives #{i : b_i = B} ≡ 0 (mod p), impossible for 1 ≤ # ≤ 3 < p.
  If exactly one, say x = π m′ with m′ ≥ 2 prime to p, is not a p-power: 1/x = 4/p − p^{−b_2} − p^{−b_3} has
  denominator a power of p, so m′ | p^B, contradiction.
* |W| = 2, tame singleton x (p ∤ x). The cluster is {π_1 m, p^b} with m ≥ 2 (if m = 1 both are p-powers,
  1/x = 4/p − p^{−b_1} − p^{−b_2} has v_p < 0 unless b_1 = b_2 = 1, which gives 1/x = 2/p: impossible) or the m = 1
  case just excluded. If π_1 = 1: 1/x + 1/m = 4/p − p^{−b} has v_p = −1 (b = 1) or −b (b ≥ 2) < 0 while the left side
  has v_p ≥ 0: impossible. So π_1 = p^a, a ≥ 1, and 1/x = 4/p − 1/(p^a m) − 1/p^b with v_p(1/x) ≥ 0.
  If a ≠ b the term of larger exponent max(a, b) ≥ 2 is the unique one of minimal valuation: v_p < 0, impossible.
  If a = b ≥ 2: 1/x = (4p^{a−1}m − m − 1)/(p^a m); gcd(4p^{a−1}m − m − 1, m) = 1 so the numerator is a power p^j
  with j ≤ a; it is ≥ (4p^{a−1} − 1)m − 1 > p^{a−1}, so j = a and m = (p^a + 1)/(4p^{a−1} − 1); reducing
  4(p^a + 1) ≡ p + 4 modulo the odd number 4p^{a−1} − 1 forces 4p^{a−1} − 1 ≤ p + 4, false for a ≥ 2, p ≥ 5.
  If a = b = 1: 1/x = (3m − 1)/(pm); p ∤ x forces p | 3m − 1, and gcd(m, 3m − 1) = 1 forces 3m − 1 | p, so
  3m − 1 = p and x = m. ∎

*Converse.* For p ≡ 2 (3), m = (p+1)/3: X_k : z^m = y^p − y with G = ⟨y ↦ y + 1⟩ × ⟨z ↦ ζ_m z⟩ ≅ C_{pm}; X_k → X_k/G
= P¹_t (t = z^m) has a wild point over t = ∞ (inertia C_{pm}, lower jump h = m) and a tame point over t = 0 of order m;
g = (p − 1)(m − 1)/2 and (2g − 2)/(pm) = (p − 4)/p. Cyclic actions lift (Oort conjecture: Obus–Wewers + Pop, Annals
2014 — source check pending, §7), and Lemma A + Theorem G identify the lift's signature as (m, p, pm). ∎

### 3.2 Check (CERTIFIED, arithmetic half)
`scripts/z65_lift_goodred_check.py 400` → `data/z65/lift/goodred_check_400.txt`: all 2 256 representations
4/p = 1/x + 1/y + 1/z for primes 5 ≤ p ≤ 400 tested against the necessary cluster conditions of G3/G4 (any partition):
the survivors are exactly the 39 Mordell triples (m, p, pm), p ≡ 2 (3); 0 non-Mordell survivors. (Also: no
representation with p² dividing a denominator occurs in this range.)

## 4. The bad-reduction branch (SWZ's actual mechanism) — to be completed

Plan: (i) source-verify Raynaud 1999 / Wewers 2003 (special G-deformation data, σ-invariants, vanishing-cycles formula,
lifting); (ii) prove an order-preservation statement (the lift's ramification orders are read off the char-p datum:
SWZ Lemma 4.7 for primitive tails, G1-type counting for wild points), so (BR) can only realise a triple that is
already present as char-p data (type I in Z64_EQUIV §5); (iii) contrast with SWZ, where the discrete data (profiles,
hence σ_j = (r_j − 1)/(p − 1)) are *given* and the char-p work is a continuous existence problem over F̄_p (Henrio
moments), whereas for ES the discrete datum *is* the unknown and its char-0 realisation is already free (Riemann
existence); (iv) formulate the precise missing lemma (an ES/(★)-equivalent Hurwitz-type problem with p-determined
data).

## 5. Pre-registered kill tests (committed at checkpoint 1, before running)

* **KT1 (kills Theorem G).** Extend `z65_lift_goodred_check.py` to all primes 5 ≤ p ≤ 1500 (all representations).
  Any non-Mordell triple passing the G3/G4 cluster conditions refutes the G4 arithmetic. Additionally, an independent
  re-derivation of G2(a)/(b) on the explicit converse example (cyclic C_{pm}: cluster {pm, p}: (a) 0 + (1 − 1/m) =
  1 − 1/m; (b) 1·(p − 1) + m(p − 1) = (p − 1)(h + 1) with h = m) must hold exactly; a mismatch kills G2.
* **KT2 (kills the (BR) branch as a construction route, or revives it).** Decision rule fixed now: if every lifting
  theorem used for three-point covers (Wewers's special G-maps; SWZ Thm 4.8) determines the lifted ramification
  orders from the char-p datum (verified from the sources), then (BR) is declared DEAD as a *construction* of ES
  certificates (it can only realise a triple supplied as input). It is REVIVED only if some step produces discrete
  data not chosen in advance (e.g. via a canonical char-p object attached to p whose inertia data are forced).
* **KT3 (F2 twin).** Run the Theorem G arithmetic with 8/p in place of 4/p (p ≤ 1500). If the numerator-8 version
  also has only identity-type survivors, the obstruction is numerator-blind (as expected); a different survivor
  pattern is recorded either way.
