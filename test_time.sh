#!/bin/bash

OUTDIR="time_test_results"
mkdir -p "$OUTDIR"

for T in 5 10; do
	echo "--- Testing T=$T ---"
	for i in {1..10}; do
		FILENAME="$OUTDIR/T${T}_run${i}.log"
		echo "Running test #$i (T=$T)"
		sysbench cpu --threads=1 --time=$T run > "$FILENAME"
	done
done
