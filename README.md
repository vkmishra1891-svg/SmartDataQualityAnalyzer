# Smart Data Quality Analyzer

A beginner Python project that checks CSV files for basic data quality issues.

## What it checks

- Number of rows and columns
- Whether the required `name` and `email` columns are present
- Blank values in each column
- Duplicate rows

## Run it

Keep the CSV file in the project folder. In the VS Code terminal, run `python main.py`, then enter the CSV filename when prompted.

## Sample data

The included `sample_data.csv` has four rows, blank values in the `age` and `email` columns, and one duplicate row.