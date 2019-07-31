#!/usr/bin/env bash

for f in ../plan/*.txt; do
    python3 gen_html.py $f;
    echo ""
done
