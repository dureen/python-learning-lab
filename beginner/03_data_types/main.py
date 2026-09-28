"""
Beginner Lesson 03 – Data Types
"""

def main() -> None:
    # int
    count = 42
    # float
    price = 19.99
    # str
    message = "Python is fun"
    # bool
    is_active = False
    # NoneType
    nothing = None

    print(type(count), count)
    print(type(price), price)
    print(type(message), message)
    print(type(is_active), is_active)
    print(type(nothing), nothing)

    # Type conversion
    print(int("10") + 5)
    print(str(3.14))


if __name__ == "__main__":
    main()
