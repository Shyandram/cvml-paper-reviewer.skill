#!/bin/bash
cd /home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill
S=academic-paper-reviewer/scripts/related_search.py
R=evals/work/results/iclr26-FmLGEJEvJ9
cd $R
python3 -I /home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill/$S search --fp fingerprint.json --query "differentially private Hamming distance sketch" --purpose claim --tag C1 --mode strict 2>&1 | cut -c1-400 | head -40
python3 -I /home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill/$S search --fp fingerprint.json --query "private edit distance" --purpose claim --tag C2 --mode strict 2>&1 | cut -c1-400 | head -40
python3 -I /home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill/$S search --fp fingerprint.json --query "differentially private function release" --purpose claim --tag C3 --mode strict 2>&1 | cut -c1-400 | head -40
python3 -I /home/runner/work/academic-paper-reviewer.skill/academic-paper-reviewer.skill/$S search --fp fingerprint.json --query "differentially private nearest neighbor" --purpose expansion --mode strict 2>&1 | cut -c1-400 | head -40
