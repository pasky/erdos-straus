# bsG_sister_Ak_stern — Lorenzini's A_k lists, Stern popcount slices, and sister conjectures (W_k) (O180)

## Idea
Lorenzini lists conjectural complements L_{A_k} for the paths A₃…A₆. By the HJ dictionary, V_{A_k}(2) is the set of n having a fraction of HJ length k.
Make the Stern coding exact, then check the lists.

## Results
* **PROVED (LORENZINI_W Prop 7.1):** s(1 0^{a₁−2} 1 ⋯ 0^{a_k−2} 1) = K⁻(a₁,…,a_k) = d_{A_k}(a). So V_{A_k}(2) = {s(N) : popcount N = k+1}, and
  (W_k): "every n ∉ L_{A_k} is a Stern value at a position with exactly k+1 ones." This makes the "continuant in the gaps" remark of bsA_minkowski_stern M3 precise.
* EVIDENCE (`scripts/bsG_Ak.c`): the complements are exactly Lorenzini's lists. L_{A₃} (13 values incl. 0, 1) and L_{A₄} (28 values, max 314) below 10⁸;
  L_{A₅} (22 values, max 88) and L_{A₆} (46 values, max 236) below 10⁷.
* (W_k) ⟹ (W_{k+1})? No. The lists are not nested (e.g. 4 ∈ L_{A₄} but 4 ∉ L_{A₃}… 4 = (2,2,2)). Lengthening a word by a letter 2 maps
  n ↦ K⁻(a, 2) = 2n − n′, which is not monotone in any useful sense.
* Analogue of Prop 8.1 for A₄: dA₄(t,2,2,2) = 4t − 3 (Lorenzini Lemma 6.1: V ∋ n(t−1)+1), so n ≡ 1 (mod 4) is trivial for A₄. Similar
  fixed-pair families exist for every k. The open residues are again "n + small is prime/2-power" type.

## Literature
Lorenzini JNT 2024 §6 (Lemma 6.1, Ex. 6.2). Stern/Calkin–Wilf (Northshield, Monthly 2010). Defant (2016), max of s on fixed popcount.
Stanley–Wilf, refined Stern via b(n,k). Allouche–Shallit, 2-regular sequences. I found no result on the *image* of s on a popcount slice.

## Barrier screen
Same as (W): B1 via the sterile-set analogue, H-A for the residue. 2-regularity gives automaton structure on *positions*, but the question is about *values*.
Images of 2-regular sequences are not regular, so no decidability shortcut.

## Cheap numerics
`scripts/bsG_Ak.c k N`, `scripts/bsG_stern.py` (brute popcount-4 images agree with V_{A₃}(2) below 600 up to bit-length truncation).

## Assessment
PROVED dictionary + EVIDENCE confirming Lorenzini's four lists to 10⁷–10⁸. Promise 0 for ES; 1/5 as a framing for Lorenzini's problem.
