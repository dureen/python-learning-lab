"""
Beginner Lesson 08 – Functions
"""

def greet(name: str = "World") -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(greet())
    print(greet("Python"))
    print(add(3, 5))

    # Lambda
    square = lambda x: x * x
    print(square(4))


if __name__ == "__main__":
    main()
