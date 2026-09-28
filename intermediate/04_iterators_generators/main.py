"""
Intermediate Lesson 04 – Iterators & Generators
"""

def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


def main() -> None:
    for i in countdown(5):
        print(i, end=" ")
    print()

    # Generator expression
    squares = (x * x for x in range(1, 6))
    print(list(squares))


if __name__ == "__main__":
    main()
