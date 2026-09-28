"""
Beginner Lesson 09 – Lists, Tuples, Sets
"""

def main() -> None:
    # List (mutable)
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    print("List:", fruits)

    # Tuple (immutable)
    point = (10, 20)
    print("Tuple:", point)

    # Set (unique, unordered)
    numbers = {1, 2, 2, 3, 3, 3}
    print("Set:", numbers)

    # List comprehension
    squares = [x * x for x in range(1, 6)]
    print("Squares:", squares)


if __name__ == "__main__":
    main()
