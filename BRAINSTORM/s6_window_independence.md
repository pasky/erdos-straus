# s6_window_independence — distinct windows are independent lotteries (O238; why many forced windows do not help)

## Idea
Hope: there are ≍ π(Q)/4 forced windows q ≤ Q; cap 0 at ANY of them suffices. Can their budgets be correlated or glued?
**Prop (PROVED, trivial).** For windows m ≠ m′, K_m − K_{m′} = (m − m′)/4, so gcd(K_m, K_{m′}) | (m − m′)/4: the mute sets of
two windows share only primes below |m − m′|/4. Together with CAP_DOWN Prop 4.1 (one solution has one x), the cap-0 events
at different windows are driven by essentially disjoint sets of primes — independent lotteries, each with its own
forced bit.
Consequence (Assessment): the probability that all windows ≤ Q fail is a product of per-window failure probabilities, the
polylog lottery of B3 (average f(p) ≍ log³p); no pigeonhole over windows exists because the objects being pigeonholed
(the K_m) are pairwise almost coprime.

## Literature
CAP_DOWN Prop 4.1; ET (2013) on the average count; POINTWISE_SIZE.

## Barrier screen
B3/B6 (counting over windows), B2 at each window.

## Cheap numerics
data from `scripts/s6_witness_caps.py`: per-window cap-0 rate ≈ 34 % (forced) / 18 % (unforced) for small windows; the least
cap-0 window ≤ 63 for all p ≤ 10⁶ ((J)66) is consistent with ≈ independent coins.

## Assessment
PROVED (trivial gcd fact) + Assessment. Negative.
