"""
Beginner Lesson 13 – Exceptions
"""

def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    finally:
        print("Division attempt finished")


def main() -> None:
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    try:
        number = int("not a number")
    except ValueError as e:
        print(f"Caught: {e}")


if __name__ == "__main__":
    main()
