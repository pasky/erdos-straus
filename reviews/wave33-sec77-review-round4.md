DEFECTIVE

Reviewed `7776f2e5bb60f24a59ab39dc29605fed38e3da4b`. Read the round-3 review in full, inspected the repair diff, the headline, §77.7, and the affected passages. The prime-support repair is correct. However, the replacement CRT sentence is false for overlapping prime powers, and the newly explicit fibre-automorphism assertion overlooks empty integral fibres. Neither issue refutes the headline “no pointwise mechanism … was found.”

## Round-3 item status

- **MEDIUM, L versus L/4 — REPAIRED.** `notes.md:31203–31205`: “not dividing \(L/4\) (for \(8\mid L\) these are the primes not dividing \(L\); for \(v_2(L)=2\) the prime \(2\) is uncontrolled: \(p=13\), \(L=12\), \(q=3\), \(x=4\), \(2\equiv-1\)).” This correctly identifies the uncontrolled prime support, with the intended assumption \(4\mid L\).
- **LOW, mean shorthand — REPAIRED.** `notes.md:31044–31045`: “a quantity with uniformly bounded fixed-cutoff means multiplied by a trivially counted factor.” This correctly refers to the bounded constants \(C_0(A)\), without asserting the untruncated mean.
- **LOW, fibre scope — PARTLY REPAIRED; remaining false assertion below.** `notes.md:30846–30852`: “Fixing one coordinate at an integer window \(x>p/4\) with \(p\nmid x\), the fibre … is the punctured hyperbola … with the point \(y=z=0\) removed (a \(\mathbb P^1\) minus three points, not a torsor)” is correct, as is the positive-divisor description. But “the only regular automorphism of the fibre preserving them is the swap” needs a nonemptiness qualification. `notes.md:31168–31169` repeats “open fibres are punctured split conics whose positive solution points are permuted only by the swap”; the geometric terminology is repaired, but this should use the corrected automorphism scope too.
- **LOW, CRT freedom — NOT REPAIRED; replacement is false.** `notes.md:31206–31207`: “at moduli \(q\nmid L\) the residue of \(p\) is free modulo \(q/\gcd(q,L)\).” See the counterexample below.
- **LOW, verifier comments — REPAIRED.** `verify.py:15865–15867` now says “Deterministic sweep” and identifies the first-window statistic as “an offline computation, not replayed here.” Lines 15885–15886 give the typed-witness sum with “floor(p/(4ab)) + 1” and the actual fixed-cutoff mean domain. These match the code.

## Remaining mathematical issues

**1. MEDIUM — CRT freedom is not freedom of p modulo q/g.** Take \(L=12\), \(q=27=4\cdot7-1\), so \(q\nmid L\), \(g=\gcd(q,L)=3\), and \(q/g=9\). Every \(p\equiv1\pmod{12}\) satisfies

    p mod 9 ∈ {1,4,7},

not an arbitrary residue modulo 9. Even the unit classes 2, 5, and 8 are excluded. Primes 13, 37, and 61 realize the three allowed classes, respectively 4, 1, and 7. CRT gives q/g compatible classes modulo q; it does not make their projections onto modulus q/g unrestricted. Correct wording: “the congruence condition permits precisely the classes modulo q congruent to 1 modulo gcd(q,L)” (with primality restricting candidates further). Equivalently, it is \((p-1)/g\), not \(p\), whose residue is unrestricted modulo \(q/g\) by the progression condition.

**2. MEDIUM — every automorphism preserves an empty integral subset.** Take \(p=13\), \(x=6\), \(q=11\). This is an allowed integer window. The positive divisors of \((px)^2=6084\) have residues exactly \(\{1,2,3,4,5,6,7,8,9\}\) modulo 11, never \(-px\equiv10\). Thus this fibre has no positive integral points.

Nevertheless, with \(a=px/q=78/11\),

    (y,z) ↦ (a−y, a²/z)

is a nonidentity regular involution of the punctured fibre, distinct from the swap. Its denominators are invertible there, and y=a is impossible on the fibre. It preserves the empty positive-integral subset. This is not merely the omitted identity automorphism. Repair: say that, apart from the identity, only the swap can send any positive real fibre point to a positive real fibre point; alternatively qualify preservation of the integral subset by its nonemptiness.

## Arithmetic confirmation and checks

For \(4\mid L\), \(p=1+kL\) gives \(t=kL/4\), hence \(t+s\equiv s\pmod{L/4}\). Consequently the prime support shared with L/4 agrees for t+s and s. For odd prime \(r\mid s\), quadratic reciprocity with \(q=4s-1\equiv3\pmod4\) and \(q\equiv-1\pmod r\) gives \((r/q)=1\). If \(2\mid s\), then \(q\equiv7\pmod8\), again giving \((2/q)=1\). These are Jacobi symbols, so composite q is allowed. Products and inverses of these primes cannot yield −1, whose Jacobi symbol is −1.

If \(8\mid L\), dividing L by 4 removes no prime from its support: 2 remains and all odd primes remain. If \(v_2(L)=2\), exactly 2 disappears. The new parenthetical distinction is therefore correct. For p=13, L=12, q=3, x=4, the script confirms Rat₃(4)={1,2} and exactly verifies

    4/13 = 1/4 + 1/26 + 1/52.

A streaming SymPy script checked all 1008 prime-factor incidences for 1≤s≤500; 19363 prime windows with L=4(4s−1)k, 1≤k≤8, p=1+mL, 1≤m≤20; and 2000 support comparisons with 8|L. All intended arithmetic assertions passed. It also verified both remaining counterexamples and the additional fibre involution exactly.

The supplied isolated `check_by()` replay passed in 1.4 seconds, reproducing the round-3 output, including 59 reconstructed primes, 1262 brute solutions, 688 pigeonhole instances, and means 0.4715/0.4722. Commands used `uv`, 60/300-second timeouts, and 1,000,000/2,000,000-KiB virtual-memory limits. No full-verifier run is claimed.

The headline is unchanged except for line displacement and retains its scoped search conclusion. No other new false statement was found in the §77.7 edits. No source files were edited; only this review was added.
