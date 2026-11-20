# An uncertified failure need not give an ES triple by complementation

Result: two Mordell-hard primes with the same phase costs at c=43 (the first nonresidue shift) give opposite answers to “does some triple contain x=(n+43)/4”; complementation of divisors cannot rescue a miss.   Label: CERTIFIED (paired example, exact); PROVED (direct factor test, complementation lemma, positive-row identity)
Scope: refutes the complementary-divisor rescue of `Z71_LIT.md` §2.1.3 at a fixed denominator. It is not an ES counterexample: the negative row has a triple at c=47.
Review: cross-lab (Opus) `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md` (P7 CORRECT)
Triage: METHOD-CX
STATUS delta: none
*(§0 block: z74 Opus xreview fix)*

**CERTIFIED (local obstruction; was labelled PROVED, an existential statement witnessed by a certified pair, z74 Opus xreview fix).** Fixing the denominator `x=(n+c)/4` matters. Even when `c` is the *first* prime `3 mod 4` with `(n/c)=-1`, failure of the Type II test with no odd-character phase certificate need not leave **any** two positive denominators completing `4/n`. Two primes `n ≡ 1 mod 840` give opposite answers at `c=43` with the **same entire list of phase costs**. This tests the proposed complementary-divisor rescue of `Z71_LIT.md` §2.1.3, not just the already-refuted converse to the phase lemma.

**PROVED (direct test).** Write `H=nx`. Completing `1/x` requires `c/H=1/y+1/z`, hence

    (cy−H)(cz−H) = H².

Both factors must be positive. Conversely any `d | H²` with `d` and `H²/d` both `≡ −H mod c` gives the positive denominators `(H+d)/c, (H+H²/d)/c`. If `gcd(H,c)=1`, the first congruence implies the second: complementation preserves the target and cannot turn a miss into a hit.

**CERTIFIED (paired examples).** In both rows `x=13·29·37·q`, with `q` and `n` prime. Euler's criterion gives `+1` at `3,7,11,19,23,31` and `−1` at `43` in each row. The residues below are modulo 43.

| `n` | `q` | `q mod 43` | `n mod 43` | triple containing `x`? |
|---:|---:|---:|---:|---|
| 12395549472601 | 222158389 | 7 | 3 | no |
| 349219296721 | 6258859 | 37 | 22 | yes |

With primitive root 3, logs of `13,29,37` are `−10,−1,7`; the log of `q` is respectively `−7` or `7`. Thus for each odd `j` the cost in units of `1/42` of a turn is `|10j|₄₂+|j|₄₂+2|7j|₄₂`, where `|·|₄₂` is distance to `42ℤ`. For `j=1,3,…,21` the costs are `25,57,27,35,57,41,31,75,33,53,63`; negation accounts for the other ten. Even the minimum exceeds a half-turn. The ratios of divisors of `x` omit exactly `{4,11,14,40,42}`, by multiplying the four sets `{s⁻¹,1,s}`. In particular **both** Type II windows fail. The sign choice affects `n=4x−43` but not the phase costs or ratio set.

* **Negative row.** `H ≡ 13`. The divisors of `H²` occupy **41 of the 42 unit classes; the sole missing one is 30 = −H mod 43**. This can be checked with just the five missing ratio residues above: `n∤x`, so the classes of `d/H` for `d | H²` are those of the ratio set multiplied by `n⁻¹,1,n`. In particular `−1` would require one of `−3,−1,−1/3 ≡ 40,42,14`, all missing. No complementary pair works. Nor does putting a divisor of this `H²` itself into *any* denominator slot: replay tests each such candidate by the direct positive-factor identity.
* **Positive row, actual identity.** Take `d=481=13·37`. More generally let `a>0`, `a ≡ ±2 mod 43`, `n=1924a−43`. Then `x=481a` and `na ≡ 4·481a² ≡ −1 mod 43`. With `y=481(na+1)/43` and `z=nay`, one has `1/y+1/z=43/(nx)` and hence a triple. In this row `a=29q ≡ −2`. It is the oriented congruence, not the phase cost, that makes `d` work.

**CERTIFIED (global control).** For the negative row the direct test at **every** `c=3,7,11,…,43` (including composite shifts) returns no triple. At the next shift `47` it gives, for example,

    (x,y,z) = (3098887368162, 817782487148702189502978, 1344434408867368729822288659).

Thus this is neither a counterexample to ES nor an example where a smaller successful shift accounts for the apparent rescue. If the conclusion is only “somewhere there is a triple for this prime”, the displayed triple makes that true irrespective of the premise. A general cross-window implication would require another argument; no ES proof for all primes follows.

**Falsifier checks (scope).**

| F1 odd squares | F2 numerator 8 / C-even | F3 composites | F4 known zeros |
|---|---|---|---|
| A square cannot meet the nonresidue premise. | The direct factor identity works with `c=8x−n` as well; no positivity is deduced there. | The two-factor test works without primality if both congruences are checked; the examples certify primes. | No implication about the restricted (★) count is used; its documented zeros are not ES zeros. |

Independent replay (trial division, direct divisors, rational checks; no imported campaign solver): `(ulimit -v 1400000; timeout 45 uv run --no-project python scripts/phase43_denominators.py)`.
