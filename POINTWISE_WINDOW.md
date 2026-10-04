# POINTWISE_WINDOW — unconditional Ω-results for the window statistic `a_min(p)`

Task O10. Builds on `POINTWISE_SIZE.md` §§8–11 (window frame, Lemma 8.2,
Cor 8.3, Prop 8.4, Lemma 11.3, Prop 11.4, Assessment 11.5).
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. **Cited** = external theorem whose statement we read (in the
source or in an archived secondary source), proof not re-checked.

Status: IN PROGRESS (sections are added one at a time).

## 1. Setup: window failure as a sifting condition

Notation as in POINTWISE_SIZE §8.1. `p≡1 (mod 8)` prime, `q≡3 (mod 4)`,
`0<q<3p`, `n_q:=x_q=(p+q)/4`. A prime `r` is **q-bad** if the Jacobi symbol
`(r/q)=−1`, **q-good** otherwise (for `r∤q`; `r|n_q` implies `r∤q`, Lemma 8.2).

**Lemma 1.1 (F1 as a sifting condition; PROVED).** If `n_q` has no q-bad
prime factor, window q fails (both targets), i.e. `Rat_q(n_q)∩{−1,−p}=∅`.

*Proof.* Lemma 8.2 gives `(r/q)=(r/p)` for every prime `r|n_q`; so "no q-bad
factor" is exactly F1 (Cor 8.3(a)). ∎

The point of writing F1 via `(r/q)` rather than `(r/p)`: the sifting set
`P_q={r prime : (r/q)=−1}` is a union of residue classes mod `4q`, of
relative density 1/2 among primes, **independent of p**. So "window q
fails by F1" is a half-dimensional sifting condition on the shifted prime
`(p+q)/4`, with a p-independent sifting set.

**Lemma 1.2 (parity of the bad part; PROVED).** Let `Ω_q^-(n)` be the
number of q-bad prime factors of n counted with multiplicity. For
`gcd(n_q,q)=1`, `(−1)^{Ω_q^-(n_q)}=(n_q/q)=(p/q)`.

*Proof.* Multiplicativity of the Jacobi symbol: `(n_q/q)=∏_{r|n_q}(r/q)^{v_r}=(−1)^{Ω_q^-}`;
and `4n_q≡p (mod q)`, `(4/q)=1`. ∎

So if `(p/q)=+1`, every `n_q` has an **even** number of q-bad factors.
Whether bad factors are present at all is not a congruence datum
(Lemma 11.3); their parity is. This is why the half-dimensional problem has
no Selberg parity barrier at the level of a single window (§4).

**Window 3.** `P_3={r≡2 (mod 3)}` (Jacobi `(r/3)=−1` iff `r≡2 (3)`; this
includes `r=2`). For `p≡1 (mod 3)`, window 3 fails **iff** `n_3` has no
prime factor `≡2 (mod 3)` (the converse of Lemma 1.1 holds at q=3: a factor
`r≡2` gives `u=r,v=1`, `u/v≡2≡−1≡−p (mod 3)`). Then `a_min(p)≥7`.
