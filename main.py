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
        required_columns = ["name", "email"]
        available_columns = {column.strip().lower() for column in columns if column}
        missing_columns = [
            column for column in required_columns
            if column.lower() not in available_columns
        ]

        if missing_columns:
            print(f"Missing required columns: {missing_columns}")
        else:
            print("All required columns are present.")

        for column in columns:
            blank_count = sum(
                1 for row in rows
                if not (row.get(column) or "").strip()
            )
            print(f"Blank values in '{column}': {blank_count}")

        seen_rows = set()
        duplicate_count = 0

        for row in rows:
            row_values = tuple(row.get(column, "") or "" for column in columns)

            if row_values in seen_rows:
                duplicate_count += 1
            else:
                seen_rows.add(row_values)

        print(f"Duplicate rows found: {duplicate_count}")