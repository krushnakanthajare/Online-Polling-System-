# Module 2 – Voter Tracking

## About this module

In the first module, the program could accept votes without keeping track of who had already voted. In this module, I added a simple voter-tracking feature. The program asks for the voter's name and checks whether that person has already voted.

## What the program does

1. Takes the poll question and options.
2. Asks each voter to enter their name.
3. Checks whether the name is already in the voter set.
4. Records the vote if the voter has not voted before.
5. Displays the results and vote history.

The name check ignores uppercase and lowercase differences. For example, `Rahul` and `rahul` are treated as the same name.

## Python concepts used

- Lists, dictionaries and sets
- Membership checking with `in`
- String method `casefold()`
- Date and time

## How to run

```bash
python program.py
```

## What I understood

I learned why a set is useful when I need to check whether a value already exists. This module prevents the same entered name from voting twice while the program is running.

**Note:** This is a basic classroom example. It does not verify a person's real identity, and the voter list is not retained after the program closes.
