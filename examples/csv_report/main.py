"""Simple CSV report example."""

import csv
from pathlib import Path

def main() -> None:
    data = [
        {"product": "Laptop", "price": 1200, "qty": 2},
        {"product": "Mouse", "price": 25, "qty": 10},
        {"product": "Keyboard", "price": 75, "qty": 5},
    ]

    path = Path("report.csv")
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["product", "price", "qty", "total"])
        writer.writeheader()
        for row in data:
            row["total"] = row["price"] * row["qty"]
            writer.writerow(row)

    print(f"Report written to {path}")
    print(path.read_text())

if __name__ == "__main__":
    main()
