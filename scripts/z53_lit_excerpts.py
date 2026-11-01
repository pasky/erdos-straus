#!/usr/bin/env python3
"""z53 LIT: write verbatim theorem excerpts (pypdf text) for the items cited in Z53_LIT.md.

Requires /tmp/z53pdf/<id>.txt and .meta produced by scripts/z53_lit_fetch.py.
Usage: uv run python scripts/z53_lit_excerpts.py > sources/z53_lit/excerpts_lane.txt
Each excerpt: id, version/dates/title from the arXiv API record, then `n` lines starting at the first line matching `anchor`.
pypdf text has broken spacing/ligatures; Z53_LIT.md quotes were read from these excerpts and normalised by hand.
"""
import re

ITEMS = [  # (arXiv id, anchor regex, number of lines)
    ("2304.07953", r"^Theorem 1\.1\.", 40), ("2304.07953", r"^3\.1\. Proof of Theorem 1\.1\. Let us", 40),
    ("2511.08445", r"^Theorem 1\.1\.", 14),
    ("2609.37434", r"^The EOS conjecture remains open", 10), ("2609.37434", r"^Result Range", 12),
    ("2609.37434", r"^Second, the exponent", 8),
    ("2610.19597", r"^Theorem1\.1", 16), ("2610.19597", r"^Theorem1\.2", 6), ("2610.19597", r"^Theorem1\.3", 4),
    ("2610.19597", r"^Theorem1\.4", 6),
    ("2301.07679", r"^Theorem 1\.1\.", 6), ("2301.07679", r"^Theorem 1\.3\.", 6),
    ("2605.27833", r"^Theorem 1\.1\.", 12), ("2511.08445", r"best one could hope for", 3),
    ("2606.30567", r"^Theorem 1\.1\.", 12),
    ("2302.06409", r"^Theorem 1\. Let", 4), ("2302.06409", r"^Theorem 2\. Let", 10),
    ("2411.17823", r"^Theorem 1\.1\.", 6),
    ("2608.27732", r"^Theorem 1\.1\.", 12),
    ("2607.07710", r"^Theorem 1\.", 16),
    ("2212.14646", r"^Theorem 1 Let", 6),
    ("2508.17979", r"^Theorem 1\.1\.", 8), ("2508.17979", r"^Theorem 1\.2\.", 6),
    ("1908.00378", r"^Theorem 1\. Let", 4), ("2306.08615", r"^Theorem 1 \(Mean", 3),
    ("2512.13669", r"^Theorem 1\.Let", 5), ("2608.27356", r"^Theorem 1\.1\.", 10),
    ("2410.03991", r"^Theorem 1\.1\.", 5), ("2410.03991", r"^Theorem 1\.2\.", 8), ("2410.03991", r"^Theorem 1\.3\.", 5),
    ("2304.08689", r"^Theorem 1\.1\.", 10),
    ("2610.15483", r"^Theorem1\.1\.", 10), ("2610.21099", r"^Theorem 1\.", 6),
    ("2205.02354", r"^Theorem 1 \(Full", 14),
]

for aid, anchor, n in ITEMS:
    meta = open(f"/tmp/z53pdf/{aid}.meta").read().splitlines()
    lines = open(f"/tmp/z53pdf/{aid}.txt", errors="replace").read().splitlines()
    idx = next((i for i, l in enumerate(lines) if re.search(anchor, l)), None)
    print("=" * 100)
    print(f"arXiv:{aid} | {meta[0]} | {meta[1]} | {meta[2]} | {meta[3]}")
    if idx is None:
        print(f"[anchor {anchor!r} not found]")
        continue
    page = max((l for l in lines[: idx + 1] if l.startswith("=== PAGE")), default="=== PAGE ? ===", key=lambda s: lines.index(s))
    print(f"[pypdf text, {page.strip('= ')}, anchor {anchor!r}]")
    print("\n".join(lines[idx: idx + n]))
