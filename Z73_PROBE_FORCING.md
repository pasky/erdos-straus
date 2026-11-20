# Steering note: coupled shifts, support, and the 1201 family

Result: on the quadratic family p=(5s²−1)/4, s ≡ 15 (16), a sharp classification of support ≤ 2 on the A=1, E=4 line (support 3 always suffices). There are three forced nonresidues, none of which need occur in any support-2 AB (4319). A ⟨2⟩-orbit lemma repairs every family prime with 7 | s at shift 7.   Label: PROVED (§1–§5 lemmas); CERTIFIED (193, table, 2911/4319 exhaustive checks)
Scope: fixed lines and the quadratic family only. No pointwise two-support theorem, no frequency statement, nothing about ES.
Review: cross-lab (Opus) `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md` (P21–P24 CORRECT)
Triage: METHOD-CX
STATUS delta: none
*(§0 block: z74 Opus xreview fix)*

**ES and the pointwise two-support assertion remain open.** Write `E=(A+B)/c` and `p+c=4ABD`. Support means `ω(AB)`, not `ω(c)`. No local condition below assumes that `c` is prime. We study `p≡1 (8)`; `5 (8)` is handled by Z72. The most specific positive result is the sharp support theorem in §3. It is a theorem on a quadratic subfamily, not an assertion about the frequency of primes on it.

## 1. No complementary character dichotomy on p+1 and 4p+1

**PROVED.** At any odd prime divisor `q` of `(p+1)/2` or `4p+1`, `(p/q)=(-1/q)` (on the second number, `4p≡−1 mod q`). The signs are the *same rule*, not opposite signs. Both numbers are `1 mod 4`, so neither full product forces a negative prime by parity. The first simultaneous all-positive prime example is 73: the two numbers are 37 and 293, both primes; the smaller primes `1 (8)` are 17,41, with halves 9,21. A different bad inference is to discard even valuations: a sum of two squares need not have every factor `1 mod 4`. At 1201 the two numbers are 601 and `5·31²`: 31 is available, though it occurs to even exponent.

**PROVED (incompatibility, all c).** If `A=1, B=2r`, with prime `r>3`, **no** `r|4p+1` can be used as that `r`, even allowing every divisor `c|2r+1`. Indeed `c≡7 mod 8`, and `E=(2r+1)/c` is odd with `1≤E<r`. From `Ep+1=B(4DE−1)` one gets `E≡4 mod r`, impossible (`r≥5`). For `r=3` the residue can be `1`; that is the ordinary `3|p+1` branch. This obstruction is algebraic, not rarity. More directly, for arbitrary prime `r`, the only possible `E` is the least positive residue `−p⁻¹ mod r` when `r≠p`; it must actually divide `2r+1` and the resulting `c` must satisfy `p+c≡0 mod 8r`.

## 2. Change B, not just c

For `A=1` and fixed E, `Ep+1=B t`, `t=4DE−1`. Conversely for any positive divisor `B` with `t≡−1 mod 4E` one has `B≡−1 mod E`, `c=(B+1)/E`, `D=(t+1)/(4E)`. For `E=2,4`, `Ep+1` is a unit modulo `4E`, and the exact `B`-targets are `5 mod 8`, `11 mod 16` respectively.

**PROVED (support compression, E=2).** There is a certificate on this line iff `2p+1` has a prime factor `5 or 7 mod 8`; whenever one exists, choose `Ω(B)≤2`. If a prime factor is 5 mod 8, take it. Otherwise the presence of a 7 forces a 3: the full product is 3, outside `{1,7}`. Take one of each; their product is 5 mod 8. Necessity follows since `{1,3}` is closed. This proves a genuine, conditional prime-factor implication at *one* p, not that such a 7 is always present. At 73, `147=3·7²` gives `B=21,c=11,D=1`. Background: the divisor/subgroup condition itself is `Z68_U7F.md` Lemma 2, `y=2`; the extra conclusion here concerns support of `AB` in Z72's Type II witness. The `y=4`/`C=1` conditions of Z68 and `Z62_INVERSEF.md` §2 need only a divisor `3 mod 4` of `4p+1`, not our stronger `11 mod 16` divisor: e.g. `p=313`, `4p+1=7·179`, with no `11 mod 16` divisor.

