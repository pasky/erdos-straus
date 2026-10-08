# Hostile review A of EXCEPTIONAL_MN.md (R94, reviewer A)

Reviewed: `EXCEPTIONAL_MN.md` at merge of `side-agent/mn-threequarter` (0bc7efc), against
`paper/es-threequarter-note.tex` ("the note"), `EXCEPTIONAL_SHORT.md` ("SHORT"),
`sources/pw.txt` / `sources/pomerance-weingartner-2511.16817/…v2.pdf` ("PW").
From-scratch scripts: `scripts/review_emnA_*.py`.

Status: IN PROGRESS (claims are appended one at a time).

## Verdict summary (filled in as claims are checked)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (identity for m) | SOUND (re-derived; machine-checked from scratch) |
| Def 1.2 / Lemma 1.3 (atom family, dedup, CRT) | SOUND (re-derived) |

## Claim-by-claim notes

### Lemma 1.1
Re-derived: over the common denominator `n s u v w`, numerators of `1/(suw), 1/(nsvw), 1/(nuvw)`
are `nv, u, s`; `nv+u = s kℓ` so the sum is `s(kℓ+1) = m·suvw`, i.e. the total is `m/n`.
`s ≥ 1` is an integer by hypothesis `kℓ | nv+u`; `w = (kℓ+1)/(muv) ≥ 1`. Holds for every
`n ≥ 1` in the class, so every m-exceptional n (incl. n = 1) avoids every atom. The class is a
unit class: `(v, kℓ) = 1` because `(v,k)=1` (atom definition) and `v < ℓ`. The PW definition
of "m/n not the sum of 3 unit fractions" is `(x,y,z) ∈ N³`, not necessarily distinct
(PW (2.1)), matching MN's. No issue.

### Lemma 1.3
Re-derived each of (i)–(iv). (iii): `kℓ ≡ k'ℓ ≡ −1 (mod muv)`, `ℓ ∤ muv` (ℓ prime,
`ℓ > X^{1/2} > m z_j^2 ≥ muv`; indeed `ℓ | kℓ+1` is impossible anyway), so `k ≡ k' (mod muv)`,
and `muv ≥ 4H^2 > K` forces `k = k'`. (ii) `|uv'−u'v| < z_j^2 ≤ x_j^{1/3} < ℓ`. `m ≤ K < ℓ`
gives `(ℓ, m L_K) = 1`. Conditional independence: the only coordinates of n used by an atom
are `n mod k` (k | L_K) and `n mod ℓ`; CRT over `L_K·Π ℓ` is exact. No m-dependence.
