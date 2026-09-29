# Expense Tracker

A small command line tool for keeping track of your daily spending. I made it to practice Python and to try out the `rich` library for nicer terminal output.

## Purpose

Writing expenses in a notebook gets messy quickly. This tool lets you add an expense with one command, list everything in a neat table and see how much you have spent in total. All data is stored in a local JSON file, so no account or internet connection is needed.

## Features

- Add an expense with amount, category and an optional note
- Show all expenses in a coloured table
- Show the total amount spent
- Data saved locally in `expenses.json`

## Requirements

- Python 3.9 or newer
- pip (comes with Python)
- External dependency: [rich](https://github.com/Textualize/rich) version 13.0 or newer

## Installation

**Step 1.** Clone the repository:

```bash
git clone https://github.com/anilkoiri/expense-tracker.git
cd expense-tracker
```

**Step 2.** (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
```

**Step 3.** Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Add an expense:

```bash
python expense_tracker.py add 4.5 food --note "lunch"
```

Show all expenses:

```bash
python expense_tracker.py list
```

Show the total:

```bash
python expense_tracker.py total
```

Example output of `list`:

| Date       | Category  | Amount (EUR) | Note  |
|------------|-----------|--------------|-------|
| 2026-09-29 | food      | 4.50         | lunch |
| 2026-09-29 | transport | 30.00        |       |

> **Note:** run the commands in the same folder each time, because `expenses.json` is created in the current directory.

## Roadmap

- [x] Add, list and total commands
- [ ] Delete an expense
- [ ] Monthly summary per category

## Maintainer

Maintained by **Anil Koiri** ([anilkoiri2054@gmail.com](mailto:anilkoiri2054@gmail.com)).

## License

This project is for educational use.
