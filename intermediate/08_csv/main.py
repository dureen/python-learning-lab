"""
Intermediate Lesson 08 – CSV
"""

import csv
from pathlib import Path


def main() -> None:
    path = Path("people.csv")

    # Write
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": 25})
        writer.writerow({"name": "Bob", "age": 30})

    # Read
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