**CERTIFIED smallest obstruction even after unbounding E.** Among primes `1 mod 8`, 193 is the first with *no* `A=1` certificate, even with unlimited support. The finite check is exact: `c≤B+1≤(p+c)/4+1`, so `c≤(p+4)/3`; scan divisors `B` of `(p+c)/4` for all `c≡3 mod 4` through this bound. At 193 these are the 16 shifts from 3 to 63. It matters to change the splitting: `p+2=195=3·5·13`, `B=13`, `A=2`, `c=15`, `D=2`. In general a prime `q≡5 mod 8` in `p+2` gives `A=2,B=q,c=q+2`, since `(p+2)/q≡7 mod 8` (a subcase of Z68's outer-2 line). All these fixed lines can fail together; see below.

## 3. A forced factorization and a sharp theorem on the family through 1201

Take `s≡15 mod 16`, `s>0`, `p=(5s²−1)/4`. Statements on this family do not need primality unless explicitly stated. The 1201 case has `s=31`. At `E=4` we seek `B≡11 mod 16` dividing `5s²`. There is an unrestricted witness `B=5s`, `c=(5s+1)/4`, `D=(s+1)/16`. The question is how much the **square** improves the support, without assuming `s` prime. The following is a group argument on prime factors with multiplicity, not a scan to a cutoff.

**PROVED (sharp).** On this family there always exists an `A=1,E=4` certificate with `ω(B)≤3`. There exists none with `ω(B)≤2` **if and only if** all of the following hold:

1. every prime of `s` is `1,5,7,9 mod 16`;
2. `5∤s`, and each prime `q≡5 mod 16` dividing `s` has `v_q(s)=1`.

*Proof.* In the proof, residue names such as “a 7” mean a prime in that class modulo 16. An 11 works alone; a 15 works multiplied by 5. Exclude both. If a 3 occurs, let it be `q`. A 9 works with `q`, as does the square of any other prime of order four modulo 16 (`3,5,11,13`); if `q²|s` use `q³` instead. If none is possible then `s` has just one occurrence of a 3 and all other primes are 1 or 7, so `s` is 3 or 5, not 15. Thus a 3 guarantees support ≤2. If none of 3,11,15 occurs, there is an odd number of 7's since `s≡3 mod 4`. Any 13 works with a 7. The remaining primes are `1,5,7,9`. To have residue 11, `B` must use a 7 to odd exponent. With at most two distinct primes this is possible precisely when a single other prime power contributes 13. Among the remaining classes this can only be the cube of a 5-class prime, available precisely if `5|s` or some `q≡5 mod 16` satisfies `q²|s`. This proves the equivalence. In the failure case the product of the positive-class factors of `s` is 9 modulo 16 (the 7's give 7); a 9 or the square of a 5-class prime dividing `s` therefore supplies residue 9 in `s²`. Multiply it by a 7 and the distinguished factor 5 to obtain residue `9·7·5=11 mod 16` at support ≤3. ∎

**Second family from the obstruction (PROVED factorization).** With `U=(5s−1)/2 ≡17 mod 20`, `V=(5s+1)/4 ≡19 mod 20`, one has

```
5p+1 = 2UV,      p+4D = sV,        D=(s+1)/16.
```

This forces an `E=5` certificate `B=2U,c=s`, exchanging the shifts `s` and `V` (the factors of `p+4D`). This uses an identity, not an independence assumption. In fact a small-support `A=1,E=5` certificate exists iff `UV` has a prime power `q^j≡17 mod 20`. For `t≡19 mod 20` is odd, so `B=2b`, `b|UV`; since `UV≡3 mod 20`, this `t` is equivalent to `b≡17 mod 20`. Only one odd prime is allowed in `b`. Equivalently one needs a `17 mod 20` prime or a `13 mod 20` prime available cubed. A genuinely forced prime: `U≡2 mod 5` forces some prime of odd valuation with `(q/5)=−1`. This is **not** enough: it gives residues `3,7,13,17 mod 20`, not the required prime power.

| s | p | E=4 minimum | E=5 small-support result |
|---:|---:|---|---|
|31|1201|2 (`B=155,c=39`)|no; forced unrestricted `B=154` has support 3|
|959 = 7·137|1149601|3 (`B=4795` only)|yes; `U=3·17·47`, take `B=34,c=7,D=8453`|
|2911 = 41·71|10592401|3 (`B=14555` only)|no; `U=19·383,V=3·1213`, so neither qualifying prime-power shape exists|

**CERTIFIED** primality and factorizations in table. At the last prime `(p+1)/2=109·48589` is all `1 mod 4`; the 2p+1 compression and the `p+2` prime-5-mod-8 test fail too. Thus even *conditioning* on the original dead branch and the exact square structure, the second split needn't repair support. The forced nonresidue factor in `U` there is 383 (`3 mod 20`). This is not a counterexample to ES or to unrestricted two-support witnesses. The `E=4,5` families are existing Type II coordinates (Z62 Thm 3.1); the two-support classification and the transfer on this quadratic subfamily are the point, not a new parametrization. No literature priority asserted.

## 4. Actually forcing primes, then testing whether they can occur in *any* split

**PROVED.** On this prime family, not just a nonresidue of 5 but **three distinct nonresidue prime factors modulo p** can be forced on the support-three branch. There is one in each of `s,U,V`: these integers are pairwise coprime (`2V−U=1`, and `5s=2U+1=4V−1`). Some `q≡7 mod 16` divides `s` on that branch (§3); `4p≡−1 mod q` makes `(q/p)=−1`. For odd `q|UV`, `5p≡−1 mod q` gives `(q/p)=(−5/q)`. Now `(−5/U)=(−5/V)=−1`: their residues are 17 and 19 mod 20, respectively. Each has a negative prime factor of odd valuation. This is an actual product-sign argument at the given prime, with no sieve hypothesis. Compare the necessary ` (AB/p)=−1 ` condition in `HARDNESS_MAP.md`; it does **not** say which nonresidue will work.

