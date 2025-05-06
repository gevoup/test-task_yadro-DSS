import os
import re
from collections import defaultdict

LOG_DIR = "parallel_results"
CSV_OUTPUT = "parallel_summary.csv"

eps_pattern = re.compile(r"events per second:\s+([0-9.]+)")

data = defaultdict(list)

for filename in os.listdir(LOG_DIR):
    if filename.endswith(".log"):
        path = os.path.join(LOG_DIR, filename)
        with open(path) as f:
            text = f.read()
            match = eps_pattern.search(text)
            if match:
                eps = float(match.group(1))
                match_n = re.search(r"N(\d+)", filename)
                if match_n:
                    N = int(match_n.group(1))
                    data[N].append(eps)

print(f"{'N':<4} {'avg':>10} {'min':>10} {'max':>10} {'spread %':>10}")

with open(CSV_OUTPUT, "w") as csv_file:
    csv_file.write("N,avg,min,max,spread_percent\n")
    for N in sorted(data.keys()):
        values = data[N]
        avg = sum(values) / len(values)
        min_v = min(values)
        max_v = max(values)
        spread = ((max_v - min_v) / avg) * 100 if avg != 0 else 0
        print(f"{N:<4} {avg:10.2f} {min_v:10.2f} {max_v:10.2f} {spread:10.3f}")
        csv_file.write(f"{N},{avg:.2f},{min_v:.2f},{max_v:.2f},{spread:.3f}\n")

print(f"\nАнализ завершён. CSV сохранён в: {CSV_OUTPUT}")
