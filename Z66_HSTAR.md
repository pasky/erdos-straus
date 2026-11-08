# Z66_HSTAR — the missing Hurwitz-type lemma (H★): design and screening of realisation problems for (★)/Type II/(S) (wave z66, lane HSTAR). Status: CHECKPOINT 1

**ES is OPEN.** Nothing here proves or disproves ES, (MS), (★), Type II or (S) at any prime. Labels: PROVED /
CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief:
`z52bbriefs/z66_lanes.md` §HSTAR (+ z58 common rules, z53 depth brief). Scripts `scripts/z66_hstar_*`, data
`data/z66/hstar/` (literature notes with URLs and V/V2 flags: `data/z66/hstar/src/lit_hurwitz.md`,
`lit_geometry.md`, gathered by two research subagents; items used in proofs re-read by me are marked ✔).

## 0. Mandatory falsifier table (checkpoint-1 version; re-stated at the end)

Mechanism under test: a *realisation scheme* 𝔖 = (p ↦ datum 𝒟(p); objects realising 𝒟; extraction ε: realisation ↦
certificate), solved by an existence engine (char-p construction + lifting, or Riemann existence + group theory).

| screen | behaviour |
|---|---|
| **F1 odd squares** | If 𝒟(n) is defined for all odd n and every realisation yields a (★)/Type II/(S)-certificate, then 𝒟(m²) is non-realisable *automatically* (T1). So F1 bites on the **engine**: its hypotheses must fail at m². SWZ's engine (degree = p) passes F1 for free (it does not apply at composite degree), which is why it is attractive; but Lemma Ord (§3) shows its primality mechanism (self-centralising C_p) is incompatible with ES pairs. The near-Euclidean arithmetic Hurwitz families (CPZ, Petronio 3.13/3.14) are realisable at every odd square (Lemma N, §4): T1-blind. |
| **F2 C-even / numerator 8** | Lemma Ord has a numerator-k version (same proof; §3.3). Theorem T and Lemma 2V are numerator-blind. Nothing found distinguishes C odd from C even. |
| **F3 composites** | Engines keyed to "degree is prime" (SWZ) see composites only through EKS-type imprimitivity, which is a statement about the *degree*, not about R(n). Lemma 2V (two-square extraction) is defined only where n = x² + y². |
| **F4 known zeros** | All 14 (★)-zeros and 38 𝔊*-zeros are ≡ 1 (mod 12). Lemma Ord applies there (every ES pair needs an element of order pk, k ≥ 2). No engine examined proves anything at them. |

No HOT LEAD at checkpoint 1.

## 1. Precise statement attacked

**Definition (realisation scheme).** A realisation scheme for a target T ∈ {(★), Type II, (S), ES} is
𝔖 = (𝒟, Real, ε): for every odd n ≥ 5 a *datum* 𝒟(n) (finite combinatorial data: a group or degree, conjugacy
classes / partitions, a base orbifold, a characteristic) computable from n alone, a set Real(𝒟(n)) of realisations
(branched covers, G-curves, monodromy tuples, char-p curves, lattices, ...), and a map ε: Real(𝒟(n)) → Cert_T(n).
*Soundness:* ε is well defined at every n (so Real(𝒟(n)) ≠ ∅ ⟹ T(n)). An **(H★)** is a sound scheme together with an
*existence engine*: a theorem whose hypotheses hold at every prime p of a class 𝒫 (e.g. 𝔐 mod 840) and which
proves Real(𝒟(p)) ≠ ∅.

**Target statements (brief).** (a) Design an (H★) with 𝒟(p) fixed by p whose realisability fails at odd squares;
(b) decide whether char-p construction + lifting, or Riemann existence + group theory (PSL₂ generation, Conder-type
constructions), can be its engine. Labels: the existence of an (H★) with a working engine is **CONJECTURE-level
open**; the scoped no-go statements below are PROVED where marked.

**Why not already closed.** Z65_LIFT killed char-p + lifting *as a construction of ES curves* (Thm G, Prop O) and
named (H★) as the one surviving escape (§5.3), screening five candidate shapes without theorems. Z64_EQUIV Lemma H
only covers degree-p realisability (not extraction). Neither memo treats (i) extraction maps other than the
signature, (ii) the centraliser structure that ES pairs force, (iii) tame realisation problems, (iv) the verified
arithmetic Hurwitz families (CPZ/Petronio) as engines. `git grep` finds 0 hits for Kani, lifting invariant,
theta-characteristic, anti-isometry, Abhyankar, Pakovich (outside a source file); Zolotarev's sign dictionary is
known (`BRAINSTORM/bsB_zolotarev_transpose.md`: sign layer only) and is not redone.

## 2. Plan
* §3 Lemma Ord (PROVED + KT1 CERTIFIED): every ES signature at p has an entry pk, k ≥ 2 ⟹ every ES pair needs a
  p-element with non-p-group centraliser. Corollary: SWZ's mechanism (C_{S_p}(P) = P), PSL₂(p), AGL₁(p), A_p, S_p,
  … never carry ES pairs.
* §4 Theorem T (tame transparency, from Grothendieck/Obus Thm 1.5 ✔), Lemma N (near-Euclidean families T1-blind),
  Lemma 2V (polynomial extraction from two-square realisations = congruence menus), the fixed-shape lemma.
* §5 Design catalogue D1–D6 (block/imprimitivity at degree 4Cp+1; CPZ two-square engine; Fried–Serre lifting
  invariant; centraliser-split C_p × K; Γ₀(p) dessin loops; Kani anti-isometric gluing / CM factorisation), each
  screened with KT2.
* §6 engines; §7 verdict, falsifier table, FRONTIER text.

