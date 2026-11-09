# Z68_SIGN — can long-word sign information be transported to length-3 words? (lane SIGN, wave z68)

**ES is OPEN; nothing here proves or disproves ES, (S), SQ₅ or (MS).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief: `z52bbriefs/z68_lanes.md` §SIGN
(+ `z53_depth.md`, `z58_lanes.md` common rules / falsifier table). Scripts `scripts/z68_sign_*`, data `data/z68/sign/`.

*Status: CHECKPOINT 1 (gate in progress).*

Notation (DEDEKIND_ES = DK, Z64_SDEEP, Z64_SDEEPF). HJ word n/A = [[b₁,…,b_r]], b_i ≥ 2, r = r(n/A); continuant
K(b₁..b_r) = n; L_r(n) = {A : r(n/A) = r}; length-3 words n/A = [[v,t,u]] ⟺ tuv − u − v = n, A = tu − 1;
χ_n(A) = (A/n). λ(n) = min{r(n/A) : χ_n(A) = −1} (DK Cor 4.6). At primes p ≡ 1 (4), p > 5: (S)(p) ⟹ λ(p) ≤ 3 ⟹ ES(p).

## 0. Mandatory falsifier table (checkpoint version; final version §8)

The lane's object is a *transport* (bridge) from long-word sign information to L₃(p), or an obstruction to it.

| screen | behaviour of a transport / of the obstruction |
|---|---|
| **F1 odd squares** | χ_{m²} ≡ 1: every word of every length has sign +1 at m² (Jacobi). A transport is vacuous there (no −1 input). The obstruction theorems below are statements about non-square profiles / primes; squares enter only as the (trivial) closed set where no length has a −1 word. |
| **F2 C-even / numerator 8** | A transport whose output is only constrained to lie in an *admissible union of cells* would equally produce words in the C-even cell set {8 ∣ t} ⊂ (Jacobi −1 cells); that set is empty at the 12 certified R₈-zero primes in [10¹⁰, 1.1·10¹⁰] (and {4 ∣ t} at the 14 (★)-zero primes). Used as obstruction (O-c). |
| **F3 composites** | The sign/tail identities are valid for all odd n ≡ 1 (4); (S) has no known composite counterexample. Primality is not used by any obstruction here. |
| **F4 known zeros** | (S) holds at all 14 + 38 + 12 screen primes (Z64_SDEEPF f4_witnesses); 21841 has one −1 pair of 10 (Z64_SDEEP). Kill test KT4 below checks that nothing here "explains" 21841. |

## 1. Precise statements

* **Target (brief task 1, gate).** Find an exact map from a p-adaptive long-word object with controlled sign
  (bounded-digit HJ/CF word, Zaremba-type witness with χ_p = −1, a word of length R ≥ 4 with χ_p = −1, …) to an element
  of L₃(p) with χ_p = −1; or prove a precise obstruction.
* **Caveat confronted first (brief).** Fable-6's upside is λ(p) ≤ C log p. (S) is λ(p) ≤ 3 *with length exactly 3*
  (DK Cor 4.6: the five slices ⟺ λ(p) ≤ 3, length 2 being the boundary certificate). λ(p) ≤ C log p is not (S) and
  has no known ES consequence; the whole question is the bridge.

## 2. Gate log: bridge candidates examined (Assessment unless labelled)

