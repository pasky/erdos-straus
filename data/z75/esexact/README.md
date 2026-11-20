# Full unordered ES counts at R8-zero primes: checkpoint

One full enumeration per input, with every output triple independently checked and independent *completeness* checks at smaller primes only. Each certificate is named `<p>.txt`.

| p | Type I | Type II | Total unordered | Elapsed s | Peak RSS KiB |
|---:|---:|---:|---:|---:|---:|
| 25277866681 | 531 | 219 | 750 | 115.85 | 22604 |
| 25606400401 | 527 | 209 | 736 | 100.56 | 22640 |

The minimum among these two inputs is **736** at `25606400401 = 160020²+1`; no claim here about other inputs.

The header is `p E F unordered_I unordered_II`, subsequent lines `type a b c d`. These are the normalized positive Elsholtz–Tao coordinates, with `a <= b`. Type I denominators are `(pabd, acd, bcd)`; Type II `(abd, pacd, pbcd)`. The verifier recovers the unordered triples, checks divisibilities and the ES identity in arbitrary precision, and rejects duplicates. The independent calibration computes the sets of triples by enumerating the smallest denominator and factoring the remaining two-term equation. **All 77** primes tested agree (every prime ≡ 1 mod 4 up to 900, plus 10009, 65537, 1000033); the large calibration primes use very small E,F to exercise the residual branch. This is a finite count, not a statement about typical primes or about ES in general.

Reproduce from repository root (one compute process at a time; keep assertions enabled):

```sh
ulimit -v 6000000
base=data/z75/esexact
exe=$base/engine
timeout 60 g++ -std=c++17 -O3 -Wall -Wextra scripts/z75_esexact.cpp -lgmpxx -lgmp -o "$exe"
for p in 25277866681 25606400401; do
  timeout 1750 "$exe" "$p" 600000 8000000 emit > "$base/replay.txt" && cmp "$base/replay.txt" "$base/$p.txt" || exit 1
done
timeout 120 uv run --offline --no-project python scripts/z75_esexact_verify.py "$base/25277866681.txt" "$base/25606400401.txt"
timeout 500 uv run --offline --no-project python scripts/z75_esexact_verify.py calibrate "$exe"
```

## Why the search is complete

Use ET (arXiv:1107.1010) Props. 2.2, 2.6: each unordered triple of the respective type has unique coordinates with `a <= b`, `gcd(a,b,c)=1`, the type-specific coprimality with p, and `a+b=ce`. Conversely the projected denominator triple is a solution when `4abcd=p(a+b)+c` (I) or `4abcd=a+b+pc` (II); the engine checks these identities, coprimalities and order and unions the accepted tuples in a set. The relevant divisibility pattern identifies the distinguished denominator. No weights for permutations.

* **II:** put `L=floor(sqrt(p))`. ET gives `4abd=p+e`, `f=4acd-1`, `bf=pc+a`, and `acde<=p` (Lemma 2.8). For `e<=L` enumerate the splits `abd=(p+e)/4`, testing `e | a+b`. For larger e, enumerate `acd <= p/(L+1)`, split that product in all orders and test `f | pc+a`. This two-region split suffices at these sizes.
* **I, small coordinates:** `4abd=pe+1`, `4acd=p+f`, `bf=pa+c`. Enumerate all splits of `(pe+1)/4` for `e<=E` and of `(p+f)/4` for `f<=F`, testing the same reconstruction identities. Here and in II the integral e-slices have `e=3 mod 4` since the input is restricted to primes `p=1 mod 4`; the I f-slices also have `f=3 mod 4`.
* **I, residual:** it remains to cover `e>E` **and** `f>F`. Write `y=acd`, `T=c²d`, `Y=floor(3p/4)`, `H=4Y²`, `K=(E+1)(F+1)-1`. By Lemma 2.8, `p/4<y<=Y`. Since `ef-1=4a²d`, we have `(ef-1)T=(p+f)²/4=4y²<=H`; hence `c²<=T<=min(Y²,H/K)`. There are two complementary regions, inspired by the `ac` and `cd` charts of ET §3:
  * `a<=d`: then `a<=floor(sqrt(Y/c))` and `a>=ceil(cK/(4Y))` since `ef-1=4ay/c`. For fixed a,c, `b(4acd-p)=pa+c` forces `b ≡ -a - c/p (mod 4ac)`, where `c/p` denotes `c*(p inverse mod 4a)`. Indeed `a` and `p` are coprime. Search the positive b in that one class up to `(pa+c)/(F+1)`, divide to recover f, then d. Skipping `gcd(a,c)>1` loses no normalized solution because `a+b=ce`.
  * `d<a`: now `d<=floor(sqrt(Y/c))`. Fix c,d and write `m=4cd`. Initially `f<=4Y-p` and `f<=(H/T+1)/(E+1)`. Given any upper bound `h` on f we may tighten it using `f<=((p+h)²/(4T)+1)/(E+1)` by the residual identity. Enumerate `a>d` with `F<ma-p<=h`, directly testing `(ma-p) | pa+c` for short intervals. For long intervals factor `p²+4T`: the divisor identity `(4acd-p)(4bcd-p)=p²+4T` means it suffices to take every divisor `F<f<=h` with `m | p+f`, and recover a. Both branches are exhaustive, with overlaps with earlier charts harmless. E and F are split points, **not truncations**.

Progression factorization sieves small primes and recursively splits composite cofactors using Pollard rho. GMP probable primes (other than GMP's definite-prime return) must pass strong Miller–Rabin to each of the first 12 prime bases; the first simultaneous strong pseudoprime is 318665857834031151167461 (Sorenson–Webster, *Strong pseudoprimes to twelve prime bases*). The code restricts `p<=2·10^11`; even `p²+4T <= p²+4Y²` is strictly below this threshold. Rho randomness is not used for accepting a factorization. No output header until all charts finish.