**CERTIFIED.** Changing the split can use a forced prime at `s=2911`: 19 in `U` gives `A=19,B=27,c=23,D=5162`, although 383 (the nonresidue of 5 there, a *residue* modulo p) occurs in no two-support `AB`. But at **`s=4319`, `p=23317201`**, even this proposal fails, allowing *every* `A,B,c,D,E`. Here `(p+1)/2=11658601` is prime; `s=7·617`, `U=3·59·61`, `V=5399` prime. The only mod-p negative prime factors on the three lists are respectively `7,59,5399`; **none divides `AB` in any two-support certificate.** Independently `A=1,B=62,c=7,D=94021` works, so a forced factor can even occur in the shift without occurring in the support. The exhaustive check for a specified `q` is short: for `k=AB` divisible by `q`, positivity gives `k≤(p+1)/3`, and `c≤k+1<4k` fixes `c=−p mod 4k`. If `ω(k)≤2`, the only coprime splits up to swap are `(1,k)` and `(q^{v_q(k)}, k/q^{v_q(k)})`. Test `c|A+B` for both. This finite computation falsifies picking the anchor from those three lists; it does not stand in for the forcing proof.

## 5. Put the forced factor in the shift instead: an unconditional repair for 7 | s

**PROVED (general local lemma).** Let `c≡7 mod 8`, `gcd(p,c)=1`, `(p/c)=−1` (Jacobi), `K=(p+c)/4`. Suppose `h=ord_c(2)=φ(c)/2` and `v₂(K)≥⌊h/2⌋`. Then there is a certificate at this specific `c` with `ω(AB)≤2`. Indeed `(K/c)=(p/c)=−1` while `(2/c)=1`, so some odd prime `q|K` has `(q/c)=−1`. This is a forced prime, not a density claim. Since `(−1/c)=−1`, the element `−q` is in the Jacobi kernel. The order hypothesis says the kernel is exactly `⟨2⟩`, even if `c` is composite. Choose a signed exponent `j`, `|j|≤⌊h/2⌋`, with `q≡−2^j mod c`. For `j≥0` take `(A,B)=(2^j,q)`; for `j<0` take `(1,2^{−j}q)`. In both cases `AB|K`, `c|A+B`; no information about which negative `q` was supplied is required. This is a sufficient bounded-orbit argument, distinct from Z72's two-log prime-shift phase inequality, but both end by the same unit-fraction identity.

**Corollary.** For `c=7`, `h=3` and one available factor of 2 always suffices at `p≡1 mod 8`. In particular **every prime on the quadratic family with `7|s` has two-support at shift 7**, including those requiring support three on the `E=4` line: `p≡−1/4≡5 mod 7` gives `(p/7)=−1`. This explains the `s=4319` rescue without knowing that 31 divides `K`: *any* forced negative prime suffices. It does not assume there are infinitely many primes of the quadratic shape. For the composite `c=15`, `h=4` and the condition is `p≡1 mod 16`, `(p/15)=−1`; e.g. `193` is rescued this way. **Overlap:** on the original `p+1` dead branch `p≡1 mod 3`, so the negative sign modulo 15 implies `p≡2 or 3 mod 5`. The second value already gives `5|p+2` and the first `5|2p+1`. Thus this composite test supplies a specified shift but does *not* extend the union of §2 on that branch. At `c=39` the order condition also holds (`h=12`), but six factors of 2 are not available at 1201, which instead uses the `E=4` repair. The `s=2911` prime has positive sign at both Jacobi tests `c=7,15`; the corollary doesn't rescue it. The size of the orbit required as `c` grows, and the failure of the sign at fixed shifts, are still real restrictions.

## Checks and steering

`scripts/z73_probe_forcing.py`, run via `uv run --with sympy python scripts/z73_probe_forcing.py`, checks the integer equation for each returned witness. The following is the union of the original Z72 branch (including its `5 mod 8` case), E=2,4,5 with `A=1,ω(B)≤2`, and the prime-5-mod-8 `p+2` line with `A=2`. On `5 mod 8` inputs only the original branch is needed and tested.

| screen | hits / inputs (CERTIFIED) |
|---|---:|
| F1 first 50 odd squares |0/50|
| F2 numerator-8 zeros, run the numerator-4 test |11/12|
| F3 composite restricted-line zeros |192/285|
| F4 star / gstar zeros |12/14, 31/38|

**Assessment.** The square transfer forces actual divisors and its three-prime bound is sharp on the indicated line. It does not force `4p+1` to have squarefree kernel 5, and it does not prove the general two-support target even on kernel 5. The prime 193 rules out any universal repair that keeps `A=1`. The three-forced-primes test (§4) also rules out choosing a nonresidue from `s,U,V` as an `AB` anchor regardless of the split. Changing the *role* of the factor works for `7|s` (§5). If continuing, target the case without 7: a forced factor `r≡7 mod 16` of `s` supplies the sign `(p/r)=−1`, but the signed two-power orbit may be too short. At `s=2911`, `r=71`, `ord₇₁(2)=35` and `v₂((p+71)/4)=1`, far short of 17. This is a concrete test for adapting the anchor or shift instead of seeking another sign.
