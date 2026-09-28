"""
Beginner Lesson 06 – Conditionals
"""

def check_number(n: int) -> str:
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def main() -> None:
    for value in [5, -3, 0]:
        print(f"{value} is {check_number(value)}")

    age = 18
    status = "adult" if age >= 18 else "minor"
    print(f"Age {age} → {status}")


if __name__ == "__main__":
    main()