## 3. First lemma: ES pairs force large p-centralisers (Lemma Ord)

**Lemma Ord (PROVED).** Let p ≥ 5 be prime and 4/p = 1/x + 1/y + 1/z with x, y, z ≥ 1. Then some entry equals pk with
k ≥ 2 and p ∤ k.

*Proof.* By Z65_LIFT Lemma P no entry is divisible by p², so each entry is p·(unit) or prime to p.
* If p divides no entry, the sum has denominator prime to p; impossible.
* If p divides all three, x = px′ etc., then 1/x′ + 1/y′ + 1/z′ = 4 > 3; impossible.
* (Type I) p divides exactly x = px′. Then 1/y + 1/z = (4x′ − 1)/(px′) with p ∤ yz. Since gcd(4x′ − 1, x′) = 1, the
  right side has p in its reduced denominator unless p | 4x′ − 1. Hence 4x′ ≥ p + 1 and x′ ≥ (p + 1)/4 > 1.
* (Type II) p divides exactly x = px′ and y = py′. If x′ = y′ = 1 then 1/z = 2/p, impossible. So max(x′, y′) ≥ 2. ∎

(Type II with x′ = 1 forces 3y′ − 1 = p, z = y′: Mordell's triple (p, p(p+1)/3, (p+1)/3), whose entry p·(p+1)/3 has
k = (p+1)/3 ≥ 2.)

**Corollary Ord (PROVED, from Lemma Ord + Z64_EQUIV Lemma A and its Corollary).** Let p ≡ 1 (mod 4), p ≥ 5, and let
(X, G) be an ES pair at p (|G|(p − 4) = p(2g − 2)). Then G contains an element g of order pk with k ≥ 2, p ∤ k; hence
the subgroup P = ⟨g^k⟩ of order p has C_G(P) ∋ g, so C_G(P) is not a p-group. Consequently **no group in which every
element of order p has a p-group centraliser** carries an ES pair at p. This includes S_p and A_p (C(p-cycle) =
⟨p-cycle⟩), every transitive G ≤ S_p, AGL₁(𝔽_p), PSL₂(𝔽_p) and SL₂(𝔽_p)/{±1}-type groups with unipotent p-elements
(C(u) = unipotent radical), and every Frobenius group with kernel of order p.

*Proof.* By Lemma A's Corollary, X/G ≅ P¹ with three cone points of orders (x, y, z), 1/x + 1/y + 1/z = 4/p, and G is
generated by g₁, g₂, g₃ of exactly these orders (g₁g₂g₃ = 1). Apply Lemma Ord. ∎

*Reading (Assessment).* SWZ's Lemma 2.5 (C_{S_p}(P) = P, N_{S_p}(P) = P ⋊ 𝔽_p^×) is where their engine uses
primality. Corollary Ord says that this very structure is incompatible with ES pairs at every p ≡ 1 (4): an ES
certificate needs C_p *times something*. This sharpens Z65 Lemma S (which treated only monodromy groups of degree-p
covers with their own signature) to *all* curves with such group actions, and replaces Z65's PSL₂(p) remark by a
theorem.

**KT1 (CERTIFIED).** `scripts/z66_hstar_ord_check.py 3000` → `data/z66/hstar/kt1_ord_3000.txt`: all 8 334
representations 4/p = 1/x + 1/y + 1/z (x ≤ y ≤ z) for the 211 primes p ≡ 1 (4), 5 ≤ p ≤ 3000, contain an entry pk with
k ≥ 2, p ∤ k; 0 exceptions; 0 entries divisible by p². (A checkpoint draft expected Mordell exceptions; the script
showed none, which led to the correct statement above.)

### 3.3 Numerator k (F2)
**Lemma Ord_k (PROVED).** For k ≥ 4 and a prime p > k, every representation k/p = 1/x + 1/y + 1/z has an entry pk′
with k′ ≥ 2, p ∤ k′. *Proof.* No p² (Lemma P's proof: two entries of maximal valuation B ≥ 2 force
p/k < a ≤ p²/(kp − 2) < (p + 1)/k). Type III needs Σ1/x′ = k > 3. Type I needs p | kx′ − 1, so x′ ≥ (p + 1)/k > 1.
Type II with x′ = y′ = 1 needs z = p/(k − 2) ∈ ℤ, impossible for p > k ≥ 4. ∎ So Corollary Ord holds verbatim for
numerator 8 (F2): the C-even / 8/p line is treated identically.

## Pre-registered kill tests (checkpoint 1)
* **KT1** (kill Lemma Ord): any representation without an entry pk, k ≥ 2. → PASSED (above).
* **KT2** (design decision rule, fixed now): every design D in the §5 catalogue is classified by its engine as
  (a) *type I* — the engine realises only data that already contain a certificate; (b) *T1-blind* — the engine's
  hypotheses hold at odd squares m² in the same congruence class and ε would output a certificate there
  (contradicting T1, so ε cannot be sound with that engine); (c) *blocked by Lemma Ord / Theorem T* — the engine
  only produces groups with self-centralising p-elements, or is tame (char p adds nothing); (d) *survives*. **If
  every design lands in (a)–(c), the lane's verdict on (H★) via these engines is DEAD/narrowed as scoped
  theorems; any (d) is reported as a lead with its own falsifier table.**
* **KT3** (computational, for the block design D1): for 4C·n + 1 ≤ 40 (C = 1, 2), enumerate the candidate block
  datum's realisations by exhaustive search in S_N (N ≤ 13) or by character counts; KILL D1 if realisability does
  not coincide with "N has a divisor ≡ −1 (mod 4C)" on the tested range, or if a primitive realisation exists for
  some N with no such divisor.
