# Independent review: Lean formalisation of F3_CONJ §6 (Claude Opus)

Scope: commits `907f2f5e5..4a4edade1` (b67f89de9, 4a4edade1): `lean/ES/ES/F3Endpoint.lean` (new, 152 lines),
`lean/ES/ES.lean` (+import), `notes/z78/F3_CONJ.md` (Review line, new §8). Reviewer: Anthropic Claude Opus, the same lab as
the Opus reviews already on file (so this is not an extra cross-lab review). No Lean, note or master file was edited.
No provider, auth or quota errors occurred.

**Verdict: the Lean check is correct and faithful. Its scope is stated accurately in §8. I found no mathematical defect and no
encoding defect. There are four minor wording and form nits (§5).**

## 1. Builds (reproduced)

Toolchain `leanprover/lean4:v4.34.1`, Mathlib `d13f23b7…`, `PATH=$HOME/.elan/bin:$PATH`, with no `ulimit -v`.

| check | command (in `lean/ES`) | result |
|---|---|---|
| independent elaboration from source (no `.olean` of the module used) | `systemd-run --user --scope -p MemoryMax=16G timeout 1800 lake env lean ES/F3Endpoint.lean` | success, 0 warnings, 0 errors, 3.3 s; only output is the two `#print axioms` lines |
| control: the same file with an appended false `example : (2:ZMod 3)=0 := by decide` | same | fails at the appended line only, so elaboration really happens |
| intermediate commit b67f89de9 version of the file | same, on `git show b67f89de9:…` | compiles; one deprecation warning (`if_true`), which the final version fixes (`ite_true`) |
| prescribed package root build | `systemd-run --user --scope -p MemoryMax=16G timeout 1800 sh -c 'lake exe cache get && lake build'` | `Build completed successfully (8932 jobs)` |
| statement and axiom probe through the built olean | `import ES.F3Endpoint`, `#check`, `#print axioms` | matches the source (the statements are quoted in §3) |

Scratch probe files were written to `/tmp/f3rev/` (outside the repository). The build artifacts are only in the ignored `.lake`.

## 2. Exact axiom report

```
'ES.F3Endpoint.no_covering_endpoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'ES.F3Endpoint.key_identity' depends on axioms: [propext, Quot.sound]
```

These are the three standard Lean/Mathlib axioms. There is no `sorryAx` and no `Lean.ofReduceBool` (that is, no
`native_decide`). `git grep` finds no `sorry`, `admit`, `native_decide`, `axiom`, `opaque`, `unsafe`, `implemented_by`,
`extern` or `set_option` in the file. The only `decide` (in `degSum`, `(1:ZMod 3)+1 ≠ 0`) is checked by the kernel. The file
imports only Mathlib, not `ES.AxiomsHC` or any other repository module, so there are no project axioms in scope. The axiom
report quoted in §8 of the note is exact, though the two lines are listed in the opposite order to the output.

## 3. The statements versus the note

`key_identity` is stated over an arbitrary `CommRing R` ✓. It has hypotheses `hMW, hMH, hXS, hM, hu : p*q=u, hN : δ+b=N`,
and its conclusion is (6.1) verbatim: `pMW + T^δ qmH² = κu + T^N(TmHW − uS)`. It does not use the companion identity.

`no_covering_endpoint` (over `Poly = (ZMod 3)[X]`, with `T := X` and `U := 1+X = u` at c=1) concludes `False`. Its
hypotheses map to the note as follows.

| Lean | note | faithful? |
|---|---|---|
| `orient`: `(p,q,κ)=(1,U,1)` or `(U,1,−1)` | §1 orientations A/B; κ=(q−p)/T at c=1 | ✓ |
| `Monic p,q,m,M,H,W` | §6 "all of p,q,u,m,H,W monic" (c=1); M=mX; H has lc q (§1); W monic (§3 subsection: lc S=lc J=lc p) | ✓ |
| `hJ : J≠0` | §3 (nonzero by §1) | ✓ |
| `_hW0 : W(0)≠0` | §3 (W is a T-unit) | ✓, but **unused** (see §4) |
| `hM : M=m*x` | §1 | ✓ (`x` is the short side X, not the indeterminate) |
| `hMW, hMH, hXS` | §3 / §6 exact identities | ✓ verbatim |
| `hcomp : p*g*J = T^b*W − κ*H` | §3 companion **pgJ=T^bW−κH** | ✓ The factor is **p**, not u. It becomes u only after `orient` is resolved to B. |
| `hN : δ+b=N`, `hδ : δ=3∨δ=4` | §3: b=n−K, n∈{2N−3,2N−2}, K=N+1 ⇒ δ=N−b∈{4,3} | ✓ |
| `hshort : N+1 ≤ deg M + deg x + deg p` | §1: d+r+P≥K, with d=deg M=z+r and r=deg X | ✓ |
| `hd : deg M ≤ b+deg q` | §1: d≤n+Q−K | ✓ |
| `hH : deg H + deg M = b+deg q` | §1: h=L+Q−K=n−d+Q−K | ✓ (encoded additively, so ℕ-safe) |
| `hw : deg W ≤ 1+deg p` | §3 second-contact subsection: w∈{0,1} (A), {0,1,2} (B) | ✓ |

