"""
Beginner Lesson 05 – Operators
"""

def main() -> None:
    a, b = 10, 3

    print("Arithmetic:")
    print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

    print("\nComparison:")
    print(a > b, a == b, a != b)

    print("\nLogical:")
    print(True and False, True or False, not True)

    print("\nAssignment:")
    x = 5
    x += 2
    print(x)


if __name__ == "__main__":
    main()
