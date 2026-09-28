"""
Advanced Lesson 01 – Type Hints
"""

from typing import Optional, Union


def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()


def find_item(items: list[str], target: str) -> Optional[int]:
    try:
        return items.index(target)
    except ValueError:
        return None


def main() -> None:
    print(greet("Alice", 2))
    print(find_item(["a", "b", "c"], "b"))
    print(find_item(["a", "b", "c"], "z"))


if __name__ == "__main__":
    main()
