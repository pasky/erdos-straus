# s7_typeII_free_controls — non-squares with no Type II solution: an enlarged T1 control set (O247, (v))

## Idea
T1 says every Type I/II route has a false step at odd squares. Any proposed Type II mechanism for primes must also be
false at the non-square n where f_II(n) = 0. Make that control set explicit.

**Lemma 1 (window bound; PROVED).** For odd n ≡ 1 (4), every Type II solution (gcd(x, n) = 1, n | y, z) has
n/4 < x ≤ n/2, so its window m = 4x − n satisfies m ≤ n. *Proof.* 4/n − 1/x = m/(nx) = (1/Y + 1/Z)/n with y = nY,
z = nZ, so m/x = 1/Y + 1/Z ≤ 2, i.e. 4x − n ≤ 2x. ∎ Hence f_II(n) = 0 is decided by the windows m ≤ n.

## Literature
Elsholtz–Tao Prop 1.6 (f_I = f_II = 0 at squares); CAP_DOWN §5 (n = 3985, no cap-0 window to 20 000).

## Barrier screen
T1 analogue: these n satisfy every local condition that a "forced" Type II argument could use (e.g. 3985 = 5·797 has
q ≡ 3 (4) windows with (q/n) = −1, so the (J)64 subgroup is forced) and still have no Type II solution. A pointwise
Type II theorem must use primality (or at least fail on this list).

## Cheap numerics (scripts/s7_typeII_free.py, s7_window_controls.py)
* Non-square n ≡ 1 (4) ≤ 2·10⁵ with f_II(n) = 0: 103 values: 21, 57, 93, 105, 141, 165, 177, 273, 345, 477, 561, 609,
  693, 1005, …, 1705 = 5·11·31, 3985 = 5·797, 4585 = 5·7·131, … — almost all divisible by 3 or 7 (the small windows
  3, 7 are then unavailable since gcd(m, n) = 1 is needed); 3985 is the only one ≤ 10⁶ with all prime factors ≡ 1 (4)
  (CAP_DOWN), and it is confirmed window-free for every m ≤ 1.2·10⁷ ⊇ [1, n].
* Its ES solutions exist (267 with x minimal), none of Type II shape (x coprime, n | y, n | z).
* Primes: f_II(p) ≥ 1 for all p ≤ 10⁸ (ledger EVIDENCE); here m₀(p) ≤ 107 for p ≤ 10⁷.

## Assessment
PROVED (Lemma 1) + EVIDENCE. Not a mechanism; a sharper control set than odd squares for any claimed Type II theorem.
The list thins out (lottery-like), so no structural T1 analogue is suggested at non-squares.
