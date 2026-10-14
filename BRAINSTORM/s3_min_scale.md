# s3_min_scale — (J)25 finite box × (J)28 Dirichlet shot × (J)30 Weil scale: the box size is a red herring

**Combines:** (J)25 (ES certificate modulus O(p²), finite search), (J)28 (ES^□ from the least prime g ≡ 3 (4) with
(p/g) = −1), (J)30 (FF mute certificates of degree ≤ 4 log_q deg P + C, i.e. |f| polylog in |P|).

## Idea
The wave's Assessment contrasts "ES: finite O(p²) search" with "variants: infinite fixed-modulus search". Test the
actual scale at which certificates appear: least Type II modulus h_min(p) versus the ES^□ Dirichlet prime g_box(p).

## Literature
Bach (least non-residue ≪ log² under GRH), Burgess (p^{1/(4√e)+ε}); Elsholtz–Tao mean log³p; FF_MUTE Thm 3.5.

## Barrier screen
Not a mechanism; recalibration. B3: a typical small h_min is consistent with the polylog lottery (the mean count of
certificates with h ≤ H is ≈ log³H-type, so small h are expected to fire).

## Cheap numerics (`scripts/s3_min_scale.py 10000000`, 8 s; primes p ≡ 1 (mod 4), 5 ≤ p < 10⁷, Type II only)
| | mean | median | 99% | max |
|---|---|---|---|---|
| h_min (ES) | 8.8 | 3 | 71 | 2495 (p = 2 031 121) |
| g_box (ES^□) | 7.8 | 3 | 43 | 139 (p = 9 665 041) |
max h_min / log³p = 0.814 (≤ 0.82), max g_box / log²p = 1.46; h_min ≤ g_box for 91.8% of primes (to 10⁶: max h_min = 419).

## Assessment
EVIDENCE: both searches end at polylog scale in practice; the O(p²) bound (J)25 is a worst-case bound, never
approached. The real difference between ES and its relaxations is the *type of firing condition* — a quadratic
character (density ½ among primes, Dirichlet/Chebotarev) versus box membership −p ∈ Box((h+1)/4) (probability ≈ τ₃/h,
B2) — not the finiteness of the search. In FF the mute certificates sit at the Weil scale for the same reason (a
character condition). So (E2) "a new finite-search mechanism" is not handicapped by finiteness per se; it must
produce a divisor-box event, i.e. it faces B2 directly. CONJECTURE-level remark (not pursued): h_min(p) ≪ log³p.
Promise 0 (recalibration only).
