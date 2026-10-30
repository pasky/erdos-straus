#!/bin/bash
# usage: z52b_analogues_arxiv.sh "query" ; prints id | title | first author
q=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$1")
curl -s --max-time 30 "https://export.arxiv.org/api/query?search_query=${q}&max_results=${2:-6}" | python3 -c '
import sys,re
t=sys.stdin.read()
for e in t.split("<entry>")[1:]:
    i=re.search(r"<id>(.*?)</id>",e).group(1).split("/abs/")[-1]
    ti=" ".join(re.search(r"<title>(.*?)</title>",e,re.S).group(1).split())
    a=re.findall(r"<name>(.*?)</name>",e)
    print(i,"|",ti,"|",", ".join(a[:3]))
'
