# Module 3 – Modular Design and Exception Handling

## About this module

In this module, I improved the structure of the polling program. Instead of writing everything in one long section, I used a class and separate methods for different tasks. I also added exception handling to deal with invalid input more clearly.

## Main parts of the program

- `create_poll()` – takes the poll question and options.
- `get_voter_name()` – checks the entered voter name.
- `get_choice()` – accepts and validates the selected option.
- `record_vote()` – records a valid vote.
- `display_results()` – displays the results and vote history.
- `run()` – controls the overall program flow.

## Python concepts used

- Classes and objects
- Methods
- `try` and `except`
- Raising and handling `ValueError`
- Input validation

## How to run

```bash
python program.py
```

## What I understood

This module helped me divide a program into smaller parts. It also helped me understand how exception handling can handle common input errors without stopping the program unexpectedly.

**Note:** Votes are stored in memory in this module. They are not saved permanently.
