#!/bin/bash
# usage: z52_thin_fetch.sh <arxiv-id> ; downloads PDF to /tmp/z52p/<id>.pdf and text to /tmp/z52p/<id>.txt
ulimit -v 8000000
id="$1"; f="/tmp/z52p/${id//\//_}"
mkdir -p /tmp/z52p
[ -s "$f.txt" ] || { timeout 120 curl -sL "https://arxiv.org/pdf/$id" -o "$f.pdf" && timeout 120 pdftotext -layout "$f.pdf" "$f.txt"; }
wc -c "$f.txt"
