"""
Intermediate Lesson 06 – Lambda, Map, Filter
"""

def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6]

    # map
    doubled = list(map(lambda x: x * 2, numbers))
    print("Doubled:", doubled)

    # filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("Evens:", evens)

    # combined
    result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    print("Squares of evens:", result)


if __name__ == "__main__":
    main()
