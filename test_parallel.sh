#!/bin/bash

T=10
REPEATS=5
N_VALUES=(1 2 3 4 5 6 7 8 16)
OUTDIR="parallel_results"
mkdir -p "$OUTDIR"

for N in "${N_VALUES[@]}"; do
  for r in $(seq 1 $REPEATS); do
    echo "testing N=$N, run #$r"
    
    prefix="${OUTDIR}/N${N}_R${r}"
    
    for i in $(seq 1 $N); do
      sysbench cpu --threads=1 --time=$T run > "${prefix}_proc${i}.log" &
    done

    wait
  done
done
