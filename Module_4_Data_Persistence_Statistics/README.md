# Module 4 – Data Persistence and Statistics

## About this module

This is the final module of my polling project. Here, I added file handling so that poll results can be saved instead of being lost when the program is closed. I also added a small statistical report.

## What the program does

1. Creates a poll and accepts votes.
2. Saves option-wise vote counts in a CSV file.
3. Saves poll details and vote history in a JSON file.
4. Calculates the mean, median and population standard deviation of the option vote counts.
5. Displays the results and saves a text report.

## Files created by the program

When the program runs, it creates a `poll_data` folder containing:

- `polls_database.csv` – stores the poll date, question, option and vote count.
- `poll_metadata.json` – stores poll details and vote history.
- `poll_report.txt` – stores the final results and statistical summary.

## Python concepts used

- File handling
- CSV and JSON
- `pathlib`
- Exception handling
- Python's `statistics` module

## How to run

```bash
python program.py
```

## What I understood

Through this module, I learned how to save program data in files and work with structured information. I also practised using Python's `statistics` module to calculate basic values from the vote counts.

**Note:** Data is stored locally. This is a learning project, not a production voting platform.
