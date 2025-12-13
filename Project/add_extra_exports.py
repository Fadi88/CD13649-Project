import json
import os

path = "Preparing-for-data-analysis-project-student.ipynb"
if not os.path.exists(path):
    print("Notebook not found!")
    exit(1)

with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Find the last code cell (Export) - ID 3d67d29c
target_id = "3d67d29c"
found = False

for cell in nb["cells"]:
    if cell.get("id") == target_id:
        found = True
        source = cell["source"]
        # Check if already has our new exports
        has_weekly = any("inflation_weekly.to_csv" in line for line in source)
        if not has_weekly:
            # Ensure last line has newline
            if source and not source[-1].endswith("\n"):
                source[-1] += "\n"

            cell["source"].append("inflation_weekly.to_csv('inflation_weekly.csv')\n")
            cell["source"].append(
                "inflation_quarterly.to_csv('inflation_quarterly.csv')\n"
            )
            print("Added extra exports to cell.")
        else:
            print("Exports already present.")

if not found:
    print("Export cell not found!")

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)