Every candidate either preserves the length (so it never reaches L₃ from L_R, R ≠ 3), or reduces to (S) itself / B2:
1. *Klein group* (reversal A ↦ A*, duality A ↦ n − A): sign-preserving (DK 8.2), length-preserving resp.
   r ↦ Σ(b_i − 2) + 1. Duality maps L₃(n) onto the words of digit excess 2 (all letters 2 except one 4 or two 3's):
   L₃ *is* a bounded-alphabet long-word set under duality, but this is a relabelling, not a transport.
2. *Split identity* (PROVED, §3 Lemma 1): for every word and every position i,
   n = b_i·X·Y − X·Y′ − X′·Y and χ_n(A) = χ_n(X)χ_n(Y). Long words are "length-3 words with fractional outer
   letters" X/X′, Y/Y′; L₃ is the case X′ = Y′ = 1. No operation sets X′ = Y′ = 1 while preserving n.
3. *Multiplicative*: (S)(n) ⟺ ⟨L₃(n)⟩ ⊄ QR_n (QR_n is the unique index-2 subgroup at primes); a QNR from a long word
   transports iff it lies in ⟨L₃(n)⟩·QR — a restatement of (S).
4. *Homological* (F₂-relations between Euclidean loops in H₁(Γ₀(n); F₂)): done in Z63_EUCLID (Prop E3, KE1: generic
   length-3 loops are F₂-independent of everything else). Not redone.
5. *Multiples* (Lemma C/D of (J)95): relaxing the size condition certifies words of kp, not of p.
6. *n_p-adaptive letters*: putting v = q (a prime QNR) gives a good word iff p + q has a divisor u ≡ 3 (mod 4),
   u ≡ −p (mod q) (+ size) — a tied divisor event at level 4q (B2).

## 3. Obstruction programme (registered at checkpoint 1)

* **(O-a) Tail/split locality (PROVED, §3).** Sign of a word = χ_n(XY) for the fixed part around any letter; the
  family "all letters fixed except one (big) letter" is the residue class n ≡ −(X′Y + XY′) (mod XY). Hence
  λ(n) ≤ R is a covering statement by such classes with moduli XY up to ≍ n.
* **(O-b) Profinite separation 4 vs 3 (to be CERTIFIED / PROVED).** For a prime ℓ and a non-residue g, consider the
  profile e_{ℓ,g} (UCOVER). Length-3 good families catch only part of the non-residue classes at ℓ (UCOVER Thm S,
  ELL0 (S-all): never all, ℓ ≥ 11). Claim to test: length-4 good families catch *every* non-residue class at level 1.
  Consequence: no *local* transport (output fixed part determined by the input fixed part and n mod a modulus
  depending on it) from length-4 good words to length-3 good words exists — the profinite obstruction appears exactly
  at the last rung.
* **(O-c) Cell-uniformity (F2) obstruction.** Exact-denominator per-cell mixing at length 3 is false at certified
  primes (R₈ zeros, (★) zeros); a transport needing only cell admissibility of its target proves a false statement.

### Pre-registered kill tests (before any computation)
* **KT1 (O-b sharpness).** For every prime 11 ≤ ℓ ≤ 199 compute the set of non-residue classes g mod ℓ caught at
  level 1 by length-R good families, R = 3 (validate against UCOVER: ℓ = 11 uncaught {2, 6}, ℓ = 13 {2, 7},
  ℓ = 17 {3, 5, 6, 7}) and R = 4 (search bound XY ≤ B, B registered as 2·10⁶). *Kill of the sharp form "R₀ = 4":*
  some ℓ in range has a non-residue class uncaught at R = 4 (then report R₀(ℓ) = least R catching all, R ≤ 6).
* **KT2 (O-c).** Recompute at the 12 R₈-zero primes and at the 14 (★)-zero primes: L₃(p) ≠ ∅, −1 words exist, and no
  word lies in {8 ∣ t} resp. {4 ∣ t}. Kill (of O-c as stated) if any listed prime has such a word.
* **KT3 (information, EVIDENCE only).** Across primes p ≡ 1 (8) ≤ 2·10⁵, Spearman correlation between the length-3
  −1 fraction N₋/|L₃| and the length-4 −1 fraction. Registered reading: |ρ| < 0.1 ⟹ "long-word sign statistics
  carry no detectable information on the length-3 deficit"; |ρ| ≥ 0.3 ⟹ examine (a possible statistical bridge).
* **KT4 (brief).** Anything claimed must (a) give nothing at odd squares, (b) be consistent with 21841 (1 −1 pair of
  10), (c) not be a finite covering of a square class (ELL0).
