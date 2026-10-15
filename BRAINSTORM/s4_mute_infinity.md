# s4_mute_infinity — "muting ∞" vs muting a finite place: one table for every relaxation in the campaign (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md. Cross-combination O218 (3): c_∞-imitation (O211, (J)50) ×
the mute place of (J)30 × the three bits of s4_three_bits_meta.

## Idea
FF_MUTE ((J)30): one place whose condition is dropped ("mute") turns the ES-variant into a theorem. y3_frob_infinity:
the ES modulus must have Frobenius c_∞, i.e. imitate ∞. Combine: what does it mean to mute ∞ itself, and how does it
compare with muting a finite r? Classify each relaxation by (which bit is dropped) × (shot family finite/infinite) ×
(c_∞-modulus fixed/moving) × (T1?) × (status).

## The table (statuses are those of the ledger; new rows marked ★)
| variant | condition dropped / relaxed | shots at fixed n | c_∞ modulus | T1 | status |
|---|---|---|---|---|---|
| signed ES, 2-adic form (R₂) ★ | ε_∞ (positivity), keep 2-adic certificate | finite (|t| ≤ n+3) | moving | **no** | trivial — PROVED for all odd n ≥ 5 at t = −1 (R219 D10b) |
| signed ES, n-adic form (R_n) ★ | ε_∞, keep χ = −1 | finite (|t| ≤ n+3) | moving (t), slots doubled | yes (automatic) | lottery; CONJECTURE SQ_±, EVIDENCE to 10⁷, no finite t-set under Dickson (R219 D3) |
| ES^□ / M^□ ((J)28, (J)41) | den z may carry an odd square | infinite (Q free) | fixed (4 or M) | yes (shots) | PROVED (one Dirichlet prime) |
| ES^{(S)} ((J)23) | finite mute set S at fixed primes | infinite | fixed (4) | yes | PROVED (sieve) |
| ES^{(y)} ((J)34) | self-mute: primes of y | infinite | fixed | yes | PROVED |
| ES^{(y,1)}, ES^{[2]} ((J)36, (J)43) | cap 1 / den z \| y² | infinite (Pell) | moving (2AB) | yes | open (Markoff-type lottery) |
| FF mute place ((J)30) | one finite place of F_q(T) | infinite | fixed | n/a | PROVED |
| ES | nothing | finite (O(p²)) | moving | yes | open |

## Reading (Assessment, with the PROVED inputs cited in the table)
* **Muting ∞ is the cheapest and the worst mute:** it keeps the search finite and the modulus moving, and in the 2-adic
  form it loses T1. A finite mute place r works because r *replaces* ∞ as the place where the c_∞-type condition can be
  met at a fixed modulus with infinitely many shots (y3_frob_infinity: r ≡ −1 (mod m) is "r imitates ∞").
* The two features that separate theorems from ES are independent: (fixed c_∞-modulus) and (infinitely many shots).
  Every PROVED row has both; (R_n) has neither yet is empirically the easiest open row; ES^{[2]} has infinitely many
  shots but a moving modulus and is open. So "infinitely many shots" alone is not enough, and the ledger's phrase
  "fixed-modulus shot family" is the conjunction of both (consistent with (J)25, (J)34).
* ES needs a mechanism that, at a single n, supplies a *finite* place imitating ∞ for a modulus that is part of the
  solution — B2 restated as "the imitator of ∞ must be found inside the box". Positivity (∞ itself) cannot be that
  imitator: L1/L2 make ∞ the anchor that *creates* the requirement.

## Barrier screen
B2/B3 (box), T1 (column), B6 (sieves need infinitely many shots), (J)41 harness: all PROVED rows are
numerator-blind; (R_n) is numerator-free.

## Cheap numerics
`scripts/s4_sqpm.c` (SQ_± and the ES-five comparison, s4_three_bits_meta P3(c)).

## Assessment
A unified classification; the new entries are the two signed rows. No route: it locates the gap as "an imitator of ∞
inside the box". Promise 1/5 (useful as a steering table).
