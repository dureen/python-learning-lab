"""
Advanced Lesson 09 – SQLite
"""

import sqlite3
from pathlib import Path


def main() -> None:
    db = Path("demo.db")
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    cur.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
    conn.commit()

    for row in cur.execute("SELECT id, name FROM users"):
        print(row)

    conn.close()
    # db.unlink()  # optional cleanup


if __name__ == "__main__":
    main()
