import csv
from pathlib import Path

file_path = Path("sample_data.csv")

if not file_path.exists():
    print(f"Could not find {file_path}. Put it in the project folder and try again.")
else:
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        columns = reader.fieldnames or []

    print(f"Rows found: {len(rows)}")
    print(f"Columns found: {len(columns)}")
    print(f"Column names: {columns}")

    for column in columns:
        blank_count = sum(
            1 for row in rows
            if not (row.get(column) or "").strip()
        )
        print(f"Blank values in '{column}': {blank_count}")