**(6.2), (6.3), the endpoint pattern (P=1, δ=3, d=b, w=2, H=1, orientation B) and False are not among the hypotheses** ✓.
The hypotheses are also not trivially inconsistent at the level of degrees. For example, the B-endpoint pattern
P=1, Q=0, δ=3, d=b, h=0, w=2, r≥3 satisfies every natDegree hypothesis, so the contradiction genuinely comes from the
algebra. The statement omits several facts that a real tuple satisfies: N≥4, S≠0, g monic or nonzero, and the T-unit
property of X, M, H. It is therefore *stronger* than needed, which is harmless.

## 4. The proof versus §6

* **Degree split.** `carry_one` takes A=pMW and B=T^δqmH² (both monic), `low`=κU of degree 1 < deg B, deg A≤N and
  deg B<N. Because `degSum` is monic with 1+1≠0, there is no top cancellation, and it gives deg A=N and carry=1. This is
  exactly the paper's "if deg(pMW)<N the left side equals κu" argument together with the degree-N coefficient read-off.
  The bounds passed to `omega` match §6:
  * deg B = δ+Q+z+2h ≤ b+2−2P < N, using hshort, hH and hdn (the identity deg M = z+r);
  * deg A = P+d+w ≤ b+2+P ≤ N.
* **Pattern forced.** deg A=N together with P+Q=1 gives P=1, δ=3, deg M=b and w=2. Then `hH` gives deg H=0 and hence H=1.
  P=1 excludes A. All of this is derived; none of it is assumed ✓.
* **(6.2)** is `hcarry` (TmW−uS=1). The relation x=TWJ+1 follows by `linear_combination T*W*hMH − x*hcarry − hXS`, which
  matches the note's "X(TmW−1)=T^(d+1)W−1". The relation `eq63` (6.3) is then derived from hMW ✓.
* **Endpoint.** `close_endpoint` splits on `by_cases Δ.natDegree = 0`, so the case split is complete.
  * *Constant case.* Evaluating at −1 gives Δ=−1, hence UW=T³+1=U³ (by `add_pow_char`) and W=U². Evaluating the companion
    UgJ=T^bW+1 at −1 then gives 0=1 ✓.
  * *Nonconstant case.* Δ≠0, and the degrees are z+2+1+degΔ+j against 3+j. This is a contradiction by `omega` because
    degΔ≥1 ✓.
* **`_hW0` really is unused.** Δ=0 is constant, and evaluation at −1 forces the constant to be −1, so W(0)≠0 is not needed.
  The §8 remark is correct. It also shows that the paper's "Δ≠0 since W(0)≠0" step is dispensable.

## 5. Critique (form and nits; none blocking)

1. **The "determinant" wording in §8.** "the monic T-unit determinant of degree ≤1+P" is unclear, because W is not a
   determinant (§7 only speaks of a "determinant equation"). Suggest "the monic T-unit W of degree ≤1+P (§3,
   second-contact subsection)". It would also be worth naming that subsection as the source of `hw` and of W's monicity.
2. **Repository convention.** The `#print axioms` lines sit inline in a library module, so they print on every build. The
   rest of the repository collects them in `ES/Axioms*.lean`. This is cosmetic.
3. **§8 could say the statement is stronger than §6 needs.** §8 could note that N≥4, S≠0, g≠0 and the T-unit hypotheses on
   X, M, H are not used. That would make clear that the check does not hide any small-level case. It also makes no claim
   about small levels, which stay in the paper.
4. **Label.** "PROVED relative to the listed hypotheses" is accurate. For consistency with AGENTS.md labels, one could add
   "(Lean kernel-checked; axioms as below)". The note's front-matter Label and STATUS delta are unchanged, which is correct.
   Mentioning the Lean check in STATUS is the orchestrator's export decision.

## 6. Challenge: what the formal check does *not* buy

This is in the spirit of the note's own scope sentence, which is accurate. The kernel-checked part is the elementary tail
of the argument: one ring identity, a monic leading-term comparison and evaluation at −1. The load-bearing inputs remain
paper proofs and are exactly the hypotheses:
* `hshort` comes from §1 via FF_THIRDS_CORNER Cor. 3.2.
* `hw` comes from the second-contact logarithmic-derivative estimate. It depends on the active-prime bound
  deg R₃(F)≥K of §2 and on the non-cube argument for G. This is the most delicate analytic step.
* `hd` and `hH` come from §1's covering normal form. Sign symmetry (reduction to c=1), small levels s≤6, same-side
  exclusion and compactness are also paper proofs.

A future formalisation effort should target `hw` (the R₃ bound and the derivation w≤1+P) first, because that is where a
hidden error would most plausibly live. Within its stated scope, the Lean check confirms that §6's elimination is
airtight. It also confirms that no case (A, δ=4, nonextreme B, Δ=0 or constant Δ) is silently skipped.
