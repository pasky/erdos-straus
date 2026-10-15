# z1_depth_bits — 2-adic density at 4 versus 8 (brief angle 1): one fair bit per extra power of 2, correlated in practice (O224)

## Idea
Brief angle (1): does the 2-adic density at 4 differ from 8 so that the main term is forced positive at Planck scale?
After z1_fano_pigeonhole, a χ = −1 word has one or two isotropic pentagon vectors x, and "8 | entry" asks Q(x) ≡ 0 (mod 8),
a condition on x mod 4L: one extra 2-adic bit per isotropic pentagon vector. Measure this (cells), then test it on actual
words.

## Literature
MODEL_SPECIFIC Thm 3.1(b) (the cell fractions 7/12, 5/16 were recorded without explanation), §5 (mean counts f_m ≈ c_m log³p/m),
TRANSPORT_LAW / (J)45 (ee′ ∈ {1 + o, N + o, 1 + No}), Pomerance–Weingartner (8/n failures).

## Results
(a) PROVED at cell level for all k (FOUR_ADIC_INPUT Prop 1.4: the two even entries are independent uniform even residues in
each parity pattern), CERTIFIED for k ≤ 5 (all cells mod 32, `scripts/z1_depth_cells.py 5`): χ = −1 cells have one (2/3) or two (1/3) isotropic pentagon
vectors, and the S_{2^k} share is f_k = (2/3)2^{−(k−2)} + (1/3)(1 − (1 − 2^{−(k−2)})²): f₃ = 7/12, f₄ = 5/16, f₅ = 31/192, exactly
the published cell fractions. Uniform over n mod 16 (`z1_depth_bycls.py`).
(b) EVIDENCE (`scripts/z1_bits_words.py 5 4000`): on actual words of primes p ≡ 1 (4) < 4000 the S_8 share of χ = −1 words is
0.501, and independence of the bits would predict 0.82 primes with S_8(p) = ∅, against 12 observed. At 131 and 241
(`z1_w131.py`) no entry divisible by 4 has v₂ ≥ 3; the 2-part of tp + 1 is split evenly between A and A*. Bits are shared
by the words of one level (v₂(tp + 1)) and tied by the even-edge Ptolemy relation.

## Barrier screen
B3: for 4 the density conditional on χ = −1 is exactly 1, so there is no "main term" to force. The ES question is only
whether a χ = −1 word exists, and its count is the log²p lottery (SQ₅). For 8 the extra bits cut the main term by 7/12 at cell
level and by much more through correlation. This explains 8/131 and 8/241 without invoking anything 4-specific beyond
Thm 1.3. No Planck-scale positivity mechanism appears for either numerator. B6: pointwise statements only.

## Assessment
PROVED/CERTIFIED (a), EVIDENCE (b). The answer to angle (1) is negative but precise: 4 costs zero 2-adic bits, 8 costs one fair bit
per isotropic pentagon vector, and in practice these bits are strongly correlated inside one prime. A Siegel/mass main term
cannot separate the numerators at the level that matters, because for 4 the issue is not a density. Promise 1/5.
