import pandas as pd
import json
import sys
from collections import defaultdict

def excel_to_json(excel_file, json_file):
    # Read the Excel file
    df = pd.read_excel(excel_file, sheet_name=None)  # sheet_name=None to load all sheets

    # Convert the Excel sheets to JSON
    json_data = {}
    for sheet_name, data in df.items():
        json_data[sheet_name] = data.to_dict(orient='records')  # Convert each sheet to a list of dictionaries

    # Write the JSON data to a file
    with open(json_file, 'w') as f:
        f.write(json.dumps(json_data, indent=4))  # Pretty-print with indent

if __name__ == "__main__":
    # You can pass the file names as arguments
    excel_file = sys.argv[1]  # Input Excel file
    json_file = sys.argv[2]   # Output JSON file
    excel_to_json(excel_file, json_file)
    
# Load the JSON file
#with open("tableConvert.com_hm5ekg.json", "r", encoding="utf-8") as file:
    data = json.load(json_file)

# Group data by "Member" (Region)
grouped_data = defaultdict(list)

for entry in data:
    member = entry.get("Member", "Unknown Region").strip()
    entry.pop("Member", None)  # Remove the "Member" key after grouping
    grouped_data[member].append(entry)

# Save the grouped data
with open("grouped_waste_data.json", "w", encoding="utf-8") as file:
    json.dump(grouped_data, file, indent=2)

print("Data successfully grouped and saved as grouped_waste_data.json")
