"""Simple Todo CLI example."""

from pathlib import Path
import json

TODO_FILE = Path("todos.json")

def load_todos() -> list[str]:
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text())
    return []

def save_todos(todos: list[str]) -> None:
    TODO_FILE.write_text(json.dumps(todos, indent=2))

def main() -> None:
    todos = load_todos()
    print("Current todos:")
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t}")

    # Demo: add one item
    todos.append("Learn Python")
    save_todos(todos)
    print("\nAdded 'Learn Python'")

if __name__ == "__main__":
    main()
