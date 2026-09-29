"""Simple command line expense tracker. Data is saved in expenses.json."""
import argparse
import json
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.table import Table

DATA_FILE = Path("expenses.json")
console = Console()


def load():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def save(items):
    DATA_FILE.write_text(json.dumps(items, indent=2))


def add(args):
    items = load()
    items.append({"date": str(date.today()), "category": args.category,
                  "amount": args.amount, "note": args.note})
    save(items)
    console.print(f"[green]Added[/green] {args.amount:.2f} EUR to {args.category}")


def show(_args):
    items = load()
    table = Table(title="Expenses")
    for col in ("Date", "Category", "Amount (EUR)", "Note"):
        table.add_column(col)
    for i in items:
        table.add_row(i["date"], i["category"], f"{i['amount']:.2f}", i["note"])
    console.print(table)


def total(_args):
    items = load()
    console.print(f"Total spent: [bold]{sum(i['amount'] for i in items):.2f} EUR[/bold]")


def main():
    p = argparse.ArgumentParser(description="Expense tracker")
    sub = p.add_subparsers(required=True)
    a = sub.add_parser("add", help="add an expense")
    a.add_argument("amount", type=float)
    a.add_argument("category")
    a.add_argument("--note", default="")
    a.set_defaults(func=add)
    sub.add_parser("list", help="show all expenses").set_defaults(func=show)
    sub.add_parser("total", help="show total").set_defaults(func=total)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
