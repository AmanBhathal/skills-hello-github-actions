import pandas as pd
import json
from collections import defaultdict
import os

# Define paths
input_file = "msw_in_region_disposal.xlsx"
output_file = "folder/grouped_waste_data.json"

# Load the Excel file
df = pd.read_excel(input_file)

# Ensure column names are correct
if "Member" not in df.columns:
    raise ValueError("Expected column 'Member' not found in the Excel file.")

# Group data by "Member" (Region)
grouped_data = defaultdict(list)

for _, row in df.iterrows():
    member = row.get("Member", "Unknown Region").strip()
    entry = row.drop("Member").to_dict()
    grouped_data[member].append(entry)

# Save as JSON
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(grouped_data, file, indent=2)

print(f"Data successfully grouped and saved to {output_file}")
