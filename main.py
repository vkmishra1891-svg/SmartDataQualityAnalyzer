import csv
from pathlib import Path

filename = input("Enter the CSV filename (for example, sample_data.csv): ").strip()
file_path = Path(filename)

if not file_path.exists():
    print(f"File not found: {file_path}")
else:
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        columns = reader.fieldnames or []

    if not columns:
        print("The CSV file is empty or its header row is blank.")
    else:
        print(f"Rows found: {len(rows)}")
        print(f"Columns found: {len(columns)}")
        print(f"Column names: {columns}")

        for column in columns:
            blank_count = sum(
                1 for row in rows
                if not (row.get(column) or "").strip()
            )
            print(f"Blank values in '{column}': {blank_count}")