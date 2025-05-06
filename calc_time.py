import os
import re
from collections import defaultdict

LOG_DIR = "time_test_results"

results = defaultdict(list)

eps_pattern = re.compile(r"events per second:\s+([0-9.]+)")

for filename in os.listdir(LOG_DIR):
    if filename.endswith(".log"):
        filepath = os.path.join(LOG_DIR, filename)
        with open(filepath) as f:
            content = f.read()
            match = eps_pattern.search(content)
            if match:
                eps = float(match.group(1))
                key = filename.split("_")[0]
                results[key].append(eps)

print(f"{'T':<6} {'avg':>10} {'min':>10} {'max':>10} {'spread %':>10}")
print("-" * 50)
for T, values in sorted(results.items()):
    avg = sum(values) / len(values)
    min_val = min(values)
    max_val = max(values)
    spread = ((max_val - min_val) / avg) * 100 if avg != 0 else 0
    print(f"{T:<6} {avg:10.2f} {min_val:10.2f} {max_val:10.2f} {spread:10.3f}")
