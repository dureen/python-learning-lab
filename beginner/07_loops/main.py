"""
Beginner Lesson 07 – Loops
"""

def main() -> None:
    print("For loop:")
    for i in range(1, 6):
        print(i, end=" ")
    print()

    print("\nWhile loop:")
    n = 5
    while n > 0:
        print(n, end=" ")
        n -= 1
    print()

    print("\nLoop with break/continue:")
    for i in range(10):
        if i == 3:
            continue
        if i == 7:
            break
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
